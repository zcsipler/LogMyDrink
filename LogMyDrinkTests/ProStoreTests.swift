import Foundation
import StoreKit
import StoreKitTest
import Testing
@testable import LogMyDrink

/// The subscription, against Xcode's local StoreKit (`LogMyDrink.storekit`):
/// the two plans load with their trial, and the entitlement follows a
/// purchase and an expiry. No App Store account is involved.
@Suite("Pro store", .serialized)
@MainActor
struct ProStoreTests {

    private func session() throws -> SKTestSession {
        let session = try SKTestSession(configurationFileNamed: "LogMyDrink")
        session.resetToDefaultState()
        session.clearTransactions()
        session.disableDialogs = true
        return session
    }

    @Test("Both plans load, each with a one-month free trial")
    func plansLoad() async throws {
        _ = try session()
        let products = try await Product.products(for: ProStore.productIDs)
        #expect(Set(products.map(\.id)) == ProStore.productIDs, "loaded: \(products.map(\.id))")
        for product in products {
            let intro = try #require(product.subscription?.introductoryOffer)
            #expect(intro.paymentMode == .freeTrial)
            #expect(intro.period.value == 1)
            #expect(intro.period.unit == .month)
        }
        let yearly = try #require(products.first { $0.id == ProStore.Plan.yearly.rawValue })
        let monthly = try #require(products.first { $0.id == ProStore.Plan.monthly.rawValue })
        // The display price, not `price`: on a Mac whose region writes a
        // decimal comma, Xcode's local StoreKit reads "24.99" as 24.
        #expect(yearly.displayPrice.contains("24.99"))
        #expect(monthly.displayPrice.contains("3.99"))
    }

    /// The test session applies an expiry asynchronously; give it a moment.
    private static func eventually(_ condition: () async -> Bool) async -> Bool {
        for _ in 0..<30 {
            if await condition() { return true }
            try? await Task.sleep(for: .milliseconds(100))
        }
        return false
    }

    @Test("No purchase, no Pro")
    func nothingBought() async throws {
        _ = try session()
        #expect(await ProStore.hasActiveSubscription() == false)
    }

    @Test("A purchase opens Pro — the free month included — and it closes when the period ends")
    func purchaseAndExpiry() async throws {
        let session = try session()
        try await session.buyProduct(identifier: ProStore.Plan.yearly.rawValue)
        #expect(await Self.eventually { await ProStore.hasActiveSubscription() })

        // Asked as of a moment past the end of the free month, rather than
        // through `expireSubscription`, which the test session does not
        // apply to a subscription still in its trial.
        let afterTrial = Date.now.addingTimeInterval(32 * 24 * 3600)
        #expect(await ProStore.hasActiveSubscription(at: afterTrial) == false)
    }

    @Test("A refunded subscription is not Pro")
    func refund() async throws {
        let session = try session()
        let id = ProStore.Plan.monthly.rawValue
        try await session.buyProduct(identifier: id)
        #expect(await Self.eventually { await ProStore.hasActiveSubscription() })
        let transaction = try #require(session.allTransactions().first { $0.productIdentifier == id })
        try session.refundTransaction(identifier: transaction.identifier)
        #expect(await Self.eventually { await ProStore.hasActiveSubscription() == false })
    }
}
