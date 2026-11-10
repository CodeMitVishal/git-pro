# Solution · Exercise 9: Make a commit without git add or git commit

Run these commands inside `playground/ex09` (after `bash exercises/ex09_commit_by_hand/setup.sh`). Try it yourself first!

```bash
blob=$(git hash-object -w hand.txt)          # 1. store the content as a blob
git update-index --add --cacheinfo 100644,$blob,hand.txt   # 2. put it in the index
tree=$(git write-tree)                         # 3. index -> tree
commit=$(git commit-tree $tree -p HEAD -m "Built by hand")  # 4. tree + parent -> commit
git update-ref refs/heads/main $commit         # 5. move main to the new commit
git cat-file -t HEAD^{tree} > answers.txt      # -> tree
git rev-parse HEAD:hand.txt >> answers.txt     # -> the blob ID
git log --oneline
git restore hand.txt 2>/dev/null; git status --short
```

Then check:

```bash
bash exercises/ex09_commit_by_hand/check.sh
```

[← Exercise](../exercises/ex09_commit_by_hand/README.md)
