"""Exercise 2 · Clean commits and a .gitignore

    python exercises/ex02_clean_commits.py setup
    python exercises/ex02_clean_commits.py check

Stuck? Compare with solutions/ex02_clean_commits.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from sandbox import exercise  # noqa: E402

NUMBER = 2
TASK = """
playground/ex02 is a repository with one commit. You changed several things since:
cart.py and README.md are modified, and there are new files .env, debug.log and coupon.py.

  1. Create a .gitignore so that .env and every *.log file are ignored. Commit it alone:
     message "Add gitignore".
  2. Commit the cart.py change together with the new coupon.py: message "Add coupons".
  3. Commit the README.md change on its own: message "Document coupons".

At the end: three new commits in that order, a clean git status, and .env never committed.
"""


def setup(sb):
    sb.script('''
git init
echo "items = []" > cart.py
echo "# Shop" > README.md
git add .
git commit -m "Initial shop"
''', show=False)
    sb.write("cart.py", "items = []\ncoupon = None\n")
    sb.write("README.md", "# Shop\n\nNow with coupons.\n")
    sb.write("coupon.py", "def apply(code): return 0.1\n")
    sb.write(".env", "STRIPE_KEY=sk_live_123\n")
    sb.write("debug.log", "debug output\n")


def check(sb):
    subjects = sb.git("log", "--format=%s", "-4").splitlines()
    if subjects[:3] != ["Document coupons", "Add coupons", "Add gitignore"]:
        yield f"the last three commits should be (oldest first) Add gitignore, Add coupons, Document coupons; got {subjects[:3][::-1]}"
        return
    def files(ref):
        return set(sb.git("show", "--name-only", "--format=", ref).split())
    if files("HEAD~2") != {".gitignore"}:
        yield "'Add gitignore' should change only .gitignore"
    if files("HEAD~1") != {"cart.py", "coupon.py"}:
        yield "'Add coupons' should contain cart.py and coupon.py only"
    if files("HEAD") != {"README.md"}:
        yield "'Document coupons' should contain README.md only"
    if ".env" in sb.git("log", "--all", "--name-only", "--format="):
        yield ".env was committed somewhere: secrets must never be committed"
    if sb.git("status", "--porcelain"):
        yield "git status is not clean (is something not ignored or not committed?)"


if __name__ == "__main__":
    exercise(NUMBER, "Clean commits and a .gitignore", TASK, setup, check)
