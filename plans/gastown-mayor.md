# AeroBeat Gastown Mayor Guide Plans

This document outlines the creation of the "Mayor's Handbook"—a specific context file (`docs/ai-prompting/gastown-mayor.md`) designed to align the Gastown Orchestrator (Mayor) with AeroBeat's strict architectural and licensing constraints.

## 1. Objective
To provide the Mayor agent with a high-level map of the project so it can intelligently break down complex user requests into safe, atomic "Beads" for the worker agents (Polecats).

## 2. The Problem
Standard agents do not understand our "Hub-and-Spoke" topology or the legal risks of mixing GPL (Feature) and MPL (Core) code. Without this guide, the Mayor might assign a task that violates these boundaries.

## 3. The Solution: `gastown-mayor.md`
We will create a prompt file that the user pastes to the Mayor at the start of a session.

### Key Sections
1.  **Identity & Role:** "You are the Mayor of AeroBeat."
2.  **The Prime Directive:** Prevent License Contamination.
3.  **Repository Topology:** A lookup table of Repo Name -> License -> Allowed Dependencies.
4.  **Bead Strategy:** Instructions on how to split tasks (e.g., "Update Core first, then update Feature").
5.  **Context Injection:** Reminder that Polecats auto-load the `AI_MANIFEST`, so the Mayor doesn't need to paste the whole file, just reference it.

## 4. Execution
- [x] Create `docs/ai-prompting/gastown-mayor.md`.
- [x] Document the Repo/License map clearly.
- [x] Define the "Dependency Flow" rules (Assembly -> Feature -> Core).

## 5. Usage
When starting a Gastown session:
`gt mayor attach` -> Paste contents of `docs/ai-prompting/gastown-mayor.md`.
