# Exercise 3 · Undo three mistakes

[← Course](../../README.md)

## 1. Create the practice repository

Open **Git Bash** (Windows) or a terminal in the course folder:

```bash
bash exercises/ex03_undo_mistakes/setup.sh
```

## 2. Your task

```text
playground/ex03 has three problems. Fix them all:

  1. app.py has messy, uncommitted changes. Throw them away.
  2. The commit "Change pricing" set every price to 0. main is shared with the team,
     so do NOT rewrite history: undo that commit with a new commit.
  3. Yesterday you deleted the branch "experiment" (its last commit is
     "Try discount banner"). Bring the branch back.

Hint: git restore, git revert, git reflog.
```

## 3. Check your work

```bash
bash exercises/ex03_undo_mistakes/check.sh
```

It prints what's still missing, or **All checks passed!**

Stuck? See the [solution](../../solutions/ex03_undo_mistakes.md).
