#!/usr/bin/env bash
# Exercise 11: builds the practice repository in playground/ex11
# Run from anywhere:  bash exercises/ex11_secret_guard_hook/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex11
git init -q -b main
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"

finish_setup ex11
