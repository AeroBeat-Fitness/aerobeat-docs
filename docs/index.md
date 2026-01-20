# Welcome to AeroBeat

**AeroBeat** is an open-source, modular rhythm game platform designed to democratize fitness gaming. Think of it as the "YouTube of Workout Games" — a place where hardware inputs, gameplay mechanics, and community content can be mixed and matched freely.

Unlike traditional rhythm games that are locked to specific hardware (VR headsets or consoles), AeroBeat's engine is **Hardware Agnostic** and **Input Agnostic**. It runs on PC's, Mobile Devices, and VR.

AeroBeat is **Gameplay Agnostic**, it can support an unlimited range of other rhythm gameplay '**Cores**'.

Right now, we are working towards version **0.0.1** a focus on our **Boxing** gameplay on **PC** platforms utilizing **Computer Vision** to turn standard webcams into motion controllers.

---

## 📚 Documentation Structure

Our documentation is divided by role. Choose your path below:

### 🥊 [Game Design (GDD)](gdd/concept.md)
*For Designers and Visionaries.*
* Read the **Core Loop** and Scoring Logic.
* Understand the "Fitness-First" approach to difficulty.
* Explore the roadmap for Multiplayer and Workshop features.

### 🛠️ [Technical Architecture](architecture/architecture.md)
*For Software Engineers and System Architects.*
* Understand the **Hub-and-Spoke Polyrepo** topology.
* Learn how `aerobeat-core` manages contracts between modules.
* Dive into the **Session Context** dependency injection system.
* **Key Tech:** Godot 4.x, GDScript, Python (MediaPipe).

### 🎨 [Asset Pipeline](assets/pipeline.md)
*For 3D Artists, Animators, and Mappers.*
* How to inherit from `base_target.tscn` to create skins.
* Understanding the **Single-Dependency Rule** for Asset Packages.
* Licensing guide for **CC BY-NC 4.0** contributions.

---

## 📂 Repository Ecosystem

AeroBeat uses a 5-tier repository structure to keep code clean and decoupled.

| Repository | Role | License |
| :--- | :--- | :--- |
| **[`aerobeat-assembly`](#)** | The Game Client (The "Glue"). Builds the executable. | **GPLv3** |
| **[`aerobeat-core`](#)** | The Engine Hub. Contracts, Signals, and Data Types. | **MPL 2.0** |
| **[`aerobeat-feature-*`](#)** | Gameplay Logic (e.g., Boxing, Input Managers). | **GPLv3** |
| **[`aerobeat-asset-*`](#)** | Content Packs (Skins, Environments). | **CC BY-NC 4.0** |
| **[`aerobeat-docs`](#)** | This documentation site. | **CC BY-SA 4.0** |

---

## 🤝 Contributing

We welcome contributions of all kinds! Whether you are fixing a bug in the Core, designing a new environment, or writing an iput driver for a new hardware device.

1.  **Check the License:** Please review our [Licensing Overview](licensing/overview.md) to understand how your contributions will be protected.
2.  **Pick a Repo:** Navigate to the specific repository relevant to your skill set.
3.  **Run Setup:** Use the included `./setup_dev` script to initialize your local environment.

> **Current Status:** AeroBeat is currently in **Prototype (v0.0.1)**. We are actively building the Core Contracts and the initial Boxing Feature.

---

*AeroBeat-Fitness &copy; 2026. "Move to the Beat."*
