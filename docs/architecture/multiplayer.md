# Multiplayer Strategy

### The "Remote Athlete" Pattern

Multiplayer opponents are visualized as "Remote Athletes" (Avatars).

1.  **Local Athlete:** Input -> Logic -> `AeroUserState` (Local).
2.  **Remote Athlete:** Network -> `AeroUserState` (Remote) -> Avatar Visualizer.
3.  **Constraint:** Gameplay Logic (`aerobeat-feature-*`) must accept a `target_user_state` in its setup. It does not assume it is always driving the main UI.

### Headless Safety (Multiplayer Prep)

Feature Logic must be safe to run on a Linux Headless Server (No GPU/Audio).

* **Forbidden:** Logic scripts calling `$Audio.play()` or `$Particles.emit()`.
* **Required:** Logic emits `signal hit_confirmed`. A separate `_view_connector.gd` (Client Only) listens and plays FX.