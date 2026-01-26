# AeroBeat Gastown Polecat Guide Plans

This document outlines the creation of the "Polecat's Field Manual"—a unified context file (`docs/ai-prompting/gastown-polecat.md`) that is automatically injected into every worker agent session.

## 1. Objective
To provide ephemeral worker agents (Polecats) with all necessary rules (Style, Topology, Terminology) in a single file, eliminating the need for the Mayor to manually paste context or for the agent to "hallucinate" rules.

## 2. The Problem
Currently, we have three separate context files (`AI_MANIFEST`, `STYLE_GUIDE`, `GLOSSARY`).
*   Agents often forget to check all three.
*   Agents do not know which License constraints apply to their current repo.

## 3. The Solution: `gastown-polecat.md`
We will combine the "Context Trinity" into a single, optimized prompt file.

### Key Sections
1.  **Identity:** "You are a Polecat."
2.  **Safety Layer:** Explicit License boundaries (MPL vs GPL).
3.  **Style Guide:** Condensed rules for GDScript (Typing, Signals).
4.  **Manifest:** Directory topology constraints.
5.  **Glossary:** Key domain terms.
6.  **Testing:** Mandate for GUT tests.

## 4. Execution
- [x] Create `docs/ai-prompting/gastown-polecat.md`.
- [x] Merge `STYLE_GUIDE.md` content.
- [x] Merge `AI_MANIFEST.md` content.
- [x] Update `gastown-mayor.md` to reference this new injection file.