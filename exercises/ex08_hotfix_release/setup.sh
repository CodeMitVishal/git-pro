#!/usr/bin/env bash
# Exercise 8: builds the practice repository in playground/ex08
# Run from anywhere:  bash exercises/ex08_hotfix_release/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex08
git init -q -b main
echo "total = sum(items)" > cart.py
git add cart.py
git commit -m "Add cart"
git tag -a v1.2.0 -m "Release 1.2.0"
git switch -c hotfix/rounding
echo "total = round(sum(items), 2)" > cart.py
git commit -qam "fix: round cart totals"
git switch main
cat > cart.py <<'EOF'
total = sum(items) - discount
EOF
cat > coupon.py <<'EOF'
def coupon(code): ...
EOF

finish_setup ex08
