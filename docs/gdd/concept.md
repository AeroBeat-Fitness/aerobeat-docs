# AeroBeat: Concept Overview

**AeroBeat** is an open-source, modular rhythm game platform designed to democratize fitness gaming.

Unlike traditional rhythm games that are locked to specific ecosystems (VR headsets or consoles), AeroBeat is **Input Agnostic**. It utilizes Computer Vision (CV) to turn standard webcams into high-fidelity motion controllers, allowing anyone with a laptop or phone to access a premium workout experience previously reserved for VR owners.

---

## 🎯 The High Concept

> **"The YouTube of Workout Games."**

AeroBeat is not just a game; it is a **Platform** consisting of three decoupled layers:
1.  **The Inputs:** How you move (Webcam, VR, Watch, Controller).
2.  **The Engine:** The core rhythm logic, audio synchronization, and scoring.
3.  **The Content:** Community-created songs, environments, and even entirely new gameplay mechanics (Boxing, Tai Chi, Dance).

### Key Pillars
* **Accessibility First:** Hardware should not be a gatekeeper. If you have a camera, you can play.
* **Fitness First:** Gameplay is designed for *range of motion* and *caloric burn*, not just finger speed.
* **Open Ecosystem:** Built on Godot 4 and open standards to encourage community modding and proprietary hardware integrations.

---

## 🥊 Gameplay Core: "Boxing" (v0.0.1)

The debut gameplay module for AeroBeat is a rhythm-boxing experience.

### The Loop
1.  **The Beat:** Targets fly toward the player in sync with the music.
2.  **The Action:** The player must punch, dodge, or duck based on the target type.
3.  **The Feedback:** Successful hits trigger haptic feedback (if available), satisfying visual effects, and score multipliers.
4.  **The Workout:** The pattern of targets forces the player into a "Flow State," seamlessly blending cardio with rhythm.

### Mechanics
* **Directional Punches:** Jabs, Hooks, and Uppercuts indicated by arrow direction.
* **Obstacles:** Walls that force the player to Squat (Legs) or Lean (Core).
* **Flow Lines:** Continuous paths that the player must trace with their hands (Tai Chi style movement).

---

## 🎮 Input Agnosticism

AeroBeat's "Secret Sauce" is its ability to normalize data from wildly different hardware into a standard `0.0 - 1.0` viewport space.

### Tier 1: Computer Vision (CV)
* **Tech:** MediaPipe (Python Sidecar on PC / Native Plugin on Mobile).
* **Experience:** "Controller-Free." The player stands in front of a camera. The game tracks wrists, head, and shoulders.
* **Pros:** Zero cost, high accessibility.
* **Cons:** Higher latency than VR, occlusion issues.

### Tier 2: Dedicated Hardware
* **Tech:** VR Controllers, JoyCons, Smart Watches.
* **Experience:** "Tactile." The player holds devices that provide rumble feedback and ultra-low latency tracking.
* **Pros:** Precision, haptics, "Pro" feel.

### Tier 3: Legacy/Debug
* **Tech:** Mouse & Keyboard, Gamepads.
* **Experience:** "Developer Mode." Used for testing charts or playing on low-end devices without cameras.

---

## 🛠️ The "Skin" System (UGC)

To support the "YouTube" vision, visual content is strictly separated from game logic.

* **Logic (The Skeleton):** A "Target" is just a mathematical hitbox and a timestamp.
* **Skin (The Visuals):** Artists can replace the default sphere with a *Boxing Glove*, a *Katana*, or a *Magic Spell*.
* **Environment:** The gym can be replaced with a *Neon City*, a *Tranquil Forest*, or a *Live Concert Stage*.

This allows the community to create "Total Conversion" aesthetics without touching a line of code.

---

## 🔮 Future Roadmap

* **Phase 1 (Prototype):** PC Build + Python CV Sidecar + Basic Boxing Core.
* **Phase 2 (Mobile):** Native Android/iOS Port + On-Device CV.
* **Phase 3 (Platform):** Workshop support for downloading community songs/skins.
* **Phase 4 (Multiplayer):** Real-time "Battle Mode" (Ghost data sync).
