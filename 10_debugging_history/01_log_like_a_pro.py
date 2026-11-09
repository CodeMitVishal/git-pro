"""Module 10 · git log like a detective

  git log --oneline --graph --all          the whole picture
  git log --author="Priya"                  by person
  git log --since="2 weeks ago"             by time (also --until)
  git log --grep="coupon" -i                by commit message
  git log -- src/cart.py                    commits that touched a file
  git log --follow -- cart.py               ...even across renames
  git log --format="%h %an %ar %s"          your own format
  git shortlog -sn HEAD                     commits per person

TEACHING NOTES
  Why it matters  "When did this change, who did it, and why?" is the first question in
                  every bug investigation.
  Picture it      The log is a searchable diary; the options are search filters.
  Watch out       A..B ranges and path filters combine: git log main..feature -- api/
  In real jobs    Finding which release introduced a change; preparing release notes.
  Interview       Q: How do you find all commits that touched a file?
                  A: git log --follow -- path (add -p to see the changes).

Run it:  python 10_debugging_history/01_log_like_a_pro.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script("git init", show=False)
for author, path, msg in [
    ("Vishal", "cart.py", "Add cart"), ("Priya", "coupon.py", "Add coupon codes"),
    ("Vishal", "cart.py", "Fix rounding in cart"), ("Raj", "README.md", "Document coupons"),
    ("Priya", "coupon.py", "Coupon: expire after 30 days"), ("Vishal", "search.py", "Add search"),
]:
    sb.append(path, f"# {msg}\n")
    sb.script(f'git add {path}\ngit commit -q -m "{msg}" --author="{author} <{author.lower()}@example.com>"', show=False)

print("--- 1. Filter by person, message and file")
sb.script('''
git log --oneline --author=Priya
git log --oneline -i --grep=coupon
git log --oneline -- cart.py
''')

print("--- 2. Your own format, and a summary per person")
sb.script('''
git log -3 --format="%h | %an | %ad | %s" --date=format:%H:%M
git shortlog -sn HEAD
''')

print("--- 3. Time filters (the sandbox clock starts at 08:00 on 27 Oct 2026)")
sb.script('''
git log --oneline --since="2026-10-27 08:10 +0000" --until="2026-10-27 08:12 +0000"
''')
