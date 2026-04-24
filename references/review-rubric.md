# Review Rubric

Review is mandatory before delivery.

## Scoring Model

Score the design on 100 total points:

- `design_quality`: 35
- `originality`: 30
- `craft`: 20
- `functionality`: 15

## Thresholds

- `85-100`: ready to hand off
- `70-84`: refine before handoff
- `<70`: pivot unless the user explicitly wants to preserve the direction

## Review Output

Write the review to `.noootwo/review.md` with:

- `Status`
- `Artifact reviewed`
- `Loop`
- `Scores`
- `What works`
- `What breaks`
- `Decision: refine or pivot`
- `Highest-leverage fixes`
- `Open risks`

## Loop Rules

- Maximum 2 full review loops before escalating the trade-off to the user
- `refine` means the direction is fundamentally right and needs execution improvement
- `pivot` means the underlying direction is wrong or too weak
- Review the lived artifact when possible: prototype, running page, screenshot set, or interactive build

## Penalties

Subtract confidence for:

- AI-slop patterns
- weak hierarchy
- mismatched tone
- missing asset realism
- handoff notes that are too vague to implement
