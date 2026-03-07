# CLAUDE.md - Project Guidelines & Preferences

> **Owner:** Đàn (User)
> **Assistant:** Zoe/Claude
> **Context:** OF1 Project (Java/Spring + React/TypeScript)

## 1. Core Philosophy (Global)
- **Mindset:** "Keep it simple". Avoid over-engineering.
- **Role:** Act as a senior partner. Don't ask for permission on trivial things; ask only when a decision has high risk/impact.
- **Language:**
  - Chat: Vietnamese (casual, terse). Technical terms in English (DTO, Mapper, Stream...).
  - Code/Comments: English.
- **Formatting:**
  - Indent: **2 spaces** (No tabs).
  - Line length: **120 chars**.
  - Break lines intentionally for readability (don't hard-wrap aggressively).
- **Logging:** **NO LOGGING** by default. Only add if explicitly requested or crucial for debugging a specific boundary.

---

## 2. Backend Guidelines (Java/Spring)
<!-- Enable for Backend/API projects -->

### Architecture
- Follow existing OF1 patterns (Controller -> Service -> Repository).
- Prefer **class-based OOP** with clear responsibilities over complex abstractions.
- **DTOs/Mappers:** Keep them dumb and simple.

### Coding Style
- **Imports:** Use `import ...;`. Avoid fully qualified class names inline unless necessary for disambiguation.
- **Chains:** Break fluent chains (Streams, Builders) into one call per line if they get too long/complex.
- **Error Handling:** Validate at boundaries. Propagate exceptions cleanly. Avoid adding custom retries/backoff unless specified.

---

## 3. Frontend Guidelines (React/TypeScript)
<!-- Enable for Frontend/UI projects -->

### Architecture
- **Structure:** Mirror existing folder structure. Do not invent new architectural patterns without discussion.
- **State Management:** Follow existing patterns (e.g., `this.state` or external stores as used in project).

### Coding Style
- **Components:** **Class Components**. Keep `render()` logic clean and readable.
- **TypeScript:** Explicit types at module boundaries (Props, State, API responses). Avoid "any" or over-engineered generics.
- **Methods:** Bind methods appropriately or use arrow functions for handlers.

---

## 4. Workflow & Artifacts

### A. DEVLOG (Mandatory)
Maintain `DEVLOG.md` at repo root. Append a short entry for each completed chunk.

```markdown
## YYYY-MM-DD - <Short Title>
- **Context:** <1 line why>
- **Changes:**
  - <bullet point>
  - <bullet point>
- **Notes:** <Optional follow-ups>
```

### B. Pull Request Template
When asked to draft a PR, use this format:

```markdown
**Title:** feat|fix|chore|refactor: <scope> - <short outcome>

**Description:**
### Summary
<1-3 sentences: what + why. No fluff.>

---

### Changes Made
**1. <Section Title>**
- **File(s):** `path/to/file`
- <Short explanation>
- <Optional: small snippet>

**2. <Section Title>**
...

---

### Configuration Required
- <Config bullets/snippet or "None">
```
