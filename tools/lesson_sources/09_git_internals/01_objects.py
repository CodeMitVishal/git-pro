"""Module 9 · Inside .git: blobs, trees and commits

Git is a key-value database. Every object is stored under the SHA-1 hash of its
content (newer repos can use SHA-256). There are only four object types:

  blob     the CONTENT of a file (no name!)
  tree     a folder: names -> blobs and other trees
  commit   a tree (the snapshot) + parent(s) + author + message
  tag      an annotated tag: a name + message pointing to an object

  git cat-file -t <id>   the type
  git cat-file -p <id>   the content, pretty-printed
  git hash-object file   the ID a file WOULD get

TEACHING NOTES
  Why it matters  Once you see commits as snapshots pointing to trees and parents,
                  branches, rebase, reset and reflog stop being magic.
  Picture it      A library where every book is filed under a fingerprint of its text:
                  identical text = the same fingerprint = stored once.
  Watch out       Git stores snapshots, not diffs: diffs are calculated when you ask
                  (packfiles compress similar objects on disk).
  In real jobs    Debugging weird repos, understanding why a rebase changes commit IDs.
  Interview       Q: Does Git store diffs or snapshots?
                  A: Snapshots: each commit points to a tree of the whole project;
                     unchanged files reuse the same blob, so it stays small.

Run it:  python 09_git_internals/01_objects.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "hello" > a.txt
echo "hello" > copy-of-a.txt
mkdir src
echo "print('shop')" > src/app.py
git add .
git commit -m "First snapshot"
''', show=False)

print("--- 1. A commit points to a tree, has an author and a message")
sb.script("git cat-file -p HEAD")

print("--- 2. The tree is a folder listing: names -> blobs and sub-trees")
sb.script('''
git cat-file -p HEAD^{tree}
git ls-tree -r HEAD
''')
print("a.txt and copy-of-a.txt share ONE blob: same content, stored once.\n")

print("--- 3. A blob is just the content. Its ID is the hash of that content")
blob = sb.git("rev-parse", "HEAD:a.txt")
sb.script(f'''
git cat-file -t {blob}
git cat-file -p {blob}
git hash-object a.txt
''')

print("--- 4. Change one file: the new commit reuses every unchanged object")
sb.script('''
echo "print('shop v2')" > src/app.py
git commit -qam "Update app"
git cat-file -p HEAD
git ls-tree -r HEAD
git count-objects -v
''')
