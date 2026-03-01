```markdown
---
name: workflow-release-assistant
description: "End-to-end workflow tool: analyzes local changes vs remote, updates DEVLOG.md, generates commit messages, drafts PR descriptions, and produces user-facing changelog and release notes. Use when the user wants to finish work, wrap up, prepare PR, commit, or release."
---

# Workflow & Release Assistant (Antigravity+)

**Goal:** Automate the entire end-of-work process — from local code changes to developer documentation and user-facing release notes.

---

## Context Logic

### 1. Identify Changes

- **Default:** Compare `HEAD` (local) vs `origin/<current_branch>` (remote) to capture all unpushed work
- **Custom Range:** If a specific range is provided (e.g., `HEAD~1`, tag, branch), use that range
- **Release Mode:** If the request involves a release or changelog, analyze commits between versions or within a time window

---

### 2. Analyze Diff & History

Analyze:

- File paths and affected modules
- Lines added/removed
- Existing commit messages
- Dependency changes
- Breaking changes or migrations
- Intent (“what” and “why”)

---

## Actions (Sequential Pipeline)

### 1. Update DEVLOG.md (Internal)

- **Location:** Repository root (create if missing)
- **Format:** Append new entry using `references/devlog-template.md`
- **Content:**
  - Summarize meaningful changes for developers
  - Group by module/area when possible
  - Skip noise (formatting, whitespace-only, trivial tests)

**Rules**

- Do NOT include a “Files touched” section
- Keep high-level and readable
- Audience: Internal dev team

---

### 2. Generate Commit Message

Use **Conventional Commits** format:

```

type(scope): description

```

Provide three options:

1. **Minimal** — concise summary
2. **Scoped** — includes module/scope
3. **Detailed** — full context

Based on the entire set of detected changes.

---

### 3. Draft Pull Request

#### Title

Conventional Commit style
Example:

```

feat(auth): add OAuth2 login

```

#### Description (using `references/pr-template.md`)

Include:

- **Summary** — What does this PR do?
- **Changes** — Key technical modifications
- **Configuration** — ENV variables, DB changes, migrations
- **Dependencies** — Updates if any
- **Breaking Changes** — If applicable

**Rules**

- Do NOT paste long code blocks
- Focus on reviewer-relevant information
- Audience: Reviewers / team

---

### 4. Generate User-Facing Changelog (External)

Transform technical commits into customer-friendly updates.

#### Categorize into:

- ✨ New Features
- 🔧 Improvements
- 🐛 Bug Fixes
- 💥 Breaking Changes
- 🔒 Security

#### Behavior

- Translate technical language → user language
- Filter out internal-only commits (refactor, tests, chores)
- Apply changelog best practices
- Maintain clear, benefit-focused wording

Audience: Customers / product users

---

### 5. Release Notes / Update Summary (Optional)

If requested, generate:

- GitHub Release notes
- App Store update text
- Email announcements
- Weekly/monthly product updates
- Public changelog entries

---

## Interaction Style

### Proactive Behavior

If the user says:

- "wrap up"
- "finish work"
- "prepare PR"
- "ready to release"
- "update devlog"
- "commit changes"

→ Execute the full pipeline

---

### Verification Mode (Default)

Show proposed outputs BEFORE applying:

- DevLog entry
- Commit message options
- PR draft
- Changelog

Only proceed after confirmation
(unless user says “just do it”)

---

### Language Policy

- Structure: English
- Internal details: Vietnamese preferred
- User-facing changelog: Match product language (EN or VN)

---

## Rules & Constraints

### DevLog

- No file-by-file listings
- High-level summaries only
- Developer-oriented

---

### Pull Request

- No long code dumps
- Mention affected modules
- Highlight configuration changes

---

### Dependencies

Must explicitly mention changes to:

- `package.json`
- `build.gradle`
- `go.mod`
- `requirements.txt`
- `pom.xml`
- or equivalent dependency files

---

### Changelog

- Include only meaningful user-visible changes
- Exclude internal engineering work
- Emphasize benefits and clarity

---

## When to Use

Use this skill when the user wants to:

- Finish a work session
- Commit and push changes
- Prepare a pull request
- Generate a changelog
- Create release notes
- Ship a version
- Update DEVLOG.md

---

## Output Pipeline

```

Code Changes
↓
Internal DevLog
↓
Commit Messages
↓
Pull Request Draft
↓
User Changelog
↓
Release Notes

```

---

## Notes

- Designed as an “AI Tech Lead” workflow assistant
- Optimized for solo developers and small teams
- Minimizes manual release overhead
- Encourages consistent documentation practices
```
