import SwiftUI
import BACKit

/// One past evening, reached from the history list.
///
/// The content is shared with the Live screen — see `SessionContentView`.
/// This is only the navigation wrapper around it, and it stays the bottom of
/// the history drill-down: year → month → week → day → this.
struct SessionDetailView: View {
    let session: DrinkingSession
    let store: SessionStore

    /// Read once, at construction: a title read from a model that has since
    /// been deleted would fault.
    private let title: String

    init(session: DrinkingSession, store: SessionStore) {
        self.session = session
        self.store = store
        self.title = session.startedAt.formatted(date: .abbreviated, time: .omitted)
    }

    @State private var editingDrink: Drink?
    @State private var openRowID: UUID?
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        ZStack {
            Theme.background.ignoresSafeArea()

            ScrollView {
                // The session can cease to exist under this screen: editing
                // a drink's time can merge it into the evening before
                // (`SessionStore.normalize`), and deleting its last drink
                // removes it. Neither is a model to keep reading.
                if !session.isGone {
                    SessionContentView(
                        session: session,
                        store: store,
                        editingDrink: $editingDrink,
                        openRowID: $openRowID
                    )
                    .padding(.horizontal, 20)
                    .padding(.vertical, 16)
                }
            }
            .scrollIndicators(.hidden)
        }
        .onChange(of: store.revision) {
            if session.isGone { dismiss() }
        }
        .navigationTitle(Text(verbatim: title))
        .navigationBarTitleDisplayMode(.inline)
        .sheet(item: $editingDrink) { drink in
            AddDrinkSheet(store: store, editing: drink, session: session)
        }
        .onChange(of: editingDrink?.id) { openRowID = nil }
    }
}
