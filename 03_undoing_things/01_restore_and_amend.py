"""Module 3 · Small undos: restore and amend

  git restore <file>            throw away unstaged changes (back to the staged/committed version)
  git restore --staged <file>   unstage (the change stays in your working tree)
  git commit --amend            fix the LAST commit: message or forgotten files

TEACHING NOTES
  Why it matters  Most mistakes are tiny: a typo in a message, a forgotten file, a debug
                  line. Fix them in seconds instead of piling up "fix typo" commits.
  Picture it      restore = undo button for a file; amend = re-taking the last photo.
  Watch out       git restore <file> deletes your unstaged edits for good. And only amend
                  commits you haven't pushed yet: amending creates a NEW commit ID.
  In real jobs    "Oops, forgot the test file" -> git add test_x.py; git commit --amend --no-edit.
  Interview       Q: How do you change the message of your last commit?
                  A: git commit --amend -m "new message" (only if it isn't pushed/shared yet).

Run it:  python 03_undoing_things/01_restore_and_amend.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "def total(items): return sum(items)" > cart.py
git add cart.py
git commit -m "Add cart total"
''', show=False)

print("--- 1. Throw away a bad edit: git restore")
sb.script('''
echo "def total(items): return 0  # broken experiment" > cart.py
git status --short
git restore cart.py
git status --short
cat cart.py
''')

print("--- 2. Staged too much? git restore --staged unstages it (the edit stays)")
sb.script('''
echo "print('debug')" > debug.py
git add debug.py
git status --short
git restore --staged debug.py
git status --short
''')

print("--- 3. Typo in the last message and a forgotten file: git commit --amend")
sb.script('''
echo "def apply(code): return 0.1" > coupon.py
git add coupon.py
git commit -m "Add copuon"
git log --oneline
echo "def test_apply(): assert apply('X') == 0.1" > test_coupon.py
git add test_coupon.py
git commit --amend -m "Add coupon with a test"
git log --oneline --stat -1
''')
print("The amended commit has a NEW ID: never amend commits others already pulled.")
