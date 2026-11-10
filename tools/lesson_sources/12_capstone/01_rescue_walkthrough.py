"""Module 12 · Capstone walkthrough: how to rescue any messy repository

When a repository is in a strange state, don't type commands at random.
Follow the same four steps every time:

  1. LOOK      git status -sb · git log --oneline --graph --all · git stash list
  2. FIND      git reflog (where was I?) · git log origin/main..main (what's unpushed?)
  3. PLAN      what should main / my branch / the remote look like at the end?
  4. ACT       small, reversible steps; check with git log after each one

This walkthrough fixes the most common mess: you committed to main by mistake,
and meanwhile a teammate pushed to main.

TEACHING NOTES
  Why it matters  Calmly fixing a broken repo is what makes people trust you with the
                  production branch.
  Picture it      A doctor: look at the symptoms, check the history, decide on a treatment,
                  then treat one step at a time.
  Watch out       Before anything risky, make a safety branch: git branch backup.
                  It costs nothing and makes every mistake reversible.
  In real jobs    "I committed to main!", "my branch is 40 commits behind", "the push is
                  rejected": everyday Slack messages you'll be able to answer.
  Interview       Q: You committed to main instead of a feature branch. Fix it.
                  A: git branch feature/x (keeps the commit), git reset --hard origin/main
                     on main, then continue on feature/x (rebase it if main moved).

Run it:  python 12_capstone/01_rescue_walkthrough.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init --bare ../github/shop.git
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
git remote add origin ../github/shop.git
git push -q -u origin main
git clone -q ../github/shop.git ../priya
cd ../priya
echo "total = round(sum(items), 2)" > cart.py
git add cart.py
git commit -qm "fix: round totals"
git push -q
cd ../project
echo "wishlist = []" > wishlist.py
git add wishlist.py
git commit -m "Add wishlist"
''', show=False)

print("=== 1. LOOK")
sb.script('''
git status -sb
git fetch
git status -sb
git log --oneline --graph --all
''')

print("=== 2. FIND: what's mine and unpushed?")
sb.script("git log --oneline origin/main..main")

print("=== 3. PLAN: main = origin/main; my commit on feature/wishlist, on top of the latest main\n")

print("=== 4. ACT, one safe step at a time")
sb.script('''
git branch backup
git branch feature/wishlist
git reset --hard origin/main
git log --oneline
git switch feature/wishlist
git rebase main
git log --oneline --graph --all
git push -u origin feature/wishlist
git branch -D backup
''')
print("Done: main matches the team, your work sits on its own branch, ready for a pull request.")
