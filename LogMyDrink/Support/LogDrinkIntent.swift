import AppIntents
import BACKit

/// "Log a drink", as an action the system can run without the app's interface:
/// from Siri, from the Shortcuts app, from Spotlight, and — once the widget
/// target exists — from a widget button.
///
/// It is the quick-add button with no screen in front of it. Everything goes
/// through `SessionStore.quickAdd`, so the favourite, the pour cut (5.13) and
/// the session routing apply unchanged; the intent adds nothing of its own.
///
/// **What Siri says back is the projection, not just a confirmation.** The app
/// exists because the decision is made before the drink is poured (2.), and a
/// voice command has no capsule to carry the level colour — so the peak that
/// the drink would take you to is spoken instead. It is the same figure the
/// quick capsule gives VoiceOver.
///
/// Performed in the app's own process (`openAppWhenRun` is false): the system
/// launches the app in the background if it is not running, `LogMyDrinkApp`
/// registers the store as a dependency, and `perform` is main-actor isolated,
/// which is where the store lives.
struct LogDrinkIntent: AppIntent {

    static let title: LocalizedStringResource = "Log a drink"
    static let description = IntentDescription("Logs your usual drink, right now, without opening the app.")
    static let openAppWhenRun = false

    @Dependency
    private var store: SessionStore

    @MainActor
    func perform() async throws -> some IntentResult & ProvidesDialog {
        // The app may have sat in the background for hours: the clock only
        // ticks while the Live screen is up, and a session left open
        // overnight is closed on refresh, not on its own. Both are what the
        // foreground transition does, and this is one.
        store.tick()
        store.refreshFromStore()

        guard let offer = store.quickAddOffer else {
            return .result(dialog: "There is no usual drink yet. Log one in the app first, and it will be remembered.")
        }

        // Asked before the add, so it is the same answer the capsule shows:
        // where this drink would take you, on top of what is already there.
        let projection = store.project(offer.drink)
        store.quickAdd()

        let name = String(localized: DrinkCatalog.name(for: offer.drink))
        let peak = store.unit.formatted(projection.peakRange.upperBound)

        switch projection.outcome {
        case .above:
            return .result(dialog: "\(name) logged. This takes you over your limit, to about \(peak).")
        case .uncertain:
            return .result(dialog: "\(name) logged. This may take you over your limit, peak around \(peak).")
        case .below:
            return .result(dialog: "\(name) logged. Peak around \(peak).")
        }
    }
}

/// The phrases Siri listens for, registered automatically on install — no
/// setup in the Shortcuts app.
///
/// Every phrase has to contain the app's name; Apple does not accept a bare
/// word. The app is named so that this constraint costs nothing: "LogMyDrink"
/// is both the name and the command, so the first phrase is the bare name.
/// The rest are the ways people naturally pad it. A personal shortcut named
/// "Drink" in the Shortcuts app still works for a shorter trigger — Siri runs
/// any shortcut by its name.
///
/// English only: Siri has no Hungarian, and the phrases follow the app's
/// source language (7.).
struct LogMyDrinkShortcuts: AppShortcutsProvider {

    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: LogDrinkIntent(),
            phrases: [
                "\(.applicationName)",
                "\(.applicationName) now",
                "Log a drink in \(.applicationName)",
                "Log my drink in \(.applicationName)",
            ],
            shortTitle: "Log a drink",
            systemImageName: "wineglass"
        )
    }

    static let shortcutTileColor: ShortcutTileColor = .teal
}
