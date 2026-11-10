"""Module 9 · Refs and HEAD: names for commits

  refs/heads/main        a branch: a file with a commit ID
  refs/tags/v1.0.0       a tag
  refs/remotes/origin/x  a remote-tracking branch
  HEAD                   usually "ref: refs/heads/main" (a SYMBOLIC ref)
  detached HEAD          HEAD contains a commit ID directly (no branch)

Commit expressions:
  HEAD~1  (= HEAD~)   the first parent        HEAD~3  three generations back
  HEAD^2              the SECOND parent (of a merge commit)
  main@{1}            where main was one move ago (reflog)

TEACHING NOTES
  Why it matters  Every command that takes a commit (reset, diff, log, rebase) accepts
                  these names; and "detached HEAD" stops being scary.
  Picture it      Refs are signposts with a commit ID written on them; HEAD is the
                  "you are here" marker standing next to one of the signposts.
  Watch out       Commits made in detached HEAD belong to no branch: create one
                  (git switch -c) before you leave, or find them later in the reflog.
  In real jobs    git switch --detach v1.2.0 to test an old release.
  Interview       Q: What is a detached HEAD?
                  A: HEAD points directly at a commit instead of a branch; new commits
                     there aren't on any branch unless you create one.

Run it:  python 09_git_internals/02_refs_and_head.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "v1" > app.txt
git add app.txt
git commit -m "Version 1"
git tag v1.0.0
echo "v2" > app.txt
git commit -qam "Version 2"
echo "v3" > app.txt
git commit -qam "Version 3"
''', show=False)

print("--- 1. Branches, tags and HEAD are tiny text files")
sb.script('''
cat .git/HEAD
cat .git/refs/heads/main
git symbolic-ref HEAD
git show-ref
''')

print("--- 2. Naming commits relative to HEAD")
sb.script('''
git rev-parse --short HEAD
git rev-parse --short HEAD~1
git log -1 --format=%s HEAD~2
''')

print("--- 3. Detached HEAD: looking at an old version")
sb.script('''
git switch --detach v1.0.0
cat .git/HEAD
git status
echo "experiment" > app.txt
git commit -qam "Experiment on old version"
git switch -c experiment-on-v1
git log --oneline --all --graph
''')
