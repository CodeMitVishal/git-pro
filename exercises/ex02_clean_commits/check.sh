#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex02
subjects=$(g log --format=%s -3 | tac | tr '\n' '|')
if [ "$subjects" != "Add gitignore|Add coupons|Document coupons|" ]; then
  problem "the last three commits should be (oldest first): Add gitignore, Add coupons, Document coupons"; report
fi
files() { g show --name-only --format= "$1" | sort | tr '\n' ' '; }
[ "$(files HEAD~2)" = ".gitignore " ] || problem "'Add gitignore' should change only .gitignore"
[ "$(files HEAD~1)" = "cart.py coupon.py " ] || problem "'Add coupons' should contain cart.py and coupon.py only"
[ "$(files HEAD)" = "README.md " ] || problem "'Document coupons' should contain README.md only"
g log --all --name-only --format= | grep -qx ".env" && problem ".env was committed: secrets must never be committed"
[ -z "$(g status --porcelain)" ] || problem "git status is not clean (is something not ignored or not committed?)"
report
