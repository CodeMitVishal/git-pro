# Module 5 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 5](README.md) · [Quiz](QUIZ.md)

---

### 1. merge vs rebase: which do you use?

**Say:** **merge** keeps the true history and adds a merge commit, so it's safe on shared branches. **rebase** replays my commits on the new base for a **linear** history that's easier to read, bisect and revert, but it rewrites commits. I rebase my own feature branch onto main before a PR, and merge (or squash-merge) the PR into main.

```bash
git fetch
git rebase origin/main
```

**Follow-up:** "What is the golden rule?" Never rebase commits that others have pulled; it creates new IDs and their history diverges.

---

### 2. How do you squash commits?

**Say:** Interactive rebase: `git rebase -i HEAD~3`, keep the first as `pick` and mark the others `squash` or `fixup`. A quicker way is `git reset --soft <base>` followed by one commit. On GitHub, "Squash and merge" does it at merge time.

```bash
git rebase -i HEAD~3
# pick, fixup, fixup
```

---

### 3. How do you edit an older commit message?

**Say:** `git rebase -i <commit>~1`, then change `pick` to `reword` on that line and save. Git then lets you edit the message. Only do this for unpushed commits, or on your own branch with force-with-lease.

---

### 4. What happens when a rebase has conflicts?

**Say:** Git stops at the commit that conflicts. Fix the files, `git add` them, then `git rebase --continue`. `git rebase --skip` drops that commit, and `git rebase --abort` returns to the state before the rebase.

---

### 5. When would you use cherry-pick?

**Say:** To copy **specific** commits to another branch, typically backporting a hotfix from main to a release branch. Use `-x` to record the source commit. If you need many commits, merge or rebase instead.

```bash
git switch release/2.3
git cherry-pick -x a1b2c3d
```

---

### 6. What are --fixup and --autosquash?

**Say:** `git commit --fixup <commit>` creates a commit titled `fixup! <subject>`. Later, `git rebase -i --autosquash` automatically moves it under its target and marks it fixup. It's great for addressing review comments.

---

### 7. What does git pull --rebase do?

**Say:** Fetches, then rebases your local commits on top of the remote branch instead of creating a merge commit, which avoids "Merge branch main of origin" noise. You can make it the default with `git config pull.rebase true`.

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
