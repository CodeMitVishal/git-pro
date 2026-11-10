#!/usr/bin/env bash
# Exercise 7: builds the practice repository in playground/ex07
# Run from anywhere:  bash exercises/ex07_conventional_commits/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex07
git init -q -b main
echo "def login(user, pw): ..." > auth.py
echo "def total(items): return sum(items)" > cart.py
echo "# Shop" > README.md
git add .
git commit -m "Initial shop"
cat >> auth.py <<'EOF'
def verify_2fa(user, code): ...
EOF
cat > cart.py <<'EOF'
def total(items): return round(sum(items), 2)
EOF
cat >> README.md <<'EOF'

Login now asks for a two-factor code.
EOF

finish_setup ex07
