import Foundation
import SwiftData
import Testing
import BACKit
@testable import LogMyDrink

/// Which person a drink ends up on, and which session.
///
/// Every case here used to be impossible: with one person there was nowhere
/// else for a drink to go. They are all silent failures — no crash, no log,
/// just a row on the wrong evening or a number computed from the wrong body.
@MainActor
@Suite("Session routing")
struct SessionRoutingTests {

    @Test("A drink goes to the active person")
    func drinkFollowsActivePerson() throws {
        let store = try makeStore()
        let guest = store.addPerson(
            name: "Guest",
            profile: BodyProfile(sex: .female, age: 29, heightCm: 166, weightKg: 58),
            frequency: .occasional,
            limit: 0.8
        )

        // addPerson switches over, which is the behaviour the sheet relies on.
        #expect(store.person.id == guest.id)

        store.add(.beer(at: .now.addingTimeInterval(-600)))

        #expect(store.session?.personID == guest.id)
        #expect(store.drinks.count == 1)
    }

    @Test("Switching back shows the owner's session, not the guest's")
    func switchingSwapsTheOpenSession() throws {
        let store = try makeStore()
        let owner = store.owner

        store.add(.beer(at: .now.addingTimeInterval(-3600)))
        let ownersSession = try #require(store.session)

        let guest = store.addPerson(
            name: "Guest",
            profile: BodyProfile(sex: .female, age: 29, heightCm: 166, weightKg: 58),
            frequency: .occasional,
            limit: 0.8
        )
        store.add(.beer(at: .now.addingTimeInterval(-1800)))
        let guestsSession = try #require(store.session)

        #expect(guestsSession.id != ownersSession.id)
        #expect(store.drinks.count == 1)

        store.activate(owner)

        #expect(store.session?.id == ownersSession.id)
        #expect(store.drinks.count == 1)
        #expect(guest.sessions?.count == 1)
    }

    @Test("A backdated drink does not land in the other person's evening")
    func backdatedDrinkStaysWithItsPerson() throws {
        let store = try makeStore()
        let owner = store.owner
        let threeWeeksAgo = Date.now.addingTimeInterval(-21 * 24 * 3600)

        // The guest drank that evening.
        let guest = store.addPerson(
            name: "Guest",
            profile: BodyProfile(sex: .female, age: 29, heightCm: 166, weightKg: 58),
            frequency: .occasional,
            limit: 0.8
        )
        store.add(.beer(at: threeWeeksAgo))
        let hers = try #require(guest.sessions?.first)

        // The owner fills in his own drink from the same evening, weeks later.
        store.activate(owner)
        store.add(.beer(at: threeWeeksAgo.addingTimeInterval(1800)))

        let ownersSessions = owner.sessions ?? []
        #expect(ownersSessions.count == 1)
        #expect(ownersSessions.first?.id != hers.id)
        // Her evening stays one drink long. Without the person filter this is
        // where the owner's beer would have silently appeared.
        #expect(hers.drinks?.count == 1)
    }

    @Test("A backdated session freezes its own person's body, not the nearest one")
    func backdatedSessionUsesOwnProfile() throws {
        let store = try makeStore()
        let owner = store.owner
        let sixMonthsAgo = Date.now.addingTimeInterval(-180 * 24 * 3600)

        // A guest session sits closest in time to the drink about to be added.
        let guest = store.addPerson(
            name: "Guest",
            profile: BodyProfile(sex: .female, age: 29, heightCm: 166, weightKg: 58),
            frequency: .occasional,
            limit: 0.8
        )
        store.add(.beer(at: sixMonthsAgo))

        store.activate(owner)
        store.add(.beer(at: sixMonthsAgo.addingTimeInterval(3 * 24 * 3600)))

        let backdated = try #require(owner.sessions?.first)
        // 58 kg here would mean the curve describes an evening that never
        // happened — and nothing on screen would look wrong.
        #expect(backdated.weightKg == owner.profile.weightKg)
        #expect(backdated.sexRaw == Sex.male.rawValue)
        #expect(guest.sessions?.first?.weightKg == 58)
    }

    @Test("An inactive person's evening gets its clearing time and summary too")
    func normalizesSessionsOfEveryone() throws {
        let store = try makeStore()
        let owner = store.owner

        let guest = store.addPerson(
            name: "Guest",
            profile: BodyProfile(sex: .female, age: 29, heightCm: 166, weightKg: 58),
            frequency: .occasional,
            limit: 0.8
        )
        store.add(.beer(at: .now.addingTimeInterval(-3600)))
        let hers = try #require(guest.sessions?.first)
        #expect(hers.isRunning(at: .now))
        #expect(hers.endedAt != nil)          // derived at once, not a status

        store.activate(owner)

        // Two days later, from the owner's side of the app.
        store.now = .now.addingTimeInterval(48 * 3600)
        store.refreshFromStore()

        // Her evening is over by the curve, and listed with its figures —
        // nothing had to "close" it.
        #expect(!hers.isRunning(at: store.now))
        #expect(hers.summary != nil)
    }

    // MARK: The curve decides what belongs together

    /// The case the whole design is for: a heavy night, and a beer the next
    /// afternoon with 0.2 ‰ of it still there. Grouped by drinking day, the
    /// beer opened a second session from zero.
    @Test("A beer the afternoon after a heavy night joins that night")
    func carryOverJoinsTheNight() throws {
        let store = try makeStore()
        let calendar = Calendar.current
        // Yesterday 17:00 by the clock, so the night and the afternoon fall
        // on different drinking days whatever time the test runs.
        let yesterday = calendar.date(byAdding: .day, value: -1, to: store.now)!
        let evening = calendar.date(bySettingHour: 17, minute: 0, second: 0, of: yesterday)!
        store.now = evening.addingTimeInterval(21 * 3600)   // 14:00 the next day

        for i in 0..<10 {
            store.add(.beer(at: evening.addingTimeInterval(Double(i) * 40 * 60)))
        }
        let night = try #require(store.session)
        #expect(night.isRunning(at: store.now))
        #expect(store.currentBAC > 0.05)

        store.add(.beer(at: store.now))

        #expect(store.owner.sessions?.count == 1)
        #expect(store.session?.id == night.id)
        #expect(store.drinks.count == 11)
    }

    @Test("A drink after the body has long cleared starts a new session")
    func clearedBodyStartsNew() throws {
        let store = try makeStore()
        store.add(.beer(at: store.now.addingTimeInterval(-30 * 3600)))
        store.add(.beer(at: store.now))

        #expect(store.owner.sessions?.count == 2)
        #expect(store.drinks.count == 1)
    }

    @Test("Deleting the drink that bridged two halves splits the session")
    func deletionSplits() throws {
        let store = try makeStore()
        let base = store.now.addingTimeInterval(-12 * 3600)
        let bridge = Drink.beer(at: base.addingTimeInterval(5 * 3600))
        for drink in [
            Drink.beer(at: base), .beer(at: base.addingTimeInterval(3600)),
            bridge,
            .beer(at: base.addingTimeInterval(9 * 3600)), .beer(at: base.addingTimeInterval(10 * 3600)),
        ] {
            store.add(drink)
        }
        #expect(store.owner.sessions?.count == 1)

        store.remove(bridge)

        let sessions = (store.owner.sessions ?? []).sorted { $0.startedAt < $1.startedAt }
        #expect(sessions.count == 2)
        #expect(sessions[0].drinks?.count == 2)
        #expect(sessions[1].drinks?.count == 2)
        #expect(sessions[1].startedAt == base.addingTimeInterval(9 * 3600))
    }

    @Test("A backdated drink that bridges two sessions merges them")
    func backdatedDrinkMerges() throws {
        let store = try makeStore()
        let base = store.now.addingTimeInterval(-12 * 3600)
        store.add(.beer(at: base))
        store.add(.beer(at: base.addingTimeInterval(7 * 3600)))
        #expect(store.owner.sessions?.count == 2)

        // Two beers in between keep the level up across the gap.
        store.add(.beer(at: base.addingTimeInterval(2.5 * 3600)))
        store.add(.beer(at: base.addingTimeInterval(5 * 3600)))

        let sessions = store.owner.sessions ?? []
        #expect(sessions.count == 1)
        #expect(sessions.first?.drinks?.count == 4)
        #expect(sessions.first?.startedAt == base)
    }

    @Test("The running session is whichever covers now, and lets go when it clears")
    func runningFollowsTheClock() throws {
        let store = try makeStore()
        store.add(.beer(at: store.now))
        #expect(store.session != nil)

        store.tick(to: store.now.addingTimeInterval(8 * 3600))

        #expect(store.session == nil)
        #expect(store.drinks.isEmpty)
        #expect(store.owner.sessions?.count == 1)   // still history
    }

    @Test("Deleting the last drink removes the session, and only that one")
    func deletingLastDrinkKeepsOtherPeople() throws {
        let store = try makeStore()
        let owner = store.owner

        let guest = store.addPerson(
            name: "Guest",
            profile: BodyProfile(sex: .female, age: 29, heightCm: 166, weightKg: 58),
            frequency: .occasional,
            limit: 0.8
        )
        store.add(.beer(at: .now.addingTimeInterval(-1800)))

        store.activate(owner)
        let mine = Drink.beer(at: .now.addingTimeInterval(-1200))
        store.add(mine)
        store.remove(mine)

        #expect(store.session == nil)
        #expect(owner.sessions?.isEmpty == true)
        #expect(guest.sessions?.count == 1)
    }

    @Test("The profile screen edits the selected person")
    func profileEditsFollowTheActivePerson() throws {
        let store = try makeStore()
        let owner = store.owner
        let guest = store.addPerson(
            name: "Guest",
            profile: BodyProfile(sex: .female, age: 29, heightCm: 166, weightKg: 58),
            frequency: .occasional,
            limit: 0.8
        )

        store.profile.weightKg = 60
        store.limit = 0.5

        #expect(guest.weightKg == 60)
        #expect(guest.limit == 0.5)
        #expect(owner.weightKg == 80)
        #expect(owner.limit == 0.8)
    }
}
