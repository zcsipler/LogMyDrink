import Foundation
import SwiftData
import Testing
import BACKit
@testable import LogMyDrink

/// The migration that gives every session an owner.
///
/// None of the failures here crash or log anything. A session that keeps the
/// unassigned id is not deleted — it is simply invisible, because every query
/// in the app filters by person. That is what "losing data" means in this
/// codebase, and it is why these cases are worth a test each.
@MainActor
@Suite("Person migration")
struct PersonMigrationTests {

    // MARK: Creating the owner

    @Test("An empty database gets exactly one owner")
    func createsOwner() throws {
        let context = try makeContext()

        let owner = PersonMigration.run(in: context)
        let people = try context.fetch(FetchDescriptor<Person>())

        #expect(people.count == 1)
        #expect(owner.isOwner)
        #expect(people.first?.id == owner.id)
    }

    @Test("Running twice does not create a second owner")
    func isIdempotent() throws {
        let context = try makeContext()

        let first = PersonMigration.run(in: context)
        let second = PersonMigration.run(in: context)

        #expect(first.id == second.id)
        #expect(try context.fetch(FetchDescriptor<Person>()).count == 1)
    }

    @Test("A fresh owner starts tracking now, with a frequency that matches its beta")
    func freshOwnerIsConsistent() {
        let before = Date.now
        let owner = PersonMigration.makeOwner()

        // The body is a placeholder the user will replace; what must hold is
        // that nothing about the new person contradicts itself — a frequency
        // that implies a different beta than the profile carries would make
        // the Profile screen disagree with the curve on first launch.
        #expect(owner.isOwner)
        #expect(owner.frequency == .closest(toBeta: owner.profile.beta))
        #expect(owner.trackingStartedAt >= before)
    }

    // MARK: Adopting sessions

    @Test("A session with no person is adopted by the owner")
    func adoptsOrphan() throws {
        let context = try makeContext()
        let orphan = DrinkingSession(startedAt: .now, profile: .test, limit: 0.8)
        context.insert(orphan)
        #expect(orphan.personID == Person.unassignedID)

        let owner = PersonMigration.run(in: context)

        #expect(orphan.personID == owner.id)
        #expect(orphan.person?.id == owner.id)
    }

    @Test("An already assigned session is left alone")
    func doesNotStealAssignedSessions() throws {
        let context = try makeContext()
        let owner = PersonMigration.run(in: context)
        let guest = makeGuest(in: context)

        let hers = DrinkingSession(startedAt: .now, person: guest, profile: .test, limit: 0.8)
        context.insert(hers)

        PersonMigration.run(in: context)

        #expect(hers.personID == guest.id)
        #expect(hers.personID != owner.id)
    }

    // MARK: Two owners

    @Test("Two owners are merged, and the sessions follow")
    func mergesDuplicateOwners() throws {
        let context = try makeContext()

        let earlier = Person(
            isOwner: true,
            createdAt: Date(timeIntervalSince1970: 1_000),
            profile: .test,
            frequency: .occasional,
            limit: 0.8,
            trackingStartedAt: Date(timeIntervalSince1970: 5_000)
        )
        let later = Person(
            isOwner: true,
            createdAt: Date(timeIntervalSince1970: 2_000),
            profile: .test,
            frequency: .occasional,
            limit: 0.8,
            trackingStartedAt: Date(timeIntervalSince1970: 3_000)
        )
        context.insert(earlier)
        context.insert(later)

        let strandedSession = DrinkingSession(startedAt: .now, person: later, profile: .test, limit: 0.8)
        context.insert(strandedSession)

        let owner = PersonMigration.run(in: context)
        let people = try context.fetch(FetchDescriptor<Person>())

        // Without the merge the user sees two identical "You" entries and
        // half their history behind the one they cannot reach.
        #expect(people.count == 1)
        #expect(owner.id == earlier.id)
        #expect(strandedSession.personID == earlier.id)
        // The surviving owner keeps the earliest start of records.
        #expect(owner.trackingStartedAt == Date(timeIntervalSince1970: 3_000))
    }

    @Test("A database with people but no owner promotes the oldest")
    func promotesOldestWhenNoOwner() throws {
        let context = try makeContext()
        let older = Person(
            createdAt: Date(timeIntervalSince1970: 1_000),
            profile: .test, frequency: .occasional, limit: 0.8
        )
        let newer = Person(
            createdAt: Date(timeIntervalSince1970: 2_000),
            profile: .test, frequency: .occasional, limit: 0.8
        )
        context.insert(older)
        context.insert(newer)

        let owner = PersonMigration.run(in: context)

        #expect(owner.id == older.id)
        #expect(try context.fetch(FetchDescriptor<Person>()).count == 2)
    }
}
