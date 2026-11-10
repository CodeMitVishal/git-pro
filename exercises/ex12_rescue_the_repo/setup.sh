#!/usr/bin/env bash
# Exercise 12: builds the practice repository in playground/ex12
# Run from anywhere:  bash exercises/ex12_rescue_the_repo/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex12
git init -q --bare -b main origin.git
git clone -q origin.git teammate
cd teammate
echo "# Shop" > README.md
echo "total = sum(items)" > cart.py
git add .
git commit -m "Initial commit"
git push -q -u origin main
cd ..
git clone -q origin.git me
cd teammate
echo "total = round(sum(items), 2)" > cart.py
git commit -qam "fix: round totals"
git push -q
cd ../me
echo "wishlist = []" > wishlist.py
echo "DEBUG 12:01 something" > debug.log
git add .
git commit -m "Add wishlist"

finish_setup ex12
