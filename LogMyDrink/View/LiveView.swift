import SwiftUI
import BACKit

/// Today, and nothing else: the window of the current drinking day onto the
/// timeline — the running occasion, whatever finished earlier today, and the
/// tail of last night if it is still in the blood.
///
/// Looking back used to live here as a swipe between days, but a horizontal
/// drag had to share the screen with the chart's own drag and with the drink
/// rows' delete swipe, and it lost to both — it was there, it just took three
/// attempts to hit. Reaching a past evening is what History is for, and the
/// "Yesterday" button at the top is the one-tap way there: it opens History
/// on the day page before today, from where the chevrons page further back.
struct LiveView: View {
    let store: SessionStore

    /// A quick add asked for from a widget. Applied once and cleared, the
    /// way History handles its requests: it may arrive before this view
    /// exists (the app was launched by the tap) or while it is on screen.
    @Binding var quickAddRequest: QuickAddRequest?

    /// Opens History on yesterday. The tab switch is the parent's to make.
    var onShowYesterday: () -> Void = {}

    @State private var showsAddDrink = false
    @State private var editingDrink: Drink?
    @State private var openRowID: UUID?

    /// The last quick add, while its correction strip is still up. Nil the rest
    /// of the time, which is nearly always.
    @State private var receipt: QuickAddReceipt?

    /// Ticks every half minute — this does not change the band, only where
    /// on it we read.
    private let clock = Timer.publish(every: 30, on: .main, in: .common).autoconnect()

    // MARK: What today is

    /// Today's window. Two cases, not three: a day with a curve on it — drinks
    /// had today, or last night still clearing — and a day with nothing. An
    /// `untracked` case used to exist for days before the app kept records
    /// (see 5.7): today can never be one of those, so it lives on in the
    /// model and belongs in History, not here.
    ///
    /// Reads `store.revision` so that any write redraws this screen: the
    /// model is derived from stored sessions, and a write that does not move
    /// the running occasion — deleting a drink from this morning's finished
    /// one — would otherwise change nothing the body observes.
    private var today: BACChartModel {
        _ = store.revision
        return store.chartModel
    }

    // MARK: Body

    var body: some View {
        ZStack {
            Theme.background.ignoresSafeArea()

            content

            VStack(spacing: 0) {
                Spacer()

                if let receipt {
                    QuickAddStrip(
                        receipt: receipt,
                        onCorrect: { store.correct(receipt.drink, stomach: $0) },
                        onSetDefault: { store.makeFavourite(receipt.drink) },
                        onUndo: {
                            store.undoQuickAdd(receipt)
                            dismissStrip()
                        }
                    )
                    .transition(.move(edge: .bottom).combined(with: .opacity))
                }

                QuickAddBar(
                    store: store,
                    offer: store.quickAddOffer,
                    onQuickAdd: quickAdd,
                    onOpenSheet: { showsAddDrink = true }
                )
            }
        }
        .onReceive(clock) { _ in store.tick() }
        .sheet(isPresented: $showsAddDrink) { AddDrinkSheet(store: store) }
        .sheet(item: $editingDrink) { drink in
            AddDrinkSheet(store: store, editing: drink, session: store.sessionOwning(drink.id))
        }
        .onChange(of: today.drinks.count) { openRowID = nil }
        .onChange(of: editingDrink?.id) { openRowID = nil }
        .onAppear { applyQuickAddRequest() }
        .onChange(of: quickAddRequest?.id) { applyQuickAddRequest() }
        // A quick add is silent by design, so the phone says what the screen
        // does not have to: the user is looking at a bar, not at this. Only on
        // the way in — the strip expiring is not an event worth a buzz, and a
        // plain `.success` trigger would fire for that too.
        .sensoryFeedback(trigger: receipt?.id) { _, new in
            new == nil ? nil : .success
        }
        // Keyed on the drink, so a second quick add restarts the countdown
        // rather than inheriting the remains of the first one's.
        .task(id: receipt?.id) {
            guard receipt != nil else { return }
            try? await Task.sleep(for: .seconds(Self.stripDuration))
            guard !Task.isCancelled else { return }
            dismissStrip()
        }
    }

    /// How long the correction strip stays up.
    ///
    /// Long enough to notice a mis-tap and read the drink's name, short enough
    /// that it is gone before the next round. It covers the list, and the list
    /// is what the screen is for.
    private static let stripDuration: Double = 6

    private func quickAdd() {
        guard let added = store.quickAdd() else { return }
        openRowID = nil
        withAnimation(.easeOut(duration: 0.22)) { receipt = added }
    }

    private func dismissStrip() {
        withAnimation(.easeOut(duration: 0.2)) { receipt = nil }
    }

    /// A widget tap lands here. The clock is caught up first: the app may
    /// have been in the background for hours, and the offer is timed at
    /// `store.now`, which only the Live timer moves.
    private func applyQuickAddRequest() {
        guard quickAddRequest != nil else { return }
        quickAddRequest = nil
        store.tick()
        quickAdd()
    }

    // MARK: Content

    private var content: some View {
        ScrollView {
            VStack(spacing: 14) {
                // Above the day, not inside it: the most likely moment to add
                // someone is a day with nothing on it yet, and a switcher that
                // only appears once a session is running would be missing
                // exactly then. The way back sits on the same row, for the
                // same reason — a dry day is exactly when you look back.
                HStack {
                    yesterdayButton
                    Spacer()
                    if FeatureFlags.shared.multiPerson {
                        PersonSwitcher(store: store)
                    }
                }

                VStack(spacing: 26) {
                    let model = today
                    if model.hasContent {
                        hero
                        DayContentView(
                            model: model,
                            store: store,
                            editingDrink: $editingDrink,
                            openRowID: $openRowID
                        )
                    } else {
                        emptyState
                    }

                    disclaimer
                }
            }
            .padding(.horizontal, 20)
            .padding(.top, 10)
            .padding(.bottom, 100)
        }
        .scrollIndicators(.hidden)
    }

    private var yesterdayButton: some View {
        Button(action: onShowYesterday) {
            HStack(spacing: 4) {
                Image(systemName: "chevron.left")
                    .font(.system(size: 11, weight: .semibold))
                Text("Yesterday")
                    .font(.system(size: 13, weight: .medium, design: .rounded))
            }
            .foregroundStyle(Theme.secondaryText)
            .padding(.horizontal, 10)
            .padding(.vertical, 6)
            .background(Theme.surface, in: Capsule())
        }
        .buttonStyle(.plain)
    }

    // MARK: Hero

    /// The level now — from the running occasion's band, which is also what
    /// the widget shows (5.15). Zero on a day whose curve has already run out.
    private var hero: some View {
        VStack(spacing: 6) {
            BACReadout(store.currentRange, unit: store.unit, limit: store.limit, size: 48)

            (store.currentRange.isPoint ? Text("estimated level") : Text("estimated range"))
                .font(.system(size: 11, weight: .medium, design: .rounded))
                .textCase(.uppercase)
                .foregroundStyle(Theme.secondaryText)
        }
    }

    // MARK: A day with nothing on it
    //
    // Not an error state. For an app about drinking less it is the good
    // outcome — so it says so plainly, without congratulating anyone for an
    // ordinary Tuesday.

    private var emptyState: some View {
        VStack(spacing: 12) {
            Image(systemName: "face.smiling")
                .font(.system(size: 42, weight: .thin))
                .foregroundStyle(Theme.calm.opacity(0.75))

            Text("Nothing logged today")
                .font(.system(size: 16, weight: .medium, design: .rounded))
                .foregroundStyle(Theme.primaryText)
                .multilineTextAlignment(.center)

            Text("Add a drink when you have one.")
                .font(.system(size: 12, design: .rounded))
                .foregroundStyle(Theme.secondaryText)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 30)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 54)
        .background(Theme.surface.opacity(0.5), in: RoundedRectangle(cornerRadius: 18))
        .padding(.top, 40)
    }

    // MARK: Disclaimer

    private var disclaimer: some View {
        VStack(spacing: 6) {
            Text("This is an estimate, not a measurement.")
                .font(.system(size: 11, weight: .semibold, design: .rounded))
                .foregroundStyle(Theme.secondaryText)
            Text("Actual values vary considerably between individuals. Never use this to decide whether you can drive.")
                .font(.system(size: 11, design: .rounded))
                .foregroundStyle(Theme.secondaryText.opacity(0.75))
                .multilineTextAlignment(.center)
        }
        .padding(.horizontal, 10)
    }

    // The add controls live in `QuickAddBar`.
    //
    // They float above the tab bar rather than moving into the navigation bar:
    // logging a drink is the app's most frequent action, and it happens
    // one-handed in a bar. Thumb reach beats tidiness here — which is also why
    // the quick add did not become a long press on the same capsule. A hidden
    // gesture is not a shortcut.
}

#Preview {
    LiveView(store: .preview, quickAddRequest: .constant(nil))
}
