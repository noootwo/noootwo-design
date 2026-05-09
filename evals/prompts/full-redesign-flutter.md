# Eval Prompt: Full Flutter Redesign

Use `$noootwo-design` for an existing Flutter app. The user says: "所有 UI 设计重新来，之前的视觉不要了，我要高级小众、实用、简约、高效。"

Expected behavior:

- Route to `adopt-project -> deep` if `.noootwo/` is missing or stale.
- Trigger the full redesign checkpoint.
- Run style discovery and produce 3 user-facing directions.
- Ask the user to choose before editing Flutter UI files.
- Record the decision requirement in `.noootwo/directions.md`.
- Prefer real Flutter route/widget preview, simulator/device screenshot, or golden-style screenshot for later review.

Failure signals:

- Directly edits Flutter UI before the user chooses a direction.
- Uses HTML proxy as stack-native proof.
- Produces blue/purple gradient AI UI, poster-like mobile screen, oversized CJK display, or thick card stack.
