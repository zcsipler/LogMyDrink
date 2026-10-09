import SwiftUI
import BACKit

/// Logging a drink — and, more importantly, the live projection of where it
/// would take the curve.
///
/// The decision is made before the drink is poured, so the projected peak
/// belongs here rather than on the main screen afterwards.
///
/// The same sheet corrects an already logged drink. Passing `editing` prefills
/// every control and switches the wording; the projection then compares the
/// session without that drink against the session with the corrected version.
struct AddDrinkSheet: View {
    let store: SessionStore

    /// Non-nil when correcting a drink that is already in the session.
    let editing: Drink?

    /// Which session the drink belongs to, when the caller knows. Nil lets
    /// the store decide by the curve: for a new drink, the occasion whose
    /// level is still up at that time; for an edit, the session holding the
    /// drink. The history detail passes its past session explicitly so the
    /// projection is made against that evening's own profile snapshot.
    let session: DrinkingSession?

    /// The past drinking day a new drink is being filled in for, when it is
    /// added from the History day page rather than logged as it happens.
    ///
    /// The day is fixed and the time is the question: the stepper and the
    /// wheel are limited to that day, and there is no "another day" link.
    let day: DrinkingDay?

    @Environment(\.dismiss) private var dismiss

    @State private var template: DrinkTemplate
    @State private var volumeMl: Double
    @State private var abv: Double
    @State private var stomach: StomachState
    @State private var drinkingMinutes: Double
    @State private var consumedAt: Date

    /// The exact-time sheet (`TimePickerSheet`), opened by tapping the time.
    @State private var showsTimePicker = false

    /// The drinking day the hour–minute wheel places its time on. Fixed while
    /// the wheel is out: derived from `consumedAt` on every spin, a time
    /// crossing the five o'clock boundary would move the day under the wheel
    /// and land a whole day away from what was dialled.
    @State private var wheelDay: DrinkingDay

    /// A stable identifier, so that dragging a slider does not mint a new
    /// drink-equivalent object on every redraw. When editing, this is the
    /// existing drink's id, which is what lets `update(_:)` find it.
    @State private var draftID: UUID

    init(
        store: SessionStore,
        editing: Drink? = nil,
        session: DrinkingSession? = nil,
        day: DrinkingDay? = nil
    ) {
        self.store = store
        self.editing = editing
        self.session = session
        self.day = day

        let template = editing.map(DrinkCatalog.template(for:)) ?? DrinkCatalog.all[0]
        _template = State(initialValue: template)
        _volumeMl = State(initialValue: editing?.volumeMl ?? template.defaultVolumeMl)
        _abv = State(initialValue: editing?.abvPercent ?? template.defaultAbv)
        _stomach = State(initialValue: editing?.stomach ?? .light)
        _drinkingMinutes = State(
            initialValue: editing?.drinkingMinutes ?? template.defaultDrinkingMinutes
        )
        let consumedAt = editing?.consumedAt
            ?? day.map { Self.startingTime(on: $0, now: store.now) }
            ?? .now
        _consumedAt = State(initialValue: consumedAt)
        _draftID = State(initialValue: editing?.id ?? UUID())
        _wheelDay = State(initialValue: day ?? DrinkingDay.containing(consumedAt))
    }

    private var isEditing: Bool { editing != nil }

    /// Where the time wheel starts on a day being filled in: the clock time
    /// right now, placed on that day — the convention every iOS date picker
    /// follows, and a rule the user can see through at a glance.
    ///
    /// It used to be cleverer: the end of the day's last drink, or 20:00 on
    /// an empty day. Clever read as random — a drink at 01:13 plus its half
    /// hour offered "01:43" with nothing on screen to say why. A starting
    /// point for spinning does not have to be a good guess; it has to be
    /// obvious.
    private static func startingTime(on day: DrinkingDay, now: Date) -> Date {
        Self.place(clockTimeOf: now, on: day, now: now)
    }

    /// A clock time, placed on the drinking day by the rule the whole app
    /// files evenings under days (5.6): hours from the boundary on are that
    /// evening, hours before it are the small hours after its midnight.
    private static func place(clockTimeOf picked: Date, on day: DrinkingDay, now: Date) -> Date {
        let calendar = Calendar.current
        let parts = calendar.dateComponents([.hour, .minute], from: picked)
        let hour = parts.hour ?? 0
        let anchor = hour >= DrinkingDay.boundaryHour
            ? day.start
            : calendar.date(byAdding: .day, value: 1, to: day.start) ?? day.start
        let placed = calendar.date(
            bySettingHour: hour, minute: parts.minute ?? 0, second: 0, of: anchor
        ) ?? picked
        return min(max(placed, day.start), Self.latestTime(on: day, now: now))
    }

    /// The last moment a drink on this day could have been had: the end of
    /// the drinking day, or now if the day is still running.
    private static func latestTime(on day: DrinkingDay, now: Date) -> Date {
        min(day.end.addingTimeInterval(-60), now)
    }

    /// The simulation is not cheap — six RK4 runs — and the body reads this
    /// from nine places. `SessionStore.project` keeps the last answer, so the
    /// repeats are a comparison of eight drinks rather than six simulations.
    ///
    /// It used to be cached here instead, in a `@State` filled by `onAppear`,
    /// with a direct call as the fallback while it was still nil. That fallback
    /// was the whole first render: every one of those nine reads ran the
    /// projection, the sheet took seconds to appear, and the cache it was
    /// meant to protect only arrived afterwards. A cache that the caller can
    /// silently miss is the wrong place for one.
    private var projection: BandedProjection {
        store.project(candidate, excluding: editing?.id, in: session)
    }

    /// The limit the projection is judged against — a past session's own, not
    /// today's, for the same reason its profile snapshot is used.
    private var limit: Double { session?.limit ?? store.limit }

    private var candidate: Drink {
        Drink(
            id: draftID,
            consumedAt: consumedAt,
            volumeMl: volumeMl,
            abvPercent: abv,
            stomach: stomach,
            drinkingMinutes: drinkingMinutes,
            name: template.id
        )
    }

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 22) {
                    // The drink first — what, how much, how strong — then
                    // its two time inputs side by side, then the stomach.
                    // The type stays first because for most people it is the
                    // first question (5.10); when and how fast are one block
                    // because they are the same kind of fact about the drink,
                    // and together they are the fields most often changed
                    // from their defaults. Stomach state is last: it rarely
                    // leaves "moderate", and the quick-add receipt lets it be
                    // corrected afterwards.
                    typePicker
                    measureSection
                    timeBlock
                    stomachSection
                    setDefaultButton
                }
                .padding(.horizontal, 20)
                .padding(.bottom, 16)
            }
            .background(Theme.background)
            .scrollIndicators(.hidden)
            .navigationTitle(isEditing ? Text("Edit drink") : Text("Add drink"))
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                        .foregroundStyle(Theme.secondaryText)
                }
            }
            .safeAreaInset(edge: .bottom) { confirmBar }
        }
        .preferredColorScheme(.dark)
    }

    // MARK: Projection
    //
    // Lives above the Add button rather than at the top of the sheet. The
    // projected peak is not what you pick a drink by — you already know you
    // want a beer — so putting it first only pushed the type picker below the
    // fold. At the button it sits where the decision actually happens, and the
    // one part that earns its place before committing, the limit warning,
    // grows out of it when there is something to say.

    private var projectionSummary: some View {
        HStack(alignment: .center, spacing: 14) {
            VStack(alignment: .leading, spacing: 2) {
                Text(isEditing ? "With this" : "Projected peak")
                    .font(.system(size: 9, weight: .semibold, design: .rounded))
                    .textCase(.uppercase)
                    .foregroundStyle(Theme.secondaryText)

                BACReadout(projection.peakRange, unit: store.unit, limit: limit, size: 22)
            }

            Spacer(minLength: 0)

            VStack(alignment: .trailing, spacing: 3) {
                miniStat("Peak at", projection.peakDate.hourMinute)
                miniStat("Clears", projection.soberRange?.hourMinuteRange ?? "—")
            }
        }
        .animation(.easeOut(duration: 0.18), value: projection.peakRange.upperBound)
    }

    private func miniStat(_ title: LocalizedStringKey, _ value: String) -> some View {
        HStack(spacing: 5) {
            Text(title)
                .font(.system(size: 9, weight: .semibold, design: .rounded))
                .textCase(.uppercase)
                .foregroundStyle(Theme.secondaryText)
            Text(verbatim: value)
                .font(.system(size: 12, weight: .medium, design: .rounded).monospacedDigit())
                .foregroundStyle(Theme.primaryText)
        }
    }

    private var outcomeTint: Color {
        switch projection.outcome {
        case .below: Theme.calm
        case .uncertain: Theme.caution
        case .above: Theme.alarm
        }
    }

    /// Three-state warning.
    ///
    /// The uncertainty leaves a middle case that would be dishonest to round
    /// in either direction: slow elimination crosses the limit, fast does not.
    /// There "might cross" is the accurate claim, not "would cross".
    private var limitWarning: some View {
        HStack(spacing: 8) {
            Image(systemName: projection.outcome == .above
                  ? "exclamationmark.triangle.fill"
                  : "questionmark.circle.fill")
                .font(.system(size: 12))

            VStack(alignment: .leading, spacing: 2) {
                if projection.outcome == .above {
                    Text("This would cross your limit")
                        .font(.system(size: 13, weight: .semibold, design: .rounded))
                    Text("Around \(crossingTime), for up to \(projection.maxTimeAboveLimit.compactDuration).")
                        .font(.system(size: 11, design: .rounded))
                        .foregroundStyle(outcomeTint.opacity(0.85))
                        .fixedSize(horizontal: false, vertical: true)
                } else {
                    Text("This might cross your limit")
                        .font(.system(size: 13, weight: .semibold, design: .rounded))
                    Text("With slower metabolism yes, with faster no. That's the uncertainty of the estimate.")
                        .font(.system(size: 11, design: .rounded))
                        .foregroundStyle(outcomeTint.opacity(0.85))
                        .fixedSize(horizontal: false, vertical: true)
                }
            }
            Spacer()
        }
        .foregroundStyle(outcomeTint)
        .padding(10)
        .background(outcomeTint.opacity(0.12), in: RoundedRectangle(cornerRadius: 11))
    }

    private var crossingTime: String {
        projection.limitCrossedAt?.hourMinute ?? candidate.consumedAt.hourMinute
    }

    // MARK: Drink type, amount and strength
    //
    // The controls themselves live in `DrinkControls`, because the favourite
    // editor needs the same ones and a second copy would drift.

    private var typePicker: some View {
        DrinkTypePicker(template: $template) { item in
            volumeMl = item.defaultVolumeMl
            abv = item.defaultAbv
            drinkingMinutes = item.defaultDrinkingMinutes
        }
    }

    private var measureSection: some View {
        DrinkMeasureControls(template: template, volumeMl: $volumeMl, abv: $abv)
    }

    // MARK: Stomach state

    private var stomachSection: some View {
        ControlSection("Stomach") {
            VStack(spacing: 10) {
                HStack(spacing: 8) {
                    ForEach(StomachState.allCases, id: \.self) { state in
                        Button {
                            withAnimation(.easeOut(duration: 0.15)) { stomach = state }
                        } label: {
                            // Icon beside the label, not above it: three
                            // chips of one line each fit the row in every
                            // language, and the section drops to the height
                            // of the steppers around it.
                            HStack(spacing: 6) {
                                Image(systemName: state.icon)
                                    .font(.system(size: 13))
                                Text(state.shortLabel)
                                    .font(.system(size: 12, weight: .medium, design: .rounded))
                                    .lineLimit(1)
                                    .minimumScaleFactor(0.75)
                            }
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 11)
                            .padding(.horizontal, 4)
                            .background(
                                stomach == state ? Theme.calm.opacity(0.18) : Theme.surface,
                                in: RoundedRectangle(cornerRadius: 12)
                            )
                            .overlay {
                                RoundedRectangle(cornerRadius: 12)
                                    .stroke(stomach == state ? Theme.calm : Theme.hairline, lineWidth: 1)
                            }
                            .foregroundStyle(stomach == state ? Theme.calm : Theme.primaryText)
                        }
                        .buttonStyle(.plain)
                    }
                }

                Text(stomach.explanation)
                    .font(.system(size: 11, design: .rounded))
                    .foregroundStyle(Theme.secondaryText)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .transition(.opacity)
                    .id(stomach)
            }
        }
    }

    // MARK: When and how fast
    //
    // Side by side, because they are the same kind of fact — the drink's
    // footprint in time — and because a stepper is half a row wide. Each is
    // a `TimeStepper`: a tap is five minutes, holding runs. Tapping the time
    // itself opens a small sheet from the bottom with the hour–minute wheel
    // and, where the day is up for change, a date — rather than unfolding
    // under the row, which pushed the stomach section and the favourite
    // button down every time. The confirm bar is pinned, so the projection
    // stays in view either way.

    private var timeBlock: some View {
        HStack(alignment: .top, spacing: 12) {
            whenSection
            paceSection
        }
        .sensoryFeedback(.selection, trigger: consumedAt)
        .sheet(isPresented: $showsTimePicker) {
            TimePickerSheet(
                time: timeOnDay,
                date: dateOnly,
                canChangeDay: day == nil,
                latest: latestStart
            )
        }
    }

    private var whenSection: some View {
        ControlSection("When") {
            VStack(alignment: .leading, spacing: 8) {
                TimeStepper(
                    canDecrement: canStepBack,
                    canIncrement: canStepForward,
                    onStep: stepTime,
                    onTapValue: openTimePicker,
                    value: { Text(verbatim: consumedAt.hourMinute) }
                )

                Text(verbatim: timeCaption)
                    .font(.system(size: 11, design: .rounded))
                    .foregroundStyle(Theme.secondaryText)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .fixedSize(horizontal: false, vertical: true)
            }
        }
    }

    private var paceSection: some View {
        DrinkPaceControl(drinkingMinutes: $drinkingMinutes)
    }

    /// Under the time: how long ago, when it is today's — the offset is the
    /// thing being dialled, and adding it up in one's head is the work the
    /// stepper was meant to remove; otherwise the calendar date, the one
    /// thing an hour–minute display cannot say. Filling in a day, always
    /// the date, since the whole point of that page is which day it is.
    private var timeCaption: String {
        if day == nil, DrinkingDay.containing(consumedAt).isCurrent(at: store.now) {
            return isNow
                ? String(localized: "Now")
                : consumedAt.formatted(.relative(presentation: .numeric))
        }
        return consumedAt.formatted(.dateTime.weekday(.abbreviated).month(.abbreviated).day())
    }

    private var isNow: Bool {
        abs(consumedAt.timeIntervalSince(Date.now)) < 60
    }

    /// The last moment the drink could have started: the end of the day
    /// being filled in, or now. Disabling "+" at that point is what says
    /// "now" — no separate button needed.
    private var latestStart: Date {
        day.map { Self.latestTime(on: $0, now: store.now) } ?? Date.now
    }

    private var canStepForward: Bool {
        consumedAt < latestStart.addingTimeInterval(-30)
    }

    /// Backwards is unbounded when logging live or editing: the five o'clock
    /// boundary is not a wall, an hour before half past five in the morning
    /// is still that night, and the store files it there. A day being filled
    /// in is bounded by its own start.
    private var canStepBack: Bool {
        guard let day else { return true }
        return consumedAt > day.start.addingTimeInterval(30)
    }

    /// Moves to the next five-minute mark that way, with the seconds dropped.
    private func stepTime(_ direction: Int) {
        let calendar = Calendar.current
        let parts = calendar.dateComponents([.hour, .minute], from: consumedAt)
        let minuteOfDay = Double((parts.hour ?? 0) * 60 + (parts.minute ?? 0))
        let delta = StepGrid.snapped(minuteOfDay, stepping: direction) - minuteOfDay

        let onTheMinute = calendar.date(bySetting: .second, value: 0, of: consumedAt) ?? consumedAt
        var next = onTheMinute.addingTimeInterval(delta * 60)
        next = min(next, latestStart)
        if let day { next = max(next, day.start) }
        consumedAt = next
    }

    /// The wheel's view of `consumedAt`: a clock time, placed on `wheelDay`.
    /// So spinning to 01:43 on the page called Yesterday lands on the morning
    /// after, without anyone having to know that a drinking day starts at
    /// five.
    private var timeOnDay: Binding<Date> {
        Binding(
            get: { consumedAt },
            set: { picked in
                consumedAt = Self.place(clockTimeOf: picked, on: wheelDay, now: store.now)
            }
        )
    }

    /// The date part alone, for the sheet's day picker. Setting it keeps
    /// the clock time and moves the day; the wheel then places its times on
    /// the new day.
    private var dateOnly: Binding<Date> {
        Binding(
            get: { consumedAt },
            set: { picked in
                let calendar = Calendar.current
                let clock = calendar.dateComponents([.hour, .minute], from: consumedAt)
                let moved = calendar.date(
                    bySettingHour: clock.hour ?? 0, minute: clock.minute ?? 0, second: 0, of: picked
                ) ?? picked
                consumedAt = min(moved, latestStart)
                wheelDay = DrinkingDay.containing(consumedAt)
            }
        )
    }

    /// Opening the wheel fixes the day it spins on to the one the time is on
    /// right now — after stepping, that may no longer be the day the sheet
    /// opened with.
    private func openTimePicker() {
        wheelDay = day ?? DrinkingDay.containing(consumedAt)
        showsTimePicker = true
    }

    // MARK: The usual one
    //
    // Here rather than only in the profile, because this is where the answer is
    // already typed in. Someone who has just dialled in a 400 ml at 4.5 % has
    // described their usual drink; asking them to go and do it again in a
    // settings screen is how a feature ends up unused.
    //
    // It writes immediately and does not wait for Add: setting what you usually
    // drink and logging one are separate acts, and an edit of a drink from last
    // Tuesday is a perfectly good moment to do the first without the second.
    //
    // Only the four fields a favourite carries. The time and the stomach state
    // belong to this drink, not to the habit (see `FavouriteDrink`).

    private var draftFavourite: FavouriteDrink {
        FavouriteDrink(
            templateID: template.id,
            volumeMl: volumeMl,
            abvPercent: abv,
            drinkingMinutes: drinkingMinutes
        )
    }

    private var isFavourite: Bool { store.favourite == draftFavourite }

    private var setDefaultButton: some View {
        Button {
            withAnimation(.easeOut(duration: 0.15)) { store.favourite = draftFavourite }
        } label: {
            HStack(spacing: 8) {
                Image(systemName: isFavourite ? "star.fill" : "star")
                    .font(.system(size: 13))
                if isFavourite {
                    Text("This is your quick-add drink")
                } else {
                    Text("Set as my quick-add drink")
                }
                Spacer()
            }
            .font(.system(size: 13, weight: .medium, design: .rounded))
            .foregroundStyle(isFavourite ? Theme.secondaryText : Theme.calm)
            .padding(.horizontal, 14)
            .padding(.vertical, 12)
            .background(Theme.surface, in: RoundedRectangle(cornerRadius: 12))
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
        .disabled(isFavourite)
    }

    // MARK: Confirmation

    private var confirmBar: some View {
        VStack(spacing: 12) {
            if projection.outcome.exceedsPossible {
                limitWarning
            }

            projectionSummary

            Button {
                if isEditing {
                    store.update(candidate, in: session)
                } else {
                    store.add(candidate)
                }
                dismiss()
            } label: {
                HStack {
                    Image(systemName: isEditing ? "checkmark.circle.fill" : "plus.circle.fill")
                    if isEditing {
                        Text("Save changes")
                    } else {
                        Text("Add")
                    }
                }
                .font(.system(size: 16, weight: .semibold, design: .rounded))
                .foregroundStyle(Theme.background)
                .frame(maxWidth: .infinity)
                .padding(.vertical, 15)
                .background(Theme.tint(for: projection.peakRange.upperBound, limit: limit), in: Capsule())
            }
            .buttonStyle(.plain)
        }
        .padding(.horizontal, 20)
        .padding(.top, 12)
        .padding(.bottom, 8)
        .background(.ultraThinMaterial)
        .overlay(alignment: .top) {
            Rectangle().fill(Theme.hairline).frame(height: 1)
        }
    }
}

// MARK: - Exact time

/// The hour–minute wheel, and the day when it is up for change, on a short
/// sheet from the bottom.
///
/// A sheet rather than unfolding in place: the wheel is 200 pt tall, and in
/// place it pushed everything under it down each time; here the form behind
/// stays where it was and the sheet has its own Done. The modern form of the
/// picker that used to rise from the bottom in UIKit — a detent, not an
/// input view.
///
/// The day is a separate, plain date picker under the wheel, not a date
/// column in the wheel itself: the wheel's day is the drinking day, which
/// starts at five in the morning, and a date column would have said "Today"
/// for a drink at 01:43 that belongs to yesterday's evening. The two bindings
/// keep that apart — `time` places a clock time on the drinking day, `date`
/// moves the day and keeps the clock time.
private struct TimePickerSheet: View {
    @Binding var time: Date
    @Binding var date: Date

    /// False when filling in a History day, which chose the day already.
    let canChangeDay: Bool

    /// Now, or the end of the day being filled in.
    let latest: Date

    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                DatePicker(selection: $time, displayedComponents: [.hourAndMinute]) {
                    Text("When")
                }
                .datePickerStyle(.wheel)
                .labelsHidden()
                .frame(maxWidth: .infinity)
                .tint(Theme.calm)

                if canChangeDay {
                    HStack {
                        Text("Day")
                            .font(.system(size: 15, design: .rounded))
                            .foregroundStyle(Theme.primaryText)
                        Spacer()
                        DatePicker(
                            selection: $date,
                            in: .distantPast...latest,
                            displayedComponents: [.date]
                        ) {
                            Text("Day")
                        }
                        .datePickerStyle(.compact)
                        .labelsHidden()
                        .tint(Theme.calm)
                    }
                    .padding(.horizontal, 14)
                    .padding(.vertical, 10)
                    .background(Theme.surface, in: RoundedRectangle(cornerRadius: 12))
                }

                Spacer(minLength: 0)
            }
            .padding(.horizontal, 20)
            .padding(.top, 8)
            .background(Theme.background)
            .navigationTitle(Text("When"))
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Done") { dismiss() }
                        .foregroundStyle(Theme.calm)
                }
            }
        }
        .presentationDetents([.height(canChangeDay ? 360 : 300)])
        .presentationDragIndicator(.visible)
        .preferredColorScheme(.dark)
    }
}

@MainActor
private struct EditSheetPreview: View {
    private let store = SessionStore.preview

    var body: some View {
        AddDrinkSheet(store: store, editing: store.drinks.last)
    }
}

#Preview("Add") {
    AddDrinkSheet(store: .preview)
}

#Preview("Edit") {
    EditSheetPreview()
}
