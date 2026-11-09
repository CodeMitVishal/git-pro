"""Exercise 8 · Interrupted: ship a hotfix release, then get back to work

    python exercises/ex08_hotfix_release.py setup
    python exercises/ex08_hotfix_release.py check

Stuck? Compare with solutions/ex08_hotfix_release.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import exercise  # noqa: E402

NUMBER = 8
WIP_CART = "total = sum(items) - discount"
WIP_COUPON = "def coupon(code): ..."
TASK = f"""
In playground/ex08 you're on main, in the middle of coupon work: cart.py is modified
and coupon.py is a new, untracked file. Don't commit them: they aren't ready.

Urgent: the branch hotfix/rounding has a tested fix that must be released NOW.
  1. Put your unfinished work aside (including the new file).
  2. Switch to hotfix/rounding and create an ANNOTATED tag v1.2.1 on its newest commit
     (any message, e.g. "Rounding hotfix").
  3. Go back to main and bring your unfinished work back, exactly as it was.

At the end: you're on main, cart.py contains "{WIP_CART}",
coupon.py exists (still untracked), and the stash list is empty.
"""


def setup(sb):
    sb.script('''
git init
echo "total = sum(items)" > cart.py
git add cart.py
git commit -m "Add cart"
git tag -a v1.2.0 -m "Release 1.2.0"
git switch -c hotfix/rounding
echo "total = round(sum(items), 2)" > cart.py
git commit -qam "fix: round cart totals"
git switch main
''', show=False)
    sb.write("cart.py", WIP_CART + "\n")
    sb.write("coupon.py", WIP_COUPON + "\n")


def check(sb):
    if sb.git("cat-file", "-t", "v1.2.1") != "tag":
        yield "v1.2.1 should exist as an ANNOTATED tag (git tag -a)"
    elif sb.git("rev-parse", "v1.2.1^{commit}") != sb.git("rev-parse", "hotfix/rounding"):
        yield "v1.2.1 should point to the newest commit of hotfix/rounding"
    if sb.git("rev-parse", "--abbrev-ref", "HEAD") != "main":
        yield "go back to main at the end"
    if sb.git("stash", "list"):
        yield "the stash list should be empty (git stash pop)"
    if not sb.path("cart.py").exists() or sb.read("cart.py").strip() != WIP_CART:
        yield "your unfinished change in cart.py is missing"
    if not sb.path("coupon.py").exists():
        yield "your new file coupon.py is missing (did you stash with -u?)"
    if sb.git("rev-list", "--count", "main") != "1":
        yield "don't commit the unfinished work on main"


if __name__ == "__main__":
    exercise(NUMBER, "Interrupted: ship a hotfix release", TASK, setup, check)
