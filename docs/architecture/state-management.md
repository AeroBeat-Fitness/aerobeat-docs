# State Management

To support multiplayer without refactoring core logic, we strictly separate **Immutable Context** from **Mutable State**.

### The Session Context (Immutable)

* **Class:** `AeroSessionContext` (Core).
* **Role:** Defines the "Rules of the Round" (Song ID, Difficulty, Modifiers, Random Seed).
* **Sync:** Sent **Once** by the Host before the round starts.
* **Rule:** Features **READ** this to configure themselves. They **NEVER** modify it.

### The User State (Mutable / Replicated)

* **Class:** `AeroUserState` (Core).
* **Role:** Holds real-time player data (Score, Combo, Health, Current Input Pose).
* **Authority:** The **Local Client** is the authority on their own score/hits (Client-Side Prediction).
* **Replication:**
    * **High Frequency (Unreliable):** Avatar Pose (Head/Hands) for visual representation.
    * **Event Based (Reliable):** Score updates, Combo breaks, Health changes.
* **Rule:** Features write to their Local `AeroUserState`. The Assembly handles replicating this object to other peers.