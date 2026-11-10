# Exercise 4 · Merge a feature and resolve the conflict

[← Course](../../README.md)

## 1. Create the practice repository

Open **Git Bash** (Windows) or a terminal in the course folder:

```bash
bash exercises/ex04_merge_conflict/setup.sh
```

## 2. Your task

```text
In playground/ex04, main and the branch feature/dark-mode both changed the first line
of config.txt.

  1. Merge feature/dark-mode INTO main. You will get a conflict.
  2. Resolve it so config.txt is exactly:
         theme = dark
         font = normal
  3. Finish the merge (a merge commit on main), with no conflict markers left anywhere.
  4. Delete the merged branch feature/dark-mode.
```

## 3. Check your work

```bash
bash exercises/ex04_merge_conflict/check.sh
```

It prints what's still missing, or **All checks passed!**

Stuck? See the [solution](../../solutions/ex04_merge_conflict.md).
