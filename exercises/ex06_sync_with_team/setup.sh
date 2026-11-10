#!/usr/bin/env bash
# Exercise 6: builds the practice repository in playground/ex06
# Run from anywhere:  bash exercises/ex06_sync_with_team/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex06
git init -q --bare -b main origin.git
git clone -q origin.git teammate
cd teammate
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
git push -q -u origin main
cd ..
git clone -q origin.git me
cd teammate
echo "def pay(): pass" > payments.py
git add payments.py
git commit -m "Add payments"
git push -q
cd ../me
echo "def ship(): pass" > shipping.py
git add shipping.py
git commit -m "Add shipping"

finish_setup ex06
