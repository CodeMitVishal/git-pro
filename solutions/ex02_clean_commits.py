"""Solution · Exercise 2: Clean commits and a .gitignore

Run it:  python solutions/ex02_clean_commits.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402

COMMANDS = """
echo ".env" > .gitignore
echo "*.log" >> .gitignore
git add .gitignore
git commit -m "Add gitignore"
git add cart.py coupon.py
git commit -m "Add coupons"
git add README.md
git commit -m "Document coupons"
git status --short
git log --oneline
"""

if __name__ == "__main__":
    solve("ex02_clean_commits.py", COMMANDS)
