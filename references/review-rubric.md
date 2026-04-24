# Review Rubric

Review is mandatory before delivery.

## Evaluator Stance

- Review as an evaluator, not as the generator defending its own draft
- Prefer the lived artifact: prototype, running page, screenshot set, or interactive build
- Judge point of view separately from cleanliness

## Scoring Model

Score the design on 100 total points:

- `design_quality`: 35
- `originality`: 30
- `craft`: 20
- `functionality`: 15

## Thresholds

- `85-100`: ready to hand off only if generic-risk flags are 0-1
- `70-84`: refine before handoff
- `<70`: pivot unless the user explicitly wants to preserve the direction

## Review Output

Write the review to `.noootwo/review.md` with:

- `Status`
- `Artifact reviewed`
- `Loop`
- `Scores`
- `Distinctiveness audit`
- `Generic SaaS flags`
- `What works`
- `What breaks`
- `Decision: ready, refine, or pivot`
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

## Decision Rules

- `ready`: the direction is strong, the craft is credible, and the output avoids generic fallbacks
- `refine`: the direction is right but execution, hierarchy, proof, or specificity is still weak
- `pivot`: the underlying direction is too generic, mismatched, derivative, or structurally wrong

## Loop Rules

- Maximum 2 full review loops before escalating the trade-off to the user
- Review should separate "cleaner than before" from "distinctive enough to keep"
- Do not let neat spacing or polished UI chrome compensate for weak originality
