import Testing
import Foundation
@testable import BACKit

private let reference = BodyProfile(sex: .male, age: 35, heightCm: 180, weightKg: 80)
private let t0 = Date(timeIntervalSince1970: 1_000_000_000)   // a fixed, arbitrary instant
private let engine = BACEngine()

private func hour(_ h: Double) -> Date { t0.addingTimeInterval(h * 3600) }

private func beer(at date: Date, ml: Double = 500) -> Drink {
    Drink(consumedAt: date, volumeMl: ml, abvPercent: 5, stomach: .light, drinkingMinutes: 30)
}

// MARK: - Splitting drinks into occasions

@Suite("Occasions")
struct OccasionsTests {

    @Test("Drinks while the level is still up are one occasion")
    func sameEvening() {
        let drinks = [beer(at: hour(0)), beer(at: hour(1)), beer(at: hour(2.5))]
        let groups = Occasions.split(drinks, profile: reference, engine: engine)
        #expect(groups.count == 1)
        #expect(groups[0].count == 3)
    }

    @Test("A drink the next afternoon, on an empty curve, starts a new occasion")
    func nextDay() {
        // One beer clears in about three hours; twenty hours later is far
        // beyond the grace period.
        let drinks = [beer(at: hour(0)), beer(at: hour(20))]
        let groups = Occasions.split(drinks, profile: reference, engine: engine)
        #expect(groups.count == 2)
        #expect(groups[1].first?.consumedAt == hour(20))
    }

    @Test("A gap shorter than the grace period after clearing does not split")
    func shortBreak() {
        // One beer clears around hour 3; the next at hour 5 is two hours
        // after that, inside the three-hour grace.
        let drinks = [beer(at: hour(0)), beer(at: hour(5))]
        #expect(Occasions.split(drinks, profile: reference, engine: engine).count == 1)

        // Four hours after clearing is outside it.
        let apart = [beer(at: hour(0)), beer(at: hour(7.5))]
        #expect(Occasions.split(apart, profile: reference, engine: engine).count == 2)
    }

    /// The case this exists for: a heavy night that is still at 0.16 ‰ the
    /// next afternoon, and a beer logged then. Grouped by drinking day, the
    /// beer opened a second occasion from zero and the 0.16 vanished.
    @Test("A beer the afternoon after a heavy night continues that night")
    func carryOverContinuesTheNight() {
        let profile = BodyProfile(sex: .male, age: 41, heightCm: 168, weightKg: 64, beta: 0.18)
        // 17:23 → 23:51 the evening before, then 14:26 the next day: the
        // same shape as 8–9 October, with t0 standing for 17:23.
        let starts: [Double] = [0, 0.49, 1.42, 1.80, 2.53, 3.40, 4.07, 4.57, 5.95, 6.47]
        var drinks = starts.map { beer(at: hour($0)) }
        let nextAfternoon = beer(at: hour(21.05))
        drinks.append(nextAfternoon)

        let level = engine.simulateBand(profile: profile, drinks: Array(drinks.dropLast()))
            .upper.value(at: nextAfternoon.consumedAt)
        #expect(level > 0.1)   // still there when the beer is logged

        let groups = Occasions.split(drinks, profile: profile, engine: engine)
        #expect(groups.count == 1)
        #expect(groups[0].count == 11)
    }

    @Test("Removing a drink from the middle can split an occasion in two")
    func deletionSplits() {
        // Two beers an hour apart, then — after a long gap bridged only by a
        // third beer in between — two more. With the bridge gone, the curve
        // clears between the pairs for longer than the grace period.
        let bridge = beer(at: hour(5))
        let drinks = [beer(at: hour(0)), beer(at: hour(1)), bridge, beer(at: hour(9)), beer(at: hour(10))]

        #expect(Occasions.split(drinks, profile: reference, engine: engine).count == 1)
        let without = drinks.filter { $0.id != bridge.id }
        let groups = Occasions.split(without, profile: reference, engine: engine)
        #expect(groups.count == 2)
        #expect(groups[0].count == 2)
        #expect(groups[1].count == 2)
    }

    @Test("The order drinks are passed in does not matter")
    func orderIndependent() {
        let drinks = [beer(at: hour(20)), beer(at: hour(0)), beer(at: hour(1))]
        let groups = Occasions.split(drinks, profile: reference, engine: engine)
        #expect(groups.map(\.count) == [2, 1])
        #expect(groups[0].map(\.consumedAt) == [hour(0), hour(1)])
    }

    @Test("Empty and single inputs")
    func degenerate() {
        #expect(Occasions.split([], profile: reference, engine: engine).isEmpty)
        #expect(Occasions.split([beer(at: t0)], profile: reference, engine: engine).count == 1)
    }

    @Test("covers: within the grace after clearing, or not yet cleared")
    func covers() {
        let sober = hour(10)
        #expect(Occasions.covers(soberAt: sober, date: hour(9)))
        #expect(Occasions.covers(soberAt: sober, date: hour(12.9)))
        #expect(!Occasions.covers(soberAt: sober, date: hour(13)))
        #expect(Occasions.covers(soberAt: nil, date: hour(100)))
    }
}

// MARK: - Windows onto the curve

@Suite("Curve windows")
struct CurveWindowTests {

    private var evening: BACCurve {
        engine.simulate(profile: reference, drinks: [beer(at: hour(0)), beer(at: hour(1)), beer(at: hour(2))])
    }

    @Test("Clipping keeps the inside and adds interpolated edges")
    func clip() {
        let curve = evening
        let window = hour(1.5)...hour(3)
        let part = curve.clipped(to: window)

        #expect(part.samples.first?.date == window.lowerBound)
        #expect(part.samples.last?.date == window.upperBound)
        #expect(part.samples.allSatisfy { window.contains($0.date) })
        #expect(abs(part.samples.first!.bac - curve.value(at: window.lowerBound)) < 1e-9)
        #expect(abs(part.samples.last!.bac - curve.value(at: window.upperBound)) < 1e-9)
        #expect(part.samples.first!.bac > 0.1)
    }

    @Test("A window the curve does not reach is empty")
    func outside() {
        let curve = evening
        #expect(curve.clipped(to: hour(30)...hour(40)).samples.isEmpty)
        #expect(curve.clipped(to: hour(-5)...hour(-1)).samples.isEmpty)
    }

    @Test("A window wider than the curve leaves it unchanged")
    func wider() {
        let curve = evening
        let part = curve.clipped(to: hour(-1)...hour(40))
        #expect(part.samples.count == curve.samples.count)
    }

    @Test("Joining two occasions keeps both and stays at zero between them")
    func join() {
        let first = engine.simulate(profile: reference, drinks: [beer(at: hour(0))])
        let second = engine.simulate(profile: reference, drinks: [beer(at: hour(20))])
        let joined = BACCurve.joined([second, first])

        #expect(joined.startedAt == first.startedAt)
        #expect(joined.samples.count == first.samples.count + second.samples.count)
        #expect(joined.value(at: hour(10)) == 0)
        #expect(joined.value(at: hour(20.5)) > 0)
        #expect(joined.value(at: hour(0.5)) > 0)
    }

    @Test("The peak after a time ignores the earlier, higher one")
    func peakAfter() {
        // A big evening, then one beer the next afternoon on the tail.
        let profile = BodyProfile(sex: .male, age: 41, heightCm: 168, weightKg: 64, beta: 0.18)
        let drinks = (0..<8).map { beer(at: hour(Double($0) * 0.6)) } + [beer(at: hour(18))]
        let curve = engine.simulate(profile: profile, drinks: drinks)

        let whole = curve.peak!.bac
        let afternoon = curve.peak(after: hour(18))!.bac
        #expect(afternoon < whole)
        #expect(afternoon > curve.value(at: hour(18)))   // the beer did raise it
        #expect(curve.peak(after: hour(18))!.date > hour(18))
    }
}
