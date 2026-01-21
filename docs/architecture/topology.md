# Repository Topology

We adhere to a strict **7-Tier** repository structure. Dependencies are categorized to ensure modularity and prevent circular references.

| Tier | Repo Name | Role | Required Deps | Allowed Deps | Dev-Only / Peer Deps | License |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Assembly** | `aerobeat-assembly` | **The Router.** Manages App State & Dependency Injection. | All Active Packages | All Assets | Test Frameworks (Gut) | **GPLv3** |
| **Core** | `aerobeat-core` | **The Hub.** Interfaces, Data Types, Global Constants. | **None** | **None** | Unit Test Tools | **MPL 2.0** |
| **Input** | `aerobeat-input-*` | **Hardware Drivers.** (Camera, VR, Watch). | `aerobeat-core` | Vendor SDKs | Testbed Scaffolding | **MPL 2.0** |
| **UI Kit** | `aerobeat-ui-kit` | **Atomic Library.** Pure, stateless components (Buttons, Cards). | `aerobeat-core` | `aerobeat-asset-common` | Testbed Scaffolding | **MPL 2.0** |
| **UI Shell** | `aerobeat-ui-*` | **Interaction Layer.** Platform-specific screens (Mobile, VR). | `aerobeat-core`<br>`aerobeat-ui-kit` | `aerobeat-asset-common`<br>(Local Assets) | Vendor Tools (Tweeners)<br>Mock Data | **GPLv3** |
| **Feature** | `aerobeat-feature-*` | **Gameplay Logic.** Pure mechanics (Boxing, Flow). | `aerobeat-core` | Vendor Utils | Testbed Scaffolding | **GPLv3** |
| **Asset** | `aerobeat-asset-*` | **Content.** Skins, Songs, Environments. | `aerobeat-core` | **One** Feature (Inheritance) | **None** | **CC BY-NC 4.0** |
| **Docs** | `aerobeat-docs` | **Manual.** Documentation Website. | **None** | **None** | MkDocs Plugins | **CC BY-NC 4.0** |
| **Vendor** | `aerobeat-vendor` | **3rd Party Tools.** Utilities and Helpers. | **None** | **None** | *(As Upstream)* | *(As Upstream)* |

### Dependency Definitions

* **Required Dependencies:** The code will not compile without these. They must be present in `addons/`.
* **Allowed Dependencies:** You may link to these if needed (e.g., using the Official Font from `asset-common`), but they are not strictly mandatory for logic.
* **Dev-Only / Peer Dependencies:** Tools used for testing (like `Gut` or `Tween` libraries). In Production, these are provided by the Host Assembly. In Development, they are cloned via `setup_dev`.

### The UI Tier Strategy (MVVM)

We do not have a "Default UI." The Assembly defines **UI Contracts** (`AeroMenuProvider`), and the UI Tier implements them.

* **`aerobeat-ui-mobile`**: 2D Touch-based interface (Scrolls, Taps).
* **`aerobeat-ui-desktop`**: Mouse/Keyboard interface (Hover states, Keybinds).
* **`aerobeat-ui-vr`**: Spatial interface (Laser pointers, World-Space Canvas).

### Repository List (v0.0.1)

* **`aerobeat-assembly`**: The main Godot project. Contains `project.godot`, Export Presets, and Main Menu logic.
* **`aerobeat-core`**: The unified hub for Contracts (`AeroInputStrategy`), Signals (`AeroEvents`), Constants (`AeroConst`), and Data Types.
* **`aerobeat-input-mediapipe-python`**: Tracks body movement using MediaPipe camera events, then passes them via UDP listeners.
* **`aerobeat-feature-boxing`**: The Boxing gameplay loop, hit detection, and choreography parser.
* **`aerobeat-asset-prototypes`**: Grey-box environments and dummy targets.