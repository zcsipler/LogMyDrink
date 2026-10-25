import SwiftUI
import WidgetKit

/// The app's three places: what happened before, what is happening now, and
/// who the app thinks you are.
///
/// Live sits in the middle and is selected at launch. It is what the app is
/// for, and a centre position keeps the two others one step away in either
/// direction rather than stacking them on one side.
struct MainTabView: View {
    let store: SessionStore

    @Environment(\.scenePhase) private var scenePhase
    @State private var selection: Tab = .live

    /// The one place a tab steers another: the Live screen's "Yesterday"
    /// button opens History on the day page before today. A labelled button
    /// that says where it goes, and the tab bar moves with it — not a screen
    /// changing on its own.
    @State private var historyRequest: HistoryRequest?

    /// A widget tap. The link opens the app on Live and logs the usual drink
    /// there, so the strip with Undo appears exactly as after the capsule.
    @State private var quickAddRequest: QuickAddRequest?

    /// The launch tip, when there is one to offer (`TipLedger`).
    @State private var tip: FeatureTip?

    #if DEBUG
    /// `-debugPaywall history|people|backup` as a launch argument opens that
    /// Pro sheet at launch — the simulator cannot be tapped from the command
    /// line, and this is how the sheet gets a screenshot (CLAUDE.md 6.).
    @State private var debugPaywall: ProPaywallSheet.Topic? = UserDefaults.standard
        .string(forKey: "debugPaywall").flatMap(ProPaywallSheet.Topic.init(rawValue:))
    #endif

    enum Tab: Hashable {
        case history, live, profile
    }

    var body: some View {
        TabView(selection: $selection) {
            HistoryView(store: store, request: $historyRequest)
                .tabItem {
                    Label {
                        Text("History")
                    } icon: {
                        Image(systemName: "calendar")
                    }
                }
                .tag(Tab.history)

            LiveView(store: store, quickAddRequest: $quickAddRequest) {
                historyRequest = HistoryRequest(segment: .day, offset: 1)
                selection = .history
            }
                .tabItem {
                    Label {
                        Text("Live")
                    } icon: {
                        Image(systemName: "chart.line.uptrend.xyaxis")
                    }
                }
                .tag(Tab.live)

            ProfileView(store: store)
                .tabItem {
                    Label {
                        Text("Profile")
                    } icon: {
                        Image(systemName: "person.crop.circle")
                    }
                }
                .tag(Tab.profile)
        }
        .tint(Theme.calm)
        .preferredColorScheme(.dark)
        // Coming back after hours away: which occasion is running and what
        // today is are re-read from the curve and the clock, not only when
        // the next drink is logged.
        .onChange(of: scenePhase) { _, phase in
            if phase == .active {
                // The clock first: the app may have sat in the background
                // for hours, and everything the refresh derives — which
                // occasion is running, which day is today — reads `now`.
                store.tick()
                store.refreshFromStore()
                Task { await offerTip() }
                // A subscription that ran out while the app slept locks
                // here, not at the next launch.
                Task { await ProStore.shared.refreshEntitlement() }
            }
        }
        // A cold launch does not always pass through `onChange` above.
        .task { await offerTip() }
        .sheet(item: $tip) { tip in
            TipSheet(
                tip: tip,
                onAction: perform,
                onDismissForGood: { TipLedger().dismiss($0) }
            )
        }
        // The second place a tab is steered from outside, and the same shape
        // as the first: a request the target screen applies and clears. The
        // add itself happens on Live, not here, because the strip that lets
        // it be undone is Live's.
        .onOpenURL { url in
            guard QuickAddLink.matches(url) else { return }
            selection = .live
            quickAddRequest = QuickAddRequest()
        }
        #if DEBUG
        .sheet(item: $debugPaywall) { ProPaywallSheet(topic: $0) }
        #endif
    }
}

// MARK: - Launch tips

extension MainTabView {
    /// Offers the day's tip, if any, a moment after the app comes forward.
    ///
    /// The wait is for the widget: a tap on it opens the app and logs a drink,
    /// and the request arrives just after the foreground transition. A tip
    /// sheet over the Undo strip would be the worst place for one, so a
    /// pending quick add — or the alcohol it just put in the curve — ends it.
    func offerTip() async {
        try? await Task.sleep(for: .seconds(1.2))
        guard tip == nil, quickAddRequest == nil, selection == .live else { return }

        let ledger = TipLedger()
        let installed = await Self.widgetIsInstalled()
        let tracked = Calendar.current.dateComponents(
            [.day], from: store.person.trackingStartedAt, to: .now
        ).day ?? 0
        let context = TipContext(
            hasFavourite: store.favourite != nil,
            widgetInstalled: installed,
            siriUsed: ledger.siriUsed,
            historyOpened: ledger.historyOpened,
            trackedDays: tracked,
            hasAlcohol: store.currentRange.upperBound > 0
        )
        guard let next = ledger.next(context, now: .now) else { return }
        ledger.markShown(at: .now)
        tip = next
    }

    /// Whether the quick-add widget is on any screen. The callback form,
    /// because the async one is iOS 18 and the app targets 17. An error
    /// reads as "not installed": the worst case is one tip too many.
    static func widgetIsInstalled() async -> Bool {
        await withCheckedContinuation { continuation in
            WidgetCenter.shared.getCurrentConfigurations { result in
                let installed = (try? result.get())?
                    .contains { $0.kind == WidgetBridge.widgetKind } ?? false
                continuation.resume(returning: installed)
            }
        }
    }

    /// The primary button of a tip whose action is somewhere else in the app.
    func perform(_ tip: FeatureTip) {
        switch tip {
        case .favourite:
            selection = .profile
        case .history:
            selection = .history
        case .siri:
            // "Got it" is "later": the tip drops out on its own once Siri
            // is used; "Don't show again" is the way to turn it off for good.
            break
        case .widget:
            break // handled inside the sheet
        }
    }
}

/// A page of History asked for from another tab. Identified, so that asking
/// for the same page twice is two requests.
struct HistoryRequest: Equatable {
    let segment: HistorySegment
    let offset: Int
    let id = UUID()
}

#Preview {
    MainTabView(store: .preview)
}
