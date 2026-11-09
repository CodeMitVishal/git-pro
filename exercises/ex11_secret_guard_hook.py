"""Exercise 11 · A pre-commit hook that stops leaked secrets

    python exercises/ex11_secret_guard_hook.py setup
    python exercises/ex11_secret_guard_hook.py check

Stuck? Compare with solutions/ex11_secret_guard_hook.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import exercise  # noqa: E402

NUMBER = 11
TASK = """
In playground/ex11, write a pre-commit hook (.git/hooks/pre-commit) that BLOCKS any
commit whose staged changes contain "PASSWORD=" or "API_KEY=", and lets every other
commit through. Make it executable.

Tip: start the file with  #!/bin/sh  (also works with Git for Windows), use
git diff --cached | grep ... and exit 1 to block.

The check really tries two commits: one with a secret (must be blocked) and one
without (must succeed). It cleans up after itself.
"""


def setup(sb):
    sb.script('''
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
''', show=False)


def _commit(sb, name, text):
    """Stage a file and try to commit it; return (succeeded, hook output)."""
    sb.write(name, text)
    sb.git("add", name)
    before = sb.git("rev-parse", "HEAD")
    r = sb._exec(["git", "commit", "-m", f"test {name}"], {})
    ok = r.returncode == 0 and sb.git("rev-parse", "HEAD") != before
    if ok:
        sb.git("reset", "--soft", before)                 # undo the test commit
    sb.git("reset", "-q", "--", name)
    sb.path(name).unlink()
    return ok


def check(sb):
    hook = sb.path(".git/hooks/pre-commit")
    if not hook.exists():
        yield "there is no .git/hooks/pre-commit file yet"
        return
    if _commit(sb, "leak.env", "API_KEY=sk_live_123\n"):
        yield "a commit containing API_KEY= got through: the hook must block it (exit 1)"
    if _commit(sb, "leak2.env", "PASSWORD=hunter2\n"):
        yield "a commit containing PASSWORD= got through"
    if not _commit(sb, "safe.py", "print('no secrets here')\n"):
        yield "a normal commit was blocked: the hook must allow commits without secrets"


if __name__ == "__main__":
    exercise(NUMBER, "A pre-commit hook that stops leaked secrets", TASK, setup, check)
