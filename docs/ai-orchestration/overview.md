# AI-Orchestration Development Using Gastown

AeroBeat is architected to be **"AI-Orchestrator-Native"**. This means the project topology and design decisions are specifically intended to be compatible with multi-agent orchestration methods.

We currently utilize the Gastown orchestration method, popularized by Steve Yegge. Gastown enables reliable multi-agent workflows by persisting work state in git-backed hooks, ensuring context isn't lost during agent restarts.

You can read more about Gastown at the public [Github repo](https://github.com/steveyegge/gastown).

---

## 🏗️ Core Architecture & Terminology

In Gastown, a **Town** acts as the workspace root containing various **Rigs** (git repositories). 

Specialized agents—primarily Claude Code instances—take up specific roles to execute work tracked via **Convoys** and **Beads**.

*   **The Mayor**: The central AI coordinator and "Chief of Staff" for the Town.

*   **Town**: The AeroBeat polyrepo root (e.g., `~/aerobeat/`).

*   **Rigs**: Individual project containers that wrap each git repository in the topology.

*   **Polecats**: Ephemeral worker agents spawned to execute specific GDScript tasks.

*   **Refinery**: The release engineer agent responsible for merge-queue management and quality gates.

*   **Beads**: Atomic units of work (issues) that track specific task states.

*   **Convoys**: Units that bundle multiple beads for tracking and assignment.

---

## 📑 Centralized Instruction Registry

To prevent configuration drift across our 15+ repositories, AeroBeat uses a **Source of Truth** (SSOT) model. All agent logic is housed within the `aerobeat-docs` repository.

### The Registry File

Every agent entering the Town is directed to the **Global Orchestration Registry**: `~/aerobeat/aerobeat-docs/docs/ai-orchestration/instructions.md`

This file acts as a directory, pointing agents to their specific operating manuals (Mayor, Polecat, Refinery, etc.) based on their assigned role.

---

## 🎩 The Mayor

The Mayor manages the overarching polyrepo structure and enforces license safety. It breaks down complex engineering requests into atomic **Beads** and assigns them to the appropriate Rigs.

### 1. Create the Mayor Alias

Register the persistent alias to ensure the Mayor always loads the correct orchestration logic:

```bash
gt config agent set aerobeat-mayor "claude --prompt-mode none --instructions-file ~/aerobeat/aerobeat-docs/docs/ai-orchestration/aerobeat-mayor.md"
```

### 2. Start the Session

Initialize the Town coordination session:

```bash
gt mayor start --agent aerobeat-mayor
```

---

## 🦨 Polecats

Polecats are the "proletariat" worker agents. They operate within a specific Rig, following sequential actionable steps assigned by the Mayor.

*   **Protocol**: Polecats must follow the **AeroBeat Style Guide** (Static Typing, Signal Up/Call Down).

*   **Quality**: They are required to use Test-Driven Development (TDD) with GUT, aiming for 100% logic coverage.

*   **Context**: Each Rig contains a `CLAUDE.md` that points the Polecat to the global `instructions.md` and the local `README.md`.

---

## 🛡️ The Refinery

The Refinery is a specialized role that serves as the automated quality gatekeeper. It reviews code produced by Polecats before it is permitted to enter the `main` branch.

### 1. Create the Refinery Alias

Register the alias for review-focused tasks:

```bash
gt config agent set aerobeat-refinery "claude --prompt-mode none --instructions-file ~/aerobeat/aerobeat-docs/docs/ai-orchestration/aerobeat-refinery.md"
```

### 2. The Review Workflow (MEOW)

The Mayor remains the "Chief of Staff" and "slings" the completed work to a Refinery-tuned agent for final verification.

```bash
# Mayor assigns a completed Bead to the Refinery for review
gt sling <bead-id> <rig-name> --agent aerobeat-refinery
```

### 3. Rig-Level Integration

Every Rig's `CLAUDE.md` must include this pointer to ensure compliance:

```text
## 🛡️ Quality Gate: The Refinery
All code in this Rig is subject to automated review by the **AeroBeat Refinery**.
* **Instructions**: Refer to `~/aerobeat/aerobeat-docs/docs/ai-orchestration/instructions.md`.
* **Requirement**: No PR will be merged without 100% GUT coverage and license verification.
```

### 4. Automated Gates

The Refinery automatically rejects PRs that fail:

*   **License Safety**: No GPLv3 code in MPL 2.0 repositories.

*   **Topology Check**: Dependencies must flow DOWN (Assembly -> Feature -> Core).

*   **Style/Coverage**: Strict adherence to the GDScript style guide and 100% test coverage.