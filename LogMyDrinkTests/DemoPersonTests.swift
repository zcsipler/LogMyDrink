import Foundation
import SwiftData
import Testing
import BACKit
@testable import LogMyDrink

/// The debug demo: where its dates land, and that it never leaves in a backup.
@MainActor
@Suite("Demo person")
struct DemoPersonTests {

    /// Budapest, because it has a daylight-saving change to get wrong.
    private let calendar: Calendar = {
        var calendar = Calendar(identifier: .gregorian)
        calendar.timeZone = TimeZone(identifier: "Europe/Budapest")!
        return calendar
    }()

    private func date(_ year: Int, _ month: Int, _ day: Int, _ hour: Int, _ minute: Int = 0) -> Date {
        calendar.date(from: DateComponents(year: year, month: month, day: day, hour: hour, minute: minute))!
    }

    // MARK: How far to move

    @Test("The last drinking day lands between six days ago and today", arguments: 0..<21)
    func lastEveningIsRecent(daysLater: Int) {
        let last = date(2026, 10, 10, 21, 30)
        let now = calendar.date(byAdding: .day, value: daysLater, to: date(2026, 10, 11, 14))!

        let weeks = DemoPerson.weeksToShift(lastDrinkAt: last, now: now, calendar: calendar)
        let moved = calendar.date(byAdding: .day, value: 7 * weeks, to: last)!
        let ago = DrinkingDay.containing(moved, calendar: calendar).daysAgo(from: now, calendar: calendar)

        #expect((0...6).contains(ago))
    }

    @Test("A fixture ending today stays today, and later drinks wait for their time")
    func todayStaysTodayAndWaits() throws {
        // A night "yesterday" and a round "today" at 13:00, written for this week.
        let night = session(drinksAt: [
            date(2026, 10, 17, 20, 0),
            date(2026, 10, 18, 13, 0),
            date(2026, 10, 18, 14, 0),
        ])
        let archive = DataArchive(people: [person(createdAt: date(2026, 1, 1, 0, 0))], sessions: [night])
        let last = date(2026, 10, 18, 14, 0)

        let noon = date(2026, 10, 18, 12, 0)
        #expect(DemoPerson.weeksToShift(lastDrinkAt: last, now: noon, calendar: calendar) == 0)

        let morning = DemoPerson.upTo(noon, archive)
        #expect(morning.drinkCount == 1)
        #expect(morning.sessions.first?.endedAt == nil)

        let afternoon = DemoPerson.upTo(date(2026, 10, 18, 13, 30), archive)
        #expect(afternoon.drinkCount == 2)

        let evening = DemoPerson.upTo(date(2026, 10, 18, 19, 0), archive)
        #expect(evening.drinkCount == 3)
        #expect(evening.sessions.first?.endedAt == night.endedAt)
    }

    @Test("A drink after midnight belongs to the evening it started in")
    func afterMidnightCountsAsTheEvening() {
        // 01:30 on Sunday is Saturday's drinking day; on Sunday afternoon that
        // is yesterday already, so nothing moves.
        let last = date(2026, 10, 11, 1, 30)
        let now = date(2026, 10, 11, 15)

        #expect(DemoPerson.weeksToShift(lastDrinkAt: last, now: now, calendar: calendar) == 0)
    }

    // MARK: Moving

    @Test("Moving keeps the weekday and the clock time, across a daylight-saving change")
    func keepsWeekdayAndTime() {
        // Saturday 22:15 in summer time, moved past the end of October.
        let drinkAt = date(2026, 10, 17, 22, 15)
        let archive = DataArchive(
            people: [],
            sessions: [session(drinksAt: [drinkAt])]
        )

        let moved = DemoPerson.shifted(archive, byWeeks: 2, calendar: calendar)
        let result = moved.sessions[0].drinks[0].consumedAt
        let parts = calendar.dateComponents([.weekday, .hour, .minute, .day, .month], from: result)

        #expect(parts.weekday == calendar.component(.weekday, from: drinkAt))
        #expect(parts.hour == 22)
        #expect(parts.minute == 15)
        #expect(parts.month == 10 && parts.day == 31)
    }

    @Test("Every date moves together: person, session and drinks")
    func movesEverything() {
        let start = date(2026, 1, 3, 20)
        let archive = DataArchive(
            people: [person(createdAt: start)],
            sessions: [session(drinksAt: [start, start.addingTimeInterval(3600)])]
        )

        let moved = DemoPerson.shifted(archive, byWeeks: 1, calendar: calendar)
        let week: TimeInterval = 7 * 24 * 3600

        #expect(moved.people[0].createdAt == start.addingTimeInterval(week))
        #expect(moved.people[0].trackingStartedAt == start.addingTimeInterval(week))
        #expect(moved.sessions[0].startedAt == start.addingTimeInterval(week))
        #expect(moved.sessions[0].endedAt == archive.sessions[0].endedAt!.addingTimeInterval(week))
        #expect(moved.sessions[0].drinks.map(\.consumedAt) == archive.sessions[0].drinks.map { $0.consumedAt.addingTimeInterval(week) })
    }

    @Test("Only the demo's rows are loaded from the file")
    func keepsOnlyTheDemo() {
        let stranger = UUID()
        var other = session(drinksAt: [date(2026, 1, 1, 20)])
        other.personID = stranger
        let archive = DataArchive(
            people: [person(createdAt: .now), person(createdAt: .now, id: stranger)],
            sessions: [session(drinksAt: [date(2026, 1, 2, 20)]), other],
            monthlyTotals: [ArchivedMonthlyTotal(personID: stranger, year: 2026, month: 1, gramsEthanol: 100)]
        )

        let trimmed = DemoPerson.demoOnly(archive)

        #expect(trimmed.people.map(\.id) == [DemoPerson.id])
        #expect(trimmed.sessions.allSatisfy { $0.personID == DemoPerson.id })
        #expect(trimmed.monthlyTotals?.isEmpty == true)
    }

    @Test("The bundled fixture decodes and holds only the demo")
    func bundledFixtureLoads() throws {
        let archive = try #require(DemoPerson.bundledArchive())

        #expect(archive.people.map(\.id) == [DemoPerson.id])
        #expect(archive.people.first?.isOwner == false)
        #expect(archive.sessions.count > 1000)
    }

    // MARK: Export

    @Test("An export never carries the demo")
    func exportSkipsTheDemo() throws {
        let context = try makeContext()
        let owner = PersonMigration.run(in: context)
        let demo = Person(
            id: DemoPerson.id,
            name: "Demo",
            profile: .test,
            frequency: .regular,
            limit: 1.5
        )
        context.insert(demo)
        for (index, who) in [owner, demo].enumerated() {
            let session = DrinkingSession(
                startedAt: date(2026, 10, 1 + index, 20),
                person: who,
                profile: .test,
                limit: 1
            )
            context.insert(session)
            context.insert(MonthlyTotal(personID: who.id, year: 2025, month: 1 + index, gramsEthanol: 50))
        }
        try context.save()

        let archive = ArchiveExport.archive(from: context)

        #expect(archive.people.map(\.id) == [owner.id])
        #expect(archive.sessions.map(\.personID) == [owner.id])
        #expect(archive.monthlyTotals?.map(\.personID) == [owner.id])
    }

    // MARK: Fixtures

    private func person(createdAt: Date, id: UUID = DemoPerson.id) -> ArchivedPerson {
        ArchivedPerson(
            id: id, name: "Demo", isOwner: false, createdAt: createdAt, accentRaw: "amber",
            sexRaw: "male", age: 38, heightCm: 181, weightKg: 86, beta: 0.2, betaUncertainty: 0,
            frequencyRaw: "daily", limit: 1.5, trackingStartedAt: createdAt
        )
    }

    private func session(drinksAt dates: [Date]) -> ArchivedSession {
        ArchivedSession(
            id: UUID(), startedAt: dates[0], endedAt: dates.last!.addingTimeInterval(5 * 3600),
            sexRaw: "male", age: 38, heightCm: 181, weightKg: 86, beta: 0.2, betaUncertainty: 0,
            limit: 1.5, personID: DemoPerson.id,
            drinks: dates.map {
                ArchivedDrink(
                    id: UUID(), consumedAt: $0, volumeMl: 500, abvPercent: 5,
                    drinkingMinutes: 30, stomachRaw: "light", templateID: "beer"
                )
            }
        )
    }
}
