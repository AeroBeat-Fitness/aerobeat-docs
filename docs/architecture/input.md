# Input Pipeline (Provider Pattern)

Input is abstracted via a Strategy Pattern to allow hot-swapping between CV, VR, and Debug modes. The game logic never talks to hardware directly; it asks the **Input Provider** for normalized data.

* **Interface:** `AeroInputProvider` (Defined in `aerobeat-core`).
* **Contract:** Must return normalized `0.0 - 1.0` Viewport Coordinates for `LeftHand`, `RightHand`, and `Head`.

**Supported Strategies:**

| Strategy Name | Repository | Technology | Target Platform |
| :--- | :--- | :--- | :--- |
| **`StrategyMediaPipePython`** | `aerobeat-input-mediapipe-python` | **Sidecar Process.** Launches a Python subprocess that pipes landmark data via UDP `localhost:8100`. | Windows, Linux, Mac |
| **`StrategyMediaPipeNative`** | `aerobeat-input-mediapipe-native` | **GDExtension / Plugin.** Runs MediaPipe directly in the application memory. | Android, iOS |
| **`StrategyJoyconHID`** | `aerobeat-input-joycon-hid` | **Raw Bluetooth.** Connects directly to JoyCons to read high-speed Gyro/Accel data. | Windows, Linux, Android |
| **`StrategyKeyboard`** | `aerobeat-input-keyboard` | **Godot Native.** Maps WASD/Arrow keys to specific lanes (Virtual Presence). | All |
| **`StrategyMouse`** | `aerobeat-input-mouse` | **Godot Native.** Maps cursor X/Y to viewport coordinates. | Desktop / Web |
| **`StrategyTouch`** | `aerobeat-input-touch` | **Godot Native.** Maps touchscreen taps to viewport coordinates. | Mobile / Tablet |
| **`StrategyGamepad`** | `aerobeat-input-gamepad` | **Godot Native.** Standard XInput (Xbox/PS5) stick mapping. | All |

### Strategy Grouping Rationale
We enforce a **One-Repo-Per-Device-Type** policy, even for standard Godot inputs.

**The Logic: Granularity & Quirks.**

1.  **Isolation of Quirks:**
    * While Godot handles generic Gamepads well, specific controllers (like DDR Dance Pads or Flight Sticks) often report as generic gamepads but require specific axis remapping or deadzone logic.
    * By isolating `aerobeat-input-gamepad`, we can implement complex remapping strategies without polluting the clean logic of `aerobeat-input-keyboard`.

2.  **The "Driver" Tier (`input-mediapipe-*`, `input-joycon`):**
    * These inputs require **Heavy External Dependencies** (Python Environments, Android .aar Libraries, GDExtensions).
    * **Isolation is Safety:** By keeping the Python CV stack in its own repo, we ensure that a Mobile developer never has to download a 200MB Python environment they can't use. Likewise, a PC developer doesn't need to compile Android Java code just to fix a keyboard bug.

**Normalization Flow:**

1.  **Raw Data:** Strategy receives device-specific data (e.g., MediaPipe Landmark `x: 0.54, y: 0.21, z: -0.1`).
2.  **Adaptation:** Strategy applies technology-specific offsets (e.g., flipping Y axis for OpenCV).
3.  **Delivery:** Strategy exposes `get_left_hand_transform()` to the Game Loop.