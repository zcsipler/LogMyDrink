import Foundation
import Observation

/// What this *build* is provisioned for — as opposed to what the user has
/// bought, which is `FeatureFlags.isPro`.
///
/// A compile-time constant rather than a debug toggle: flipping a switch at
/// runtime cannot conjure an entitlement, and the store is opened once at
/// launch, before any switch could be read.
///
/// Not a `ProFeature`: sync is free (5.29). It carries data, not a view of
/// it — without Pro the history beyond seven days stays locked on every
/// device it syncs to — and a free user who changes phones keeps everything.
enum BuildCapabilities {

    /// Whether to open the store with CloudKit mirroring.
    ///
    /// **On since October 2026**, when the paid Apple Developer Program
    /// membership arrived and the target got its iCloud capability. With it
    /// off the app opens a local store and behaves exactly as it did before
    /// any of the sync work — nothing gated, nothing hidden,
    /// `LogMyDrinkApp.makeContainer` and the remote-change observer in
    /// `SessionStore` simply idle. Turning it on requires the iCloud
    /// capability on the target (a Personal Team cannot add it, and Xcode
    /// does not even list it). See 5.17 in CLAUDE.md for the checklist.
    static let cloudSync = true
}

/// What a Pro subscription unlocks.
///
/// There is one thing to buy — Pro — and this is the list of what it opens.
/// A new paid feature is a new case here and nothing else: the entitlement
/// is a single yes or no (`FeatureFlags.isPro`), so no feature can be
/// bought, trialled or lost on its own.
///
/// What is **not** here is free, and stays free: the Live screen, adding,
/// editing and deleting drinks, the last seven days of history, quick add
/// from the capsule, from Siri and from the widget's button, and iCloud
/// sync. Logging is what the app is for, and the paid side lives on what has
/// been logged.
enum ProFeature: String, CaseIterable, Identifiable {

    /// History beyond the free window: the week / month / year views, and
    /// the detail of any day older than `FeatureFlags.freeHistoryWindowDays`.
    ///
    /// Gates the *view*, never the record. Every session is stored for
    /// everyone, so subscribing later reveals the whole past, not only what
    /// was logged from that day on.
    case fullHistory

    /// Recording drinks for more than one person, and switching between them.
    case multiPerson

    /// The level, its direction and the coming crest on the widget. The
    /// button itself is free: without Pro the widget is the plain quick-add
    /// button it always was when nothing was on the curve.
    case widgetLevel

    /// Exporting a backup to a file, and importing one.
    ///
    /// Pro, unlike sync, because a file is a view of the data: an export
    /// holds every evening back to the first, readable by any spreadsheet,
    /// which would be the full history handed out for free in another app.
    case dataTransfer

    var id: String { rawValue }
}

/// Something built but not yet believed in: on the device it did not read
/// well, and it is kept off the menu until the concept has had another pass.
///
/// Not a `ProFeature`, because a Pro feature unlocks with the subscription
/// and would go on sale the day StoreKit lands. An experiment can only be
/// switched on by hand, in a debug build; in release it does not exist —
/// not for free users, not for Pro.
enum Experiment: String, CaseIterable, Identifiable {

    /// The Trend segment of the History screen: the whole recorded span on
    /// two scrolling, pinch-zoomable curves (`HistoryTrend`).
    case trendSegment

    var id: String { rawValue }

    var title: String {
        switch self {
        case .trendSegment: "Trend segment"
        }
    }
}

extension Notification.Name {

    /// Posted on the main actor when `FeatureFlags.isPro` flips. For whoever
    /// publishes outside SwiftUI's observation — the widget snapshot — and
    /// so has to be told rather than re-rendered.
    static let proEntitlementDidChange = Notification.Name("logmydrink.proEntitlementDidChange")
}

/// The one place that decides what is switched on.
///
/// The views ask, they never decide — `if flags.multiPerson`. When StoreKit
/// arrives, the entitlement lookup goes into `isSubscribed` and no view
/// changes.
///
/// What a flag must **not** gate is the schema. A model behind a flag would
/// need the same migration the moment the flag went on, and would hide
/// existing rows the moment it went off — two shapes of the database to keep
/// alive, for no gain. Migrations run for everyone; the flag hides UI (5.18).
@Observable
@MainActor
final class FeatureFlags {

    static let shared = FeatureFlags()

    private init() {
        #if DEBUG
        simulatesPro = UserDefaults.standard.bool(forKey: Self.simulatedProKey)
        experiments = Self.loadExperiments()
        // The per-feature overrides this replaced. Nothing reads them.
        UserDefaults.standard.removeObject(forKey: "logmydrink.featureFlags.debug.v1")
        #endif
    }

    // MARK: Pro

    /// Whether this user has Pro. One answer for every Pro feature.
    var isPro: Bool {
        #if DEBUG
        if simulatesPro { return true }
        #endif
        return isSubscribed
    }

    /// Asked by feature, although today every feature has the same answer,
    /// so that a call site says what it is gating — and so that a feature
    /// could one day move between free and Pro without touching the views.
    func isEnabled(_ feature: ProFeature) -> Bool {
        isPro
    }

    /// Named accessors, because `flags.multiPerson` reads better at a call
    /// site inside a view body than a lookup does.
    var fullHistory: Bool { isEnabled(.fullHistory) }
    var multiPerson: Bool { isEnabled(.multiPerson) }
    var widgetLevel: Bool { isEnabled(.widgetLevel) }
    var dataTransfer: Bool { isEnabled(.dataTransfer) }

    // MARK: Experiments

    /// Off unless switched on by hand in a debug build. There is no
    /// entitlement to fall through to: an experiment is not for sale.
    func isEnabled(_ experiment: Experiment) -> Bool {
        #if DEBUG
        return experiments[experiment] ?? false
        #else
        return false
        #endif
    }

    var trendSegment: Bool { isEnabled(.trendSegment) }

    // MARK: The free history window

    /// How many drinking days back, today included, history stays open
    /// without Pro. Seven: long enough to feel what the history is worth,
    /// short enough that after a few weeks there is visibly something behind
    /// the lock.
    nonisolated static let freeHistoryWindowDays = 7

    /// Whether this day's history may be shown in full.
    ///
    /// The one question a history view asks. Today is always inside the window
    /// — the current day is the Live screen's territory and is never gated.
    func canShowHistory(for day: DrinkingDay, at now: Date = .now) -> Bool {
        fullHistory || Self.isWithinFreeWindow(day, at: now)
    }

    /// The window rule on its own, without the entitlement, so it can be
    /// tested without touching the shared flags. `nonisolated` because it is
    /// pure arithmetic on dates and `HistoryWindow`, a plain value type,
    /// calls it from wherever it happens to be built.
    nonisolated static func isWithinFreeWindow(
        _ day: DrinkingDay,
        at now: Date = .now,
        calendar: Calendar = .current
    ) -> Bool {
        day.daysAgo(from: now, calendar: calendar) < freeHistoryWindowDays
    }

    // MARK: Entitlement
    //
    // Always false: nothing can be bought yet. When StoreKit lands this
    // becomes the subscription's state (a one-month free trial included), it
    // posts `proEntitlementDidChange` when it flips, and nothing else in this
    // file changes.

    private var isSubscribed: Bool { false }

    // MARK: Debug
    //
    // Debug builds only. One switch, the way a user sees it: Pro or not. A
    // release build must not carry a switch that hands out Pro.

    #if DEBUG
    private static let simulatedProKey = "logmydrink.pro.debug.simulated"

    private(set) var simulatesPro = false

    func setSimulatesPro(_ value: Bool) {
        let wasPro = isPro
        simulatesPro = value
        UserDefaults.standard.set(value, forKey: Self.simulatedProKey)
        if isPro != wasPro {
            NotificationCenter.default.post(name: .proEntitlementDidChange, object: self)
        }
    }

    private static let experimentsKey = "logmydrink.experiments.debug.v1"

    private var experiments: [Experiment: Bool] = [:]

    func setEnabled(_ value: Bool, for experiment: Experiment) {
        experiments[experiment] = value
        let raw = Dictionary(uniqueKeysWithValues: experiments.map { ($0.key.rawValue, $0.value) })
        UserDefaults.standard.set(raw, forKey: Self.experimentsKey)
    }

    private static func loadExperiments() -> [Experiment: Bool] {
        let raw = UserDefaults.standard.dictionary(forKey: experimentsKey) as? [String: Bool] ?? [:]
        return raw.reduce(into: [:]) { result, pair in
            guard let experiment = Experiment(rawValue: pair.key) else { return }
            result[experiment] = pair.value
        }
    }
    #endif
}
