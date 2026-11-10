"""Module 5 · git rebase: replay your commits on top of the latest main

merge joins histories with a merge commit. rebase instead takes YOUR commits and
replays them, one by one, on top of another branch: the result is a straight line,
as if you had started your work from the latest main.

  git switch feature
  git rebase main               replay feature's commits onto main
  git rebase --continue         after fixing a conflict
  git rebase --abort            give up, back to before the rebase

THE GOLDEN RULE: never rebase commits that other people already have (pushed and
pulled). Rebasing creates NEW commits with new IDs.

TEACHING NOTES
  Why it matters  A linear history is easy to read, bisect and revert; many teams require
                  it for pull requests.
  Picture it      Cutting your branch off and re-planting it on the newest tip of main.
  Watch out       Conflicts can happen once per replayed commit: fix, git add, git rebase
                  --continue (not git commit).
  In real jobs    git fetch && git rebase origin/main before opening a pull request.
  Interview       Q: merge vs rebase?
                  A: merge keeps the true history with a merge commit; rebase rewrites your
                     commits onto the new base for a linear history. Never rebase shared commits.

Run it:  python 05_rebase_history/01_rebase_basics.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "home" > home.txt
git add home.txt
git commit -m "Add home page"
git switch -c feature/search
echo "search v1" > search.txt
git add search.txt
git commit -m "Add search box"
echo "search v2" > search.txt
git commit -qam "Add search results"
git switch main
echo "footer" > footer.txt
git add footer.txt
git commit -m "Add footer"
''', show=False)

print("--- 1. Before: feature/search started from an OLD main")
sb.script("git log --oneline --graph --all")

print("--- 2. Rebase: replay the two feature commits on top of the new main")
sb.script('''
git switch feature/search
git rebase main
git log --oneline --graph --all
''')
print("The feature commits got NEW IDs: they are new commits with the same changes.")
print()

print("--- 3. Now main can fast-forward: a perfectly straight history")
sb.script('''
git switch main
git merge feature/search
git log --oneline
''')

print("--- 4. A conflict during rebase: fix the file, git add, git rebase --continue")
sb.script('''
git switch -c feature/home
echo "home with banner" > home.txt
git commit -qam "Add banner to home"
git switch main
echo "home with menu" > home.txt
git commit -qam "Add menu to home"
git switch feature/home
git rebase main
''')
sb.write("home.txt", "home with menu and banner\n")
sb.script('''
git add home.txt
GIT_EDITOR=true git rebase --continue
git log --oneline -3
''')
