# Module 2 · Your first repository

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-02.pdf) · [Interview Q&A](INTERVIEW.md)

The everyday loop: edit → `git add` → `git commit`, the three areas, reading history, and keeping junk out with `.gitignore`.

## Lessons

Every lesson runs real Git commands in a throwaway sandbox and prints them with their output. Your own repositories are never touched.

| Lesson | File | Key idea |
|---|---|---|
| The three areas | [`01_three_areas.py`](01_three_areas.py) | working tree → staging → repository; git status |
| diff & log | [`02_diff_and_log.py`](02_diff_and_log.py) | diff, diff --staged, log, show |
| .gitignore | [`03_gitignore.py`](03_gitignore.py) | ignore patterns, check-ignore, rm --cached |

```bash
python 02_first_repository/01_three_areas.py
```

## Exercise: Clean commits and a .gitignore

Split messy changes into three focused commits and keep secrets and logs out of Git.

```bash
python exercises/ex02_clean_commits.py setup
```

```bash
python exercises/ex02_clean_commits.py check
```

- Solution: [`solutions/ex02_clean_commits.py`](../solutions/ex02_clean_commits.py)

## Knowledge check

Test yourself with the [Module 2 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 3 · Undoing things](../03_undoing_things/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
