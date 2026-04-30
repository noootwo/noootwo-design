# Handoff Bundle

The handoff bundle translates design intent into implementation-ready instructions.

## Required Files

- `.noootwo/handoff/implementation.md`
- `.noootwo/handoff/acceptance.md`
- `.noootwo/handoff/assets.md`

## `implementation.md`

Must include:

- design intent
- design decisions that must survive implementation
- chosen direction
- layout map
- component responsibilities
- interaction and state notes
- motion guidance
- stack-specific implementation notes
- artifact reviewed and review evidence
- token mapping from `.noootwo/design-tokens.md`
- artifact verification requirements
- edge states: loading, empty, error, focus, disabled, hover or pressed
- implementation risks
- implementation priority order

## `acceptance.md`

Must include:

- what "done" means visually
- state and interaction checks
- responsive or platform checks
- accessibility or clarity checks
- screenshot or preview checks
- regression risks to watch

## `assets.md`

Must include:

- required brand assets
- approved fallbacks
- source links or origin notes
- unresolved asset gaps

## Rules

- Write for another agent or engineer who was not present in the design conversation
- Prefer concrete rules over taste-only commentary
- If something is still uncertain, mark it as a decision point instead of hiding it
- Preserve component names, motion intent, state behavior, and implementation risks from the review
- Do not let handoff become a style moodboard; it must tell the implementer what to build and what not to lose
