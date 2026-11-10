#!/usr/bin/env bash
# Exercise 9: builds the practice repository in playground/ex09
# Run from anywhere:  bash exercises/ex09_commit_by_hand/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex09
git init -q -b main
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
cat > hand.txt <<'EOF'
made with plumbing
EOF

finish_setup ex09
