---
name: noootwo-design
description: Noootwo Design turns a rough design request into a reusable design system, direction exploration, review loop, and implementation handoff. Use when the user asks to design a new page, evolve an existing UI, extract a project's design system, review a visual artifact, or prepare a design-to-implementation handoff for web, Flutter, or HTML-native work.
license: MIT
---

# Noootwo Design

Type once, get a design worth shipping.

Noootwo Design is not a generic frontend helper. It is a design partner that keeps durable context, explores directions before committing, critiques its own work, and hands implementation to another agent in a structured bundle.

## Use This Skill For

- Designing a new page, flow, prototype, screen, or workbench
- Extracting a project's design system from code, screenshots, or live product surfaces
- Reviewing an existing visual artifact and deciding whether to refine or pivot
- Producing an implementation handoff for Claude Code, Codex, Cursor, or another agent

Do not use this skill for non-visual back-end work, CLI tools, or pure bug fixing without a design question.

## Harness Contract

Noootwo Design persists project context in `.noootwo/`.

If `.noootwo/` does not exist yet, bootstrap it from `assets/noootwo-harness-template/` or run `python scripts/bootstrap_noootwo_harness.py`.

Always read these files first when they exist:

- `.noootwo/system.md`
- `.noootwo/product-facts.md`
- `.noootwo/brief.md`
- `.noootwo/directions.md`
- `.noootwo/review.md`
- `.noootwo/handoff/implementation.md`
- `.noootwo/handoff/acceptance.md`
- `.noootwo/handoff/assets.md`

If a file is missing, stale, or marked `Status: pending`, refresh it before relying on it. Treat these files as the durable truth between sessions.

## Mode Routing

Pick one primary mode before you work:

- `design`: New surface, redesign, prototype, or direction exploration
- `extract-system`: Build or refresh `.noootwo/system.md`
- `review`: Critique an existing artifact and decide `refine` vs `pivot`
- `handoff`: Convert an approved design into `.noootwo/handoff/*`

If a task spans multiple modes, execute them in this order:

1. `extract-system`
2. `design`
3. `review`
4. `handoff`

## Core Workflow

### 1. Context Intake

- Read the user's request, current repo, existing UI, and `.noootwo/*`
- If the task names a specific brand, product, feature launch, or versioned technology, read [fact-first.md](references/fact-first.md) before anything else
- If the request depends on brand assets, read [asset-protocol.md](references/asset-protocol.md)

### 2. System Extraction

- Read `.noootwo/system.md` first
- If it is absent or incomplete, extract the design language from code, screenshots, or live product surfaces using [system-extraction.md](references/system-extraction.md)
- Update `.noootwo/system.md` with concrete tokens, vocabulary, and constraints

### 3. Brief Expansion

- Expand the current task into `.noootwo/brief.md`
- Capture audience, desired outcome, constraints, non-goals, and success criteria
- Keep the brief strategic. Do not lock implementation details too early
- See [brief-expansion.md](references/brief-expansion.md)

### 4. Direction Exploration

- For new design work, ambiguous requests, or major redesigns, create 3 distinct directions before building
- Each direction must include design philosophy, visual tone, why it fits, and main risks
- Recommend one default direction
- Use [direction-exploration.md](references/direction-exploration.md)
- Minor polish work or strict follow-existing-style work may skip this step only if the brief is explicit and the surface is already established

### 5. Prototype Or Draft

- New surfaces or major redesigns: build a v0 draft first, then the fuller design or prototype
- Existing product refinements: work inside the target stack after extracting the system
- Apply [anti-slop.md](references/anti-slop.md) and [target-stack-rules.md](references/target-stack-rules.md)

### 6. Independent Review And Handoff

- Every design deliverable must go through review before it is considered ready
- Use [review-rubric.md](references/review-rubric.md)
- Decide `refine` or `pivot`
- Run at most 2 full review loops before surfacing the trade-off to the user
- If the result is meant to be implemented, produce `.noootwo/handoff/implementation.md`, `.noootwo/handoff/acceptance.md`, and `.noootwo/handoff/assets.md`
- Use [handoff-bundle.md](references/handoff-bundle.md)

## Hard Rules

- Fact verification outranks intuition. Never guess the status, existence, or version of a named product or technology
- Read durable memory before re-deriving context
- Do not design from thin air if you can extract a real system
- New design work defaults to 3 directions first
- A design is not ready without a review artifact
- An implementation handoff is not ready without assets, acceptance criteria, and interaction notes
- Review is based on quality, originality, craft, and functionality, not personal taste alone

## Reference Map

- Facts and brand reality: [fact-first.md](references/fact-first.md)
- Asset sourcing and recording: [asset-protocol.md](references/asset-protocol.md)
- Persistent system memory: [system-extraction.md](references/system-extraction.md)
- Task brief: [brief-expansion.md](references/brief-expansion.md)
- Design directions: [direction-exploration.md](references/direction-exploration.md)
- Anti-slop guardrails: [anti-slop.md](references/anti-slop.md)
- Review scoring and loop rules: [review-rubric.md](references/review-rubric.md)
- Handoff output: [handoff-bundle.md](references/handoff-bundle.md)
- Stack-specific execution: [target-stack-rules.md](references/target-stack-rules.md)
