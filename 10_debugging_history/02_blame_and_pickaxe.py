"""Module 10 · Who changed this line, and when did this code appear?

  git blame -L 2,4 cart.py      last commit + author for each line (lines 2-4)
  git log -S "discount" -p      the PICKAXE: commits that added or removed this text
  git log -G "rate\\s*="         commits whose diff matches a regex
  git grep -n "TODO"            search the current files (fast, respects .gitignore)
  git grep "SECRET" v1.0.0      search an old version

TEACHING NOTES
  Why it matters  To fix a bug well you need the context: which commit, which ticket,
                  and what the author intended.
  Picture it      blame = "who wrote this sentence"; pickaxe = "in which edition was this
                  word first printed (or removed)".
  Watch out       blame shows the LAST change to a line; a reformat commit hides the real
                  author: use --ignore-rev or follow up with log -S.
  In real jobs    blame a weird line -> open the commit -> read the PR -> understand why.
  Interview       Q: How do you find when a piece of code was added or removed?
                  A: git log -S "text" (pickaxe) or -G for a regex; git blame for each
                     line's last change.

Run it:  python 10_debugging_history/02_blame_and_pickaxe.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script("git init", show=False)
versions = [
    ("Vishal", "Add cart", ["def total(items):", "    return sum(items)"]),
    ("Priya", "Add discount", ["def total(items, discount=0):", "    rate = 1 - discount", "    return sum(items) * rate"]),
    ("Raj", "Cap discount at 50%", ["def total(items, discount=0):", "    rate = 1 - min(discount, 0.5)", "    return sum(items) * rate"]),
]
for author, msg, lines in versions:
    sb.write("cart.py", "\n".join(lines) + "\n")
    sb.script(f'git add cart.py\ngit commit -q -m "{msg}" --author="{author} <{author.lower()}@example.com>"', show=False)

print("--- 1. blame: who last changed each line?")
sb.script("git blame -s -L 1,3 cart.py\ngit blame --date=short -L 2,2 cart.py")

print("--- 2. The pickaxe: when did 'discount' appear? When did 'min(' appear?")
sb.script('''
git log --oneline -S discount
git log --oneline -S "min("
''')

print("--- 3. git grep: search the code, now and in the past")
sb.script('''
git grep -n rate
git grep -n rate HEAD~1
''')
