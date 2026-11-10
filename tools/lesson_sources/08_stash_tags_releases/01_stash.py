"""Module 8 · git stash: put unfinished work aside

You're in the middle of something and must switch branches NOW (urgent bug,
reviewer asks for a change). Your work isn't ready to commit.

  git stash push -m "msg"      save tracked changes and clean the working tree
  git stash push -u -m "msg"   also include UNTRACKED (new) files
  git stash list               see the stack of stashes
  git stash pop                re-apply the newest stash and drop it
  git stash apply stash@{1}    re-apply a specific one and keep it
  git stash drop / clear       delete one / all

TEACHING NOTES
  Why it matters  Interruptions are constant; stash lets you switch context in seconds
                  without junk "WIP" commits.
  Picture it      A drawer: sweep your desk into it, deal with the visitor, then pull
                  everything back out.
  Watch out       Plain git stash ignores new (untracked) files: use -u. Stashes are local
                  and easy to forget; for anything longer than a day, commit on a branch.
  In real jobs    git stash -u; fix the hotfix; git stash pop.
  Interview       Q: What does git stash do?
                  A: Saves uncommitted changes on a stack and cleans the working tree, so you
                     can switch branches; git stash pop restores them.

Run it:  python 08_stash_tags_releases/01_stash.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "total = sum(items)" > cart.py
git add cart.py
git commit -m "Add cart"
git switch -c hotfix/rounding
echo "total = round(sum(items), 2)" > cart.py
git commit -qam "Fix rounding"
git switch main
''', show=False)

print("--- 1. Half-done work on main...")
sb.script('''
echo "total = sum(items) - discount" > cart.py
echo "def coupon(code): ..." > coupon.py
git status --short
''')

print("--- 2. ...and an urgent switch. Git refuses: your edit would be overwritten")
sb.script("git switch hotfix/rounding")

print("--- 3. Stash it (with -u for the new file), switch, do the urgent work")
sb.script('''
git stash push -u -m "coupon work in progress"
git status --short
git stash list
git switch hotfix/rounding
cat cart.py
git switch main
''')

print("--- 4. Back to your work: pop the stash")
sb.script('''
git stash pop
git status --short
cat cart.py
git stash list
''')
