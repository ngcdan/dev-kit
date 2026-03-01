---
name: devlog-writer
description: Maintain DEVLOG.md at repo root using Đàn’s preferred format. Use when the user asks to update/write DEVLOG, summarize work done, record changes for later review, or create DEVLOG.md if missing.
---

# DEVLOG Writer (Đàn)

Goal: keep a clean, scannable `DEVLOG.md` so Đàn can review changes later.

## Instructions
1. Locate repo root (current workspace).
2. Ensure `DEVLOG.md` exists at repo root. If missing, create it.
3. Append a new entry in the format from `references/devlog-format.md`.
4. Ask one clarifying question only if needed (e.g., title or missing context).

## Constraints
- Do NOT add a "Files touched" section.
- Do NOT paste long code blocks.
- Keep it short; focus on what changed and why.

## Example
User: "Update devlog for this change"
Output: append an entry with today’s date, a short title, context line, and 2-6 change bullets.
