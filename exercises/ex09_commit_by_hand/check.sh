#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex09
[ "$(g log -1 --format=%s main)" = "Built by hand" ] || { problem "the newest commit on main should be 'Built by hand'"; report; }
[ "$(g log -1 --format=%s main~1)" = "Initial commit" ] || problem "its parent should be 'Initial commit'"
[ "$(g ls-tree --name-only main | tr '\n' ' ')" = "README.md hand.txt " ] || problem "the commit should contain README.md and hand.txt"
[ "$(g show main:hand.txt)" = "made with plumbing" ] || problem "hand.txt in the commit should say 'made with plumbing'"
if [ ! -f answers.txt ]; then problem "answers.txt needs two lines"; report; fi
a1=$(sed -n 1p answers.txt | tr -d '\r '); a2=$(sed -n 2p answers.txt | tr -d '\r ')
[ "$a1" = "tree" ] || problem "line 1 of answers.txt: the type of a commit's tree is... tree"
blob=$(g rev-parse main:hand.txt)
if [ ${#a2} -lt 7 ] || [ "${blob#$a2}" = "$blob" ]; then problem "line 2 of answers.txt should be the blob ID of hand.txt (7+ characters)"; fi
report
