# Module 4 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 4](README.md) · [Quiz](QUIZ.md)

---

### 1. What is a branch in Git?

**Say:** A **lightweight, movable pointer** to a commit: a small file holding a commit ID. Creating one is instant. HEAD points to the current branch, and each new commit moves that branch forward.

```bash
git switch -c feature/login
git branch -v
```

---

### 2. Fast-forward vs three-way merge?

**Say:** **Fast-forward**: the target branch hasn't moved, so Git just moves its pointer to the feature tip; there's no merge commit. **Three-way**: both sides have new commits, so Git uses the common ancestor plus both tips to create a **merge commit** with two parents.

```bash
git merge --no-ff feature/login   # force a merge commit
```

**Follow-up:** "Why use --no-ff?" To keep the feature visible as one unit in history, which also makes it easy to revert as a whole.

---

### 3. How do you resolve a merge conflict?

**Say:** `git status` lists the conflicted files (UU). Open each one, decide the final content between `<<<<<<<`, `=======` and `>>>>>>>`, remove the markers, then `git add` and `git commit`. Run the tests. Use `git merge --abort` to cancel.

```bash
git merge feature/sale
git status
# edit the files
git add banner.txt
git commit
```

**Follow-up:** "How do you reduce conflicts?" Small, short-lived branches, merging or rebasing on main often, and clear code ownership.

---

### 4. git switch vs git checkout?

**Say:** `git checkout` did two jobs (switch branches **and** restore files). Git 2.23 split it into `git switch` for branches and `git restore` for files, which is clearer and safer. checkout still works.

---

### 5. How do you list merged and unmerged branches?

**Say:** `git branch --merged main` shows branches already in main (safe to delete); `--no-merged` shows the rest. `-d` refuses to delete unmerged work; `-D` forces it.

```bash
git branch --merged main
git branch -d feature/old
```

---

### 6. What is a detached HEAD?

**Say:** HEAD points directly to a commit instead of a branch (for example after `git switch --detach <id>` or checking out a tag). New commits there belong to no branch. Create a branch (`git switch -c name`) to keep them.

---

### 7. What is a merge base?

**Say:** The best common ancestor of two branches; a three-way merge compares both tips against it. `git merge-base main feature` prints it.

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
