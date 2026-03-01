#!/usr/bin/env python3
import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# --- CONFIGURATION ---
HOME = Path.home()
REPO_ROOT = Path(__file__).resolve().parent.parent

# Define sources and targets (relative to REPO_ROOT)
# Format: "target_subfolder": ("source_path", ["files_or_folders_to_include"])
# If list is empty, copy everything (excluding hidden/git).
SOURCES = {
    "gemini": (
        HOME / ".gemini",
        ["GEMINI.md"]  # Only GEMINI.md at root; skills handled separately below
    ),
    "claude": (
        HOME / ".anthropic",  # Placeholder path - adjust if needed
        [] # Copy all visible files by default
    )
}

# Special handling for Codex/OpenClaw to sync multiple workspace folders
CODEX_ROOT = HOME / ".openclaw"

# Files/Folders to always ignore
IGNORE_PATTERNS = shutil.ignore_patterns(
    ".git", ".DS_Store", "__pycache__", "venv", "node_modules", "browser_recordings", "*.log",
    # Secrets & Configs
    ".env", ".env.*", "secrets", "credentials.json", "token.json", "key.pem", "*.key", "id_rsa*",
    "config.json", "config.yaml", "config.yml", # Be careful with configs
    "oauth-token.json", "TOOLS.md", "tools.md" # Ignore tools documentation with credentials
)

def run_command(cmd, cwd=None):
    """Run a shell command."""
    try:
        subprocess.run(cmd, check=True, cwd=cwd, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}\n{e}")

def sync_folder(name, source_path, include_list):
    """Sync content from source to target subfolder in repo."""
    target_path = REPO_ROOT / name
    
    print(f"\n--- Syncing {name} ---")
    
    # 1. Clean target folder (fresh copy)
    if target_path.exists():
        shutil.rmtree(target_path)
    target_path.mkdir(parents=True, exist_ok=True)

    # Special logic for Codex: Sync all workspace* folders from .openclaw root
    if name == "codex":
        print(f"Scanning for workspaces in {CODEX_ROOT}...")
        if not CODEX_ROOT.exists():
            print(f"Warning: OpenClaw root {CODEX_ROOT} not found.")
            return

        for item in CODEX_ROOT.iterdir():
            if item.is_dir() and item.name.startswith("workspace"):
                dst_item = target_path / item.name
                print(f"  Copying {item.name} -> {dst_item}")
                shutil.copytree(item, dst_item, ignore=IGNORE_PATTERNS)
        return

    # Special logic for Gemini: Sync GEMINI.md + ONLY antigravity/skills
    if name == "gemini":
        print(f"Source: {source_path}")
        print(f"Target: {target_path}")
        
        # 1. Copy GEMINI.md (from include_list logic below or manually here)
        gemini_md = source_path / "GEMINI.md"
        if gemini_md.exists():
            shutil.copy2(gemini_md, target_path / "GEMINI.md")
            print("  Copied file: GEMINI.md")

        # 2. Copy ONLY antigravity/skills
        src_skills = source_path / "antigravity" / "skills"
        dst_skills = target_path / "antigravity" / "skills"
        
        if src_skills.exists():
            # Create parent folder first
            (target_path / "antigravity").mkdir(exist_ok=True)
            shutil.copytree(src_skills, dst_skills, ignore=IGNORE_PATTERNS)
            print(f"  Copied dir: antigravity/skills -> {dst_skills}")
        else:
            print("  Skipping missing dir: antigravity/skills")
        return

    # Standard sync logic for others
    print(f"Source: {source_path}")
    print(f"Target: {target_path}")

    if not source_path.exists():
        print(f"Warning: Source path {source_path} does not exist. Skipping.")
        return

    # 2. Copy content
    if include_list:
        # Copy specific items
        for item_name in include_list:
            src_item = source_path / item_name
            dst_item = target_path / item_name
            
            if src_item.exists():
                if src_item.is_dir():
                    shutil.copytree(src_item, dst_item, ignore=IGNORE_PATTERNS)
                    print(f"  Copied dir: {item_name}")
                else:
                    shutil.copy2(src_item, dst_item)
                    print(f"  Copied file: {item_name}")
            else:
                print(f"  Skipping missing item: {item_name}")
    else:
        # Copy entire folder content (excluding ignored)
        for item in source_path.iterdir():
            if item.name.startswith("."): continue # Skip hidden files
            
            dst_item = target_path / item.name
            if item.is_dir():
                shutil.copytree(item, dst_item, ignore=IGNORE_PATTERNS)
            else:
                shutil.copy2(item, dst_item)
        print(f"  Copied all visible content from {source_path}")

def git_commit_push():
    """Commit and push changes to GitHub."""
    print("\n--- Git Operations ---")
    
    # Check for changes
    status = subprocess.run("git status --porcelain", cwd=REPO_ROOT, shell=True, capture_output=True, text=True)
    
    if not status.stdout.strip():
        print("No changes to commit.")
        return

    print("Changes detected. Committing...")
    run_command("git add .", cwd=REPO_ROOT)
    
    commit_msg = f"chore: sync dev-kit skills ({datetime.now().strftime('%Y-%m-%d %H:%M')})"
    run_command(f'git commit -m "{commit_msg}"', cwd=REPO_ROOT)
    
    print("Pushing to remote...")
    run_command("git push origin main", cwd=REPO_ROOT)
    print("Done!")

def main():
    print(f"Starting Dev-Kit Sync... (Repo: {REPO_ROOT})")
    
    for name, (src_path, includes) in SOURCES.items():
        sync_folder(name, src_path, includes)
        
    git_commit_push()

if __name__ == "__main__":
    main()
