#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex08
if [ "$(g cat-file -t v1.2.1)" != "tag" ]; then
  problem "v1.2.1 should exist as an ANNOTATED tag (git tag -a)"
elif [ "$(g rev-parse 'v1.2.1^{commit}')" != "$(g rev-parse hotfix/rounding)" ]; then
  problem "v1.2.1 should point to the newest commit of hotfix/rounding"
fi
[ "$(g rev-parse --abbrev-ref HEAD)" = "main" ] || problem "go back to main at the end"
[ -z "$(g stash list)" ] || problem "the stash list should be empty (git stash pop)"
[ "$(tr -d '\r' < cart.py 2>/dev/null)" = "total = sum(items) - discount" ] || problem "your unfinished change in cart.py is missing"
[ -f coupon.py ] || problem "your new file coupon.py is missing (did you stash with -u?)"
[ "$(g rev-list --count main)" = "1" ] || problem "don't commit the unfinished work on main"
report
