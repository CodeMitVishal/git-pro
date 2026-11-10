# Exercise 11 · A pre-commit hook that stops leaked secrets

[← Course](../../README.md)

## 1. Create the practice repository

Open **Git Bash** (Windows) or a terminal in the course folder:

```bash
bash exercises/ex11_secret_guard_hook/setup.sh
```

## 2. Your task

```text
In playground/ex11, write a pre-commit hook (.git/hooks/pre-commit) that BLOCKS any
commit whose staged changes contain "PASSWORD=" or "API_KEY=", and lets every other
commit through. Make it executable.

Tip: start the file with #!/bin/sh (it also works in Git for Windows), use
git diff --cached | grep ... and exit 1 to block.

The check really tries two commits: one with a secret (must be blocked) and one
without (must succeed). It cleans up after itself.
```

## 3. Check your work

```bash
bash exercises/ex11_secret_guard_hook/check.sh
```

It prints what's still missing, or **All checks passed!**

Stuck? See the [solution](../../solutions/ex11_secret_guard_hook.md).
