# Target Stack Rules

Noootwo Design supports three primary implementation paths.

## 1. HTML-Native Prototype

Use when:

- the goal is exploration, direction approval, or handoff
- the product surface is new
- the implementation stack is not settled yet

Rules:

- optimize for fidelity and clarity
- make interaction flows believable
- use this path to validate direction, not to masquerade as production code
- critique the draft before polishing it

## 2. Web Or React Implementation

Use when:

- the design is headed directly into an existing web codebase
- the repo already has a component system worth following
- the task is an evolution of an existing web surface

Rules:

- extract tokens and vocabulary first
- match the established design language before adding novelty
- express the chosen direction through composition, rhythm, typography, and motion, not through a total style reset
- do not jump to handoff until review says the direction is ready

## 3. Flutter Or Existing Application Handoff

Use when:

- the target stack is Flutter or another non-web application stack
- the design work is meant for an implementation agent rather than immediate HTML production

Rules:

- prefer structured handoff over forcing a web-shaped mockup into the codebase
- capture component behavior, spacing, hierarchy, and motion in platform-neutral terms
- include implementation priorities and acceptance criteria specific enough for the app team to execute
- handoff is a post-review artifact, not the first draft

## Decision Rule

Default to HTML-native for new or ambiguous work.
Default to direct in-stack work for local refinements inside a mature codebase.
Default to handoff when the target stack is not the same as the fastest prototyping medium.
