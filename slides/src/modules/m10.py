"""Slides · Module 10 · Debugging with history"""
import pathlib
import sys

from teach_kit import cover, interview, job, mistake, picture, recap, terminal, trace, why

M = "Module 10 · Debugging with history"
PY = pathlib.Path(sys.executable).as_posix()


def team_log(sb):
    sb.script("git init", show=False)
    for author, path, msg in [("Vishal", "cart.py", "Add cart"), ("Priya", "coupon.py", "Add coupon codes"),
                              ("Vishal", "cart.py", "Fix rounding in cart"), ("Raj", "README.md", "Document coupons"),
                              ("Priya", "coupon.py", "Coupon: expire after 30 days"), ("Vishal", "search.py", "Add search")]:
        sb.append(path, f"# {msg}\n")
        sb.script(f'git add {path}\ngit commit -q -m "{msg}" --author="{author} <{author.lower()}@example.com>"', show=False)


def cart_history(sb):
    sb.script("git init", show=False)
    for author, msg, lines in [
        ("Vishal", "Add cart", ["def total(items):", "    return sum(items)"]),
        ("Priya", "Add discount", ["def total(items, discount=0):", "    rate = 1 - discount", "    return sum(items) * rate"]),
        ("Raj", "Cap discount at 50%", ["def total(items, discount=0):", "    rate = 1 - min(discount, 0.5)", "    return sum(items) * rate"])]:
        sb.write("cart.py", "\n".join(lines) + "\n")
        sb.script(f'git add cart.py\ngit commit -q -m "{msg}" --author="{author} <{author.lower()}@example.com>"', show=False)


def sixteen(sb):
    sb.script("git init", show=False)
    sb.write("check_price.py", "from price import gross\nimport sys\nsys.exit(0 if gross(100) == 119 else 1)\n")
    for i in range(1, 17):
        rate = "1.91" if i >= 11 else "1.19"
        sb.write("price.py", f"# version {i}\ndef gross(net):\n    return round(net * {rate})\n")
        sb.script(f'git add .\ngit commit -q -m "Change {i}"', show=False)
    sb.script("git tag v1.0.0 HEAD~15", show=False)


SLIDES = [
 cover("10", "Debugging with history", "History is evidence: filter the log, blame a line, search with the pickaxe, and bisect a bug.",
       [("git log like a detective", "01_log_like_a_pro.py"), ("blame &amp; the pickaxe", "02_blame_and_pickaxe.py"),
        ("git bisect", "03_bisect.py"), ("Exercise: find the bug", "ex10_find_the_bug.py"), ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "Debugging", "\"It worked last week\"",
     "Prices are wrong in production. 200 commits went in since the last good release. Reading them one by one takes a day, "
     "and you don't even know which file to look at.",
     "Git history is <b>evidence</b>. Filter it (<b>log</b>), trace a line (<b>blame</b>, <b>-S</b>), and let <b>bisect</b> find the culprit in ~8 steps."),

 terminal(M, "git log", "Filter the history", '''
git log --oneline --author=Priya
git log --oneline -i --grep=coupon
git log --oneline -- cart.py
git shortlog -sn HEAD
''', ["By person, by message, by file.", "Also <b>--since</b>, <b>--until</b>, <b>--follow</b>, <b>--no-merges</b>.",
      "<b>shortlog</b>: commits per author."], before=team_log),

 terminal(M, "blame and pickaxe", "Who changed this line? When did it appear?", '''
git blame -s -L 1,3 cart.py
git log --oneline -S discount
git log --oneline -S "min("
git grep -n rate HEAD~1
''', ["<b>blame</b>: the last commit per line.", "<b>-S</b> (pickaxe): commits that added/removed the text.",
      "<b>git grep</b> searches any version."], before=cart_history),

 picture(M, "bisect", "bisect = the number-guessing game",
     "&#127919; \"I'm thinking of a number between 1 and 1,000.\" \"Higher or lower?\" Halving each time finds it in 10 guesses. "
     "bisect does the same with commits: <b>good or bad?</b>",
     [("git bisect start", "bad = HEAD, good = v1.0.0"), ("Git checks out the middle", "you test it"),
      ("good / bad", "half the commits are ruled out"), ("~log2(n) steps later", "the first bad commit")]),

 terminal(M, "bisect", "Let a script do the testing", f'''
git bisect start HEAD v1.0.0
git bisect run "{PY}" check_price.py
git bisect reset
''', ["Exit code 0 = good, 1-127 = bad, 125 = skip.", "16 commits &#8594; 4 checks.",
      "Always <b>git bisect reset</b> at the end."], before=sixteen),

 trace(M, "Debugging", "Which tool for which question?", ["Question", "Tool"],
       [["What changed recently in payments/?", "<span class=\"m\">git log --oneline --since=\"1 week ago\" -- payments/</span>"],
        ["Who wrote this odd line, and why?", "<span class=\"m\">git blame -L 40,60 file</span> &#8594; <span class=\"m\">git show &lt;id&gt;</span> &#8594; the PR"],
        ["When was this function removed?", "<span class=\"m\">git log -S \"def apply_coupon\" --oneline</span>"],
        ["Which commit broke the build?", "<span class=\"m\">git bisect run pytest -x</span>"],
        ["Is this TODO in the released version?", "<span class=\"m\">git grep TODO v2.3.0</span>"]]),

 mistake(M, "bisect", "A flaky test leads bisect astray",
     '''
git bisect run pytest
# runs the WHOLE suite: unrelated
# flaky tests fail randomly''',
     "bisect trusts every answer. One wrong \"bad\" sends it into the wrong half, and it confidently blames an innocent commit.",
     '''
git bisect run pytest tests/test_prices.py -x
# a small, reliable test that
# reproduces exactly this bug''',
     "Write a tiny, deterministic reproduction script first, then bisect with it."),

 job(M, "Debugging", "History at work", [
     ("Production regression", '''
git bisect start HEAD v2.3.0
git bisect run ./repro.sh'''),
     ("Understand a decision", '''
git blame -L 120,130 billing.py
git show a1b2c3d   # + the linked PR'''),
     ("Ignore formatting commits in blame", '''
echo <reformat-id> >> .git-blame-ignore-revs'''),
     ("Release-level history", '''
git log --first-parent --oneline main'''),
 ]),

 interview(M, "How do you find which commit introduced a bug?",
     ["<b>git bisect</b> between a known good commit (last release tag) and a bad one (HEAD).",
      "Binary search: about <b>log2(n)</b> steps, so 1,000 commits need ~10 checks.",
      "Best with <b>git bisect run</b> and a small script that reproduces the bug.",
      "Then <b>git show</b> the culprit, read its PR, write a test, fix.",
      "For a single line: <b>git blame</b>; for added/removed code: <b>git log -S</b>."],
     None,
     "\"A commit in the range doesn't build?\" (git bisect skip, or exit 125 from the script)."),

 recap(M, "Module 10 in 5 lines",
     ["<b>log</b> filters: --author, --grep, --since, -- path, --follow.",
      "<b>blame -L</b>: who last changed these lines.",
      "<b>log -S / -G</b>: when code appeared or disappeared.",
      "<b>git grep</b>: search any version.",
      "<b>bisect run</b>: the first bad commit in ~log2(n) steps."],
     "Do <b>exercises/ex10_find_the_bug.py</b>: 30 commits, one bug, bisect it."),
]
