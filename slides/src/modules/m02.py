"""Slides · Module 2 · Your first repository"""
from teach_kit import cover, interview, job, mistake, picture, recap, terminal, trace, why

M = "Module 2 · Your first repository"
SLIDES = [
 cover("02", "Your first repository", "The everyday loop: edit, add, commit. Read history and keep junk out.",
       [("The three areas", "01_three_areas.md"), ("diff &amp; log", "02_diff_and_log.md"), (".gitignore", "03_gitignore.md"),
        ("Exercise: clean commits", "ex02_clean_commits/"), ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "The staging area", "Why add before commit?",
     "You fixed a bug, added debug prints and started a new feature, all in the same files. One big commit called "
     "<b>\"stuff\"</b> makes the history useless.",
     "The <b>staging area</b> lets you pick exactly what goes into each commit: <b>one commit per idea</b>."),

 picture(M, "The three areas", "Desk, box, shelf",
     "&#128230; Your <b>desk</b> is the working tree where you edit. <b>git add</b> puts things in an open <b>box</b> (the staging area). "
     "<b>git commit</b> seals the box with a label and puts it on the <b>shelf</b> (the repository).",
     [("working tree", "files you edit"), ("staging area (index)", "the next commit, being packed"),
      ("repository (.git)", "sealed commits, forever")]),

 terminal(M, "The three areas", "Follow one file through the three areas", '''
git init
echo "print('hello')" > app.py
git status --short
git add app.py
git status --short
git commit -m "Add hello app"
git status --short
''', ["<b>??</b> untracked: Git sees it, doesn't save it.", "<b>A</b> = added to the staging area.",
      "After the commit, the status is clean."]),

 terminal(M, "Partial commits", "Commit only what belongs together", '''
echo "print('hello, world')" > app.py
echo "debug notes" > notes.txt
git status --short
git add app.py
git status --short
git commit -m "Greet the whole world"
''', ["Left column = staged, right column = not staged.", "<b>notes.txt</b> stays out of the commit.",
      "Interactive picking inside a file: <b>git add -p</b>."],
     setup='''
git init
echo "print('hello')" > app.py
git add app.py
git commit -m "Add hello app"
'''),

 terminal(M, "diff", "What exactly changed?", '''
echo "pears = 5" >> cart.py
git diff
git add cart.py
git diff --staged --stat
''', ["<b>git diff</b>: changes NOT yet staged.", "<b>git diff --staged</b>: what the next commit will contain.",
      "Read your diff before every commit."],
     setup='''
git init
echo "apples = 3" > cart.py
git add cart.py
git commit -m "Add cart"
'''),

 trace(M, "History", "Reading the log", ["Command", "Shows"],
       [["<span class=\"m\">git log --oneline</span>", "one line per commit"],
        ["<span class=\"m\">git log --stat</span>", "which files changed in each commit"],
        ["<span class=\"m\">git log -p -- cart.py</span>", "every change to one file"],
        ["<span class=\"m\">git show HEAD</span>", "the last commit: message + diff"],
        ["<span class=\"m\">git log --oneline --graph --all</span>", "branches as a picture (Module 4)"]]),

 terminal(M, ".gitignore", "Keep junk and secrets out", '''
git status --short --untracked-files=all
echo ".env" > .gitignore
echo "*.log" >> .gitignore
echo "__pycache__/" >> .gitignore
git status --short --untracked-files=all
git check-ignore -v server.log
''', ["Patterns: names, <b>*.log</b>, folders with <b>/</b>.", "<b>check-ignore -v</b> tells you which rule matched.",
      "Templates: github.com/github/gitignore."],
     setup='''
git init
echo "print('shop')" > app.py
echo "DB_PASSWORD=secret123" > .env
echo "error at 12:01" > server.log
mkdir __pycache__
echo "bytecode" > __pycache__/app.pyc
'''),

 mistake(M, ".gitignore", "Ignoring a file that is already tracked",
     '''
git add settings.ini
git commit -m "Add app"
echo "settings.ini" >> .gitignore
# settings.ini is STILL tracked''',
     "<b>.gitignore</b> only affects <b>untracked</b> files. Once committed, a file stays tracked.",
     '''
git rm --cached settings.ini
git commit -m "Stop tracking settings.ini"
# the file stays on disk, Git forgets it''',
     "<b>git rm --cached</b> removes it from the index only. A leaked secret is still in history: rotate it."),

 job(M, "Everyday Git", "The loop you'll run 20 times a day", [
     ("See where you are", '''
git status -sb'''),
     ("Review before committing", '''
git diff
git add -p'''),
     ("Commit one idea", '''
git commit -m "Fix rounding in coupon total"'''),
     ("Check the result", '''
git log --oneline -5'''),
 ]),

 interview(M, "What is the staging area, and why does it exist?",
     ["The staging area (index) is the <b>snapshot being prepared</b> for the next commit.",
      "<b>git add</b> copies changes into it; <b>git commit</b> saves it as a commit.",
      "It lets you commit <b>part</b> of your work: focused commits that are easy to review and revert.",
      "<b>git diff</b> shows unstaged changes; <b>git diff --staged</b> shows staged ones."],
     None,
     "\"A file is in .gitignore but still tracked: why?\" (it was committed before; use git rm --cached)."),

 recap(M, "Module 2 in 5 lines",
     ["Working tree &#8594; <b>git add</b> &#8594; staging area &#8594; <b>git commit</b> &#8594; repository.",
      "<b>git status -s</b>: ?? untracked, A added, M modified.",
      "<b>git diff</b> vs <b>git diff --staged</b>.",
      "<b>git log --oneline</b>, <b>--stat</b>, <b>-p</b>, <b>git show</b>.",
      "<b>.gitignore</b> for junk and secrets; <b>git rm --cached</b> for tracked files."],
     "Do <b>exercises/ex02_clean_commits/</b>: three focused commits and a .gitignore."),
]

from visuals import add_visuals  # noqa: E402
SLIDES = add_visuals(2, SLIDES)
