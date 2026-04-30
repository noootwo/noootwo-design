# Flutter Playbook

Use this when the target stack is Flutter.

## Artifact Path

- Prefer running the app, a focused route, a widget preview harness, or simulator/device screenshots.
- If execution is blocked, provide an HTML-native visual prototype plus Flutter-specific token, widget, and motion mapping.
- Record screenshot or blocker details in `.noootwo/review.md`.

## Token Mapping

- Map approved direction into `ThemeData`, `ColorScheme`, `TextTheme`, and `ThemeExtension` where useful.
- Define spacing, radius, surface, shadow/elevation, motion duration/easing, and component vocabulary.
- Keep text scale, safe areas, touch targets, and accessibility in scope.

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
- Check text scale, overflow, loading/empty/error states, reduced motion feasibility, and frame-risk effects.
