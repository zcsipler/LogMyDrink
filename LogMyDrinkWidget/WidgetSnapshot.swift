import Foundation
import SwiftUI

/// The widget's copy of what the app publishes — see
/// `LogMyDrink/Support/WidgetSnapshot.swift` for why it exists and what it
/// means. Field names, the date encoding (JSON default) and `version` must
/// agree with the app's type; this target compiles its own copy so that it
/// builds without touching the app's file memberships, like the rest of the
/// bridge.
///
/// Everything in g/L. This side only reads a value off the curve and
/// formats it; it never computes a level of its own.
struct WidgetSnapshot: Decodable {

    static let version = 1

    struct Sample: Decodable {
        let date: Date
        let low: Double
        let mid: Double
        let high: Double
    }

    let version: Int
    let drinkCount: Int
    let standardUnits: Double
    let limit: Double
    let unit: String
    let amountUnit: String

    let peakLow: Double?
    let peakHigh: Double?
    let peakAt: Date?
    let soberEarly: Date?
    let soberLate: Date?

    let samples: [Sample]

    var isEmpty: Bool { drinkCount == 0 || samples.isEmpty || version != Self.version }

    /// Must match `WidgetBridge` in the app target.
    static let appGroup = "group.dev.zcsipler.logmydrink"
    static let snapshotKey = "widget.snapshot"

    static func load() -> WidgetSnapshot? {
        guard
            let data = UserDefaults(suiteName: appGroup)?.data(forKey: snapshotKey),
            let snapshot = try? JSONDecoder().decode(WidgetSnapshot.self, from: data),
            !snapshot.isEmpty
        else { return nil }
        return snapshot
    }

    // MARK: Reading the curve

    /// The band at a moment, linearly interpolated between the published
    /// points — the same interpolation `BACCurve.value(at:)` does in the app.
    func range(at date: Date) -> ClosedRange<Double> {
        guard let first = samples.first, let last = samples.last else { return 0...0 }
        if date <= first.date { return bounds(first.low, first.high) }
        if date >= last.date { return bounds(last.low, last.high) }
        let (a, b) = neighbours(of: date)
        let span = b.date.timeIntervalSince(a.date)
        let w = span > 0 ? date.timeIntervalSince(a.date) / span : 0
        return bounds(a.low + w * (b.low - a.low), a.high + w * (b.high - a.high))
    }

    func value(at date: Date) -> Double {
        guard let first = samples.first, let last = samples.last else { return 0 }
        if date <= first.date { return first.mid }
        if date >= last.date { return last.mid }
        let (a, b) = neighbours(of: date)
        let span = b.date.timeIntervalSince(a.date)
        let w = span > 0 ? date.timeIntervalSince(a.date) / span : 0
        return a.mid + w * (b.mid - a.mid)
    }

    /// The next crest of the curve after a moment: the first local maximum
    /// ahead. Nil when the curve only falls from here.
    ///
    /// Not the evening's highest point. After a drink logged on the way down
    /// the curve turns up again to a *lower* crest than the earlier one, and
    /// that lower crest is what you are heading to now — measured against
    /// the global peak it would never show.
    ///
    /// The curve is allowed to dip first. In the minutes right after a drink
    /// is logged, elimination still outruns absorption, so the level keeps
    /// falling for a little before it turns — a rule that demanded "the next
    /// sample is higher than now" saw only the dip and said "falling" for
    /// the one drink that had just been poured. Whether the crest is worth
    /// naming (higher than now by a printable amount) is the caller's call.
    func nextCrest(after date: Date) -> (date: Date, range: ClosedRange<Double>)? {
        guard let start = samples.firstIndex(where: { $0.date > date }) else { return nil }
        // A crest is a sample above its predecessor and not below its
        // successor; the last sample is the floor at zero, never a crest.
        var index = start
        while index + 1 < samples.count {
            let previous = index == start ? value(at: date) : samples[index - 1].mid
            if samples[index].mid > previous, samples[index].mid >= samples[index + 1].mid {
                let crest = samples[index]
                return (crest.date, bounds(crest.low, crest.high))
            }
            index += 1
        }
        return nil
    }

    private func neighbours(of date: Date) -> (Sample, Sample) {
        var low = 0, high = samples.count - 1
        while high - low > 1 {
            let mid = (low + high) / 2
            if samples[mid].date <= date { low = mid } else { high = mid }
        }
        return (samples[low], samples[high])
    }

    private func bounds(_ a: Double, _ b: Double) -> ClosedRange<Double> {
        min(a, b)...max(a, b)
    }

    // MARK: Formatting — the app's `BACUnit` / `AmountUnit`, reduced to what
    // the widget prints. No words: numbers, symbols and times format
    // themselves in the system language, and this target has no string
    // catalog of its own.

    var unitSuffix: String { unit == "percent" ? "%" : "‰" }

    func formatLevel(_ gramsPerLiter: Double) -> String {
        let percent = unit == "percent"
        let value = percent ? gramsPerLiter / 10 : gramsPerLiter
        return value.formatted(.number.precision(.fractionLength(percent ? 3 : 2)).grouping(.never))
    }

    /// Collapses when both ends print the same — never "0.52–0.52" (5.8).
    func formatLevelRange(_ range: ClosedRange<Double>) -> String {
        let low = formatLevel(range.lowerBound), high = formatLevel(range.upperBound)
        return low == high ? low : "\(low)–\(high)"
    }

    var formattedAmount: String {
        if amountUnit == "standardUnits" {
            return standardUnits.formatted(.number.precision(.fractionLength(1)).grouping(.never))
        }
        let grams = standardUnits * 10
        return "\(grams.formatted(.number.precision(.fractionLength(0)).grouping(.never))) g"
    }
}

extension ClosedRange where Bound == Date {
    /// "19:00–22:00", or one time when they coincide — as in the app.
    var hourMinuteRange: String {
        let from = lowerBound.formatted(date: .omitted, time: .shortened)
        let to = upperBound.formatted(date: .omitted, time: .shortened)
        return from == to ? from : "\(from)–\(to)"
    }
}

/// The app's level ramp (`Theme.tint(for:limit:)`), copied so that the Home
/// Screen widget colours the number the way the app does: against the
/// person's own limit, full red exactly at it. The Lock Screen never sees
/// this — accessory widgets render monochrome — which is also why the arrow
/// there has to carry its meaning by direction alone.
enum WidgetTheme {
    static let background = Color(red: 0.043, green: 0.051, blue: 0.071)
    static let secondaryText = Color(red: 0.561, green: 0.588, blue: 0.643)

    private static let ramp: [(at: Double, rgb: (Double, Double, Double))] = [
        (0.00, (0.271, 0.749, 0.706)),
        (0.55, (0.949, 0.714, 0.310)),
        (0.85, (0.937, 0.427, 0.396)),
        (1.00, (0.925, 0.176, 0.196)),
        (1.50, (0.745, 0.043, 0.157)),
    ]

    static func tint(for bac: Double, limit: Double) -> Color {
        let x = bac / max(limit, 0.05)
        guard let first = ramp.first, let last = ramp.last else { return .white }
        if x <= first.at { return color(first.rgb) }
        if x >= last.at { return color(last.rgb) }
        for (lower, upper) in zip(ramp, ramp.dropFirst()) where x < upper.at {
            let t = (x - lower.at) / (upper.at - lower.at)
            return Color(
                red: lower.rgb.0 + (upper.rgb.0 - lower.rgb.0) * t,
                green: lower.rgb.1 + (upper.rgb.1 - lower.rgb.1) * t,
                blue: lower.rgb.2 + (upper.rgb.2 - lower.rgb.2) * t
            )
        }
        return color(last.rgb)
    }

    private static func color(_ rgb: (Double, Double, Double)) -> Color {
        Color(red: rgb.0, green: rgb.1, blue: rgb.2)
    }
}
