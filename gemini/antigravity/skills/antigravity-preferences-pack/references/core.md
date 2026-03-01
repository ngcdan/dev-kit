# Core preferences (Đàn / OF1)

## Non-negotiables
- Keep it simple. Avoid over-engineering.
- Prefer class-based/OOP with clear responsibilities.
- Follow existing OF1 source patterns (folder structure, naming, layering). Do not introduce new architectural styles unless explicitly requested.
- Ask before large/wide refactors or changes that are time-consuming, hard to roll back, or touch many modules.

## Formatting
- Max line length: 120 characters.
- Indent: 2 spaces. Never use tabs.
- Break lines intentionally:
  - Keep information density high (do not hard-wrap aggressively).
  - Break when chains/conditions/params become hard to scan.
  - Break after ~3+ parameters or when a single parameter is very long.

## Comments & docs
- Keep comments short and purposeful.
- Prefer "why" over "what".

## Logging & error handling
- Default: do not add logging unless explicitly requested.
- If logging is necessary, keep it minimal and meaningful.
- Prefer durable audit mechanisms (events/topics/db rows) over log spam.

## Testing
- On request.
- If a change is risky, propose tests and ask for confirmation (do not auto-add by default).

## Delivery artifacts
- Maintain `DEVLOG.md` at repo root: append a short entry for each completed chunk of work.
- Prepare PR title + PR description text that can be copy-pasted.
