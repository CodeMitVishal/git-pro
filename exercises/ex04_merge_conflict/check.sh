#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex04
[ "$(g rev-parse --abbrev-ref HEAD)" = "main" ] || problem "you should be on main at the end"
[ "$(g log -1 --format=%p main | wc -w)" -eq 2 ] || problem "the newest commit on main should be a merge commit (two parents)"
[ "$(g show main:config.txt | tr -d '\r')" = "$(printf 'theme = dark\nfont = normal')" ] || problem "config.txt on main should be exactly 'theme = dark' and 'font = normal'"
g ls-tree --name-only main | grep -qx "dark.css" || problem "dark.css from the feature branch is missing on main"
g grep -q "<<<<<<<" main && problem "conflict markers (<<<<<<<) are still in a committed file"
[ -z "$(g branch --list feature/dark-mode)" ] || problem "delete the merged branch feature/dark-mode (git branch -d)"
[ -z "$(g status --porcelain)" ] || problem "the working tree is not clean"
report
