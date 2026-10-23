import Foundation
import Testing
import BACKit
@testable import LogMyDrink

/// The second stats card (5.24): energy, sessions, time under the
/// influence, days over the limit, the longest sober run, the usual drink.
///
/// The figures are sums over days, so most tests build the days by hand. The
/// one that cannot — how a session's time is sliced across the days it
/// touches — goes through the store, because that slice is cut from the
/// cached clearing time and nowhere else.
@Suite("History figures")
struct HistoryFiguresTests {

    static let calendar = HistoryAggregateTests.calendar
    var calendar: Calendar { Self.calendar }

    func date(_ y: Int, _ m: Int, _ d: Int, _ h: Int = 12, _ min: Int = 0) -> Date {
        calendar.date(from: DateComponents(year: y, month: m, day: d, hour: h, minute: min))!
    }

    func occasion(
        session: UUID = UUID(),
        at start: Date,
        units: Double = 2,
        drinks: Int = 2,
        peak: ClosedRange<Double>? = 0.4...0.4,
        limit: Double = 0.8,
        kcal: Double = 0,
        servings: [HistoryServing: Int] = [:],
        influence: DateInterval? = nil
    ) -> HistoryOccasion {
        HistoryOccasion(
            id: "\(session.uuidString)/\(start.timeIntervalSinceReferenceDate)",
            sessionID: session, startedAt: start, totalUnits: units, drinkCount: drinks,
            peakRange: peak, carryIn: nil, limit: limit,
            kilocalories: kcal, servings: servings, influence: influence
        )
    }

    func days(_ occasions: [HistoryOccasion], from start: Date, now: Date) -> [DayBucket] {
        HistoryAggregate.days(from: occasions, trackingStartedAt: start, now: now, calendar: calendar)
    }

    // MARK: Calories

    @Test("Beer, wine and sparkling add their typical energy; the rest count their alcohol only")
    func caloriesByKind() {
        func drink(_ template: String, _ ml: Double, _ abv: Double) -> Drink {
            Drink(consumedAt: .now, volumeMl: ml, abvPercent: abv, stomach: .light, name: template)
        }
        // 500 ml at 5 %: 19.725 g ethanol → 138.1 kcal, plus 75 kcal.
        #expect(abs(DrinkCatalog.kilocalories(for: drink("beer", 500, 5)) - 213.075) < 0.001)
        // 150 ml at 12 %: 14.202 g → 99.4 kcal, plus 15.
        #expect(abs(DrinkCatalog.kilocalories(for: drink("wine", 150, 12)) - 114.414) < 0.001)
        // A cocktail and a spirit: alcohol alone.
        #expect(abs(DrinkCatalog.kilocalories(for: drink("cocktail", 200, 15)) - 165.69) < 0.001)
        #expect(abs(DrinkCatalog.kilocalories(for: drink("spirit", 40, 40)) - 88.368) < 0.001)
    }

    @Test("A month known only by total adds its alcohol's energy")
    func monthlyTotalCalories() {
        // All of September before records began, known as 300 g.
        let known = KnownMonth(year: 2026, month: 9, gramsEthanol: 300)
        let now = date(2026, 10, 3)
        let all = HistoryAggregate.days(
            from: [], knownMonths: [known], trackingStartedAt: date(2026, 10, 1),
            now: now, calendar: calendar
        )
        let september = all.filter { calendar.component(.month, from: $0.day.calendarDate) == 9 }
        let figures = HistoryFigures(days: september, now: now)
        #expect(abs(figures.kilocalories - 2100) < 0.001)
    }

    // MARK: Sessions

    @Test("A session over two days is one session, and the average is per session")
    func sessionsCountOnce() {
        let night = UUID()
        let now = date(2026, 9, 20)
        let all = days([
            occasion(session: night, at: date(2026, 9, 12, 21), units: 6),
            occasion(session: night, at: date(2026, 9, 13, 14), units: 2),
            occasion(at: date(2026, 9, 15, 20), units: 4),
        ], from: date(2026, 9, 10), now: now)
        let figures = HistoryFigures(days: all, now: now)
        #expect(figures.sessions == 2)
        #expect(figures.unitsPerSession == 6)
    }

    @Test("No sessions, no average")
    func noSessions() {
        let now = date(2026, 9, 20)
        let figures = HistoryFigures(days: days([], from: date(2026, 9, 10), now: now), now: now)
        #expect(figures.sessions == 0)
        #expect(figures.unitsPerSession == nil)
        #expect(figures.favourite == nil)
    }

    // MARK: Time under the influence

    @Test("Influence sums the slices and is a share of the recorded time lived so far")
    func influenceShare() {
        // Records from the 10th; today is the 12th, at 17:00. Twelve hours
        // on the 10th, six on the 12th of which five are past.
        let now = date(2026, 9, 12, 17)
        let first = DateInterval(start: date(2026, 9, 10, 20), duration: 12 * 3600)
        let today = DateInterval(start: date(2026, 9, 12, 12), duration: 6 * 3600)
        let all = days([
            occasion(at: first.start, influence: first),
            occasion(at: today.start, influence: today),
        ], from: date(2026, 9, 10), now: now)

        let figures = HistoryFigures(days: all, now: now)
        #expect(figures.influence == 17 * 3600)
        // Two whole drinking days (05:00 to 05:00) and today from 05:00 to 17:00.
        #expect(figures.recordedTime == (24 + 24 + 12) * 3600)
        #expect(figures.influenceIsComplete)
    }

    @Test("Days before records are not in the share")
    func influenceIgnoresUnknown() {
        let now = date(2026, 9, 12, 17)
        let window = HistoryWindow.make(
            range: .week, offset: 0,
            days: days([], from: date(2026, 9, 12), now: now),
            now: now, calendar: calendar
        )
        #expect(window.figures.recordedTime == 12 * 3600)
    }

    @Test("A drinking day without a clearing time makes the figure incomplete")
    func influenceIncomplete() {
        let now = date(2026, 9, 20)
        let all = days([occasion(at: date(2026, 9, 12, 21), influence: nil)], from: date(2026, 9, 10), now: now)
        #expect(!HistoryFigures(days: all, now: now).influenceIsComplete)
    }

    // MARK: Control

    @Test("Days over the limit go by the day's own limit; the sober run by dry days in a row")
    func overLimitAndSoberRun() {
        let now = date(2026, 9, 20)
        let all = days([
            occasion(at: date(2026, 9, 11, 21), peak: 0.9...0.9, limit: 0.8),   // over
            occasion(at: date(2026, 9, 12, 21), peak: 0.9...0.9, limit: 1.0),   // under its own limit
            occasion(at: date(2026, 9, 16, 21), peak: 0.5...0.5, limit: 0.5),   // exactly at: counts
        ], from: date(2026, 9, 10), now: now)
        let figures = HistoryFigures(days: all, now: now)
        #expect(figures.daysOverLimit == 2)
        // 13, 14, 15 → three; 17–20 → four.
        #expect(figures.longestSoberRun == 4)
    }

    // MARK: Favourite

    @Test("The favourite is the kind had most often, in its most usual size")
    func favourite() {
        let now = date(2026, 9, 20)
        let pint = HistoryServing(templateID: "beer", volumeMl: 500)
        let small = HistoryServing(templateID: "beer", volumeMl: 330)
        let wine = HistoryServing(templateID: "wine", volumeMl: 150)
        let all = days([
            occasion(at: date(2026, 9, 11, 21), servings: [small: 2, pint: 1]),
            occasion(at: date(2026, 9, 12, 21), servings: [wine: 2, small: 1]),
            occasion(at: date(2026, 9, 13, 21), servings: [wine: 1]),
        ], from: date(2026, 9, 10), now: now)
        // Beer four times against wine three; most of the beers were small.
        #expect(HistoryFigures(days: all, now: now).favourite == small)
    }
}

/// The slice of a session each day gets — cut from the cached clearing time,
/// so it goes through the store.
@MainActor
@Suite("History figures, from sessions")
struct HistoryInfluenceSliceTests {

    @Test("A night that runs into the next day is sliced at 05:00, and the slices add up to the session")
    func slicesAcrossDays() throws {
        let store = try makeStore()
        let twoDaysAgo = Calendar.current.date(byAdding: .day, value: -2, to: .now)!
        let start = Calendar.current.date(bySettingHour: 22, minute: 0, second: 0, of: twoDaysAgo)!
        for i in 0..<8 {
            store.add(.beer(at: start.addingTimeInterval(Double(i) * 1800)))
        }
        let day = DrinkingDay.containing(start)
        let session = try #require(store.sessions(overlapping: day.range).first)
        let soberAt = try #require(session.summary?.centerSoberAt)
        #expect(soberAt > day.end)

        let occasions = session.historyOccasions()
        let slices = occasions.compactMap(\.influence)
        #expect(slices.count == 2)
        #expect(slices.first?.start == start)
        #expect(slices.first?.end == day.end)
        #expect(slices.last?.end == soberAt)
        let total = slices.reduce(0) { $0 + $1.duration }
        #expect(abs(total - soberAt.timeIntervalSince(start)) < 1)
    }

    @Test("With the range switched on, the time runs to the middle curve's clearing, not the slow branch's")
    func middleCurveWithUncertainty() throws {
        let store = try makeStore()
        store.person.betaUncertainty = 0.04
        let twoDaysAgo = Calendar.current.date(byAdding: .day, value: -2, to: .now)!
        let start = Calendar.current.date(bySettingHour: 18, minute: 0, second: 0, of: twoDaysAgo)!
        for i in 0..<4 {
            store.add(.beer(at: start.addingTimeInterval(Double(i) * 1800)))
        }
        let session = try #require(store.sessions(overlapping: DrinkingDay.containing(start).range).first)
        let summary = try #require(session.summary)
        let slow = try #require(summary.soberAt)
        let middle = try #require(summary.centerSoberAt)
        // A band this wide puts the slow branch's clearing well over an hour later.
        #expect(slow.timeIntervalSince(middle) > 3600)
        #expect(session.historyOccasions().compactMap(\.influence).last?.end == middle)
    }

    @Test("Turning the range off clears the band from a past evening too, without moving where it ended")
    func uncertaintyIsADisplaySetting() throws {
        let store = try makeStore()
        store.person.betaUncertainty = 0.04
        let twoDaysAgo = Calendar.current.date(byAdding: .day, value: -2, to: .now)!
        let start = Calendar.current.date(bySettingHour: 18, minute: 0, second: 0, of: twoDaysAgo)!
        for i in 0..<4 {
            store.add(.beer(at: start.addingTimeInterval(Double(i) * 1800)))
        }
        let session = try #require(store.sessions(overlapping: DrinkingDay.containing(start).range).first)
        let endedAt = try #require(session.endedAt)
        let wide = try #require(session.summary?.peakRange)
        #expect(wide.upperBound - wide.lowerBound > 0.01)

        var profile = store.profile
        profile.betaUncertainty = 0
        store.profile = profile

        // The snapshot keeps its own value; only the way it is shown changed.
        #expect(session.betaUncertainty == 0.04)
        #expect(session.displayProfile.betaUncertainty == 0)
        #expect(session.endedAt == endedAt)
        // Drawn with the old spread, so stale until the backfill redraws it.
        #expect(session.summary == nil)
        let peak = try #require(session.chartModel(unit: .perMille).band.peakRange)
        #expect(peak.upperBound - peak.lowerBound < 1e-9)
    }
}
