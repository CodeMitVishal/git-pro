# Exercise 5 · Clean up a branch before the pull request

[← Course](../../README.md)

## 1. Create the practice repository

Open **Git Bash** (Windows) or a terminal in the course folder:

```bash
bash exercises/ex05_clean_history/setup.sh
```

## 2. Your task

```text
In playground/ex05, the branch feature/search has three messy commits ("WIP search",
"fix typo", "more wip") and it started from an OLD main. main has a new commit since.

Before opening the pull request:
  1. Turn the three commits into ONE commit with the message "Add search".
  2. Put that commit on top of the CURRENT main (linear history, no merge commit).
  3. Leave main itself unchanged.

Hint: git rebase main, then git rebase -i (squash/fixup) or git reset --soft main.
```

## 3. Check your work

```bash
bash exercises/ex05_clean_history/check.sh
```

It prints what's still missing, or **All checks passed!**

Stuck? See the [solution](../../solutions/ex05_clean_history.md).
