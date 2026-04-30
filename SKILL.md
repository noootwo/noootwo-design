---
name: noootwo-design
description: Use when UI design, frontend design, visual redesign, design system extraction, artifact review, screenshot critique, React, Vue, Flutter, SwiftUI, Compose, native app UI, or implementation handoff work needs distinctive and non-generic product design.
license: MIT
---

# Noootwo Design

Noootwo Design helps agents turn UI requests into design-system-aware, stack-aware, reviewable interface work.

## Use This Skill For

- New UI pages, app screens, flows, dashboards, workbenches, landing pages, and prototypes
- Visual redesign, UI polish, layout improvement, typography, motion, or art direction
- React, Vue, web, Flutter, SwiftUI, Jetpack Compose, or native app visual work
- Extracting or refreshing `.noootwo/` design system memory
- Reviewing screenshots, prototypes, previews, or artifacts for `ready`, `refine`, `pivot`, or `needs artifact`
- Preparing design-to-implementation handoff

Do not use this for non-visual backend work, CLI tasks, pure logic bug fixes, or refactors with no UI impact.

## Project Context

Noootwo stores durable project context in `.noootwo/`. If missing, bootstrap from `assets/noootwo-harness-template/` or run `python scripts/bootstrap_noootwo_harness.py`.

Read existing files before re-deriving context:

- `.noootwo/system.md`
- `.noootwo/design-tokens.md`
- `.noootwo/product-facts.md`
- `.noootwo/brief.md`
- `.noootwo/style-calibration.md`
- `.noootwo/directions.md`
- `.noootwo/review.md`
- `.noootwo/handoff/implementation.md`
- `.noootwo/handoff/acceptance.md`
- `.noootwo/handoff/assets.md`

If a file is missing, stale, or `Status: pending`, refresh only what the selected mode needs.

## Mode Routing

Pick one mode first. Do not run the full deep flow by default.

- `quick`: Minor UI polish, small layout fixes, copy/spacing/type refinement, or "stay close to current style".
- `standard`: Default for new UI or ordinary redesign. Use light style calibration, 3 directions, artifact review.
- `deep`: High-end, niche, rare, experimental, brand-heavy, Claude Design-like, or major redesign work. Use visual references, casebook mechanisms, calibration, 3 directions, artifact loop.
- `production`: Approved design going into implementation. Focus on design tokens, target stack mapping, screenshots/previews, and handoff.
- `extract-system`: Build or refresh `.noootwo/system.md` and `.noootwo/design-tokens.md`.
- `review`: Critique an existing artifact and decide `ready`, `refine`, `pivot`, or `needs artifact`.

If a task spans modes, use this order: `extract-system -> quick/standard/deep -> review -> production`.

## Mode Workflows

### Quick

- Read current UI, `.noootwo/system.md`, and `.noootwo/design-tokens.md` when available.
- Skip full style calibration and 3 directions unless the user asks.
- Make the smallest visual improvement that preserves the existing system.
- Use artifact evidence when available; otherwise state the limitation.

### Standard

- Refresh system facts if needed.
- Write or update a short brief.
- Run lightweight style calibration from [style-calibration.md](references/style-calibration.md).
- Present 3 materially different directions using [direction-exploration.md](references/direction-exploration.md).
- Build the fastest reviewable artifact for the target stack.
- Review with [review-rubric.md](references/review-rubric.md).

### Deep

- Use [claude-design-principles.md](references/claude-design-principles.md), [verified-ui-casebook.md](references/verified-ui-casebook.md), [style-lineages.md](references/style-lineages.md), and [anti-slop.md](references/anti-slop.md).
- Gather visual references or record the gap explicitly.
- Run style calibration before directions.
- Require 3 directions with different type, density, composition, component language, motion, and artifact strategy.
- Do not polish a generic direction. Pivot.

### Production

- Convert the chosen direction into `.noootwo/design-tokens.md`.
- Use the relevant stack playbook:
  - Web, React, Vue, Nuxt: [web-react-vue.md](references/stacks/web-react-vue.md)
  - Flutter: [flutter.md](references/stacks/flutter.md)
  - SwiftUI, Jetpack Compose, native: [native.md](references/stacks/native.md)
- Produce implementation notes, token mapping, artifact verification, states, risks, and acceptance criteria.

### Review

- Prefer the lived artifact: screenshot, running page, simulator preview, target-stack prototype, or recorded interaction.
- If no artifact evidence exists, mark `needs artifact` unless the user explicitly accepts the limitation.
- Judge design quality and originality separately from cleanliness.

## Hard Rules

- Establish design system truth before inventing aesthetics.
- Visual evidence beats style adjectives.
- Use standard `AGENTS.md` project guidance when present; if it says to use `$noootwo-design` for UI work, follow it.
- Do not ask users to fill long style questionnaires. Recommend a calibration and proceed if they do not choose.
- Do not default to `Inter-only`, `system-only`, `hero + cards`, generic shadcn-like UI, or Flutter `Scaffold + AppBar + Card + ListView` without a product reason.
- Every non-trivial design must declare artifact strategy and stack translation before implementation.
- A design is not `ready` without artifact evidence or an explicit artifact limitation.
- Handoff must preserve design intent, tokens, component naming, states, motion decisions, artifact verification, and implementation risks.

## Reference Map

- Project integration: [project-integration.md](references/project-integration.md)
- Facts and assets: [fact-first.md](references/fact-first.md), [asset-protocol.md](references/asset-protocol.md)
- System and tokens: [design-system-setup.md](references/design-system-setup.md), [system-extraction.md](references/system-extraction.md)
- Brief and style: [brief-expansion.md](references/brief-expansion.md), [style-calibration.md](references/style-calibration.md)
- Directions and aesthetics: [direction-exploration.md](references/direction-exploration.md), [style-lineages.md](references/style-lineages.md), [frontend-aesthetic-principles.md](references/frontend-aesthetic-principles.md), [anti-slop.md](references/anti-slop.md)
- Claude Design alignment: [claude-design-principles.md](references/claude-design-principles.md), [verified-ui-casebook.md](references/verified-ui-casebook.md)
- Artifact and stacks: [canvas-artifact-loop.md](references/canvas-artifact-loop.md), [target-stack-rules.md](references/target-stack-rules.md), [web-react-vue.md](references/stacks/web-react-vue.md), [flutter.md](references/stacks/flutter.md), [native.md](references/stacks/native.md)
- Review and handoff: [review-rubric.md](references/review-rubric.md), [handoff-bundle.md](references/handoff-bundle.md)
