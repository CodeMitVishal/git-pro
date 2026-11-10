"""Slides · Module 7 · Team workflows"""
from teach_kit import cover, interview, job, mistake, picture, recap, snippet, terminal, trace, why

M = "Module 7 · Team workflows"
PR = '''
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
git switch -c feature/wishlist
echo "wishlist = []" > wishlist.py
git add wishlist.py
git commit -m "Add wishlist model"
echo "def add(item): wishlist.append(item)" >> wishlist.py
git commit -qam "Add items to the wishlist"
git switch main
echo "footer" > footer.txt
git add footer.txt
git commit -m "Add footer"
'''
SLIDES = [
 cover("07", "Team workflows", "How real teams ship: GitHub flow, pull requests, reviews, commit conventions and branching strategies.",
       [("GitHub flow", "01_github_flow.md"), ("Conventional Commits", "02_conventional_commits.md"),
        ("Branching strategies", "03_branching_strategies.md"), ("Pull requests &amp; reviews", "04_pull_requests_and_reviews.md"),
        ("Exercise: great commits", "ex07_conventional_commits/"), ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "Workflows", "Ten developers, one main branch",
     "Without rules, people push half-finished work to main, production breaks on Friday evening, and nobody knows which change caused it.",
     "A <b>workflow</b> is the team's agreement: branch per task, <b>pull request</b> with CI and review, then merge into a protected main."),

 picture(M, "GitHub flow", "The GitHub flow loop",
     "&#127859; A restaurant kitchen: each dish (branch) is prepared at its own station and only reaches the customer (main) "
     "after the head chef tastes it (review + CI).",
     [("branch", "git switch -c feature/x"), ("commit + push", "small commits, push the branch"),
      ("pull request", "CI + review + discussion"), ("merge", "into protected main"), ("deploy", "main goes live")]),

 terminal(M, "Merge buttons", "\"Squash and merge\" = one commit per PR", '''
git merge --squash feature/wishlist
git commit -qm "Add wishlist (#42)"
git log --oneline --graph
''', ["The 2 branch commits become 1 on main.", "Easy to read; easy to revert a whole PR.",
      "\"Create a merge commit\" = <b>--no-ff</b>; \"Rebase and merge\" = rebase + fast-forward."], setup=PR),

 trace(M, "Merge buttons", "The three GitHub merge buttons", ["Button", "History on main", "Choose when"],
       [["Create a merge commit", "all commits + a merge commit", "you want the full branch story"],
        ["<b>Squash and merge</b>", "one commit per PR", "most teams: clean main, easy reverts"],
        ["Rebase and merge", "linear, every commit kept", "commits are already clean and meaningful"]]),

 snippet(M, "Conventional Commits", "Commit messages that tools can read", '''
feat(cart): add coupon codes          -> minor  1.2.0 -> 1.3.0
fix(cart): round totals to 2 decimals -> patch  1.2.0 -> 1.2.1
docs: explain how to run the shop
refactor(search): extract query parser
test(auth): cover expired tokens
chore: bump django to 5.1
feat(auth)!: require two-factor login -> major  1.2.0 -> 2.0.0''',
     ["<b>type(scope): summary</b> in the imperative.", "Tools turn the log into <b>release notes</b> and pick the next version.",
      "The body explains <b>why</b>; the diff already shows what."]),

 trace(M, "Branching strategies", "GitHub flow vs Git flow vs trunk-based", ["", "GitHub flow", "Git flow", "Trunk-based"],
       [["Long-lived branches", "main", "main + develop", "main"],
        ["Branch lifetime", "days", "weeks", "hours"],
        ["Releases", "every merge", "planned versions", "continuous"],
        ["Unfinished work", "on a branch", "on a branch", "feature flags"],
        ["Best for", "web apps, services", "versioned products", "strong-CI teams"]],
       "Most web teams: <b>GitHub flow</b>. Say which you'd choose and why."),

 trace(M, "Pull requests", "Protect main", ["Setting", "Effect"],
       [["Branch protection / rulesets", "no direct pushes, no force pushes to main"],
        ["Required reviews", "e.g. 1 approval; stale approvals dismissed on new commits"],
        ["Required status checks", "CI must be green"],
        ["CODEOWNERS", "<span class=\"m\">/payments/ @shop/payments-team</span> auto-requested"],
        ["Require linear history", "only squash / rebase merges"]]),

 mistake(M, "Pull requests", "The 2,000-line pull request",
     '''
Title: Update
Description: (empty)
+2,143 -871 in 46 files
"LGTM" after 3 minutes''',
     "Nobody can review that properly. Bugs slip through, and the branch has drifted for weeks: merge conflicts everywhere.",
     '''
Title: Add coupon codes to checkout
What / Why (SHOP-142) / How I tested
+180 -12 in 5 files, CI green''',
     "Small PRs, a clear description, green CI. Big features: several PRs behind a feature flag."),

 job(M, "Teamwork", "Your daily team routine", [
     ("Start a ticket", '''
git switch main && git pull
git switch -c feature/SHOP-142-coupons'''),
     ("Open the PR", '''
git push -u origin feature/SHOP-142-coupons
# GitHub: Compare & pull request'''),
     ("Answer the review", '''
git commit -m "fix(cart): handle empty coupon"
git push'''),
     ("After the merge", '''
git switch main && git pull
git branch -d feature/SHOP-142-coupons'''),
 ]),

 interview(M, "Describe your team's Git workflow.",
     ["<b>GitHub flow</b>: a short-lived branch per ticket from the latest main.",
      "Push, open a <b>PR</b> with a description; <b>CI</b> runs; one or two reviewers approve.",
      "<b>Squash-merge</b> into a <b>protected</b> main, which deploys automatically.",
      "Big features land in small PRs behind <b>feature flags</b>."],
     None,
     "\"GitHub flow vs Git flow?\" (Git flow adds develop/release/hotfix branches for versioned releases; heavier, more merge pain)."),

 recap(M, "Module 7 in 5 lines",
     ["Branch &#8594; PR &#8594; CI + review &#8594; merge &#8594; deploy.",
      "Merge buttons: merge commit, <b>squash</b>, rebase.",
      "<b>type(scope): summary</b> commits power changelogs and versions.",
      "GitHub flow for most web teams; Git flow for versioned releases.",
      "Protect main: reviews, checks, CODEOWNERS."],
     "Do <b>exercises/ex07_conventional_commits/</b>: three changes, three clean commits."),
]
