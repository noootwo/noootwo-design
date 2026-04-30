# Review Rubric

Review is mandatory before delivery.

## Evaluator Stance

- Review as an evaluator, not as the generator defending its own draft
- Prefer the lived artifact: prototype, running page, screenshot set, or interactive build
- Judge point of view separately from cleanliness
- If no artifact evidence exists, the review must say `needs artifact` unless the user explicitly accepted a handoff-only result
- Check for Claude-like convergence separately from generic SaaS failure

## Scoring Model

Score the design on 100 total points:

- `design_quality`: 35
- `originality`: 30
- `craft`: 15
- `functionality`: 10
- `artifact_evidence`: 5
- `stack_native_craft`: 5

## Thresholds

- `85-100`: ready to hand off only if generic-risk flags are 0-1 and artifact evidence is present or explicitly waived
- `70-84`: refine before handoff
- `<70`: pivot unless the user explicitly wants to preserve the direction

## Review Output

Write the review to `.noootwo/review.md` with:

- `Status`
- `Artifact evidence`
- `Loop`
- `Scores`
- `Style calibration fit`
- `Generic SaaS flags`
- `Claude-like convergence flags`
- `Framework smell flags`
- `Designer-grade failure flags`
- `Role-based critique`
- `What is the memorable move`
- `Code/design mismatch risks`
- `Multi-viewport evidence`
- `Responsive visual gate`
- `Typography craft`
- `Spike comparison` for deep mode
- `Data UI evidence` when relevant
- `Readiness gate result`
- `Decision: ready, refine, pivot, or needs artifact`
- `Return action`
- `Highest-leverage fixes`
- `Next action`

## Generic-Risk Flags

Flag the draft when it looks like:

- `Inter-only` or `system-only` typography without brand reason
- centered template hero with generic supporting cards
- card wall UI with interchangeable radius and shadows
- pure black plus glow plus pills as the main aesthetic move
- gradient-led styling with weak composition underneath
- a generic AI landing page, generic SaaS page, or obvious shadcn derivative

If 2 or more flags are present, the design cannot be marked `ready`.
If 3 or more flags are present, or originality is structurally weak, default to `pivot`.

## Designer-Grade Taste Checks

Use [taste-fit-matrix.md](taste-fit-matrix.md) for deep mode and style-sensitive work.

- Distinctive but not weird for its own sake
- Niche but not cosplay
- Practical within the user's task
- Minimal but not empty
- Efficient but not generic
- Premium through proportion, type, spacing, material, and restraint
- Fashionable through credible current signals, not stale trend skins

Flag these failures:

- `AI gradient SaaS`
- `styled but crude`
- `unique but impractical`
- `minimal but empty`
- `fashionable but unusable`
- `efficient but generic`
- `premium cosplay`

Any `styled but crude`, `unique but impractical`, or `fashionable but unusable` flag prevents `ready`.

## Typography Craft Checks

Use [typography-craft-rubric.md](typography-craft-rubric.md).

Any of these prevents `ready`:

- Display headline is too heavy, clipped, or unstable on mobile.
- Body text is below 16px on web without a valid density reason.
- Font sizes, weights, or line heights are arbitrary instead of tokenized.
- Monospace is used as a lazy aesthetic shortcut.
- Display/body contrast is absent or muddy.
- Data-heavy UI does not use tabular numbers where alignment matters.

If type is promising but flawed, use `Return action: return to typography pass`.

## Style Calibration Fit

- If the draft ignores the selected novelty, density, typography, motion, or brand-safety dials, it cannot be `ready`.
- If the direction is strong but one dial is under-expressed, default to `refine`.
- If the artifact contradicts the calibration thesis, return to directions instead of polishing.
- If the user changed taste direction during review, update `.noootwo/style-calibration.md` before generating a new direction.

## Claude-Like Convergence Flags

Flag polished outputs that still feel templated:

- too many nested rounded containers without structural purpose
- serif headline plus generic sans body plus pills/status dots with no product-specific reason
- Claude-ish serif plus mono annotations plus dossier panels plus status dots as a replacement template
- clean panels replacing a real layout idea
- first screen that could describe any AI product after swapping the logo
- handoff that loses the specific component, state, or motion decisions from the design

## Framework Smell Flags

Flag stack-specific defaults that weaken the design:

- Web/React/Vue: unmodified UI-kit components, shadcn-like card walls, Lucide icon grids, generic fade-up motion
- Flutter: default `Scaffold + AppBar + Card + ListView`, Material seed colors without art direction, no sliver or native motion strategy in a high-character app
- SwiftUI: default list/form styling when the brief asks for a distinctive product surface
- Jetpack Compose: default Material surfaces without token reinterpretation, no native transition or state feedback plan
- Native apps: web landing-page structure forced into an app shell

## Data UI Checks

For dashboards, analytics, ops, monitoring, finance, admin panels, and metric-heavy workbenches, use [data-ui-rubric.md](data-ui-rubric.md).

- If charts or metrics have no axes, units, state, time window, action path, or priority logic, the design cannot be `ready`.
- If a workbench looks impressive but the data is decorative, default to `refine`.
- If the surface lacks a credible operational action path, default to `pivot`.

## Responsive Visual Gate

Use [responsive-visual-gates.md](responsive-visual-gates.md).

Before `ready`, record evidence for phone, narrow/tablet, desktop, and text scale or zoom.

Any of these prevents `ready`:

- `document.documentElement.scrollWidth > window.innerWidth`
- critical headline, nav, primary action, or data clipped
- mobile title wraps into an unreadable block
- primary action or recovery path unreachable
- native preview ignores safe area or text scale

If the direction is good but viewport adaptation fails, use `Return action: return to responsive pass`.

## Deep Mode Evidence Gate

Deep mode cannot enter `ready` unless:

- `.noootwo/style-discovery.md` records source accessibility, URL/artifact evidence, source levels, rejected surfaces, and fit scores.
- `.noootwo/reference-board.md` records source mechanisms.
- `.noootwo/review.md` records spike comparison.

If 2-3 spikes were not possible, record the limitation and do not claim full exploration confidence.

## Readiness Gate

Before marking any non-trivial design `ready`, check:

- `.noootwo/directions.md` exists and is not `Status: pending`
- `.noootwo/review.md` exists and is not `Status: pending`
- `.noootwo/design-tokens.md` exists and is not `Status: pending`
- Required files do not contain unresolved `TBD` placeholders
- `.noootwo/review.md` records artifact evidence and a decision
- `.noootwo/review.md` records typography craft evidence
- `.noootwo/review.md` records responsive visual evidence

If this fails, the decision is `needs artifact` or `refine`, not `ready`.

## Decision Rules

- `ready`: the direction is strong, the craft is credible, and the output avoids generic fallbacks
- `refine`: the direction is right but execution, hierarchy, proof, or specificity is still weak
- `pivot`: the underlying direction is too generic, mismatched, derivative, or structurally wrong
- `needs artifact`: the design may be promising but cannot be judged ready because no artifact, screenshot, preview, or acceptable visual substitute was reviewed

## Memorable Move Check

- If the reviewer cannot name the one unforgettable move, the design cannot be `ready`
- If the memorable move exists in concept but is too weak in execution, default to `refine`

## Aesthetic Coherence Check

- Typography, color, layout, motion, components, and background/detail treatment should point at the same mood
- If those systems pull in different directions, default to `refine`

## Forced Redo Rules

- If the draft lacks explicit type contrast, density stance, component vocabulary, motion thesis, or background/detail thesis, return to directions before refining
- If the draft lacks a clear relationship to `.noootwo/style-calibration.md`, return to directions before refining
- If the draft lacks artifact strategy, stack translation, or visual proof, return to directions or stack translation before polishing
- If production work lacks token mapping, return to `.noootwo/design-tokens.md` before handoff
- If readiness gate fails because required `.noootwo/` files are pending or unresolved, return to the missing file before handoff
- If typography craft fails, return to typography pass before visual polish
- If responsive checks fail, return to responsive pass before handoff
- If deep source evidence or spike comparison is missing, return to discovery or artifact before drafting
- If the direction is right but execution is weak, return to draft with concrete fixes
- If the direction itself is generic, return to directions instead of polishing the draft
- "Clean but ordinary" is a failure mode, not a near-ready state
- If safe SaaS layout, generic typography, and low-risk motion appear together, default to `pivot`
- If framework smell flags hide the chosen art direction, return to draft or stack translation

## Loop Rules

- Maximum 2 full review loops before escalating the trade-off to the user
- Review should separate "cleaner than before" from "distinctive enough to keep"
- Do not let neat spacing or polished UI chrome compensate for weak originality
- Do not spend polish loops on a direction that needs a structural pivot

## Return Actions

Use exactly one primary return action for non-ready work:

- `return to discovery`
- `return to directions`
- `return to artifact`
- `return to responsive pass`
- `return to typography pass`
- `return to stack pass`
- `return to handoff`
