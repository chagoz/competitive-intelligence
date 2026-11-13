#!/usr/bin/env bash
# Pre-release check. Fails if any private term appears in tracked files.
#
# The terms live in .release-denylist, one per line, which is deliberately
# gitignored: a committed denylist would publish exactly what it protects.
# Copy .release-denylist.example to .release-denylist and fill it in.
#
# Usage: scripts/check-release.sh [denylist-path]
set -uo pipefail

list="${1:-.release-denylist}"
if [ ! -f "$list" ]; then
  echo "No $list found. Copy .release-denylist.example to .release-denylist and fill it in."
  exit 2
fi

fail=0
while IFS= read -r term || [ -n "$term" ]; do
  term="$(printf '%s' "$term" | sed 's/[[:space:]]*$//')"
  [ -z "$term" ] && continue
  case "$term" in \#*) continue ;; esac
  if hits="$(git grep -I -n -i -e "$term" -- . ':!.release-denylist*' ':!scripts/check-release.sh' 2>/dev/null)"; then
    echo "BLOCKED: \"$term\" appears in tracked files"
    printf '%s\n' "$hits" | head -5 | sed 's/^/    /'
    fail=1
  fi
done < "$list"

if [ "$fail" -eq 0 ]; then
  echo "Clean. No denylisted term found in tracked files."
fi
exit "$fail"
