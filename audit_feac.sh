#!/usr/bin/env bash
set -e

echo "=== AUDIT START: $(date) ==="
echo

# 1) Git status
echo ">>> GIT STATUS"
git status
echo

# 2) Current branch
echo ">>> CURRENT BRANCH"
git branch --show-current
echo

# 3) Remote branches
echo ">>> REMOTE BRANCHES"
git fetch --all --prune
git branch -r
echo

# 4) Branch diff vs main
echo ">>> DIFF SUMMARY (branch vs main)"
for br in $(git branch -r | sed 's|origin/||' | grep -v HEAD); do
  echo "---- $br vs main"
  git diff --stat origin/main...origin/$br || true
  echo
done

# 5) Files only on branches, not in main
echo ">>> FILES PRESENT ON BRANCHES BUT NOT ON MAIN"
for br in $(git branch -r | sed 's|origin/||' | grep -v HEAD); do
  echo "--- $br unique files:"
  git diff --name-only origin/main...origin/$br | sort | uniq
  echo
done

# 6) AST file health check (Python/JS)
echo ">>> AST BASELINE CHECK"
find . -type f \( -name \"*.py\" -o -name \"*.js\" \) | while read file; do
  # Skip node_modules
  echo "$file"
done

echo "=== AUDIT COMPLETE ==="
