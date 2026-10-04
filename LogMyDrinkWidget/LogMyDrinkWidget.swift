import SwiftUI
import WidgetKit

/// One button: log the usual drink.
///
/// Meant for the Lock Screen (`accessoryCircular`, `accessoryRectangular`),
/// where it is the shortest path there is — the phone is picked up and the
/// button is already on screen, before Face ID. The Home Screen size is the
/// same button, larger.
///
/// The tap opens the app on Live and logs the drink there, through
/// `QuickAddLink`. Nothing is written from this process: the widget has no
/// access to the store, and the app's own screen is where the Undo strip is.
/// So this widget shows no count and no level either. The one thing it does
/// know is the favourite's icon, published by the app into the App Group's
/// shared defaults (`WidgetBridge`); the store itself staying in the app is
/// what keeps this a prototype, and moving it is the next step, not this one.
struct QuickAddWidget: Widget {

    static let kind = "dev.zcsipler.logmydrink.quickadd"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: Self.kind, provider: Provider()) { entry in
            QuickAddWidgetView(icon: entry.icon)
                .widgetURL(QuickAddWidget.link)
        }
        .configurationDisplayName("Log My Drink")
        .description("Logs your usual drink with one tap.")
        .supportedFamilies([.accessoryCircular, .accessoryRectangular, .systemSmall])
    }

    /// Must match `QuickAddLink.url` in the app target. Duplicated rather
    /// than shared, so that this target compiles without touching the app's
    /// file memberships.
    static let link = URL(string: "logmydrink://quick-add")!

    /// Nothing changes with time; the one thing that changes is the
    /// favourite, and the app asks for a reload when it does
    /// (`WidgetBridge`). So: one entry, never refreshed on a schedule.
    struct Provider: TimelineProvider {
        struct Entry: TimelineEntry {
            let date: Date
            /// The favourite's SF Symbol, or the generic glass when the app
            /// has not published one (no favourite yet, or no App Group).
            let icon: String
        }

        func placeholder(in context: Context) -> Entry { Entry(date: .now, icon: Self.defaultIcon) }

        func getSnapshot(in context: Context, completion: @escaping (Entry) -> Void) {
            completion(Entry(date: .now, icon: Self.currentIcon))
        }

        func getTimeline(in context: Context, completion: @escaping (Timeline<Entry>) -> Void) {
            completion(Timeline(entries: [Entry(date: .now, icon: Self.currentIcon)], policy: .never))
        }

        static let defaultIcon = "wineglass"

        /// Must match `WidgetBridge` in the app target.
        static let appGroup = "group.dev.zcsipler.logmydrink"
        static let favouriteIconKey = "widget.favourite.icon"

        static var currentIcon: String {
            UserDefaults(suiteName: appGroup)?.string(forKey: favouriteIconKey) ?? defaultIcon
        }
    }
}

struct QuickAddWidgetView: View {
    @Environment(\.widgetFamily) private var family

    /// The favourite's icon: the button shows the beer it will log, not a
    /// glass in general. The circular size keeps the plus — at that size the
    /// drink would not read, and the plus says what the tap does.
    let icon: String

    var body: some View {
        switch family {
        case .accessoryCircular:
            ZStack {
                AccessoryWidgetBackground()
                Image(systemName: "plus")
                    .font(.system(size: 22, weight: .bold))
            }
            .containerBackground(.clear, for: .widget)

        case .accessoryRectangular:
            HStack(spacing: 8) {
                Image(systemName: icon)
                    .font(.system(size: 20, weight: .semibold))
                VStack(alignment: .leading, spacing: 1) {
                    Text(verbatim: "Log My Drink")
                        .font(.headline)
                    Text("Your usual, one tap")
                        .font(.caption)
                        .opacity(0.8)
                }
                Spacer(minLength: 0)
            }
            .containerBackground(.clear, for: .widget)

        default:
            VStack(spacing: 10) {
                Image(systemName: icon)
                    .font(.system(size: 30, weight: .semibold))
                Text(verbatim: "Log My Drink")
                    .font(.system(size: 15, weight: .semibold, design: .rounded))
            }
            .foregroundStyle(.white)
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .containerBackground(Color(red: 0.11, green: 0.61, blue: 0.58), for: .widget)
        }
    }
}

#Preview("Lock Screen", as: .accessoryRectangular) {
    QuickAddWidget()
} timeline: {
    QuickAddWidget.Provider.Entry(date: .now, icon: "mug.fill")
}
