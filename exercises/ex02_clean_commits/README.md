# Exercise 2 · Clean commits and a .gitignore

[← Course](../../README.md)

## 1. Create the practice repository

Open **Git Bash** (Windows) or a terminal in the course folder:

```bash
bash exercises/ex02_clean_commits/setup.sh
```

## 2. Your task

```text
playground/ex02 is a repository with one commit. You changed several things since:
cart.py and README.md are modified, and there are new files .env, debug.log and coupon.py.

  1. Create a .gitignore so that .env and every *.log file are ignored. Commit it alone:
     message "Add gitignore".
  2. Commit the cart.py change together with the new coupon.py: message "Add coupons".
  3. Commit the README.md change on its own: message "Document coupons".

At the end: three new commits in that order, a clean git status, and .env never committed.
```

## 3. Check your work

```bash
bash exercises/ex02_clean_commits/check.sh
```

It prints what's still missing, or **All checks passed!**

Stuck? See the [solution](../../solutions/ex02_clean_commits.md).
