import SwiftUI

/// What stands between a free user and a Pro feature.
///
/// One sheet for every lock, told which lock was tapped (`Topic`), because
/// there is one thing to buy: whatever brought you here, the button opens
/// the same Pro. The topic only decides what the sheet says first.
///
/// For history it says three things, in this order: what is behind the
/// lock, that the data is already there, and how to open it. The middle one
/// matters most — the flag gates the view, never the record (5.16), and a
/// user deciding whether to pay should know they are buying a window onto
/// data they already own, not a subscription to start collecting it.
///
/// Built like `TipSheet`: as tall as its content, measured; a lighter
/// surface with a light hairline at the top, so that it does not melt into
/// the near-black screen behind it.
///
/// There is no store behind the button yet. In debug builds it switches on
/// the simulated Pro, which is how the locked and unlocked screens get
/// tested side by side; in release it says so and does nothing. With
/// StoreKit the button starts the subscription (5.29, `TODO.md`).
struct ProPaywallSheet: View {

    enum Topic: String, Identifiable {
        case history
        case people
        case backup

        var id: String { rawValue }
    }

    let topic: Topic

    @Environment(\.dismiss) private var dismiss

    /// Measured, then used as the only detent — no empty band between the
    /// text and the button.
    @State private var contentHeight: CGFloat = 320

    private static let cornerRadius: CGFloat = 28

    private var flags: FeatureFlags { .shared }

    var body: some View {
        content
            .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .top)
            .background(Theme.surface)
            .presentationDetents([.height(contentHeight)])
            .presentationDragIndicator(.visible)
            .presentationCornerRadius(Self.cornerRadius)
            .presentationBackground(Theme.surface)
            .overlay {
                RoundedRectangle(cornerRadius: Self.cornerRadius, style: .continuous)
                    .strokeBorder(Color.white.opacity(0.14), lineWidth: 1)
                    .mask(
                        LinearGradient(colors: [.white, .white.opacity(0)],
                                       startPoint: .top, endPoint: .init(x: 0.5, y: 0.35))
                    )
                    .ignoresSafeArea()
                    .allowsHitTesting(false)
            }
            .preferredColorScheme(.dark)
    }

    private var content: some View {
        VStack(spacing: 18) {
            Image(systemName: symbol)
                .font(.system(size: 30, weight: .light))
                .foregroundStyle(Theme.calm)
                .frame(width: 72, height: 72)
                .background(Theme.calm.opacity(0.12), in: Circle())

            VStack(spacing: 8) {
                title
                    .font(.system(size: 20, weight: .semibold, design: .rounded))
                    .foregroundStyle(Theme.primaryText)
                lines
                    .font(.system(size: 15, design: .rounded))
                    .foregroundStyle(Theme.secondaryText)
            }
            .multilineTextAlignment(.center)
            .fixedSize(horizontal: false, vertical: true)
            .padding(.horizontal, 12)

            action
                .padding(.top, 6)
        }
        .padding(.horizontal, 24)
        // Clear of the drag indicator at the top.
        .padding(.top, 36)
        .padding(.bottom, 12)
        .fixedSize(horizontal: false, vertical: true)
        .onGeometryChange(for: CGFloat.self) { $0.size.height } action: { height in
            let fitted = ceil(height)
            guard abs(fitted - contentHeight) > 0.5 else { return }
            contentHeight = fitted
        }
    }

    @ViewBuilder
    private var action: some View {
        #if DEBUG
        Button {
            flags.setSimulatesPro(true)
            dismiss()
        } label: {
            Text(verbatim: "Simulate Pro (debug)")
                .font(.system(size: 16, weight: .semibold, design: .rounded))
                .frame(maxWidth: .infinity)
                .padding(.vertical, 13)
                .background(Theme.calm, in: Capsule())
                .foregroundStyle(Theme.background)
        }
        #else
        Text("Coming soon")
            .font(.system(size: 14, weight: .medium, design: .rounded))
            .foregroundStyle(Theme.secondaryText)
            .padding(.vertical, 13)
        #endif
    }

    private var symbol: String {
        switch topic {
        case .history: "chart.bar.xaxis"
        case .people: "person.2"
        case .backup: "externaldrive"
        }
    }

    private var title: Text {
        switch topic {
        case .history: Text("See further back")
        case .people: Text("Log for friends too")
        case .backup: Text("Back up and restore")
        }
    }

    @ViewBuilder
    private var lines: some View {
        switch topic {
        case .history:
            VStack(spacing: 10) {
                Text("Weeks, months and years side by side — and every evening older than seven days.")
                Text("Everything you have logged is already saved. Unlocking only shows it.")
            }
        case .people:
            Text("Switch to someone else in one tap and log their drinks with their own body and limit — each person gets their own curve and history.")
        case .backup:
            Text("Save everything to a file, and read a backup back in — on this phone or on a new one.")
        }
    }
}

#Preview("History") {
    Color.black.sheet(isPresented: .constant(true)) { ProPaywallSheet(topic: .history) }
}

#Preview("People") {
    Color.black.sheet(isPresented: .constant(true)) { ProPaywallSheet(topic: .people) }
}

#Preview("Backup") {
    Color.black.sheet(isPresented: .constant(true)) { ProPaywallSheet(topic: .backup) }
}
