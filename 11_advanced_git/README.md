# Module 11 · Advanced Git

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-11.pdf) · [Interview Q&A](INTERVIEW.md)

The tools senior developers reach for: hooks that guard every commit, worktrees, submodules, line endings, cleaning secrets out of history, Git LFS, signed commits and huge repositories.

## Lessons

Every lesson is a page to read: an everyday picture, a commit-graph diagram, then real Git commands with their real output. Each lesson ends with **Try it yourself**: type the same commands in Git Bash, in a new empty folder.

| Lesson | File | Key idea |
|---|---|---|
| Hooks | [`01_hooks.md`](01_hooks.md) | pre-commit and commit-msg hooks; sharing them; --no-verify |
| Worktrees | [`02_worktrees.md`](02_worktrees.md) | two branches checked out at once |
| Submodules & subtree | [`03_submodules_and_subtree.md`](03_submodules_and_subtree.md) | pinned dependencies on other repos |
| Line endings & .gitattributes | [`04_line_endings_and_attributes.md`](04_line_endings_and_attributes.md) | CRLF vs LF, text=auto, --renormalize |
| Secrets, big files, signing | [`05_secrets_big_files_and_signing.md`](05_secrets_big_files_and_signing.md) | filter-repo, rotate keys, Git LFS, signed commits, sparse/partial clones |

## Exercise: A pre-commit hook that stops leaked secrets

Write a hook that blocks commits containing PASSWORD= or API_KEY= and lets everything else through.

Open **Git Bash** (Windows) or any terminal in the course folder. The full task is in [`exercises/ex11_secret_guard_hook/README.md`](../exercises/ex11_secret_guard_hook/README.md).

```bash
bash exercises/ex11_secret_guard_hook/setup.sh
```

```bash
bash exercises/ex11_secret_guard_hook/check.sh
```

- Solution: [`solutions/ex11_secret_guard_hook.md`](../solutions/ex11_secret_guard_hook.md)

## Knowledge check

Test yourself with the [Module 11 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 12 · Capstone: rescue a messy repo](../12_capstone/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
