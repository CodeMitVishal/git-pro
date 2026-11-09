# Module 11 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 11](README.md) · [Quiz](QUIZ.md)

---

### 1. What are Git hooks? Give examples.

**Say:** Scripts in `.git/hooks` that Git runs on events: `pre-commit` (lint, block secrets), `commit-msg` (message format), `pre-push` (tests), and server-side `pre-receive`. A non-zero exit blocks the action. Teams share them with the pre-commit framework or `core.hooksPath`, and run the same checks in CI because hooks can be bypassed with `--no-verify`.

---

### 2. You committed and pushed a password. What do you do?

**Say:** 1) **Rotate the secret immediately**. 2) If it isn't pushed, amend or rebase it out. If it is pushed: `git filter-repo --replace-text` or `--path ... --invert-paths`, force-push all branches and tags, and have everyone re-clone. 3) Prevent it: .gitignore, pre-commit secret scanning (gitleaks), GitHub push protection, a vault for secrets.

---

### 3. Submodule vs subtree vs package manager?

**Say:** A **submodule** pins another repo at a commit in a subfolder: precise, but clumsy (`--recurse-submodules`, detached HEAD). A **subtree** copies the other repo's content into yours: simple for users, harder to contribute back. A **package** (pip/npm) with versions is usually cleanest for libraries.

---

### 4. How do you handle line endings across Windows and Linux?

**Say:** Commit a `.gitattributes` with `* text=auto eol=lf` (plus `*.bat eol=crlf`, `*.png binary`), and run `git add --renormalize .` once. `.gitattributes` is shared and overrides each developer's `core.autocrlf`.

---

### 5. When would you use git worktree?

**Say:** When I need another branch checked out **at the same time** (a hotfix while my feature's dev server keeps running, or reviewing a PR), without stashing or cloning again. All worktrees share one object database.

```bash
git worktree add ../shop-hotfix hotfix/rounding
```

---

### 6. How do you deal with large files or huge repos?

**Say:** **Git LFS** for large binaries (pointer files in Git, content on an LFS server). For huge repos: shallow clones in CI (`--depth 1`), partial clones (`--filter=blob:none`), `sparse-checkout` for the folders you need, and `git maintenance`.

---

### 7. Why sign commits?

**Say:** `user.email` can be faked, so signing (GPG or SSH keys) proves who made a commit, and GitHub shows Verified. Branch protection can require signed commits.

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
