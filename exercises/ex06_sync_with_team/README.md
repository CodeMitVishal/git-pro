# Exercise 6 · Sync with your team

[← Course](../../README.md)

## 1. Create the practice repository

Open **Git Bash** (Windows) or a terminal in the course folder:

```bash
bash exercises/ex06_sync_with_team/setup.sh
```

## 2. Your task

```text
playground/ex06 contains:
  origin.git   the shared repository (it plays GitHub)
  me/          YOUR clone. You have a local commit "Add shipping" that isn't pushed.
  teammate/    Priya's clone. She already pushed "Add payments" to origin.

Work inside playground/ex06/me:
  1. Get Priya's commit.
  2. Push your commit.
  3. The history on origin must be LINEAR: no merge commits.

Hint: git pull --rebase, then git push.
```

## 3. Check your work

```bash
bash exercises/ex06_sync_with_team/check.sh
```

It prints what's still missing, or **All checks passed!**

Stuck? See the [solution](../../solutions/ex06_sync_with_team.md).
