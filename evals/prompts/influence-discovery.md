# Eval Prompt: Influence Discovery

Use `$noootwo-design` in deep mode. The user says: "现在的 UI 和交互我不满意，想完全重构。请探索一下适合这个产品调性和用户需求的设计师、艺术家、工作室或产品风格，不要局限当前设计，找到真正好的风格体系。"

Expected behavior:

- Do not implement immediately.
- Run source discovery and optional influence discovery.
- Present 3 influence territories with `source / why relevant / borrowable mechanisms / do not copy / translation / risk`.
- Recommend a mechanism mix, such as base atmosphere + information grammar + interaction efficiency.
- Ask the user to choose a starting point before directions, spikes, or implementation.

Failure signals:

- Outputs "in the style of X" as the direction.
- Copies signature artwork, exact compositions, logo/brand skins, or a living artist's recognizable surface.
- Gives only mood adjectives without source evidence or mechanism translation.
- Proceeds directly to UI implementation.
