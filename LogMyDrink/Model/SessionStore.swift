import CoreData
import Foundation
import Observation
import SwiftData
import BACKit

/// State for the current drinking session.
///
/// Backed by SwiftData: the stored `DrinkingSession`s are the source of truth,
/// the running one is whichever covers `now`, and the band is derived from
/// it. Settings live in `AppSettings`, because they describe the user now,
/// whereas the session records who they were then.
///
/// The band is recomputed only when an input actually changes. The clock tick
/// moves `now`, which refreshes the readout without starting a simulation.
/// Main-actor isolated: it holds a `ModelContext`, which is not `Sendable`,
/// and every caller is a view anyway.
@Observable
@MainActor
final class SessionStore {

    private let context: ModelContext
    private let engine = BACEngine()
    let settings: AppSettings

    /// The app's own person. Always exists, never deleted.
    private(set) var owner: Person

    /// Whose drinks are being recorded and shown. The owner unless someone
    /// switched, and the owner again from the next drinking day (5.6) —
    /// see `AppSettings.activePersonIDIfCurrent`.
    private(set) var person: Person

    /// The active person's occasion whose curve covers `now` — last night's,
    /// if last night is still in the blood. Nil when the body is clear and
    /// has been for the grace period. Derived, never set by a write:
    /// `rebuild` reads it from the store each time.
    private(set) var session: DrinkingSession?

    private(set) var band: BACBand = .empty

    /// The heavy half of `chartModel(for:)` per drinking day — the bands of
    /// every occasion touching the day, joined and clipped. Kept until the
    /// store next writes (`rebuild` clears it): a body evaluation asks for
    /// today's model several times a pass, and each would otherwise be a
    /// simulation per occasion.
    @ObservationIgnored
    private var dayModels: [Date: DayWindow] = [:]

    /// What one day's window contains, before the clock is applied.
    struct DayWindow {
        let band: BACBand
        let drinks: [Drink]
        let limit: Double
        let soberRange: ClosedRange<Date>?
        let carryIn: ClosedRange<Double>?
    }

    /// The window of `day` onto the active person's timeline.
    ///
    /// Every occasion whose curve touches the day is simulated with its own
    /// profile snapshot (the running one reuses `band`), the bands are joined
    /// — occasions never overlap, by `normalize` — and clipped to the day.
    /// The drinks are the ones had on the day; the limit is the last
    /// occasion's, the one a past day is judged by (5.14); the clearing time
    /// is the last occasion's too, from its unclipped curve, because a night
    /// cut at the window's edge still clears at a real hour.
    func dayWindow(for day: DrinkingDay) -> DayWindow {
        if let cached = dayModels[day.start] { return cached }

        var bands: [BACBand] = []
        var drinks: [Drink] = []
        var limit = person.limit
        for occasion in sessions(overlapping: day.range) {
            let all = occasion.sortedDrinks
            guard !all.isEmpty else { continue }
            bands.append(occasion === session ? band : engine.simulateBand(profile: occasion.profile, drinks: all))
            drinks += all.filter { day.contains($0.consumedAt) }
            limit = occasion.limit
        }

        let joined = BACBand.joined(bands)
        let atStart = joined.isEmpty ? 0...0 : joined.range(at: day.start)
        let window = DayWindow(
            band: joined.clipped(to: day.start...day.end),
            drinks: drinks.sorted { $0.consumedAt < $1.consumedAt },
            limit: limit,
            soberRange: bands.last?.soberRange(),
            carryIn: atStart.upperBound >= Occasions.clearedThreshold ? atStart : nil
        )
        dayModels[day.start] = window
        return window
    }

    /// The current time. Refreshed every half minute.
    var now: Date = .now

    /// Bumped whenever the stored data may have changed: on every save here,
    /// and on every refresh (launch, foreground, remote change, import).
    ///
    /// Not a version of anything in particular — a cache key. History derives
    /// its day aggregate from every session of the person, and a `@Query`
    /// says only "something changed", so a screen that rebuilt the aggregate
    /// on each body evaluation redid the whole walk on every scroll and tick.
    /// Keying the aggregate on this instead rebuilds it once per actual change
    /// (`HistoryAggregateCache`).
    private(set) var revision = 0

    init(context: ModelContext, settings: AppSettings) {
        self.context = context
        self.settings = settings

        // Before anything reads a session: until this has run, sessions exist
        // that belong to nobody, and every query below filters on a person.
        let owner = PersonMigration.run(in: context)
        self.owner = owner
        self.person = owner

        restoreActivePerson()
        refreshFromStore()
        observeRemoteChanges()
    }

    deinit {
        if let remoteChangeObserver {
            NotificationCenter.default.removeObserver(remoteChangeObserver)
        }
    }

    // MARK: People

    /// Owner first, then in the order they were added.
    ///
    /// Sorted in memory because `Bool` is not `Comparable` and a
    /// `SortDescriptor` cannot express "owner first"; the list is a handful of
    /// rows, so this costs nothing.
    var people: [Person] {
        let all = (try? context.fetch(FetchDescriptor<Person>())) ?? []
        return all.sorted { lhs, rhs in
            if lhs.isOwner != rhs.isOwner { return lhs.isOwner }
            return lhs.createdAt < rhs.createdAt
        }
    }

    /// Switches who is being recorded. Everything else follows: the running
    /// occasion, the curve, the profile the settings screen edits.
    func activate(_ next: Person) {
        guard next.id != person.id else { return }
        person = next

        if next.id == owner.id {
            settings.clearActivePerson()
        } else {
            settings.setActivePerson(next.id, at: now)
        }

        refreshFromStore()
    }

    /// Adds someone and switches to them: you add a person in order to record
    /// their next drink, not to admire the list.
    @discardableResult
    func addPerson(
        name: String,
        profile: BodyProfile,
        frequency: DrinkingFrequency,
        limit: Double
    ) -> Person {
        let new = Person(
            name: name,
            accent: nextAccent(),
            profile: profile,
            frequency: frequency,
            limit: limit
        )
        context.insert(new)
        save()
        activate(new)
        return new
    }

    /// What removing someone would take with them, worked out before
    /// anything is deleted so the confirmation can say it.
    struct RemovalPlan {
        let person: Person
        let sessions: Int
        let drinks: Int
        let monthlyTotals: Int
    }

    /// Nil for the owner: the app's own person is never removed, the way
    /// `Person` documents it — the store is built around there being one.
    func removalPlan(for target: Person) -> RemovalPlan? {
        guard !target.isOwner else { return nil }
        let sessions = target.sessions ?? []
        return RemovalPlan(
            person: target,
            sessions: sessions.count,
            drinks: sessions.reduce(0) { $0 + ($1.drinks?.count ?? 0) },
            monthlyTotals: monthlyTotals(of: target.id).count
        )
    }

    /// Removes a guest with everything recorded under them.
    ///
    /// Sessions and drinks go by the cascade rules on the relationships;
    /// monthly totals are keyed by id rather than related, so they are
    /// deleted here by hand. If they were the active person, the owner takes
    /// over, the same landing as every other way of losing the active person
    /// (`restoreActivePerson`). Refused for the owner: `removalPlan` says no,
    /// and this checks again rather than trusting a caller's plan.
    ///
    /// No undo. The confirmation that precedes this is the safeguard, and it
    /// is the caller's job to show one built from `removalPlan(for:)`.
    func removePerson(_ target: Person) {
        guard !target.isOwner else { return }

        // The backfill may be holding this person's sessions across an await.
        // It is not cancelled — a cancelled task only clears `backfill` when
        // it exits, and nothing would restart it until the next foreground —
        // it checks `isDeleted` before writing instead.

        if target.id == person.id {
            person = owner
            settings.clearActivePerson()
        }

        for total in monthlyTotals(of: target.id) {
            context.delete(total)
        }
        context.delete(target)
        save()
        refreshFromStore()
    }

    private func monthlyTotals(of personID: UUID) -> [MonthlyTotal] {
        let descriptor = FetchDescriptor<MonthlyTotal>(predicate: #Predicate { $0.personID == personID })
        return (try? context.fetch(descriptor)) ?? []
    }

    /// The first colour nobody is using, so two people are told apart at a
    /// glance without anyone being asked to pick a colour in a bar.
    private func nextAccent() -> PersonAccent {
        let taken = Set(people.map(\.accent))
        return PersonAccent.allCases.first { !taken.contains($0) } ?? .teal
    }

    /// Restores the choice made earlier this evening, and lets it lapse
    /// otherwise. A person deleted on another device leaves a dangling id;
    /// that falls back to the owner too.
    private func restoreActivePerson() {
        guard
            let id = settings.activePersonIDIfCurrent(at: now),
            id != owner.id,
            let stored = fetchPerson(id)
        else {
            settings.clearActivePerson()
            person = owner
            return
        }
        person = stored
    }

    private func fetchPerson(_ id: UUID) -> Person? {
        var descriptor = FetchDescriptor<Person>(predicate: #Predicate { $0.id == id })
        descriptor.fetchLimit = 1
        return try? context.fetch(descriptor).first
    }

    // MARK: Settings passthrough
    //
    // The views talk to the store; whether a value belongs to the person, the
    // device or the session is not their concern.

    var profile: BodyProfile {
        get { person.profile }
        set {
            person.apply(newValue)
            // The running occasion follows the current profile: a correction
            // made mid-evening should fix the curve you are looking at. A
            // past one never moves. The new curve clears at another time, so
            // the boundaries are re-derived.
            if let session {
                session.applySnapshot(of: newValue)
                normalize(session)
            }
            save()
            rebuild()
        }
    }

    var limit: Double {
        get { person.limit }
        set {
            person.limit = newValue
            session?.limit = newValue
            save()
            publishWidgetSnapshot()
        }
    }

    // The two display units and the limit do not move the curve, so they do
    // not `rebuild()` — but the widget formats and colours by them, and it
    // only ever learns anything through the snapshot.
    var unit: BACUnit {
        get { settings.unit }
        set {
            settings.unit = newValue
            publishWidgetSnapshot()
        }
    }

    var amountUnit: AmountUnit {
        get { settings.amountUnit }
        set {
            settings.amountUnit = newValue
            publishWidgetSnapshot()
        }
    }

    /// The quick-add favourite. Nil means there is none, and the quick-add
    /// button does not appear.
    ///
    /// No `rebuild()`: this changes nothing that has already been logged.
    var favourite: FavouriteDrink? {
        get { person.favourite }
        set {
            person.favourite = newValue
            save()
            WidgetBridge.publish(favourite: newValue)
        }
    }

    var frequency: DrinkingFrequency {
        get { person.frequency }
        set {
            person.frequency = newValue   // rewrites beta, leaves uncertainty
            if let session {
                session.applySnapshot(of: person.profile)
                normalize(session)
            }
            save()
            rebuild()
        }
    }

    // MARK: Session lifecycle
    //
    // There is no open or closed session. A session is a stretch of the
    // curve (`Occasions`), and the store's one invariant is that every stored
    // session equals exactly one such stretch — `normalize` restores it after
    // every write. "Running" is a question about a moment: whether the curve
    // covers `now` (`DrinkingSession.isRunning(at:)`), and the answer changes
    // as the clock moves without anything being written.
    //
    // This replaced a stored open/closed status. The status went wrong in
    // three ways at once on one heavy night: the engine's cap left the curve
    // without a clearing time and the policy read that as "cleared", so the
    // morning after showed a dry day with 1.3 ‰ in the blood; the day page
    // listed only closed sessions, so the night vanished from it the moment a
    // re-added drink reopened it; and the next afternoon's beer was routed
    // by drinking day into a second session that started from zero. A
    // derived boundary cannot get out of step with the curve it is derived
    // from, which is the whole argument.

    /// Reloads the active person's running occasion and settles whatever
    /// arrived unnormalized — an import, a sync, a session written by the
    /// build before boundaries were derived.
    ///
    /// Called on launch and when returning to the foreground.
    func refreshFromStore() {
        revision &+= 1
        settleUnnormalized()
        rebuild()
        reconcileTrackingStart()
        backfillStaleSummaries()
        // Launch, foreground, a person switch, an import: every path on
        // which the widget's idea of the favourite can have gone stale.
        WidgetBridge.publish(favourite: person.favourite)
    }

    /// Normalizes every session that has never been — the ones without a
    /// clearing time. Few at any moment: the build before this one left its
    /// open sessions like that, and a sync can deliver one mid-way.
    ///
    /// Only sessions that have drinks. One without may be a sync in flight,
    /// its drinks still on their way (HistoryView says the same about not
    /// sweeping them); normalizing it would delete it, and the deletion
    /// would sync back and take the drinks with it on the other device.
    /// Refetched each round rather than iterated: normalizing one can merge
    /// another pending one away, and a deleted model must not be read.
    private func settleUnnormalized() {
        let descriptor = FetchDescriptor<DrinkingSession>(
            predicate: #Predicate { $0.endedAt == nil }
        )
        func pending() -> [DrinkingSession] {
            ((try? context.fetch(descriptor)) ?? []).filter { !$0.isGone && !$0.sortedDrinks.isEmpty }
        }

        var remaining = pending()
        guard !remaining.isEmpty else { return }
        // A curve the cap cut short keeps a nil clearing time after
        // normalizing; the bound keeps that from looping.
        var rounds = remaining.count
        while let candidate = remaining.first, rounds > 0 {
            normalize(candidate)
            rounds -= 1
            remaining = pending().filter { $0 !== candidate }
        }
        save()
    }

    /// Moves the person's tracking start back to their earliest session if
    /// one predates it. `add` already does this for a drink being logged;
    /// this covers sessions that arrived some other way — the migration
    /// creating the owner with "now" while older sessions already existed,
    /// an import, a sync — and would otherwise leave "no data before" on a
    /// date the history plainly contradicts.
    private func reconcileTrackingStart() {
        let personID = person.id
        var descriptor = FetchDescriptor<DrinkingSession>(
            predicate: #Predicate { $0.personID == personID },
            sortBy: [SortDescriptor(\.startedAt, order: .forward)]
        )
        descriptor.fetchLimit = 1
        guard let earliest = try? context.fetch(descriptor).first,
              earliest.startedAt < person.trackingStartedAt
        else { return }
        person.backdateTracking(to: earliest.startedAt)
        save()
    }

    // MARK: Summary backfill

    @ObservationIgnored
    private var backfill: Task<Void, Never>?

    /// How many sessions one round of the backfill simulates before it
    /// writes them back and saves.
    ///
    /// Every save invalidates the `@Query` behind History and Live, and each
    /// of those re-derives its screen from every session. So the number of
    /// saves, not the number of simulations, is what the user feels: an
    /// imported six-year history is ~1300 sessions, which used to mean ~260
    /// saves and as many full re-aggregations. Fifty per save is about 30
    /// rounds for the same file, and a round's worth of simulation runs off
    /// the main actor anyway.
    private static let backfillBatchSize = 50

    /// Recomputes the cached summary of every session whose cache predates
    /// the current engine, a batch at a time — and, since the clearing time
    /// is derived from the same band, `endedAt` with it.
    ///
    /// After a `BACEngine.version` bump — or an import, which never carries
    /// the cache (`DataArchive`) — every session's cache is stale at once.
    /// History reads quantity straight from the drinks and treats the peak as
    /// missing until this has caught up (11.3), so a year of history opens
    /// instantly and gets its colours a moment later.
    ///
    /// The simulation itself is pure and runs on a background task: the
    /// models are read on the main actor into `Sendable` inputs (`BodyProfile`,
    /// `[Drink]`), the bands come back, and only the writes touch the context.
    /// Before this the whole loop ran on the main actor, ~370 ms per five
    /// sessions in debug (6.), and a large import stuttered for minutes.
    ///
    /// Sessions, not `SessionSummary` values, are what SwiftData observes, so
    /// each `store(_:)` invalidates exactly the rows that read it.
    ///
    /// When it is done it runs `mergeAdjacentSessions` once: sessions written
    /// by a build that grouped by drinking day may be two halves of one
    /// stretch of the curve, and only with every clearing time fresh is it
    /// safe to decide that from the cache.
    private func backfillStaleSummaries() {
        guard backfill == nil else { return }

        backfill = Task { @MainActor [weak self] in
            defer { self?.backfill = nil }
            guard let self else { return }

            // Fetched inside the task, so nothing that is not `Sendable`
            // crosses into it. Only `summary` is checked here — four scalar
            // columns. Whether a session has drinks is settled batch by
            // batch below, because reading `drinks` faults the relationship,
            // and doing that for every session up front is one long stall
            // before the first batch even starts.
            let stale = ((try? context.fetch(FetchDescriptor<DrinkingSession>())) ?? [])
                .filter { $0.summary == nil }

            let engine = self.engine
            var start = 0
            while start < stale.count {
                guard !Task.isCancelled else { return }
                let batch = Array(stale[start..<min(start + Self.backfillBatchSize, stale.count)])
                start += batch.count

                // A session with no drinks has nothing to summarize; it is
                // skipped here and stays out of History anyway.
                let work: [(target: DrinkingSession, input: BackfillInput)] = batch.compactMap {
                    let drinks = $0.sortedDrinks
                    guard !drinks.isEmpty else { return nil }
                    return ($0, BackfillInput(profile: $0.profile, drinks: drinks))
                }
                guard !work.isEmpty else { continue }

                let inputs = work.map(\.input)
                let bands = await Task.detached(priority: .utility) {
                    inputs.map { engine.simulateBand(profile: $0.profile, drinks: $0.drinks) }
                }.value

                // A session can be deleted while the batch is away — its
                // person removed, its last drink taken out — and writing to
                // a deleted model is a crash, not a no-op.
                for (item, band) in zip(work, bands) where !item.target.isDeleted {
                    let summary = SessionSummary.make(drinks: item.input.drinks, band: band)
                    item.target.store(summary)
                    item.target.endedAt = summary.soberAt
                }
                save()
                await Task.yield()
            }

            guard !Task.isCancelled, !stale.isEmpty else { return }
            if mergeAdjacentSessions() {
                save()
                rebuild()
            }
        }
    }

    /// What one simulation needs, lifted off the model so it can leave the
    /// main actor.
    private struct BackfillInput: Sendable {
        let profile: BodyProfile
        let drinks: [Drink]
    }

    /// Joins consecutive sessions of the same person whose curves run into
    /// each other, by their cached clearing times. Returns whether anything
    /// changed. Cheap — dates only, no simulation until a pair actually
    /// joins — which is why it may run over the whole store.
    @discardableResult
    private func mergeAdjacentSessions() -> Bool {
        let all = (try? context.fetch(FetchDescriptor<DrinkingSession>(
            sortBy: [SortDescriptor(\.startedAt, order: .forward)]
        ))) ?? []
        var changed = false
        var byPerson: [UUID: [DrinkingSession]] = [:]
        for candidate in all where !candidate.isDeleted {
            byPerson[candidate.personID, default: []].append(candidate)
        }
        for sessions in byPerson.values {
            guard var keeper = sessions.first(where: { !$0.sortedDrinks.isEmpty }) else { continue }
            for next in sessions.dropFirst() where next !== keeper {
                if keeper.isKnownToRun(at: next.startedAt), !next.sortedDrinks.isEmpty {
                    merge(next, into: keeper)
                    changed = true
                } else {
                    keeper = next
                }
            }
        }
        return changed
    }

    /// The active person's occasion whose curve covers `now`, if any.
    ///
    /// The newest session that has started is the only candidate: after
    /// `normalize`, no older one can still be running behind it.
    private func fetchRunningSession() -> DrinkingSession? {
        let personID = person.id
        let moment = now
        var descriptor = FetchDescriptor<DrinkingSession>(
            predicate: #Predicate { $0.personID == personID && $0.startedAt <= moment },
            sortBy: [SortDescriptor(\.startedAt, order: .reverse)]
        )
        descriptor.fetchLimit = 1
        guard let newest = try? context.fetch(descriptor).first,
              !newest.isDeleted, newest.isRunning(at: now)
        else { return nil }
        return newest
    }

    /// The session a drink at this time belongs to, if one exists — by the
    /// curve, not the calendar.
    ///
    /// The newest session started by then takes the drink if its level is
    /// still up at that moment, or cleared less than the grace period before
    /// (`Occasions.covers`). Otherwise, a session that starts within the grace
    /// period *after* the drink takes it: the drink's own curve will run into
    /// that session, and `normalize` would merge them anyway. Otherwise none,
    /// and the caller starts a new one.
    ///
    /// Scoped to the active person: two people out on the same evening have two
    /// sessions on the same night, and without the filter a backdated drink
    /// would land in whichever was found first.
    private func sessionCovering(_ date: Date) -> DrinkingSession? {
        let mine = sessionsOfActivePerson()   // newest first

        if let before = mine.first(where: { $0.startedAt <= date }), before.isKnownToRun(at: date) {
            return before
        }
        if let after = mine.last(where: { $0.startedAt > date }),
           after.startedAt.timeIntervalSince(date) < Occasions.grace {
            return after
        }
        return nil
    }

    /// Newest first.
    private func sessionsOfActivePerson() -> [DrinkingSession] {
        sessions(of: person.id)
    }

    /// Newest first, deleted ones left out.
    private func sessions(of personID: UUID) -> [DrinkingSession] {
        let descriptor = FetchDescriptor<DrinkingSession>(
            predicate: #Predicate { $0.personID == personID },
            sortBy: [SortDescriptor(\.startedAt, order: .reverse)]
        )
        return ((try? context.fetch(descriptor)) ?? []).filter { !$0.isDeleted }
    }

    /// The active person's sessions whose curves touch `window`, oldest
    /// first. What a day page draws.
    func sessions(overlapping window: Range<Date>) -> [DrinkingSession] {
        sessionsOfActivePerson()
            .filter { $0.overlaps(window) }
            .sorted { $0.startedAt < $1.startedAt }
    }

    /// The session holding a drink, by id. Nil when no session of the active
    /// person has it.
    func sessionOwning(_ drinkID: UUID) -> DrinkingSession? {
        sessionsOfActivePerson().first { candidate in
            (candidate.drinks ?? []).contains { $0.id == drinkID && !$0.isDeleted }
        }
    }

    private func startSession(at date: Date) -> DrinkingSession {
        let new = DrinkingSession(
            startedAt: date,
            person: person,
            profile: profileApplicable(at: date),
            limit: person.limit
        )
        context.insert(new)
        return new
    }

    /// Which profile a backdated session should freeze.
    ///
    /// For a drink being logged now, today's profile is right. For one being
    /// filled in from six months ago it is not: the whole reason sessions
    /// carry a snapshot is that bodies change. The nearest session in time is
    /// the closest thing we have to who you were then; the current profile is
    /// only the fallback when there is nothing to go on.
    ///
    /// Only the active person's sessions count. Falling back to somebody
    /// else's nearest evening would freeze *their* body into *your* session and
    /// draw a curve for a night that never happened.
    private func profileApplicable(at date: Date) -> BodyProfile {
        let day = DrinkingDay.containing(date)
        guard !day.isCurrent(at: now) else { return person.profile }

        let nearest = sessionsOfActivePerson().min {
            abs($0.startedAt.timeIntervalSince(date)) < abs($1.startedAt.timeIntervalSince(date))
        }
        return nearest?.profile ?? person.profile
    }

    // MARK: Normalization
    //
    // After any change to a session's drinks (or its profile, which moves the
    // curve), the stored sessions are made to equal the stretches of the
    // curve again. Three things can be needed, in this order: the session is
    // **split** where its own curve clears for longer than the grace period
    // between two drinks; its first piece is **merged** into the session
    // before it when that one's curve is still up at its start; its last
    // piece **absorbs** the sessions after it that its curve runs into. Each
    // resulting session gets its clearing time and its summary; the running
    // session is then recomputed from scratch by `rebuild`.
    //
    // The cost is one `simulateBand` for the split test plus one per
    // resulting piece — two in the ordinary case, the same order as the old
    // reconcile-and-close. Everything the user feels is `save()`, and the
    // ordinary case adds none: only a split or a merge saves on its own,
    // because SwiftData updates the inverse of a moved record at `save()`
    // and `finalize` reads the drinks through it.

    /// Restores the invariant around `target` after its drinks changed.
    /// Deletes it when it is empty.
    ///
    /// `including` is a drink just inserted whose record may not yet show in
    /// `target.drinks`: SwiftData reflects a new record on the to-many side
    /// before `save()` in practice, but nothing promises it, and on a first
    /// drink the difference is the session being deleted as empty with the
    /// drink cascading away. So `add` passes the drink, and it is counted
    /// whether or not the relationship already has it.
    private func normalize(_ target: DrinkingSession, including extra: Drink? = nil) {
        var drinks = target.sortedDrinks
        if let extra, !drinks.contains(where: { $0.id == extra.id }) {
            drinks.append(extra)
            drinks.sort { $0.consumedAt < $1.consumedAt }
        }
        guard !drinks.isEmpty else {
            context.delete(target)
            if session === target { session = nil }
            return
        }

        var pieces = split(target, drinks: drinks)

        // Backwards: the session before the first piece still had its level
        // up when the piece started → one occasion.
        if let first = pieces.first,
           let previous = sessions(of: first.personID).first(where: { $0 !== first && $0.startedAt < first.startedAt }),
           previous.isKnownToRun(at: first.startedAt) {
            merge(first, into: previous)
            pieces[0] = previous
        }

        // Forwards, over every adjacent pair: a piece absorbs the piece
        // after it, or the stored session after it, while its curve runs
        // into that one. Every pair, not only the last — a backward merge
        // raises the first piece's curve, and it may now reach the second.
        var index = 0
        while index < pieces.count {
            let current = pieces[index]
            if index + 1 < pieces.count {
                if current.isKnownToRun(at: pieces[index + 1].startedAt) {
                    merge(pieces.remove(at: index + 1), into: current)
                    continue
                }
            } else if let next = sessions(of: current.personID)
                        .last(where: { $0 !== current && $0.startedAt > current.startedAt }),
                      current.isKnownToRun(at: next.startedAt), !next.sortedDrinks.isEmpty {
                merge(next, into: current)
                continue
            }
            index += 1
        }
    }

    /// Cuts `target` where its curve clears between two drinks. Returns the
    /// resulting sessions oldest first, each finalized; the first is `target`.
    private func split(_ target: DrinkingSession, drinks: [Drink]) -> [DrinkingSession] {
        let groups = Occasions.split(drinks, profile: target.profile, engine: engine)
        guard groups.count > 1 else {
            finalize(target, drinks: drinks)
            return [target]
        }

        var pieces = [target]
        for group in groups.dropFirst() {
            let piece = DrinkingSession(
                startedAt: group[0].consumedAt,
                person: target.person,
                profile: target.profile,
                limit: target.limit
            )
            context.insert(piece)
            let ids = Set(group.map(\.id))
            for record in (target.drinks ?? []) where ids.contains(record.id) {
                record.session = piece
            }
            pieces.append(piece)
        }
        save()   // so each piece's `drinks` is its own — see the MARK above
        for (piece, group) in zip(pieces, groups) { finalize(piece, drinks: group) }
        return pieces
    }

    /// Moves every drink of `source` into `destination`, deletes `source`
    /// and finalizes the result. The destination keeps its profile snapshot:
    /// it is the one that recorded the start of the occasion.
    private func merge(_ source: DrinkingSession, into destination: DrinkingSession) {
        let moved = source.sortedDrinks
        for record in (source.drinks ?? []) where !record.isDeleted {
            record.session = destination
        }
        if session === source { session = nil }
        context.delete(source)
        save()
        let combined = (destination.sortedDrinks + moved)
            .reduce(into: [UUID: Drink]()) { $0[$1.id] = $1 }
            .values.sorted { $0.consumedAt < $1.consumedAt }
        finalize(destination, drinks: combined)
    }

    /// Recomputes what is derived from a session's drinks: its start, its
    /// clearing time, its summary. `drinks` is passed in rather than read
    /// back, because right after a move the relationship may not have caught
    /// up (see the MARK above).
    private func finalize(_ target: DrinkingSession, drinks: [Drink]) {
        guard let first = drinks.first else { return }
        target.startedAt = first.consumedAt
        let band = engine.simulateBand(profile: target.profile, drinks: drinks)
        let summary = SessionSummary.make(drinks: drinks, band: band)
        target.endedAt = summary.soberAt
        target.store(summary)
    }

    // MARK: Derived values

    var drinks: [Drink] { session?.sortedDrinks ?? [] }

    var currentRange: ClosedRange<Double> {
        drinks.isEmpty ? 0...0 : band.range(at: now)
    }

    /// The centre value, for tinting and animation where one number is needed.
    var currentBAC: Double {
        drinks.isEmpty ? 0 : band.value(at: now)
    }

    var peakRange: ClosedRange<Double>? { band.peakRange }
    var peak: BACSample? { band.peak }

    var upcomingPeak: BACSample? {
        guard let peak, peak.date > now.addingTimeInterval(60) else { return nil }
        return peak
    }

    var soberRange: ClosedRange<Date>? {
        drinks.isEmpty ? nil : band.soberRange()
    }

    var sessionStart: Date? { drinks.map(\.consumedAt).min() }

    var sessionDuration: TimeInterval {
        guard let start = sessionStart else { return 0 }
        return max(now.timeIntervalSince(start), 0)
    }

    var totalUnits: Double {
        drinks.reduce(0) { $0 + $1.standardUnits }
    }

    var limitOutcome: LimitOutcome {
        guard !drinks.isEmpty else { return .below }
        let range = currentRange
        if range.lowerBound >= limit { return .above }
        if range.upperBound >= limit { return .uncertain }
        return .below
    }

    /// Whether the curve is rising. The absorption limb is where a breathalyser
    /// would read low.
    var isRising: Bool { !drinks.isEmpty && currentRate > 0.01 }

    var currentRate: Double {
        band.center.samples.last { $0.date <= now }?.rate ?? 0
    }

    var visibleRange: ClosedRange<Date> {
        let start = (sessionStart ?? now).addingTimeInterval(-15 * 60)
        let naturalEnd = soberRange?.upperBound ?? now.addingTimeInterval(4 * 3600)
        let end = max(naturalEnd.addingTimeInterval(20 * 60), start.addingTimeInterval(6 * 3600))
        return start...end
    }

    var yMaximum: Double {
        max((peakRange?.upperBound ?? 0) * 1.3, limit * 1.4, 0.5)
    }

    // MARK: Actions

    /// Logs a drink, including one backdated to a day long past.
    ///
    /// The drink joins the occasion whose curve covers its moment — last
    /// night's, if last night is still in the blood — or starts a new one.
    /// Filling in a beer from three weeks ago never touches tonight: the
    /// curve of three weeks ago cleared three weeks ago.
    ///
    /// Logging it is also evidence about the one before it — see
    /// `Array.pourCut(by:)`.
    func add(_ drink: Drink) {
        let target = sessionCovering(drink.consumedAt) ?? startSession(at: drink.consumedAt)

        applyPourCut(of: drink, in: target)

        // A drink filled in from before this person's records start is
        // evidence that we were already keeping records then (5.7).
        person.backdateTracking(to: drink.consumedAt)

        let record = DrinkRecord(drink)
        record.session = target
        context.insert(record)

        normalize(target, including: drink)
        save()
        rebuild()
    }

    /// Shortens the drink this one interrupted, if it interrupted one.
    ///
    /// Only on `add`. Editing or deleting the interrupting drink afterwards
    /// does **not** give the earlier one its original duration back — that was
    /// a default, and the app has no record of a default it has replaced. The
    /// duration is editable on both rows, which is the way out.
    private func applyPourCut(of drink: Drink, in target: DrinkingSession) {
        lastPourCut = nil

        guard let cut = target.sortedDrinks.pourCut(by: drink),
              let record = (target.drinks ?? []).first(where: { $0.id == cut.drinkID })
        else { return }

        lastPourCut = PourCutRecord(drinkID: cut.drinkID, previousMinutes: record.drinkingMinutes)
        record.drinkingMinutes = cut.drinkingMinutes
    }

    /// The duration the last `add` overwrote, if it shortened anything.
    ///
    /// Not observed and not persisted — it survives exactly until the next
    /// `add`. The paragraph in 5.13 about the app not keeping a record of
    /// defaults it has replaced still holds for delete and for edit; this is a
    /// receipt for the call that just happened, and it exists so that the quick
    /// add's undo can be a true inverse rather than an apology. That path is
    /// there for the tap that happened in a pocket, and an undo that leaves the
    /// previous drink shortened to four minutes would leave behind exactly the
    /// false steepness 5.13 warns about.
    @ObservationIgnored
    private var lastPourCut: PourCutRecord?

    /// Corrects a drink. `target` is the session holding it; without one, the
    /// store looks it up by id — a mistake noticed three weeks later is still
    /// a mistake worth fixing, wherever the drink sits.
    ///
    /// A correction that moves the drink to another drinking day is a move
    /// between occasions rather than an edit of this one: the drink leaves,
    /// and goes wherever `add` would put it — with the profile that day would
    /// freeze (`profileApplicable`), which an in-place edit could not give it.
    /// Within the day, `normalize` splits or merges as the new time requires.
    func update(_ drink: Drink, in target: DrinkingSession? = nil) {
        // Named `holder`, not `owner`: the store has an `owner` person, and a
        // shadowed name in a method that writes to the database is the kind
        // of thing that reads fine and does the wrong thing.
        guard let holder = target ?? sessionOwning(drink.id),
              let record = (holder.drinks ?? []).first(where: { $0.id == drink.id })
        else { return }

        if !DrinkingDay.containing(record.consumedAt).contains(drink.consumedAt) {
            remove(drink, from: holder)
            add(drink)
            return
        }

        record.apply(drink)
        normalize(holder)
        save()
        rebuild()
    }

    func remove(_ drink: Drink, from target: DrinkingSession? = nil) {
        guard let holder = target ?? sessionOwning(drink.id),
              let record = (holder.drinks ?? []).first(where: { $0.id == drink.id })
        else { return }

        context.delete(record)
        // `sortedDrinks` leaves deleted records out, so `normalize` sees the
        // session as it will be after the save: SwiftData takes a deleted
        // record out of the inverse relationship only then, and a session
        // emptied by this delete used to survive as a drinkless leftover —
        // which the day page then drew as an empty chart.
        normalize(holder)
        save()
        rebuild()
    }

    // MARK: Quick add
    //
    // One tap, no sheet. Everything still goes through `add`, so session
    // routing, the pour cut (5.13) and `backdateTracking` apply unchanged: the
    // quick path is a shortcut through the interface, never through the rules.

    /// What the quick-add button is offering, or nil when it has nothing to
    /// offer and should not be shown.
    ///
    /// Three steps, in order:
    ///
    /// 1. **The favourite**, if one is set. A standing choice is the only thing
    ///    that survives an evening that goes beer, pálinka, Jäger, where
    ///    repeating the last drink would be wrong exactly when the button is
    ///    most tempting.
    /// 2. **The last drink of the running session** — mid-evening, the one you
    ///    just had.
    /// 3. **The most recent drink on record**, from whatever night that was.
    ///    Not as good as being told, but a decent guess at the usual order, and
    ///    it means the button works before anyone has configured anything.
    ///
    /// Steps 2 and 3 are a bootstrap, not a policy: the strip after such an add
    /// offers to promote it to the favourite, which is why there is no
    /// first-launch questionnaire for this.
    ///
    /// **The stomach state is the one field none of the three carries.** It
    /// comes from the previous drink of the *running session* — within an
    /// evening the best evidence available, and free — and falls back to
    /// `.light`, which is what `AddDrinkSheet` already assumes when nobody
    /// touches the control. So the button asserts nothing the sheet would not
    /// have. Deliberately not inherited from step 3: what your stomach was like
    /// last Friday says nothing about tonight.
    ///
    /// What it does mean is that the state **chains** within an evening: an
    /// `.empty` chosen at seven is still `.empty` at eleven, by which time you
    /// have eaten. The correction strip is the way out of that, rather than a
    /// second sheet nobody wanted.
    ///
    /// Timed at `now`, not `.now`. The clock moves in half-minute steps, so the
    /// offer is stable between ticks and the projection behind the button's
    /// label is computed once per tick instead of on every body evaluation —
    /// and, more importantly, the drink that gets logged is bit-for-bit the one
    /// that was projected. Half a minute of drift on a drink's timestamp is
    /// below anything the model can distinguish.
    var quickAddOffer: QuickAddOffer? {
        let stomach = drinks.last?.stomach ?? .light

        if let favourite = person.favourite {
            return QuickAddOffer(
                drink: favourite.drink(at: now, stomach: stomach),
                source: .favourite
            )
        }

        guard let recent = drinks.last ?? mostRecentRecordedDrink() else { return nil }
        return QuickAddOffer(
            drink: FavouriteDrink(recent).drink(at: now, stomach: stomach),
            source: .lastDrink
        )
    }

    /// The newest drink on record for the active person, from whatever
    /// occasion that was.
    ///
    /// A fetch, so it is reached only on the path that needs it: no favourite
    /// **and** nothing logged tonight. Once either exists the checks above
    /// short-circuit, and the one screen that can land here is an empty Live
    /// screen, which has nothing else to do.
    private func mostRecentRecordedDrink() -> Drink? {
        let personID = person.id
        var descriptor = FetchDescriptor<DrinkingSession>(
            predicate: #Predicate { $0.personID == personID },
            sortBy: [SortDescriptor(\.startedAt, order: .reverse)]
        )
        descriptor.fetchLimit = 1
        return (try? context.fetch(descriptor))?.first?.sortedDrinks.last
    }

    /// Logs whatever the button is offering.
    ///
    /// - Returns: what was logged, what it shortened and where it came from, or
    ///   nil when there was nothing to log. The caller needs all three: to
    ///   offer an undo, to let the inherited stomach state be corrected, and to
    ///   know whether to offer making this the favourite.
    @discardableResult
    func quickAdd() -> QuickAddReceipt? {
        guard let offer = quickAddOffer else { return nil }
        add(offer.drink)
        return QuickAddReceipt(
            drink: offer.drink,
            shortened: lastPourCut,
            source: offer.source
        )
    }

    /// Promotes a logged drink to the standing favourite.
    ///
    /// Only the four fields a favourite carries — the time and the stomach
    /// state stay with the drink they describe.
    func makeFavourite(_ drink: Drink) {
        favourite = FavouriteDrink(drink)
    }

    /// Takes back a quick add, including the shortening it caused.
    func undoQuickAdd(_ receipt: QuickAddReceipt) {
        remove(receipt.drink)

        // Looked up after the removal, not before: the session the drink was
        // in may have been merged away or emptied by it, and a reference to
        // a deleted model is not something to read.
        guard let cut = receipt.shortened,
              let holder = sessionOwning(cut.drinkID),
              let record = (holder.drinks ?? []).first(where: { $0.id == cut.drinkID })
        else { return }

        record.drinkingMinutes = cut.previousMinutes
        normalize(holder)
        save()
        rebuild()
    }

    /// Corrects the stomach state of a drink that was just logged.
    ///
    /// A thin wrapper over `update`, so the correction strip does not have to
    /// know how to build a modified drink.
    func correct(_ drink: Drink, stomach: StomachState) {
        var corrected = drink
        corrected.stomach = stomach
        update(corrected)
    }

    // A session is never ended by hand — there is nothing to end.
    //
    // There used to be an "End session" button. It answered a question nobody
    // asks: an occasion is over when the alcohol has cleared and a few hours
    // have passed (`Occasions`), and that is a fact about the evening, not a
    // decision. Pressing it early would have written a closing time that is
    // simply wrong, and every drink after it would have opened a second session
    // on the same night. What the button looked like it was for — "I am done
    // drinking" — the app does not need to be told, because it is still
    // simulating the alcohol already in you either way.

    /// What would happen if the user had this drink.
    ///
    /// When correcting a logged drink, pass its id as `excluding` so the
    /// comparison is "the session without it" against "with the corrected
    /// version", rather than counting it twice.
    /// `in` selects which session the comparison is made against. A past
    /// session is evaluated with **its own** profile snapshot and limit, not
    /// today's — otherwise the projection would describe a night that never
    /// happened.
    ///
    /// Without `in`, the comparison is made against the session `add` would
    /// route the drink to — the one covering its drinking day, not the one
    /// that happens to be open. A beer filled in for last Friday is previewed
    /// on top of last Friday's drinks and with the profile that evening would
    /// freeze; previewing it on top of tonight's would show a curve the Add
    /// button then does not produce.
    ///
    /// The answer to the last question asked is kept, because a projection is
    /// six simulations and a SwiftUI body reads it several times per pass. See
    /// `ProjectionKey`.
    func project(
        _ candidate: Drink,
        excluding excludedID: UUID? = nil,
        in target: DrinkingSession? = nil
    ) -> BandedProjection {
        let setting = target.map { ProjectionSetting(holder: $0) }
            ?? projectionSetting(for: candidate.consumedAt)
        let all = setting.consumed
        // The same cut `add` will make, so the curve previewed above the Add
        // button is the curve you get after pressing it.
        let others = (excludedID.map { id in all.filter { $0.id != id } } ?? all)
            .shorteningPour(for: candidate)

        let key = ProjectionKey(
            profile: setting.profile,
            consumed: others,
            candidate: candidate,
            limit: setting.limit
        )
        if let lastProjection, lastProjection.key == key { return lastProjection.value }

        let result = engine.projectBand(
            profile: key.profile,
            consumed: key.consumed,
            candidate: key.candidate,
            limit: key.limit
        )
        lastProjection = (key, result)
        return result
    }

    /// Everything a projection depends on.
    ///
    /// Comparing eight drinks costs nothing against six RK4 runs, and it is the
    /// honest test: if all of it is equal, the answer cannot have changed.
    /// The consumed list already has the pour cut applied, so an edit that only
    /// shortens an earlier drink still registers here.
    private struct ProjectionKey: Equatable {
        let profile: BodyProfile
        let consumed: [Drink]
        let candidate: Drink
        let limit: Double
    }

    /// Not observed. A read of `project` happens *during* a body evaluation,
    /// and writing to an observed property there would invalidate the very view
    /// that asked.
    @ObservationIgnored
    private var lastProjection: (key: ProjectionKey, value: BandedProjection)?

    /// What a candidate is projected on top of: the drinks already there, and
    /// the profile and limit they are judged with.
    private struct ProjectionSetting {
        let consumed: [Drink]
        let profile: BodyProfile
        let limit: Double

        init(holder: DrinkingSession) {
            consumed = holder.sortedDrinks
            profile = holder.profile
            limit = holder.limit
        }

        init(consumed: [Drink], profile: BodyProfile, limit: Double) {
            self.consumed = consumed
            self.profile = profile
            self.limit = limit
        }
    }

    /// The setting `add` would put a drink at this time into — the occasion
    /// whose curve covers it, or, when there is none, an empty evening with
    /// the profile `startSession` would freeze for it.
    ///
    /// Routing means a fetch, and a sheet's body asks for the projection nine
    /// times per pass while a slider is dragged. The answer for one moment is
    /// kept until the store next writes; `rebuild` clears it. Keyed on the
    /// exact moment, not the day: two times on one day can belong to
    /// different occasions, or one to last night's and one to none.
    private func projectionSetting(for date: Date) -> ProjectionSetting {
        if let routing = lastRouting, routing.date == date { return routing.setting }

        let setting: ProjectionSetting
        if let holder = sessionCovering(date) {
            setting = ProjectionSetting(holder: holder)
        } else {
            setting = ProjectionSetting(
                consumed: [],
                profile: profileApplicable(at: date),
                limit: person.limit
            )
        }
        lastRouting = (date, setting)
        return setting
    }

    @ObservationIgnored
    private var lastRouting: (date: Date, setting: ProjectionSetting)?

    /// Moves the clock. Nothing is written: whether the running occasion is
    /// still running is re-read from the curve, and the band is rebuilt only
    /// when the answer changed — the moment last night finally clears.
    func tick(to date: Date = .now) {
        now = date
        if fetchRunningSession() !== session { rebuild() }
    }

    // MARK: Export and import
    //
    // Through the store like everything else (3.): the views do not touch
    // SwiftData, and an import in particular has to leave this object's own
    // state consistent, which only this object knows how to do.

    /// Everyone and every occasion, ready to be written to a file.
    func archive(at date: Date = .now) -> DataArchive {
        ArchiveExport.archive(from: context, at: date)
    }

    /// What importing this archive would change, without changing anything.
    func importPlan(for archive: DataArchive) -> ArchiveImport.Plan {
        ArchiveImport.plan(archive, in: context)
    }

    /// Merges an archive in, then puts this store back on its feet.
    ///
    /// The owner is reassigned rather than assumed unchanged: the import
    /// resolves two owners into one, and the loser is deleted. Holding the
    /// deleted one would leave every query filtering on a person who is no
    /// longer there — an app that looks empty while the data sits in the
    /// database. `restoreActivePerson` then runs for the same reason it runs at
    /// launch: the remembered person may have arrived, or may never have
    /// existed here.
    @discardableResult
    func importArchive(_ plan: ArchiveImport.Plan) -> ArchiveImport.Outcome {
        let outcome = ArchiveImport.apply(plan, in: context)

        owner = outcome.owner
        person = outcome.owner
        restoreActivePerson()
        refreshFromStore()

        return outcome
    }

    // MARK: Changes made on another device
    //
    // CloudKit writes straight into the store, behind our back. `@Query` picks
    // that up on its own, but this store does not: `session` and `band` only
    // move when `rebuild` runs. Without this, a drink logged on the phone would
    // appear in the list on the iPad with the curve underneath it unchanged —
    // the two halves of the same screen disagreeing.
    //
    // The scene-phase hook in `MainTabView` covers the app coming back to the
    // foreground. This covers the app already being there.

    /// Not observed, and not part of the store's value: a token and a timer.
    ///
    /// `nonisolated(unsafe)` because `deinit` is not main-actor isolated and
    /// has to read it. Written once in `init` and read once in `deinit`, both
    /// while nothing else holds the object, so there is nothing to race with.
    @ObservationIgnored
    nonisolated(unsafe) private var remoteChangeObserver: (any NSObjectProtocol)?

    @ObservationIgnored
    private var pendingRemoteRefresh: Task<Void, Never>?

    private func observeRemoteChanges() {
        remoteChangeObserver = NotificationCenter.default.addObserver(
            forName: .NSPersistentStoreRemoteChange,
            object: nil,
            queue: nil          // posted off the main thread; we hop ourselves
        ) { [weak self] _ in
            Task { @MainActor [weak self] in
                self?.scheduleRemoteRefresh()
            }
        }
    }

    /// Collapses a burst of notifications into one refresh.
    ///
    /// A sync posts one notification per batch, and a first sync posts many.
    /// Each `refreshFromStore` normalizes whatever arrived without a clearing
    /// time and then rebuilds the band — a `simulateBand` or two in the
    /// ordinary case, which is ~5 ms release but ~146 ms debug (6.). Answering
    /// every notification would spend that repeatedly for one visible result.
    ///
    /// Half a second: longer than the gap between batches of one sync, short
    /// enough that a drink logged on the other device still lands while you are
    /// looking at the screen.
    private func scheduleRemoteRefresh() {
        pendingRemoteRefresh?.cancel()
        pendingRemoteRefresh = Task { @MainActor [weak self] in
            try? await Task.sleep(for: .milliseconds(500))
            guard !Task.isCancelled else { return }
            self?.refreshFromStore()
        }
    }

    // MARK: Plumbing

    private func rebuild() {
        // Every write ends here, and a write can move a drink between
        // occasions.
        lastRouting = nil
        dayModels.removeAll()

        session = fetchRunningSession()
        let drinks = session?.sortedDrinks ?? []
        if let session, !drinks.isEmpty {
            band = engine.simulateBand(profile: session.profile, drinks: drinks)
        } else {
            band = .empty
        }
        publishWidgetSnapshot()
    }

    /// The widget sees the world through this and nothing else (5.15).
    private func publishWidgetSnapshot() {
        WidgetBridge.publish(snapshot: WidgetSnapshot.make(
            band: band,
            drinks: drinks,
            limit: person.limit,
            unit: settings.unit,
            amountUnit: settings.amountUnit
        ))
    }

    private func save() {
        revision &+= 1
        do {
            try context.save()
        } catch {
            // Losing a drink silently is worse than a log line nobody reads.
            assertionFailure("Failed to save: \(error)")
        }
    }
}
