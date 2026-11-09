"""Solution · Exercise 7: Commits a reviewer will love

Run it:  python solutions/ex07_conventional_commits.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402

COMMANDS = """
git status --short
git add auth.py
git commit -m "feat(auth): add two-factor login"
git add cart.py
git commit -m "fix(cart): round totals to 2 decimals"
git add README.md
git commit -m "docs: explain two-factor login"
git log --oneline
"""

if __name__ == "__main__":
    solve("ex07_conventional_commits.py", COMMANDS)
