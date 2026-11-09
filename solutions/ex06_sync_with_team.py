"""Solution · Exercise 6: Sync with your team

Run it:  python solutions/ex06_sync_with_team.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402

COMMANDS = """
cd me
git status -sb
git push
git pull --rebase
git log --oneline --graph
git push
git status -sb
"""

if __name__ == "__main__":
    solve("ex06_sync_with_team.py", COMMANDS)
