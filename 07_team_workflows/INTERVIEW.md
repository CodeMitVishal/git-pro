# Module 7 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 7](README.md) · [Quiz](QUIZ.md)

---

### 1. Describe a Git workflow you've used.

**Say:** GitHub flow: a short-lived branch per ticket from the latest main, small commits, push, open a PR with a description, CI runs the tests, one or two reviewers approve, squash-merge into a protected main, and main deploys automatically. Then delete the branch.

**Follow-up:** "How long do your branches live?" Ideally 1–3 days. Long-lived branches drift and cause painful merges.

---

### 2. GitHub flow vs Git flow vs trunk-based?

**Say:** **GitHub flow**: main plus short feature branches, for continuous deployment. **Git flow**: main + develop + feature/release/hotfix branches, for versioned releases and several supported versions. **Trunk-based**: everyone integrates into main at least daily, with feature flags hiding unfinished work; it needs strong CI.

---

### 3. Merge commit vs squash vs rebase merge?

**Say:** **Merge commit** keeps all commits plus a merge commit, so the history is complete but noisy. **Squash** gives one commit per PR: clean, and easy to revert a whole PR. **Rebase merge** gives a linear history that keeps each commit, best when the commits are already meaningful.

---

### 4. What makes a good pull request?

**Say:** Small and focused, a clear title, a description (what, why, how it was tested, linked ticket), green CI, and self-reviewed. Respond to every comment, and push fixes as new commits during review.

**Follow-up:** "How do you review?" Correctness, design, tests, security and performance, leaving style to linters. Be specific and kind.

---

### 5. What is branch protection?

**Say:** Repository rules on branches like main: no direct or force pushes, required PR approvals, required passing status checks, optional linear history and signed commits. CODEOWNERS auto-assigns the right reviewers.

---

### 6. What are Conventional Commits?

**Say:** A message convention, `type(scope): summary` (feat, fix, docs, refactor, test, chore; `!` for breaking changes), so tools can generate changelogs and choose semantic version bumps automatically.

```bash
git commit -m "fix(cart): round totals to 2 decimals"
```

---

### 7. How do you handle a big feature that takes weeks?

**Say:** Split it into small PRs merged behind a **feature flag**, so main stays releasable and integration happens continuously. Avoid a weeks-old branch with a giant merge at the end.

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
