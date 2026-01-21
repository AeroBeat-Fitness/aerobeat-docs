# UI Architecture (Atomic Design)

We utilize the **Atomic Design Methodology** to maximize code reuse across disparate platforms (VR vs. Mobile). UI development is split between a centralized "Kit" and platform-specific "Shells."

### The UI Kit (`aerobeat-ui-kit`)

* **Role:** The Source of Truth. Contains pure, stateless visual components.
* **License:** **MPL 2.0** (Treat as a standard library).
* **Structure:**
    * **Atoms:** Irreducible controls (e.g., `AeroButton`, `AeroLabel`, `AeroSlider`). Styles are driven by Theme Resources.
    * **Molecules:** Simple functional groups (e.g., `SongCard` = Cover Art + Title + Difficulty Badge).
    * **Organisms:** Complex, distinct sections (e.g., `SongList`, `LeaderboardRow`, `ProfileHeader`).
* **Testing:** Every Atom/Molecule must include a `_testbed/` scene demonstrating its states (Normal, Hover, Disabled, Focused).

### The UI Shells (`aerobeat-ui-mobile`, `aerobeat-ui-vr`)

* **Role:** The Assembler. Defines "Templates" and "Pages."
* **License:** **GPLv3** (Contains Application Logic).
* **Responsibility:**
    1.  **Import:** Consumes the `aerobeat-ui-kit` via the **UI Sync Protocol**.
    2.  **Layout:** Arranges Organisms into usable Screens (`MainMenu`, `GameplayHUD`).
    3.  **Wiring:** Connects component signals to App Logic (`aerobeat-assembly-*`).

### The UI Sync Protocol (Tooling)

Since Godot lacks a native package manager for assets, we enforce consistency via custom tooling.

1.  **The Script:** `./sync_ui_kit` (Python/Bash).
    * Located in the root of every UI Shell repo.
    * **Action:** Pulls the specific version of `aerobeat-ui-kit` defined in `.kit_version`.
    * **Validation:** Runs the `test_components` command to ensure the imported atoms are compatible with the current project settings.
2.  **The Workflow:**
    * Developers **NEVER** modify `addons/aerobeat-ui-kit` inside a Shell repo.
    * Updates are made in the `aerobeat-ui-kit` repo, tagged, and then pulled into Shells via the sync script.

### UI Dependency Rules

To ensure UI repositories remain lightweight and fast to test, we enforce the following dependency limits:

| Dependency Type | Repository | Status | Logic |
| :--- | :--- | :--- | :--- |
| **Contract Hub** | `aerobeat-core` | **Required** | Needed for `AeroMenuProvider` interface. |
| **Component Kit** | `aerobeat-ui-kit` | **Required** | Source of all buttons, sliders, and standard widgets. |
| **Shared Assets** | `aerobeat-asset-common` | **Allowed** | Fonts, Logos, and Global Icons only. |
| **Vendor Tools** | `aerobeat-vendor-*` | **Dev-Only** | Tween libs or UI helpers. In Prod, these are Peer Dependencies provided by Assembly. |
| **Game Content** | `aerobeat-asset-*` | **FORBIDDEN** | UI must never depend on specific Level/Env packs. Use Mock Data for testing. |

### UI Dependency Rules

* **UI Code:** Licensed under **GPLv3** because it contains complex logic (state handling, animation controllers).
* **Assets:** Visuals used by the UI (Icons, Fonts) can be stored inside the UI repo if they are specific to that UI, or pulled from `aerobeat-asset-common` if shared.