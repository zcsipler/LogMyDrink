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

    /// What was drunk on the day, and when it started. A day the night
    /// before ran into says so instead of a start time: its curve did not
    /// start here.
    private var statRow: some View {
        VStack(spacing: 12) {
            HStack(spacing: 0) {
                if let first = drinks.first {
                    stat("Started", Text(verbatim: first.consumedAt.hourMinute))
                } else {
                    // Only reached with a carried-in level: the view is not
                    // shown for a day with neither drinks nor a curve.
                    stat("Started", Text("Night before"))
                }
                divider
                stat("Drinks", Text(verbatim: drinks.count.formatted()))
                divider
                stat(store.amountUnit.shortLabel, Text(verbatim: store.amountUnit.format(standardUnits: totalUnits)))
            }

            if let sober = model.soberRange, model.isLive, model.currentBAC > 0 {
                Divider().overlay(Theme.hairline).padding(.horizontal, 14)

                VStack(spacing: 3) {
                    Text("Expected to clear")
                        .font(.system(size: 9, weight: .semibold, design: .rounded))
                        .textCase(.uppercase)
                        .foregroundStyle(Theme.secondaryText)
                    Text(verbatim: sober.hourMinuteRange)
                        .font(.system(size: 17, weight: .medium, design: .rounded).monospacedDigit())
                        .foregroundStyle(Theme.primaryText)
                }
            }
        }
        .padding(.vertical, 14)
        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 16))
    }

    private var totalUnits: Double {
        drinks.reduce(0) { $0 + $1.standardUnits }
    }

    private var divider: some View {
        Rectangle()
            .fill(Theme.hairline)
            .frame(width: 1, height: 26)
    }

    private func stat(_ title: LocalizedStringResource, _ value: Text) -> some View {
        VStack(spacing: 4) {
            Text(title)
                .font(.system(size: 9, weight: .semibold, design: .rounded))
                .textCase(.uppercase)
                .foregroundStyle(Theme.secondaryText)
            value
                .font(.system(size: 15, weight: .medium, design: .rounded).monospacedDigit())
                .foregroundStyle(Theme.primaryText)
        }
        .frame(maxWidth: .infinity)
    }
}
