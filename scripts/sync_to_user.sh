#!/bin/bash
# Script sync .gemini from current user to 'nqcdan.dev'
# Usage: sudo ./sync_to_user.sh

SOURCE_DIR="/Users/nqcdan/.gemini"
DEST_USER="nqcdan.dev"
DEST_DIR="/Users/$DEST_USER/.gemini"

# 1. Check Root/Sudo
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (use sudo)"
  exit 1
fi

echo "=== Syncing Gemini from nqcdan to $DEST_USER ==="

# 2. Check Rsync
if ! command -v rsync &> /dev/null; then
    echo "rsync not found. Please install it: brew install rsync"
    exit 1
fi

# 3. Create destination if not exists
if [ ! -d "$DEST_DIR" ]; then
    echo "Creating directory: $DEST_DIR"
    mkdir -p "$DEST_DIR"
fi

# 4. Sync Data
# -a: archive mode (preserves permissions, times, symbolic links)
# -v: verbose
# --delete: delete files in dest that are missing in source (exact mirror)
echo "Syncing files..."
rsync -av --delete "$SOURCE_DIR/" "$DEST_DIR/" --exclude ".git"

# 5. Fix Permissions (CRITICAL)
# Change owner to destination user so they can read/write
echo "Fixing permissions for $DEST_USER..."
chown -R "$DEST_USER:staff" "$DEST_DIR"

echo "=== Done! ==="
echo "Verifying owner:"
ls -ld "$DEST_DIR"
