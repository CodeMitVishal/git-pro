"""Module 3 · git reset: move the branch back (soft, mixed, hard)

git reset <commit> moves your current branch to <commit>. The mode decides what
happens to the changes from the commits you "removed":

  --soft    keep them STAGED          (ready to commit again, e.g. squash 3 commits into 1)
  --mixed   keep them in the WORKING TREE, unstaged   (the default)
  --hard    THROW THEM AWAY           (working tree = that commit; careful!)

TEACHING NOTES
  Why it matters  reset is the power tool for rewriting LOCAL history: undo commits,
                  squash work-in-progress, start over.
  Picture it      Moving a bookmark back in a book. soft: the later pages stay on your desk
                  in a neat pile; mixed: loose on the desk; hard: into the shredder.
  Watch out       Don't reset commits that are already pushed and shared; use git revert.
                  reset --hard also deletes uncommitted work (reflog can't save that).
  In real jobs    git reset --soft HEAD~3 then one clean commit before opening a PR.
  Interview       Q: Difference between reset --soft, --mixed and --hard?
                  A: All move the branch; soft keeps changes staged, mixed keeps them
                     unstaged, hard discards them.

Run it:  python 03_undoing_things/02_reset_three_modes.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

START = '''
git init
echo "v1" > app.txt
git add app.txt
git commit -m "Version 1"
echo "v2" > app.txt
git commit -qam "Version 2"
echo "v3" > app.txt
git commit -qam "Version 3"
'''

for mode in ("--soft", "--mixed", "--hard"):
    sb = Sandbox()
    sb.script(START, show=False)
    print(f"--- git reset {mode} HEAD~2   (back from Version 3 to Version 1)")
    sb.script(f'''
git reset {mode} HEAD~2
git log --oneline
git status --short
cat app.txt
''')

print("soft: changes staged (M in the left column) | mixed: unstaged (right column) | hard: gone")
