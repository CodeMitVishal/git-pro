#!/usr/bin/env bash
# Exercise 4: builds the practice repository in playground/ex04
# Run from anywhere:  bash exercises/ex04_merge_conflict/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex04
git init -q -b main
echo "theme = light" > config.txt
echo "font = normal" >> config.txt
git add config.txt
git commit -m "Add config"
git switch -c feature/dark-mode
echo "theme = dark" > config.txt
echo "font = normal" >> config.txt
echo "body { background: #111; }" > dark.css
git add .
git commit -m "Add dark mode"
git switch main
echo "theme = blue" > config.txt
echo "font = normal" >> config.txt
git commit -qam "Use the blue theme"

finish_setup ex04
