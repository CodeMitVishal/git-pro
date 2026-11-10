"""Module 7 · GitHub flow: how most teams ship code

  1. main is always deployable (protected: no direct pushes)
  2. git switch -c feature/x from the latest main
  3. commit, push the branch, open a Pull Request (PR)
  4. CI runs the tests; teammates review and comment
  5. merge the PR (merge commit, squash, or rebase), delete the branch
  6. main deploys

GitHub offers three merge buttons. This lesson shows what each one does to history:
  Create a merge commit  -> git merge --no-ff
  Squash and merge       -> git merge --squash + one commit
  Rebase and merge       -> rebase, then fast-forward

TEACHING NOTES
  Why it matters  This is the workflow you'll use from your first day in almost any team.
  Picture it      A restaurant kitchen: dishes (branches) are prepared separately and only
                  reach the customer (main) after the head chef checks them (review + CI).
  Watch out       Long-lived branches drift from main and end in painful merges: keep PRs
                  small and merge within days.
  In real jobs    Branch per ticket, PR with a description, green CI, one approval, squash merge.
  Interview       Q: Describe your team's Git workflow.
                  A: GitHub flow: short-lived feature branches from main, PRs with CI and code
                     review, squash or merge into a protected main, which deploys.

Run it:  python 07_team_workflows/01_github_flow.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

START = '''
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
git switch -c feature/wishlist
echo "wishlist = []" > wishlist.py
git add wishlist.py
git commit -m "Add wishlist model"
echo "def add(item): wishlist.append(item)" >> wishlist.py
git commit -qam "Add items to the wishlist"
git switch main
echo "footer" > footer.txt
git add footer.txt
git commit -m "Add footer"
'''

for title, commands in [
    ("Create a merge commit (keeps every commit + a merge commit)", "git merge --no-ff --no-edit feature/wishlist"),
    ("Squash and merge (one commit on main)", 'git merge --squash feature/wishlist\ngit commit -m "Add wishlist (#42)"'),
    ("Rebase and merge (linear, keeps each commit)", "git switch feature/wishlist\ngit rebase -q main\ngit switch main\ngit merge feature/wishlist"),
]:
    sb = Sandbox()
    sb.script(START, show=False)
    print(f"=== {title}")
    sb.script(commands + "\ngit log --oneline --graph", show=True)

print("After merging, delete the branch on GitHub; teammates run: git fetch --prune")
