# System Extraction

Persistent design memory lives in `.noootwo/system.md`.

Read [design-system-setup.md](design-system-setup.md) first when the file is missing, stale, or still pending extraction.

## Source Priority

1. Existing `.noootwo/system.md`
2. Code and tokens in the current repo
3. Current live product or internal screenshots
4. Brand guidelines or component libraries
5. User-provided references
6. Industry fallback patterns

## What To Extract

- Brand primitives: colors, marks, imagery, and visual materials
- Product purpose and audience
- Tone and writing posture
- Type system: confirmed fonts, fallback logic, hierarchy, and contrast strategy
- Component patterns: recurring shells, cards, rails, panels, forms, navigation, and evidence patterns
- Layout density: spacing rhythm, information density, and preferred structural moves
- Motion language
- Platform constraints
- Known generic fallbacks that would degrade the work
- Forbidden combinations and "never do this" constraints

## Output Shape For `.noootwo/system.md`

- `Status`
- `Updated From`
- `Brand primitives`
- `Product`
- `Audience and jobs`
- `Tone and language`
- `Type system`
- `Component patterns`
- `Layout density`
- `Motion language`
- `Known generic fallbacks`
- `Forbidden combinations`
- `Platform constraints`
- `Refresh triggers`

## Rules

- Prefer exact values from code over inferred values from screenshots
- If the current file says `Status: pending extraction`, treat it as missing
- Keep project truth separate from task-specific experimentation
- Mark inferred values as inferred
- Update the file only when new information is concrete enough to persist
