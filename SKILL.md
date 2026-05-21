---
name: noootwo-design
description: Use when UI design, frontend design, visual redesign, agentic style discovery, influence discovery, existing-project UI adoption, design system extraction, artifact review, screenshot critique, React, Vue, Flutter, SwiftUI, Compose, native app UI, or implementation handoff work needs distinctive and non-generic product design.
license: MIT
---

# Noootwo Design

Noootwo Design turns UI requests into design-system-aware, stack-aware, reviewable interface work, with explicit preservation contracts so the discovered style survives translation into tokens, components, motion, and handoff. For implementation-bound work, it can also run a detail-translation pass so the style survives the last mile: surface inventory, component restyling, default overrides, and micro-detail review.

Use for new UI pages, app screens, dashboards, workbenches, landing pages, visual redesign, typography, motion, art direction, screenshot review, design-system extraction, and handoff. Do not use for backend-only work, CLI tasks, pure logic bug fixes, or refactors with no UI impact.

## Project Context

Durable context lives in `.noootwo/`. If missing, bootstrap minimal context from `assets/noootwo-harness-template/` or run `python scripts/bootstrap_noootwo_harness.py`. Use `--profile deep`, `--profile production`, or `--profile full` only when those templates are needed.

Read only what the selected mode needs. Useful files include:

- `.noootwo/system.md`, `.noootwo/design-tokens.md`, `.noootwo/adoption.md`, `.noootwo/product-facts.md`
- `.noootwo/brief.md`, `.noootwo/style-calibration.md`, `.noootwo/style-discovery.md`, `.noootwo/reference-board.md`, `.noootwo/directions.md`
- `.noootwo/specs/active-design.md`, `.noootwo/plans/active-implementation.md`
- `.noootwo/review.md`, `.noootwo/handoff/implementation.md`, `.noootwo/handoff/acceptance.md`, `.noootwo/handoff/assets.md`

If a file is missing, stale, or `Status: pending`, refresh only the minimum needed for the current step. Write decisions as structured design specs: evidence, confidence, color roles, type roles, layout/density, component vocabulary, motion, do/don't guidance, preservation contract, detail translation, and stack mapping.

## Mode Routing

Pick one mode first; do not run deep by default.

- `quick`: minor polish, spacing/type fixes, or "stay close to current style".
- `adopt-project`: first Noootwo use in an existing UI project; capture baseline before redesigning.
- `standard`: ordinary new UI/redesign; light calibration, 3 directions, 1 artifact, review.
- `deep`: high-end, niche, rare, brand-heavy, Claude Design-like, full redesign, or previous output was too generic.
- `production`: approved design implementation; tokens, stack mapping, artifact verification, handoff.
- `extract-system`: build or refresh design memory and tokens.
- `review`: critique an artifact and decide `ready`, `refine`, `pivot`, or `needs artifact`.

Order for multi-step work: `adopt-project -> extract-system -> quick/standard/deep -> review -> production`.

## Workflow Gates

Use this state machine for non-trivial UI work:

`intake -> system/adoption -> discovery -> directions -> user decision -> approved design spec -> implementation plan -> artifact -> review -> handoff`

Do not skip from directions to UI edits. After user selection, write `.noootwo/specs/active-design.md`; before UI edits, write `.noootwo/plans/active-implementation.md`. Skip this spec/plan gate only for `quick` polish, handoff-only analysis, or explicit user approval.

Full redesign checkpoint: if the user asks to redo all UI, start over, abandon the current visual language, or says the design is unacceptable, run discovery, present 3 user-facing directions, then stop. Do not implement until `User selected direction` is recorded.

User decision gate: ask the user when material uncertainty affects direction, brand safety, novelty, target stack, artifact strategy, cost, scope, or review return path. Present 2-3 options with a recommendation and tradeoffs. Batch questions; do not create a long questionnaire.

## Mode Workflows

### Quick

- Read current UI, `.noootwo/system.md`, and `.noootwo/design-tokens.md` when available.
- Preserve the existing system. Ask before changing style direction, color system, navigation, component language, or interaction model.
- Use artifact evidence when available; otherwise state the limitation.

### Adopt Project

- Use [adoption-playbook.md](references/adoption-playbook.md).
- Inspect current UI code, tokens, components, screenshots/previews, `AGENTS.md`, and `.noootwo/` status.
- Update `.noootwo/adoption.md`, establish preserve/improve boundaries, then route to the next mode.

### Standard

- Refresh system facts if needed, write a short brief, and use [structured-design-spec.md](references/structured-design-spec.md).
- Run light calibration, present 3 materially different directions with openable case links, ask for selection, then create approved spec and implementation plan before UI edits.
- Build the fastest target-stack artifact and review with typography/responsive gates.

### Deep

- Use deep only for high-character work. Read discovery references only when needed: [agentic-style-discovery.md](references/agentic-style-discovery.md), [source-registry.md](references/source-registry.md), [reference-board.md](references/reference-board.md), [taste-fit-matrix.md](references/taste-fit-matrix.md), [workflow-cost-model.md](references/workflow-cost-model.md), and [anti-slop.md](references/anti-slop.md).
- Run source accessibility, source weighting, mechanism clustering, and optional influence discovery before directions.
- Influence discovery finds designers, artists, studios, products, movements, or spatial systems as mechanism sources. Extract transferable mechanisms; do not imitate signature style.
- Product/data UI must use product evidence and data rules; campaign/editorial UI may use more experimental references after rejecting low-utility surfaces.
- For deep confidence, record 3-5 mechanisms, present 3 directions with openable case links, build 2-3 small spikes when feasible, compare visual evidence, ask for selection, then continue to approved spec and plan.
- If source evidence, rejected surfaces, fit scores, spike comparison, or artifact evidence is missing, lower confidence and do not claim full exploration.

### Production

- Read the approved spec and implementation plan before UI edits.
- Map the chosen direction into `.noootwo/design-tokens.md` and target-stack notes.
- For implementation-bound work that risks drifting generic, run a detail-translation pass: surface inventory, component restyling matrix, default override pass, then micro-detail review.
- Use stack playbooks only when relevant: [web-react-vue.md](references/stacks/web-react-vue.md), [flutter.md](references/stacks/flutter.md), [native.md](references/stacks/native.md).

### Review

- Prefer lived artifacts: screenshot, running page, simulator preview, target-stack prototype, or recorded interaction.
- If no artifact evidence exists, mark `needs artifact` unless the user accepted the limitation.
- Use [review-rubric.md](references/review-rubric.md), [typography-craft-rubric.md](references/typography-craft-rubric.md), and [responsive-visual-gates.md](references/responsive-visual-gates.md). Use [data-ui-rubric.md](references/data-ui-rubric.md) for dashboards or metric-heavy UI.
- If the artifact feels directionally right but still generic, return to a micro-detail pass or enable the detail-translation gate before calling it ready.
- A non-ready decision needs one return action: `return to discovery`, `return to directions`, `return to approved spec`, `return to artifact`, `return to responsive pass`, `return to typography pass`, `return to stack pass`, or `return to handoff`.

## Hard Rules

- Establish design-system truth before inventing aesthetics.
- Visual evidence beats style adjectives.
- Never default to `Inter-only`, `system-only`, `hero + cards`, generic shadcn-like UI, or Flutter `Scaffold + AppBar + Card + ListView` without product reason.
- Do not replace generic SaaS with Claude-ish formula: serif headline, mono annotations, dossier panels, pills/status dots, and archival language without product reason.
- Do not imitate a specific designer/artist's signature look. Borrow mechanisms and reject mimicry.
- Do not keep only the surface style of a reference while losing its mechanism, token logic, or component/motion vocabulary.
- Do not present a direction menu without openable case links or source evidence the user can inspect.
- Do not justify product UI using only campaign-gallery references.
- Flutter/native work needs stack-native preview evidence; HTML proxy is fallback only and cannot be stack-native ready.
- A design is not complete while required `.noootwo/` deliverables are pending, unresolved, or missing artifact evidence.

## Reference Map

- State: `python scripts/noootwo_status.py <project>`
- Artifact eval: `python scripts/eval_noootwo_artifacts.py <project> --scenario all`
- Core workflow: [workflow-cost-model.md](references/workflow-cost-model.md), [adoption-playbook.md](references/adoption-playbook.md), [project-integration.md](references/project-integration.md)
- Discovery: [agentic-style-discovery.md](references/agentic-style-discovery.md), [source-registry.md](references/source-registry.md), [research-source-fallback.md](references/research-source-fallback.md), [reference-board.md](references/reference-board.md)
- System/spec/tokens: [system-extraction.md](references/system-extraction.md), [design-system-setup.md](references/design-system-setup.md), [structured-design-spec.md](references/structured-design-spec.md)
- Directions/taste: [direction-exploration.md](references/direction-exploration.md), [taste-fit-matrix.md](references/taste-fit-matrix.md), [mechanism-library.md](references/mechanism-library.md), [style-lineages.md](references/style-lineages.md), [frontend-aesthetic-principles.md](references/frontend-aesthetic-principles.md), [impeccable-style-details.md](references/impeccable-style-details.md), [anti-slop.md](references/anti-slop.md)
- Artifacts/stacks/review: [canvas-artifact-loop.md](references/canvas-artifact-loop.md), [target-stack-rules.md](references/target-stack-rules.md), [review-rubric.md](references/review-rubric.md), [review-gates.md](references/review-gates.md), [detail-translation-pass.md](references/detail-translation-pass.md), [handoff-bundle.md](references/handoff-bundle.md)
