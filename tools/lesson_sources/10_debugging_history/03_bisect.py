"""Module 10 · git bisect: binary search for the commit that broke something

"It worked in v1.0, it's broken now, and there are 200 commits in between."
bisect asks you good/bad about the middle commit, halves the range, and finds the
first bad commit in about log2(200) = 8 steps.

  git bisect start
  git bisect bad                 the current commit is broken
  git bisect good v1.0.0         this one was fine
  ...test, then: git bisect good / git bisect bad ...
  git bisect reset               back to where you started

  git bisect run <test command>  fully automatic: exit code 0 = good, 1-127 = bad
                                 (here: sh check_price.sh, a one-line grep)

TEACHING NOTES
  Why it matters  It turns a day of guessing into minutes, even in histories you don't know.
  Picture it      The number-guessing game: "higher or lower?" halves the possibilities
                  each time.
  Watch out       Always finish with git bisect reset. And the test must be reliable:
                  a flaky test sends bisect the wrong way.
  In real jobs    A regression found in production: bisect between the last good release
                  tag and HEAD with a small script that reproduces it.
  Interview       Q: How do you find which commit introduced a bug?
                  A: git bisect between a known good and bad commit, ideally with
                     git bisect run and a test that reproduces the bug.

Run it:  python 10_debugging_history/03_bisect.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

SETUP_MD = r"""
git init
printf '#!/bin/sh\ngrep -q "1.19" price.txt\n' > check_price.sh
for i in $(seq 1 16); do
  if [ $i -ge 11 ]; then rate=1.91; else rate=1.19; fi   # change 11 swaps two digits: the bug
  echo "gross = net * $rate" > price.txt
  echo "change $i" >> CHANGELOG.txt
  git add . && git commit -q -m "Change $i"
done
git tag v1.0.0 HEAD~15
"""

sb = Sandbox()
sb.script("git init", show=False)
sb.write("check_price.sh", '#!/bin/sh\ngrep -q "1.19" price.txt\n')
for i in range(1, 17):
    rate = "1.91" if i >= 11 else "1.19"                  # commit 11 swaps two digits: the bug
    sb.write("price.txt", f"gross = net * {rate}\n")
    sb.append("CHANGELOG.txt", f"change {i}\n")
    sb.script(f'git add .\ngit commit -q -m "Change {i}"', show=False)
sb.script("git tag v1.0.0 HEAD~15", show=False)

print("--- 1. 16 commits; v1.0.0 (the first) was fine, HEAD is broken")
sb.script('''
git log --oneline -3
cat price.txt
git bisect start HEAD v1.0.0
''')

print("--- 2. Let Git find it: run the check script on each step automatically")
sb.script('''
git bisect run sh check_price.sh
git bisect reset
''')
print("Found in 4 steps instead of checking 16 commits one by one.")
