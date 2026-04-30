# Flutter Playbook

Use this when the target stack is Flutter.

## Artifact Path

- Prefer running the app, a focused route, a widget preview harness, golden-style screenshot, or simulator/device screenshots.
- A real Flutter artifact should come before HTML proxy when Flutter tooling is available.
- If execution is blocked, provide an HTML-native visual prototype plus Flutter-specific token, widget, and motion mapping, and mark it as fallback.
- Record screenshot or blocker details in `.noootwo/review.md`.
- Do not mark Flutter work stack-native ready when the only artifact is an HTML phone-shell proxy.
- Deep Flutter work needs at least one real route/widget preview, simulator/device screenshot, or golden-style screenshot before `stack_native_craft` can be treated as strong.

## Token Mapping

- Map approved direction into `ThemeData`, `ColorScheme`, `TextTheme`, and `ThemeExtension` where useful.
- Define spacing, radius, surface, shadow/elevation, motion duration/easing, and component vocabulary.
- Keep text scale, safe areas, touch targets, and accessibility in scope.
- Record font fallback, display/body contrast, text scale behavior, and tabular numeric behavior when relevant.

## Implementation Moves

- Use `CustomScrollView`, slivers, and composed layout primitives for distinctive structure.
- Use `Hero`, implicit animations, explicit animations, gestures, or page transitions when motion carries meaning.
- Use `CustomPainter`, shaders, Rive, or Lottie only when they support the chosen art direction.
- Prefer reusable widgets and theme extensions over one-off styling.

## Smell Checks

- Default `Scaffold + AppBar + Card + ListView` for a high-character screen
- Material seed color without art direction
- Generic large-radius cards and shadows
- Motion as decorative garnish
- Ignoring text scale, safe area, performance, or accessibility

## Verification

- Review at least one phone viewport when possible.
- Check text scale, safe area, touch targets, overflow, loading/empty/error states, reduced motion feasibility, and frame-risk effects.
- Record whether `ThemeData`, `TextTheme`, `ThemeExtension`, slivers, `CustomPainter`, Rive, or other stack-native moves were actually used.
- If only an HTML proxy was reviewed, the decision is `needs artifact`, `refine`, or fallback-ready only by explicit user acceptance.
