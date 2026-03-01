---
name: pr-drafter
description: Draft Pull Request title and description for OF1 work in Đàn’s style. Use when the user asks to create/draft PR text, prepare PR title/description, summarize changes for a PR, or generate copy-pastable PR notes including Configuration Required.
---

# PR Drafter (Đàn / OF1)

Goal: produce PR text that Đàn can copy-paste with minimal edits.

## Instructions
1. Ask for missing essentials if not provided: feature name/scope + list of changes + any config changes.
2. Generate:
   - PR Title (conventional style)
   - PR Description using `references/pr-template.md`
3. Organize Changes Made into numbered sections (1, 2, 3...) grouped by module/area.
4. Include **Configuration Required** with clean property snippets when needed; otherwise put `None`.

## Constraints
- No fluff.
- Keep snippets minimal.
- Do not add logging unless user explicitly requests it.
