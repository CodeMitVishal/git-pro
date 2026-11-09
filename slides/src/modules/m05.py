"""Slides · Module 5 · Rebase & rewriting history"""
from teach_kit import cover, interview, job, mistake, picture, recap, snippet, terminal, trace, why

M = "Module 5 · Rebase &amp; history"
OLD_BASE = '''
git init
echo "home" > home.txt
git add home.txt
git commit -m "Add home page"
git switch -c feature/search
echo "search v1" > search.txt
git add search.txt
git commit -m "Add search box"
echo "search v2" > search.txt
git commit -qam "Add search results"
git switch main
echo "footer" > footer.txt
git add footer.txt
git commit -m "Add footer"
'''
MESSY = '''
git init
echo "shop" > shop.txt
git add shop.txt
git commit -m "Add shop"
echo "search box" > search.txt
git add search.txt
git commit -m "Add search"
echo "search boxx" > search.txt
git commit -qam "WIP"
echo "search box with results" > search.txt
git commit -qam "fix typo"
'''


def squash(sb):
    ids = sb.git("log", "--format=%h", "-3").split()[::-1]
    sb.env["GIT_SEQUENCE_EDITOR"] = sb.fake_editor(f"pick {ids[0]} Add search\nfixup {ids[1]} WIP\nfixup {ids[2]} fix typo")


SLIDES = [
 cover("05", "Rebase &amp; rewriting history", "Clean, linear history: rebase, squash, reword and cherry-pick, plus the golden rule.",
       [("rebase basics", "01_rebase_basics.py"), ("Interactive rebase", "02_interactive_rebase.py"),
        ("cherry-pick", "03_cherry_pick.py"), ("Exercise: clean up a branch", "ex05_clean_history.py"),
        ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "Rebase", "Why rewrite history?",
     "Your branch is 3 days behind main and has commits called <b>\"wip\"</b>, <b>\"fix\"</b>, <b>\"fix again\"</b>. Merging it adds noise "
     "and a tangled graph that's hard to review, bisect or revert.",
     "Before sharing, <b>rebase</b> onto the latest main and <b>squash</b> the noise: reviewers see a few clear commits in a straight line."),

 picture(M, "Rebase", "Re-planting your branch",
     "&#127793; <b>merge</b> ties two branches together with a knot (a merge commit). <b>rebase</b> cuts your commits off and "
     "<b>re-plants</b> them on the newest tip of main: same changes, new commits, straight line.",
     [("before", "feature grew from an OLD main"), ("git rebase main", "replay each feature commit on the new main"),
      ("after", "feature sits on top of main"), ("git merge", "main just fast-forwards")]),

 terminal(M, "Rebase", "Replay the feature on the latest main", '''
git log --oneline --graph --all
git switch -q feature/search
git rebase main
git log --oneline --graph --all
''', ["Before: two lines of history.", "After: one straight line.",
      "The feature commits have <b>new IDs</b>."], setup=OLD_BASE),

 trace(M, "Rebase", "merge vs rebase", ["", "merge", "rebase"],
       [["History", "true history, with merge commits", "linear, as if you started later"],
        ["Rewrites commits?", "no", "<b>yes</b>: new IDs"],
        ["Safe on shared branches?", "yes", "<b>no</b>: only your own commits"],
        ["Conflicts", "once, at the merge", "possibly once per replayed commit"],
        ["Typical use", "merging a PR into main", "updating your feature branch before a PR"]],
       "<b>Golden rule</b>: never rebase commits that other people already pulled."),

 snippet(M, "Interactive rebase", "git rebase -i: edit your history like a draft", '''
# git rebase -i HEAD~3   opens this todo list:
pick  8510441 Add search
fixup 0a937f5 WIP
fixup 4f5af1c fix typo

# pick   = keep          reword = new message
# squash = melt + keep the message
# fixup  = melt + drop the message
# drop   = delete        (reorder lines to reorder commits)''',
     ["Edit the words, save, close: Git rewrites the commits.", "Oldest commit at the TOP.",
      "Abort any time: <b>git rebase --abort</b>."]),

 terminal(M, "Interactive rebase", "Three commits become one", '''
git log --oneline
git rebase -i HEAD~3
git log --oneline
''', ["Here a tiny script plays you editing the todo list.", "fixup + fixup = one clean <b>Add search</b> commit.",
      "Shortcut: <b>git commit --fixup X</b> + <b>git rebase -i --autosquash</b>."],
     setup=MESSY, before=squash),

 terminal(M, "cherry-pick", "Copy ONE commit to another branch", '''
git log --oneline --all
git switch -q release/1.0
git cherry-pick -x main
git log --oneline
git ls-files
''', ["Only the fix comes over, not the unreleased feature.", "<b>-x</b> records the original commit ID.",
      "Typical: backport a hotfix to a release branch."],
     setup='''
git init
echo "total = price * qty" > cart.py
git add cart.py
git commit -m "Add cart"
git branch release/1.0
echo "new checkout page" > checkout.py
git add checkout.py
git commit -m "Add new checkout"
echo "total = round(price * qty, 2)" > cart.py
git commit -qam "Fix rounding in cart total"
'''),

 mistake(M, "The golden rule", "Rebasing a shared branch",
     '''
git switch main
git rebase feature/x
git push --force
# everyone who pulled main is now broken''',
     "Rebase creates new commits. Teammates still have the old ones, and their next pull duplicates or loses work.",
     '''
git switch feature/x       # YOUR branch
git rebase origin/main
git push --force-with-lease
# main is only ever merged into''',
     "Rebase your <b>own</b> branch onto main; never rebase main or any shared branch."),

 job(M, "Rebase", "Rebase at work", [
     ("Update your branch before a PR", '''
git fetch
git rebase origin/main'''),
     ("Address review comments neatly", '''
git commit --fixup a1b2c3d
git rebase -i --autosquash origin/main'''),
     ("Avoid merge noise when pulling", '''
git config --global pull.rebase true'''),
     ("Backport a fix", '''
git switch release/2.3
git cherry-pick -x a1b2c3d'''),
 ]),

 interview(M, "merge vs rebase: which do you use, and when?",
     ["<b>merge</b> preserves the true history with a merge commit: safe for shared branches.",
      "<b>rebase</b> replays my commits on a new base for a <b>linear</b> history, but rewrites them (new IDs).",
      "I rebase <b>my own</b> feature branch onto main before a PR, and merge or squash-merge the PR into main.",
      "Golden rule: never rebase commits others have pulled."],
     None,
     "\"How do you squash commits?\" (git rebase -i with squash/fixup, or git reset --soft base + one commit, or Squash and merge on GitHub)."),

 recap(M, "Module 5 in 5 lines",
     ["<b>rebase</b> = replay your commits on a new base: linear history.",
      "Conflict while rebasing: fix, <b>add</b>, <b>rebase --continue</b>.",
      "<b>rebase -i</b>: pick, reword, squash, fixup, drop, reorder.",
      "<b>cherry-pick</b> copies single commits (hotfix backports).",
      "Never rebase shared history."],
     "Do <b>exercises/ex05_clean_history.py</b>: squash and rebase a messy branch."),
]
