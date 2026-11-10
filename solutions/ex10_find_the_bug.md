# Solution · Exercise 10: Find the commit that broke the prices

Run these commands inside `playground/ex10` (after `bash exercises/ex10_find_the_bug/setup.sh`). Try it yourself first!

```bash
git bisect start HEAD v1.0.0
git bisect run sh check_price.sh               # prints "<id> is the first 'bad' commit"
bad=$(git rev-parse refs/bisect/bad)           # the first bad commit
git bisect reset
echo $bad > answer.txt
cat answer.txt
```

Then check:

```bash
bash exercises/ex10_find_the_bug/check.sh
```

[← Exercise](../exercises/ex10_find_the_bug/README.md)
