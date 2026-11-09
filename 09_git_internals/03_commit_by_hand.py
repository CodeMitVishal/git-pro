"""Module 9 · Build a commit by hand with plumbing commands

The everyday commands (add, commit, branch) are "porcelain". Underneath, Git uses
small "plumbing" commands. Doing a commit with them shows exactly what git commit does:

  1. git hash-object -w file          store the content as a blob      -> blob ID
  2. git update-index --add ...       put blob + name in the index
  3. git write-tree                   turn the index into a tree       -> tree ID
  4. git commit-tree <tree> -p <parent> -m "msg"                       -> commit ID
  5. git update-ref refs/heads/main <commit>   move the branch to it

TEACHING NOTES
  Why it matters  If you can explain these five steps, you understand Git better than
                  most people who use it every day.
  Picture it      Building furniture from parts instead of buying it assembled:
                  boards (blobs) -> frame (tree) -> labelled product (commit) -> shelf (ref).
  Watch out       Plumbing doesn't protect you: update-ref will move a branch anywhere.
  In real jobs    Plumbing is used in scripts, hooks and CI tools (rev-parse, cat-file, ls-tree).
  Interview       Q: What happens when you run git commit?
                  A: Git writes the index as a tree, creates a commit object pointing to
                     that tree and the parent, then moves the current branch to it.

Run it:  python 09_git_internals/03_commit_by_hand.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
''', show=False)

print("--- 1. Store the content as a blob")
sb.write("hand.txt", "made with plumbing\n")
sb.script("git hash-object -w hand.txt")
blob = sb.git("hash-object", "-w", "hand.txt")

print("--- 2. Put it in the index under a name, 3. write the index as a tree")
sb.script(f'''
git update-index --add --cacheinfo 100644,{blob},hand.txt
git write-tree
''')
tree = sb.git("write-tree")

print("--- 4. Create the commit object (parent = current main)")
parent = sb.git("rev-parse", "HEAD")
line = f'git commit-tree {tree} -p {parent[:7]} -m "Built by hand"'
commit = sb.run(line)                       # run it ONCE and keep the new commit ID
print(f"$ {line}\n{commit}\n")

print("--- 5. Move the branch to the new commit")
sb.script(f'''
git update-ref refs/heads/main {commit}
git log --oneline
git show --stat HEAD
git status --short
''')
print("Exactly what 'git add hand.txt && git commit -m ...' would have done.")
