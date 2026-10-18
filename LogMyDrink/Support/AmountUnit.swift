import Foundation
import BACKit

/// How much alcohol a figure stands for: grams of ethanol, or units.
///
/// One or the other, never both: the two are the same number in different
/// words, and side by side they only cost space (5.16; tried and taken back
/// in 2026 October). Grams is the default: a gram means the same thing
/// everywhere.
enum AmountUnit: String, CaseIterable, Codable, Identifiable, Sendable {
    case grams
    case standardUnits

    var id: String { rawValue }

    /// The full name, for the settings row.
    var label: LocalizedStringResource {
        switch self {
        case .grams: "Grams of alcohol"
        case .standardUnits: "Standard units"
        }
    }

    /// The word over a figure in a stat row or on an axis.
    var shortLabel: LocalizedStringResource {
        switch self {
        case .grams: "Grams"
        case .standardUnits: "Units"
        }
    }
}

/// What a unit is worth in grams — which depends on where you live.
///
/// A "unit" is 8 g in Britain, 10 g for the WHO and most of Europe, 12 g in
/// the Nordic countries and 14 g as a US standard drink: the same 20 g beer
/// is 2.5, 2.0, 1.7 or 1.4 of them. Someone who counts in units counts in
/// the ones their doctor or their country uses, so the size is a setting,
/// offered once units are chosen; until the user picks one, the device's
/// region decides.
///
/// The model still counts in 10 g standard units (`Drink.standardUnits`,
/// `Physiology.gramsPerStandardUnit`); this is display only.
enum UnitSize {
    /// The sizes offered, in grams.
    static let options: [Double] = [8, 10, 12, 14]

    /// The size where the device is, by its region: the UK 8 g, the US 14 g,
    /// Denmark, Sweden and Finland 12 g, and 10 g — the WHO's — elsewhere.
    static func regional(_ region: Locale.Region? = Locale.current.region) -> Double {
        switch region?.identifier {
        case "GB": 8
        case "US": 14
        case "DK", "SE", "FI": 12
        default: 10
        }
    }

    /// Where a size is the convention, for the settings row.
    static func convention(_ grams: Double) -> LocalizedStringResource {
        switch grams {
        case 8: "UK"
        case 12: "Nordic countries"
        case 14: "US standard drink"
        default: "WHO, most of Europe"
        }
    }
}

/// An amount unit together with the size of a unit: everything needed to
/// write an amount down. Built by the store from the device settings, so a
/// view cannot format units with the wrong size by forgetting to pass it.
struct AmountFormat: Equatable, Sendable {
    var unit: AmountUnit
    var gramsPerUnit: Double

    var shortLabel: LocalizedStringResource { unit.shortLabel }

    /// From the model's 10 g standard units to this format's figure.
    func convert(standardUnits: Double) -> Double {
        let grams = standardUnits * Physiology.gramsPerStandardUnit
        switch unit {
        case .grams: return grams
        case .standardUnits: return grams / gramsPerUnit
        }
    }

    /// Whole grams, or units to one decimal.
    func format(standardUnits: Double) -> String {
        convert(standardUnits: standardUnits).formatted(
            .number
                .precision(.fractionLength(unit == .grams ? 0 : 1))
                .grouping(.never)
        )
    }

    /// With the symbol where there is one: "334 g", or "33.4" — a unit count
    /// has no symbol, and the label next to it says what it is.
    func formatted(standardUnits: Double) -> String {
        switch unit {
        case .grams: "\(format(standardUnits: standardUnits)) g"
        case .standardUnits: format(standardUnits: standardUnits)
        }
    }
}
