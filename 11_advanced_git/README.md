# Module 11 · Advanced Git

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-11.pdf) · [Interview Q&A](INTERVIEW.md)

The tools senior developers reach for: hooks that guard every commit, worktrees, submodules, line endings, cleaning secrets out of history, Git LFS, signed commits and huge repositories.

## Lessons

Every lesson runs real Git commands in a throwaway sandbox and prints them with their output. Your own repositories are never touched.

| Lesson | File | Key idea |
|---|---|---|
| Hooks | [`01_hooks.py`](01_hooks.py) | pre-commit and commit-msg hooks; sharing them; --no-verify |
| Worktrees | [`02_worktrees.py`](02_worktrees.py) | two branches checked out at once |
| Submodules & subtree | [`03_submodules_and_subtree.py`](03_submodules_and_subtree.py) | pinned dependencies on other repos |
| Line endings & .gitattributes | [`04_line_endings_and_attributes.py`](04_line_endings_and_attributes.py) | CRLF vs LF, text=auto, --renormalize |
| Secrets, big files, signing | [`05_secrets_big_files_and_signing.md`](05_secrets_big_files_and_signing.md) | filter-repo, rotate keys, Git LFS, signed commits, sparse/partial clones |

```bash
python 11_advanced_git/01_hooks.py
```

## Exercise: A pre-commit hook that stops leaked secrets

Write a hook that blocks commits containing PASSWORD= or API_KEY= and lets everything else through.

```bash
python exercises/ex11_secret_guard_hook.py setup
```

```bash
python exercises/ex11_secret_guard_hook.py check
```

- Solution: [`solutions/ex11_secret_guard_hook.py`](../solutions/ex11_secret_guard_hook.py)

## Knowledge check

Test yourself with the [Module 11 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 12 · Capstone: rescue a messy repo](../12_capstone/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
