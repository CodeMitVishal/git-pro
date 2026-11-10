#!/usr/bin/env bash
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
open_playground ex03
[ -z "$(g status --porcelain app.py)" ] || problem "app.py still has uncommitted changes"
g log --format=%s main | grep -qx "Change pricing" || problem "'Change pricing' vanished from history: on a shared branch use revert, not reset"
[ "$(g log -1 --format=%s main)" = 'Revert "Change pricing"' ] || problem "the newest commit on main should be the revert of 'Change pricing'"
[ "$(g show main:shop.txt)" = "price = 10" ] || problem "shop.txt on main should be back to 'price = 10'"
[ "$(g log -1 --format=%s experiment)" = "Try discount banner" ] || problem "branch 'experiment' should exist again, ending with 'Try discount banner'"
report
