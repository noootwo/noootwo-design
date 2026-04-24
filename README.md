# Noootwo Design

Type once, get a design worth shipping.

Noootwo Design is an open skill for turning a rough design request into a reusable design system, direction exploration, review loop, and implementation handoff. It is built for people who want something closer to the working behavior of Claude Design: design-system-first setup, explicit direction work, structured generator/evaluator loops, and implementation-ready handoff.

## What It Does

- Establishes or refreshes project design system memory before task work
- Expands a rough ask into a durable design brief
- Explores 2-3 design directions with explicit typography, density, and anti-pattern rules
- Forces an evaluator loop with `ready`, `refine`, or `pivot`
- Produces a handoff bundle for another agent or engineer only after review passes

## Install

From a published repository:

```bash
npx skills add noootwo/noootwo-design -g -y
```

From a local checkout:

```bash
npx skills add /path/to/noootwo-design -g -y
```

## Use

Examples:

- `Use $noootwo-design to establish the design system for this product, then design a new workbench home page.`
- `Use $noootwo-design to extract this project's design system.`
- `Use $noootwo-design to review this prototype and decide whether it is ready, should refine, or should pivot.`
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
