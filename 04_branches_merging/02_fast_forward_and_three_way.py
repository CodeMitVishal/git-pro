"""Module 4 · Merging: fast-forward vs three-way merge

  fast-forward   main hasn't moved since you branched -> Git just slides main forward.
                 No new commit; history stays a straight line.
  three-way      both branches have new commits -> Git combines them in a MERGE COMMIT
                 with two parents.

  git merge feature        merge feature INTO the current branch
  git merge --no-ff x      always create a merge commit (keeps the feature visible)

TEACHING NOTES
  Why it matters  Every pull request ends with a merge; knowing which kind explains the
                  shape of your history.
  Picture it      Fast-forward: catching up on the same road. Three-way: two roads joining
                  at a junction (the merge commit).
  Watch out       Merge INTO the branch you're on: switch to main first, then git merge feature.
  In real jobs    GitHub's "Merge", "Squash and merge" and "Rebase and merge" buttons.
  Interview       Q: What is a fast-forward merge?
                  A: When the target branch has no new commits, Git just moves its pointer
                     forward to the feature tip; no merge commit is created.

Run it:  python 04_branches_merging/02_fast_forward_and_three_way.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

START = '''
git init
echo "home page" > home.txt
git add home.txt
git commit -m "Add home page"
git switch -c feature/search
echo "search box" > search.txt
git add search.txt
git commit -m "Add search"
'''

print("=== A. FAST-FORWARD: main did not move")
sb = Sandbox()
sb.script(START, show=False)
sb.script('''
git switch main
git merge feature/search
git log --oneline --graph --all
''')

print("=== B. THREE-WAY: main moved too")
sb = Sandbox()
sb.script(START, show=False)
sb.script('''
git switch main
echo "footer" > footer.txt
git add footer.txt
git commit -m "Add footer"
git merge --no-edit feature/search
git log --oneline --graph --all
git log -1 --format="merge commit parents: %p"
''')

print("Delete the branch after merging:  git branch -d feature/search")
