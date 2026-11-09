"""Exercise 4 · Merge a feature and resolve the conflict

    python exercises/ex04_merge_conflict.py setup
    python exercises/ex04_merge_conflict.py check

Stuck? Compare with solutions/ex04_merge_conflict.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import exercise  # noqa: E402

NUMBER = 4
TASK = """
In playground/ex04, main and the branch feature/dark-mode both changed the first line
of config.txt.

  1. Merge feature/dark-mode INTO main. You will get a conflict.
  2. Resolve it so config.txt is exactly:
         theme = dark
         font = normal
  3. Finish the merge (a merge commit on main), with no conflict markers left anywhere.
  4. Delete the merged branch feature/dark-mode.
"""


def setup(sb):
    sb.script('''
git init
echo "theme = light" > config.txt
echo "font = normal" >> config.txt
git add config.txt
git commit -m "Add config"
git switch -c feature/dark-mode
echo "theme = dark" > config.txt
echo "font = normal" >> config.txt
echo "body { background: #111; }" > dark.css
git add .
git commit -m "Add dark mode"
git switch main
echo "theme = blue" > config.txt
echo "font = normal" >> config.txt
git commit -qam "Use the blue theme"
''', show=False)


def check(sb):
    if sb.git("rev-parse", "--abbrev-ref", "HEAD") != "main":
        yield "you should be on main at the end"
    parents = sb.git("log", "-1", "--format=%p", "main").split()
    if len(parents) != 2:
        yield "the newest commit on main should be a merge commit (two parents)"
    if sb.git("show", "main:config.txt") != "theme = dark\nfont = normal":
        yield "config.txt on main should be exactly 'theme = dark' and 'font = normal'"
    if "dark.css" not in sb.git("ls-tree", "--name-only", "main").split():
        yield "dark.css from the feature branch is missing on main"
    if sb.git("grep", "-n", "<<<<<<<", "main") :
        yield "conflict markers (<<<<<<<) are still in a committed file"
    if "feature/dark-mode" in sb.git("branch", "--list", "feature/dark-mode"):
        yield "delete the merged branch feature/dark-mode (git branch -d)"
    if sb.git("status", "--porcelain"):
        yield "the working tree is not clean"


if __name__ == "__main__":
    exercise(NUMBER, "Merge a feature and resolve the conflict", TASK, setup, check)
