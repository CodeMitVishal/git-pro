# Module 10 · Debugging with history

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-10.pdf) · [Interview Q&A](INTERVIEW.md)

Use history as a detective: filter the log, find who changed a line and why, find when code appeared or disappeared, and let bisect find the commit that broke something.

## Lessons

Every lesson is a page to read: an everyday picture, a commit-graph diagram, then real Git commands with their real output. Each lesson ends with **Try it yourself**: type the same commands in Git Bash, in a new empty folder.

| Lesson | File | Key idea |
|---|---|---|
| git log like a detective | [`01_log_like_a_pro.md`](01_log_like_a_pro.md) | --author, --grep, --since, -- path, --format, shortlog |
| blame & the pickaxe | [`02_blame_and_pickaxe.md`](02_blame_and_pickaxe.md) | blame -L, log -S / -G, git grep in any version |
| git bisect | [`03_bisect.md`](03_bisect.md) | binary search for the first bad commit; bisect run |

## Exercise: Find the commit that broke the prices

30 commits, one of them broke the prices. Use git bisect run to find it.

Open **Git Bash** (Windows) or any terminal in the course folder. The full task is in [`exercises/ex10_find_the_bug/README.md`](../exercises/ex10_find_the_bug/README.md).

```bash
bash exercises/ex10_find_the_bug/setup.sh
```

```bash
bash exercises/ex10_find_the_bug/check.sh
```

- Solution: [`solutions/ex10_find_the_bug.md`](../solutions/ex10_find_the_bug.md)

## Knowledge check

Test yourself with the [Module 10 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 11 · Advanced Git](../11_advanced_git/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
