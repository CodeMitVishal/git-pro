"""Module 6 · fetch vs pull, and remote-tracking branches

  git fetch          download new commits from the remote; your branches DON'T move.
                     They appear as remote-tracking branches like origin/main.
  git pull           git fetch + git merge origin/main (into your current branch)
  git pull --rebase  git fetch + git rebase origin/main  (no merge commit)

  git status -sb     shows "ahead 1, behind 2" compared with the upstream

TEACHING NOTES
  Why it matters  fetch lets you LOOK before you integrate; knowing ahead/behind avoids
                  surprise merges and rejected pushes.
  Picture it      fetch = the post arrives in your mailbox; pull = you open it and file it
                  into your folder straight away.
  Watch out       pull merges by default, creating "Merge branch 'main' of ..." commits;
                  many teams set pull.rebase = true.
  In real jobs    git fetch; git log --oneline main..origin/main to review incoming work.
  Interview       Q: git fetch vs git pull?
                  A: fetch downloads and updates origin/* only; pull = fetch + merge
                     (or rebase) into your current branch.

Run it:  python 06_remotes_github/02_fetch_vs_pull.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
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
git clone ../github/shop.git ../priya
cd ../priya
echo "def pay(): pass" > payments.py
git add payments.py
git commit -m "Add payments"
git push
cd ../project
echo "def ship(): pass" > shipping.py
git add shipping.py
git commit -m "Add shipping"
''', show=False)

print("--- 1. fetch: download, but don't touch your branch")
sb.script('''
git fetch
git status -sb
git log --oneline --all --graph
''')

print("--- 2. Look before you integrate: what's new on the remote?")
sb.script('''
git log --oneline main..origin/main
git diff --stat main...origin/main
''')

print("--- 3. pull --rebase: integrate without a merge commit")
sb.script('''
git pull --rebase
git log --oneline --graph
git status -sb
git push
git status -sb
''')
