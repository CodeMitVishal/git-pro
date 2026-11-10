#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex11
[ -f .git/hooks/pre-commit ] || { problem "there is no .git/hooks/pre-commit file yet"; report; }
export GIT_AUTHOR_NAME="Git Pro check" GIT_AUTHOR_EMAIL="check@git-pro.local"
export GIT_COMMITTER_NAME="Git Pro check" GIT_COMMITTER_EMAIL="check@git-pro.local"
try_commit() {            # try_commit FILE TEXT -> exit 0 if the commit went through
  local before ok=1
  before=$(g rev-parse HEAD)
  printf '%s\n' "$2" > "$1"; git add "$1"
  if git commit -q -m "test $1" >/dev/null 2>&1 && [ "$(g rev-parse HEAD)" != "$before" ]; then
    ok=0; git reset -q --soft "$before"
  fi
  git reset -q -- "$1"; rm -f "$1"
  return $ok
}
try_commit leak.env "API_KEY=sk_live_123" && problem "a commit containing API_KEY= got through: the hook must block it (exit 1)"
try_commit leak2.env "PASSWORD=hunter2" && problem "a commit containing PASSWORD= got through"
try_commit safe.txt "no secrets here" || problem "a normal commit was blocked: the hook must allow commits without secrets"
report
