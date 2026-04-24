# Design System Setup

Set up `.noootwo/system.md` before task-specific design work.

## Purpose

The design system memory is the durable source of truth for brand behavior, type, composition, and taste boundaries. Without it, drafts tend to be functional but generic.

## Source Order

1. Existing `.noootwo/system.md`
2. Code, tokens, component names, and theme files in the current repo
3. Official product screenshots or internal screenshots
4. Brand guidelines, logos, press kits, or product pages
5. User-provided references
6. Fallback lineages from [style-lineages.md](style-lineages.md) when brand evidence is incomplete

## Required Output

Update `.noootwo/system.md` with:

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

## Confirmation Rules

- Prefer exact values from code over inferred values from screenshots
- Mark every inferred font, spacing rule, or motion rule as inferred
- If the brand type system is unknown, record the fallback lineage and why it was chosen
- Keep task-specific experiments out of the design system memory unless they are promoted into durable truth
- Record the generic fallbacks that repeatedly weaken outputs for this product
