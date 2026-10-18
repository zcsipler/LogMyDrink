import Foundation
import Testing
@testable import LogMyDrink

/// How an amount is written, and how big a unit is (5.16).
@Suite("Amount format")
struct AmountFormatTests {

    /// A 500 ml, 5 % beer: 19.7 g of ethanol, 1.97 of the model's 10 g units.
    private let beer = 500 * 0.05 * 0.789 / 10

    @Test("A unit is the size the user counts in", arguments: [(8.0, 2.5), (10, 2.0), (12, 1.6), (14, 1.4)])
    func unitSize(grams: Double, expected: Double) {
        let format = AmountFormat(unit: .standardUnits, gramsPerUnit: grams)
        #expect(abs(format.convert(standardUnits: beer) - expected) < 0.06)
    }

    @Test("Grams do not depend on the unit size")
    func gramsIgnoreTheSize() {
        let a = AmountFormat(unit: .grams, gramsPerUnit: 8)
        let b = AmountFormat(unit: .grams, gramsPerUnit: 14)
        #expect(a.formatted(standardUnits: beer) == b.formatted(standardUnits: beer))
        #expect(a.formatted(standardUnits: beer) == "20 g")
    }

    @Test("The region decides until the user does")
    func regionalDefault() {
        #expect(UnitSize.regional(Locale.Region("GB")) == 8)
        #expect(UnitSize.regional(Locale.Region("US")) == 14)
        #expect(UnitSize.regional(Locale.Region("DK")) == 12)
        #expect(UnitSize.regional(Locale.Region("HU")) == 10)
        #expect(UnitSize.regional(nil) == 10)

        let defaults = UserDefaults(suiteName: "logmydrink.tests.\(UUID().uuidString)")!
        let settings = AppSettings(defaults: defaults)
        #expect(settings.unitGrams == nil)
        settings.unitGrams = 14
        #expect(AppSettings(defaults: defaults).unitGrams == 14)
        #expect(AppSettings(defaults: defaults).effectiveUnitGrams == 14)
    }
}
