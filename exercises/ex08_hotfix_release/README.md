# Exercise 8 · Interrupted: ship a hotfix release, then get back to work

[← Course](../../README.md)

## 1. Create the practice repository

Open **Git Bash** (Windows) or a terminal in the course folder:

```bash
bash exercises/ex08_hotfix_release/setup.sh
```

## 2. Your task

```text
In playground/ex08 you're on main, in the middle of coupon work: cart.py is modified
and coupon.py is a new, untracked file. Don't commit them: they aren't ready.

Urgent: the branch hotfix/rounding has a tested fix that must be released NOW.
  1. Put your unfinished work aside (including the new file).
  2. Switch to hotfix/rounding and create an ANNOTATED tag v1.2.1 on its newest commit
     (any message, e.g. "Rounding hotfix").
  3. Go back to main and bring your unfinished work back, exactly as it was.

At the end: you're on main, cart.py contains "total = sum(items) - discount",
coupon.py exists (still untracked), and the stash list is empty.
```

## 3. Check your work

```bash
bash exercises/ex08_hotfix_release/check.sh
```

It prints what's still missing, or **All checks passed!**

Stuck? See the [solution](../../solutions/ex08_hotfix_release.md).
