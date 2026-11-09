"""Exercise 10 · Find the commit that broke the prices

    python exercises/ex10_find_the_bug.py setup
    python exercises/ex10_find_the_bug.py check

Stuck? Compare with solutions/ex10_find_the_bug.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import exercise  # noqa: E402

NUMBER = 10
BAD = 23                           # the commit number that introduces the bug
TASK = """
playground/ex10 has 30 commits. Release v1.0.0 (the first commit) had correct prices;
today gross(100) returns the wrong value. check_price.py exits with 0 when the
prices are right and 1 when they're wrong:

    python check_price.py

  1. Use git bisect (ideally git bisect run python check_price.py) to find the FIRST
     bad commit.
  2. Write its commit ID (at least 7 characters) into answer.txt.
  3. Finish the bisect session (git bisect reset) so you're back on main.
"""


def setup(sb):
    sb.script("git init", show=False)
    sb.write("check_price.py", "from price import gross\nimport sys\nsys.exit(0 if gross(100) == 119 else 1)\n")
    sb.write(".gitignore", "answer.txt\n__pycache__/\n")
    for i in range(1, 31):
        rate = "1.18" if i >= BAD else "1.19"
        sb.write("price.py", f"# build {i}\ndef gross(net):\n    return round(net * {rate})\n")
        sb.append("CHANGELOG.txt", f"change {i}\n")
        sb.script(f'git add .\ngit commit -q -m "Change {i}"', show=False)
    sb.script("git tag v1.0.0 HEAD~29", show=False)


def check(sb):
    if sb.path(".git/BISECT_LOG").exists():
        yield "a bisect session is still running: git bisect reset"
    if sb.git("rev-parse", "--abbrev-ref", "HEAD") != "main":
        yield "you should be back on main"
    if not sb.path("answer.txt").exists():
        yield "write the first bad commit ID into answer.txt"
        return
    answer = sb.read("answer.txt").strip().split()[0] if sb.read("answer.txt").strip() else ""
    bad = sb.git("rev-list", "--reverse", "main").split()[BAD - 1]
    if len(answer) < 7 or not bad.startswith(answer):
        yield "answer.txt doesn't contain the first bad commit (look for the line \"<id> is the first 'bad' commit\")"


if __name__ == "__main__":
    exercise(NUMBER, "Find the commit that broke the prices", TASK, setup, check)
