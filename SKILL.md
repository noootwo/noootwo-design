---
name: noootwo-design
description: Noootwo Design turns a rough design request into a reusable design system, explicit 3-direction exploration, review loop, and implementation handoff. Use when the user asks to design a new page, evolve an existing UI, extract a project's design system, review a visual artifact, or prepare a design-to-implementation handoff for web, Flutter, or HTML-native work.
license: MIT
---

# Noootwo Design

Type once, get a design worth shipping.

Noootwo Design is not a generic frontend helper. It is a design partner that establishes a design system before task work, explicitly presents 3 strong art directions before drafting, uses a first-draft then critique loop, and only hands work off after it has passed review.

## Use This Skill For

- Designing a new page, flow, prototype, screen, or workbench
- Extracting a project's design system from code, screenshots, or live product surfaces
- Reviewing an existing visual artifact and deciding whether it is ready, needs refinement, or should pivot
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
- `review`: Critique an existing artifact and decide `ready`, `refine`, or `pivot`
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

### 2. Design System Setup

- Read `.noootwo/system.md` first
- If it is absent or incomplete, establish it before any task-specific design work
- Use [design-system-setup.md](references/design-system-setup.md) for source order and confirmation rules
- Use [system-extraction.md](references/system-extraction.md) to capture concrete design-system memory
- Update `.noootwo/system.md` with brand primitives, type system, component patterns, layout density, motion language, known generic fallbacks, and forbidden combinations
- Mark inferred values as inferred; do not present them as confirmed brand truth

### 3. Brief Expansion

- Expand the current task into `.noootwo/brief.md`
- Capture audience, desired outcome, constraints, non-goals, and success criteria
- Capture tone extreme, aesthetic ambition, novelty target, motion appetite, brand-safety tolerance, one unforgettable thing, and what the result must or must not feel like
- If the user does not specify these, write explicit defaults instead of silently choosing a conservative path
- Keep the brief strategic. Do not lock implementation details too early
- See [brief-expansion.md](references/brief-expansion.md)

### 4. Direction Exploration

- For new design work, redesigns, and major refinements of existing surfaces, explicitly present 3 distinct directions before building
- Only skip directions when the user clearly asks for minor polish or to stay close to the current system
- Each direction must include a concrete lineage, a tone extreme, one unforgettable thing, typography plan, color discipline, grid and density target, shape rules, component vocabulary, motion thesis, background/detail thesis, image treatment, why it feels rare, and explicit anti-patterns
- Recommend one default direction
- Use [direction-exploration.md](references/direction-exploration.md)
- Use [style-lineages.md](references/style-lineages.md) by default unless the current brand system is already strong enough to support 3 clearly differentiated directions without it
- Use [frontend-aesthetic-principles.md](references/frontend-aesthetic-principles.md) to keep typography, color, motion, composition, and detail treatment coordinated
- Show all 3 directions to the user before proceeding to draft work
- Minor polish work or strict follow-existing-style work may skip this step only if the user explicitly says so

### 5. Direction Preflight, First Draft, Critique, Polish

- After choosing a direction, declare the chosen lineage, tone extreme, one unforgettable thing, type pairing, color discipline, density target, component vocabulary, motion thesis, background/detail thesis, and forbidden patterns before generating a draft
- Do not start a draft if the chosen direction still lacks type contrast, density stance, component language, motion thesis, or background/detail thesis
- New surfaces or major redesigns: build a first draft fast enough to expose direction risk, then iterate into the fuller design or prototype
- Existing product refinements: work inside the target stack after extracting the system
- Apply [frontend-aesthetic-principles.md](references/frontend-aesthetic-principles.md), [anti-slop.md](references/anti-slop.md), and [target-stack-rules.md](references/target-stack-rules.md)
- Review the draft as an evaluator, not as the generator that just made it
- Only polish after critique confirms the direction is fundamentally right

### 6. Independent Review And Handoff

- Every design deliverable must go through review before it is considered ready
- Use [review-rubric.md](references/review-rubric.md)
- Decide `ready`, `refine`, or `pivot`
- Run at most 2 full review loops before surfacing the trade-off to the user
- If the result is meant to be implemented and has passed review, produce `.noootwo/handoff/implementation.md`, `.noootwo/handoff/acceptance.md`, and `.noootwo/handoff/assets.md`
- Use [handoff-bundle.md](references/handoff-bundle.md)

## Hard Rules

- Fact verification outranks intuition. Never guess the status, existence, or version of a named product or technology
- Read durable memory before re-deriving context
- Do not design from thin air if you can extract a real system
- Establish the design system before task-specific aesthetics
- New design work defaults to 3 explicit directions first
- Existing-surface redesigns also default to 3 explicit directions unless the user explicitly asks for polish only
- Every direction must answer two questions before drafting: what is the tone extreme, and what is the one unforgettable thing
- Do not fall back to `Inter-only`, `system-only`, or generic SaaS patterns without a brand-backed reason
- Default to strong, opinionated directions unless the user explicitly asks for a conservative path
- Typography, color, motion, composition, and background/detail treatment must support the same point of view
- A design is not ready without a review artifact
- An implementation handoff is not ready without assets, acceptance criteria, and interaction notes
- Review is based on quality, originality, craft, and functionality, not personal taste alone

## Reference Map

- Facts and brand reality: [fact-first.md](references/fact-first.md)
- Asset sourcing and recording: [asset-protocol.md](references/asset-protocol.md)
- Design system setup: [design-system-setup.md](references/design-system-setup.md)
- Persistent system memory: [system-extraction.md](references/system-extraction.md)
- Task brief: [brief-expansion.md](references/brief-expansion.md)
- Design directions: [direction-exploration.md](references/direction-exploration.md)
- Fallback archetypes and lineages: [style-lineages.md](references/style-lineages.md)
- Frontend aesthetic principles: [frontend-aesthetic-principles.md](references/frontend-aesthetic-principles.md)
- Anti-slop guardrails: [anti-slop.md](references/anti-slop.md)
- Review scoring and loop rules: [review-rubric.md](references/review-rubric.md)
- Handoff output: [handoff-bundle.md](references/handoff-bundle.md)
- Stack-specific execution: [target-stack-rules.md](references/target-stack-rules.md)
