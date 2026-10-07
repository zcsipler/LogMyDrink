import Foundation
import Testing
import BACKit
@testable import LogMyDrink

/// The band flattened for the widget (5.15). What matters: the thinned curve
/// still carries the real peak, it ends where the band ends, and an evening
/// with nothing on it publishes as empty rather than as a curve of zeros.
@Suite("Widget snapshot")
struct WidgetSnapshotTests {

    private let engine = BACEngine()
    private let start = Date(timeIntervalSince1970: 1_700_000_000)

    private func band(_ drinks: [Drink]) -> BACBand {
        engine.simulateBand(profile: .test, drinks: drinks)
    }

    @Test("No drinks publishes an empty snapshot")
    func empty() {
        let snapshot = WidgetSnapshot.make(band: .empty, drinks: [], limit: 0.5, unit: .perMille, amountUnit: .grams)
        #expect(snapshot.isEmpty)
        #expect(snapshot.samples.isEmpty)
        #expect(snapshot.limit == 0.5)
    }

    @Test("Thinning keeps the centre peak and the last point")
    func thinningKeepsPeakAndEnd() throws {
        let drinks = [Drink.beer(at: start), .beer(at: start.addingTimeInterval(1800))]
        let band = band(drinks)
        let snapshot = WidgetSnapshot.make(band: band, drinks: drinks, limit: 0.5, unit: .perMille, amountUnit: .grams)

        let peak = try #require(band.peak)
        #expect(snapshot.peakAt == peak.date)
        let highest = try #require(snapshot.samples.max { $0.mid < $1.mid })
        #expect(highest.date == peak.date)
        #expect(abs(highest.mid - peak.bac) < 1e-9)

        // Roughly one point in five survives, plus the crests and the end.
        let full = band.samples.count
        #expect(snapshot.samples.count <= full / WidgetSnapshot.sampleStep + 2 + drinks.count)
        #expect(snapshot.samples.last?.date == band.samples.last?.date)
    }

    @Test("A drink logged on the way down leaves its own, lower crest in the samples")
    func secondCrestSurvives() throws {
        // Two beers, then a third four hours later, well into the descent.
        let late = start.addingTimeInterval(4 * 3600)
        let drinks = [Drink.beer(at: start), .beer(at: start.addingTimeInterval(1800)), .beer(at: late)]
        let band = band(drinks)
        let snapshot = WidgetSnapshot.make(band: band, drinks: drinks, limit: 0.5, unit: .perMille, amountUnit: .grams)

        let samples = snapshot.samples
        let crests = samples.indices.dropFirst().dropLast().filter { i in
            samples[i - 1].mid < samples[i].mid && samples[i].mid >= samples[i + 1].mid
        }
        let second = try #require(crests.first { samples[$0].date > late })
        let globalPeak = try #require(band.peak)
        #expect(samples[second].mid < globalPeak.bac)
        #expect(samples[second].mid > band.value(at: late))
        // The crest is the engine's own local maximum, not a grid point near it.
        let exact = band.center.samples.filter { $0.date > late }.max { $0.bac < $1.bac }
        #expect(samples[second].date == exact?.date)
    }

    @Test("Totals and the clearing window come from the same inputs the app shows")
    func totalsAndSober() throws {
        let drinks = [Drink.beer(at: start), .beer(at: start.addingTimeInterval(1800)), .beer(at: start.addingTimeInterval(3600))]
        let band = band(drinks)
        let snapshot = WidgetSnapshot.make(band: band, drinks: drinks, limit: 0.8, unit: .percent, amountUnit: .standardUnits)

        #expect(snapshot.drinkCount == 3)
        #expect(abs(snapshot.standardUnits - drinks.reduce(0) { $0 + $1.standardUnits }) < 1e-9)
        let sober = try #require(band.soberRange())
        #expect(snapshot.soberEarly == sober.lowerBound)
        #expect(snapshot.soberLate == sober.upperBound)
        #expect(snapshot.unit == .percent)
        #expect(snapshot.amountUnit == .standardUnits)
    }

    @Test("Round-trips through JSON with the field names the widget decodes")
    func roundTrip() throws {
        let drinks = [Drink.beer(at: start)]
        let snapshot = WidgetSnapshot.make(band: band(drinks), drinks: drinks, limit: 0.5, unit: .perMille, amountUnit: .grams)
        let data = try JSONEncoder().encode(snapshot)
        let decoded = try JSONDecoder().decode(WidgetSnapshot.self, from: data)
        #expect(decoded == snapshot)

        let object = try #require(try JSONSerialization.jsonObject(with: data) as? [String: Any])
        for key in ["version", "drinkCount", "standardUnits", "limit", "unit", "amountUnit", "samples", "peakAt", "soberLate"] {
            #expect(object[key] != nil, "missing \(key)")
        }
        #expect(object["unit"] as? String == "perMille")
    }
}
