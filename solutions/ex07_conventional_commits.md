# Solution · Exercise 7: Commits a reviewer will love

Run these commands inside `playground/ex07` (after `bash exercises/ex07_conventional_commits/setup.sh`). Try it yourself first!

```bash
git status --short
git add auth.py
git commit -m "feat(auth): add two-factor login"
git add cart.py
git commit -m "fix(cart): round totals to 2 decimals"
git add README.md
git commit -m "docs: explain two-factor login"
git log --oneline
```

Then check:

```bash
bash exercises/ex07_conventional_commits/check.sh
```

[← Exercise](../exercises/ex07_conventional_commits/README.md)
