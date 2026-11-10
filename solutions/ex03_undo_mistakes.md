# Solution · Exercise 3: Undo three mistakes

Run these commands inside `playground/ex03` (after `bash exercises/ex03_undo_mistakes/setup.sh`). Try it yourself first!

```bash
# 3 first: find the lost commit while it's still HEAD@{1} in the reflog
git reflog -3
git branch experiment HEAD@{1}
# 1: throw away the uncommitted mess
git restore app.py
# 2: undo a shared commit with a NEW commit
git log --oneline
git revert --no-edit HEAD~1
git log --oneline
```

Then check:

```bash
bash exercises/ex03_undo_mistakes/check.sh
```

[← Exercise](../exercises/ex03_undo_mistakes/README.md)
