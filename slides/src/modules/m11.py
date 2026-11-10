"""Slides · Module 11 · Advanced Git"""
from teach_kit import cover, interview, job, mistake, picture, recap, snippet, terminal, trace, why

M = "Module 11 · Advanced Git"
HOOK = """#!/bin/sh
if git diff --cached | grep -qE "(PASSWORD|SECRET|API_KEY)="; then
  echo "pre-commit: a secret is staged. Commit blocked."
  exit 1
fi
"""


def with_hook(sb):
    sb.script('git init\necho "# Shop" > README.md\ngit add README.md\ngit commit -qm "Initial commit"', show=False)
    sb.write(".git/hooks/pre-commit", HOOK)
    sb.script("chmod +x .git/hooks/pre-commit", show=False)


def crlf(sb):
    sb.script("git init", show=False)
    sb.path("deploy.sh").write_bytes(b"echo deploying\r\necho done\r\n")
    sb.script('git add deploy.sh\ngit commit -qm "Add deploy script"', show=False)
    sb.write(".gitattributes", "* text=auto eol=lf\n*.bat text eol=crlf\n*.png binary\n")


SLIDES = [
 cover("11", "Advanced Git", "Hooks, worktrees, submodules, line endings, secrets in history, LFS and huge repos.",
       [("Hooks", "01_hooks.md"), ("Worktrees", "02_worktrees.md"), ("Submodules &amp; subtree", "03_submodules_and_subtree.md"),
        ("Line endings", "04_line_endings_and_attributes.md"), ("Secrets, LFS, signing", "05_secrets_big_files_and_signing.md"),
        ("Exercise: secret guard hook", "ex11_secret_guard_hook/"), ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "Advanced Git", "Problems that appear in real teams",
     "An API key pushed to GitHub. A diff where all 500 lines \"changed\". A hotfix needed while your dev server is running. "
     "A 3 GB repository nobody can clone.",
     "Each has a precise tool: <b>hooks</b>, <b>.gitattributes</b>, <b>worktrees</b>, <b>filter-repo</b>, <b>LFS</b>, <b>partial clones</b>."),

 snippet(M, "Hooks", "A pre-commit hook in 5 lines", HOOK.strip(),
     ["Lives in <b>.git/hooks/pre-commit</b> (make it executable).", "Exit 1 = the commit is blocked.",
      "Others: <b>commit-msg</b>, <b>pre-push</b>; share with pre-commit.com."]),

 terminal(M, "Hooks", "The hook in action", '''
echo "API_KEY=sk_live_123" > settings.py
git add settings.py
git commit -m "Add settings"
git log --oneline
''', ["The commit never happened.", "Bypass: <b>--no-verify</b>, so CI must run the same checks.",
      "Real teams: ruff, gitleaks, detect-secrets."], before=with_hook),

 terminal(M, "Worktrees", "Two branches open at the same time", '''
git worktree add ../shop-hotfix hotfix/rounding
git worktree list
git status --short
''', ["A second folder sharing the same .git.", "Your unfinished feature stays untouched.",
      "<b>git worktree remove</b> when done."],
     setup='''
git init
echo "total = sum(items)" > cart.py
git add cart.py
git commit -m "Add cart"
git branch hotfix/rounding
git switch -c feature/coupons
echo "half-finished coupon work" > coupon.py
'''),

 trace(M, "Reusing code", "Submodule vs subtree vs package", ["", "Submodule", "Subtree", "Package (pip/npm)"],
       [["What's in your repo", "a pointer to a commit", "a copy of the files", "a version number"],
        ["Clone needs", "<span class=\"m\">--recurse-submodules</span>", "nothing special", "pip install"],
        ["Update", "<span class=\"m\">git submodule update --remote</span>", "<span class=\"m\">git subtree pull</span>", "bump the version"],
        ["Best for", "pinned infra modules, protos", "vendoring small libs", "most shared libraries"]]),

 terminal(M, "Line endings", "Fix CRLF vs LF once for the whole team", '''
git ls-files --eol
cat .gitattributes
git add --renormalize .
git add .gitattributes
git commit -qm "Normalise line endings"
git ls-files --eol
''', ["<b>i/crlf</b>: the repo stored Windows endings.", "<b>.gitattributes</b> is the team rule.",
      "After renormalising: <b>i/lf</b>."], before=crlf),

 mistake(M, "Secrets", "\"Fixing\" a leaked key with a new commit",
     '''
# pushed: API_KEY=sk_live_123
git rm --cached .env
git commit -m "Remove secret"
git push
# the key is still in history (and already scraped)''',
     "Anyone can read the old commit. Bots find public keys within minutes. The key is compromised.",
     '''
# 1. ROTATE the key now (provider dashboard)
# 2. clean history:
git filter-repo --replace-text expressions.txt
git push --force --all
# 3. prevent: .gitignore, gitleaks, push protection''',
     "Rotate first. Then clean history and make everyone re-clone."),

 trace(M, "Big repos", "Big files and huge repositories", ["Problem", "Tool"],
       [["Large binaries (videos, models, PSDs)", "<b>Git LFS</b>: <span class=\"m\">git lfs track \"*.mp4\"</span>"],
        ["CI only needs the latest code", "<span class=\"m\">git clone --depth 1</span> (shallow)"],
        ["History yes, all blobs no", "<span class=\"m\">git clone --filter=blob:none</span> (partial)"],
        ["Only some folders of a monorepo", "<span class=\"m\">git sparse-checkout set services/api</span>"],
        ["Prove who made a commit", "signed commits (SSH/GPG) &#8594; <b>Verified</b>"]]),

 job(M, "Advanced Git", "Senior-level habits", [
     ("Shared hooks", '''
pip install pre-commit
pre-commit install    # .pre-commit-config.yaml'''),
     ("Day-one repo hygiene", '''
.gitignore + .gitattributes + CODEOWNERS'''),
     ("Fast CI checkouts", '''
git clone --depth 1 --filter=blob:none <url>'''),
     ("Signed commits", '''
git config --global gpg.format ssh
git config --global commit.gpgsign true'''),
 ]),

 interview(M, "You pushed a password to GitHub. What do you do?",
     ["<b>Rotate the credential immediately</b>: assume it's compromised.",
      "Not pushed yet? Amend or rebase it out.",
      "Pushed: <b>git filter-repo</b> to remove it from all history, force-push, everyone re-clones.",
      "Prevent: .gitignore, pre-commit secret scanning, GitHub <b>push protection</b>, a vault for secrets."],
     None,
     "\"What are Git hooks?\" (scripts on events like pre-commit/commit-msg/pre-push; share via pre-commit; CI repeats them)."),

 recap(M, "Module 11 in 5 lines",
     ["<b>Hooks</b> guard commits locally; CI repeats the checks.",
      "<b>worktree</b>: another branch in another folder, same repo.",
      "<b>Submodules</b> pin other repos; packages are often simpler.",
      "<b>.gitattributes</b> + <b>--renormalize</b> end line-ending wars.",
      "Leaked secret: rotate, filter-repo, prevent. Big files: LFS."],
     "Do <b>exercises/ex11_secret_guard_hook/</b>: block secrets with a hook."),
]
