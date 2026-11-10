#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex12
o() { g -C origin.git "$@"; }
m() { g -C me "$@"; }
origin_main=$(o rev-parse main)
o log --format=%s main | grep -qx "fix: round totals" || problem "origin/main lost the teammate's 'fix: round totals'"
o log --format=%s main | grep -qx "Add wishlist" && problem "'Add wishlist' ended up on origin/main: it belongs on feature/wishlist"
[ "$(m rev-parse main)" = "$origin_main" ] || problem "your local main should be exactly origin/main"
feature=$(m rev-parse --verify -q feature/wishlist)
[ -n "$feature" ] || { problem "branch feature/wishlist is missing in your clone"; report; }
m log --format=%s main..feature/wishlist | grep -qx "Add wishlist" || problem "feature/wishlist should contain your 'Add wishlist' commit"
[ "$(m merge-base main feature/wishlist)" = "$origin_main" ] || problem "feature/wishlist should sit on top of the latest main (rebase it)"
m log --name-only --format= main..feature/wishlist | grep -qx "debug.log" && problem "a commit on feature/wishlist still contains debug.log (remove it and amend)"
[ "$(o rev-parse --verify -q feature/wishlist)" = "$feature" ] || problem "push feature/wishlist to origin (and again after rewriting it)"
if [ "$(o cat-file -t v1.3.0)" != "tag" ]; then
  problem "origin needs an ANNOTATED tag v1.3.0 (git tag -a, then git push origin v1.3.0)"
elif [ "$(o rev-parse 'v1.3.0^{commit}')" != "$origin_main" ]; then
  problem "v1.3.0 should point to the latest main"
fi
[ -z "$(m status --porcelain)" ] || problem "your working tree in me/ is not clean"
report
