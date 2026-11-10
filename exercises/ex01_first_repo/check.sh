#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex01
[ -d .git ] || { problem "the folder is not a Git repository yet (git init)"; report; }
[ -n "$(g config --local user.email)" ] || problem "no local user.email (git config --local user.email you@example.com)"
[ "$(g rev-list --count --all)" = "1" ] || { problem "there should be exactly one commit"; report; }
files=$(g ls-tree --name-only HEAD | tr '\n' ' ')
[ "$files" = "README.md hello.py " ] || problem "the commit should contain README.md and hello.py only (it has: $files)"
[ "$(g log -1 --format=%s)" = "Add hello app" ] || problem 'the commit message should be "Add hello app"'
report
