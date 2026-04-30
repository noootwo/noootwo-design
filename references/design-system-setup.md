# Design System Setup

Set up `.noootwo/system.md` before task-specific design work.

## Purpose

The design system memory is the durable source of truth for brand behavior, type, composition, and taste boundaries. Without it, drafts tend to be functional but generic.

The memory must not become a second source of truth. It records what is confirmed, what is inferred, and what is missing.

## Source Order

1. Existing `.noootwo/system.md`
2. Code, tokens, component names, and theme files in the current repo
3. Official product screenshots or internal screenshots
4. Brand guidelines, logos, press kits, or product pages
5. Design files, decks, annotated frames, or existing prototypes
6. User-provided references
7. Fallback lineages from [style-lineages.md](style-lineages.md) when brand evidence is incomplete

## Required Output

Update `.noootwo/system.md` with:

- `Status`
- `Updated From`
- `Source of truth`
- `Extracted from`
- `Confidence`
- `Missing evidence`
- `Published design system rules`
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
- `Target stack`
- `Rendering surface`
- `Stack-native component vocabulary`
- `Interaction grammar`
- `Motion primitives`
- `Visual reference library`
- `Refresh triggers`

## Confirmation Rules

- Prefer exact values from code over inferred values from screenshots
- Mark every inferred font, spacing rule, or motion rule as inferred
- If the brand type system is unknown, record the fallback lineage and why it was chosen
- Keep task-specific experiments out of the design system memory unless they are promoted into durable truth
- Record the generic fallbacks that repeatedly weaken outputs for this product
- If screenshots or code disagree with a generated system summary, prefer the actual artifact and record the conflict
