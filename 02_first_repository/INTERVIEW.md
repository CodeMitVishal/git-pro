# Module 2 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 2](README.md) · [Quiz](QUIZ.md)

---

### 1. Explain the working tree, staging area and repository.

**Say:** The **working tree** is the files you edit. The **staging area** (index) is the snapshot you're preparing. The **repository** (.git) stores the commits. `git add` moves changes into the index, and `git commit` saves the index as a new commit.

```bash
git add app.py
git commit -m "Fix login"
```

**Follow-up:** "Why have a staging area at all?" So you can commit part of your changes: one focused commit per idea, even after editing many files.

---

### 2. git diff vs git diff --staged?

**Say:** `git diff` shows unstaged changes (working tree vs index). `git diff --staged` (or `--cached`) shows what will be committed (index vs HEAD). `git diff HEAD` shows both.

---

### 3. How do you write a good commit message?

**Say:** A short imperative summary under ~50 characters ("Add coupon validation"), a blank line, then a body that explains **why** if it isn't obvious. One logical change per commit.

**Follow-up:** "What is Conventional Commits?" A format like `feat:`, `fix:`, `docs:` that tools use to generate changelogs and versions (Module 7).

---

### 4. A file is ignored but still tracked. How do you fix it?

**Say:** `.gitignore` only affects untracked files. Remove the file from the index but keep it on disk with `git rm --cached`, then commit.

```bash
git rm --cached settings.ini
git commit -m "Stop tracking settings.ini"
```

**Follow-up:** "Is the secret now gone?" No, it's still in the history. Rotate the secret; rewriting history is Module 11.

---

### 5. How do you see the history of one file?

**Say:** `git log -- path` lists the commits that touched it, `-p` adds the diffs, and `--follow` keeps going across renames.

```bash
git log --oneline --follow -- cart.py
```

---

### 6. What does git status tell you?

**Say:** The current branch, what's staged, what's modified but not staged, untracked files, and whether you're ahead of or behind the remote. `-s` is the short form and `-b` adds the branch.

```bash
git status -sb
```

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
