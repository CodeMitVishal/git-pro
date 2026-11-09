"""Solution · Exercise 12: Capstone: rescue the repository and ship a release

Run it:  python solutions/ex12_rescue_the_repo.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402

COMMANDS = """
cd me
# 1. LOOK
git status -sb
git fetch
git log --oneline --graph --all
# 2. keep the commit safe on its branch, then make main = origin/main
git branch backup
git branch feature/wishlist
git reset --hard origin/main
# 3. move the feature on top of the latest main and clean the commit
git switch feature/wishlist
git rebase main
git rm --cached debug.log
echo "*.log" > .gitignore
git add .gitignore
git commit --amend --no-edit
rm debug.log
git show --stat HEAD
# 4. publish the branch
git push -u origin feature/wishlist
# 5. release from main
git switch main
git tag -a v1.3.0 -m "Release 1.3.0"
git push origin v1.3.0
git branch -D backup
git status -sb
git log --oneline --graph --all
"""

if __name__ == "__main__":
    solve("ex12_rescue_the_repo.py", COMMANDS)
