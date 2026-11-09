"""Module 11 · git worktree: two branches checked out at the same time

Stash is fine for a quick switch. When you need to work on a hotfix while your
feature branch keeps running (a dev server, a long test run), use a worktree:
a second folder linked to the SAME repository, with a different branch checked out.

  git worktree add ../shop-hotfix hotfix/rounding     new folder on that branch
  git worktree list
  git worktree remove ../shop-hotfix

TEACHING NOTES
  Why it matters  No stashing, no lost context, no re-installing dependencies:
                  each task gets its own folder.
  Picture it      Two desks in the same office, sharing one filing cabinet (.git).
  Watch out       A branch can be checked out in only one worktree at a time.
  In real jobs    Reviewing a colleague's PR in a separate folder while your own work stays open.
  Interview       Q: stash vs worktree?
                  A: stash shelves changes so you can switch in the same folder; a worktree
                     gives another branch its own folder at the same time.

Run it:  python 11_advanced_git/02_worktrees.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "total = sum(items)" > cart.py
git add cart.py
git commit -m "Add cart"
git branch hotfix/rounding
git switch -c feature/coupons
echo "half-finished coupon work" > coupon.py
''', show=False)

print("--- 1. Mid-feature, with uncommitted work... open the hotfix in a second folder")
sb.script('''
git status --short
git worktree add ../shop-hotfix hotfix/rounding
git worktree list
''')

print("--- 2. Fix the bug over there; your feature folder is untouched")
sb.script('''
cd ../shop-hotfix
echo "total = round(sum(items), 2)" > cart.py
git commit -qam "fix: round totals"
git log --oneline -1
cd ../project
git status --short
git log --oneline -1 hotfix/rounding
''')

print("--- 3. Clean up")
sb.script('''
git worktree remove ../shop-hotfix
git worktree list
''')
