import Foundation
import BACKit

/// The open occasion, flattened for the widget.
///
/// The widget runs in its own process without the store, so it is handed
/// the *answer* rather than the inputs: the band already simulated, thinned
/// to one point every few minutes, plus the few numbers the Live hero shows.
/// The widget does no pharmacokinetics — it reads a level off this curve for
/// each timeline entry — so the two processes cannot disagree, and the
/// extension never needs the engine or a profile.
///
/// Why a curve and not just today's number: a widget timeline is a list of
/// future entries, and the band *is* the future. Publishing it once per
/// write lets the Lock Screen count down through the night with no reload
/// and no app launch in between.
///
/// Every concentration is g/L (= ‰), like everywhere else; the display unit
/// travels alongside so the widget formats the way the app does.
///
/// The widget target decodes this with its own copy of the type
/// (`LogMyDrinkWidget/WidgetSnapshot.swift`); field names and the date
/// encoding must agree. `version` is bumped when they change, so a stale
/// extension shows the plain button instead of nonsense.
struct WidgetSnapshot: Codable, Equatable {

    static let version = 1

    struct Sample: Codable, Equatable {
        let date: Date
        /// Fast elimination.
        let low: Double
        let mid: Double
        /// Slow elimination.
        let high: Double
    }

    let version: Int
    let drinkCount: Int
    let standardUnits: Double
    let limit: Double
    let unit: BACUnit
    let amountUnit: AmountUnit

    let peakLow: Double?
    let peakHigh: Double?
    /// The centre curve's highest point. The widget names the *next* crest,
    /// read off the samples; this is the evening's figure for anything else.
    let peakAt: Date?
    let soberEarly: Date?
    let soberLate: Date?

    let samples: [Sample]

    var isEmpty: Bool { drinkCount == 0 || samples.isEmpty }

    /// Thinning step. The widget's timeline advances in the same steps, so
    /// nothing finer would ever be shown; every crest is kept regardless, so
    /// the peaks the widget prints are the real ones.
    static let sampleStep = 5

    /// Nobody drinking, or no open occasion.
    static func empty(limit: Double, unit: BACUnit, amountUnit: AmountUnit) -> WidgetSnapshot {
        WidgetSnapshot(
            version: version, drinkCount: 0, standardUnits: 0,
            limit: limit, unit: unit, amountUnit: amountUnit,
            peakLow: nil, peakHigh: nil, peakAt: nil, soberEarly: nil, soberLate: nil,
            samples: []
        )
    }

    init(
        version: Int, drinkCount: Int, standardUnits: Double,
        limit: Double, unit: BACUnit, amountUnit: AmountUnit,
        peakLow: Double?, peakHigh: Double?, peakAt: Date?, soberEarly: Date?, soberLate: Date?,
        samples: [Sample]
    ) {
        self.version = version
        self.drinkCount = drinkCount
        self.standardUnits = standardUnits
        self.limit = limit
        self.unit = unit
        self.amountUnit = amountUnit
        self.peakLow = peakLow
        self.peakHigh = peakHigh
        self.peakAt = peakAt
        self.soberEarly = soberEarly
        self.soberLate = soberLate
        self.samples = samples
    }

    /// The open occasion, or `empty` when there is nothing on the curve.
    static func make(band: BACBand, drinks: [Drink], limit: Double, unit: BACUnit, amountUnit: AmountUnit) -> WidgetSnapshot {
        guard !drinks.isEmpty, !band.isEmpty else {
            return .empty(limit: limit, unit: unit, amountUnit: amountUnit)
        }

        let all = band.samples
        let peakDate = band.peak?.date

        // Every local maximum survives the thinning, not only the evening's
        // highest point: a drink logged on the way down raises a second,
        // lower crest, and that is the one the widget has to name next.
        var thinned: [Sample] = []
        thinned.reserveCapacity(all.count / Self.sampleStep + 8)
        for (index, sample) in all.enumerated() {
            let onGrid = index % Self.sampleStep == 0
            let isLast = index == all.count - 1
            let isCrest = index > 0 && index < all.count - 1
                && all[index - 1].mid < sample.mid && sample.mid >= all[index + 1].mid
            guard onGrid || isLast || isCrest else { continue }
            thinned.append(Sample(date: sample.date, low: sample.low, mid: sample.mid, high: sample.high))
        }

        let peakRange = band.peakRange
        let sober = band.soberRange()
        return WidgetSnapshot(
            version: version,
            drinkCount: drinks.count,
            standardUnits: drinks.reduce(0) { $0 + $1.standardUnits },
            limit: limit, unit: unit, amountUnit: amountUnit,
            peakLow: peakRange?.lowerBound, peakHigh: peakRange?.upperBound, peakAt: peakDate,
            soberEarly: sober?.lowerBound, soberLate: sober?.upperBound,
            samples: thinned
        )
    }
}
