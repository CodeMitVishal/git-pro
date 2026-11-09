"""Slides · Module 8 · Stash, tags & releases"""
from teach_kit import cover, interview, job, mistake, picture, recap, terminal, trace, why

M = "Module 8 · Stash, tags &amp; releases"
WIP = '''
git init
echo "total = sum(items)" > cart.py
git add cart.py
git commit -m "Add cart"
git switch -c hotfix/rounding
echo "total = round(sum(items), 2)" > cart.py
git commit -qam "Fix rounding"
git switch main
echo "total = sum(items) - discount" > cart.py
echo "def coupon(code): ..." > coupon.py
'''
SLIDES = [
 cover("08", "Stash, tags &amp; releases", "Switch context in seconds, name your releases, and answer \"what changed?\".",
       [("git stash", "01_stash.py"), ("Tags &amp; SemVer", "02_tags_and_semver.py"), ("Release notes", "03_release_notes.py"),
        ("Exercise: hotfix release", "ex08_hotfix_release.py"), ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "Stash", "Interrupted in the middle of your work",
     "You're halfway through a feature when the boss says: <b>\"Production is broken, fix it now!\"</b> Your changes aren't ready to "
     "commit, and Git won't let you switch branches.",
     "<b>git stash</b> sweeps your unfinished work into a drawer. Fix the bug, come back, and <b>git stash pop</b> it out again."),

 terminal(M, "Stash", "Put work aside, switch, come back", '''
git status --short
git switch hotfix/rounding
git stash push -u -m "coupon WIP"
git switch -q hotfix/rounding
git switch -q main
git stash pop -q
git status --short
''', ["Git refuses to switch: your edit would be lost.", "<b>-u</b> includes the new file coupon.py.",
      "<b>pop</b> restores the work and removes the stash."], setup=WIP),

 trace(M, "Stash", "Stash commands", ["Command", "Does"],
       [["<span class=\"m\">git stash push -u -m \"msg\"</span>", "save changes + new files, clean the tree"],
        ["<span class=\"m\">git stash list</span>", "stash@{0} (newest), stash@{1}, ..."],
        ["<span class=\"m\">git stash pop</span>", "re-apply the newest and drop it"],
        ["<span class=\"m\">git stash apply stash@{1}</span>", "re-apply one and keep it"],
        ["<span class=\"m\">git stash show -p stash@{0}</span>", "see what's inside"],
        ["<span class=\"m\">git stash branch fix-later</span>", "turn a stash into a branch"]],
       "Longer than a day? Commit on a branch instead: stashes are easy to forget."),

 picture(M, "Tags", "A tag is a bookmark that never moves",
     "&#127991;&#65039; A <b>branch</b> moves forward with every commit. A <b>tag</b> stays on one commit forever: perfect for "
     "\"this is exactly what we released as v1.2.0\".",
     [("lightweight", "git tag v1.0.0: just a name"), ("annotated", "git tag -a v1.0.0 -m ...: tagger, date, message"),
      ("push", "git push origin v1.0.0 (not automatic!)"), ("release", "CI builds + GitHub Release")]),

 terminal(M, "Tags", "Annotated tags and git describe", '''
git tag -a v1.0.0 -m "First public release"
git cat-file -t v1.0.0
echo "wishlist" > wishlist.txt
git add wishlist.txt
git commit -qm "feat: wishlist"
git describe --tags
git push origin --follow-tags
''', ["<b>cat-file -t</b>: an annotated tag is its own object.", "<b>describe</b>: v1.0.0-1-g&lt;id&gt; = 1 commit after v1.0.0.",
      "<b>--follow-tags</b> pushes annotated tags along with the commits."],
     setup='''
git init --bare ../github/shop.git
git init
git remote add origin ../github/shop.git
echo "shop 1.0" > shop.txt
git add shop.txt
git commit -m "First version of the shop"
git push -q -u origin main
'''),

 trace(M, "SemVer", "Semantic Versioning: MAJOR.MINOR.PATCH", ["Change", "Example", "Bump"],
       [["bug fix only", "fix: round totals", "1.4.2 &#8594; <b>1.4.3</b>"],
        ["new feature, backwards compatible", "feat: wishlist", "1.4.2 &#8594; <b>1.5.0</b>"],
        ["breaking change", "feat!: new API format", "1.4.2 &#8594; <b>2.0.0</b>"],
        ["pre-release", "release candidate", "<b>2.0.0-rc.1</b>"]],
       "Conventional Commits (Module 7) make the bump automatic."),

 terminal(M, "Release notes", "What's in v1.1.0?", '''
git log --oneline v1.0.0..v1.1.0
git shortlog -sn v1.0.0..v1.1.0
''', ["<b>A..B</b> = commits in B that aren't in A.", "<b>shortlog -sn</b>: who contributed.",
      "Paste into the GitHub Release notes."],
     setup='''
git init
echo "pages" > pages.txt
git add pages.txt
git commit -qm "feat: product pages"
git tag -a v1.0.0 -m "Release 1.0.0"
echo "coupons" > coupons.txt
git add coupons.txt
git commit -qm "feat: coupons" --author="Priya <priya@example.com>"
echo "fix" > cart.txt
git add cart.txt
git commit -qm "fix: rounding in cart"
echo "wishlist" > wishlist.txt
git add wishlist.txt
git commit -qm "feat: wishlist" --author="Priya <priya@example.com>"
git tag -a v1.1.0 -m "Release 1.1.0"
'''),

 mistake(M, "Tags", "Moving a public tag",
     '''
git tag -f v1.2.0 HEAD
git push --force origin v1.2.0
# customers' v1.2.0 != your v1.2.0''',
     "Anyone who already fetched v1.2.0 keeps the old commit. Two different \"v1.2.0\" builds now exist: a support nightmare.",
     '''
# fix it with a NEW version
git tag -a v1.2.1 -m "Fix packaging"
git push origin v1.2.1''',
     "Released tags are immutable. Mistake? Ship the next patch version."),

 job(M, "Releases", "Releases at work", [
     ("Cut a release", '''
git tag -a v2.3.0 -m "Release 2.3.0"
git push origin v2.3.0'''),
     ("CI on tag push", '''
on: push: tags: ["v*"]
# build, test, publish, GitHub Release'''),
     ("Which version is deployed?", '''
git describe --tags   # v2.3.0-4-g1a2b3c'''),
     ("Quick context switch", '''
git stash -u && git switch hotfix
...
git switch - && git stash pop'''),
 ]),

 interview(M, "Lightweight vs annotated tags? How do you release?",
     ["A <b>lightweight</b> tag is just a name; an <b>annotated</b> tag stores tagger, date and message, and can be signed.",
      "I use annotated tags with <b>SemVer</b>: v2.3.0.",
      "Tags aren't pushed automatically: <b>git push origin v2.3.0</b> or <b>--follow-tags</b>.",
      "Pushing the tag triggers CI to build, publish and create the GitHub Release.",
      "Released tags never move; mistakes get a new patch version."],
     None,
     "\"What does git stash do?\" (saves uncommitted changes on a stack and cleans the tree; -u for untracked; pop restores)."),

 recap(M, "Module 8 in 5 lines",
     ["<b>git stash push -u</b> &#8594; switch &#8594; <b>git stash pop</b>.",
      "Tags name releases; use <b>annotated</b> tags.",
      "Push tags explicitly: <b>origin v1.2.0</b> / <b>--follow-tags</b>.",
      "SemVer: <b>MAJOR.MINOR.PATCH</b>.",
      "<b>log A..B</b> + <b>shortlog -sn</b> = release notes."],
     "Do <b>exercises/ex08_hotfix_release.py</b>: stash, tag, restore."),
]
