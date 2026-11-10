"""Module 2 · See what changed: git diff and git log

  git diff            working tree vs staging area  (not yet added)
  git diff --staged   staging area vs last commit    (what WILL be committed)
  git log             the history, newest first
  git show <commit>   one commit: message + changes

TEACHING NOTES
  Why it matters  Reviewing your own diff before committing catches debug prints, secrets
                  and mistakes before anyone else sees them.
  Picture it      diff is a red pen on a printout: - lines removed, + lines added.
  Watch out       git diff alone shows nothing for staged changes; use git diff --staged.
  In real jobs    Read git diff --staged before every commit; pull requests show the same diff.
  Interview       Q: git diff vs git diff --staged?
                  A: diff = unstaged changes vs the index; --staged = staged changes vs the
                     last commit.

Run it:  python 02_first_repository/02_diff_and_log.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "apples = 3" > cart.py
echo "pears = 1" >> cart.py
git add cart.py
git commit -m "Add cart"
''', show=False)

print("--- 1. Change a line: git diff shows it (not staged yet)")
sb.script('''
echo "apples = 3" > cart.py
echo "pears = 5" >> cart.py
git diff
''')

print("--- 2. After git add, plain diff is empty; --staged shows it")
sb.script('''
git add cart.py
git diff
git diff --staged --stat
git commit -m "Buy more pears"
''')

print("--- 3. Read history in different ways")
sb.script('''
git log --oneline
git log --stat -1
git show --stat HEAD~1
''')
