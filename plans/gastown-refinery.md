# AeroBeat Gastown Refinery Guide Plans

This document outlines the creation of the "Refinery's Handbook"—a context file (`docs/ai-prompting/gastown-refinery.md`) that turns an AI agent into an automated code reviewer and merger for the Gastown system.

## 1. Objective
To create a "gatekeeper" agent that automatically reviews Pull Requests from Polecat agents, ensuring all code merged into the main branch meets our strict quality and licensing standards.

## 2. The Problem
A swarm of Polecats can generate dozens of PRs quickly. Manual human review is a significant bottleneck and is prone to error. Without an automated reviewer, bad code (license violations, style issues) could be merged.

## 3. The Solution: `gastown-refinery.md`
We will create a system prompt that gives the Refinery agent a non-negotiable checklist for reviewing code.

### Key Sections
1.  **Identity & Role:** "You are the Refinery."
2.  **The Prime Directive:** "Your job is to protect the `main` branch."
3.  **The Review Checklist:** A step-by-step process for validating a PR.
    *   License & Topology Check.
    *   Style Guide Adherence Check.
    *   Test Coverage Mandate Check (TDD).
    *   Defensive Coding & Safety Check.
    *   Bead Completion Check.
4.  **Merge & Reject Protocols:** Clear instructions on how to merge, how to close duplicates, and how to provide actionable feedback on rejected PRs.

## 4. Execution
- [x] Create `docs/ai-prompting/gastown-refinery.md`.
- [x] Define the strict, multi-point review checklist.
- [x] Provide templates for rejection messages.