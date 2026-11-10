#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex10
[ -f .git/BISECT_LOG ] && problem "a bisect session is still running: git bisect reset"
[ "$(g rev-parse --abbrev-ref HEAD)" = "main" ] || problem "you should be back on main"
if [ ! -f answer.txt ]; then problem "write the first bad commit ID into answer.txt"; report; fi
answer=$(head -1 answer.txt | tr -d '\r ')
bad=$(g rev-list --reverse main | sed -n 23p)
if [ ${#answer} -lt 7 ] || [ "${bad#$answer}" = "$bad" ]; then
  problem "answer.txt doesn't contain the first bad commit (look for: <id> is the first 'bad' commit)"
fi
report
