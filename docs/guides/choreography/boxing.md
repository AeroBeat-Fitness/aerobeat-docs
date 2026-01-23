# Creating Boxing Choreography

Boxing is the core gameplay of AeroBeat. A good boxing chart is a conversation between the music and the athlete's body. It uses punches to express rhythm and obstacles to force body movement (squats and leans).

## 🛠️ The Boxing Studio

*   **Tool:** **Boxing Choreography Studio**
*   **Grid:** 5 Zones (Left, Right, Low-Left, Low-Right, Center).
*   **Perspective:** 3D Portal View (Targets fly towards you).

## 🥊 Mechanics & Objects

### Targets (Punches)

*   **Color Coding:**
    *   **Black:** Left Hand.
    *   **White:** Right Hand.
*   **Positioning:** Targets spawn at specific heights relative to the user's calibration.
    *   **Standard:** Arm height (Left/Right).
    *   **Low:** Crouch height (Left/Right).
    *   **Center:** Reserved for **Guard/Block** targets.
*   **Direction:** The arrow on the target dictates the punch type.
    *   *Up Arrow:* Uppercut (Left or right vertical punch).
    *   *Side Arrow:* Hook (Left or right horizontal punch).
    *   *Dot:* Jab Or Cross (Left or right hand forward punch).

### Obstacles (Movement)

Obstacles spawn within a specific radius around the active portal, using a separate positioning system to force body movement.

> **Tracking Note:** Collision is determined solely by the player's **Head** position.

*   **Vertical Wall:** Forces a lean (engages core).
*   **Horizontal Bar:** Forces a squat (engages legs).
*   **Angled Wall:** Forces a specific body rotation.

### Stance Changes (Form)

Stance indicators appear on the track to guide the athlete's foot placement. While the game does not track feet in Boxing mode, proper stance is critical for power and flow.

*   **Orthodox:** Swap body position so your **Left Foot** is pointing forward.
*   **Southpaw:** Swap body position so your **Right Foot** is pointing forward.

> **Note:** Failing to change your body to the correct side does not affect your score. It is merely a guide to keep the athlete in proper form for the upcoming choreography, as determined by you (the choreographer).

### Knee Strikes (Legs)

Knee strikes add lower-body intensity to the workout.

*   **Target:** A specific "Knee Target" (Black or White) that appears low in the portal.
*   **Action:** Lift the corresponding knee (Left=Black, Right=White) to intercept the target.
*   **Placement:** These should always be placed on the **Bottom Row** of the grid to align with the knee lift height.
*   **Tracking:** The engine does not track legs in Boxing mode. Instead, it checks if the player's **Head** is horizontally aligned with the target lane. This allows for accessibility modifications (like substituting a Knee Strike for a Block/Crunch).

## 📐 Mapping Best Practices

### 1. Flow & Parity

The "Golden Rule" of boxing mapping is **Flow**.

*   **Alternation:** The most natural rhythm is L -> R -> L -> R.
*   **Reset:** After a punch, the hand needs time to return to the "Guard" position.
*   **Bad Parity:** Avoid "Double Vision" (placing a target directly behind another) or "Hand Tangles" (Cross-body Left punch followed immediately by a far-left punch).

### 2. Fitness Intensity

*   **Squats:** The most calorie-burning move. Use horizontal bars on the downbeats of the chorus.
*   **Reach:** Use the outer lanes to force full arm extension.
*   **Core:** Use vertical walls to force rapid side-to-side weaving.

### 3. 360 vs. 2D

When mapping in the Boxing SDK, you can place targets in a 360-degree ring.

*   **VR Players:** Will physically rotate to face the new portal.
*   **2D Players:** The engine automatically "folds" these targets to the front.
*   **Relative Lanes:** The 5-Zone Grid is always **relative to the Active Portal**. If the player turns 90 degrees right, "Left Arm" is still their physical left hand.

#### Rotation Cues (The Fitness Flow)

Instead of random portal jumps, use the choreography to guide the turn.

*   **The Guide:** Use obstacles and directional punches (Hooks) to force body rotation towards the next target zone. Sequential portals in a single direction also create a strong guiding flow.
*   **Example:** If the next portal is to the **Right**, end the current phrase with a **Left Hook** or **Right Cross**. This naturally rotates the athlete's torso to the right, setting them up for the new portal.
*   **Visuals:** Every active portal emits a particle trail flowing towards the player to help them center their stance.

> **Note:** **Simultaneous Portals** (targets coming from multiple directions) are a valid mechanic for high-intensity "Pro" charts, but use them sparingly to maintain flow.

## 🚀 Workflow Tips

### Pattern Prefabs

Use the **Prefab Library** (Spacebar) to drag-and-drop common boxing combos:

*   **"The 1-2":** Left Jab, Right Cross.
*   **"The Weave":** Wall Left, Wall Right, Wall Left.
*   **"The Burpee":** High Target, Squat Wall, High Target.

### Difficulty Grading

| Difficulty | Mechanics | Density |
| :--- | :--- | :--- |
| **Easy** | On-beat only. No obstacles. | Low |
| **Medium** | Simple 1-2 combos. Basic walls. | Moderate |
| **Hard** | 1/8th streams. Squats. Wide reaches. | High |
| **Pro** | 1/16th bursts. Complex weaves. 360 rotation. | Extreme |

## 🛡️ Validation

Always run the **"Flow Validator"** before uploading. It checks for impossible reaches and vision blocks specific to the human arm span.