# React (TypeScript) rules (OF1)

## Follow existing codebase
- Mirror the existing OF1 React structure (folders, naming, component patterns).
- Do not introduce new global patterns (state management, routing patterns, UI frameworks) unless requested.

## Hooks usage
- Use hooks sparingly.
- Prefer the existing patterns in the codebase over inventing new custom hooks.

## TypeScript
- Prefer explicit, readable types at module boundaries (props, API responses, public helpers).
- Avoid over-engineered generics.

## Formatting
- 120 chars max.
- 2-space indent.
- Break lines intentionally for readability (do not aggressive wrap).

## Logging
- Do not add logging unless requested.
