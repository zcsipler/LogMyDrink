import Foundation
import WidgetKit

/// What the app tells its widget.
///
/// The widget runs in its own process and cannot see the store, so the little
/// it needs is published into the App Group's shared `UserDefaults`: today,
/// the favourite drink's icon, so that the button shows the beer that will be
/// logged rather than a generic glass. Deliberately not the store itself —
/// moving the database into the App Group container is the step that would
/// let the widget write and draw the curve, and it migrates every existing
/// record, so it is a round of its own (12.).
///
/// Requires the App Groups capability on **both** targets with the group
/// below. Without it `UserDefaults(suiteName:)` still returns an object, but
/// a private one: nothing is shared, nothing crashes, and the widget keeps its
/// default icon — which is how it should degrade.
///
/// The widget target compiles its own copy of the group and key names
/// (`DrinkSmartWidget/DrinkSmartWidget.swift`); the two must agree.
enum WidgetBridge {

    static let appGroup = "group.dev.zcsipler.drinksmart"

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
        WidgetCenter.shared.reloadAllTimelines()
    }
}
