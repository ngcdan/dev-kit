# Global rules (Đàn)

These rules are always-on.

## Default coding preferences (OF1)
When generating, refactoring, or reviewing code, ALWAYS follow the existing OF1 codebase patterns.

Also apply the preferences from the global skill:
- `antigravity-preferences-pack`
  - Java/Spring + React/TypeScript
  - 2-space indent, no tabs
  - <= 120 chars per line
  - intentional line breaks (avoid aggressive wrapping)
  - short comments (prefer "why")
  - no logging unless explicitly requested
  - tests on request
  - ask before large/wide refactors or hard-to-rollback changes

## Implementation Plan language
- When writing an **Implementation Plan**, write it in **Vietnamese**, but keep technical terminology in **English** (do not translate established terms).

## Delivery artifacts
- If a chunk of work is completed, update/create `DEVLOG.md` at repo root using the `devlog-writer` skill format.
- If the user asks for PR notes, draft PR title + description using the `pr-drafter` template.
