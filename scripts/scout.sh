#!/usr/bin/env bash
# Daily scout, catch-up style: cron calls this hourly; it runs once per day,
# the first time the laptop is awake. Works with whichever Claude account is logged in.
set -euo pipefail
cd "$(dirname "$0")/.."
TODAY=$(date +%F)
git pull --rebase --quiet 2>/dev/null || true
[ -f "05-digests/$TODAY.md" ] && exit 0
LOCK="/tmp/taste-lab-scout.lock"
mkdir "$LOCK" 2>/dev/null || exit 0
trap 'rmdir "$LOCK"' EXIT
echo "=== scout $(date -Iseconds) ==="
claude -p "/scout" --permission-mode acceptEdits
if [ -d .git ]; then
  git add 00-inbox 01-papers 02-concepts 03-threads 05-digests 2>/dev/null || true
  git commit -m "scout: $TODAY" -m "Session-Account: ${TASTE_LAB_ACCOUNT:-unknown}" --quiet || echo "nothing new"
  git push --quiet 2>/dev/null || echo "push failed; retry next run"
fi
