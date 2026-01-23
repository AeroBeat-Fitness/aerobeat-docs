# Plan: Modding SDK Template Implementation

This document outlines the steps to generate the specialized SDK templates for AeroBeat modders.

## 1. Directory Structure

We need to create three new directories in `templates/` to serve as the source of truth for the standalone SDK repositories.

*   `templates/sdk-cosmetics/`
*   `templates/sdk-avatars/`
*   `templates/sdk-environment/`

## 2. Base Template Inheritance

All three SDKs should inherit the foundational files from `templates/asset/` to ensure consistency in licensing and CI/CD.

**Files to Copy from `templates/asset/`:**
*   `.gitignore`
*   `LICENSE` (CC BY-NC 4.0)
*   `setup_dev.py` (Dependency manager)
*   `.github/workflows/cla.yml`

## 3. SDK-Specific Implementation

### A. Cosmetics SDK (`templates/sdk-cosmetics/`)
*Target: Gloves, Targets, Obstacles*

1.  **`plugin.cfg`**:
    *   Name: "AeroBeat Cosmetics SDK"
    *   Description: "Tools for creating custom gameplay assets."
2.  **`project.godot`**:
    *   Enable standard 3D import settings.
3.  **Scripts (`addons/aerobeat_sdk_cosmetics/`)**:
    *   `AeroGlove.gd`: Resource definition for gloves.
    *   `AeroTarget.gd`: Resource definition for targets.
    *   `AeroObstacle.gd`: Resource definition for walls.

### B. Avatars SDK (`templates/sdk-avatars/`)
*Target: 3D Characters*

1.  **`plugin.cfg`**:
    *   Name: "AeroBeat Avatar SDK"
    *   Description: "Tools for rigging and importing custom avatars."
2.  **`project.godot`**:
    *   Enable advanced 3D import settings (Bone mapping).
3.  **Scripts (`addons/aerobeat_sdk_avatars/`)**:
    *   `AeroAvatar.gd`: Resource definition for characters.
    *   `AvatarValidator.gd`: Editor plugin to check bone hierarchy.

### C. Environment SDK (`templates/sdk-environment/`)
*Target: Levels, Lighting, Skyboxes*

1.  **`plugin.cfg`**:
    *   Name: "AeroBeat Environment SDK"
    *   Description: "Tools for baking lightmaps and creating reactive stages."
2.  **`project.godot`**:
    *   Enable `LightmapGI` baking tools.
    *   Enable High-Quality texture import.
3.  **Scripts (`addons/aerobeat_sdk_environment/`)**:
    *   `AeroEnvironment.gd`: Resource definition for the level.
    *   `ReactiveLight.gd`: Helper script for beat-synced lighting.

## 4. Execution Steps

1.  [ ] Create folders.
2.  [ ] Copy base files.
3.  [ ] Create dummy `.gd` scripts for the resources (to be replaced by actual Core logic later or symlinked).
4.  [ ] Run `scripts/sync_templates.ps1` to push to GitHub.