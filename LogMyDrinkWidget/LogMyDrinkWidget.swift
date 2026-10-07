import SwiftUI
import WidgetKit

/// The button that logs the usual drink — and, while an occasion is open,
/// the one glance that says where the evening stands.
///
/// Meant for the Lock Screen (`accessoryCircular`, `accessoryRectangular`),
/// where it is the shortest path there is — the phone is picked up and the
/// button is already on screen, before Face ID. The Home Screen size is the
/// same, larger and in colour.
///
/// With nothing logged it is the plain button. With drinks on the curve it
/// stays the button — plus, icon, name — and adds, underneath, the level
/// now with an arrow for which limb of the curve this is, and, only while
/// it is still rising, the peak it is heading to and when.
/// All of it is read off the band the app published (`WidgetSnapshot`): the
/// widget simulates nothing, so it can never disagree with the Live screen. The timeline is one entry every
/// few minutes until the band clears — the number counts down through the
/// night without a reload, because the curve already knew the future.
///
/// The tap still opens the app on Live and logs the drink there, through
/// `QuickAddLink`. Nothing is written from this process: the widget has no
/// access to the store, and the app's own screen is where the Undo strip is.
struct QuickAddWidget: Widget {

    /// Must match `WidgetBridge.widgetKind` in the app target.
    static let kind = "dev.zcsipler.logmydrink.quickadd"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: Self.kind, provider: Provider()) { entry in
            QuickAddWidgetView(entry: entry)
                .widgetURL(QuickAddWidget.link)
        }
        .configurationDisplayName("Log My Drink")
        .description("Logs your usual drink with one tap, and shows where your evening stands.")
        .supportedFamilies([.accessoryCircular, .accessoryRectangular, .systemSmall])
    }

    /// Must match `QuickAddLink.url` in the app target. Duplicated rather
    /// than shared, so that this target compiles without touching the app's
    /// file memberships.
    static let link = URL(string: "logmydrink://quick-add")!

    struct Provider: TimelineProvider {
        struct Entry: TimelineEntry {
            let date: Date
            /// The favourite's SF Symbol, or the generic glass when the app
            /// has not published one (no favourite yet, or no App Group).
            let icon: String
            /// Nil: nothing on the curve — the plain button.
            let reading: Reading?
        }

        /// What one entry shows. Resolved here, once per entry, so the view
        /// is a layout and nothing else.
        struct Reading {
            let level: Double
            /// Already formatted: the view prints, it does not convert.
            let levelText: String
            let isRising: Bool
            /// The next crest ahead — range and time — while rising; nil
            /// once the curve only falls from here. The one figure a glance
            /// needs beyond the level: not where you are, but where this
            /// is going.
            let peakText: String?
            let peakAt: String?
            let limit: Double
            let unitSuffix: String

            init(snapshot: WidgetSnapshot, at date: Date) {
                level = snapshot.value(at: date)
                levelText = snapshot.formatLevel(level)
                limit = snapshot.limit
                unitSuffix = snapshot.unitSuffix

                // Rising means: the curve climbs from here to a crest that
                // prints as a different number. The *next* crest, not the
                // evening's highest — a drink logged on the way down turns
                // the curve back up to a lower crest, and that is where you
                // are heading now. Read off the curve's shape rather than a
                // stored slope: a first round used the thinned samples'
                // rate and never once said "rising".
                if let crest = snapshot.nextCrest(after: date),
                   snapshot.value(at: crest.date) - level >= 0.005 {
                    isRising = true
                    peakText = snapshot.formatLevelRange(crest.range)
                    peakAt = crest.date.formatted(date: .omitted, time: .shortened)
                } else {
                    isRising = false
                    peakText = nil
                    peakAt = nil
                }
            }
        }

        func placeholder(in context: Context) -> Entry {
            Entry(date: .now, icon: Self.defaultIcon, reading: nil)
        }

        func getSnapshot(in context: Context, completion: @escaping (Entry) -> Void) {
            let snapshot = WidgetSnapshot.load()
            completion(Entry(date: .now, icon: Self.currentIcon, reading: snapshot.map { Reading(snapshot: $0, at: .now) }))
        }

        /// One entry per step until the band clears, then the plain button.
        ///
        /// `.never`: the app reloads the timeline whenever the curve changes
        /// (`WidgetBridge`), and between those moments the future is already
        /// in the entries. After the last one there is nothing new to say.
        func getTimeline(in context: Context, completion: @escaping (Timeline<Entry>) -> Void) {
            let icon = Self.currentIcon
            let now = Date.now

            guard let snapshot = WidgetSnapshot.load() else {
                completion(Timeline(entries: [Entry(date: now, icon: icon, reading: nil)], policy: .never))
                return
            }

            // The band's late end is when the slowest plausible elimination
            // reaches zero; past it the evening is over as far as a glance is
            // concerned, and the button goes back to being a button.
            let end = snapshot.soberLate ?? snapshot.samples.last?.date ?? now
            var entries: [Entry] = []
            var date = now
            while date < end {
                entries.append(Entry(date: date, icon: icon, reading: Reading(snapshot: snapshot, at: date)))
                date = date.addingTimeInterval(Self.step)
            }
            entries.append(Entry(date: max(end, now), icon: icon, reading: nil))

            completion(Timeline(entries: entries, policy: .never))
        }

        /// Matches `WidgetSnapshot.sampleStep` on the app side: five minutes.
        static let step: TimeInterval = 5 * 60

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

    let entry: QuickAddWidget.Provider.Entry

    var body: some View {
        if let reading = entry.reading {
            switch family {
            case .accessoryCircular: circularReading(reading)
            case .accessoryRectangular: rectangularReading(reading)
            default: smallReading(reading)
            }
        } else {
            switch family {
            case .accessoryCircular: circularButton
            case .accessoryRectangular: rectangularButton
            default: smallButton
            }
        }
    }

    // MARK: The button, nothing logged

    /// The circular size keeps the plus — at that size the drink would not
    /// read, and the plus says what the tap does.
    private var circularButton: some View {
        ZStack {
            AccessoryWidgetBackground()
            Image(systemName: "plus")
                .font(.system(size: 22, weight: .bold))
        }
        .containerBackground(.clear, for: .widget)
    }

    private var rectangularButton: some View {
        HStack(spacing: 8) {
            Image(systemName: entry.icon)
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
    }

    private var smallButton: some View {
        VStack(spacing: 10) {
            Image(systemName: entry.icon)
                .font(.system(size: 30, weight: .semibold))
            Text(verbatim: "Log My Drink")
                .font(.system(size: 15, weight: .semibold, design: .rounded))
        }
        .foregroundStyle(.white)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .containerBackground(Color(red: 0.11, green: 0.61, blue: 0.58), for: .widget)
    }

    // MARK: The reading, an occasion open
    //
    // The button stays the button. A first round replaced it with figures —
    // level, destination, count, grams — and on the device the plus and the
    // name were gone, so nothing on the Lock Screen said what a tap would do;
    // a second round kept the header but still printed a "→ 0.00 · 03:40"
    // line on the way down, which answers nothing a glance asks. What is
    // left is what bears on the next pour: the level now, and — only while
    // it is still climbing — the peak it is climbing to. The circular size
    // shows no figure at all; the plus is the whole of it.
    //
    // No words anywhere in the figures: the Lock Screen renders them
    // monochrome and small, this target has no string catalog, and numbers,
    // symbols and times format themselves in the system language. The
    // arrow's direction is the whole of its meaning — colour would not
    // survive the Lock Screen, and a green arrow would be a verdict the app
    // does not give.
    //
    // `.privacySensitive()` on every figure: a Lock Screen is read by whoever
    // picks the phone up, so the numbers blur until the owner has unlocked.

    /// Direction of the limb, not a judgement.
    private func limbArrow(_ reading: Reading) -> some View {
        Image(systemName: reading.isRising ? "arrow.up.right" : "arrow.down.right")
    }

    /// "0,56 ‰ ↗"
    private func levelLine(_ reading: Reading, size: CGFloat) -> some View {
        HStack(alignment: .firstTextBaseline, spacing: 3) {
            Text(verbatim: reading.levelText)
                .font(.system(size: size, weight: .semibold, design: .rounded).monospacedDigit())
            Text(verbatim: reading.unitSuffix)
                .font(.system(size: size * 0.6, weight: .medium))
                .opacity(0.8)
            limbArrow(reading)
                .font(.system(size: size * 0.65, weight: .bold))
        }
    }

    /// "→ 0,71 ‰ · 21:40": the peak ahead. Only while rising; past the
    /// peak the line is absent rather than replaced.
    @ViewBuilder
    private func peakLine(_ reading: Reading) -> some View {
        if let peakText = reading.peakText, let peakAt = reading.peakAt {
            HStack(spacing: 3) {
                Image(systemName: "arrow.right")
                    .font(.system(size: 9, weight: .bold))
                Text(verbatim: "\(peakText) \(reading.unitSuffix)")
                Text(verbatim: "·").opacity(0.5)
                Text(verbatim: peakAt)
            }
            .monospacedDigit()
        }
    }

    /// The circle is the plus and nothing else, with or without drinks: at
    /// this size a figure under it crowded the one thing the tap promises.
    private func circularReading(_ reading: Reading) -> some View {
        circularButton
    }

    /// The button's own header, then the figures where its caption was.
    private func rectangularReading(_ reading: Reading) -> some View {
        HStack(spacing: 8) {
            Image(systemName: entry.icon)
                .font(.system(size: 20, weight: .semibold))
            VStack(alignment: .leading, spacing: 1) {
                Text(verbatim: "Log My Drink")
                    .font(.headline)
                levelLine(reading, size: 15)
                peakLine(reading)
                    .font(.caption)
                    .opacity(0.8)
            }
            .privacySensitive()
            Spacer(minLength: 0)
        }
        .lineLimit(1)
        .minimumScaleFactor(0.8)
        .containerBackground(.clear, for: .widget)
    }

    private func smallReading(_ reading: Reading) -> some View {
        let tint = WidgetTheme.tint(for: reading.level, limit: reading.limit)
        return VStack(alignment: .leading, spacing: 2) {
            HStack(spacing: 6) {
                Image(systemName: entry.icon)
                    .font(.system(size: 18, weight: .semibold))
                Text(verbatim: "Log My Drink")
                    .font(.system(size: 13, weight: .semibold, design: .rounded))
            }
            .foregroundStyle(.white)
            Spacer(minLength: 0)
            levelLine(reading, size: 28)
                .foregroundStyle(tint)
            peakLine(reading)
                .font(.system(size: 12, weight: .medium, design: .rounded))
                .foregroundStyle(.white.opacity(0.85))
        }
        .lineLimit(1)
        .minimumScaleFactor(0.8)
        .privacySensitive()
        .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .leading)
        .containerBackground(WidgetTheme.background, for: .widget)
    }
}

private typealias Reading = QuickAddWidget.Provider.Reading

#Preview("Lock Screen", as: .accessoryRectangular) {
    QuickAddWidget()
} timeline: {
    QuickAddWidget.Provider.Entry(date: .now, icon: "mug.fill", reading: nil)
}
