"""Solution · Exercise 4: Merge a feature and resolve the conflict

Run it:  python solutions/ex04_merge_conflict.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402

COMMANDS = """
git merge feature/dark-mode
git status --short
cat config.txt
# write the resolved file (in real life: edit it in VS Code and remove the markers)
echo "theme = dark" > config.txt
echo "font = normal" >> config.txt
git add config.txt
git commit --no-edit
git branch -d feature/dark-mode
git log --oneline --graph
"""

if __name__ == "__main__":
    solve("ex04_merge_conflict.py", COMMANDS)
