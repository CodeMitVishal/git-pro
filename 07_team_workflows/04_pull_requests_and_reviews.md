# Module 7 · Pull requests & code review

[← Module 7](README.md)

A **pull request** (PR; GitLab calls it a merge request) asks: *"please review my branch and merge it into main"*. It's where code review, CI and discussion happen.

## A good pull request

- **Small**: one topic, ideally under ~400 changed lines. Small PRs get reviewed faster and more carefully.
- **A clear title**: `Add coupon codes to checkout`, not `Update`.
- **A description**: *what* changed, *why* (link the ticket), *how you tested it*, screenshots for UI changes.
- **Green CI** before you ask for a review.
- **Self-review first**: read your own diff on GitHub as a reviewer would.

A PR template file (`.github/pull_request_template.md`):

```markdown
## What
## Why  (ticket: SHOP-142)
## How I tested it
- [ ] unit tests  - [ ] manual test in staging
## Screenshots
```

## Reviewing code

Check, in this order:
1. **Correctness**: does it do what the ticket asks? Edge cases? Error handling?
2. **Design**: is it in the right place, readable, and not over-engineered?
3. **Tests**: are the important paths covered?
4. **Security and performance**: input validation, secrets, N+1 queries.
5. **Style**: leave formatting to the tools (ruff, prettier).

Be kind and specific: *"What happens if `items` is empty? Maybe return 0 here?"* beats *"this is wrong"*. Prefix optional ideas with **nit:**.

## Protecting main (repository settings)

| Setting | Effect |
|---|---|
| **Branch protection / rulesets** on `main` | no direct pushes, no force pushes |
| **Require pull request reviews** | e.g. 1 approval before merging |
| **Require status checks** | CI must pass |
| **CODEOWNERS** file | auto-requests reviews from the owning team (`/payments/ @shop/payments-team`) |
| **Require linear history** | only squash or rebase merges |
| **Dismiss stale approvals** | new commits need a new review |

## Merge buttons (see `01_github_flow.py`)

| Button | History | Use when |
|---|---|---|
| Create a merge commit | every commit + a merge commit | you want the full branch history |
| **Squash and merge** | one commit per PR | most teams: a clean `main`, easy to revert one PR |
| Rebase and merge | linear, every commit kept | the commits are already clean and meaningful |

## Addressing review comments

```bash
# fix what the reviewer asked
git commit --fixup a1b2c3d          # or a normal commit
git push                            # the PR updates automatically
# before merging, optionally tidy up:
git rebase -i --autosquash origin/main
git push --force-with-lease
```

## Interview answer

> *"I keep PRs small with a clear description and green CI, and self-review the diff first. As a reviewer I look at correctness, design, tests and security, and leave style to the linters. `main` is protected: PRs need one approval and passing checks, and we squash-merge so every PR is one revertable commit."*

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
