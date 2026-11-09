# Module 9 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 9](README.md) · [Quiz](QUIZ.md)

---

### 1. How does Git store data internally?

**Say:** As a content-addressable object database in `.git/objects`: **blobs** (file contents), **trees** (directories), **commits** (a tree + parents + metadata) and **annotated tags**, each named by the SHA-1 (or SHA-256) hash of its content. Branches and tags are refs: files holding object IDs.

```bash
git cat-file -p HEAD
git cat-file -p HEAD^{tree}
```

---

### 2. Does Git store diffs or snapshots?

**Say:** Snapshots: every commit points to a full tree. Unchanged files reuse the same blob, so it's cheap, and packfiles delta-compress similar objects on disk. Diffs are computed when you ask for them.

---

### 3. Why do commit IDs change after a rebase or amend?

**Say:** A commit's ID is a hash of its content: tree, **parent IDs**, author, committer, dates and message. Change any of these (a new parent after a rebase, a new message after amend) and you get a different hash, so it's a new commit.

---

### 4. What happens when you run git commit?

**Say:** Git writes the index as tree objects (`write-tree`), creates a commit object with that tree, the current HEAD as parent, author and message (`commit-tree`), then moves the current branch ref to it (`update-ref`) and logs it in the reflog.

---

### 5. What is a detached HEAD, and how do you get out of it?

**Say:** HEAD contains a commit ID instead of `ref: refs/heads/<branch>`, for example after checking out a tag or a commit. Commits made there aren't on a branch. To keep them: `git switch -c new-branch`. To leave: `git switch main`.

---

### 6. HEAD~ vs HEAD^?

**Say:** `HEAD~n` follows the **first** parent n generations back. `HEAD^n` picks the **n-th parent** of a merge commit. `HEAD~1` and `HEAD^` are the same.

---

### 7. What is git gc?

**Say:** Garbage collection: it packs loose objects into packfiles (with delta compression) and removes unreachable objects older than the expiry period. Git runs it automatically from time to time.

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
