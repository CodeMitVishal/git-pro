"""Module 4 · Merge conflicts: when both branches changed the same lines

Git merges different lines automatically. When BOTH sides changed the SAME lines,
it stops and asks you. The file then contains conflict markers:

  <<<<<<< HEAD
  your branch's version
  =======
  the other branch's version
  >>>>>>> feature

To resolve: edit the file to the final content (remove the markers),
git add it, then git commit (or git merge --abort to cancel).

TEACHING NOTES
  Why it matters  Conflicts are normal in teams; resolving them calmly is a core skill.
  Picture it      Two editors changed the same sentence; Git hands you both versions and
                  asks: which one, or a mix?
  Watch out       Never commit files that still contain <<<<<<< markers. Run the tests
                  after resolving: a clean merge can still be logically wrong.
  In real jobs    Pull often and keep branches short-lived to get fewer, smaller conflicts.
  Interview       Q: How do you resolve a merge conflict?
                  A: git status shows the conflicted files; edit them to the intended result,
                     remove the markers, git add, commit; test; or abort with git merge --abort.

Run it:  python 04_branches_merging/03_merge_conflicts.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "Welcome to our shop" > banner.txt
git add banner.txt
git commit -m "Add banner"
git switch -c feature/sale
echo "Big SALE: 20% off" > banner.txt
git commit -qam "Announce sale"
git switch main
echo "Welcome! Free shipping today" > banner.txt
git commit -qam "Announce free shipping"
''', show=False)

print("--- 1. Both branches changed the same line -> CONFLICT")
sb.script('''
git merge feature/sale
git status --short
cat banner.txt
''')

print("--- 2. Resolve: write the final content, remove the markers, add, commit")
sb.write("banner.txt", "Big SALE: 20% off + free shipping today\n")
sb.script('''
cat banner.txt
git add banner.txt
git commit --no-edit
git log --oneline --graph
''')

print("--- 3. Changed your mind in the middle of a conflict? git merge --abort")
sb.script('''
git switch -c try-again HEAD~1
echo "Something else" > banner.txt
git commit -qam "Other banner"
git merge feature/sale
git merge --abort
git status --short
''')
