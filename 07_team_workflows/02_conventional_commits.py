"""Module 7 · Commit messages that tools can read: Conventional Commits

Format:   <type>(<optional scope>): <short summary in the imperative>

  feat:     a new feature              -> minor version bump (1.2.0 -> 1.3.0)
  fix:      a bug fix                  -> patch bump        (1.2.0 -> 1.2.1)
  docs:     documentation only
  refactor: code change, no behaviour change
  test:     tests only
  chore:    tooling, dependencies
  feat!: or "BREAKING CHANGE:" in the body -> major bump (1.2.0 -> 2.0.0)

Good:  fix(cart): round totals to 2 decimals
Bad:   fixed stuff / wip / update

This lesson writes a few commits, then a little Python reads `git log` and
builds release notes, which is exactly what tools like semantic-release do.

TEACHING NOTES
  Why it matters  Clear messages make reviews, git log, blame and changelogs useful years later.
  Picture it      Labels on moving boxes: "kitchen: plates" beats "stuff".
  Watch out       Explain WHY in the body when it isn't obvious; the diff already shows WHAT.
  In real jobs    Many teams enforce the format with a commit-msg hook or a CI check.
  Interview       Q: What makes a good commit message?
                  A: A short imperative summary (~50 chars), a blank line, and a body that
                     explains why; one logical change per commit.

Run it:  python 07_team_workflows/02_conventional_commits.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script("git init", show=False)
for path, message in [
    ("cart.py", "feat(cart): add coupon codes"),
    ("cart.py", "fix(cart): round totals to 2 decimals"),
    ("README.md", "docs: explain how to run the shop"),
    ("auth.py", "feat(auth)!: require two-factor login"),
    ("search.py", "fix(search): ignore case when matching"),
]:
    sb.append(path, f"# {message}\n")
    sb.script(f'git add {path}\ngit commit -q -m "{message}"', show=False)

print("--- 1. The history")
sb.script("git log --oneline")

print("--- 2. Release notes generated from the log")
PATTERN = re.compile(r"^(?P<type>\w+)(\((?P<scope>[^)]+)\))?(?P<breaking>!)?: (?P<text>.+)$")
sections = {"feat": "Features", "fix": "Bug fixes", "docs": "Documentation"}
notes = {name: [] for name in sections.values()}
breaking = False
for subject in sb.git("log", "--format=%s").splitlines():
    m = PATTERN.match(subject)
    if not m or m["type"] not in sections:
        continue
    scope = f"**{m['scope']}**: " if m["scope"] else ""
    notes[sections[m["type"]]].append(f"- {scope}{m['text']}")
    breaking |= bool(m["breaking"])
for title, lines in notes.items():
    if lines:
        print(f"### {title}")
        print("\n".join(lines))
print("\nNext version:", "2.0.0 (breaking change)" if breaking else "1.1.0")
