#!/bin/bash
# One-click script to sync Dev-Kit skills
# Usage: ./run.sh

set -e

# Path to script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SYNC_SCRIPT="$SCRIPT_DIR/scripts/sync_kit.py"

echo "=== Syncing Dev-Kit Skills ==="
echo "Repo: $SCRIPT_DIR"

# Check Python environment
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 not found. Please install Python 3."
    exit 1
fi

# Run the sync script (using system python is fine as we use stdlib only)
# If you prefer venv, uncomment below:
# if [ ! -d "venv" ]; then python3 -m venv venv; fi
# source venv/bin/activate
# pip install -r requirements.txt (if any)

python3 "$SYNC_SCRIPT"

echo "=== Sync Complete! ==="
