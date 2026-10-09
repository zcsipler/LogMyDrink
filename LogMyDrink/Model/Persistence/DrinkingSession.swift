import Foundation
import SwiftData
import BACKit

/// One drinking occasion, from the first drink until the level has cleared.
///
/// A session is **not** a calendar day, and not a drinking day either: it is
/// a stretch of the curve. An evening that runs past midnight is one session,
/// and so is a heavy night plus the beer had the next afternoon while 0.2 ‰
/// of it was still there. The boundaries are derived — `Occasions.split`
/// decides them from the drinks and the profile, and `SessionStore.normalize`
/// keeps every stored session equal to exactly one such stretch. There is no
/// "open" or "closed" state to get out of step with the curve: `endedAt` is
/// the clearing time the curve gives, recomputed whenever the drinks change.
///
/// Days are windows onto this timeline. A day page shows the part of every
/// session that falls inside its five-to-five window; the history books each
/// drink to the day it was had and each day's peak to the drinks had on it.
///
/// ## Why the profile is stored here
///
/// The curve is a pure function of (drinks, profile). If we kept only the
/// drinks and always recomputed with the *current* profile, every past session
/// would be redrawn whenever the user's weight changed — the same three drinks
/// peak at 0.578 g/L at 60 kg and 0.507 g/L at 70 kg, a 14 % difference. A
/// record that rewrites itself is not a record.
///
/// So each session carries the profile that was in effect. A past session is
/// frozen; the running one tracks the current profile while its curve covers
/// now, because a correction made mid-evening should fix the curve you are
/// looking at.
///
/// The engine is deliberately *not* frozen: the inputs are stored, so a later
/// improvement to the model can recompute old sessions correctly.
///
/// ## CloudKit constraints
///
/// Every property has a default value or is optional, there are no unique
/// attributes, and the relationship is optional with an inverse. CloudKit
/// requires all of this, and retrofitting it later means a migration.
@Model
final class DrinkingSession {
    var id: UUID = UUID()
    var startedAt: Date = Date.now

    /// When the slow branch of the curve clears, as last computed. Nil only
    /// for a session nobody has normalized yet, or one the engine's cap cut
    /// short — never a status. Whether the occasion is still running at some
    /// moment is a question for `Occasions.covers(soberAt:date:)`.
    var endedAt: Date?

    // MARK: Profile snapshot
    //
    // Flattened rather than a Codable blob: CloudKit is happiest with scalars,
    // the values are readable in the debugger, and a diff shows what changed.

    var sexRaw: String = Sex.male.rawValue
    var age: Double = 35
    var heightCm: Double = 180
    var weightKg: Double = 80
    var beta: Double = Physiology.defaultBeta
    var betaUncertainty: Double = Physiology.legacyBetaUncertainty

    /// The personal limit as it stood for this session.
    var limit: Double = 0.8

    // MARK: Whose session this is
    //
    // Both, deliberately. The relationship is the truth and carries the
    // cascade; the flat id is what `@Query` can filter on — a predicate that
    // has to walk an optional relationship is the kind that stops compiling
    // for reasons nobody can explain. They are written together, in `assign`.

    var person: Person?
    var personID: UUID = Person.unassignedID

    func assign(to person: Person) {
        self.person = person
        self.personID = person.id
    }

    // MARK: Drinks

    @Relationship(deleteRule: .cascade, inverse: \DrinkRecord.session)
    var drinks: [DrinkRecord]? = []

    // MARK: Cached summary
    //
    // Never the truth — always recomputable from the drinks and the snapshot.
    // Stored only so that listing a year of history does not run hundreds of
    // simulations while the user scrolls.

    var cachedPeakLow: Double?
    var cachedPeakHigh: Double?
    var cachedSoberAt: Date?
    var cachedTotalUnits: Double?
    var cachedEngineVersion: Int?

    /// The per-day figures (`DaySummary`), JSON-encoded. A blob rather than a
    /// second entity: one session touches one or two days, the data is a few
    /// numbers, and an optional `Data` column is the one shape of this that
    /// CloudKit takes without a migration.
    var cachedDaysData: Data?

    init(
        id: UUID = UUID(),
        startedAt: Date = .now,
        endedAt: Date? = nil,
        person: Person? = nil,
        profile: BodyProfile,
        limit: Double
    ) {
        self.id = id
        self.startedAt = startedAt
        self.endedAt = endedAt
        self.limit = limit
        self.drinks = []
        self.person = person
        self.personID = person?.id ?? Person.unassignedID
        applySnapshot(of: profile)
    }

    // MARK: Profile access

    /// The profile this session was recorded with.
    var profile: BodyProfile {
        BodyProfile(
            sex: Sex(rawValue: sexRaw) ?? .male,
            age: age,
            heightCm: heightCm,
            weightKg: weightKg,
            beta: beta,
            betaUncertainty: betaUncertainty
        )
    }

    /// Overwrites the snapshot. Only legitimate while the occasion is still
    /// running, or as an explicit correction of a past session by the user.
    func applySnapshot(of profile: BodyProfile) {
        sexRaw = profile.sex.rawValue
        age = profile.age
        heightCm = profile.heightCm
        weightKg = profile.weightKg
        beta = profile.beta
        betaUncertainty = profile.betaUncertainty
        invalidateSummary()
    }

    // MARK: Derived

    /// Whether the occasion is still running at `date`: the level has not
    /// cleared, or cleared less than the grace period ago. Not a stored
    /// state — the same `endedAt` answers differently as time passes.
    func isRunning(at date: Date) -> Bool {
        startedAt <= date && Occasions.covers(soberAt: endedAt, date: date)
    }

    /// `isRunning`, but a session with no clearing time yet does **not**
    /// count. For every decision that joins sessions or routes a drink: an
    /// unnormalized session read as "running forever" would swallow weeks
    /// of later evenings. `isRunning` keeps the lenient reading for the one
    /// question where it is right — is this curve still up now — because a
    /// curve the engine's cap cut short really is.
    func isKnownToRun(at date: Date) -> Bool {
        endedAt != nil && isRunning(at: date)
    }

    /// Whether any part of the curve falls inside `window`. Without a
    /// clearing time only the start is known, and only it is tested.
    func overlaps(_ window: Range<Date>) -> Bool {
        guard startedAt < window.upperBound else { return false }
        guard let endedAt else { return window.contains(startedAt) }
        return endedAt > window.lowerBound
    }

    /// Deleted, or deleted and saved — a model a view may still be holding
    /// but must not read. `isDeleted` alone goes stale after the save.
    var isGone: Bool { isDeleted || modelContext == nil }

    /// Deleted records left out: SwiftData takes them off the inverse only
    /// at `save()`, and the store normalizes before it saves.
    var sortedDrinks: [Drink] {
        (drinks ?? [])
            .filter { !$0.isDeleted }
            .map(\.asDrink)
            .sorted { $0.consumedAt < $1.consumedAt }
    }

    var lastDrinkAt: Date? {
        (drinks ?? []).map(\.consumedAt).max()
    }

    var totalUnits: Double {
        sortedDrinks.reduce(0) { $0 + $1.standardUnits }
    }

    // MARK: Summary cache

    /// The stored summary, or nil when it is missing or was produced by an
    /// older version of the engine.
    var summary: SessionSummary? {
        guard
            cachedEngineVersion == BACEngine.version,
            let low = cachedPeakLow,
            let high = cachedPeakHigh,
            let units = cachedTotalUnits
        else { return nil }

        let days = cachedDaysData.flatMap { try? JSONDecoder().decode([DaySummary].self, from: $0) } ?? []
        return SessionSummary(
            peakRange: min(low, high)...max(low, high),
            soberAt: cachedSoberAt,
            totalUnits: units,
            drinkCount: drinks?.count ?? 0,
            days: days
        )
    }

    func store(_ summary: SessionSummary) {
        cachedPeakLow = summary.peakRange.lowerBound
        cachedPeakHigh = summary.peakRange.upperBound
        cachedSoberAt = summary.soberAt
        cachedTotalUnits = summary.totalUnits
        cachedDaysData = try? JSONEncoder().encode(summary.days)
        cachedEngineVersion = BACEngine.version
    }

    func invalidateSummary() {
        cachedEngineVersion = nil
    }
}

/// The few numbers a history list needs, without redrawing the curve.
struct SessionSummary: Hashable, Sendable {
    let peakRange: ClosedRange<Double>
    let soberAt: Date?
    let totalUnits: Double
    let drinkCount: Int
    /// One entry per drinking day the curve touches, oldest first.
    let days: [DaySummary]
}

extension SessionSummary {
    /// The summary of a computed band — the one place the per-day split is
    /// worked out, for the store's cache and for a row drawing itself while
    /// the cache is stale.
    static func make(drinks: [Drink], band: BACBand, calendar: Calendar = .current) -> SessionSummary {
        let ordered = drinks.sorted { $0.consumedAt < $1.consumedAt }
        return SessionSummary(
            peakRange: band.peakRange ?? 0...0,
            soberAt: band.soberRange()?.upperBound,
            totalUnits: ordered.reduce(0) { $0 + $1.standardUnits },
            drinkCount: ordered.count,
            days: daySummaries(of: ordered, band: band, calendar: calendar)
        )
    }

    /// Every drinking day from the first drink to the clearing, in order.
    ///
    /// A day's peak is taken from its first drink up to the next day's first
    /// drink — the stretch the day's own drinks are responsible for — so a
    /// peak that falls just past five in the morning still belongs to the
    /// evening that produced it, and the morning after is not a second peak.
    private static func daySummaries(of drinks: [Drink], band: BACBand, calendar: Calendar) -> [DaySummary] {
        guard let first = drinks.first, let end = band.end else { return [] }
        let lastDay = DrinkingDay.containing(end, calendar: calendar)
        var day = DrinkingDay.containing(first.consumedAt, calendar: calendar)

        var firstDrinkByDay: [DrinkingDay: Date] = [:]
        var unitsByDay: [DrinkingDay: Double] = [:]
        var countByDay: [DrinkingDay: Int] = [:]
        for drink in drinks {
            let key = DrinkingDay.containing(drink.consumedAt, calendar: calendar)
            firstDrinkByDay[key] = min(firstDrinkByDay[key] ?? drink.consumedAt, drink.consumedAt)
            unitsByDay[key, default: 0] += drink.standardUnits
            countByDay[key, default: 0] += 1
        }
        let drinkDays = firstDrinkByDay.keys.sorted { $0.start < $1.start }

        var result: [DaySummary] = []
        while day.start <= lastDay.start {
            var peak: ClosedRange<Double>?
            if let from = firstDrinkByDay[day] {
                let next = drinkDays.first { $0.start > day.start }.flatMap { firstDrinkByDay[$0] }
                let until = next ?? end
                peak = band.clipped(to: from...max(until, from)).peakRange
            }
            let carry = day.start > first.consumedAt ? band.range(at: day.start) : 0...0
            result.append(DaySummary(
                dayStart: day.start,
                drinkCount: countByDay[day] ?? 0,
                totalUnits: unitsByDay[day] ?? 0,
                peakLow: peak?.lowerBound,
                peakHigh: peak?.upperBound,
                carryLow: carry.lowerBound,
                carryHigh: carry.upperBound
            ))
            day = day.offset(by: 1, calendar: calendar)
        }
        return result
    }
}

/// What one drinking day of a session looks like from the history (5.16).
///
/// The peak is of the drinks had **on this day**: the maximum of the curve
/// from the day's first drink until the next day's first (or the end). The
/// level carried in at the five o'clock boundary is reported separately, so
/// a night out is one bar in the week view, on the day it happened, and the
/// morning after says "started at 1.3 ‰" instead of claiming a second peak.
struct DaySummary: Codable, Hashable, Sendable {
    /// `DrinkingDay.start` of the day.
    let dayStart: Date
    let drinkCount: Int
    let totalUnits: Double
    /// Nil on a day the curve only ran through, with nothing drunk on it.
    let peakLow: Double?
    let peakHigh: Double?
    /// The band at the start of the day; zero on the day the session began.
    let carryLow: Double
    let carryHigh: Double

    var peakRange: ClosedRange<Double>? {
        guard let peakLow, let peakHigh else { return nil }
        return min(peakLow, peakHigh)...max(peakLow, peakHigh)
    }

    /// Nil when nothing was carried in.
    var carryIn: ClosedRange<Double>? {
        guard carryHigh >= Occasions.clearedThreshold else { return nil }
        return min(carryLow, carryHigh)...max(carryLow, carryHigh)
    }
}
