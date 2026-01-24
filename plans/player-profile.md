# Strategic Plan: Athlete Profile & Customization

This document outlines the design and architecture for the **Athlete Profile**, the central hub where players manage their identity, track progress, and customize their appearance.

## 1. Philosophy: "The Mirror"

The Profile is the digital mirror of the athlete. It should reflect their effort (Stats/Streak) and their style (Avatar/Cosmetics). It is not just a settings menu; it is a trophy room.

## 2. Access Points

To ensure the profile is accessible but not intrusive:

1.  **The "Badge" (Always Visible):**
    *   **Location:** Top-Right corner of the Main Menu and Song Select screens.
    *   **Content:** Mini-Avatar Headshot, Username, Current Level/WP, Streak Flame.
    *   **Action:** Clicking opens the full **Profile Hub**.

2.  **The Locker Room (Customization):**
    *   **Access:** Via the Profile Hub or a dedicated "Locker Room" button in the main nav.
    *   **Context:** A 3D environment where the Avatar is the focus.

3.  **The Web Portal (Companion):**
    *   **Access:** `aerobeat-workouts.com/profile`
    *   **Context:** Read-only view of stats, history, and shareable badges.

## 3. Profile Hub Features

The Profile Hub is a dashboard composed of modular widgets.

### A. Identity Card

*   **Avatar:** Full-body 3D render (idle animation).
*   **Name & Title:** e.g., "Speed Demon", "Early Riser".
*   **Join Date:** "Member since 2024".

### B. The "Sweat Stats" (Progress)

*   **Weekly Goal:** The 7-day Stamp Card (Visualized as outlined in Gamification).
*   **Streak:** Current active weeks.
*   **Total WP:** Lifetime earnings.
*   **Play Time:** Total hours active.

### C. Goal Control Center

Athletes need to adjust goals as their fitness changes.

*   **Frequency Slider:** "I want to workout [3] days a week."
*   **Difficulty Preference:** "Preferred Difficulty: [Hard]." (Used for "Quick Play" suggestions).

### D. Workout History
*   **List:** Last 10 sessions.
*   **Details:** Date, Song/Playlist Name, Duration, WP Earned, Accuracy.

## 4. The Locker Room (Avatar Customization)

This is the primary "Sink" for the Economy.

### UI Layout

*   **Center:** The Avatar (Rotatable, Zoomable).
*   **Left Panel (Categories):** Head, Face, Torso, Hands, Legs, Accessories.
*   **Right Panel (Inventory/Shop):** Grid of items.
    *   *Owned:* Equip immediately.
    *   *Unowned:* Show Price (WP). "Hold to Buy".

### The "Fitting Room" Logic

*   **Preview:** Clicking an unowned item equips it temporarily.
*   **Validation:** Ensure incompatible items (e.g., Full Helmet + Glasses) handle conflicts gracefully (e.g., unequip the conflict or hide it).
*   **Gizmos:** As defined in `ui-ux.md`, allow minor position/scale adjustments for accessories to prevent clipping.

## 5. UI Flow Suggestions

### Flow 1: Checking Progress

1.  **User** is on Main Menu.
2.  **User** clicks Top-Right Profile Badge.
3.  **System** opens `ProfileOverlay` (Modal).
4.  **User** views Stamp Card.
5.  **User** clicks outside to close.

### Flow 2: Changing a Goal

1.  **User** opens `ProfileOverlay`.
2.  **User** clicks "Edit Goals".
3.  **System** transitions to `GoalSettingsView`.
4.  **User** slides "Days per Week" from 3 to 5.
5.  **User** clicks "Save".
6.  **System** updates `AeroUserProfile` locally and syncs to Server.

### Flow 3: Buying a Hat

1.  **User** enters `LockerRoom`.
2.  **User** selects "Head" category.
3.  **User** filters by "Shop" (Unowned).
4.  **User** clicks "Neon Cap" (500 WP). Avatar previews it.
5.  **User** holds "Buy" button.
6.  **System** validates funds -> Deducts WP -> Adds to Inventory -> Plays "Unlock" FX.

## 6. Execution Checklist

### Documentation
- [x] Create `docs/gdd/meta/profile.md` detailing the Profile Hub UI and stats.
- [x] Create `docs/gdd/meta/locker_room.md` detailing the Customization UI and Shop logic.
- [x] Update `docs/architecture/ui-ux.md` with the Profile and Locker Room flows.

### Code
- [ ] **UI:** Create `ProfileBadge` component (Atom).
- [ ] **UI:** Create `ProfileHub` scene (Organism).
- [ ] **UI:** Create `LockerRoom` scene (3D Environment + UI).
- [ ] **Logic:** Implement `AeroProfileManager` for handling goal changes and shop transactions.