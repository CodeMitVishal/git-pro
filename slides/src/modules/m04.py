"""Slides · Module 4 · Branches & merging"""
from teach_kit import cover, interview, job, mistake, picture, recap, terminal, trace, why

M = "Module 4 · Branches &amp; merging"
FEATURE = '''
git init
echo "home page" > home.txt
git add home.txt
git commit -m "Add home page"
git switch -c feature/search
echo "search box" > search.txt
git add search.txt
git commit -m "Add search"
'''
CONFLICT = '''
git init
echo "Welcome to our shop" > banner.txt
git add banner.txt
git commit -m "Add banner"
git switch -c feature/sale
echo "Big SALE: 20% off" > banner.txt
git commit -qam "Announce sale"
git switch main
echo "Welcome! Free shipping today" > banner.txt
git commit -qam "Announce free shipping"
'''
SLIDES = [
 cover("04", "Branches &amp; merging", "Build features in parallel without breaking main, then bring the work together.",
       [("Branches are pointers", "01_branches_are_pointers.md"), ("Fast-forward vs three-way", "02_fast_forward_and_three_way.md"),
        ("Merge conflicts", "03_merge_conflicts.md"), ("Exercise: resolve a conflict", "ex04_merge_conflict/"),
        ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "Branches", "Why branches?",
     "You're halfway through a big feature when a production bug comes in. Your half-done code can't be released, "
     "and five teammates are changing the same project at the same time.",
     "A <b>branch</b> is a separate line of work. main stays releasable; each feature or fix lives on its own branch until it's merged."),

 picture(M, "Branches", "A branch is a sticky note on a commit",
     "&#128204; Commits form a timeline. A branch is just a <b>sticky note</b> with a commit ID on it; creating one copies nothing. "
     "<b>HEAD</b> is the note you're holding: new commits move that note forward.",
     [("main", "points to the release commit"), ("feature/search", "points to your newest commit"),
      ("HEAD", "points to the branch you're on"), ("new commit", "moves your branch forward")]),

 terminal(M, "Branches", "Create, commit, switch", '''
git switch -c feature/coupons
echo "coupons" > coupons.txt
git add coupons.txt
git commit -m "Add coupons"
git log --oneline --all --graph
git switch main
git ls-files
''', ["<b>switch -c</b>: create + switch in one step.", "main doesn't know about coupons.txt yet.",
      "Switching branches changes the files in your folder."],
     setup='''
git init
echo "home page" > home.txt
git add home.txt
git commit -m "Add home page"
'''),

 terminal(M, "Merging", "Fast-forward: main didn't move", '''
git switch main
git merge feature/search
git log --oneline --graph --all
''', ["Git just slides main forward.", "No merge commit: history stays a straight line."], setup=FEATURE),

 terminal(M, "Merging", "Three-way: both branches moved", '''
git switch main
echo "footer" > footer.txt
git add footer.txt
git commit -qm "Add footer"
git merge --no-edit feature/search
git log --oneline --graph --all
''', ["Git creates a <b>merge commit</b> with two parents.", "The graph shows the two lines joining.",
      "<b>--no-ff</b> forces a merge commit even when a fast-forward is possible."], setup=FEATURE),

 terminal(M, "Conflicts", "Both branches changed the same line", '''
git merge feature/sale
git status --short
cat banner.txt
''', ["<b>UU</b> = unmerged: Git needs you.", "Between <b>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</b> and <b>=======</b>: your branch (HEAD).",
      "Between <b>=======</b> and <b>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</b>: theirs."], setup=CONFLICT),

 trace(M, "Conflicts", "Resolving a conflict in 4 steps", ["Step", "Do"],
       [["1 Find", "<span class=\"m\">git status</span>: every UU file"],
        ["2 Decide", "edit the file to the final content (keep one side, the other, or a mix); delete the markers"],
        ["3 Mark resolved", "<span class=\"m\">git add banner.txt</span>"],
        ["4 Finish", "<span class=\"m\">git commit</span> (run the tests first!)"],
        ["or cancel", "<span class=\"m\">git merge --abort</span>"]],
       "VS Code shows buttons: Accept Current / Incoming / Both. Still read the result."),

 mistake(M, "Conflicts", "Committing conflict markers",
     '''
git add .
git commit -m "Merge sale"
# banner.txt now contains:
# <<<<<<< HEAD ... ======= ... >>>>>>>''',
     "The site shows raw markers, or the code doesn't even compile. It happens when you <b>git add .</b> without looking.",
     '''
git diff --check        # finds leftover markers
git grep -n "<<<<<<<"
# fix, test, then add and commit''',
     "Check for markers and run the tests before committing a resolution."),

 job(M, "Branches", "Branching at work", [
     ("One branch per ticket", '''
git switch -c feature/SHOP-142-coupons'''),
     ("Keep up with main", '''
git fetch
git merge origin/main      # or rebase (Module 5)'''),
     ("Merge through a pull request", '''
push the branch -> open PR -> review -> merge'''),
     ("Tidy up", '''
git branch --merged main
git branch -d feature/SHOP-142-coupons'''),
 ]),

 interview(M, "How do you resolve a merge conflict?",
     ["Conflicts happen when both branches changed the <b>same lines</b>.",
      "<b>git status</b> lists the conflicted files; open each one and decide the final content.",
      "Remove the <b>&lt;&lt;&lt;&lt;&lt;&lt;&lt; ======= &gt;&gt;&gt;&gt;&gt;&gt;&gt;</b> markers, <b>git add</b>, then <b>git commit</b>.",
      "Run the tests; <b>git merge --abort</b> cancels everything.",
      "Avoid them: small branches, merge main often."],
     None,
     "\"Fast-forward vs three-way merge?\" (no new commits on the target: just move the pointer; otherwise a merge commit with two parents)."),

 recap(M, "Module 4 in 5 lines",
     ["A branch = a movable pointer; HEAD = where you are.",
      "<b>git switch -c</b> to create, <b>git switch</b> to move.",
      "Fast-forward: just move the pointer. Three-way: a merge commit.",
      "Conflicts: edit, remove markers, <b>add</b>, <b>commit</b> (or <b>--abort</b>).",
      "Delete merged branches with <b>git branch -d</b>."],
     "Do <b>exercises/ex04_merge_conflict/</b>: merge dark mode and resolve the conflict."),
]

from visuals import add_visuals  # noqa: E402
SLIDES = add_visuals(4, SLIDES)
