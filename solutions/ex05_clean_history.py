"""Solution · Exercise 5: Clean up a branch before the pull request

Run it:  python solutions/ex05_clean_history.py

Two ways: interactive rebase (pick + fixup + fixup, then reword), or the quick way
below: rebase onto main, then soft-reset to main and commit once.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402

COMMANDS = """
git switch feature/search
git rebase main
git log --oneline
git reset --soft main
git commit -m "Add search"
git log --oneline --graph --all
"""

if __name__ == "__main__":
    solve("ex05_clean_history.py", COMMANDS)
