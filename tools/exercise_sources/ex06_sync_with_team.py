"""Exercise 6 · Sync with your team

    python exercises/ex06_sync_with_team.py setup
    python exercises/ex06_sync_with_team.py check

Stuck? Compare with solutions/ex06_sync_with_team.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from sandbox import exercise  # noqa: E402

NUMBER = 6
TASK = """
playground/ex06 contains:
  origin.git   the shared repository (it plays GitHub)
  me/          YOUR clone. You have a local commit "Add shipping" that isn't pushed.
  teammate/    Priya's clone. She already pushed "Add payments" to origin.

Work inside playground/ex06/me:
  1. Get Priya's commit.
  2. Push your commit.
  3. The history on origin must be LINEAR: no merge commits.

Hint: git pull --rebase, then git push.
"""


def setup(sb):
    sb.script('''
git init --bare origin.git
git clone -q origin.git teammate
cd teammate
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
git push -q -u origin main
cd ..
git clone -q origin.git me
cd teammate
echo "def pay(): pass" > payments.py
git add payments.py
git commit -m "Add payments"
git push -q
cd ../me
echo "def ship(): pass" > shipping.py
git add shipping.py
git commit -m "Add shipping"
''', show=False)


def check(sb):
    origin = ["-C", "origin.git"]
    subjects = sb.git(*origin, "log", "--format=%s", "main").splitlines()
    if "Add payments" not in subjects:
        yield "origin lost Priya's commit 'Add payments'"
    if not subjects or subjects[0] != "Add shipping":
        yield "your commit 'Add shipping' should be the newest commit on origin/main (push it)"
    if sb.git(*origin, "rev-list", "--merges", "--count", "main") != "0":
        yield "origin/main contains a merge commit: use git pull --rebase for a linear history"
    if sb.git("-C", "me", "rev-parse", "main") != sb.git(*origin, "rev-parse", "main"):
        yield "your local main and origin/main should point to the same commit"
    if sb.git("-C", "me", "status", "--porcelain"):
        yield "your working tree in me/ is not clean"


if __name__ == "__main__":
    exercise(NUMBER, "Sync with your team", TASK, setup, check)
