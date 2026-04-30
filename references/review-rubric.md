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
- `Artifact reviewed`
- `Artifact evidence`
- `Screenshots reviewed`
- `Loop`
- `Scores`
- `Distinctiveness audit`
- `Generic SaaS flags`
- `Claude-like convergence flags`
- `Framework smell flags`
- `What feels generic`
- `What is the memorable move`
- `Aesthetic coherence`
- `Code/design mismatch risks`
- `Token/time budget note`
- `What works`
- `What breaks`
- `Decision: ready, refine, pivot, or needs artifact`
- `Forced redo trigger`
- `Next action: return to directions or draft`
- `Highest-leverage fixes`
- `Open risks`

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

## Claude-Like Convergence Flags

Flag polished outputs that still feel templated:

- too many nested rounded containers without structural purpose
- serif headline plus generic sans body plus pills/status dots with no product-specific reason
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
- If the draft lacks artifact strategy, stack translation, or visual proof, return to directions or stack translation before polishing
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
