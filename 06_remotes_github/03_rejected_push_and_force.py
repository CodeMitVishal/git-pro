"""Module 6 · Rejected pushes, --force and --force-with-lease

If the remote has commits you don't have, git push is REJECTED (non-fast-forward):
Git refuses to throw away your teammate's work. Fix: pull (rebase), then push.

After rewriting YOUR OWN branch (rebase, amend), a normal push is also rejected.
Then you must force-push:

  git push --force             overwrite the remote, no questions asked (dangerous)
  git push --force-with-lease  overwrite ONLY if the remote is still where you last
                               saw it; if someone pushed meanwhile, it refuses

TEACHING NOTES
  Why it matters  A careless --force deletes teammates' commits from the server.
  Picture it      --force-with-lease = "replace this page, but only if nobody edited it
                  since I last looked".
  Watch out       Never force-push main or other shared branches; protect them on GitHub
                  (branch protection rules).
  In real jobs    After rebasing your PR branch: git push --force-with-lease.
  Interview       Q: Why --force-with-lease instead of --force?
                  A: It refuses to overwrite commits on the remote that you haven't seen,
                     so you can't silently delete a teammate's work.

Run it:  python 06_remotes_github/03_rejected_push_and_force.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init --bare ../github/shop.git
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
git remote add origin ../github/shop.git
git push -u origin main
git switch -c feature/cart
echo "cart v1" > cart.txt
git add cart.txt
git commit -m "Add cart"
git push -u origin feature/cart
git clone ../github/shop.git ../priya
''', show=False)

print("--- 1. Priya pushed to main meanwhile -> your push to main is rejected")
sb.script('''
cd ../priya
echo "def pay(): pass" > payments.py
git add payments.py
git commit -qm "Add payments"
git push
cd ../project
git switch main
echo "footer" > footer.txt
git add footer.txt
git commit -qm "Add footer"
git push
''')

print("--- 2. The fix: integrate first, then push")
sb.script('''
git pull --rebase
git push
''')

print("--- 3. You amended YOUR feature branch -> a force push is needed")
sb.script('''
git switch feature/cart
echo "cart v2" > cart.txt
git commit -q -a --amend --no-edit
git push
''')

print("--- 4. ...but a reviewer pushed a commit to your branch first. --force-with-lease protects it")
sb.script('''
cd ../priya
git fetch -q
git switch feature/cart
echo "review note" > review.txt
git add review.txt
git commit -qm "Add review note"
git push
cd ../project
git push --force-with-lease
''')
print("Rejected: 'stale info'. Fetch, look at the new commit, rebase onto it, then push again.")
