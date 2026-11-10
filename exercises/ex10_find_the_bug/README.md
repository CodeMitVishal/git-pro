# Exercise 10 · Find the commit that broke the prices

[← Course](../../README.md)

## 1. Create the practice repository

Open **Git Bash** (Windows) or a terminal in the course folder:

```bash
bash exercises/ex10_find_the_bug/setup.sh
```

## 2. Your task

```text
playground/ex10 has 30 commits. Release v1.0.0 (the first commit) had correct prices;
today gross(100) returns the wrong value. check_price.py exits with 0 when the
prices are right and 1 when they're wrong:

    sh check_price.sh

  1. Use git bisect (ideally git bisect run sh check_price.sh) to find the FIRST
     bad commit.
  2. Write its commit ID (at least 7 characters) into answer.txt.
  3. Finish the bisect session (git bisect reset) so you're back on main.
```

## 3. Check your work

```bash
bash exercises/ex10_find_the_bug/check.sh
```

It prints what's still missing, or **All checks passed!**

Stuck? See the [solution](../../solutions/ex10_find_the_bug.md).
