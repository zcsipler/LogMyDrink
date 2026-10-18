import Foundation
import Testing
import BACKit
@testable import LogMyDrink

/// What a day's window says about the occasion running through it (5.22).
/// A night that runs on into the next day was not over until it cleared,
/// and every day it touches has to say so.
@MainActor
@Suite("Day window")
struct DayWindowTests {

    /// An evening two days back, so every drink in the test is in the past
    /// whatever time the suite runs at.
    private func evening() -> Date {
        let twoDaysAgo = Calendar.current.date(byAdding: .day, value: -2, to: .now)!
        return Calendar.current.date(bySettingHour: 20, minute: 0, second: 0, of: twoDaysAgo)!
    }

    @Test("A night continued the next day clears, on both days, when the whole occasion does")
    func clearingIsTheOccasions() throws {
        let store = try makeStore()
        let start = evening()
        for i in 0..<10 {
            store.add(.beer(at: start.addingTimeInterval(Double(i) * 1800)))
        }
        let day = DrinkingDay.containing(start)
        let alone = try #require(store.dayWindow(for: day).soberAt)

        // The next morning, while ten beers are still well above zero.
        let morning = Calendar.current.date(bySettingHour: 9, minute: 0, second: 0, of: day.end)!
        store.add(.beer(at: morning))
        store.add(.beer(at: morning.addingTimeInterval(1800)))
        #expect(store.sessions(overlapping: day.range).count == 1)

        let first = store.dayWindow(for: day)
        let next = store.dayWindow(for: DrinkingDay.containing(morning))

        // Later than the first night alone, and the same on both pages.
        let sober = try #require(first.soberAt)
        #expect(sober > alone)
        #expect(next.soberAt == sober)

        // Both pages begin the occasion at the first night's first beer.
        #expect(first.occasionStart == start)
        #expect(next.occasionStart == start)
    }
}
