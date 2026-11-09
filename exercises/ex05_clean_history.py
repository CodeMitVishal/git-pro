"""Exercise 5 · Clean up a branch before the pull request

    python exercises/ex05_clean_history.py setup
    python exercises/ex05_clean_history.py check

Stuck? Compare with solutions/ex05_clean_history.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import exercise  # noqa: E402

NUMBER = 5
TASK = """
In playground/ex05, the branch feature/search has three messy commits ("WIP search",
"fix typo", "more wip") and it started from an OLD main. main has a new commit since.

Before opening the pull request:
  1. Turn the three commits into ONE commit with the message "Add search".
  2. Put that commit on top of the CURRENT main (linear history, no merge commit).
  3. Leave main itself unchanged.

Hint: git rebase main, then git rebase -i (squash/fixup) or git reset --soft main.
"""


def setup(sb):
    sb.script('''
git init
echo "shop" > shop.txt
git add shop.txt
git commit -m "Add shop"
git switch -c feature/search
echo "def search(q): pass" > search.py
git add search.py
git commit -m "WIP search"
echo "def search(q): return []" > search.py
git commit -qam "fix typo"
echo "def search(q): return [q]" > search.py
git commit -qam "more wip"
git switch main
echo "footer" > footer.txt
git add footer.txt
git commit -m "Add footer"
''', show=False)


def check(sb):
    main_tip = sb.git("rev-parse", "main")
    if sb.git("log", "-1", "--format=%s", "main") != "Add footer":
        yield "main should be unchanged (its newest commit is 'Add footer')"
    commits = sb.git("rev-list", "main..feature/search").split()
    if len(commits) != 1:
        yield f"feature/search should have exactly 1 commit on top of main, it has {len(commits)}"
        return
    if sb.git("log", "-1", "--format=%P", "feature/search") != main_tip:
        yield "the feature commit should sit directly on top of the current main"
    if sb.git("log", "-1", "--format=%s", "feature/search") != "Add search":
        yield "the commit message should be 'Add search'"
    if sb.git("show", "feature/search:search.py") != "def search(q): return [q]":
        yield "search.py should keep the final version from the old commits"
    if "footer.txt" not in sb.git("ls-tree", "--name-only", "feature/search").split():
        yield "footer.txt from main is missing on the feature branch"


if __name__ == "__main__":
    exercise(NUMBER, "Clean up a branch before the pull request", TASK, setup, check)
