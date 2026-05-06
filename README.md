# Noootwo Design

Type once, get a design worth shipping.

Noootwo Design is an open skill for UI design, frontend design, app-screen design, visual redesign, design-system extraction, artifact review, screenshot critique, token mapping, and implementation handoff.

Current version: `v0.1.11`
Version source: repository tag plus the root `VERSION` file.

## What It Does

- Helps agents choose the right workflow mode: `adopt-project`, `quick`, `standard`, `deep`, `production`, `extract-system`, or `review`
- Establishes durable `.noootwo/` design system memory before substantial UI work
- Writes design systems and selected directions as structured design specs with color roles, type roles, layout rules, component vocabulary, motion thesis, do/don't guidance, and stack mapping
- Captures baseline context when adopted into an existing project midway through development
- Calibrates style targets without turning the process into a long questionnaire
- Explores 3 directions when useful, then pushes toward a real artifact or screenshot review
- Stops for user decisions when direction, style system, brand safety, novelty, artifact path, implementation cost, or review return path has multiple viable options
- Stops at a 3-direction menu for full redesign requests until the user selects a direction
- Uses stage roles and agentic style discovery for deep high-character design work
- Mines product flows, design systems, curated galleries, domestic fallback sources, and community signals, then transfers mechanisms instead of copying surfaces
- Requires typography and responsive evidence before calling non-trivial design work ready
- Keeps high-cost deep workflow limited to high-end, niche, brand-heavy, or major redesign tasks
- Maps approved design decisions into reusable design tokens and stack-specific implementation notes
- Produces handoff only after artifact evidence, readiness checks, or an explicit limitation is recorded

## Install

From a published repository:

```bash
npx skills add noootwo/noootwo-design -g -y
```

From a local checkout:

```bash
npx skills add /path/to/noootwo-design -g -y
```

## Project AGENTS.md Integration

For best model discovery, integrate a short Noootwo Design note into the target project's root `AGENTS.md`.

Bootstrap creates or merges that short section by default:

```bash
python scripts/bootstrap_noootwo_harness.py /path/to/project
```

If the project already has `AGENTS.md`, bootstrap preserves existing project instructions and only adds or replaces the short `## UI/Design Workflow` section from [assets/AGENTS.md](assets/AGENTS.md). Repeated runs are idempotent.

Use `--skip-agents` when you only want `.noootwo/` files:

```bash
python scripts/bootstrap_noootwo_harness.py /path/to/project --skip-agents
```

This is only a small project-level pointer. Keep the detailed workflow rules inside the `$noootwo-design` skill.

## Use

Examples:

- `Use $noootwo-design in deep mode to redesign this launch page with a more niche, high-end direction.`
- `Use $noootwo-design to redo all UI design in this Flutter app; show 3 directions before implementing.`
- `Use $noootwo-design in deep mode and run style discovery before drafting this dashboard.`
- `Use $noootwo-design in adopt-project mode to introduce Noootwo into this existing Flutter app before redesigning.`
- `Use $noootwo-design in standard mode to design a new workbench home page and show 3 directions before building.`
- `Use $noootwo-design in quick mode to polish spacing and type while staying close to the current UI.`
- `Use $noootwo-design in production mode to map this approved design into React tokens and implementation notes.`
- `Use $noootwo-design to review these screenshots and decide ready, refine, pivot, or needs artifact.`

## Harness

Noootwo Design stores durable context in `.noootwo/`.

Bootstrap the template into a project with:

```bash
python scripts/bootstrap_noootwo_harness.py
```

This creates:

- `.noootwo/system.md`
- `.noootwo/design-tokens.md`
- `.noootwo/adoption.md`
- `.noootwo/product-facts.md`
- `.noootwo/brief.md`
- `.noootwo/style-calibration.md`
- `.noootwo/style-discovery.md`
- `.noootwo/reference-board.md`
- `.noootwo/directions.md`
- `.noootwo/review.md`
- `.noootwo/handoff/implementation.md`
- `.noootwo/handoff/acceptance.md`
- `.noootwo/handoff/assets.md`

## Readiness Validation

Check that the required Noootwo deliverables are no longer pending before claiming a design is ready:

```bash
python scripts/validate_noootwo_readiness.py /path/to/project
```

The validator fails when `.noootwo/directions.md`, `.noootwo/review.md`, or `.noootwo/design-tokens.md` is missing, still `Status: pending`, contains unresolved `TBD` placeholders, or when `.noootwo/review.md` does not record a `ready` decision.

Use `--allow-non-ready` only when you want to verify that the workflow documents are complete but the design is still expected to be `refine`, `pivot`, or `needs artifact`.

Use `--deep-mode` when validating a deep-mode deliverable. It also requires `.noootwo/style-discovery.md` and `.noootwo/reference-board.md` to be complete.

For full redesign work, keep the same `--deep-mode` validator. If `.noootwo/directions.md` records `Full redesign trigger: yes`, it must also record `User selected direction` before the work can be ready.

For local web artifacts, run the lightweight visual gate:

```bash
python scripts/check_visual_gates.py http://localhost:3000 --screenshot-dir /tmp/noootwo-shots
```

The visual gate checks common viewport overflow and obvious clipped text. If browser automation is unavailable, record manual screenshot evidence and the limitation in `.noootwo/review.md`.

## Package Layout

```text
.
├── SKILL.md
├── agents/openai.yaml
├── assets/AGENTS.md
├── assets/noootwo-harness-template/
├── references/
└── scripts/
```

## Claude Design Alignment

This project does not copy private prompts. It implements public, repeatable mechanisms that make Claude Design-like workflows stronger:

- durable design-system memory before task work
- standard project `AGENTS.md` guidance for model discovery
- stage roles so research, art direction, implementation, and evaluation do not blur together
- agentic style discovery before deep high-character drafts
- source weighting and mechanism transfer instead of surface copying
- structured design specs instead of vague style adjectives or external template dependencies
- foreign-source accessibility checks with domestic fallback when needed
- full redesign checkpoint before implementation when the user asks to redo all UI
- typography, responsive, and spike-comparison gates for high-cost deep work
- explicit but compact style calibration
- code-native or stack-native artifacts before final judgment
- token mapping before production handoff
- independent review using screenshots, previews, readiness validation, or explicit artifact limitations

## License

MIT
