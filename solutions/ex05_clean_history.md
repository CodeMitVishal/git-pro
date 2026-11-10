# Solution · Exercise 5: Clean up a branch before the pull request

Run these commands inside `playground/ex05` (after `bash exercises/ex05_clean_history/setup.sh`). Try it yourself first!

Two ways: interactive rebase (pick + fixup + fixup, then reword), or the quick way
below: rebase onto main, then soft-reset to main and commit once.

```bash
git switch feature/search
git rebase main
git log --oneline
git reset --soft main
git commit -m "Add search"
git log --oneline --graph --all
```

Then check:

```bash
bash exercises/ex05_clean_history/check.sh
```

[← Exercise](../exercises/ex05_clean_history/README.md)
