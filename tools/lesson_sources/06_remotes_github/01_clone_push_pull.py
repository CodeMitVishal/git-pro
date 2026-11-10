"""Module 6 · Remotes: clone, push, pull

A REMOTE is another copy of the repository, usually on GitHub, GitLab or Azure
DevOps. "origin" is the default name for the one you cloned from.

  git clone <url>                 copy a repository (all history) to your machine
  git remote -v                   list remotes
  git push -u origin main         send your commits; -u remembers the upstream
  git pull                        get teammates' commits (fetch + merge)

Here a BARE repository (a repo without a working folder) plays GitHub, so the
lesson runs offline. On GitHub the URL looks like git@github.com:you/repo.git.

Connecting to GitHub (one time):
  SSH    ssh-keygen -t ed25519 -C "you@example.com", add the .pub key on GitHub
  HTTPS  use a Personal Access Token or the Git Credential Manager

TEACHING NOTES
  Why it matters  Pushing is how your work reaches the team, CI and production; the remote
                  is also your backup.
  Picture it      A shared bookshelf: you take a copy home (clone), add pages, and bring
                  them back (push); you pick up others' pages (pull).
  Watch out       Pushing to someone else's repo needs permission; fork it instead (Module 7).
  In real jobs    Clone with SSH, push your branch, open a pull request.
  Interview       Q: What is origin?
                  A: The default name of the remote you cloned from; just an alias for a URL.

Run it:  python 06_remotes_github/01_clone_push_pull.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()

print("--- 1. Create 'GitHub' (a bare repo) and push your project to it")
sb.script('''
git init --bare ../github/shop.git
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
git remote add origin ../github/shop.git
git remote -v
git push -u origin main
''')

print("--- 2. A teammate clones it, commits and pushes")
sb.script('''
git clone ../github/shop.git ../priya
cd ../priya
git log --oneline
echo "def pay(): pass" > payments.py
git add payments.py
git commit -m "Add payments"
git push
''')

print("--- 3. You pull the teammate's work")
sb.script('''
cd ../project
git pull
git log --oneline
git status -sb
''')
