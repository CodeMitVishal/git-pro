# Module 3 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 3](README.md) · [Quiz](QUIZ.md)

---

### 1. git reset vs git revert?

**Say:** `reset` **moves the branch pointer** back, rewriting history: only for local, unpushed commits. `revert` creates a **new commit** that undoes an old one, so history is kept. It's the safe choice on shared branches like main.

```bash
git revert <bad-commit>
git push
```

---

### 2. Explain reset --soft, --mixed and --hard.

**Say:** All three move the branch to the given commit. **--soft** keeps the undone changes staged, **--mixed** (the default) keeps them in the working tree unstaged, and **--hard** discards them and makes the working tree match the commit.

```bash
git reset --soft HEAD~3   # squash 3 commits into one
git commit -m "Add search"
```

**Follow-up:** "When would you use --soft?" To combine several local work-in-progress commits into one clean commit.

---

### 3. How do you recover a commit after reset --hard or a deleted branch?

**Say:** Use `git reflog`: it records every position of HEAD. Find the commit ID, then `git reset --hard <id>` or `git branch <name> <id>`. Entries are kept for about 90 days by default.

```bash
git reflog
git branch rescue HEAD@{2}
```

**Follow-up:** "Is reflog shared?" No, it's local to your clone.

---

### 4. How do you change the last commit message?

**Say:** `git commit --amend -m "new message"`, only if the commit isn't pushed. For older commits, use interactive rebase with `reword` (Module 5).

---

### 5. restore vs reset vs checkout?

**Say:** `git restore` works on **files** (discard or unstage changes). `git reset` moves the **branch** (and can unstage). `git checkout` is the old all-in-one command; `git switch` and `git restore` replaced its two jobs.

---

### 6. You committed to main by mistake instead of a feature branch. Fix it?

**Say:** Create the branch at the current commit, then move main back. If main was already pushed, revert instead.

```bash
git branch feature/login
git reset --hard HEAD~1
git switch feature/login
```

---

### 7. How do you undo a merge that's already pushed?

**Say:** `git revert -m 1 <merge-commit>`: `-m 1` says to keep the first parent (main) as the mainline. Note that re-merging the same branch later needs a revert of the revert.

```bash
git revert -m 1 a1b2c3d
```

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
