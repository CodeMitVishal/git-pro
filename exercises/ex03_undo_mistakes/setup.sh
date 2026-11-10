#!/usr/bin/env bash
# Exercise 3: builds the practice repository in playground/ex03
# Run from anywhere:  bash exercises/ex03_undo_mistakes/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex03
git init -q -b main
echo "print('shop')" > app.py
echo "price = 10" > shop.txt
git add .
git commit -m "Add shop"
echo "price = 0" > shop.txt
git commit -qam "Change pricing"
echo "tax = 0.19" > tax.txt
git add tax.txt
git commit -qm "Add tax"
git switch -c experiment
echo "banner = True" > banner.txt
git add banner.txt
git commit -qm "Try discount banner"
git switch main
git branch -D experiment
cat > app.py <<'EOF'
print('shop')
import pdb; pdb.set_trace()
x = 1 / 0
EOF

finish_setup ex03
