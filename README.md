# Dev-Kit Skills Central

Central repository for AI Agent skills and configurations.

## Setup & Usage

### Quick Start
Just run the sync script:
```bash
./run.sh
```

This will:
1.  Mirror skills/configs from local agents (`~/.gemini`, `~/.openclaw`, etc.) into subfolders.
2.  Auto-commit and push changes to GitHub (`main` branch).

### Managed Agents
The script syncs the following paths by default:

- **Gemini:** `~/.gemini` -> `gemini/`
  - Includes: `GEMINI.md`, `antigravity/skills`
- **Codex:** `~/.openclaw/workspace` -> `codex/`
  - Includes: `AGENTS.md`, `MEMORY.md`, `SOUL.md`, `TOOLS.md`, `USER.md`, and any `skills/` folder.
- **Claude:** `~/.anthropic` (Default placeholder) -> `claude/`
  - Includes: All visible files.

### Requirements
- Python 3 (Standard Library only - no pip install needed).
- Git configured with SSH key (`git push` access).

To modify source paths, edit `scripts/sync_kit.py`.
