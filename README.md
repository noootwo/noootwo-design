# Noootwo Design

Type once, get a design worth shipping.

Noootwo Design is an open skill for UI design, frontend design, app-screen design, visual redesign, design-system extraction, artifact review, screenshot critique, token mapping, and implementation handoff.

Current version: `v0.1.7`
Version source: repository tag plus the root `VERSION` file.

## What It Does

- Helps agents choose the right workflow mode: `quick`, `standard`, `deep`, `production`, `extract-system`, or `review`
- Establishes durable `.noootwo/` design system memory before substantial UI work
- Calibrates style targets without turning the process into a long questionnaire
- Explores 3 directions when useful, then pushes toward a real artifact or screenshot review
- Maps approved design decisions into reusable design tokens and stack-specific implementation notes
- Produces handoff only after artifact evidence or an explicit limitation is recorded

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

If the project has no `AGENTS.md`, create one from the provided template:

```bash
cp assets/AGENTS.md /path/to/project/AGENTS.md
```

If the project already has `AGENTS.md`, merge the short `UI/Design Workflow` section from [assets/AGENTS.md](assets/AGENTS.md) into the existing file. Preserve existing project instructions, and add or update only the UI/design-related guidance.

This is only a small project-level pointer. Keep the detailed workflow rules inside the `$noootwo-design` skill.

## Use

Examples:

- `Use $noootwo-design in deep mode to redesign this launch page with a more niche, high-end direction.`
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
- `.noootwo/product-facts.md`
- `.noootwo/brief.md`
- `.noootwo/style-calibration.md`
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
├── assets/AGENTS.md
├── assets/noootwo-harness-template/
├── references/
└── scripts/bootstrap_noootwo_harness.py
```

## Claude Design Alignment

This project does not copy private prompts. It implements public, repeatable mechanisms that make Claude Design-like workflows stronger:

- durable design-system memory before task work
- standard project `AGENTS.md` guidance for model discovery
- visual references before style invention
- explicit but compact style calibration
- code-native or stack-native artifacts before final judgment
- token mapping before production handoff
- independent review using screenshots, previews, or explicit artifact limitations

## License

MIT
