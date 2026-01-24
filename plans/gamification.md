# Strategic Plan: Gamification & Habit Building

This document outlines the systems designed to promote retention and healthy habits, sitting on top of the [Workout Points Economy](./workout-points.md).

## 1. Philosophy: "Consistency over Intensity"

Unlike traditional games that want you to play 24/7, AeroBeat is a fitness tool. We want athletes to hit their *personal* goals, not burn out.

**Core Principle:** We reward showing up.

## 2. The Weekly Stamp Card (Retention)

**Objective:** Visualize progress towards the athlete's specific weekly goal.

### Mechanics
1.  **Setup:** During onboarding (or Profile settings), the athlete sets a **"Weekly Frequency Goal"** (1 to 7 days).
2.  **The Stamp:** Completing at least one Playlist (min duration: 10 mins) on a unique day grants a "Day Stamp".
3.  **Visuals:** A 7-day horizontal bar.
    *   Empty slots: Grey.
    *   Stamped slots: Green Checkmark.
    *   Goal Marker: A flag placed at the Nth slot (e.g., 3rd slot).

### Rewards
*   **Goal Met:** Upon placing the stamp that hits the goal (e.g., the 3rd stamp), grant a **"Weekly Bonus"** (e.g., 1,000 WP).
*   **Overachiever:** Stamps earned *after* the goal is met grant a smaller bonus (e.g., 100 WP), treating them as "Extra Credit" without pressure.

## 3. The Streak System (Loyalty)

**Objective:** Long-term retention.

### Mechanics
*   **Streak Counter:** Increments every week the **Weekly Frequency Goal** is met.
*   **Multiplier:** Higher streaks provide a passive multiplier to WP earned from workouts.
    *   Week 1-4: 1.0x
    *   Week 5-10: 1.1x
    *   Week 10+: 1.25x (Cap)

### Risk Mitigation: "Life Happens"
Breaking a streak because of illness or vacation is demoralizing and causes churn.
*   **The "Freeze" Item:** Players can buy a "Streak Freeze" in the Locker Room using WP. It automatically consumes itself if a week is missed, preserving the streak count.
*   **Banked Days:** If a user sets a goal of 3 days but works out 5 days, the extra 2 days add to a hidden "Bank". If they miss a day next week, the bank covers it.

## 4. The Explorer Bonus (Variety)

**Objective:** Encourage athletes to try different gameplay styles (Boxing, Flow, etc.).

### Mechanics
*   **Tracking:** Track unique gameplay modes played within the current week.
*   **Reward:** If the player completes at least one playlist of *every* available gameplay type (e.g., Boxing, Flow, Step) within the week, grant a **"Jack of All Trades" Bonus** (e.g., 500 WP).

## 5. Daily Quests (Engagement)

**Objective:** Encourage exploring different modes (Boxing vs Flow) and content.

### Mechanics
Every 24h, generate 3 quests based on the player's history.
*   *Easy:* "Play 1 Song in Boxing Mode" (100 WP)
*   *Medium:* "Complete 2 Playlists" (250 WP)
*   *Hard:* "Complete over 30 minutes of Pro level playlists" (500 WP)

### Reroll Logic
Players can Reroll 1 quest per day to avoid modes they physically cannot play (e.g., injury preventing Squats in Flow mode).

## 6. Risk Analysis

| Risk | Impact | Mitigation |
| :--- | :--- | :--- |
| **Cheating** | Players start a playlist and sit on the couch to get a Stamp. | **Activity Threshold.** A stamp is only awarded if the player achieves a minimum score or accuracy threshold (e.g. Accuracy > 10%) for the session. |
| **Demotivation** | "I missed Monday, now I can't hit my 7-day goal." | **Flexible Goals.** Encourage 3-5 day goals rather than 7. UI should emphasize "Weekly Goal" not "Daily Streak". |
| **Hoarding** | Players save WP for Streak Freezes instead of Cosmetics. | **Pricing Balance.** Freezes should be expensive enough to be a strategic choice, but cheap enough that active players can afford one per month easily. |

## 7. Technical Requirements

### A. `AeroUserProfile` Updates
Need to track timestamps and history.
```gdscript
@export_group("Gamification")
@export var weekly_goal_days: int = 3
@export var current_week_stamps: Array[Dictionary] = [] # [{ "date": "2023-10-27", "score": 15000 }]
@export var weekly_modes_played: Array[String] = [] # ["boxing", "flow"]
@export var streak_weeks: int = 0
@export var streak_freezes: int = 0
@export var last_quest_generation: int = 0 # Unix Timestamp
@export var active_quests: Array[Resource] = []
```

### B. `AeroGamificationManager`
A new logic controller in `aerobeat-core` to:
1.  Check date changes. *Decision: Use Server time exclusively. Offline play does not contribute to gamification.*
2.  Reset Weekly Stamps on Monday 00:00.
3.  Generate Quests and track Explorer Bonus progress.

## 8. Online-Only Policy

Similar to the Economy, Gamification relies on Server Authority to prevent date manipulation (e.g., changing system clock to keep a streak).

*   **Server Time:** Streaks and Quests rely on Server Time, not Local Time.
*   **Offline Limitations:** Workouts completed offline do not count towards Quests, Streaks, or Weekly Goals.

## 9. Execution Checklist

### Documentation
- [x] Update `docs/gdd/gamification/overview.md` with the Stamp Card, Streak, and Explorer Bonus mechanics.
- [x] Update `docs/gdd/gamification/overview.md` with the identified Risks and Mitigation strategies.
- [x] Update `docs/architecture/security.md` regarding Online-Only Gamification rules.
- [x] Create `docs/gdd/gamification/quests.md` detailing the quest generation logic and types.
- [x] Update `docs/architecture/state-management.md` with the new `AeroUserProfile` fields.

### Code
- [ ] **Core:** Update `AeroUserProfile` with gamification fields.
- [ ] **Logic:** Implement `AeroGamificationManager` (Time checks, Quest generation).
- [ ] **UI:** Create `StampCard` and `QuestLog` components in `aerobeat-ui-shell`.