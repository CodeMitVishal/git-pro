"""Exercise 1 · Your first repository

    python exercises/ex01_first_repo.py setup    # creates playground/ex01
    python exercises/ex01_first_repo.py check    # checks your work

Stuck? Compare with solutions/ex01_first_repo.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from sandbox import exercise  # noqa: E402

NUMBER = 1
TASK = """
In playground/ex01 there are three files: README.md, hello.py and notes.txt.

  1. Turn the folder into a Git repository.
  2. Set YOUR email for this repository only (git config --local user.email ...).
  3. Make ONE commit that contains README.md and hello.py, but NOT notes.txt.
     Message: "Add hello app"
"""


def setup(sb):
    sb.write("README.md", "# Hello app\n")
    sb.write("hello.py", "print('hello')\n")
    sb.write("notes.txt", "my private notes\n")


def check(sb):
    if not sb.path(".git").exists():
        yield "the folder is not a Git repository yet (git init)"
        return
    if not sb.git("config", "--local", "user.email"):
        yield "no local user.email set (git config --local user.email you@example.com)"
    if sb.git("rev-list", "--count", "--all") != "1":
        yield "there should be exactly one commit"
        return
    files = set(sb.git("ls-tree", "--name-only", "HEAD").split())
    if files != {"README.md", "hello.py"}:
        yield f"the commit should contain README.md and hello.py only, it has {sorted(files)}"
    if sb.git("log", "-1", "--format=%s") != "Add hello app":
        yield 'the commit message should be "Add hello app"'


if __name__ == "__main__":
    exercise(NUMBER, "Your first repository", TASK, setup, check)
