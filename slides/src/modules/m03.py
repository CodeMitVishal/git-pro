"""Slides · Module 3 · Undoing things"""
from teach_kit import cover, interview, job, mistake, picture, recap, terminal, trace, why

M = "Module 3 · Undoing things"
BASE = '''
git init
echo "v1" > app.txt
git add app.txt
git commit -m "Version 1"
echo "v2" > app.txt
git commit -qam "Version 2"
echo "v3" > app.txt
git commit -qam "Version 3"
'''
SLIDES = [
 cover("03", "Undoing things", "Every mistake has an undo: restore, amend, reset, revert, and the reflog safety net.",
       [("restore &amp; amend", "01_restore_and_amend.md"), ("reset: soft, mixed, hard", "02_reset_three_modes.md"),
        ("revert &amp; reflog", "03_revert_and_reflog.md"), ("Exercise: undo three mistakes", "ex03_undo_mistakes/"),
        ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "Undo", "Mistakes are normal. Panic is optional.",
     "A broken experiment in a file, a typo in a commit message, three commits that should have been one, a bad commit "
     "already on main, a branch deleted by accident...",
     "Pick the undo by asking two questions: <b>where is the mistake</b> (file, staging, commit)? And <b>is it already shared</b>?"),

 trace(M, "Undo", "Which undo do I need?", ["Situation", "Command"],
       [["Throw away edits in a file", "<span class=\"m\">git restore app.py</span>"],
        ["Unstage a file (keep the edit)", "<span class=\"m\">git restore --staged app.py</span>"],
        ["Fix the last commit (not pushed)", "<span class=\"m\">git commit --amend</span>"],
        ["Undo local commits", "<span class=\"m\">git reset --soft | --mixed | --hard HEAD~N</span>"],
        ["Undo a commit that's already <b>shared</b>", "<span class=\"m\">git revert &lt;commit&gt;</span>"],
        ["\"I lost commits!\"", "<span class=\"m\">git reflog</span> &#8594; reset / branch to it"]],
       "Shared history (pushed main) is never rewritten: <b>revert</b> it."),

 terminal(M, "restore and amend", "Fix the last commit", '''
git add coupon.py
git commit -m "Add copuon"
git add test_coupon.py
git commit --amend -m "Add coupon with a test"
git log --oneline --stat -1
''', ["Typo and a forgotten file, fixed in one step.", "<b>--no-edit</b> keeps the old message.",
      "The ID changes: only amend <b>unpushed</b> commits."],
     setup='''
git init
echo "def total(items): return sum(items)" > cart.py
git add cart.py
git commit -m "Add cart total"
echo "def apply(code): return 0.1" > coupon.py
echo "def test_apply(): pass" > test_coupon.py
'''),

 picture(M, "reset", "reset moves the branch back",
     "&#128278; Like moving a <b>bookmark</b> back in a book. What happens to the pages after it? "
     "<b>--soft</b>: a neat pile on your desk (staged). <b>--mixed</b>: loose on the desk (unstaged). <b>--hard</b>: the shredder.",
     [("--soft", "branch moves, changes STAGED"), ("--mixed (default)", "branch moves, changes UNSTAGED"),
      ("--hard", "branch moves, changes DELETED")]),

 terminal(M, "reset", "Same reset, three modes", '''
git reset --soft HEAD~2
git status --short
git reset --mixed HEAD
git status --short
git reset --hard HEAD
git status --short
cat app.txt
''', ["After <b>--soft</b>: M in the LEFT column (staged).", "After <b>--mixed</b>: M in the RIGHT column (unstaged).",
      "After <b>--hard</b>: clean, the v3 content is gone."], setup=BASE),

 terminal(M, "revert", "Undo a shared commit safely", '''
git log --oneline
git revert --no-edit HEAD~1
git log --oneline
cat shop.txt
''', ["<b>revert</b> adds a NEW commit that does the opposite.", "History stays intact: safe for main.",
      "Undo a merge: <b>git revert -m 1 &lt;merge&gt;</b>."],
     setup='''
git init
echo "price = 10" > shop.txt
git add shop.txt
git commit -m "Add shop"
echo "price = 0" > shop.txt
git commit -qam "Change pricing"
echo "tax = 0.19" > tax.txt
git add tax.txt
git commit -qm "Add tax"
'''),

 terminal(M, "reflog", "The safety net: nothing committed is lost", '''
git reset --hard HEAD~2
git log --oneline
git reflog -3
git reset --hard HEAD@{1}
git log --oneline
''', ["<b>reflog</b> = every place HEAD has been.", "Find the commit, then reset or <b>git branch rescue &lt;id&gt;</b>.",
      "Kept ~90 days, local only."], setup=BASE),

 mistake(M, "Shared history", "Rewriting history that others have",
     '''
git reset --hard HEAD~1     # on main
git push --force
# teammates' next pull: chaos''',
     "Everyone who pulled the old commit now has history that conflicts with yours. Work gets lost or duplicated.",
     '''
git revert HEAD
git push
# history only moves forward''',
     "Rule: <b>reset/amend/rebase</b> only local commits; <b>revert</b> shared ones."),

 job(M, "Undo", "Undo at work", [
     ("Hotfix: undo yesterday's release commit", '''
git revert a1b2c3d
git push    # CI deploys the fix'''),
     ("Clean up before a pull request", '''
git reset --soft origin/main
git commit -m "Add CSV export"'''),
     ("Committed to main by mistake", '''
git branch feature/csv
git reset --hard origin/main'''),
     ("\"I lost my work!\"", '''
git reflog
git branch rescue HEAD@{3}'''),
 ]),

 interview(M, "git reset vs git revert?",
     ["<b>reset</b> moves the branch pointer back: history is rewritten. Use it only for <b>local</b> commits.",
      "<b>revert</b> creates a <b>new</b> commit that undoes an old one: history is kept, so it's safe on shared branches.",
      "reset modes: <b>--soft</b> keeps changes staged, <b>--mixed</b> unstaged, <b>--hard</b> discards them.",
      "If you lose commits: <b>git reflog</b>."],
     None,
     "\"How do you undo a pushed merge?\" (git revert -m 1 &lt;merge-commit&gt;)."),

 recap(M, "Module 3 in 5 lines",
     ["<b>restore</b> files, <b>restore --staged</b> to unstage.",
      "<b>commit --amend</b> fixes the last unpushed commit.",
      "<b>reset --soft/--mixed/--hard</b> moves the branch back.",
      "<b>revert</b> for anything already shared.",
      "<b>reflog</b> finds \"lost\" commits."],
     "Do <b>exercises/ex03_undo_mistakes/</b>: three mistakes, three undos."),
]

from visuals import add_visuals  # noqa: E402
SLIDES = add_visuals(3, SLIDES)
