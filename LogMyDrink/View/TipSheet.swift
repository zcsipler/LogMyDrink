import SwiftUI

/// One feature tip, offered at launch (`FeatureTip`, `TipLedger`).
///
/// A sheet at a medium detent rather than an alert: it has a picture, three
/// choices and, for the widget, a guide to push onto — an alert has room for
/// none of that. Swiping it down is the same as "Later".
struct TipSheet: View {
    let tip: FeatureTip
    /// The primary button, for the tips whose action leaves this sheet
    /// (set a favourite → Profile, open History). The widget tip keeps its
    /// action here, as a pushed guide.
    let onAction: (FeatureTip) -> Void
    let onDismissForGood: (FeatureTip) -> Void

    @Environment(\.dismiss) private var dismiss
    @State private var detent: PresentationDetent = .medium
    @State private var showsGuide = false

    var body: some View {
        NavigationStack {
            VStack(spacing: 18) {
                Image(systemName: tip.icon)
                    .font(.system(size: 34, weight: .light))
                    .foregroundStyle(Theme.calm)
                    .frame(width: 72, height: 72)
                    .background(Theme.calm.opacity(0.12), in: Circle())
                    .padding(.top, 8)

                VStack(spacing: 8) {
                    Text(tip.title)
                        .font(.system(size: 20, weight: .semibold, design: .rounded))
                        .foregroundStyle(Theme.primaryText)
                        .multilineTextAlignment(.center)
                    Text(tip.message)
                        .font(.system(size: 15, design: .rounded))
                        .foregroundStyle(Theme.secondaryText)
                        .multilineTextAlignment(.center)
                        .fixedSize(horizontal: false, vertical: true)
                }
                .padding(.horizontal, 12)

                Spacer(minLength: 0)

                VStack(spacing: 6) {
                    primaryButton

                    Button { dismiss() } label: {
                        Text("Later")
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 10)
                    }
                    .foregroundStyle(Theme.primaryText)

                    Button {
                        onDismissForGood(tip)
                        dismiss()
                    } label: {
                        Text("Don’t show again")
                            .font(.system(size: 14, design: .rounded))
                            .padding(.vertical, 4)
                    }
                    .foregroundStyle(Theme.secondaryText)
                }
            }
            .padding(.horizontal, 24)
            .padding(.bottom, 12)
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .background(Theme.background)
            .navigationDestination(isPresented: $showsGuide) { WidgetGuideView() }
        }
        .presentationDetents([.medium, .large], selection: $detent)
        .presentationDragIndicator(.visible)
        .preferredColorScheme(.dark)
    }

    @ViewBuilder
    private var primaryButton: some View {
        let label = Text(tip.actionTitle)
            .font(.system(size: 16, weight: .semibold, design: .rounded))
            .frame(maxWidth: .infinity)
            .padding(.vertical, 13)
            .background(Theme.calm, in: Capsule())
            .foregroundStyle(Theme.background)

        if tip == .widget {
            // iOS has no link into the widget gallery, so the best the
            // button can do is the steps, with the sheet grown to fit them.
            Button {
                detent = .large
                showsGuide = true
            } label: { label }
        } else {
            Button {
                onAction(tip)
                dismiss()
            } label: { label }
        }
    }
}

// MARK: - Widget guide

/// The steps to put the widget on the Lock Screen or the Home Screen.
///
/// The app cannot add a widget, and there is no link to the gallery
/// (CLAUDE.md, 5.15) — telling the steps is all it can do. Two tabs, because
/// the two screens are edited in entirely different ways.
struct WidgetGuideView: View {
    enum Place: Hashable { case lockScreen, homeScreen }

    @State private var place: Place = .lockScreen

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 22) {
                Picker(selection: $place) {
                    Text("Lock Screen").tag(Place.lockScreen)
                    Text("Home Screen").tag(Place.homeScreen)
                } label: {
                    Text("Where")
                }
                .pickerStyle(.segmented)

                VStack(alignment: .leading, spacing: 18) {
                    switch place {
                    case .lockScreen:
                        step(1, icon: "lock.iphone", Text("Lock your phone, then touch and hold the Lock Screen."))
                        step(2, icon: "slider.horizontal.below.rectangle", Text("Tap Customize, then Lock Screen, then the widget row under the clock."))
                        step(3, icon: "checkmark.circle", Text("Choose LogMyDrink, then tap Done."))
                    case .homeScreen:
                        step(1, icon: "hand.tap", Text("Touch and hold an empty area of the Home Screen until the icons jiggle."))
                        step(2, icon: "plus.square", Text("Tap Edit, then Add Widget."))
                        step(3, icon: "magnifyingglass", Text("Search for LogMyDrink, pick a size and tap Add Widget."))
                    }
                }

                Text("A tap on the widget opens the app and logs your favourite drink. While there is alcohol in your system, it also shows your level and which way it is going.")
                    .font(.system(size: 14, design: .rounded))
                    .foregroundStyle(Theme.secondaryText)
                    .fixedSize(horizontal: false, vertical: true)
            }
            .padding(20)
        }
        .background(Theme.background)
        .navigationTitle(Text("Add the widget"))
        .navigationBarTitleDisplayMode(.inline)
    }

    private func step(_ number: Int, icon: String, _ text: Text) -> some View {
        HStack(alignment: .top, spacing: 14) {
            Text(verbatim: "\(number)")
                .font(.system(size: 15, weight: .bold, design: .rounded))
                .foregroundStyle(Theme.background)
                .frame(width: 28, height: 28)
                .background(Theme.calm, in: Circle())
            VStack(alignment: .leading, spacing: 6) {
                text
                    .font(.system(size: 15, design: .rounded))
                    .foregroundStyle(Theme.primaryText)
                    .fixedSize(horizontal: false, vertical: true)
                Image(systemName: icon)
                    .font(.system(size: 22, weight: .light))
                    .foregroundStyle(Theme.secondaryText)
            }
        }
    }
}

// MARK: - The Profile switch

/// "Show tips" — the one switch for all of them, on the Display & language
/// page. The per-tip "Don't show again" stays where the tip is.
struct TipsSection: View {
    @AppStorage(TipLedger.enabledKey) private var enabled = true

    var body: some View {
        Section {
            Toggle(isOn: $enabled) {
                Text("Show tips")
            }
            .tint(Theme.calm)
        } footer: {
            Text("One tip a day at most, when you open the app — never while there is alcohol in your system.")
        }
        .listRowBackground(Theme.surface)
    }
}

#Preview {
    Color.black.sheet(isPresented: .constant(true)) {
        TipSheet(tip: .widget, onAction: { _ in }, onDismissForGood: { _ in })
    }
}
