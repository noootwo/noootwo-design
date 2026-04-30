# Noootwo Design

Type once, get a design worth shipping.

Noootwo Design is an open skill for turning a rough design request into reusable design system memory, visual-reference-backed direction exploration, reviewable artifacts, evaluator critique, and implementation handoff. It is built for people who want something closer to the public working behavior of Claude Design: design-system-first setup, code-native artifacts, opinionated art-direction exploration, screenshot/live review, and implementation-ready handoff.

Current version: `v0.1.5`
Version source: repository tag plus the root `VERSION` file.

## What It Does

- Establishes or refreshes project design system memory before task work
- Records source of truth, confidence, missing evidence, visual references, and target stack
- Expands a rough ask into a durable design brief with explicit aesthetic ambition, tone extreme, and memorable move
- Explores 3 design directions with explicit typography, density, motion, component language, background treatment, artifact strategy, stack translation, and anti-pattern rules
- Forces an evaluator loop with `ready`, `refine`, `pivot`, or `needs artifact`
- Pushes Web/React/Vue toward browser-visible artifacts and Flutter/native work toward stack-native previews or screenshotable handoff fallbacks
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

- `Use $noootwo-design to establish the design system for this product, gather visual references, then show me 3 strong directions before designing a new workbench home page. Each direction should define its artifact strategy, tone extreme, and one unforgettable thing.`
- `Use $noootwo-design to extract this project's design system.`
- `Use $noootwo-design to design this Flutter home screen. If the app can run, review simulator screenshots; otherwise create a visual prototype plus Flutter widget, token, and motion mapping.`
- `Use $noootwo-design to review this prototype with screenshots and decide whether it is ready, should refine, should pivot, or still needs artifact evidence.`
- `Use $noootwo-design to prepare an implementation handoff for this approved design, preserving component names, states, motion intent, and review evidence.`

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

## Claude Design Alignment

This project does not copy private prompts. It implements the public, repeatable mechanisms that make Claude Design-like workflows stronger:

- durable design-system memory before task work
- visual references before style invention
- code-native or stack-native artifacts before final judgment
- independent evaluator review using screenshots, previews, or explicit artifact limitations
- handoff that preserves design intent instead of becoming a moodboard

## License

MIT

## Notes

- Inspired by public research and public skill ecosystems around Claude Design, design harnesses, `huashu-design`, `web-design-engineer`, Flutter showcase work, Rive workflows, and stack-native frontend/app design practices
- The implementation is original to this package and optimized for cross-agent use
