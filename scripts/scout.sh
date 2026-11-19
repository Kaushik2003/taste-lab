#!/usr/bin/env bash
# Headless daily scout. Run from cron. Needs Claude Code installed and logged in.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "=== scout $(date -Iseconds) ==="
claude -p "/scout" --permission-mode acceptEdits

# commit the digest + any new notes so history shows what the scout added
if [ -d .git ]; then
  git add 00-inbox 01-papers 02-concepts 05-digests 03-threads 2>/dev/null || true
  git commit -m "scout: $(date +%F)" --quiet || echo "nothing new to commit"
fi
