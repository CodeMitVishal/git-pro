# Module 5 · Rebase & rewriting history

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-05.pdf) · [Interview Q&A](INTERVIEW.md)

Keep history clean and linear: rebase onto main, squash and reword with interactive rebase, and copy single commits with cherry-pick, without breaking the golden rule.

## Lessons

Every lesson is a page to read: an everyday picture, a commit-graph diagram, then real Git commands with their real output. Each lesson ends with **Try it yourself**: type the same commands in Git Bash, in a new empty folder.

| Lesson | File | Key idea |
|---|---|---|
| rebase basics | [`01_rebase_basics.md`](01_rebase_basics.md) | replay commits on main; conflicts during rebase; the golden rule |
| Interactive rebase | [`02_interactive_rebase.md`](02_interactive_rebase.md) | squash, fixup, reword, drop; --fixup + --autosquash |
| cherry-pick | [`03_cherry_pick.md`](03_cherry_pick.md) | copy one commit (a hotfix) to another branch |

## Exercise: Clean up a branch before the pull request

Squash three messy commits into one and move them onto the latest main.

Open **Git Bash** (Windows) or any terminal in the course folder. The full task is in [`exercises/ex05_clean_history/README.md`](../exercises/ex05_clean_history/README.md).

```bash
bash exercises/ex05_clean_history/setup.sh
```

```bash
bash exercises/ex05_clean_history/check.sh
```

- Solution: [`solutions/ex05_clean_history.md`](../solutions/ex05_clean_history.md)

## Knowledge check

Test yourself with the [Module 5 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 6 · Remotes & GitHub](../06_remotes_github/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
