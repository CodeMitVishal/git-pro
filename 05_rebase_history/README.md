# Module 5 · Rebase & rewriting history

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-05.pdf) · [Interview Q&A](INTERVIEW.md)

Keep history clean and linear: rebase onto main, squash and reword with interactive rebase, and copy single commits with cherry-pick, without breaking the golden rule.

## Lessons

Every lesson runs real Git commands in a throwaway sandbox and prints them with their output. Your own repositories are never touched.

| Lesson | File | Key idea |
|---|---|---|
| rebase basics | [`01_rebase_basics.py`](01_rebase_basics.py) | replay commits on main; conflicts during rebase; the golden rule |
| Interactive rebase | [`02_interactive_rebase.py`](02_interactive_rebase.py) | squash, fixup, reword, drop; --fixup + --autosquash |
| cherry-pick | [`03_cherry_pick.py`](03_cherry_pick.py) | copy one commit (a hotfix) to another branch |

```bash
python 05_rebase_history/01_rebase_basics.py
```

## Exercise: Clean up a branch before the pull request

Squash three messy commits into one and move them onto the latest main.

```bash
python exercises/ex05_clean_history.py setup
```

```bash
python exercises/ex05_clean_history.py check
```

- Solution: [`solutions/ex05_clean_history.py`](../solutions/ex05_clean_history.py)

## Knowledge check

Test yourself with the [Module 5 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 6 · Remotes & GitHub](../06_remotes_github/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
