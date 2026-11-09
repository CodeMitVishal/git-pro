"""Solution · Exercise 10: Find the commit that broke the prices

Run it:  python solutions/ex10_find_the_bug.py

What you type:
    git bisect start HEAD v1.0.0
    git bisect run python check_price.py      # prints "<id> is the first 'bad' commit"
    git bisect reset
    echo <id> > answer.txt
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402

PY = pathlib.Path(sys.executable).as_posix()


def bisect(sb):
    out = sb.script(f'git bisect start HEAD v1.0.0\ngit bisect run "{PY}" check_price.py', show=False)
    print(out)
    bad = re.search(r"([0-9a-f]{40}) is the first '?bad'? commit", out).group(1)
    sb.script("git bisect reset", show=False)
    sb.write("answer.txt", bad[:10] + "\n")
    print(sb.script("cat answer.txt", show=False))


if __name__ == "__main__":
    solve("ex10_find_the_bug.py", bisect)
