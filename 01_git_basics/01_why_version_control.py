"""Module 1 · Why version control? Snapshots instead of final_v2_REALLY_final.py

Without version control people copy files: app_old.py, app_backup.py,
app_final_v2.py. Nobody knows which one is current, what changed, or why.

Git saves SNAPSHOTS of your whole project. Each snapshot (a commit) records
WHAT changed, WHO changed it, WHEN, and WHY (the message). You can look at any
old version, compare versions, and go back, and a whole team can work in parallel.

TEACHING NOTES
  Why it matters  Every software team uses Git. "Do you know Git?" is assumed, not asked.
  Picture it      A photo album of your project: every commit is a photo with a caption.
  Watch out       Git is not GitHub. Git is the tool on your laptop; GitHub is a website
                  that hosts Git repositories.
  In real jobs    Every change you make at work is a commit, reviewed in a pull request.
  Interview       Q: What is Git and why use it?
                  A: A distributed version control system: it tracks every change with
                     who/when/why, lets you go back, and lets many people work in parallel.

Run it:  python 01_git_basics/01_why_version_control.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()

print("--- 1. Three versions of a file, saved as three snapshots (commits)")
sb.script('''
git init
echo "price = 10" > shop.py
git add shop.py
git commit -m "Add shop with a fixed price"
echo "price = 12" > shop.py
git commit -am "Raise the price to 12"
echo "price = 12 * 1.19  # with VAT" > shop.py
git commit -am "Show prices with VAT"
''')

print("--- 2. The history: what changed, when, by whom, and why")
sb.script("git log --oneline")
sb.script('git log -1 --format="%h | %an | %ad | %s" --date=short')

print("--- 3. Look at any old version without losing the new one")
sb.script('''
git show HEAD~2:shop.py
git show HEAD~1:shop.py
cat shop.py
''')

print("--- 4. Compare two versions")
sb.script("git diff HEAD~2 HEAD")

print("Git is DISTRIBUTED: every clone has the full history, so you can work offline.")
