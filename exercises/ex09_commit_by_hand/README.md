# Exercise 9 · Make a commit without git add or git commit

[← Course](../../README.md)

## 1. Create the practice repository

Open **Git Bash** (Windows) or a terminal in the course folder:

```bash
bash exercises/ex09_commit_by_hand/setup.sh
```

## 2. Your task

```text
playground/ex09 has one commit ("Initial commit", with README.md) and a new file
hand.txt. Using ONLY plumbing commands (hash-object, update-index, write-tree,
commit-tree, update-ref), create a new commit on main:

  - message:  Built by hand
  - parent:   the current main ("Initial commit")
  - contents: README.md (unchanged) and hand.txt

Then answer in answers.txt (one per line, untracked is fine):
  line 1: the object TYPE of the new commit's tree   (git cat-file -t ...)
  line 2: the blob ID of hand.txt                      (git rev-parse HEAD:hand.txt)
```

## 3. Check your work

```bash
bash exercises/ex09_commit_by_hand/check.sh
```

It prints what's still missing, or **All checks passed!**

Stuck? See the [solution](../../solutions/ex09_commit_by_hand.md).
