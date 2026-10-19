import Foundation
import Testing
@testable import LogMyDrink

/// Which launch tip is offered, and when none is.
@Suite("Feature tips")
struct FeatureTipsTests {

    private let calendar: Calendar = {
        var c = Calendar(identifier: .gregorian)
        c.timeZone = TimeZone(identifier: "Europe/Budapest")!
        return c
    }()

    /// A fresh ledger whose first day is long gone.
    private func ledger() -> TipLedger {
        let defaults = UserDefaults(suiteName: "tips-\(UUID().uuidString)")!
        let ledger = TipLedger(defaults: defaults, calendar: calendar)
        _ = ledger.next(Self.fresh, now: day(-30))
        return ledger
    }

    private func day(_ offset: Int) -> Date {
        calendar.date(byAdding: .day, value: offset, to: Date(timeIntervalSince1970: 1_790_000_000))!
    }

    /// Nothing in use yet, a month of tracking, sober.
    static let fresh = TipContext(
        hasFavourite: false, widgetInstalled: false, siriUsed: false,
        historyOpened: false, trackedDays: 30, hasAlcohol: false
    )

    @Test("Nothing on the first day the app is opened")
    func notOnFirstDay() {
        let defaults = UserDefaults(suiteName: "tips-\(UUID().uuidString)")!
        let ledger = TipLedger(defaults: defaults, calendar: calendar)
        #expect(ledger.next(Self.fresh, now: day(0)) == nil)
        #expect(ledger.next(Self.fresh, now: day(1)) == .favourite)
    }

    @Test("In order, skipping what is already in use")
    func order() {
        let ledger = ledger()
        var context = Self.fresh
        #expect(ledger.next(context, now: day(0)) == .favourite)
        context.hasFavourite = true
        #expect(ledger.next(context, now: day(0)) == .widget)
        context.widgetInstalled = true
        #expect(ledger.next(context, now: day(0)) == .siri)
        context.siriUsed = true
        #expect(ledger.next(context, now: day(0)) == .history)
        context.historyOpened = true
        #expect(ledger.next(context, now: day(0)) == nil)
    }

    @Test("Never while there is alcohol in the blood")
    func notWhileDrinking() {
        var context = Self.fresh
        context.hasAlcohol = true
        #expect(ledger().next(context, now: day(0)) == nil)
    }

    @Test("At most one a day")
    func oncePerDay() {
        let ledger = ledger()
        ledger.markShown(at: day(0))
        #expect(ledger.next(Self.fresh, now: day(0)) == nil)
        #expect(ledger.next(Self.fresh, now: day(1)) == .favourite)
    }

    @Test("Don't show again is per tip")
    func dismissal() {
        let ledger = ledger()
        ledger.dismiss(.favourite)
        #expect(ledger.next(Self.fresh, now: day(0)) == .widget)
    }

    @Test("History waits for a week of data")
    func historyNeedsAWeek() {
        var context = Self.fresh
        context.hasFavourite = true
        context.widgetInstalled = true
        context.siriUsed = true
        context.trackedDays = 6
        #expect(ledger().next(context, now: day(0)) == nil)
    }

    @Test("The switch turns them all off")
    func switchedOff() {
        let ledger = ledger()
        ledger.defaults.set(false, forKey: TipLedger.enabledKey)
        #expect(ledger.next(Self.fresh, now: day(0)) == nil)
    }
}
