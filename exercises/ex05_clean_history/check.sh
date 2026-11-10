#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex05
[ "$(g log -1 --format=%s main)" = "Add footer" ] || problem "main should be unchanged (its newest commit is 'Add footer')"
n=$(g rev-list --count main..feature/search)
[ "$n" = "1" ] || { problem "feature/search should have exactly 1 commit on top of main (it has $n)"; report; }
[ "$(g log -1 --format=%P feature/search)" = "$(g rev-parse main)" ] || problem "the feature commit should sit directly on top of the current main"
[ "$(g log -1 --format=%s feature/search)" = "Add search" ] || problem "the commit message should be 'Add search'"
[ "$(g show feature/search:search.py)" = "def search(q): return [q]" ] || problem "search.py should keep the final version of the old commits"
g ls-tree --name-only feature/search | grep -qx footer.txt || problem "footer.txt from main is missing on the feature branch"
report
