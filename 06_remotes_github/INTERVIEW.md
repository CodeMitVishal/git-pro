# Module 6 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 6](README.md) · [Quiz](QUIZ.md)

---

### 1. git fetch vs git pull?

**Say:** `git fetch` downloads new commits and updates remote-tracking branches (`origin/main`) without touching my branches or files. `git pull` is `fetch` + `merge` (or `rebase` with `--rebase`) into my current branch. I often fetch first to see what's coming.

```bash
git fetch
git log --oneline main..origin/main
git pull --rebase
```

---

### 2. What is a remote-tracking branch?

**Say:** A read-only local copy of a remote branch, like `origin/main`, updated by fetch, pull and push. It shows where the remote branch was the last time you talked to it.

---

### 3. Your push was rejected. Why, and what do you do?

**Say:** The remote has commits I don't have (non-fast-forward), so Git refuses to overwrite them. I run `git pull --rebase` (or fetch + rebase), resolve any conflicts, run the tests, then push.

**Follow-up:** "Would you use --force?" Not on shared branches. On my own branch after a rebase I use --force-with-lease.

---

### 4. --force vs --force-with-lease?

**Say:** `--force` overwrites the remote branch unconditionally and can delete teammates' commits. `--force-with-lease` overwrites only if the remote still points where my origin/ branch says. If someone pushed meanwhile, it's rejected.

```bash
git push --force-with-lease
```

---

### 5. SSH vs HTTPS for GitHub?

**Say:** **SSH** uses a key pair (`ssh-keygen -t ed25519`, then add the public key to GitHub): no passwords, good for daily use. **HTTPS** uses a personal access token or a credential manager, and works through strict firewalls. Passwords are no longer accepted for Git operations on GitHub.

---

### 6. What is a bare repository?

**Say:** A repository without a working tree: just the .git contents. Servers (GitHub, GitLab) store bare repos, because nobody edits files there directly.

```bash
git init --bare shop.git
```

---

### 7. How do you work with a fork?

**Say:** Clone your fork (`origin`), add the original as `upstream`, then fetch upstream and rebase or merge to stay current. Push branches to your fork and open PRs to upstream.

```bash
git remote add upstream https://github.com/org/project.git
git fetch upstream
git rebase upstream/main
```

---

### 8. How do you delete a remote branch?

**Say:** `git push origin --delete feature/x`. Others clean up stale remote-tracking branches with `git fetch --prune`.

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
