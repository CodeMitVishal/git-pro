#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex06
o() { g -C origin.git "$@"; }
o log --format=%s main | grep -qx "Add payments" || problem "origin lost Priya's commit 'Add payments'"
[ "$(o log -1 --format=%s main)" = "Add shipping" ] || problem "your 'Add shipping' should be the newest commit on origin/main (push it)"
[ "$(o rev-list --merges --count main)" = "0" ] || problem "origin/main has a merge commit: use git pull --rebase for a linear history"
[ "$(g -C me rev-parse main)" = "$(o rev-parse main)" ] || problem "your local main and origin/main should point to the same commit"
[ -z "$(g -C me status --porcelain)" ] || problem "your working tree in me/ is not clean"
report
