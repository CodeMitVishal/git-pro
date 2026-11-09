"""Solution · Exercise 8: Interrupted: ship a hotfix release

Run it:  python solutions/ex08_hotfix_release.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402

COMMANDS = """
git status --short
git stash push -u -m "coupon work in progress"
git switch hotfix/rounding
git tag -a v1.2.1 -m "Rounding hotfix"
git switch main
git stash pop
git status --short
git tag
"""

if __name__ == "__main__":
    solve("ex08_hotfix_release.py", COMMANDS)
