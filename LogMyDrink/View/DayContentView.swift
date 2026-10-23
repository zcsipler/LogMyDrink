import SwiftUI
import BACKit

/// One drinking day, drawn as a window onto the timeline: the curve of
/// everything that was in the blood between five in the morning and five
/// the next, the day's figures, and the drinks had on it.
///
/// Shared by the Live screen (today) and the History day page (any day), so
/// a day looks the same wherever you reach it from. Not an occasion: a night
/// that ran past the boundary is cut at the edge here and continues on the
/// next day's page, starting at the level it left behind. `SessionContentView`
/// still draws a single occasion for the history list's detail.
struct DayContentView: View {
    let model: BACChartModel
    let store: SessionStore

    /// Set when the user taps a drink to correct it.
    @Binding var editingDrink: Drink?
    @Binding var openRowID: UUID?

    private var drinks: [Drink] { model.drinks }

    var body: some View {
        VStack(spacing: 26) {
            BACChartView(model: model)
            statRow
            if !drinks.isEmpty {
                DrinkListSection(
                    drinks: drinks,
                    openRowID: $openRowID,
                    onEdit: { editingDrink = $0 },
                    onDelete: { drink in withAnimation { store.remove(drink) } }
                )
            }
        }
    }

    // MARK: Stats

    /// The day's drinks in the first row; in the second, the occasion the
    /// day belongs to, told whole: when it began, when it clears, how long
    /// that is, and on a running evening how long is still to go.
    ///
    /// The occasion, not the day (5.22): a heavy night that runs on into the
    /// next afternoon kept someone from being sober the whole time, and both
    /// days say so — the start and the clearing time carry a caption when
    /// they fall on another day ("previous day", "2 days later"), and the
    /// duration may run past a day. The truth, however it reads. One time
    /// each, from the centre curve: the uncertainty is the chart's band, and
    /// as a range here it was unreadable.
    private var statRow: some View {
        VStack(spacing: 12) {
            HStack(alignment: .center, spacing: 0) {
                if let start = model.occasionStart {
                    stat("Started", Text(verbatim: start.hourMinute), under: dayCaption(for: start))
                } else {
                    stat("Started", Text(verbatim: "—"))
                }
                divider
                stat("Drinks", Text(verbatim: drinks.count.formatted()))
                divider
                stat(store.amountFormat.shortLabel, Text(verbatim: store.amountFormat.format(standardUnits: totalUnits)))
                divider
                // The same figure the week, month and year cards add up
                // (5.24), so a day reads against them.
                stat("Calories", Text(verbatim: "\(kilocalories.formatted(.number.precision(.fractionLength(0)))) kcal"))
            }

            if let sober = model.soberAt {
                Divider().overlay(Theme.hairline).padding(.horizontal, 14)

                HStack(alignment: .center, spacing: 0) {
                    if sober <= (model.focusDate ?? .now) {
                        stat("Sober at", Text(verbatim: sober.hourMinute), under: dayCaption(for: sober))
                    } else {
                        stat("Sober around", Text(verbatim: sober.hourMinute), under: dayCaption(for: sober))
                    }
                    if let start = model.occasionStart {
                        divider
                        stat("Duration", Text(verbatim: sober.timeIntervalSince(start).spanDuration))
                    }
                    if model.isLive, model.currentBAC > 0, let now = model.focusDate, sober > now {
                        divider
                        stat("Remaining", Text(verbatim: sober.timeIntervalSince(now).spanDuration))
                    }
                }
            }
        }
        .padding(.vertical, 14)
        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 16))
    }

    /// Which day a time falls on, said against the day on screen — nothing
    /// when it is the same drinking day.
    private func dayCaption(for date: Date) -> String? {
        guard let window = model.window else { return nil }
        let shown = DrinkingDay.containing(window.lowerBound)
        let other = DrinkingDay.containing(date)
        let days = Calendar.current.dateComponents([.day], from: shown.start, to: other.start).day ?? 0
        switch days {
        case 0: return nil
        case 1: return String(localized: "next day")
        case -1: return String(localized: "previous day")
        case 2...: return String(localized: "\(days.formatted()) days later")
        default: return String(localized: "\((-days).formatted()) days earlier")
        }
    }

    private var totalUnits: Double {
        drinks.reduce(0) { $0 + $1.standardUnits }
    }

    private var kilocalories: Double {
        drinks.reduce(0) { $0 + DrinkCatalog.kilocalories(for: $1) }
    }

    private var divider: some View {
        Rectangle()
            .fill(Theme.hairline)
            .frame(width: 1, height: 26)
    }

    private func stat(_ title: LocalizedStringResource, _ value: Text, under: String? = nil) -> some View {
        VStack(spacing: 4) {
            Text(title)
                .font(.system(size: 9, weight: .semibold, design: .rounded))
                .textCase(.uppercase)
                .foregroundStyle(Theme.secondaryText)
                .lineLimit(1)
                .minimumScaleFactor(0.8)
            value
                .font(.system(size: 15, weight: .medium, design: .rounded).monospacedDigit())
                .foregroundStyle(Theme.primaryText)
                .lineLimit(1)
                .minimumScaleFactor(0.7)
            if let under {
                Text(verbatim: under)
                    .font(.system(size: 10, design: .rounded))
                    .foregroundStyle(Theme.calm)
                    .lineLimit(1)
                    .minimumScaleFactor(0.8)
            }
        }
        .frame(maxWidth: .infinity)
        .padding(.horizontal, 4)
    }
}
