---
name: noootwo-design
description: Use when UI design, frontend design, visual redesign, agentic style discovery, existing-project UI adoption, design system extraction, artifact review, screenshot critique, React, Vue, Flutter, SwiftUI, Compose, native app UI, or implementation handoff work needs distinctive and non-generic product design.
license: MIT
---

# Noootwo Design

Noootwo Design helps agents turn UI requests into design-system-aware, stack-aware, reviewable interface work.

## Use This Skill For

- New UI pages, app screens, flows, dashboards, workbenches, landing pages, and prototypes
- Visual redesign, UI polish, layout improvement, typography, motion, or art direction
- React, Vue, web, Flutter, SwiftUI, Jetpack Compose, or native app visual work
- Extracting or refreshing `.noootwo/` design system memory
- Adopting Noootwo Design into an existing project midway through development
- Reviewing screenshots, prototypes, previews, or artifacts for `ready`, `refine`, `pivot`, or `needs artifact`
- Preparing design-to-implementation handoff

Do not use this for non-visual backend work, CLI tasks, pure logic bug fixes, or refactors with no UI impact.

## Project Context

Noootwo stores durable project context in `.noootwo/`. If missing, bootstrap from `assets/noootwo-harness-template/` or run `python scripts/bootstrap_noootwo_harness.py`.

Read existing files before re-deriving context:

- `.noootwo/system.md`
- `.noootwo/design-tokens.md`
- `.noootwo/adoption.md`
- `.noootwo/product-facts.md`
- `.noootwo/brief.md`
- `.noootwo/style-calibration.md`
- `.noootwo/style-discovery.md`
- `.noootwo/reference-board.md`
- `.noootwo/directions.md`
- `.noootwo/specs/active-design.md`
- `.noootwo/plans/active-implementation.md`
- `.noootwo/review.md`
- `.noootwo/handoff/implementation.md`
- `.noootwo/handoff/acceptance.md`
- `.noootwo/handoff/assets.md`

If a file is missing, stale, or `Status: pending`, refresh only what the selected mode needs.
Write system, direction, token, and handoff decisions as structured design specs: role-based rules, evidence/confidence, do/don't guidance, and implementation mapping.

## Mode Routing

Pick one mode first. Do not run the full deep flow by default.

- `quick`: Minor UI polish, small layout fixes, copy/spacing/type refinement, or "stay close to current style".
- `adopt-project`: First Noootwo use in an existing UI project. Capture baseline UI, tokens, components, screenshots/previews, constraints, and preserve/improve boundaries before redesigning.
- `standard`: Default for new UI or ordinary redesign. Use light style calibration, 3 directions, 1 artifact, typography review, and responsive review.
- `deep`: High-end, niche, rare, experimental, brand-heavy, Claude Design-like, or major redesign work. Use source evidence, mechanism clustering, spike comparison, typography gates, responsive gates, and artifact loop.
- `production`: Approved design going into implementation. Focus on design tokens, target stack mapping, screenshots/previews, and handoff.
- `extract-system`: Build or refresh `.noootwo/system.md` and `.noootwo/design-tokens.md`.
- `review`: Critique an existing artifact and decide `ready`, `refine`, `pivot`, or `needs artifact`.

If a task spans modes, use this order: `adopt-project -> extract-system -> quick/standard/deep -> review -> production`.

## Workflow State Machine

Use this state order for non-trivial UI work:

`intake -> system/adoption -> discovery -> directions -> user decision -> approved design spec -> implementation plan -> artifact -> review -> handoff`

Do not skip from directions to UI edits. After the user selects a direction, write `.noootwo/specs/active-design.md` as the approved design contract, then write `.noootwo/plans/active-implementation.md` before implementation. Skip this spec/plan gate only for `quick` polish or when the user explicitly asks for handoff-only analysis.

## Full Redesign Checkpoint

This is not a mode; it is a blocking checkpoint inside `deep` or `adopt-project -> deep`.

Trigger it when the user asks to redo all UI, start over, abandon the current visual language, or says the design is unacceptable. Capture baseline, run discovery, present 3 user-facing directions, then stop. Do not edit UI files, build Flutter routes, create final artifacts, or write handoff until `User selected direction` is recorded in `.noootwo/directions.md`.

## User Decision Gate

Ask the user whenever a material uncertainty or multi-path choice affects design direction, brand safety, novelty level, target stack, artifact strategy, implementation cost, scope, or review return path.

Present 2-3 clear options, include a recommended option with tradeoffs, and wait for the user's choice before irreversible UI edits or implementation. Record the decision in `.noootwo/directions.md`, `.noootwo/review.md`, or handoff notes.

Do not turn this into a long questionnaire. Batch related questions, ask at most 3 at once, and skip only when the existing design system gives a clear answer or the user explicitly delegates the decision to the agent.

## Mode Workflows

### Quick

- Read current UI, `.noootwo/system.md`, and `.noootwo/design-tokens.md` when available.
- Skip full style calibration and 3 directions unless the user asks.
- Ask before changing style direction, component language, color system, navigation, or interaction model.
- Make the smallest visual improvement that preserves the existing system.
- Use artifact evidence when available; otherwise state the limitation.

### Adopt Project

- Use [adoption-playbook.md](references/adoption-playbook.md).
- Inspect current UI code, tokens, components, previews, screenshots, project `AGENTS.md`, and existing `.noootwo/` status.
- Write or update `.noootwo/adoption.md` before redesigning.
- Establish preserve/improve boundaries and the first safe UI changes.
- Route to `quick`, `standard`, `deep`, `production`, `extract-system`, or `review` only after adoption baseline is recorded.

### Standard

- Refresh system facts if needed.
- Use [structured-design-spec.md](references/structured-design-spec.md) when updating system, directions, tokens, or handoff.
- Write or update a short brief.
- Run lightweight style calibration from [style-calibration.md](references/style-calibration.md).
- Present 3 materially different directions using [direction-exploration.md](references/direction-exploration.md).
- Ask the user to choose a direction before building the artifact, unless the user explicitly asks the agent to choose.
- After direction choice, create or update `.noootwo/specs/active-design.md`.
- Create `.noootwo/plans/active-implementation.md` before editing UI files.
- Build the fastest reviewable artifact for the target stack.
- Review with [review-rubric.md](references/review-rubric.md), [typography-craft-rubric.md](references/typography-craft-rubric.md), and [responsive-visual-gates.md](references/responsive-visual-gates.md).
- Do not run full source mining or spike comparison unless the user asks for a stronger, rarer, or higher-confidence exploration.

### Deep

- Use [stage-roles.md](references/stage-roles.md), [agentic-style-discovery.md](references/agentic-style-discovery.md), [source-registry.md](references/source-registry.md), [research-source-fallback.md](references/research-source-fallback.md), [taste-fit-matrix.md](references/taste-fit-matrix.md), [research-protocol.md](references/research-protocol.md), [claude-design-principles.md](references/claude-design-principles.md), [verified-ui-casebook.md](references/verified-ui-casebook.md), [reference-board.md](references/reference-board.md), [mechanism-library.md](references/mechanism-library.md), [style-lineages.md](references/style-lineages.md), [typography-craft-rubric.md](references/typography-craft-rubric.md), [responsive-visual-gates.md](references/responsive-visual-gates.md), [impeccable-style-details.md](references/impeccable-style-details.md), [workflow-cost-model.md](references/workflow-cost-model.md), and [anti-slop.md](references/anti-slop.md).
- Use [structured-design-spec.md](references/structured-design-spec.md) to convert research mechanisms into role-based design rules.
- Follow the role sequence: `Context Auditor -> Accessibility Scout -> Source Scout -> Signal Curator -> Mechanism Extractor -> Taste Strategist -> Art Director -> Typography & Composition Editor -> Artifact Spike -> Evaluator`.
- Do not generate UI directly from adjectives like "high-end", "niche", or "fashionable".
- Start with source accessibility. If preferred foreign sources are unavailable, use domestic fallback sources and record that choice.
- Search or otherwise gather real source signals, URLs, screenshots, source levels, rejected surfaces, clusters, and transfer mechanisms; record the work in `.noootwo/style-discovery.md`.
- Determine surface type before choosing sources: product UI uses real product flows, design systems, and data/task evidence; campaign/editorial UI can use more experimental galleries after downweighting utility risk.
- Record 3-5 source mechanisms in `.noootwo/reference-board.md` before generating a high-character draft.
- Run style calibration before directions.
- Require 3 directions with different type, density, composition, component language, motion, artifact strategy, discovery method, source pool, borrowed mechanisms, rejected surfaces, and taste fit score.
- Build 2-3 small artifact spikes before investing in a polished deep draft. If only 1 spike is possible, mark the review low-confidence and do not claim full exploration.
- Compare spike screenshots or previews before selecting the final direction.
- Ask the user to choose the direction or spike to continue unless they explicitly delegate the choice.
- After selection, create or update `.noootwo/specs/active-design.md`.
- Create `.noootwo/plans/active-implementation.md` before editing UI files.
- Run typography and responsive gates before `ready`; use `scripts/check_visual_gates.py` when a local web artifact is available.
- Do not polish a generic direction. Pivot.

### Production

- Convert the chosen direction into `.noootwo/design-tokens.md`.
- Read `.noootwo/specs/active-design.md` and `.noootwo/plans/active-implementation.md` before implementation. If missing, create them or ask the user to confirm skipping the gate.
- Include a design spec snapshot in `.noootwo/handoff/implementation.md`: color roles, type roles, layout model, component vocabulary, motion thesis, and forbidden moves.
- Use the relevant stack playbook:
  - Web, React, Vue, Nuxt: [web-react-vue.md](references/stacks/web-react-vue.md)
  - Flutter: [flutter.md](references/stacks/flutter.md)
  - SwiftUI, Jetpack Compose, native: [native.md](references/stacks/native.md)
- Produce implementation notes, token mapping, artifact verification, states, risks, and acceptance criteria.

### Review

- Prefer the lived artifact: screenshot, running page, simulator preview, target-stack prototype, or recorded interaction.
- If no artifact evidence exists, mark `needs artifact` unless the user explicitly accepts the limitation.
- Judge design quality and originality separately from cleanliness.
- For dashboards, workbenches, analytics, ops, monitoring, finance, or metric-heavy UI, use [data-ui-rubric.md](references/data-ui-rubric.md).
- For deep mode and style-sensitive work, use [taste-fit-matrix.md](references/taste-fit-matrix.md) and record role-based critique.
- Use [typography-craft-rubric.md](references/typography-craft-rubric.md) and [responsive-visual-gates.md](references/responsive-visual-gates.md) before `ready`.
- A `refine` decision must include one return action: `return to discovery`, `return to directions`, `return to artifact`, `return to responsive pass`, `return to typography pass`, or `return to stack pass`.
- If multiple return actions are plausible, ask the user which path to take before reworking implementation.
- If `.noootwo/directions.md`, `.noootwo/review.md`, or `.noootwo/design-tokens.md` is still `Status: pending` or full of `TBD`, do not mark the work complete or `ready`.

## Hard Rules

- Establish design system truth before inventing aesthetics.
- Design instructions must be structured: evidence/confidence, visual positioning, color roles, typography roles, layout/density, component vocabulary, states, motion, do/don't guidance, and implementation mapping.
- Visual evidence beats style adjectives.
- Material uncertainty belongs to the user. Ask for a decision when multiple viable directions, style systems, cost levels, artifact paths, or return actions exist.
- Use standard `AGENTS.md` project guidance when present; if it says to use `$noootwo-design` for UI work, follow it.
- Do not ask users to fill long style questionnaires. Recommend a calibration and proceed if they do not choose.
- Do not default to `Inter-only`, `system-only`, `hero + cards`, generic shadcn-like UI, or Flutter `Scaffold + AppBar + Card + ListView` without a product reason.
- Do not replace generic SaaS with a new generic Claude-ish formula: serif headline, mono annotations, dossier panels, pills/status dots, and archival language without product reason.
- If the full redesign checkpoint is triggered, do not internally choose a direction and start implementation unless the user explicitly says to choose and implement without review.
- Do not silently resolve high-impact design choices. Present options and wait unless the user delegates.
- For non-quick implementation, do not edit UI files until an approved design spec and an approved or delegated implementation plan exist.
- Deep mode needs a reference board; if references are missing, say so and do not pretend style invention is evidence.
- Deep mode needs agentic style discovery; if URLs, screenshots/artifact evidence, source levels, clusters, mechanisms, fit scores, or rejected surfaces are missing, return to discovery before drafting.
- Deep mode needs spike comparison; if only one spike was possible, record low confidence instead of claiming comprehensive exploration.
- Product UI and campaign UI must use different evidence pools. Do not justify a dashboard with only campaign gallery references.
- Typography craft and responsive behavior are readiness gates, not polish nice-to-haves.
- Flutter work should prefer a real route, widget preview, simulator/device screenshot, or golden-style screenshot. HTML proxy is fallback only and cannot be called stack-native ready.
- Data UI must have credible axes, units, data state, action paths, and exception priority before it can be `ready`.
- Every non-trivial design must declare artifact strategy and stack translation before implementation.
- Every selected direction must have a design-spec delta that can be translated into tokens and target-stack components.
- Every approved non-quick direction must be captured in `.noootwo/specs/active-design.md` before implementation planning.
- Every non-quick implementation must have `.noootwo/plans/active-implementation.md` before UI file edits.
- A design is not `ready` without artifact evidence or an explicit artifact limitation.
- A design is not complete while required `.noootwo/` deliverables remain `pending` or filled with `TBD`.
- Handoff must preserve design intent, tokens, component naming, states, motion decisions, artifact verification, and implementation risks.

## Reference Map

- Status script: run `python scripts/noootwo_status.py <project>` to summarize current state, blockers, and next step without reading every file.
- Project integration: [project-integration.md](references/project-integration.md)
- Research, roles, cost, and adoption: [research-protocol.md](references/research-protocol.md), [stage-roles.md](references/stage-roles.md), [agentic-style-discovery.md](references/agentic-style-discovery.md), [source-registry.md](references/source-registry.md), [research-source-fallback.md](references/research-source-fallback.md), [workflow-cost-model.md](references/workflow-cost-model.md), [adoption-playbook.md](references/adoption-playbook.md)
- Facts and assets: [fact-first.md](references/fact-first.md), [asset-protocol.md](references/asset-protocol.md)
- System and tokens: [design-system-setup.md](references/design-system-setup.md), [system-extraction.md](references/system-extraction.md), [structured-design-spec.md](references/structured-design-spec.md)
- Brief and style: [brief-expansion.md](references/brief-expansion.md), [style-calibration.md](references/style-calibration.md)
- Directions and aesthetics: [reference-board.md](references/reference-board.md), [mechanism-library.md](references/mechanism-library.md), [taste-fit-matrix.md](references/taste-fit-matrix.md), [direction-exploration.md](references/direction-exploration.md), [style-lineages.md](references/style-lineages.md), [frontend-aesthetic-principles.md](references/frontend-aesthetic-principles.md), [impeccable-style-details.md](references/impeccable-style-details.md), [anti-slop.md](references/anti-slop.md)
- Claude Design alignment: [claude-design-principles.md](references/claude-design-principles.md), [verified-ui-casebook.md](references/verified-ui-casebook.md)
- Artifact and stacks: [canvas-artifact-loop.md](references/canvas-artifact-loop.md), [target-stack-rules.md](references/target-stack-rules.md), [web-react-vue.md](references/stacks/web-react-vue.md), [flutter.md](references/stacks/flutter.md), [native.md](references/stacks/native.md)
- Review and handoff: [review-rubric.md](references/review-rubric.md), [typography-craft-rubric.md](references/typography-craft-rubric.md), [responsive-visual-gates.md](references/responsive-visual-gates.md), [data-ui-rubric.md](references/data-ui-rubric.md), [handoff-bundle.md](references/handoff-bundle.md)
