"""Solution · Exercise 1: Your first repository

Run it:  python solutions/ex01_first_repo.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402

COMMANDS = """
git init
git config --local user.email "vishal@example.com"
git add README.md hello.py
git status --short
git commit -m "Add hello app"
git log --oneline
"""

if __name__ == "__main__":
    solve("ex01_first_repo.py", COMMANDS)
