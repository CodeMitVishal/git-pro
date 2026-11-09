"""Exercise 9 · Make a commit without git add or git commit

    python exercises/ex09_commit_by_hand.py setup
    python exercises/ex09_commit_by_hand.py check

Stuck? Compare with solutions/ex09_commit_by_hand.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import exercise  # noqa: E402

NUMBER = 9
TASK = """
playground/ex09 has one commit ("Initial commit", with README.md) and a new file
hand.txt. Using ONLY plumbing commands (hash-object, update-index, write-tree,
commit-tree, update-ref), create a new commit on main:

  - message:  Built by hand
  - parent:   the current main ("Initial commit")
  - contents: README.md (unchanged) and hand.txt

Then answer in answers.txt (one per line, untracked is fine):
  line 1: the object TYPE of the new commit's tree   (git cat-file -t ...)
  line 2: the blob ID of hand.txt                      (git rev-parse HEAD:hand.txt)
"""


def setup(sb):
    sb.script('''
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
''', show=False)
    sb.write("hand.txt", "made with plumbing\n")


def check(sb):
    if sb.git("log", "-1", "--format=%s", "main") != "Built by hand":
        yield "the newest commit on main should be 'Built by hand'"
        return
    if sb.git("log", "-1", "--format=%s", "main~1") != "Initial commit":
        yield "its parent should be 'Initial commit'"
    files = set(sb.git("ls-tree", "--name-only", "main").split())
    if files != {"README.md", "hand.txt"}:
        yield f"the commit should contain README.md and hand.txt, it has {sorted(files)}"
    if sb.git("show", "main:hand.txt") != "made with plumbing":
        yield "hand.txt in the commit should say 'made with plumbing'"
    answers = sb.read("answers.txt").split() if sb.path("answers.txt").exists() else []
    if len(answers) < 2:
        yield "answers.txt needs two lines"
        return
    if answers[0] != "tree":
        yield "line 1 of answers.txt: the type of a commit's tree is... tree"
    if not sb.git("rev-parse", "main:hand.txt").startswith(answers[1]) or len(answers[1]) < 7:
        yield "line 2 of answers.txt should be the blob ID of hand.txt (at least 7 characters)"


if __name__ == "__main__":
    exercise(NUMBER, "Make a commit without git add or git commit", TASK, setup, check)
