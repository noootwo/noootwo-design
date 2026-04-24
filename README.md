# Noootwo Design

Type once, get a design worth shipping.

Noootwo Design is an open skill for turning a rough design request into a reusable design system, direction exploration, review loop, and implementation handoff. It is built for people who want something closer to the working behavior of Claude Design: persistent design memory, explicit direction work, structured review, and implementation-ready handoff.

## What It Does

- Expands a rough ask into a durable design brief
- Extracts and refreshes project design system memory
- Explores 3 design directions before committing
- Forces an independent review loop with `refine` vs `pivot`
- Produces a handoff bundle for another agent or engineer

## Install

From a published repository:

```bash
npx skills add <owner>/noootwo-design -g -y
```

From a local checkout:

```bash
npx skills add ./open-source/noootwo-design -g -y
```

## Use

Examples:

- `Use $noootwo-design to design a new workbench home page for this product.`
- `Use $noootwo-design to extract this project's design system.`
- `Use $noootwo-design to review this prototype and decide whether to refine or pivot.`
- `Use $noootwo-design to prepare an implementation handoff for this approved design.`

## Harness

Noootwo Design stores durable context in `.noootwo/`.

Bootstrap the template into a project with:

```bash
python scripts/bootstrap_noootwo_harness.py
```

This creates:

- `.noootwo/system.md`
- `.noootwo/product-facts.md`
- `.noootwo/brief.md`
- `.noootwo/directions.md`
- `.noootwo/review.md`
- `.noootwo/handoff/implementation.md`
- `.noootwo/handoff/acceptance.md`
- `.noootwo/handoff/assets.md`

## Package Layout

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
├── scripts/bootstrap_noootwo_harness.py
└── assets/noootwo-harness-template/
```

## License

MIT

## Notes

- Inspired by public research and public skill ecosystems around Claude Design, design harnesses, `huashu-design`, and `web-design-engineer`
- The implementation is original to this package and optimized for cross-agent use
