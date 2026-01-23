# 🎮 Input Agnosticism

AeroBeat's "Secret Sauce" is its ability to normalize data from wildly different hardware into a standard viewport space.

### Tier 1: Computer Vision (CV)
* **Tech:** MediaPipe (Python on PC / Native Plugin on Mobile).
* **Experience:** "Controller-Free." The athlete stands in front of a camera. The game tracks hands, arms, shoulders, and your head.
* **Pros:** Zero cost, high accessibility.
* **Cons:** Higher latency than VR, occlusion issues.

### Tier 2: Dedicated Hardware
* **Tech:** VR Controllers, JoyCons, Dance Pads
* **Experience:** "Tactile." The athlete holds devices that provide rumble feedback and ultra-low latency tracking.
* **Pros:** Precision, haptics, "Pro" feel.

### Tier 3: Accessibility & Legacy
* **Tech:** Xbox Adaptive Controller, Gamepads (XInput), Mouse & Keyboard, Touch.
* **Experience:** Enables play via specialized accessibility hardware, or used for testing charts when no other input is available.
