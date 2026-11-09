"""Slides · Module 12 · Capstone: rescue a messy repository"""
from teach_kit import cover, interview, job, mistake, picture, recap, terminal, trace, why

M = "Module 12 · Capstone"
MESS = '''
git init --bare ../github/shop.git
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
git remote add origin ../github/shop.git
git push -q -u origin main
git clone -q ../github/shop.git ../priya
cd ../priya
echo "total = round(sum(items), 2)" > cart.py
git add cart.py
git commit -qm "fix: round totals"
git push -q
cd ../project
echo "wishlist = []" > wishlist.py
git add wishlist.py
git commit -qm "Add wishlist"
'''
SLIDES = [
 cover("12", "Capstone: rescue a messy repo", "Look, find, plan, act: fix any broken repository calmly and ship a release.",
       [("Rescue walkthrough", "01_rescue_walkthrough.py"), ("Exercise: rescue + release", "ex12_rescue_the_repo.py"),
        ("Final exam", "QUIZ.md"), ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "Rescue", "\"Help, I broke Git!\"",
     "Committed to main by mistake. Pushed a debug file. A teammate pushed meanwhile. The release has to go out today. "
     "Typing random commands from Stack Overflow makes it worse.",
     "Use the same 4 steps every time: <b>LOOK</b>, <b>FIND</b>, <b>PLAN</b>, <b>ACT</b>. With a safety branch, every step is reversible."),

 picture(M, "Rescue", "Look, find, plan, act",
     "&#129658; Like a doctor: check the symptoms, read the history, decide on the treatment, then treat one step at a time "
     "and check after each one.",
     [("LOOK", "status -sb, log --graph --all, stash list"), ("FIND", "reflog, log origin/main..main"),
      ("PLAN", "what should each branch look like?"), ("ACT", "git branch backup, then small steps")]),

 terminal(M, "LOOK and FIND", "Diagnose the mess", '''
git fetch -q
git status -sb
git log --oneline --graph --all
git log --oneline origin/main..main
''', ["<b>ahead 1, behind 1</b>: main diverged from origin.", "My commit sits on main by mistake.",
      "The teammate's fix is on origin/main."], setup=MESS),

 terminal(M, "ACT", "Move the commit and sync with the team", '''
git branch backup
git branch feature/wishlist
git reset -q --hard origin/main
git switch -q feature/wishlist
git rebase -q main
git log --oneline --graph --all
''', ["<b>backup</b> first: free insurance.", "main = origin/main again.",
      "The feature sits on top of the latest main."], setup=MESS + "\ngit fetch -q"),

 trace(M, "Cheat sheet", "\"Oh no\" &#8594; the fix", ["Situation", "Fix"],
       [["Committed to main by mistake", "<span class=\"m\">git branch x; git reset --hard origin/main</span>"],
        ["Wrong message / forgot a file", "<span class=\"m\">git commit --amend</span>"],
        ["Bad commit already shared", "<span class=\"m\">git revert &lt;id&gt;</span>"],
        ["Lost commits", "<span class=\"m\">git reflog</span> &#8594; <span class=\"m\">git branch rescue &lt;id&gt;</span>"],
        ["Push rejected", "<span class=\"m\">git pull --rebase</span> &#8594; push"],
        ["Need to switch NOW", "<span class=\"m\">git stash -u</span> &#8594; ... &#8594; <span class=\"m\">git stash pop</span>"],
        ["Which commit broke it?", "<span class=\"m\">git bisect run &lt;test&gt;</span>"],
        ["Leaked secret", "rotate &#8594; <span class=\"m\">git filter-repo</span> &#8594; prevent"]]),

 mistake(M, "Rescue", "Panic commands",
     '''
rm -rf .git && git init      # "start fresh"
git push --force             # "make it work"
git reset --hard             # with unsaved work''',
     "These destroy history, teammates' work, or uncommitted changes, and they're the hardest mistakes to undo.",
     '''
git branch backup            # insurance first
git status -sb; git log --graph --all; git reflog
# then one small step at a time''',
     "Look first. Back up first. Small steps. Almost everything is recoverable if you don't panic."),

 job(M, "Git Pro", "You're ready for real teams", [
     ("Daily", '''
git switch -c feature/x
git add -p && git commit
git pull --rebase && git push'''),
     ("Pull requests", '''
small PRs, Conventional Commits,
rebase onto main, --force-with-lease'''),
     ("Releases", '''
git tag -a v1.3.0 -m "Release 1.3.0"
git push origin v1.3.0'''),
     ("Emergencies", '''
reflog · revert · bisect · stash'''),
 ]),

 interview(M, "You committed to main instead of a feature branch. Fix it.",
     ["Keep the work: <b>git branch feature/x</b> at the current commit.",
      "Move main back: <b>git reset --hard origin/main</b> (only if not pushed!).",
      "Continue on <b>feature/x</b>; <b>git rebase main</b> if main moved.",
      "Already pushed to shared main? <b>git revert</b> instead, and re-apply on a branch.",
      "Prevent it: protect main on GitHub."],
     None,
     "\"How do you approach a repo in a weird state?\" (look, find, plan, act, with a backup branch first)."),

 recap(M, "Git Pro in 6 lines",
     ["Commit small and often; read your diff first.",
      "Branch per task; PR + review + CI; protect main.",
      "Rebase your own branch; revert shared commits.",
      "fetch/pull --rebase; force only with --force-with-lease.",
      "reflog, bisect, blame and -S solve the hard problems.",
      "Hooks, .gitignore, .gitattributes, secret scanning from day one."],
     "Do <b>exercises/ex12_rescue_the_repo.py</b>, then the <b>final exam</b> and the <b>interview prep</b>."),
]
