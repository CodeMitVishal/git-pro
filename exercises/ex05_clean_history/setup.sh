#!/usr/bin/env bash
# Exercise 5: builds the practice repository in playground/ex05
# Run from anywhere:  bash exercises/ex05_clean_history/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex05
git init -q -b main
echo "shop" > shop.txt
git add shop.txt
git commit -m "Add shop"
git switch -c feature/search
echo "def search(q): pass" > search.py
git add search.py
git commit -m "WIP search"
echo "def search(q): return []" > search.py
git commit -qam "fix typo"
echo "def search(q): return [q]" > search.py
git commit -qam "more wip"
git switch main
echo "footer" > footer.txt
git add footer.txt
git commit -m "Add footer"

finish_setup ex05
