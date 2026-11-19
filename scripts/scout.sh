#!/usr/bin/env bash
# Daily scout, catch-up style: cron calls this hourly; it runs once per day,
# the first time the laptop is awake. Works with whichever Claude account is logged in.
set -euo pipefail
cd "$(dirname "$0")/.."
# Load .env (gitignored) without overriding anything already set, e.g. by the cron line.
if [ -f .env ]; then
  while IFS='=' read -r k v || [ -n "$k" ]; do
    [[ $k =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]] || continue
    v="${v%\"}"; v="${v#\"}"
    [ -z "${!k+x}" ] && export "$k=$v"
  done < .env
fi
TODAY=$(date +%F)
git pull --rebase --quiet 2>/dev/null || true
[ -f "9 Claude files/Reports/$TODAY.md" ] && exit 0
LOCK="/tmp/taste-lab-scout.lock"
mkdir "$LOCK" 2>/dev/null || exit 0
trap 'rmdir "$LOCK"' EXIT
echo "=== scout $(date -Iseconds) ==="
claude -p "/scout" --permission-mode acceptEdits
if [ -d .git ]; then
  git add "9 Claude files/Inbox" "2 Papers" "3 Ideas" "5 Research ideas (later)" "9 Claude files/Reports" 2>/dev/null || true
  git commit -m "scout: $TODAY" -m "Session-Account: ${TASTE_LAB_ACCOUNT:-unknown}" --quiet || echo "nothing new"
  git push --quiet 2>/dev/null || echo "push failed; retry next run"
fi
