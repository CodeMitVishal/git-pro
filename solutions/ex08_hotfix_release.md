# Solution · Exercise 8: Interrupted: ship a hotfix release, then get back to work

Run these commands inside `playground/ex08` (after `bash exercises/ex08_hotfix_release/setup.sh`). Try it yourself first!

```bash
git status --short
git stash push -u -m "coupon work in progress"
git switch hotfix/rounding
git tag -a v1.2.1 -m "Rounding hotfix"
git switch main
git stash pop
git status --short
git tag
```

Then check:

```bash
bash exercises/ex08_hotfix_release/check.sh
```

[← Exercise](../exercises/ex08_hotfix_release/README.md)
