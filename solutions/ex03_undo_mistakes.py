"""Solution · Exercise 3: Undo three mistakes

Run it:  python solutions/ex03_undo_mistakes.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402

COMMANDS = """
# 3 first: find the lost commit while it's still HEAD@{1} in the reflog
git reflog -3
git branch experiment HEAD@{1}
# 1: throw away the uncommitted mess
git restore app.py
# 2: undo a shared commit with a NEW commit
git log --oneline
git revert --no-edit HEAD~1
git log --oneline
"""

if __name__ == "__main__":
    solve("ex03_undo_mistakes.py", COMMANDS)
