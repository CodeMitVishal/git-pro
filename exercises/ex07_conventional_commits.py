"""Exercise 7 · Commits a reviewer will love

    python exercises/ex07_conventional_commits.py setup
    python exercises/ex07_conventional_commits.py check

Stuck? Compare with solutions/ex07_conventional_commits.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import exercise  # noqa: E402

NUMBER = 7
TASK = """
In playground/ex07 you changed three files for three different reasons:
  auth.py     a NEW feature (two-factor login)
  cart.py     a BUG fix (rounding)
  README.md   documentation

Make three separate commits, in this order, using Conventional Commits:
  1. a  feat  commit with only auth.py     e.g.  feat(auth): add two-factor login
  2. a  fix   commit with only cart.py     e.g.  fix(cart): round totals to 2 decimals
  3. a  docs  commit with only README.md   e.g.  docs: explain two-factor login

Format: type(optional-scope): summary   (lowercase type, a colon and a space, a summary
of at least 10 characters, no full stop at the end)
"""
RULE = re.compile(r"^(?P<type>feat|fix|docs)(\([a-z0-9-]+\))?!?: \S.{8,}[^.]$")


def setup(sb):
    sb.script('''
git init
echo "def login(user, pw): ..." > auth.py
echo "def total(items): return sum(items)" > cart.py
echo "# Shop" > README.md
git add .
git commit -m "Initial shop"
''', show=False)
    sb.append("auth.py", "def verify_2fa(user, code): ...\n")
    sb.write("cart.py", "def total(items): return round(sum(items), 2)\n")
    sb.append("README.md", "\nLogin now asks for a two-factor code.\n")


def check(sb):
    subjects = sb.git("log", "--format=%s", "-3").splitlines()[::-1]
    expected = [("feat", "auth.py"), ("fix", "cart.py"), ("docs", "README.md")]
    if len(subjects) < 3 or subjects[0] == "Initial shop":
        yield "make three new commits (feat, fix, docs)"
        return
    for i, (subject, (kind, file)) in enumerate(zip(subjects, expected)):
        ref = f"HEAD~{2 - i}"
        m = RULE.match(subject)
        if not m:
            yield f"'{subject}' doesn't follow type(scope): summary"
            continue
        if m["type"] != kind:
            yield f"commit {i + 1} should be a '{kind}' commit, got '{m['type']}'"
        files = sb.git("show", "--name-only", "--format=", ref).split()
        if files != [file]:
            yield f"the {kind} commit should change only {file}, it changes {files}"
    if sb.git("status", "--porcelain"):
        yield "git status is not clean"


if __name__ == "__main__":
    exercise(NUMBER, "Commits a reviewer will love", TASK, setup, check)
