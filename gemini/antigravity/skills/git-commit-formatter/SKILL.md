---
name: git-commit-formatter
description: Formats git commit messages using Conventional Commits. Use this when the user asks to write a commit message, commit changes, or suggests a vague message like wip/fix/updates.
---

# Git Commit Formatter (Conventional Commits)

## Goal
Produce a clean **Conventional Commits** message that matches the actual change.

## Required format
`<type>[optional scope]: <description>`

Optional additions:
- Body (why/what) after a blank line
- Footer after a blank line (e.g. `BREAKING CHANGE:` or issue refs)

## Types (use exactly one)
- `feat`: new feature
- `fix`: bug fix
- `docs`: documentation only
- `style`: formatting (no logic change)
- `refactor`: code change that neither fixes a bug nor adds a feature
- `perf`: performance improvement
- `test`: add/fix tests
- `build`: build system or deps
- `ci`: CI config/scripts
- `chore`: maintenance tasks
- `revert`: revert a previous commit

## Description rules
- Present tense, imperative mood ("add", "fix", "remove")
- Lowercase start (unless proper noun)
- No trailing period
- Keep subject <= 72 chars when possible

## Scope rules
- Scope is optional; include it when it increases clarity (module/package/app)
- Use kebab-case for scope (e.g. `mobile-auth`, `crm-api`)

## If information is missing
Ask **one** question to choose the correct type/scope, for example:
- "Is this change a bug fix or a refactor? Which module should be the scope?"

## Examples
- `feat(crm-api): add shipment status filter`
- `fix(mobile-auth): handle token refresh race`
- `docs: update release checklist`
- `refactor: simplify pricing calculation flow`
- `build: bump flutter to 3.22`

## Output behavior
When the user provides a diff/summary, return **3 options**:
1) minimal
2) with scope
3) with body (if needed)

If user says "commit it", first propose the message; do **not** run git commands unless explicitly asked.
