import Foundation

/// The link a widget opens the app with to log the usual drink.
///
/// A widget button could run `LogDrinkIntent` in place, but a widget
/// extension is its own process, and for it to write a drink the SwiftData
/// store would have to move into an App Group container — which relocates
/// every existing record on every installed device. Not a change to make for
/// a prototype. Opening the app instead costs one screen transition and gains
/// the one thing an in-place add cannot show: the strip with Undo and the
/// stomach correction, right after a tap that asked no questions.
///
/// No URL scheme needs registering: a `widgetURL` is delivered straight to
/// the containing app's `onOpenURL`.
///
/// The widget target compiles its own copy of this string
/// (`DrinkSmartWidget/DrinkSmartWidget.swift`); the two must agree.
enum QuickAddLink {

    static let url = URL(string: "drinksmart://quick-add")!

    static func matches(_ url: URL) -> Bool {
        url.scheme == Self.url.scheme && url.host == Self.url.host
    }
}

/// A quick add asked for from outside the Live screen. Identified, so that
/// two taps on the widget are two drinks.
struct QuickAddRequest: Equatable {
    let id = UUID()
}
