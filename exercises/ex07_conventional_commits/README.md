# Exercise 7 · Commits a reviewer will love

[← Course](../../README.md)

## 1. Create the practice repository

Open **Git Bash** (Windows) or a terminal in the course folder:

```bash
bash exercises/ex07_conventional_commits/setup.sh
```

## 2. Your task

```text
In playground/ex07 you changed three files for three different reasons:
  auth.py     a NEW feature (two-factor login)
  cart.py     a BUG fix (rounding)
  README.md   documentation

Make three separate commits, in this order, using Conventional Commits:
  1. a  feat  commit with only auth.py     e.g.  feat(auth): add two-factor login
  2. a  fix   commit with only cart.py     e.g.  fix(cart): round totals to 2 decimals
  3. a  docs  commit with only README.md   e.g.  docs: explain two-factor login

Format: type(optional-scope): summary   (lowercase type, a colon and a space, a summary
of at least 10 characters, no full stop at the end)
```

## 3. Check your work

```bash
bash exercises/ex07_conventional_commits/check.sh
```

It prints what's still missing, or **All checks passed!**

Stuck? See the [solution](../../solutions/ex07_conventional_commits.md).
