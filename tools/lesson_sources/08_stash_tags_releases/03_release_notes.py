"""Module 8 · What changed between two releases?

  git log v1.0.0..v1.1.0 --oneline     commits in v1.1.0 that weren't in v1.0.0
  git diff --stat v1.0.0 v1.1.0        files changed between the releases
  git shortlog -sn v1.0.0..v1.1.0      who contributed, and how much
  git log --oneline --no-merges A..B   skip merge commits

A GitHub Release = a tag + release notes (+ files to download). Release notes are
usually generated from these commands or from Conventional Commits (Module 7).

TEACHING NOTES
  Why it matters  "What's in this release?" is asked by product managers, support and
                  customers every time you ship.
  Picture it      Two bookmarks in a book; A..B means "the pages between them".
  Watch out       A..B means "reachable from B but not from A": the order matters.
  In real jobs    CI builds the changelog from git log between the last two tags.
  Interview       Q: How do you list the commits between two releases?
                  A: git log v1.0.0..v1.1.0 --oneline (two dots: in the second, not the first).

Run it:  python 08_stash_tags_releases/03_release_notes.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script("git init", show=False)
for i, (author, msg) in enumerate([
    ("Vishal", "feat: product pages"), ("Vishal", "feat: cart"), (None, "TAG v1.0.0"),
    ("Priya", "feat: coupons"), ("Vishal", "fix: rounding in cart"), ("Priya", "docs: coupon guide"),
    ("Raj", "feat: wishlist"), (None, "TAG v1.1.0"),
]):
    if author is None:
        sb.script(f'git tag -a {msg[4:]} -m "Release {msg[4:]}"', show=False)
        continue
    name = msg.split(": ")[1].split()[0] + ".txt"           # e.g. coupons.txt
    sb.append(name, msg + "\n")
    sb.script(f'git add {name}\ngit commit -q -m "{msg}" --author="{author} <{author.lower()}@example.com>"', show=False)

print("--- What's new in v1.1.0?")
sb.script('''
git log --oneline v1.0.0..v1.1.0
git diff --stat v1.0.0 v1.1.0
git shortlog -sn v1.0.0..v1.1.0
''')
