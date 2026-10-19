import Foundation
import SwiftUI

/// A feature the user would not find on their own, offered once a day at
/// launch until it is used or turned down.
///
/// The order is the order they are offered in: the favourite first, because
/// the widget and Siri both log it; then the two ways to log without opening
/// the app; then History, once there is a week of it to look at.
enum FeatureTip: String, CaseIterable, Identifiable {
    case favourite
    case widget
    case siri
    case history

    var id: String { rawValue }

    var icon: String {
        switch self {
        case .favourite: "star"
        case .widget: "rectangle.on.rectangle"
        case .siri: "mic"
        case .history: "calendar"
        }
    }

    var title: LocalizedStringResource {
        switch self {
        case .favourite: "One tap and done"
        case .widget: "Your favourite from the Lock Screen"
        case .siri: "Say it, don’t type it"
        case .history: "See your patterns"
        }
    }

    var message: LocalizedStringResource {
        switch self {
        case .favourite: "Set what you drink most often and log it with a single tap."
        case .widget: "One tap on the widget logs your favourite, no searching for the app. In the evening it shows your level too."
        case .siri: "“Hey Siri, LogMyDrink now” — Siri logs your favourite and tells you where your peak is heading."
        case .history: "History shows how much and how high you drink over weeks, months and years, and which way it is changing."
        }
    }

    var actionTitle: LocalizedStringResource {
        switch self {
        case .favourite: "Set favourite"
        case .widget: "Add widget"
        case .siri: "Got it"
        case .history: "Open History"
        }
    }
}

/// What the app knows about the user when it decides whether to offer a tip.
/// A value, so the decision is a pure function and can be tested.
struct TipContext {
    var hasFavourite: Bool
    var widgetInstalled: Bool
    var siriUsed: Bool
    var historyOpened: Bool
    /// Whole days since tracking started.
    var trackedDays: Int
    /// Alcohol in the blood right now, by the estimate.
    var hasAlcohol: Bool
}

/// The tips' memory, in this device's defaults: which were turned down,
/// when one was last shown, and the two facts the app cannot read back from
/// anywhere else (Siri was used, History was opened).
///
/// Per device, not per person and not synced: a widget is on this phone's
/// Lock Screen, and a tip seen on one device is worth seeing on another.
struct TipLedger {
    let defaults: UserDefaults
    var calendar: Calendar = .current

    init(defaults: UserDefaults = .standard, calendar: Calendar = .current) {
        self.defaults = defaults
        self.calendar = calendar
    }

    private enum Key {
        static let enabled = "logmydrink.tips.enabled"
        static let dismissed = "logmydrink.tips.dismissed"
        static let lastShown = "logmydrink.tips.lastShown"
        static let firstSeen = "logmydrink.tips.firstSeen"
        static let siriUsed = "logmydrink.tips.siriUsed"
        static let historyOpened = "logmydrink.tips.historyOpened"
    }

    /// The Profile switch. On unless turned off.
    static let enabledKey = Key.enabled

    var isEnabled: Bool {
        defaults.object(forKey: Key.enabled) as? Bool ?? true
    }

    var siriUsed: Bool { defaults.bool(forKey: Key.siriUsed) }
    var historyOpened: Bool { defaults.bool(forKey: Key.historyOpened) }

    func markSiriUsed() { defaults.set(true, forKey: Key.siriUsed) }
    func markHistoryOpened() { defaults.set(true, forKey: Key.historyOpened) }

    func isDismissed(_ tip: FeatureTip) -> Bool {
        dismissed.contains(tip.rawValue)
    }

    /// "Don't show again": this tip only, for good.
    func dismiss(_ tip: FeatureTip) {
        defaults.set(Array(dismissed.union([tip.rawValue])).sorted(), forKey: Key.dismissed)
    }

    /// Debug only: every tip back, as on a fresh install a day later.
    func reset() {
        for key in [Key.dismissed, Key.lastShown, Key.siriUsed, Key.historyOpened] {
            defaults.removeObject(forKey: key)
        }
        defaults.set(Date.distantPast, forKey: Key.firstSeen)
    }

    func markShown(at date: Date) {
        defaults.set(date, forKey: Key.lastShown)
    }

    private var dismissed: Set<String> {
        Set(defaults.stringArray(forKey: Key.dismissed) ?? [])
    }

    /// The tip to offer now, or nil.
    ///
    /// Nothing on the first day the app is opened — the user has not seen
    /// the app itself yet, and a tip about a widget for it is out of order.
    /// Nothing while there is alcohol in the blood: that is when the app is
    /// opened to log a drink, and a sheet over Live then stands between the
    /// user and the one thing they came for. At most one a day.
    func next(_ context: TipContext, now: Date) -> FeatureTip? {
        guard isEnabled, !context.hasAlcohol else { return nil }

        let firstSeen = defaults.object(forKey: Key.firstSeen) as? Date ?? {
            defaults.set(now, forKey: Key.firstSeen)
            return now
        }()
        if calendar.isDate(firstSeen, inSameDayAs: now) { return nil }

        if let last = defaults.object(forKey: Key.lastShown) as? Date,
           calendar.isDate(last, inSameDayAs: now) {
            return nil
        }

        return FeatureTip.allCases.first { tip in
            !isDismissed(tip) && Self.isRelevant(tip, context)
        }
    }

    /// Whether the tip still has something to say. A tip whose feature is
    /// already in use drops out on its own, without anyone dismissing it.
    static func isRelevant(_ tip: FeatureTip, _ context: TipContext) -> Bool {
        switch tip {
        case .favourite: !context.hasFavourite
        case .widget: !context.widgetInstalled
        case .siri: !context.siriUsed
        case .history: context.trackedDays >= 7 && !context.historyOpened
        }
    }
}
