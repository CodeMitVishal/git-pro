"""Module 2 · The three areas: working tree -> staging area -> repository

  working tree   the files you edit
  staging area   what goes into the NEXT commit   (git add puts it here)
  repository     the saved snapshots              (git commit saves it here)

git status tells you, for every file, which area it's in.

TEACHING NOTES
  Why it matters  The staging area lets you commit PART of your work: one clean commit
                  per idea, even if you changed five things.
  Picture it      Packing a parcel: the desk (working tree), the open box (staging),
                  the sealed, labelled parcel on the shelf (commit).
  Watch out       git commit only saves what you staged; changes made after git add need
                  another git add.
  In real jobs    "Commit only the fix, not the debug prints" is a daily habit.
  Interview       Q: What is the staging area (index)?
                  A: The snapshot being prepared for the next commit; git add copies changes
                     into it, git commit saves it.

Run it:  python 02_first_repository/01_three_areas.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script("git init", show=False)

print("--- 1. A new file is UNTRACKED: Git sees it but doesn't save it")
sb.script('''
echo "print('hello')" > app.py
git status --short
''')

print("--- 2. git add puts it in the STAGING AREA (?? -> A)")
sb.script('''
git add app.py
git status --short
''')

print("--- 3. git commit saves the staged snapshot in the REPOSITORY")
sb.script('''
git commit -m "Add hello app"
git status --short
git log --oneline
''')

print("--- 4. Edit two files, but commit only one of them")
sb.script('''
echo "print('hello, world')" > app.py
echo "debug notes" > notes.txt
git status --short
git add app.py
git status --short
git commit -m "Greet the whole world"
git status --short
''')

print("Status codes:  ?? untracked   A added   M modified (left column = staged, right = not staged)")
