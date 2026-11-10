"""Mermaid diagrams for each lesson (GitHub renders them as pictures)."""

DIAGRAMS = {
"01_git_basics/01_why_version_control": """
gitGraph
   commit id: "price = 10"
   commit id: "price = 12"
   commit id: "price with VAT"
""",
"01_git_basics/02_install_and_config": """
flowchart LR
    S["--system<br/>all users"] --> G["--global<br/>~/.gitconfig"] --> L["--local<br/>.git/config"]
    L --> W(["the most specific setting wins"])
""",
"02_first_repository/01_three_areas": """
flowchart LR
    W["Working tree<br/>(files you edit)"] -- "git add" --> I["Staging area<br/>(next commit)"]
    I -- "git commit" --> R["Repository<br/>(.git history)"]
    R -- "git restore / checkout" --> W
    I -- "git restore --staged" --> W
""",
"02_first_repository/02_diff_and_log": """
flowchart LR
    W["Working tree"] -- "git diff" --- I["Staging area"]
    I -- "git diff --staged" --- R["Last commit (HEAD)"]
    W -- "git diff HEAD" --- R
""",
"02_first_repository/03_gitignore": """
flowchart LR
    F["new file"] --> Q{"matches .gitignore?"}
    Q -- yes --> X["ignored: git status hides it"]
    Q -- no --> U["untracked: you can git add it"]
    T["already tracked file"] --> N["NOT affected by .gitignore<br/>(git rm --cached)"]
""",
"03_undoing_things/01_restore_and_amend": """
gitGraph
   commit id: "Add cart total"
   commit id: "Add copuon" type: REVERSE
   commit id: "Add coupon with a test" type: HIGHLIGHT
""",
"03_undoing_things/02_reset_three_modes": """
flowchart TB
    R["git reset HEAD~2: the branch moves back 2 commits"] --> S["--soft<br/>changes stay STAGED"]
    R --> M["--mixed (default)<br/>changes stay in files, UNSTAGED"]
    R --> H["--hard<br/>changes DELETED"]
""",
"03_undoing_things/03_revert_and_reflog": """
gitGraph
   commit id: "Add shop"
   commit id: "Change pricing" type: REVERSE
   commit id: "Add tax"
   commit id: "Revert Change pricing" type: HIGHLIGHT
""",
"04_branches_merging/01_branches_are_pointers": """
gitGraph
   commit id: "Add home page"
   branch feature/coupons
   checkout feature/coupons
   commit id: "Add coupons"
""",
"04_branches_merging/02_fast_forward_and_three_way": """
gitGraph
   commit id: "Add home page"
   branch feature/search
   checkout feature/search
   commit id: "Add search"
   checkout main
   commit id: "Add footer"
   merge feature/search id: "merge commit"
""",
"04_branches_merging/03_merge_conflicts": """
gitGraph
   commit id: "Add banner"
   branch feature/sale
   checkout feature/sale
   commit id: "SALE: 20% off"
   checkout main
   commit id: "Free shipping"
   merge feature/sale id: "resolve conflict" type: HIGHLIGHT
""",
"05_rebase_history/01_rebase_basics": """
gitGraph
   commit id: "Add home page"
   commit id: "Add footer"
   branch feature/search
   checkout feature/search
   commit id: "Add search box'"
   commit id: "Add search results'"
""",
"05_rebase_history/02_interactive_rebase": """
flowchart LR
    A["Add search"] --> B["WIP"] --> C["fix typo"]
    C -- "git rebase -i HEAD~3<br/>pick, fixup, fixup" --> D["Add search (one clean commit)"]
""",
"05_rebase_history/03_cherry_pick": """
gitGraph
   commit id: "Add cart"
   branch release/1.0
   checkout main
   commit id: "New checkout"
   commit id: "Fix rounding"
   checkout release/1.0
   cherry-pick id: "Fix rounding"
""",
"06_remotes_github/01_clone_push_pull": """
flowchart LR
    Y["Your laptop<br/>main"] -- "git push" --> G[("GitHub<br/>origin/main")]
    G -- "git pull" --> Y
    G -- "git clone / pull" --> P["Priya's laptop"]
    P -- "git push" --> G
""",
"06_remotes_github/02_fetch_vs_pull": """
flowchart LR
    G[("GitHub")] -- "git fetch" --> O["origin/main<br/>(remote-tracking)"]
    O -- "git merge / rebase" --> M["your main"]
    G -. "git pull = fetch + merge" .-> M
""",
"06_remotes_github/03_rejected_push_and_force": """
flowchart TB
    P["git push"] --> Q{"remote has commits<br/>you don't have?"}
    Q -- no --> OK["pushed"]
    Q -- yes --> R["rejected"] --> F["git pull --rebase, then push"]
    R -. "own branch, after rebase" .-> L["git push --force-with-lease"]
""",
"07_team_workflows/01_github_flow": """
gitGraph
   commit id: "Initial"
   branch feature/wishlist
   checkout feature/wishlist
   commit id: "Add wishlist model"
   commit id: "Add items"
   checkout main
   merge feature/wishlist id: "PR #42 merged"
""",
"07_team_workflows/02_conventional_commits": """
flowchart LR
    F["feat: ..."] --> MI["minor 1.2.0 → 1.3.0"]
    X["fix: ..."] --> PA["patch 1.2.0 → 1.2.1"]
    B["feat!: / BREAKING CHANGE"] --> MA["major 1.2.0 → 2.0.0"]
""",
"08_stash_tags_releases/01_stash": """
flowchart LR
    W["unfinished work"] -- "git stash push -u" --> S[("stash stack")]
    S -- "git stash pop" --> W
    W -. "clean folder: switch branches freely" .-> B["hotfix branch"]
""",
"08_stash_tags_releases/02_tags_and_semver": """
gitGraph
   commit id: "First version" tag: "v1.0.0"
   commit id: "fix: rounding" tag: "v1.0.1"
   commit id: "feat: wishlist"
""",
"08_stash_tags_releases/03_release_notes": """
gitGraph
   commit id: "product pages"
   commit id: "cart" tag: "v1.0.0"
   commit id: "coupons"
   commit id: "rounding fix"
   commit id: "coupon guide"
   commit id: "wishlist" tag: "v1.1.0"
""",
"09_git_internals/01_objects": """
flowchart LR
    C["commit<br/>message, author, parent"] --> T["tree (root folder)"]
    T --> B1["blob: hello"]
    T --> T2["tree: src/"]
    T2 --> B2["blob: print('shop')"]
""",
"09_git_internals/02_refs_and_head": """
flowchart LR
    H["HEAD"] --> M["refs/heads/main"] --> C3["commit Version 3"] --> C2["Version 2"] --> C1["Version 1"]
    T["refs/tags/v1.0.0"] --> C1
""",
"09_git_internals/03_commit_by_hand": """
flowchart LR
    F["hand.txt"] -- "hash-object -w" --> B["blob"]
    B -- "update-index" --> I["index"]
    I -- "write-tree" --> T["tree"]
    T -- "commit-tree" --> C["commit"]
    C -- "update-ref" --> M["main"]
""",
"10_debugging_history/01_log_like_a_pro": """
flowchart LR
    L["git log"] --> A["--author=Priya"]
    L --> G["--grep=coupon"]
    L --> P["-- cart.py"]
    L --> S["--since / --until"]
""",
"10_debugging_history/02_blame_and_pickaxe": """
flowchart LR
    Q1["Who changed this line?"] --> B["git blame -L"]
    Q2["When did this text appear?"] --> S["git log -S 'text'"]
    Q3["Where is it in an old version?"] --> G["git grep text v1.0.0"]
""",
"10_debugging_history/03_bisect": """
flowchart LR
    G["v1.0.0 good"] --- M1["Change 8 ?"] --- M2["Change 12 ?"] --- B["HEAD bad"]
    M1 -. "good: search the right half" .-> M2
    M2 -. "bad: search the left half" .-> F["first bad commit"]
""",
"11_advanced_git/01_hooks": """
flowchart LR
    C["git commit"] --> H{"pre-commit hook<br/>exit code"}
    H -- "0" --> OK["commit created"]
    H -- "1" --> NO["commit blocked"]
""",
"11_advanced_git/02_worktrees": """
flowchart LR
    G[(".git (one repository)")] --> W1["~/project<br/>feature/coupons"]
    G --> W2["~/shop-hotfix<br/>hotfix/rounding"]
""",
"11_advanced_git/03_submodules_and_subtree": """
flowchart LR
    S["shop repo"] -- "libs/logger points to commit b78ae7c" --> L["logger repo"]
""",
"11_advanced_git/04_line_endings_and_attributes": """
flowchart LR
    W["Windows file<br/>CRLF"] -- "git add (text=auto eol=lf)" --> R["repository<br/>LF"] -- "checkout" --> U["every machine<br/>LF"]
""",
"12_capstone/01_rescue_walkthrough": """
flowchart LR
    L["1 LOOK<br/>status, log --graph"] --> F["2 FIND<br/>reflog, origin/main..main"] --> P["3 PLAN<br/>target state"] --> A["4 ACT<br/>backup branch, small steps"]
""",
}
