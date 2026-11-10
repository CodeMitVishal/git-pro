#!/usr/bin/env bash
# Exercise 1: builds the practice repository in playground/ex01
# Run from anywhere:  bash exercises/ex01_first_repo/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex01
cat > README.md <<'EOF'
# Hello app
EOF
cat > hello.py <<'EOF'
print('hello')
EOF
cat > notes.txt <<'EOF'
my private notes
EOF

finish_setup ex01
