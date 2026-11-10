# Solution · Exercise 4: Merge a feature and resolve the conflict

Run these commands inside `playground/ex04` (after `bash exercises/ex04_merge_conflict/setup.sh`). Try it yourself first!

```bash
git merge feature/dark-mode
git status --short
cat config.txt
# write the resolved file (in real life: edit it in VS Code and remove the markers)
echo "theme = dark" > config.txt
echo "font = normal" >> config.txt
git add config.txt
git commit --no-edit
git branch -d feature/dark-mode
git log --oneline --graph
```

Then check:

```bash
bash exercises/ex04_merge_conflict/check.sh
```

[← Exercise](../exercises/ex04_merge_conflict/README.md)
