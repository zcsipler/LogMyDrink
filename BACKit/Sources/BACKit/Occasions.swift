import Foundation

/// Where one drinking occasion ends and the next begins — decided by the
/// curve, not by the clock.
///
/// An occasion is a run of drinks whose curve never clears for long between
/// two of them: while there is still alcohol in the body, or it cleared less
/// than `grace` ago, the next drink is the same occasion. A beer at two in
/// the afternoon with last night's 0.2 ‰ still there continues last night;
/// a beer the day after that, on an empty curve, starts something new.
///
/// Nothing about days: the five o'clock boundary files evenings under days
/// for the history, and a window onto the timeline is what a day page shows.
/// Grouping by the calendar instead split one long night in two at the
/// boundary and drew the second half from zero, with the first half's level
/// silently dropped.
public enum Occasions {

    /// How long after the level has cleared a drink still joins the same
    /// occasion.
    ///
    /// A short break — leaving one bar for another — should not start a new
    /// occasion. Three hours covers that and is short enough that tomorrow's
    /// first drink is clearly its own.
    public static let grace: TimeInterval = 3 * 3600

    /// The level below which the body counts as cleared.
    public static let clearedThreshold = 0.01

    /// Splits `drinks` into occasions, oldest first, each in consumption order.
    ///
    /// One simulation for the lot: between two drinks only the earlier ones
    /// contribute, so the curve of all of them *is* the curve of the earlier
    /// ones up to the moment the next starts. The slow branch of the band
    /// decides, the same branch that gives the latest clearing time.
    public static func split(
        _ drinks: [Drink],
        profile: BodyProfile,
        engine: BACEngine = BACEngine(),
        grace: TimeInterval = grace,
        threshold: Double = clearedThreshold
    ) -> [[Drink]] {
        let ordered = drinks.sorted { $0.consumedAt < $1.consumedAt }
        guard ordered.count > 1 else { return ordered.isEmpty ? [] : [ordered] }

        let curve = engine.simulateBand(profile: profile, drinks: ordered).upper
        var groups: [[Drink]] = [[ordered[0]]]

        for index in 1..<ordered.count {
            let previous = ordered[index - 1]
            let next = ordered[index]
            if let cleared = clearing(of: curve, after: previous, before: next.consumedAt, threshold: threshold),
               next.consumedAt.timeIntervalSince(cleared) >= grace {
                groups.append([next])
            } else {
                groups[groups.count - 1].append(next)
            }
        }
        return groups
    }

    /// Whether a drink at `date` continues an occasion whose slow branch
    /// clears at `soberAt` — or has not cleared at all, when `soberAt` is nil
    /// for a curve the engine's cap cut short. Only for dates after the
    /// occasion started; the caller checks that.
    public static func covers(soberAt: Date?, date: Date, grace: TimeInterval = grace) -> Bool {
        guard let soberAt else { return true }
        return date.timeIntervalSince(soberAt) < grace
    }

    /// When the level cleared after `drink` took effect, if it did before
    /// `deadline`.
    ///
    /// "Took effect" matters: at the instant a drink starts the level can
    /// still be below threshold — the very first drink starts from zero — and
    /// reading that as "cleared" would cut every occasion after its first
    /// sip. So the search first waits for the curve to rise above threshold,
    /// then for it to fall back. A drink too small to ever show counts as
    /// cleared when it was finished.
    private static func clearing(
        of curve: BACCurve,
        after drink: Drink,
        before deadline: Date,
        threshold: Double
    ) -> Date? {
        let samples = curve.samples
        guard let rose = samples.firstIndex(where: { $0.date >= drink.consumedAt && $0.bac >= threshold }) else {
            // Never registered on the curve at all: cleared when finished.
            return drink.consumedAt.addingTimeInterval(drink.drinkingMinutes * 60)
        }
        // Rose only after the next drink had started — the two overlap.
        guard samples[rose].date < deadline else { return nil }
        guard let fell = samples[rose...].first(where: { $0.bac < threshold }), fell.date <= deadline else {
            return nil
        }
        return fell.date
    }
}
