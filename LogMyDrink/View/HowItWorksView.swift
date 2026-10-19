import SwiftUI

// MARK: - The estimate card under the Live figure

/// "Estimate, not a measurement. Never use this to decide whether you can
/// drive." — under the Live figure, in place of the old "estimated level"
/// caption, and the way into `HowItWorksView`.
///
/// It replaces two lines of small print that sat at the very bottom of Live,
/// usually behind the tab bar. The product thesis says the disclaimer is part
/// of the screen, not a footnote (CLAUDE.md, 2.), so it sits on the number it
/// qualifies. The driving sentence stays on the main screen on purpose: it is
/// what an App Review pass sees first, and the case against 1.4.3 is that
/// this is not a driving tool (9.).
///
/// A card, not a one-line capsule: a first round had a small outlined
/// capsule, and it read as a label rather than something to tap. The link
/// line with its chevron says there is more behind it, and the whole card is
/// the button. Blue (`Theme.info`), because red on this screen means "at
/// your limit" (5.14).
struct EstimateCard: View {
    /// Whether the figure above is a range (5.8). The wording follows it.
    let isRange: Bool
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            HStack(alignment: .top, spacing: 10) {
                Image(systemName: "info.circle.fill")
                    .font(.system(size: 15))
                    .foregroundStyle(Theme.info)
                VStack(alignment: .leading, spacing: 8) {
                    (isRange
                        ? Text("Estimated range, not a measurement. Never use this to decide whether you can drive.")
                        : Text("Estimate, not a measurement. Never use this to decide whether you can drive."))
                        .font(.system(size: 13, weight: .medium, design: .rounded))
                        .foregroundStyle(Theme.primaryText)
                        .multilineTextAlignment(.leading)
                        .fixedSize(horizontal: false, vertical: true)
                    HStack(spacing: 4) {
                        Text("How does the app calculate this?")
                        Spacer(minLength: 4)
                        Image(systemName: "chevron.right")
                            .font(.system(size: 12, weight: .semibold))
                    }
                    .font(.system(size: 13, weight: .semibold, design: .rounded))
                    .foregroundStyle(Theme.info)
                }
            }
            .padding(14)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(Theme.info.opacity(0.10), in: RoundedRectangle(cornerRadius: 14))
            .overlay(RoundedRectangle(cornerRadius: 14).strokeBorder(Theme.info.opacity(0.55), lineWidth: 1))
            .contentShape(RoundedRectangle(cornerRadius: 14))
        }
        .buttonStyle(.plain)
    }
}

// MARK: - The sheet around the page

/// `HowItWorksView` as a sheet, for the badge on Live. From Profile the same
/// page is pushed instead, inside that tab's own navigation stack.
struct HowItWorksSheet: View {
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            HowItWorksView()
                .toolbar {
                    ToolbarItem(placement: .confirmationAction) {
                        Button { dismiss() } label: { Text("Done") }
                    }
                }
        }
        .preferredColorScheme(.dark)
    }
}

// MARK: - The page

/// What the app is for, how it calculates, why the figure is only an
/// estimate, and the features nobody finds on their own.
///
/// One long page rather than a menu of sub-pages: it is read once, top to
/// bottom, and the warning about driving has to be the first thing on it. The
/// warning lived at the bottom of Live until this page existed; it moved here
/// because the badge on Live now says "estimate" on its own, and a second
/// line saying it again was small print nobody read.
///
/// The science is written for someone without the vocabulary, with the names
/// and numbers folded away under "Details" for whoever wants them. The model
/// is described as what it is — a refinement of Widmark, not Widmark's
/// formula (CLAUDE.md, 4.) — and the numbers here are the ones the engine
/// uses; if `Physiology` changes, this page changes with it.
struct HowItWorksView: View {
    @State private var showsDetails = false

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 28) {
                drivingWarning
                purpose
                calculation
                estimate
                tips
            }
            .padding(.horizontal, 20)
            .padding(.vertical, 16)
        }
        .scrollIndicators(.hidden)
        .background(Theme.background)
        .navigationTitle(Text("How it works"))
        .navigationBarTitleDisplayMode(.inline)
    }

    // MARK: Sections

    private var drivingWarning: some View {
        HStack(alignment: .top, spacing: 12) {
            Image(systemName: "exclamationmark.triangle.fill")
                .font(.system(size: 18))
                .foregroundStyle(Theme.alarm)
            Text("Never use this to decide whether you can drive. The app estimates, it does not measure, and your actual level can differ considerably.")
                .font(.system(size: 15, weight: .semibold, design: .rounded))
                .foregroundStyle(Theme.primaryText)
                .fixedSize(horizontal: false, vertical: true)
        }
        .padding(16)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(Theme.alarm.opacity(0.12), in: RoundedRectangle(cornerRadius: 14))
        .overlay(RoundedRectangle(cornerRadius: 14).strokeBorder(Theme.alarm.opacity(0.5), lineWidth: 1))
    }

    private var purpose: some View {
        section(Text("Why this app exists")) {
            paragraph(Text("LogMyDrink helps you drink more mindfully and stay in control. The decision happens before the next glass, so the app shows you in advance where another drink would take your level, and when it would peak."))
            paragraph(Text("But it is not only about tonight. Every drink you log goes into your History, so over months and years you can see how much, how often and how high you drink. Your patterns emerge from it, and so does the direction they are moving in — whether things are getting better or worse."))
        }
    }

    private var calculation: some View {
        section(Text("How it calculates")) {
            paragraph(Text("The estimate builds on the Widmark method, used to estimate blood alcohol since the 1930s; the app runs a refined version of it."))
            paragraph(Text("From your weight, height, age and sex it works out how much water your body holds, because that is where alcohol spreads. It follows every drink separately: how much alcohol it had, how fast you drank it, and how much you had eaten, because that sets how quickly it is absorbed."))
            paragraph(Text("Meanwhile your liver breaks down a roughly constant amount every hour; how much in your case is estimated from how often you drink. The result is a curve, minute by minute: where you are now, where you are heading, and when you will be clear."))

            DisclosureGroup(isExpanded: $showsDetails) {
                VStack(alignment: .leading, spacing: 12) {
                    detail(Text("Body water"), Text("The Watson formula (1980), from weight, height, age and sex. The female formula has no age term — a property of the formula, not a bug. The distribution volume is body water divided by 0.85, the water content of blood."))
                    detail(Text("Absorption"), Text("Every drink has its own “stomach”. On an empty stomach half of the alcohol is absorbed in about 7 minutes, on a full one in about 21. A drink you sip enters the stomach evenly over the time you drink it."))
                    detail(Text("Full stomach"), Text("Gives a lower peak and an earlier clear time. Surprising, but measured: with food the stomach breaks down part of the alcohol before it is absorbed (the app uses 5, 10 and 15 percent), and what never got in does not need to be broken down."))
                    detail(Text("Elimination"), Text("About 0.15 ‰ per hour (published range 0.10–0.25), higher in regular drinkers as liver enzymes adapt. Close to zero it slows down (Michaelis–Menten kinetics), so the curve tapers off instead of stopping abruptly."))
                    detail(Text("Computation"), Text("The curve comes from a numerical simulation at one-minute resolution."))
                }
                .padding(.top, 10)
            } label: {
                Text("Details")
                    .font(.system(size: 15, weight: .semibold, design: .rounded))
                    .foregroundStyle(Theme.primaryText)
            }
            .tint(Theme.calm)
            .padding(14)
            .background(Theme.surface, in: RoundedRectangle(cornerRadius: 14))
        }
    }

    private var estimate: some View {
        section(Text("Why it is only an estimate")) {
            paragraph(Text("The app measures nothing. What it shows is the output of a model using average values, and reality can differ. The biggest unknown is how fast you break alcohol down: within the plausible range, that alone can move the peak by 40 percent and the clear time by four hours on the same evening."))
            paragraph(Text("Genetics, liver health, medication, what you ate, sleep and tiredness matter too — the app knows none of these. Only a certified breathalyser or a blood test gives an exact value."))
            paragraph(Text("The number is still useful. If the app reads consistently a little high or low for you, it is off in the same direction every evening, so over time you learn what a given value means for you. In Profile you can also show the uncertainty of the elimination rate: you then see a range instead of a single number."))
        }
    }

    private var tips: some View {
        section(Text("Tips")) {
            featureRow(icon: "hand.tap", Text("Favourite drink in one tap"), Text("Set a favourite in Profile and the Live button logs it with a single tap."))

            VStack(alignment: .leading, spacing: 8) {
                featureRow(icon: "rectangle.on.rectangle", Text("Widget"), Text("Add it to your Lock Screen or Home Screen: one tap logs your favourite. While there is alcohol in your system, it also shows your level and which way it is going."))
                NavigationLink {
                    WidgetGuideView()
                } label: {
                    HStack(spacing: 4) {
                        Text("How do I add it?")
                        Image(systemName: "chevron.right")
                            .font(.system(size: 11, weight: .semibold))
                    }
                    .font(.system(size: 14, weight: .medium, design: .rounded))
                    .foregroundStyle(Theme.calm)
                }
                .padding(.leading, 38)
            }

            featureRow(icon: "mic", Text("Siri"), Text("Say “Hey Siri, LogMyDrink now” and Siri logs your favourite, then tells you where your peak is heading."))
            featureRow(icon: "calendar", Text("Looking back"), Text("“Yesterday” at the top of Live takes you to the previous day in one tap; the History tab shows your patterns over weeks, months and years."))
            featureRow(icon: "clock.arrow.circlepath", Text("Logging later"), Text("If you log a drink after the fact, set the time back with the − and + buttons; a missed day can be filled in from the Day view in History."))
        }
    }

    // MARK: Building blocks

    private func section<Content: View>(_ title: Text, @ViewBuilder content: () -> Content) -> some View {
        VStack(alignment: .leading, spacing: 12) {
            title
                .font(.system(size: 13, weight: .semibold, design: .rounded))
                .textCase(.uppercase)
                .foregroundStyle(Theme.secondaryText)
            content()
        }
    }

    private func paragraph(_ text: Text) -> some View {
        text
            .font(.system(size: 15, design: .rounded))
            .foregroundStyle(Theme.primaryText)
            .lineSpacing(3)
            .fixedSize(horizontal: false, vertical: true)
    }

    private func detail(_ title: Text, _ body: Text) -> some View {
        VStack(alignment: .leading, spacing: 3) {
            title
                .font(.system(size: 14, weight: .semibold, design: .rounded))
                .foregroundStyle(Theme.primaryText)
            body
                .font(.system(size: 14, design: .rounded))
                .foregroundStyle(Theme.secondaryText)
                .lineSpacing(2)
                .fixedSize(horizontal: false, vertical: true)
        }
    }

    private func featureRow(icon: String, _ title: Text, _ body: Text) -> some View {
        HStack(alignment: .top, spacing: 14) {
            Image(systemName: icon)
                .font(.system(size: 17))
                .foregroundStyle(Theme.calm)
                .frame(width: 24)
            VStack(alignment: .leading, spacing: 3) {
                title
                    .font(.system(size: 15, weight: .semibold, design: .rounded))
                    .foregroundStyle(Theme.primaryText)
                body
                    .font(.system(size: 14, design: .rounded))
                    .foregroundStyle(Theme.secondaryText)
                    .lineSpacing(2)
                    .fixedSize(horizontal: false, vertical: true)
            }
        }
    }
}

#Preview {
    HowItWorksSheet()
}
