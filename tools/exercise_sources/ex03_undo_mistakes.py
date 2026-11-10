"""Exercise 3 · Undo three mistakes

    python exercises/ex03_undo_mistakes.py setup
    python exercises/ex03_undo_mistakes.py check

Stuck? Compare with solutions/ex03_undo_mistakes.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from sandbox import exercise  # noqa: E402

NUMBER = 3
TASK = """
playground/ex03 has three problems. Fix them all:

  1. app.py has messy, uncommitted changes. Throw them away.
  2. The commit "Change pricing" set every price to 0. main is shared with the team,
     so do NOT rewrite history: undo that commit with a new commit.
  3. Yesterday you deleted the branch "experiment" (its last commit is
     "Try discount banner"). Bring the branch back.

Hint: git restore, git revert, git reflog.
"""


def setup(sb):
    sb.script('''
git init
echo "print('shop')" > app.py
echo "price = 10" > shop.txt
git add .
git commit -m "Add shop"
echo "price = 0" > shop.txt
git commit -qam "Change pricing"
echo "tax = 0.19" > tax.txt
git add tax.txt
git commit -qm "Add tax"
git switch -c experiment
echo "banner = True" > banner.txt
git add banner.txt
git commit -qm "Try discount banner"
git switch main
git branch -D experiment
''', show=False)
    sb.write("app.py", "print('shop')\nimport pdb; pdb.set_trace()\nx = 1 / 0\n")


def check(sb):
    if sb.git("status", "--porcelain", "app.py"):
        yield "app.py still has uncommitted changes"
    subjects = sb.git("log", "--format=%s", "main").splitlines()
    if "Change pricing" not in subjects:
        yield "'Change pricing' disappeared from history: on a shared branch use revert, not reset"
    if not subjects or subjects[0] != 'Revert "Change pricing"':
        yield "the newest commit on main should be the revert of 'Change pricing'"
    if sb.git("show", "main:shop.txt") != "price = 10":
        yield "shop.txt on main should be back to 'price = 10'"
    if sb.git("log", "-1", "--format=%s", "experiment") != "Try discount banner":
        yield "branch 'experiment' should exist again, ending with 'Try discount banner'"


if __name__ == "__main__":
    exercise(NUMBER, "Undo three mistakes", TASK, setup, check)
