#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex07
RULE='^(feat|fix|docs)(\([a-z0-9-]+\))?!?: [^ ].{8,}[^.]$'
[ "$(g rev-list --count HEAD)" -ge 4 ] || { problem "make three new commits (feat, fix, docs)"; report; }
i=0
for expect in "feat auth.py" "fix cart.py" "docs README.md"; do
  set -- $expect
  ref="HEAD~$((2 - i))"
  subject=$(g log -1 --format=%s "$ref")
  if ! echo "$subject" | grep -qE "$RULE"; then
    problem "'$subject' doesn't follow type(scope): summary"
  else
    [ "${subject%%[(:!]*}" = "$1" ] || problem "commit $((i + 1)) should be a '$1' commit"
    files=$(g show --name-only --format= "$ref" | tr '\n' ' ')
    [ "$files" = "$2 " ] || problem "the $1 commit should change only $2 (it changes: $files)"
  fi
  i=$((i + 1))
done
[ -z "$(g status --porcelain)" ] || problem "git status is not clean"
report
