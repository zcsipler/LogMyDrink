import Foundation

/// The made-up drinker debug builds carry, so every screen has years of
/// history to show without anyone's real evenings being involved.
///
/// ## Why a bundled file and not part of the owner's export
///
/// The demo used to live in the same archive as the developer's own data,
/// which meant every export and every restore carried a stranger along. Now
/// it has its own source — `DemoData/demo-person.json`, committed to the repo
/// and edited like any other fixture — and the store never writes it back out
/// (`ArchiveExport` skips this id).
///
/// ## Why the dates move
///
/// A fixture with fixed dates goes stale: a month later the Live tab, the
/// week chart and the free history window all show an empty demo. So on load
/// every date is moved forward by **whole weeks**, as many as it takes for the
/// last evening to land within the past seven drinking days. Whole weeks keep
/// the weekdays — Friday nights stay on Fridays, which is most of what makes
/// the history look like a person's — and adding calendar days rather than
/// seconds keeps the clock times across a daylight-saving change.
///
/// The id is the one the demo always had, so the first load on a device that
/// still holds the old copy replaces it rather than adding a second demo.
enum DemoPerson {

    /// Known in every build, because the export filters on it — a release
    /// build signed into the same iCloud must not write the demo out either.
    static let id = UUID(uuidString: "5D9BFB7E-DF32-4B3A-A599-6A76A4A6891B")!

    #if DEBUG
    static let resourceName = "demo-person"

    /// The bundled fixture, trimmed to the demo person. Nil when the file is
    /// missing or unreadable — a debug convenience is not worth a crash.
    static func bundledArchive(in bundle: Bundle = .main) -> DataArchive? {
        guard
            let url = bundle.url(forResource: resourceName, withExtension: "json"),
            let data = try? Data(contentsOf: url),
            let archive = try? DataArchive.decoded(from: data)
        else { return nil }
        return demoOnly(archive)
    }

    /// Only the demo's rows. A file edited by hand could pick up someone
    /// else, and loading it must never touch anyone but the demo.
    static func demoOnly(_ archive: DataArchive) -> DataArchive {
        var trimmed = archive
        trimmed.people = archive.people.filter { $0.id == id }
        trimmed.sessions = archive.sessions.filter { $0.personID == id }
        trimmed.monthlyTotals = (archive.monthlyTotals ?? []).filter { $0.personID == id }
        return trimmed
    }

    /// Whole weeks to move the fixture so that its last drinking day falls
    /// between seven days ago and yesterday.
    ///
    /// Yesterday rather than today: today is where the developer tests the
    /// Live tab, and a demo evening already sitting there would get in the
    /// way. Never into the future either — a drink after `now` would be one
    /// the app itself refuses to log.
    static func weeksToShift(
        lastDrinkAt last: Date,
        now: Date,
        calendar: Calendar = .current
    ) -> Int {
        let lastDay = DrinkingDay.containing(last, calendar: calendar)
        let yesterday = DrinkingDay.containing(now, calendar: calendar).offset(by: -1, calendar: calendar)
        let days = calendar.dateComponents([.day], from: lastDay.start, to: yesterday.start).day ?? 0
        return Int((Double(days) / 7).rounded(.down))
    }

    /// Every date in the archive, `weeks` weeks later.
    ///
    /// Monthly totals are left alone: a month does not move by a week, and the
    /// demo has none.
    static func shifted(
        _ archive: DataArchive,
        byWeeks weeks: Int,
        calendar: Calendar = .current
    ) -> DataArchive {
        guard weeks != 0 else { return archive }
        func move(_ date: Date) -> Date {
            calendar.date(byAdding: .day, value: 7 * weeks, to: date) ?? date
        }

        var moved = archive
        moved.people = archive.people.map { person in
            var person = person
            person.createdAt = move(person.createdAt)
            person.trackingStartedAt = move(person.trackingStartedAt)
            return person
        }
        moved.sessions = archive.sessions.map { session in
            var session = session
            session.startedAt = move(session.startedAt)
            session.endedAt = session.endedAt.map(move)
            session.drinks = session.drinks.map { drink in
                var drink = drink
                drink.consumedAt = move(drink.consumedAt)
                return drink
            }
            return session
        }
        return moved
    }

    /// What has to match for the loaded copy to still be current: the shift,
    /// and the file itself — an edited fixture is reloaded the next launch
    /// even inside the same week.
    static func fingerprint(of source: DataArchive, weeks: Int) -> String {
        "\(weeks)|\(source.exportedAt.timeIntervalSince1970)|\(source.sessions.count)|\(source.drinkCount)"
    }
    #endif
}

#if DEBUG
/// Keeps the demo person loaded and recent, in debug builds only.
///
/// Runs at launch. Most launches it compares a fingerprint and returns; when
/// the week has turned or the fixture changed, it removes the demo and loads
/// it again, moved to the new week. Removal goes through the same
/// `removePerson` the People screen uses and the load through the same
/// import the backup uses, so the store ends up exactly as consistent as
/// after either of those.
///
/// What that costs: the demo's own test edits do not survive a reload, and
/// every reload deletes and re-creates ~1250 sessions in the CloudKit
/// development environment — weekly, not daily, because of the whole-week
/// shift. A demo removed on purpose comes back on the next launch.
@MainActor
enum DemoSeed {

    private static let fingerprintKey = "logmydrink.debug.demoFingerprint"

    static func refreshIfNeeded(
        _ store: SessionStore,
        defaults: UserDefaults = .standard,
        now: Date = .now
    ) {
        // The test target launches the app as its host. Seeding there would
        // load four thousand drinks into the simulator's real store before
        // every test run, for nothing — the tests use their own in-memory one.
        guard ProcessInfo.processInfo.environment["XCTestConfigurationFilePath"] == nil else { return }

        guard
            let source = DemoPerson.bundledArchive(),
            let last = source.sessions.flatMap(\.drinks).map(\.consumedAt).max()
        else { return }

        let weeks = DemoPerson.weeksToShift(lastDrinkAt: last, now: now)
        let fingerprint = DemoPerson.fingerprint(of: source, weeks: weeks)
        let existing = store.people.first { $0.id == DemoPerson.id }

        if existing != nil, defaults.string(forKey: fingerprintKey) == fingerprint { return }

        let wasActive = store.person.id == DemoPerson.id
        if let existing { store.removePerson(existing) }

        let moved = DemoPerson.shifted(source, byWeeks: weeks)
        store.importArchive(store.importPlan(for: moved))
        defaults.set(fingerprint, forKey: fingerprintKey)

        if wasActive, let demo = store.people.first(where: { $0.id == DemoPerson.id }) {
            store.activate(demo)
        }
    }
}
#endif
