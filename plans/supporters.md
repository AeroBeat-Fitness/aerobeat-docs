# Strategic Plan: Supporter Model

This document outlines the monetization strategy for AeroBeat's Community Edition. Following the successful model of *osu!*, we rely on voluntary contributions rather than forced subscriptions or pay-to-win mechanics.

## 1. Philosophy: "Support, Don't Buy"

AeroBeat is open-source and community-driven. Our "Supporter" status is a donation to keep the servers running and fund development, not a purchase of a product.

*   **Free-to-Win:** Every gameplay feature, song, and mode is available to free players.
*   **No UGC Gating:** We never charge for access to Community Content (Songs/Skins). Doing so would expose us to massive copyright liability.
*   **Account-Level Perks:** Benefits are focused on social status, convenience, and customization.

## 2. Pricing Structure

We aim for accessibility. Pricing is set to cover server costs (bandwidth/storage) per user plus a contribution to development.

*   **1 Month:** $4.00
*   **2 Months:** $8.00
*   **4 Months:** $12.00 (Save 25%)
*   **6 Months:** $16.00 (Save 33%)
*   **1 Year:** $24.00 (Save 50%)
*   **18 Months:** $39.00 (Save 46%)
*   **2 Years:** $52.00 (Save 46%)

*Note: Regional pricing should be considered during implementation.*

## 3. Supporter Benefits

### A. Social Status (The "Clout")

*   **In-Game Badge:** A "Supporter Heart" icon next to the username on Leaderboards and Lobbies.
*   **Discord Role:** Automatic sync via bot to grant the "AeroBeat Supporter" role (access to private channels).
*   **Profile Flair:** Gold border or special effects on the Web Profile and In-Game Badge.

### B. Convenience & Limits

*   **Cloud Storage:** Increased quota for UGC uploads (e.g., 2GB -> 5GB).
*   **Friends List:** Cap increased from 500 to 1000.
*   **Download Priority:** Higher bandwidth limits for downloading mods from the CDN (if throttling is active).

### C. Cosmetic Exclusives

*   **Locker Room Access:** Access to a specific "Supporter Collection" of Avatar items.
    *   *Note:* These items still cost Workout Points (WP) to unlock. The "Supporter" status just reveals them in the shop.
*   **Menu Customization:** Ability to change the Main Menu background environment to one your downloaded environments.

### D. Community Influence

*   **Voting Power:** Weighted votes on the "Feature Roadmap" polls.
*   **Playlist of the Day:** Ability to nominate playlists for the daily featured slot.

### E. Multiplayer Enhancements

*   **Lobby Host Customization:** When hosting a lobby, Supporters can change the visual environment (Skybox/Lighting) for all players in the waiting room.
*   **Entrance FX:** Unique particle effects (e.g., "Lightning Strike", "Digital Materialize") when joining a session.
*   **Lobby Emotes:** Access to animated stickers and reactions in the multiplayer chat.

### F. Advanced Analytics (The "Pro" Stats)

*   **Extended History:** Access to workout data beyond the standard 10-session limit (e.g., Monthly/Yearly trends).
*   **Performance Heatmaps:** Visual breakdown of accuracy per lane/sector to identify weak spots (e.g., "You consistently miss low-left targets").

### G. Interface Customization

*   **HUD Skins:** Ability to theme the in-game scoring UI (Combo Counter, Health Bar) with different styles (e.g., "Retro", "Minimalist").

### H. External Integrations (The "Connected Athlete")
*   **Health Platform Sync:** Automatic synchronization of workout data (Calories, Duration, Heart Rate) to external platforms like **Strava**, **Apple Health**, or **Google Fit**.
*   **Export Data:** Ability to download raw CSV logs of workout history for personal analysis.

### I. Social Structures (Crews)
*   **Crew Creation:** Ability to found and manage a "Crew" (Guild/Clan). Includes a custom Tag (e.g., `[NEON]`), a private leaderboard, and management tools.
    *   *Note:* Free players can join Crews, but only Supporters can create them.

## 4. Risk Analysis

| Risk | Impact | Mitigation |
| :--- | :--- | :--- |
| **"Paywalling" Accusations** | Community feels forced to pay. | **Strict Policy.** Never lock gameplay features (Modes, Songs) behind the tag. Ensure the free tier is fully functional. |
| **Copyright Liability** | Charging for UGC access. | **Separation.** The Supporter tag is for *Service* (Servers/Dev), not *Content*. We explicitly state we do not sell the songs. |
| **Payment Fraud** | Chargebacks costing fees. | **Provider Choice.** Use a Merchant of Record (e.g., Paddle, Stripe) with robust fraud detection. |
| **API Costs** | External integrations (Strava) charge for high usage. | **Supporter Only.** Limiting this feature to paid supporters ensures the subscription fee covers any API usage costs. |
| **Performance Degradation** | Supporter FX (Entrance particles, Lobby skins) cause lag on mobile/VR. | **Client Toggles.** Allow players to disable "Remote Player FX" in settings. Enforce strict particle count limits on all cosmetic assets. |
| **Data Privacy** | Health Sync handles sensitive user data (GDPR compliance). | **Client-Side Sync.** Where possible, push data directly from the Client to the Health API (e.g. Apple HealthKit). If server-side, do not persist health data; treat it as transient. |
| **Toxic Socials** | Crew Tags or Lobby Names contain hate speech. | **Automated Filtering.** Apply strict profanity filters to all custom text fields. Implement a "Report Crew" feature. |
| **Gatekeeping** | "Supporter Only" Crews create a class divide. | **Open Membership.** While only Supporters can *create* crews, *anyone* can join them. This fosters community leadership rather than segregation. |
| **Manual Renewal Friction** | Non-recurring payments lead to churn as users forget to renew. | **In-Game Reminders.** Notify users 3 days before expiry. Allow "Stacking" (buying more time adds to current expiry). |
| **Revenue Volatility** | "Lumpy" income (e.g., holiday spikes) makes monthly server cost forecasting difficult. | **Reserve Fund.** Maintain a 3-month operating runway in the bank to smooth out low-revenue months. |
| **Refund Disputes** | Users buying 2-year packs and quitting/getting banned demand refunds. | **Clear Policy.** Explicitly label payments as "Non-Refundable Donations" in the checkout flow. Implement a strict pro-rated refund policy for exceptional cases. |

## 5. Technical Requirements

### A. Backend (API)

*   **Payment Gateway:** Integration with Stripe/PayPal.
*   **Database:** Add `supporter_expiry: Timestamp` to the User table.
*   **Endpoints:**
    *   `POST /api/billing/checkout`
    *   `POST /api/billing/webhook` (Stripe callback)
    *   `GET /api/user/status` (Returns `is_supporter: true`)

### B. Client (Godot)

*   **UI:** "Become a Supporter" button in the Profile Hub.
*   **Logic:** `AeroUserProfile` needs a synced `is_supporter` boolean to enable UI elements.

## 6. Execution Checklist

### Documentation
- [x] Create `docs/gdd/economy/supporter_perks.md` detailing the exact list of benefits.
- [x] Update `docs/architecture/backend_api.md` with billing endpoints.
- [x] Update `docs/gdd/meta/locker_room.md` to mention Supporter-exclusive items.
- [x] Update `docs/architecture/multiplayer.md` with Supporter FX and Lobby customization logic.
- [x] Update `docs/architecture/telemetry.md` with data retention policies for Advanced Analytics.
- [x] Update `docs/architecture/security.md` with Health Data privacy and GDPR compliance.
- [x] Create `docs/gdd/social/crews.md` detailing the Crew system mechanics.
- [x] Update `docs/gdd/meta/profile.md` to include "Pro Stats" and "Connected Athlete" settings.
- [x] Create `docs/legal/refund_policy.md` outlining the non-recurring/donation terms.

### Code

- [ ] **Backend:** Implement Stripe Checkout session generation.
- [ ] **Backend:** Implement "Stacking" logic (extending expiry timestamps) for existing supporters.
- [ ] **Core:** Update `AeroUserProfile` to include supporter status.
- [ ] **UI:** Design the "Supporter Badge" atom.