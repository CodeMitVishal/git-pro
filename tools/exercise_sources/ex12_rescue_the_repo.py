"""Exercise 12 · Capstone: rescue the repository and ship a release

    python exercises/ex12_rescue_the_repo.py setup
    python exercises/ex12_rescue_the_repo.py check

Stuck? Compare with solutions/ex12_rescue_the_repo.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from sandbox import exercise  # noqa: E402

NUMBER = 12
TASK = """
playground/ex12 contains origin.git (plays GitHub), me/ (YOUR clone) and teammate/.
Work in playground/ex12/me. The situation:
  - You committed "Add wishlist" directly on main by mistake (not pushed yet).
  - That commit also contains debug.log, which must never be committed.
  - Meanwhile your teammate pushed "fix: round totals" to origin/main.

Make it right:
  1. main must equal origin/main (with the teammate's fix) and must NOT contain your commit.
  2. Your work goes on a branch feature/wishlist, on top of the latest main,
     and NO commit on that branch may contain debug.log.
  3. Push feature/wishlist to origin.
  4. Release: create an ANNOTATED tag v1.3.0 on the latest main and push the tag.
  5. Leave a clean working tree.

Tip: make a safety branch first (git branch backup) and look before every step.
"""


def setup(sb):
    sb.script('''
git init --bare origin.git
git clone -q origin.git teammate
cd teammate
echo "# Shop" > README.md
echo "total = sum(items)" > cart.py
git add .
git commit -m "Initial commit"
git push -q -u origin main
cd ..
git clone -q origin.git me
cd teammate
echo "total = round(sum(items), 2)" > cart.py
git commit -qam "fix: round totals"
git push -q
cd ../me
echo "wishlist = []" > wishlist.py
echo "DEBUG 12:01 something" > debug.log
git add .
git commit -m "Add wishlist"
''', show=False)


def check(sb):
    me, origin = ["-C", "me"], ["-C", "origin.git"]
    origin_main = sb.git(*origin, "rev-parse", "main")
    origin_subjects = sb.git(*origin, "log", "--format=%s", "main").splitlines()
    if "fix: round totals" not in origin_subjects:
        yield "origin/main lost the teammate's 'fix: round totals'"
    if "Add wishlist" in origin_subjects:
        yield "'Add wishlist' ended up on origin/main: it belongs on feature/wishlist"
    if sb.git(*me, "rev-parse", "main") != origin_main:
        yield "your local main should be exactly origin/main"
    feature = sb.git(*me, "rev-parse", "--verify", "-q", "feature/wishlist")
    if not feature:
        yield "branch feature/wishlist is missing in your clone"
        return
    if "Add wishlist" not in sb.git(*me, "log", "--format=%s", "main..feature/wishlist").splitlines():
        yield "feature/wishlist should contain your 'Add wishlist' commit"
    if sb.git(*me, "merge-base", "main", "feature/wishlist") != origin_main:
        yield "feature/wishlist should sit on top of the latest main (rebase it)"
    if "debug.log" in sb.git(*me, "log", "--name-only", "--format=", "main..feature/wishlist").split():
        yield "a commit on feature/wishlist still contains debug.log (remove it and amend)"
    if sb.git(*origin, "rev-parse", "--verify", "-q", "feature/wishlist") != feature:
        yield "push feature/wishlist to origin (and push again after rewriting it)"
    if sb.git(*origin, "cat-file", "-t", "v1.3.0") != "tag":
        yield "origin needs an ANNOTATED tag v1.3.0 (git tag -a, then git push origin v1.3.0)"
    elif sb.git(*origin, "rev-parse", "v1.3.0^{commit}") != origin_main:
        yield "v1.3.0 should point to the latest main"
    if sb.git(*me, "status", "--porcelain"):
        yield "your working tree in me/ is not clean"


if __name__ == "__main__":
    exercise(NUMBER, "Capstone: rescue the repository and ship a release", TASK, setup, check)
