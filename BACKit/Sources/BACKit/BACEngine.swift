import Foundation

/// One sample on the BAC curve.
public struct BACSample: Hashable, Sendable {
    /// Absolute timestamp — usable directly as a Swift Charts x value.
    public let date: Date
    /// Blood alcohol concentration in g/L (= per mille).
    public let bac: Double
    /// Signed rate of change in g/L/h. Positive means the absorption limb.
    public let rate: Double
}

/// The result of a simulation.
public struct BACCurve: Sendable {
    public let samples: [BACSample]
    public let startedAt: Date

    public init(samples: [BACSample], startedAt: Date) {
        self.samples = samples
        self.startedAt = startedAt
    }

    public var isEmpty: Bool { samples.allSatisfy { $0.bac <= 0 } }

    /// The highest point on the curve.
    public var peak: BACSample? {
        samples.max { $0.bac < $1.bac }
    }

    /// The steepest rise. Memory impairment correlates with this better than
    /// with the total amount consumed.
    public var steepestRise: BACSample? {
        samples.max { $0.rate < $1.rate }
    }

    /// Linearly interpolated value at an arbitrary time.
    public func value(at date: Date) -> Double {
        guard let first = samples.first, let last = samples.last else { return 0 }
        if date <= first.date { return first.bac }
        if date >= last.date { return last.bac }

        var low = 0, high = samples.count - 1
        while high - low > 1 {
            let mid = (low + high) / 2
            if samples[mid].date <= date { low = mid } else { high = mid }
        }
        let a = samples[low], b = samples[high]
        let span = b.date.timeIntervalSince(a.date)
        guard span > 0 else { return a.bac }
        let w = date.timeIntervalSince(a.date) / span
        return a.bac + w * (b.bac - a.bac)
    }

    /// The first time after the peak at which the level drops below `threshold`.
    ///
    /// `nil` means the curve had **not** cleared when the simulation stopped —
    /// see `hasCleared`. It never means "already clear": an empty curve has
    /// no peak and returns `nil` too, but callers that need the distinction
    /// check `isEmpty` first.
    public func soberDate(threshold: Double = 0.01) -> Date? {
        guard let peak else { return nil }
        return samples.first { $0.date >= peak.date && $0.bac < threshold }?.date
    }

    /// Whether the level is below `threshold` at the end of the curve.
    ///
    /// The engine simulates until the body has cleared or `BACEngine.horizonMinutes`
    /// runs out, so this is `false` only for an evening the cap cut short.
    /// It exists because a missing `soberDate` was once read as "nothing left
    /// to clear" and closed a heavy night at breakfast with 1.3 ‰ still in
    /// the blood. A curve still above threshold at its last sample is still
    /// running, and the caller must treat it that way.
    public func hasCleared(threshold: Double = 0.01) -> Bool {
        guard let last = samples.last else { return true }
        return last.bac < threshold
    }

    /// The highest point at or after `date`.
    ///
    /// A day's peak is the peak of what was drunk on that day, not the
    /// highest level seen on it: a morning that starts at 1.3 ‰ from the
    /// night before and adds one beer at noon peaked at the beer, and the
    /// 1.3 is the previous evening's to report. So the caller passes the
    /// first drink of the day and gets the maximum from there on.
    public func peak(after date: Date) -> BACSample? {
        samples.filter { $0.date >= date }.max { $0.bac < $1.bac }
    }

    /// The part of the curve inside `window`, with interpolated samples at
    /// both edges so a curve that enters or leaves the window mid-way still
    /// starts and ends at the right level.
    ///
    /// A day is a window onto one continuous timeline, and the chart for it
    /// draws only this part: an evening that runs past the five o'clock
    /// boundary is cut there and continues on the next day's page. Samples
    /// outside the window are dropped, not zeroed — the level at the edge
    /// is whatever the curve says it is.
    public func clipped(to window: ClosedRange<Date>) -> BACCurve {
        guard let first = samples.first, let last = samples.last,
              first.date <= window.upperBound, last.date >= window.lowerBound
        else { return BACCurve(samples: [], startedAt: window.lowerBound) }

        var inside = samples.filter { window.contains($0.date) }
        if first.date < window.lowerBound {
            let edge = BACSample(date: window.lowerBound, bac: value(at: window.lowerBound), rate: rate(at: window.lowerBound))
            inside.insert(edge, at: 0)
        }
        if last.date > window.upperBound {
            let edge = BACSample(date: window.upperBound, bac: value(at: window.upperBound), rate: rate(at: window.upperBound))
            inside.append(edge)
        }
        return BACCurve(samples: inside, startedAt: inside.first?.date ?? window.lowerBound)
    }

    /// The rate of the last sample at or before `date` — a step, not an
    /// interpolation, which is what the rising badge reads anyway.
    public func rate(at date: Date) -> Double {
        samples.last { $0.date <= date }?.rate ?? 0
    }

    /// Several curves that do not overlap in time, as one.
    ///
    /// Occasions are cut where the body has cleared, so two of them never
    /// overlap and the samples simply follow one another; between them the
    /// level is zero on both sides, and interpolation across the gap stays at
    /// zero. The caller guarantees the non-overlap — this only sorts.
    public static func joined(_ curves: [BACCurve]) -> BACCurve {
        let ordered = curves.filter { !$0.samples.isEmpty }.sorted { $0.startedAt < $1.startedAt }
        guard let first = ordered.first else {
            return BACCurve(samples: [], startedAt: curves.first?.startedAt ?? Date())
        }
        return BACCurve(samples: ordered.flatMap(\.samples), startedAt: first.startedAt)
    }

    /// The first time the curve reaches the given limit.
    public func firstCrossing(of limit: Double) -> Date? {
        samples.first { $0.bac >= limit }?.date
    }

    /// How long the level stays above the given limit.
    public func duration(above limit: Double) -> TimeInterval {
        let above = samples.filter { $0.bac >= limit }
        guard let first = above.first, let last = above.last else { return 0 }
        return last.date.timeIntervalSince(first.date)
    }
}

/// One-compartment pharmacokinetic model with a separate gut compartment per drink.
///
/// ```
/// dGᵢ/dt = -kaᵢ · Gᵢ
/// dC/dt  = (Σᵢ kaᵢ · Gᵢ) / Vd − β · C / (Km + C)
/// ```
///
/// Integrated with RK4, because the saturable elimination term makes a plain
/// Euler step noticeably underestimate at low concentrations.
///
/// The type is deliberately a pure value and free of UI concerns: SwiftData
/// `@Model` classes call into this, never the other way round.
public struct BACEngine: Sendable {

    /// Bumped whenever a change to the model would alter the numbers it
    /// produces for the same inputs.
    ///
    /// Stored summaries carry the version they were computed with, so a model
    /// improvement invalidates them instead of silently leaving stale figures
    /// in the history. Do not bump it for refactors that keep the output
    /// identical — that would needlessly recompute every past session.
    public static let version = 3

    /// Integration step in minutes.
    public var stepMinutes: Double
    /// Sampling interval in minutes.
    public var sampleEveryMinutes: Double
    /// Safety cap on the simulated span, in minutes.
    ///
    /// The simulation stops on its own once the body has cleared, so this is
    /// not how long a curve is — it is how long one is *allowed* to be before
    /// the loop gives up. It was 24 hours from the first drink, which sounds
    /// generous and is not: ten half-litre beers between 17:00 and midnight
    /// clear around 16:00 the next day, and anything heavier ran past the
    /// cap, lost its sober time, and was closed as if it had cleared. Three
    /// days covers any evening a person survives; a curve that reaches it is
    /// reported through `BACCurve.hasCleared`, never silently truncated.
    public var horizonMinutes: Double

    public static let defaultHorizonMinutes: Double = 72 * 60

    public init(
        stepMinutes: Double = 0.25,
        sampleEveryMinutes: Double = 1,
        horizonMinutes: Double = BACEngine.defaultHorizonMinutes
    ) {
        self.stepMinutes = stepMinutes
        self.sampleEveryMinutes = sampleEveryMinutes
        self.horizonMinutes = horizonMinutes
    }

    public func simulate(profile: BodyProfile, drinks: [Drink], from origin: Date? = nil) -> BACCurve {
        let ordered = drinks.sorted { $0.consumedAt < $1.consumedAt }
        guard let start = origin ?? ordered.first?.consumedAt else {
            return BACCurve(samples: [], startedAt: Date())
        }

        let vd = profile.distributionVolume
        let betaPerMinute = profile.beta / 60
        let km = Physiology.michaelisConstant

        let offsets = ordered.map { $0.consumedAt.timeIntervalSince(start) / 60 }
        let durations = ordered.map(\.drinkingMinutes)
        let ka = ordered.map(\.stomach.absorptionRatePerMinute)
        let doses = ordered.map(\.absorbedGrams)

        var gut = [Double](repeating: 0, count: ordered.count)
        // Only instantaneous drinks wait to be deposited; the rest flow in.
        var pending = Set(ordered.indices.filter { durations[$0] <= 0 })
        var concentration = 0.0

        /// Zero-order flow into the stomach while a drink is being consumed.
        func intakeRate(_ i: Int, _ t: Double) -> Double {
            guard durations[i] > 0 else { return 0 }   // a bolus, deposited on arrival
            guard t >= offsets[i], t < offsets[i] + durations[i] else { return 0 }
            return doses[i] / durations[i]
        }

        /// Derivatives of the gut compartments and the central concentration.
        func derivatives(_ gutState: [Double], _ c: Double, _ t: Double) -> ([Double], Double) {
            var dGut = [Double](repeating: 0, count: gutState.count)
            var influx = 0.0
            for i in gutState.indices {
                let flow = ka[i] * gutState[i]
                dGut[i] = intakeRate(i, t) - flow
                influx += flow
            }
            let elimination = c > 0 ? betaPerMinute * c / (km + c) : 0
            return (dGut, influx / vd - elimination)
        }

        var samples: [BACSample] = []
        var t = 0.0
        var nextSample = 0.0
        let dt = stepMinutes

        while t <= horizonMinutes + 1e-9 {
            // drinks downed in one go enter the stomach whole
            let arrived = pending.filter { offsets[$0] <= t + 1e-9 }
            for i in arrived {
                gut[i] += doses[i]
                pending.remove(i)
            }

            if t >= nextSample - 1e-9 {
                let (_, rate) = derivatives(gut, concentration, t)
                samples.append(BACSample(
                    date: start.addingTimeInterval(t * 60),
                    bac: max(concentration, 0),
                    rate: rate * 60
                ))
                nextSample += sampleEveryMinutes
            }

            let (k1g, k1c) = derivatives(gut, concentration, t)
            let g2 = zip(gut, k1g).map { $0 + 0.5 * dt * $1 }
            let (k2g, k2c) = derivatives(g2, concentration + 0.5 * dt * k1c, t + 0.5 * dt)
            let g3 = zip(gut, k2g).map { $0 + 0.5 * dt * $1 }
            let (k3g, k3c) = derivatives(g3, concentration + 0.5 * dt * k2c, t + 0.5 * dt)
            let g4 = zip(gut, k3g).map { $0 + dt * $1 }
            let (k4g, k4c) = derivatives(g4, concentration + dt * k3c, t + dt)

            for i in gut.indices {
                gut[i] = max(gut[i] + dt / 6 * (k1g[i] + 2 * k2g[i] + 2 * k3g[i] + k4g[i]), 0)
            }
            concentration = max(concentration + dt / 6 * (k1c + 2 * k2c + 2 * k3c + k4c), 0)
            t += dt

            // early exit once nothing is left to pour, absorb or eliminate
            let stillPouring = ordered.indices.contains { t < offsets[$0] + durations[$0] }
            if concentration <= 1e-6, pending.isEmpty, !stillPouring,
               gut.allSatisfy({ $0 <= 1e-9 }), t > 1 {
                samples.append(BACSample(date: start.addingTimeInterval(t * 60), bac: 0, rate: 0))
                break
            }
        }

        return BACCurve(samples: samples, startedAt: start)
    }
}
