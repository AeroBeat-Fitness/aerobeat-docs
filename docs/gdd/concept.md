# AeroBeat: Concept Overview

**AeroBeat** is an open-source, modular rhythm game platform designed to democratize fitness gaming.

Unlike traditional rhythm games that are locked to specific ecosystems (VR headsets, pc, mobile, or consoles), AeroBeat is **Gameplay Agnostic**, **Hardware Agnostic**, and **Input Agnostic**. Each piece of the engine is expandable to support a variety of rhythm workout gameplay mechanics across a variety of devices.

Our first featured rhythm workout Gameplay style is **Boxing** on for laptop and desktop PC's. By utilizing Computer Vision (CV) to turn standard webcams into high-fidelity motion controllers, we allow anyone with a laptop or desktop to access a premium workout experience previously reserved for VR owners.

---

## 🎯 The High Concept

> **"The YouTube of Workout Games."**

AeroBeat is not just a game; it is a **Platform** consisting of three decoupled layers:
1.  **The Inputs:** How you move (Webcam, VR, Joycons, Keyboard, Mouse, Controller).
2.  **The Engine:** The core rhythm logic, audio synchronization, and scoring.
3.  **The Content:** Community-created songs, environments, and even entirely new gameplay mechanics (ex: **Flow**, **Step**, and **Dance**).

### Key Pillars
* **Accessibility First:** Hardware should not be a gatekeeper. If you have a supported device, you can play.
* **Fitness First:** Gameplay is designed for healthy habits, pushing for full movements that are safe to perform repeatedly.
* **Open Ecosystem:** Built on Godot and open standards to encourage community modding and proprietary hardware integrations.

---

## 🥊 Gameplay Core: "Boxing"

The debut gameplay module for AeroBeat is a rhythm-boxing experience.

### The Loop
1.  **The Beat:** Targets fly toward the player in sync with the music.
2.  **The Action:** The player must punch, dodge, or block based on the incoming target or obstacles.
3.  **The Feedback:** Successful hits trigger haptic feedback (if available), satisfying visual effects, and score multipliers if available.
4.  **The Workout:** The pattern of targets forces the player into a "Flow State," seamlessly blending cardio with rhythm.

### Mechanics
* **Directional Punches:** Actions such as Jabs, Crosses, Hooks, and Uppercuts are used to hit targets based on the their income direction.
* **Left Targets** Black targets come from portals toward the athlete. They must be hit with the athletes left hand.
* **Right Targets** White targets come from portals toward the athlete. They must be hit with the ahtletes right hand.
* **Boxing Gloves** Your left hand has a visible black glove, and your right hand has a white glove. This helps you know what targets to hit with each hand.
* **Hit** If a target is hit appropriately, it explodes into a quickly decaying black or white particle with a satisfiying `smack` sound effect.
* **Near Miss** If a target hits your hand without you performing the appropriate action it flies off your hand with a `bonk` sound effect.
* **Miss** If a target gets passed you without getting hit, no sound effect is heard, but if a score multiplier is present, it will be reduced or reset.
* **Guard Targets** A target with a mix of black and white in yin-yang pattern. Requires player bring their arms together to block.
* **Obstacles:** Walls that force the player to Squat (Legs) or Lean (Core), or both.
* **Portals:** Targets fly towards the athlete from portals which can appear from one of 8 locations around the player. On 2D screens without full VR support, the targets appear from one central portal instead.
* **Stance Changes:** At the start of a song and throughout, athletes may have to swap stances (Orthodox or Southpaw) which effects their real-world leg position and ability to throw quick punches from a cetain hand. This is not tracked by gameplay and is purely as a recommendation from the choreographer or coach.
* **Knee Strikes** Lift your left or right leg at the right time to hit the knee strike target.

---

## Gameplay Agnosticism

In time, additional gameplay modules will become available, based on community requests and support.

### `FLOW` - Swing bats at targets to destroy them. Based on the `Flow` mode made popular in SuperNatural and first popularized in Beat Saber.
### `STEP` - Step on targets as they come towards you. Made popular in Stepmania and originally seen in arcades with Dance Dance Revolution.
### `DANCE` - Perform popular dance moves to match the required gestures on screen. Originally seen in Dance Central.

---

## 🎮 Input Agnosticism

AeroBeat's "Secret Sauce" is its ability to normalize data from wildly different hardware into a standard viewport space.

### Tier 1: Computer Vision (CV)
* **Tech:** MediaPipe (Python Sidecar on PC / Native Plugin on Mobile).
* **Experience:** "Controller-Free." The player stands in front of a camera. The game tracks hands, arms, shoulders, and your head.
* **Pros:** Zero cost, high accessibility.
* **Cons:** Higher latency than VR, occlusion issues.

### Tier 2: Dedicated Hardware
* **Tech:** VR Controllers, JoyCons, Dance Pads
* **Experience:** "Tactile." The player holds devices that provide rumble feedback and ultra-low latency tracking.
* **Pros:** Precision, haptics, "Pro" feel.

### Tier 3: Legacy/Debug
* **Tech:** Mouse & Keyboard, Gamepads, Touch.
* **Experience:** Used for testing charts or playing when no other input is capable.

---

## 🛠️ The "Skin" System (UGC)

To support the "YouTube" vision, visual content is strictly separated from game logic.

* **Logic (The Skeleton):** A "Target" is just a mathematical hitbox and a timestamp.
* **Skin (The Visuals):** Artists can replace the default `targets`, `obstacles`, `portals`, and `hands` to skin the games visuals.
* **Environment:** The games included environments primary show outdoor scenes on natural wonder. They can be replaced with anything from a *Live Concert Stage* to the *Moon*.

This allows the community to create "Total Conversion" aesthetics without touching a line of code.



---

## 🔮 Future Roadmap

* **Phase 1 (Prototype):** PC Build + Python CV Sidecar + Basic Boxing Core.
* **Phase 2 (Mobile):** Native Android/iOS Port + On-Device CV.
* **Phase 3 (Platform):** Support for downloading community songs/skins.
* **Phase 4 (Multiplayer):** Real-time multiplayer with other athletes or compete against ghost data.
