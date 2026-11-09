"""Module 11 · Reusing another repository: submodules (and subtree)

A SUBMODULE is a pointer from your repo to a specific commit of another repo,
checked out in a sub-folder.

  git submodule add <url> libs/logger         add it (creates .gitmodules)
  git clone --recurse-submodules <url>        clone with submodules
  git submodule update --init --recursive     fetch them after a normal clone
  git submodule update --remote               move to the library's newest commit

Alternatives: a git SUBTREE copies the other repo's files (and optionally history)
into a folder: simpler for users, harder to send changes back. Usually best of all:
a normal package (pip, npm) with a version number.

TEACHING NOTES
  Why it matters  Shared code (design systems, SDKs, infra modules) has to live somewhere.
  Picture it      A submodule is a bookmark to page N of someone else's book, glued into
                  your book; it doesn't follow their later pages until you move it.
  Watch out       Forgetting --recurse-submodules gives you empty folders; and a submodule
                  sits in detached HEAD at the pinned commit.
  In real jobs    Pinned Terraform modules or a shared protocol definitions repo.
  Interview       Q: Submodule vs subtree vs package?
                  A: Submodule = a pinned pointer to another repo; subtree = a copy merged into
                     yours; a package = versioned dependency, usually the cleanest.

Run it:  python 11_advanced_git/03_submodules_and_subtree.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init ../logger
cd ../logger
echo "def log(msg): print(msg)" > logger.py
git add logger.py
git commit -m "Logger v1"
cd ../project
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
''', show=False)

print("--- 1. Add the logger repository as a submodule")
sb.script('''
git submodule add ../logger libs/logger
cat .gitmodules
git status --short
git commit -qm "Add logger submodule"
git submodule status
''')

print("--- 2. The library moves on; your repo stays pinned until you update it")
sb.script('''
cd ../logger
echo "def warn(msg): print('WARN', msg)" >> logger.py
git commit -qam "Logger v2: add warn"
cd ../project
git submodule status
git submodule update --remote libs/logger
git status --short
git commit -qam "Update logger to v2"
git submodule status
''')

print("--- 3. Clone a project that has submodules")
sb.script('''
cd ..
git clone -q --recurse-submodules project shop-copy
cd shop-copy
git submodule status
cat libs/logger/logger.py
''')
