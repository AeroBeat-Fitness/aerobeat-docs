# Coding Style Guide

### CONTEXT: AEROBEAT

- Target Engine: Godot 4.6
- Priority: Timing accuracy, signal safety, and static typing.
- Style: Godot 2.0 (GDScript 2) Standard.

This guide contains rules for .gdscript files in AeroBeat.

### SYNTAX RULES (GODOT 4.x ONLY)

1. NO LEGACY ANNOTATIONS: Always use '@' prefix (e.g., @onready, @export, @tool, @icon). Never use 'onready var' or 'export var'.

2. SIGNAL CONNECTIVITY: Use the Callable-based syntax: `signal_name.connect(target_method)`. Never use the old string-based `.connect("signal", self, "method")`.

3. INSTANTIATION: Use `.instantiate()`. Never use `.instance()`.

4. COROUTINES: Use `await`. Never use `yield`.

5. PROPERTY ACCESS: Use direct properties (e.g., `node.name = "X"`) instead of setters (e.g., `node.set_name("X")`) unless a setter is specifically required for logic.

6. TYPED ARRAYS: Always use typed arrays for rhythm data: `var notes: Array[NoteResource] = []`.

### Additional Syntax Rules

1.  **Typed Variables:** ALWAYS use explicit types.
    *   ❌ `var score = 0`
    *   ✅ `var score: int = 0`
2.  **Private Methods:** Prefix internal functions with `_`.
    *   ✅ `func _calculate_score() -> void:`
3.  **Inferred Types:** Use `:=` only for unambiguous types (Vector2, String).

### Architectural Patterns

1.  **Composition over Inheritance:** Use components (`Node` children) rather than deep `extends` chains.
2.  **Signal Up, Call Down:**
    *   Children emit **Signals** to talk to Parents.
    *   Parents call **Functions** to talk to Children.
    *   **NEVER** let a Child node access `get_parent()`.

### AeroBeat Specifics

1.  **Input:** NEVER use `Input.is_action_pressed()`. ALWAYS use `AeroInputProvider`.
2.  **Time:** NEVER use `delta` for rhythm sync. ALWAYS use `AudioServer.get_dsp_time()`.

### File Structure & Organization

1.  **Docstring:** `##` Description of the class.
2.  **Class Definition:** `class_name` then `extends`.
3.  **Regions:** Organize code in this order using `#region`:
    1.  `SIGNALS`
    2.  `ENUMS & CONSTANTS`
    3.  `EXPORTS`
    4.  `PUBLIC VARIABLES`
    5.  `PRIVATE VARIABLES` (`_`)
    6.  `ONREADY`
    7.  `LIFECYCLE` (`_ready`, `_process`)
    8.  `PUBLIC API`
    9.  `PRIVATE API` (`_`)

### Documentation & Formatting

1.  **Docstrings:** Use `##` for all classes and public functions (required for auto-docs).
2.  **Separators:** Use `# ---------------------------------------------` for major blocks.
3.  **Spacing:** Two empty lines between functions.

### Godot Syntax Rules

1. **Prefixes:** All core classes must start with `Aero` (e.g., `AeroSessionContext`).
2. **Extensions:** Use `.gd` for logic, `.tscn` for scenes, `.tres` for data.
3. **Strict Typing:** All GDScript must be static typed (e.g., `func get_name() -> String:`).

### ANTI-HALLUCINATION PROTOCOL

- STOICISM: If you are unsure if a method exists in Godot 4.x, do not guess. State "API_UNKNOWN: [Method Name]" and ask for clarification.

- STATIC TYPING: Every variable and function return MUST be explicitly typed (e.g., `func _process(delta: float) -> void:`). This prevents type-inference hallucinations.

- PLAN-THEN-CODE: Before writing any code, provide a 1-sentence logic plan.
  - *Example: "Plan: I will use a Tween to handle the hit-sprite fade to ensure it doesn't interrupt the physics thread."*

### ERROR HANDLING

If the user provides an error log, analyze it using "Step-Back" reasoning: 

1. What node owns the script? 

2. Is the signal connected? 

3. Is the variable null?