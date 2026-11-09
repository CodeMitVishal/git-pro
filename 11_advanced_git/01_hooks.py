"""Module 11 · Git hooks: scripts that run automatically

Hooks are scripts in .git/hooks/ that Git runs at certain moments. If a hook exits
with a non-zero code, Git stops the action.

  pre-commit   before a commit is created   -> block secrets, run the linter
  commit-msg   checks the message           -> enforce Conventional Commits
  pre-push     before pushing               -> run the tests

Hooks live in .git/, so they are NOT shared by cloning. Teams share them with
the pre-commit framework (https://pre-commit.com) or core.hooksPath.

TEACHING NOTES
  Why it matters  The cheapest place to catch a leaked password or a lint error is on
                  the developer's laptop, before it reaches the server.
  Picture it      A security guard at the door: every commit is checked on the way out.
  Watch out       Hooks can be skipped with --no-verify, so CI must run the same checks.
  In real jobs    pre-commit with ruff, black, detect-secrets; CI runs pre-commit too.
  Interview       Q: What are Git hooks?
                  A: Scripts Git runs on events like pre-commit or pre-push; a non-zero exit
                     blocks the action. Shared via the pre-commit framework or core.hooksPath.

Run it:  python 11_advanced_git/01_hooks.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
''', show=False)

print("--- 1. A pre-commit hook that blocks secrets")
sb.write(".git/hooks/pre-commit", """#!/bin/sh
if git diff --cached | grep -qE "(PASSWORD|SECRET|API_KEY)="; then
  echo "pre-commit: a secret is staged. Commit blocked."
  exit 1
fi
""")
sb.script('''
chmod +x .git/hooks/pre-commit
cat .git/hooks/pre-commit
echo "API_KEY=sk_live_123" > settings.py
git add settings.py
git commit -m "Add settings"
git log --oneline
''')

print("--- 2. A commit-msg hook that enforces Conventional Commits")
sb.write(".git/hooks/commit-msg", """#!/bin/sh
if ! head -1 "$1" | grep -qE "^(feat|fix|docs|refactor|test|chore)(\\(.+\\))?!?: .+"; then
  echo "commit-msg: use 'type(scope): summary', e.g. 'fix(cart): round totals'"
  exit 1
fi
""")
sb.script('''
chmod +x .git/hooks/commit-msg
echo "API_KEY = os.environ['API_KEY']" > settings.py
git add settings.py
git commit -m "stuff"
git commit -m "feat(settings): read the API key from the environment"
git log --oneline
''')
print("Bypass (careful!): git commit --no-verify. That's why CI must run the same checks.")
