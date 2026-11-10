"""Module 5 · git cherry-pick: copy ONE commit to another branch

  git cherry-pick <commit>     apply the changes of that commit on top of the current branch

Typical use: a bug fix landed on main, and the same fix is needed on the release
branch that customers are running, without bringing all of main's new features.

TEACHING NOTES
  Why it matters  Hotfixes for older releases are a daily reality in product teams.
  Picture it      Picking one cherry from another tree and placing it on yours.
  Watch out       The copy is a NEW commit with a new ID; cherry-picking many commits is
                  a sign you should merge or rebase instead.
  In real jobs    "Backport the fix to release/2.3": git cherry-pick -x <commit>.
  Interview       Q: When would you use cherry-pick?
                  A: To copy specific commits (like a hotfix) to another branch without
                     merging everything else; -x records the original commit ID.

Run it:  python 05_rebase_history/03_cherry_pick.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "total = price * qty" > cart.py
git add cart.py
git commit -m "Add cart"
git branch release/1.0
echo "new checkout page" > checkout.py
git add checkout.py
git commit -m "Add new checkout (not released yet)"
echo "total = round(price * qty, 2)" > cart.py
git commit -qam "Fix rounding in cart total"
''', show=False)

print("--- 1. main has a new feature AND a bug fix. release/1.0 needs only the fix")
sb.script("git log --oneline --all --graph")

print("--- 2. Copy just the fix")
sb.script('''
git switch release/1.0
git cherry-pick -x main
git log --oneline
git log -1 --format=%B
cat cart.py
git ls-files
''')
print("checkout.py is NOT on the release branch: only the fix came over.")
