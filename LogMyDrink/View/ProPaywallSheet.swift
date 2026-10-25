import StoreKit
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
/// Below the topic: the two plans (yearly preselected — it is the one most
/// people keep), the buy button, the renewal terms, and the links App Review
/// asks for on a subscription paywall: restore, terms, privacy. "Redeem
/// code" opens Apple's own sheet for offer codes (5.30).
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

    // MARK: Plans and buying

    private var proStore: ProStore { .shared }

    @State private var selectedPlan: ProStore.Plan = .yearly
    @State private var showsRedeem = false
    @State private var message: Message?

    /// What went wrong or is still on its way, said under the button.
    enum Message: Equatable {
        case pending, failed, nothingToRestore
    }

    /// Apple's standard licence agreement, which applies when an app has
    /// none of its own. App Review wants it one tap from a subscription's
    /// paywall (3.1.2).
    static let termsURL = URL(string: "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/")!

    /// The privacy policy, also required next to a subscription. Published
    /// from the public `zcsipler/logmydrink-site` repository (GitHub Pages);
    /// the same address goes into App Store Connect. Optional so that the
    /// link can be hidden rather than broken, should the page ever move.
    static let privacyURL: URL? = URL(string: "https://zcsipler.github.io/logmydrink-site/privacy/")

    /// One row of the plan picker, already formatted.
    struct PlanRow: Identifiable {
        let plan: ProStore.Plan
        let price: String
        /// Yearly only: the same price spread over twelve months.
        let perMonth: String?
        /// Yearly only: how much cheaper than twelve months.
        let saving: Double?
        var id: ProStore.Plan { plan }
    }

    private var rows: [PlanRow]? {
        if proStore.loadState == .loaded {
            return ProStore.Plan.allCases.compactMap { plan in
                guard let product = proStore.products[plan] else { return nil }
                return PlanRow(
                    plan: plan,
                    price: product.displayPrice,
                    perMonth: plan == .yearly ? proStore.yearlyPerMonth() : nil,
                    saving: plan == .yearly ? proStore.yearlySaving() : nil
                )
            }
        }
        #if DEBUG
        // Launched from the command line there is no StoreKit configuration
        // and nothing loads. The prices of 5.30 stand in, so the sheet can be
        // looked at; buying one switches on the simulated Pro.
        if proStore.loadState == .failed { return Self.sampleRows }
        #endif
        return nil
    }

    #if DEBUG
    private static let sampleRows = [
        PlanRow(plan: .yearly, price: "$24.99", perMonth: "$2.08", saving: 0.48),
        PlanRow(plan: .monthly, price: "$3.99", perMonth: nil, saving: nil),
    ]
    #endif

    @ViewBuilder
    private var action: some View {
        VStack(spacing: 14) {
            if let rows {
                VStack(spacing: 10) {
                    ForEach(rows) { row in planRow(row) }
                }
                buyButton
                finePrint(rows)
            } else if proStore.loadState == .failed {
                VStack(spacing: 10) {
                    Text("Prices could not be loaded.")
                        .font(.system(size: 14, design: .rounded))
                        .foregroundStyle(Theme.secondaryText)
                    Button("Try again") { Task { await proStore.loadProducts() } }
                        .font(.system(size: 15, weight: .semibold, design: .rounded))
                        .foregroundStyle(Theme.calm)
                }
                .padding(.vertical, 8)
            } else {
                ProgressView()
                    .tint(Theme.secondaryText)
                    .padding(.vertical, 24)
            }

            if let message {
                messageText(message)
                    .font(.system(size: 13, design: .rounded))
                    .foregroundStyle(Theme.secondaryText)
                    .multilineTextAlignment(.center)
            }

            footer
        }
        .task { await proStore.loadProducts() }
        .offerCodeRedemption(isPresented: $showsRedeem) { _ in
            Task {
                await proStore.refreshEntitlement()
                if flags.isPro { dismiss() }
            }
        }
    }

    private func planRow(_ row: PlanRow) -> some View {
        let selected = row.plan == selectedPlan
        return Button {
            selectedPlan = row.plan
        } label: {
            HStack(spacing: 12) {
                Image(systemName: selected ? "checkmark.circle.fill" : "circle")
                    .font(.system(size: 20))
                    .foregroundStyle(selected ? Theme.calm : Theme.secondaryText)
                VStack(alignment: .leading, spacing: 2) {
                    HStack(spacing: 6) {
                        planTitle(row.plan)
                            .font(.system(size: 16, weight: .semibold, design: .rounded))
                            .foregroundStyle(Theme.primaryText)
                        if let saving = row.saving {
                            Text("Save \(saving.formatted(.percent.precision(.fractionLength(0))))")
                                .font(.system(size: 11, weight: .bold, design: .rounded))
                                .foregroundStyle(Theme.background)
                                .padding(.horizontal, 7)
                                .padding(.vertical, 2)
                                .background(Theme.calm, in: Capsule())
                        }
                    }
                    if let perMonth = row.perMonth {
                        Text("About \(perMonth) a month")
                            .font(.system(size: 13, design: .rounded))
                            .foregroundStyle(Theme.secondaryText)
                    }
                }
                Spacer(minLength: 8)
                pricePerPeriod(row)
                    .font(.system(size: 15, weight: .medium, design: .rounded))
                    .foregroundStyle(Theme.primaryText)
            }
            .padding(.horizontal, 14)
            .padding(.vertical, 12)
            .background(Theme.calm.opacity(selected ? 0.12 : 0.04),
                        in: RoundedRectangle(cornerRadius: 14, style: .continuous))
            .overlay {
                RoundedRectangle(cornerRadius: 14, style: .continuous)
                    .strokeBorder(selected ? Theme.calm : Theme.secondaryText.opacity(0.3),
                                  lineWidth: selected ? 1.5 : 1)
            }
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
    }

    private func planTitle(_ plan: ProStore.Plan) -> Text {
        switch plan {
        case .yearly: Text("Yearly")
        case .monthly: Text("Monthly")
        }
    }

    private func pricePerPeriod(_ row: PlanRow) -> Text {
        switch row.plan {
        case .yearly: Text("\(row.price) / year")
        case .monthly: Text("\(row.price) / month")
        }
    }

    private var buyButton: some View {
        Button {
            Task { await buy() }
        } label: {
            Group {
                if proStore.isPurchasing {
                    ProgressView().tint(Theme.background)
                } else if proStore.isEligibleForTrial {
                    Text("Start my free month")
                } else {
                    Text("Subscribe")
                }
            }
            .font(.system(size: 16, weight: .semibold, design: .rounded))
            .frame(maxWidth: .infinity)
            .padding(.vertical, 13)
            .background(Theme.calm, in: Capsule())
            .foregroundStyle(Theme.background)
        }
        .disabled(proStore.isPurchasing)
    }

    /// What the subscription costs and how it ends, under the button — App
    /// Review wants the renewal terms stated before the purchase (3.1.2).
    private func finePrint(_ rows: [PlanRow]) -> some View {
        let price = rows.first { $0.plan == selectedPlan }?.price ?? ""
        return VStack(spacing: 4) {
            switch (selectedPlan, proStore.isEligibleForTrial) {
            case (.yearly, true): Text("Free for one month, then \(price) a year.")
            case (.monthly, true): Text("Free for one month, then \(price) a month.")
            case (.yearly, false): Text("\(price) a year.")
            case (.monthly, false): Text("\(price) a month.")
            }
            Text("Renews automatically until you cancel. Cancel anytime in Settings.")
        }
        .font(.system(size: 12, design: .rounded))
        .foregroundStyle(Theme.secondaryText)
        .multilineTextAlignment(.center)
        .fixedSize(horizontal: false, vertical: true)
    }

    private var footer: some View {
        VStack(spacing: 8) {
            HStack(spacing: 18) {
                Button("Restore purchases") { Task { await restore() } }
                Button("Redeem code") { showsRedeem = true }
            }
            HStack(spacing: 18) {
                Link(destination: Self.termsURL) { Text("Terms of Use") }
                if let privacy = Self.privacyURL {
                    Link(destination: privacy) { Text("Privacy Policy") }
                }
            }
        }
        .font(.system(size: 13, weight: .medium, design: .rounded))
        .foregroundStyle(Theme.calm)
        .padding(.top, 2)
    }

    private func messageText(_ message: Message) -> Text {
        switch message {
        case .pending: Text("Waiting for approval. Pro opens as soon as the purchase goes through.")
        case .failed: Text("The purchase did not go through. Please try again.")
        case .nothingToRestore: Text("No active subscription was found for this Apple ID.")
        }
    }

    private func buy() async {
        message = nil
        #if DEBUG
        if proStore.loadState != .loaded {
            flags.setSimulatesPro(true)
            dismiss()
            return
        }
        #endif
        switch await proStore.purchase(selectedPlan) {
        case .purchased: dismiss()
        case .pending: message = .pending
        case .cancelled: break
        case .failed: message = .failed
        }
    }

    private func restore() async {
        message = nil
        if await proStore.restore() {
            dismiss()
        } else {
            message = .nothingToRestore
        }
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
