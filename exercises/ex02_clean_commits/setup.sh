#!/usr/bin/env bash
# Exercise 2: builds the practice repository in playground/ex02
# Run from anywhere:  bash exercises/ex02_clean_commits/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex02
git init -q -b main
echo "items = []" > cart.py
echo "# Shop" > README.md
git add .
git commit -m "Initial shop"
cat > cart.py <<'EOF'
items = []
coupon = None
EOF
cat > README.md <<'EOF'
# Shop

Now with coupons.
EOF
cat > coupon.py <<'EOF'
def apply(code): return 0.1
EOF
cat > .env <<'EOF'
STRIPE_KEY=sk_live_123
EOF
cat > debug.log <<'EOF'
debug output
EOF

finish_setup ex02
