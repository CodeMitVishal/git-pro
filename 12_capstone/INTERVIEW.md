# Module 12 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 12](README.md) · [Quiz](QUIZ.md)

---

### 1. You committed to main instead of a feature branch. Fix it.

**Say:** Keep the commit by creating the branch where I am (`git branch feature/x`), move main back (`git reset --hard origin/main`), switch to the feature branch, and rebase it if main moved. If it was already pushed to a shared main, revert instead of resetting.

```bash
git branch feature/wishlist
git reset --hard origin/main
git switch feature/wishlist
git rebase main
```

---

### 2. Your branch is 40 commits behind main and has conflicts. What do you do?

**Say:** `git fetch`, then `git rebase origin/main` (or merge, if the branch is shared). Resolve conflicts commit by commit, run the tests, and push with `--force-with-lease`. In future, keep branches short-lived and integrate main often.

---

### 3. Walk me through what you check when a repo is in a weird state.

**Say:** Look: `git status -sb`, `git log --oneline --graph --all`, `git stash list`. Find: `git reflog`, `git log origin/main..main`. Plan the target state. Act in small steps, with a safety branch (`git branch backup`) before anything destructive.

---

### 4. How would you set up Git for a new team project?

**Say:** A protected main with required PR reviews and CI checks, CODEOWNERS, a .gitignore and .gitattributes, pre-commit hooks (lint, secret scanning) mirrored in CI, Conventional Commits with an automated changelog, squash merges, and tagged SemVer releases that trigger deployment.

---

### 5. A teammate force-pushed and your commits disappeared from the remote. Recover?

**Say:** My local clone still has them: check `git reflog` or `git log origin/main@{1}`, and recover with a branch. Push them back after agreeing with the team. Then enable branch protection so force pushes to main are blocked.

---

### 6. Explain the difference between git reset, revert, restore and checkout.

**Say:** `restore` changes **files** (discard or unstage). `reset` moves the **branch** (soft/mixed/hard), for local history. `revert` adds a **new commit** that undoes one, for shared history. `checkout` is the old command that did both switching and restoring; `switch` and `restore` replaced it.

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
