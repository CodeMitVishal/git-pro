# Exercise 12 · Capstone: rescue the repository and ship a release

[← Course](../../README.md)

## 1. Create the practice repository

Open **Git Bash** (Windows) or a terminal in the course folder:

```bash
bash exercises/ex12_rescue_the_repo/setup.sh
```

## 2. Your task

```text
playground/ex12 contains origin.git (plays GitHub), me/ (YOUR clone) and teammate/.
Work in playground/ex12/me. The situation:
  - You committed "Add wishlist" directly on main by mistake (not pushed yet).
  - That commit also contains debug.log, which must never be committed.
  - Meanwhile your teammate pushed "fix: round totals" to origin/main.

Make it right:
  1. main must equal origin/main (with the teammate's fix) and must NOT contain your commit.
  2. Your work goes on a branch feature/wishlist, on top of the latest main,
     and NO commit on that branch may contain debug.log.
  3. Push feature/wishlist to origin.
  4. Release: create an ANNOTATED tag v1.3.0 on the latest main and push the tag.
  5. Leave a clean working tree.

Tip: make a safety branch first (git branch backup) and look before every step.
```

## 3. Check your work

```bash
bash exercises/ex12_rescue_the_repo/check.sh
```

It prints what's still missing, or **All checks passed!**

Stuck? See the [solution](../../solutions/ex12_rescue_the_repo.md).
