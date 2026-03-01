---
name: workflow-assistant
description: "All-in-one workflow tool: Updates DEVLOG.md, generates git commit messages, and drafts PR descriptions based on local changes vs remote. Use when the user wants to 'finish work', 'wrap up', 'prepare PR', or 'update devlog/commit'."
---

# Workflow Assistant (Antigravity)

**Goal:** Streamline the "finish work" process by automatically tracking changes, committing, and preparing for review.

## Context Logic
1.  **Identify Changes:**
    *   **Default:** Compare `HEAD` (local) vs `origin/<current_branch>` (remote) to capture all unpushed work.
    *   **If specific range provided:** Use that range (e.g., `HEAD~1`, `feature-branch`).
2.  **Analyze Diff:** Look at file paths, added/removed lines, and commit history to understand the "what" and "why".

## Actions (Sequential)

### 1. Update DEVLOG.md
*   **Locate:** `DEVLOG.md` at repo root (create if missing).
*   **Format:** Append a new entry using `references/devlog-template.md`.
*   **Content:** Summarize *meaningful* changes (skip noise like whitespace/formatting unless relevant).
*   **Style:** Bullet points, grouped by module/area if possible.

### 2. Generate Commit Message
*   **Style:** Conventional Commits (`type(scope): description`).
*   **Options:** Provide 3 options (Minimal, Scoped, Detailed).
*   **Input:** Based on the *entire* set of changes detected.

### 3. Draft Pull Request
*   **Title:** Conventional Commit style (e.g., `feat(crm): add partner sync`).
*   **Description:** Use `references/pr-template.md`.
*   **Content:**
    *   **Summary:** High-level "what does this do?".
    *   **Changes:** Technical details (files/modules touched).
    *   **Configuration:** specific ENV vars or DB changes if any.

## Interaction Style
*   **Proactive:** If the user says "wrap up" or "prepare PR", do all 3 steps.
*   **Verification:** Show the proposed DevLog entry, Commit Message, and PR Draft *before* applying (unless asked to "just do it").
*   **Language:** English wrapper, Vietnamese details (as per user preference).

## Rules
*   **Do NOT** include a "Files touched" section in DevLog (keep it high-level).
*   **Do NOT** paste long code blocks in PR description.
*   **Do** mention if `package.json`, `build.gradle`, or `go.mod` changed (dependency updates).
