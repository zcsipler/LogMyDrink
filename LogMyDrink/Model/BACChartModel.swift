import Foundation
import BACKit

/// Everything the curve needs to draw itself: a day's window onto the
/// timeline, or one stored occasion.
///
/// The chart used to read `SessionStore` directly, which meant it could only
/// ever show tonight. This value type is the seam: the live store produces one
/// for today, the day page one for any day, and a `DrinkingSession` out of the
/// history one for itself — with that session's own profile snapshot, so a
/// past evening is drawn as it actually was.
///
/// A **day** is a window from five in the morning to five the next: the band
/// is the part of every occasion that falls inside it, joined and clipped
/// (`BACBand.clipped`, `BACBand.joined`). A night that runs past the boundary
/// is cut there and continues on the next page, which starts at the level the
/// night left behind — `carryIn`. The IntelliDrink picture: one continuous
/// curve, and days are where you look at it.
struct BACChartModel {
    /// What is drawn — clipped to `window` when there is one.
    let band: BACBand
    /// The drinks inside the window.
    let drinks: [Drink]
    let limit: Double
    let unit: BACUnit

    /// Where the marker and the readout sit. `nil` on a finished occasion or
    /// a past day, which have no "now" worth pointing at.
    let focusDate: Date?

    /// Live days get the "still rising" badge and a dashed now-line;
    /// finished ones do not, because neither means anything in the past.
    let isLive: Bool

    /// The day drawn, or nil for a single occasion framed to itself.
    let window: ClosedRange<Date>?

    /// When the level clears, from the **unclipped** curve: a night cut at the
    /// window's edge still clears tomorrow afternoon, and that is the time
    /// to tell.
    let soberRange: ClosedRange<Date>?

    /// The band at the window's start, when the previous night is still
    /// there. Nil for a day that began clear, and for a single occasion.
    let carryIn: ClosedRange<Double>?

    // MARK: Derived

    /// The first drink inside the window — where this day's own curve begins.
    private var firstDrinkAt: Date? { drinks.map(\.consumedAt).min() }

    /// The peak of **this day's drinks**: the highest point from the first
    /// drink on. A morning that starts at 1.3 ‰ from the night before and
    /// adds a beer at noon peaked at the beer; the 1.3 is last night's peak,
    /// reported on last night's page (5.16). Nil on a day with nothing drunk.
    var peak: BACSample? {
        guard let firstDrinkAt else { return nil }
        return band.center.peak(after: firstDrinkAt)
    }

    var peakRange: ClosedRange<Double>? {
        guard let firstDrinkAt else { return nil }
        return band.peakRange(after: firstDrinkAt)
    }

    /// The peak is only "expected" while it is still ahead of us.
    var upcomingPeak: BACSample? {
        guard isLive, let focusDate, let peak,
              peak.date > focusDate.addingTimeInterval(60)
        else { return nil }
        return peak
    }

    var currentRange: ClosedRange<Double> {
        guard let focusDate, !band.isEmpty else { return 0...0 }
        return band.range(at: focusDate)
    }

    var currentBAC: Double {
        guard let focusDate, !band.isEmpty else { return 0 }
        return band.value(at: focusDate)
    }

    var currentRate: Double {
        guard let focusDate else { return 0 }
        return band.center.rate(at: focusDate)
    }

    var isRising: Bool { isLive && !band.isEmpty && currentRate > 0.01 }

    /// Whether there is anything to draw: drinks, or a level carried in.
    var hasContent: Bool { !drinks.isEmpty || carryIn != nil }

    /// The span to plot.
    ///
    /// Inside a window: from the window's start when a level was carried in,
    /// otherwise from a little before the first drink; to where the curve
    /// clears, or the window's end if it runs past it. A live day is padded
    /// to at least six hours so the curve has room to grow into. A single
    /// occasion is framed to what actually happened.
    var visibleRange: ClosedRange<Date> {
        let first = firstDrinkAt ?? focusDate ?? band.center.startedAt
        var start = first.addingTimeInterval(-15 * 60)
        if let window, carryIn != nil { start = window.lowerBound }

        let natural = soberRange?.upperBound
            ?? focusDate?.addingTimeInterval(4 * 3600)
            ?? start.addingTimeInterval(6 * 3600)
        var end = natural.addingTimeInterval(20 * 60)
        if isLive { end = max(end, start.addingTimeInterval(6 * 3600)) }
        end = max(end, start.addingTimeInterval(3600))

        if let window {
            start = max(start, window.lowerBound)
            end = min(end, window.upperBound)
            if end <= start { end = window.upperBound }
        }
        return start...end
    }

    /// The highest level the drawn band reaches, carried-in level included —
    /// what the curve is coloured by, as opposed to `peakRange`, which is
    /// what this day's drinks did.
    var highestLevel: Double {
        band.upper.samples.map(\.bac).max() ?? 0
    }

    /// Room for the whole visible band, not only for this day's own peak.
    var yMaximum: Double {
        max(highestLevel * 1.3, limit * 1.4, 0.5)
    }
}

// MARK: - Producers

extension DrinkingSession {
    /// A stored occasion, recomputed with **its own** profile snapshot.
    ///
    /// Not the current profile: that is the whole point of storing the
    /// snapshot. Changing your weight today must not redraw last month.
    func chartModel(unit: BACUnit, engine: BACEngine = BACEngine()) -> BACChartModel {
        let drinks = sortedDrinks
        let band = drinks.isEmpty ? BACBand.empty : engine.simulateBand(profile: profile, drinks: drinks)
        return BACChartModel(
            band: band,
            drinks: drinks,
            limit: limit,
            unit: unit,
            focusDate: nil,
            isLive: false,
            window: nil,
            soberRange: drinks.isEmpty ? nil : band.soberRange(),
            carryIn: nil
        )
    }
}

extension SessionStore {
    /// Today's window, for the Live screen: the running occasion if there
    /// is one, whatever finished earlier today, and the tail of last night.
    var chartModel: BACChartModel {
        chartModel(for: DrinkingDay.containing(now))
    }

    /// The window of any drinking day. Live when `day` is today.
    ///
    /// Each occasion is drawn with its own profile snapshot; the running one
    /// reuses the band the store already has. The heavy part — bands, joined
    /// and clipped — is kept per day until the store next writes
    /// (`DayWindow`); only the focus moves with the clock.
    func chartModel(for day: DrinkingDay) -> BACChartModel {
        let live = day.isCurrent(at: now)
        let window = dayWindow(for: day)
        return BACChartModel(
            band: window.band,
            drinks: window.drinks,
            limit: live ? limit : window.limit,
            unit: unit,
            focusDate: live ? now : nil,
            isLive: live,
            window: day.start...day.end,
            soberRange: window.soberRange,
            carryIn: window.carryIn
        )
    }
}
