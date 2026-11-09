"""Slides · Module 6 · Remotes & GitHub"""
from teach_kit import cover, interview, job, mistake, picture, recap, terminal, trace, why

M = "Module 6 · Remotes &amp; GitHub"
TEAM = '''
git init --bare ../github/shop.git
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
git remote add origin ../github/shop.git
git push -q -u origin main
git clone -q ../github/shop.git ../priya
cd ../priya
echo "def pay(): pass" > payments.py
git add payments.py
git commit -qm "Add payments"
git push -q
cd ../project
echo "def ship(): pass" > shipping.py
git add shipping.py
git commit -qm "Add shipping"
'''
SLIDES = [
 cover("06", "Remotes &amp; GitHub", "Share work with a team: clone, push, pull, fetch, and force-push safely.",
       [("clone, push, pull", "01_clone_push_pull.py"), ("fetch vs pull", "02_fetch_vs_pull.py"),
        ("Rejected pushes &amp; force", "03_rejected_push_and_force.py"), ("Exercise: sync with your team", "ex06_sync_with_team.py"),
        ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "Remotes", "Your laptop is not a team",
     "Commits on your laptop help nobody: the team can't review them, CI can't test them, and if the disk dies they're gone.",
     "A <b>remote</b> (GitHub, GitLab, Azure DevOps) is the shared copy. You <b>push</b> your commits to it and <b>pull</b> everyone else's."),

 picture(M, "Remotes", "A shared bookshelf",
     "&#128218; Everyone has a full copy at home. You <b>push</b> new pages to the shelf and <b>pull</b> pages others added. "
     "<b>origin/main</b> is your note of what the shelf looked like the last time you checked.",
     [("git clone", "copy the whole shelf home"), ("git push", "put your new pages on the shelf"),
      ("git fetch", "check the shelf, update origin/*"), ("git pull", "fetch + bring the pages into your branch")]),

 terminal(M, "Remotes", "Connect a project and push it", '''
git init --bare ../github/shop.git
git remote add origin ../github/shop.git
git remote -v
git push -u origin main
git status -sb
''', ["A bare repo plays GitHub (offline).", "<b>-u</b> links main to origin/main for later pushes/pulls.",
      "Real URL: <b>git@github.com:you/shop.git</b>."],
     setup='''
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
'''),

 terminal(M, "fetch vs pull", "fetch first, look, then integrate", '''
git fetch
git status -sb
git log --oneline main..origin/main
git pull --rebase
git log --oneline --graph
git push
''', ["<b>fetch</b> moves only origin/main.", "<b>ahead 1, behind 1</b>: both sides have new work.",
      "<b>pull --rebase</b>: linear, no merge commit."], setup=TEAM),

 trace(M, "Remotes", "Remote commands cheat sheet", ["Command", "Does"],
       [["<span class=\"m\">git clone &lt;url&gt;</span>", "copy a repository with all history"],
        ["<span class=\"m\">git remote -v</span> / <span class=\"m\">add</span> / <span class=\"m\">remove</span>", "manage remote names and URLs"],
        ["<span class=\"m\">git fetch --prune</span>", "download new commits, drop deleted remote branches"],
        ["<span class=\"m\">git pull --rebase</span>", "fetch + rebase your commits on top"],
        ["<span class=\"m\">git push -u origin feature/x</span>", "publish a new branch and track it"],
        ["<span class=\"m\">git push origin --delete feature/x</span>", "delete a remote branch"]]),

 terminal(M, "Rejected push", "When the remote has work you don't", '''
git push
git pull --rebase
git push
''', ["Git refuses to overwrite Priya's commit.", "Integrate first, then push.",
      "Never \"fix\" this with --force on a shared branch."], setup=TEAM),

 mistake(M, "Force push", "--force on a shared branch",
     '''
git rebase -i HEAD~3      # on main
git push --force
# Priya's pushed commits: gone from GitHub''',
     "<b>--force</b> overwrites the remote no matter what's there. Teammates' work disappears from the server.",
     '''
git switch feature/cart     # your own branch
git rebase origin/main
git push --force-with-lease
# refuses if someone pushed meanwhile''',
     "Only force-push your own branch, and always with <b>--force-with-lease</b>. Protect main on GitHub."),

 job(M, "Remotes", "Remotes at work", [
     ("Clone with SSH", '''
ssh-keygen -t ed25519 -C "you@company.com"
git clone git@github.com:company/shop.git'''),
     ("Publish your branch", '''
git push -u origin feature/SHOP-142'''),
     ("Contribute via a fork", '''
git remote add upstream git@github.com:org/proj.git
git fetch upstream && git rebase upstream/main'''),
     ("Keep things tidy", '''
git fetch --prune
git branch -vv'''),
 ]),

 interview(M, "git fetch vs git pull?",
     ["<b>fetch</b> downloads new commits and updates remote-tracking branches like <b>origin/main</b>; my branches and files don't change.",
      "<b>pull</b> = fetch + merge (or rebase with <b>--rebase</b>) into my current branch.",
      "I fetch first and look (<b>git log main..origin/main</b>), then integrate.",
      "A rejected push means the remote has work I don't have: pull --rebase, then push."],
     None,
     "\"--force vs --force-with-lease?\" (with-lease refuses to overwrite commits you haven't seen; never force shared branches)."),

 recap(M, "Module 6 in 5 lines",
     ["A remote = a shared copy; <b>origin</b> = the one you cloned.",
      "<b>push -u</b> once, then <b>push</b> / <b>pull</b>.",
      "<b>fetch</b> updates origin/*; <b>pull</b> = fetch + merge/rebase.",
      "Rejected push &#8594; <b>pull --rebase</b> &#8594; push.",
      "Force only your own branch, with <b>--force-with-lease</b>."],
     "Do <b>exercises/ex06_sync_with_team.py</b>: get Priya's commit and push yours."),
]
