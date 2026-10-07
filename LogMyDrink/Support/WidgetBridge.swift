import Foundation
import WidgetKit

/// What the app tells its widget.
///
/// The widget runs in its own process and cannot see the store, so the little
/// it needs is published into the App Group's shared `UserDefaults`: the
/// favourite drink's icon, so that the button shows the beer that will be
/// logged rather than a generic glass, and a `WidgetSnapshot` of the open
/// occasion — the simulated band and the evening's totals — so that the Lock
/// Screen can show the level and where it is heading. Deliberately not the
/// store itself: moving the database into the App Group container is the step
/// that would let the widget *write*, and it migrates every existing record,
/// so it is a round of its own (12.). Reading needs none of that: the app has
/// already computed everything the widget could show.
///
/// Requires the App Groups capability on **both** targets with the group
/// below. Without it `UserDefaults(suiteName:)` still returns an object, but
/// a private one: nothing is shared, nothing crashes, and the widget keeps its
/// default icon — which is how it should degrade.
///
/// The widget target compiles its own copy of the group and key names
/// (`LogMyDrinkWidget/LogMyDrinkWidget.swift`); the two must agree.
enum WidgetBridge {

    static let appGroup = "group.dev.zcsipler.logmydrink"

    /// Must match `QuickAddWidget.kind` in the widget target. Reloading by
    /// kind rather than everything: a reload is a *request* WidgetKit
    /// schedules against a daily budget and coalesces, so the less it is
    /// asked to redraw, the sooner the one widget that matters gets its turn.
    static let widgetKind = "dev.zcsipler.logmydrink.quickadd"

    /// The SF Symbol of the favourite, or absent when there is no favourite.
    static let favouriteIconKey = "widget.favourite.icon"

    /// Publishes the active person's favourite and asks the widget to redraw.
    ///
    /// Called wherever the favourite can change from the widget's point of
    /// view: when it is set, and when the active person changes — the
    /// widget shows whoever's drink would be logged, which is the same rule
    /// the quick capsule follows.
    static func publish(favourite: FavouriteDrink?) {
        guard let shared = UserDefaults(suiteName: appGroup) else { return }

        let icon = favourite?.template.icon
        guard shared.string(forKey: favouriteIconKey) != icon else { return }

        shared.set(icon, forKey: favouriteIconKey)
        WidgetCenter.shared.reloadTimelines(ofKind: widgetKind)
    }

    /// The open occasion as JSON, or an empty snapshot when there is none.
    static let snapshotKey = "widget.snapshot"

    /// Publishes the band and asks the widget to rebuild its timeline.
    ///
    /// Called from every `rebuild()` — each write ends there — and from the
    /// setters that change how the same curve is *read* (limit, units).
    /// Compared byte for byte before writing: a reload is budgeted by
    /// WidgetKit, and most refreshes change nothing the widget shows.
    static func publish(snapshot: WidgetSnapshot) {
        guard let shared = UserDefaults(suiteName: appGroup) else { return }
        // Sorted keys so that equal snapshots are equal bytes; without it
        // the comparison below would depend on the encoder's key order.
        let encoder = JSONEncoder()
        encoder.outputFormatting = .sortedKeys
        guard let data = try? encoder.encode(snapshot) else { return }
        guard shared.data(forKey: snapshotKey) != data else { return }

        shared.set(data, forKey: snapshotKey)
        WidgetCenter.shared.reloadTimelines(ofKind: widgetKind)
    }
}
