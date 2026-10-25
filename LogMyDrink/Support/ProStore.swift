import Foundation
import Observation
import StoreKit

/// The App Store side of Pro: which plans exist, what they cost, buying one,
/// and whether this Apple ID currently has one.
///
/// It does not decide what Pro opens — `FeatureFlags` does. It only tells
/// `FeatureFlags` the one thing it cannot know by itself: whether there is an
/// active subscription (`setSubscribed`). Everything that reacts to Pro — the
/// locks, the widget snapshot — keeps listening to the flags, as before.
///
/// One subscription group, two auto-renewable products, a one-month free
/// trial on both as the introductory offer (5.30). The trial is Apple's to
/// grant: once per subscription group per Apple ID, whichever plan it was
/// taken on.
@Observable
@MainActor
final class ProStore {

    static let shared = ProStore()

    // MARK: Products

    /// The product identifiers, as created in App Store Connect and in
    /// `LogMyDrinkTests/LogMyDrink.storekit`. Changing one after release
    /// orphans every subscriber on the old identifier.
    enum Plan: String, CaseIterable, Identifiable, Sendable {
        case yearly = "dev.zcsipler.logmydrink.pro.yearly"
        case monthly = "dev.zcsipler.logmydrink.pro.monthly"

        var id: String { rawValue }
    }

    nonisolated static let productIDs = Set(Plan.allCases.map(\.rawValue))

    enum LoadState: Equatable {
        case idle
        case loading
        case loaded
        case failed
    }

    private(set) var products: [Plan: Product] = [:]
    private(set) var loadState: LoadState = .idle

    /// Whether the first month is still free for this Apple ID. Asked once
    /// per load; Apple answers for the whole group.
    private(set) var isEligibleForTrial = true

    /// Set while the App Store's own sheet is up, so the button cannot be
    /// pressed twice.
    private(set) var isPurchasing = false

    // MARK: Lifecycle

    private var updatesTask: Task<Void, Never>?

    private init() {}

    /// Called once at launch. Listens for transactions that arrive outside a
    /// purchase this app started — a renewal, a refund, an offer code
    /// redeemed in the App Store, Ask to Buy approved on a parent's phone —
    /// and reads the current entitlement.
    func start() {
        guard updatesTask == nil else { return }
        updatesTask = Task { [weak self] in
            for await result in Transaction.updates {
                if case .verified(let transaction) = result {
                    await transaction.finish()
                }
                await self?.refreshEntitlement()
            }
        }
        Task { await refreshEntitlement() }
    }

    /// Reads the entitlement again. Cheap and offline — StoreKit keeps the
    /// signed transactions on the device — so it also runs whenever the app
    /// comes forward, which is how an expiry that happened while the app was
    /// asleep becomes a lock.
    func refreshEntitlement() async {
        let active = await Self.hasActiveSubscription()
        FeatureFlags.shared.setSubscribed(active)
    }

    /// Whether any verified, unrevoked, unexpired Pro subscription is in
    /// effect.
    ///
    /// `currentEntitlements` holds a subscription in its free trial and in
    /// Apple's billing grace period — both count as Pro, as they should. The
    /// expiry is checked here as well, against `now`, so that the answer does
    /// not depend on how promptly StoreKit drops an ended period.
    nonisolated static func hasActiveSubscription(at now: Date = .now) async -> Bool {
        for await result in Transaction.currentEntitlements {
            guard case .verified(let transaction) = result,
                  productIDs.contains(transaction.productID),
                  transaction.revocationDate == nil
            else { continue }
            if let expiry = transaction.expirationDate, expiry <= now { continue }
            return true
        }
        return false
    }

    /// Fetches the two plans and the trial eligibility. Called by the Pro
    /// sheet when it appears, again on "Try again".
    func loadProducts() async {
        guard loadState != .loading else { return }
        loadState = .loading
        do {
            let fetched = try await Product.products(for: Self.productIDs)
            var byPlan: [Plan: Product] = [:]
            for product in fetched {
                if let plan = Plan(rawValue: product.id) { byPlan[plan] = product }
            }
            products = byPlan
            if let any = byPlan.values.first, let subscription = any.subscription {
                isEligibleForTrial = await subscription.isEligibleForIntroOffer
            }
            loadState = byPlan.count == Plan.allCases.count ? .loaded : .failed
        } catch {
            loadState = .failed
        }
    }

    // MARK: Buying

    enum Outcome: Equatable {
        case purchased
        /// Ask to Buy, or a payment that needs the user's bank first. The
        /// subscription arrives later through `Transaction.updates`.
        case pending
        case cancelled
        case failed
    }

    func purchase(_ plan: Plan) async -> Outcome {
        guard let product = products[plan], !isPurchasing else { return .failed }
        isPurchasing = true
        defer { isPurchasing = false }
        do {
            switch try await product.purchase() {
            case .success(let verification):
                guard case .verified(let transaction) = verification else { return .failed }
                await transaction.finish()
                await refreshEntitlement()
                return .purchased
            case .pending:
                return .pending
            case .userCancelled:
                return .cancelled
            @unknown default:
                return .failed
            }
        } catch {
            return .failed
        }
    }

    /// "Restore purchases": asks the App Store to send this Apple ID's
    /// transactions again. Mandatory on a paywall (App Review 3.1.1), and
    /// the only way back for someone whose device lost them. Shows Apple's
    /// sign-in if needed. Returns whether Pro is active afterwards.
    func restore() async -> Bool {
        try? await AppStore.sync()
        await refreshEntitlement()
        return FeatureFlags.shared.isPro
    }

    // MARK: Prices for display

    /// The yearly price as a monthly figure ("about 2,08 € a month"), in the
    /// product's own currency and format.
    func yearlyPerMonth() -> String? {
        guard let yearly = products[.yearly] else { return nil }
        return (yearly.price / 12).formatted(yearly.priceFormatStyle)
    }

    /// How much cheaper a year is than twelve months, as a whole percent.
    func yearlySaving() -> Double? {
        guard let yearly = products[.yearly], let monthly = products[.monthly],
              monthly.price > 0
        else { return nil }
        let twelve = monthly.price * 12
        let saving = (twelve - yearly.price) / twelve
        let rounded = (NSDecimalNumber(decimal: saving).doubleValue * 100).rounded() / 100
        return rounded > 0 ? rounded : nil
    }
}
