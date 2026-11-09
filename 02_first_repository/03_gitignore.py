"""Module 2 · .gitignore: keep junk and secrets out of Git

A .gitignore file lists patterns Git should NOT track:

  .env              secrets (passwords, API keys)
  __pycache__/      generated files
  *.log             logs
  .venv/            virtual environments
  !keep.log         ! = an exception: DO track this one

TEACHING NOTES
  Why it matters  A pushed .env file leaks passwords to everyone who can see the repo.
  Picture it      A bouncer list at the door: anything matching the list doesn't get in.
  Watch out       .gitignore only affects UNTRACKED files. A file already committed stays
                  tracked until you run git rm --cached <file>.
  In real jobs    Every project has a .gitignore (github.com/github/gitignore has templates).
  Interview       Q: You added a file to .gitignore but Git still tracks it. Why?
                  A: It was already tracked; remove it from the index with git rm --cached
                     and commit.

Run it:  python 02_first_repository/03_gitignore.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script("git init", show=False)

print("--- 1. A project with junk next to the code")
sb.script('''
echo "print('shop')" > app.py
echo "DB_PASSWORD=secret123" > .env
echo "error at 12:01" > server.log
mkdir __pycache__
echo "bytecode" > __pycache__/app.cpython-312.pyc
git status --short --untracked-files=all
''')

print("--- 2. Add a .gitignore: the junk disappears from git status")
sb.script('''
echo ".env" > .gitignore
echo "*.log" >> .gitignore
echo "__pycache__/" >> .gitignore
git status --short --untracked-files=all
git check-ignore -v server.log
''')

print("--- 3. The classic trap: a file committed BEFORE it was ignored")
sb.script('''
echo "API_KEY=abc" > settings.ini
git add settings.ini app.py .gitignore
git commit -m "Add app"
echo "settings.ini" >> .gitignore
echo "API_KEY=new" > settings.ini
git status --short
git rm --cached settings.ini
git commit -am "Stop tracking settings.ini"
git status --short
''')
print("The old API_KEY is still in the history: a leaked secret must be rotated (Module 11).")
