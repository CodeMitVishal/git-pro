# Module 10 · Debugging with history

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-10.pdf) · [Interview Q&A](INTERVIEW.md)

Use history as a detective: filter the log, find who changed a line and why, find when code appeared or disappeared, and let bisect find the commit that broke something.

## Lessons

Every lesson runs real Git commands in a throwaway sandbox and prints them with their output. Your own repositories are never touched.

| Lesson | File | Key idea |
|---|---|---|
| git log like a detective | [`01_log_like_a_pro.py`](01_log_like_a_pro.py) | --author, --grep, --since, -- path, --format, shortlog |
| blame & the pickaxe | [`02_blame_and_pickaxe.py`](02_blame_and_pickaxe.py) | blame -L, log -S / -G, git grep in any version |
| git bisect | [`03_bisect.py`](03_bisect.py) | binary search for the first bad commit; bisect run |

```bash
python 10_debugging_history/01_log_like_a_pro.py
```

## Exercise: Find the commit that broke the prices

30 commits, one of them broke the prices. Use git bisect run to find it.

```bash
python exercises/ex10_find_the_bug.py setup
```

```bash
python exercises/ex10_find_the_bug.py check
```

- Solution: [`solutions/ex10_find_the_bug.py`](../solutions/ex10_find_the_bug.py)

## Knowledge check

Test yourself with the [Module 10 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 11 · Advanced Git](../11_advanced_git/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
