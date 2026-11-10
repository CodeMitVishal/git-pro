"""Module 3 · Safe undo for shared history (revert) and the safety net (reflog)

  git revert <commit>   makes a NEW commit that undoes <commit>. History is kept,
                        so it's safe on branches others have pulled (main!).
  git reflog            a diary of where HEAD has been. "Lost" commits after a
                        reset or a deleted branch are still there for ~90 days.

TEACHING NOTES
  Why it matters  On shared branches you must never rewrite history; and almost nothing
                  committed is ever truly lost if you know reflog.
  Picture it      revert = a correction notice printed in the next issue of a newspaper;
                  reflog = the CCTV recording of everything HEAD did.
  Watch out       reflog is local only (not pushed) and can't recover work that was never
                  committed. Commit often!
  In real jobs    Production bug from yesterday's merge -> git revert it, push, deploy.
  Interview       Q: reset vs revert?
                  A: reset moves the branch and rewrites history (local only); revert adds
                     a new undo commit and is safe for shared branches.

Run it:  python 03_undoing_things/03_revert_and_reflog.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "price = 10" > shop.txt
git add shop.txt
git commit -m "Add shop"
echo "price = 0" > shop.txt
git commit -qam "Change pricing"
echo "tax = 0.19" > tax.txt
git add tax.txt
git commit -qm "Add tax"
''', show=False)

print("--- 1. 'Change pricing' broke production. Undo it WITHOUT rewriting history")
sb.script('''
git log --oneline
git revert --no-edit HEAD~1
git log --oneline
cat shop.txt
''')

print("--- 2. Disaster: reset --hard threw away 3 commits...")
sb.script('''
git reset --hard HEAD~3
git log --oneline
''')

print("--- 3. ...reflog remembers where HEAD was. Jump back:")
sb.script('''
git reflog -5
git reset --hard HEAD@{1}
git log --oneline
''')

print("--- 4. A deleted branch can be brought back too")
sb.script('''
git switch -c experiment
echo "banner = True" > banner.txt
git add banner.txt
git commit -m "Try discount banner"
git switch main
git branch -D experiment
git reflog -3
git branch experiment HEAD@{1}
git log --oneline -1 experiment
''')
