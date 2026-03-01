# Java (Spring) rules (OF1)

## Architecture
- Use class-based design with clear responsibilities.
- Follow existing OF1 patterns for:
  - package structure
  - config classes
  - DTOs/mappers
  - services/repositories
  - consumers/producers
- Prefer straightforward code over clever abstractions.

## Formatting
- Keep lines <= 120 chars.
- Use 2-space indent.
- When formatting fluent chains (builders/streams), prefer one-call-per-line when the chain becomes hard to scan.

## Error handling
- Handle errors "just enough":
  - validate inputs at boundaries
  - propagate/translate exceptions in the established OF1 way
- Avoid adding retries/backoff/etc. unless requested or the existing module already does so.

## Logging
- Do not add logs unless explicitly requested.
- If a boundary case must be visible, prefer a single `warn`/`error` with essential fields.

## Config changes
- When introducing properties, include a clean `application.properties`/`yaml` snippet in the PR description under **Configuration Required**.
- Keep config keys consistent with OF1 naming.
