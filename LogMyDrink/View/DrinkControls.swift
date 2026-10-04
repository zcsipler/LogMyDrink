import SwiftUI
import BACKit

/// The controls that describe a drink: type, amount and strength, pace.
///
/// Extracted from `AddDrinkSheet` when the favourite editor needed the same
/// four. Two copies would mean that adding a drink type, or widening a slider,
/// has to be remembered in two places — and the one that gets forgotten is the
/// one nobody is looking at.
///
/// Stomach state and time are deliberately **not** here. They describe a
/// particular drink at a particular moment, which is the one thing a standing
/// favourite is not (see `FavouriteDrink`).

/// The label-and-value chrome every control sits in.
struct ControlSection<Content: View>: View {
    let title: LocalizedStringKey
    let trailing: String?
    let content: Content

    init(
        _ title: LocalizedStringKey,
        trailing: String? = nil,
        @ViewBuilder content: () -> Content
    ) {
        self.title = title
        self.trailing = trailing
        self.content = content()
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack {
                Text(title)
                    .font(.sectionLabel)
                    .textCase(.uppercase)
                    .foregroundStyle(Theme.secondaryText)
                Spacer()
                if let trailing {
                    Text(verbatim: trailing)
                        .font(.system(size: 12, weight: .medium, design: .rounded).monospacedDigit())
                        .foregroundStyle(Theme.primaryText)
                }
            }
            content
        }
    }
}

// MARK: - Type

struct DrinkTypePicker: View {
    @Binding var template: DrinkTemplate

    /// Picking a type replaces the values that belong to it. The caller owns
    /// them, so the caller applies them — this view does not reach into state
    /// it cannot see.
    let onSelect: (DrinkTemplate) -> Void

    var body: some View {
        ControlSection("Type") {
            LazyVGrid(columns: Array(repeating: GridItem(.flexible(), spacing: 10), count: 3), spacing: 10) {
                ForEach(DrinkCatalog.all) { item in
                    Button {
                        withAnimation(.easeOut(duration: 0.15)) {
                            template = item
                            onSelect(item)
                        }
                    } label: {
                        VStack(spacing: 7) {
                            Image(systemName: item.icon)
                                .font(.system(size: 18))
                            Text(item.name)
                                .font(.system(size: 12, weight: .medium, design: .rounded))
                                .lineLimit(1)
                                .minimumScaleFactor(0.8)
                        }
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 14)
                        .background(
                            template.id == item.id ? Theme.calm.opacity(0.18) : Theme.surface,
                            in: RoundedRectangle(cornerRadius: 14)
                        )
                        .overlay {
                            RoundedRectangle(cornerRadius: 14)
                                .stroke(template.id == item.id ? Theme.calm : Theme.hairline, lineWidth: 1)
                        }
                        .foregroundStyle(template.id == item.id ? Theme.calm : Theme.primaryText)
                    }
                    .buttonStyle(.plain)
                }
            }
        }
    }
}

// MARK: - Amount and strength
//
// Two steppers side by side, the way the time inputs are. Neither value is
// a choice from a list: a glass at home holds 220 ml, a keg is poured into
// whatever is to hand, a shot glass is filled three-quarters. There used to
// be preset chips and a slider for each; the chips said "pick one of these"
// about values that are not like that, and the slider could not be read or
// hit to ten millilitres. The step is the template's — 5 ml for spirits,
// 10 ml otherwise — and 0.5 % for strength. The footer under the pair is
// the one place the two numbers become a quantity of alcohol.

struct DrinkMeasureControls: View {
    let template: DrinkTemplate
    @Binding var volumeMl: Double
    @Binding var abv: Double

    static let volumeRange: ClosedRange<Double> = 10...1000
    static let abvStep: Double = 0.5

    private var grams: Double {
        volumeMl * (abv / 100) * Physiology.ethanolDensity
    }

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack(alignment: .top, spacing: 12) {
                ControlSection("Amount") {
                    TimeStepper(
                        canDecrement: volumeMl > Self.volumeRange.lowerBound,
                        canIncrement: volumeMl < Self.volumeRange.upperBound,
                        onStep: stepVolume,
                        value: { Text(verbatim: "\(volumeMl.formatted(.number.precision(.fractionLength(0)))) ml") }
                    )
                }
                .sensoryFeedback(.selection, trigger: volumeMl)

                ControlSection("Strength") {
                    TimeStepper(
                        canDecrement: abv > template.abvRange.lowerBound,
                        canIncrement: abv < template.abvRange.upperBound,
                        onStep: stepAbv,
                        value: { Text(verbatim: abv.formatted(.number.precision(.fractionLength(1))) + " %") }
                    )
                }
                .sensoryFeedback(.selection, trigger: abv)
            }

            HStack {
                Text("\((grams / Physiology.gramsPerStandardUnit).formatted(.number.precision(.fractionLength(1)))) units")
                Spacer()
                Text("\(grams.formatted(.number.precision(.fractionLength(0)))) g alcohol")
            }
            .font(.system(size: 11, design: .rounded))
            .foregroundStyle(Theme.secondaryText)
        }
    }

    private func stepVolume(_ direction: Int) {
        let next = StepGrid.snapped(volumeMl, step: template.volumeStepMl, stepping: direction)
        volumeMl = min(Self.volumeRange.upperBound, max(Self.volumeRange.lowerBound, next))
    }

    private func stepAbv(_ direction: Int) {
        let next = StepGrid.snapped(abv, step: Self.abvStep, stepping: direction)
        abv = min(template.abvRange.upperBound, max(template.abvRange.lowerBound, next))
    }
}

// MARK: - Pace
//
// Across an evening this barely moves the peak, but it roughly halves the rate
// of rise — and that is the number memory impairment tracks. A shot thrown back
// and a pint nursed for half an hour are not the same event, even when the
// alcohol is identical.

struct DrinkPaceControl: View {
    @Binding var drinkingMinutes: Double

    static let longestMinutes: Double = 180

    var body: some View {
        ControlSection("How fast") {
            VStack(alignment: .leading, spacing: 8) {
                TimeStepper(
                    canDecrement: drinkingMinutes > 0,
                    canIncrement: drinkingMinutes < Self.longestMinutes,
                    onStep: step,
                    value: { Text(verbatim: paceLabel) }
                )

                Text(explanation)
                    .font(.system(size: 11, design: .rounded))
                    .foregroundStyle(Theme.secondaryText)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .fixedSize(horizontal: false, vertical: true)
            }
        }
        .sensoryFeedback(.selection, trigger: drinkingMinutes)
    }

    private func step(_ direction: Int) {
        let next = StepGrid.snapped(drinkingMinutes, stepping: direction)
        drinkingMinutes = min(Self.longestMinutes, max(0, next))
    }

    private var paceLabel: String {
        drinkingMinutes <= 0
            ? String(localized: "In one go")
            : (drinkingMinutes * 60).compactDuration
    }

    private var explanation: LocalizedStringResource {
        switch drinkingMinutes {
        case 0: "Counts as a single swallow — the steepest possible rise."
        case ..<20: "A quick drink. The level climbs fast."
        case ..<45: "A normal pace."
        default: "Nursed slowly. Much gentler climb for the same alcohol."
        }
    }
}

// MARK: - Stepper
//
// The two time inputs — when the drink started and how long it took — used
// to be a chip row and a slider each. Chips read as a choice, but the useful
// values are a continuum, and the slider's precision is wasted on minutes. A
// stepper is the honest control for "a bit earlier": one tap is five minutes,
// holding runs, and the value in the middle is the state, not something to
// read back from a highlight. It is also half a row wide, which is what lets
// the two sit side by side.
//
// Constant step, accelerating repeat — not a step that grows with distance.
// A growing step changes under the finger and is asymmetric at its
// boundaries (fifty-five minutes reachable going out, not coming back); the
// repeat rate is what `UIStepper` does, so nobody has to learn it.

struct TimeStepper<Value: View>: View {
    let canDecrement: Bool
    let canIncrement: Bool

    /// Called with −1 or +1. The owner clamps and snaps (`StepGrid.snapped`).
    let onStep: (Int) -> Void

    /// Tapping the value, when it leads somewhere — the exact-time wheel.
    let onTapValue: (() -> Void)?

    let value: Value

    init(
        canDecrement: Bool,
        canIncrement: Bool,
        onStep: @escaping (Int) -> Void,
        onTapValue: (() -> Void)? = nil,
        @ViewBuilder value: () -> Value
    ) {
        self.canDecrement = canDecrement
        self.canIncrement = canIncrement
        self.onStep = onStep
        self.onTapValue = onTapValue
        self.value = value()
    }

    var body: some View {
        HStack(spacing: 0) {
            RepeatButton(systemImage: "minus", isEnabled: canDecrement) { onStep(-1) }

            Group {
                if let onTapValue {
                    Button(action: onTapValue) { valueLabel }
                        .buttonStyle(.plain)
                } else {
                    valueLabel
                }
            }
            .frame(maxWidth: .infinity)

            RepeatButton(systemImage: "plus", isEnabled: canIncrement) { onStep(1) }
        }
        .frame(height: 44)
        .background(Theme.surface, in: RoundedRectangle(cornerRadius: 12))
        .overlay {
            RoundedRectangle(cornerRadius: 12).stroke(Theme.hairline, lineWidth: 1)
        }
    }

    private var valueLabel: some View {
        value
            .font(.system(size: 15, weight: .semibold, design: .rounded).monospacedDigit())
            .foregroundStyle(Theme.primaryText)
            .lineLimit(1)
            .minimumScaleFactor(0.8)
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .contentShape(Rectangle())
    }
}

/// The grids the steppers move on.
enum StepGrid {
    /// Both time steppers: five minutes.
    static let minutes: Double = 5

    /// The next value on the grid in the given direction. A value between
    /// grid points — a pour cut to 23 minutes, a drink logged at 21:28:37, a
    /// 333 ml can — goes to the nearest grid point that way, so the first tap
    /// lands on a round number rather than carrying the odd offset along.
    static func snapped(_ value: Double, step: Double = minutes, stepping direction: Int) -> Double {
        // Rounded to the grid first: 4.5 / 0.5 is 9.000000000000002 in
        // floating point, and rounding that down would skip a step.
        let units = (value / step * 1e6).rounded() / 1e6
        return direction > 0
            ? (units.rounded(.down) + 1) * step
            : (units.rounded(.up) - 1) * step
    }
}

/// A button that fires once on a tap and keeps firing while held, faster
/// the longer it is held.
///
/// Built on a zero-distance drag rather than `Button`, because a button
/// cannot say when the finger lifts. The first repeat waits long enough that
/// a deliberate tap never doubles.
private struct RepeatButton: View {
    let systemImage: String
    let isEnabled: Bool
    let action: () -> Void

    @State private var repeating: Task<Void, Never>?
    @State private var fired = false

    var body: some View {
        Image(systemName: systemImage)
            .font(.system(size: 15, weight: .semibold))
            .foregroundStyle(isEnabled ? Theme.calm : Theme.secondaryText.opacity(0.4))
            .frame(width: 44, height: 44)
            .contentShape(Rectangle())
            .gesture(
                DragGesture(minimumDistance: 0)
                    .onChanged { _ in
                        guard isEnabled, repeating == nil else { return }
                        fired = false
                        repeating = Task { @MainActor in
                            try? await Task.sleep(for: .milliseconds(450))
                            var interval = 200
                            while !Task.isCancelled {
                                fired = true
                                action()
                                try? await Task.sleep(for: .milliseconds(interval))
                                interval = max(50, interval * 85 / 100)
                            }
                        }
                    }
                    .onEnded { _ in
                        repeating?.cancel()
                        repeating = nil
                        if isEnabled, !fired { action() }
                    }
            )
            .accessibilityAddTraits(.isButton)
    }
}
