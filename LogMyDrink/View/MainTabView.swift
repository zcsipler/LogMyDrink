import SwiftUI

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
        // A session left open overnight has to be closed when the app comes
        // back, not only when the next drink is logged.
        .onChange(of: scenePhase) { _, phase in
            if phase == .active { store.refreshFromStore() }
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
