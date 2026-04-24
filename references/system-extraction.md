# System Extraction

Persistent design memory lives in `.noootwo/system.md`.

## Source Priority

1. Existing `.noootwo/system.md`
2. Code and tokens in the current repo
3. Current live product or internal screenshots
4. Brand guidelines or component libraries
5. User-provided references
6. Industry fallback patterns

## What To Extract

- Product purpose and audience
- Tone and writing posture
- Color system and token names if available
- Typography stack and hierarchy
- Spacing rhythm
- Border radius, shadows, density, and surface language
- Layout patterns
- Interaction and motion language
- Accessibility or platform constraints
- "Never do this" constraints

## Output Shape For `.noootwo/system.md`

- `Status`
- `Updated from`
- `Product`
- `Audience and jobs`
- `Tone and language`
- `Visual system`
- `Interaction language`
- `Platform constraints`
- `Known anti-patterns`
- `Refresh triggers`

## Rules

- Prefer exact values from code over inferred values from screenshots
- If the current file says `Status: pending extraction`, treat it as missing
- Keep project truth separate from task-specific experimentation
- Update the file only when new information is concrete enough to persist
