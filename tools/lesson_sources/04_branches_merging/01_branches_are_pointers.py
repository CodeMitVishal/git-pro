"""Module 4 · Branches are just movable pointers

A branch is a tiny file containing ONE commit ID. Creating a branch copies
nothing; it's instant. HEAD points to the branch you're on. Each new commit
moves that branch forward.

  git branch                 list branches (* = current)
  git switch -c feature/x    create a branch and switch to it
  git switch main            go back
  git branch -d feature/x    delete a merged branch

TEACHING NOTES
  Why it matters  Branches let you build a feature without breaking main, and let
                  10 developers work at the same time.
  Picture it      Sticky notes on a timeline of photos: each note (branch) marks one photo;
                  HEAD is the note you're holding.
  Watch out       Switching branches with uncommitted changes carries them along (or Git
                  refuses). Commit or stash first (Module 8).
  In real jobs    One branch per ticket: feature/JIRA-123-coupon-codes.
  Interview       Q: What is a branch in Git?
                  A: A lightweight movable pointer to a commit; HEAD points to the current
                     branch, and each commit moves it forward.

Run it:  python 04_branches_merging/01_branches_are_pointers.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "home page" > home.txt
git add home.txt
git commit -m "Add home page"
''', show=False)

print("--- 1. A branch is a file with a commit ID in it")
sb.script('''
git branch
git rev-parse main
cat .git/HEAD
''')

print("--- 2. Create a feature branch: nothing is copied, it's instant")
sb.script('''
git switch -c feature/coupons
git branch
echo "coupons" > coupons.txt
git add coupons.txt
git commit -m "Add coupons"
git log --oneline --all --graph
''')

print("--- 3. Switching branches changes the files in your folder")
sb.script('''
git switch main
git status --short
git ls-files
git switch feature/coupons
git ls-files
''')
