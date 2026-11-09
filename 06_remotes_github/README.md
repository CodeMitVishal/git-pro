# Module 6 · Remotes & GitHub

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-06.pdf) · [Interview Q&A](INTERVIEW.md)

Work with a shared repository: clone, push and pull, the difference between fetch and pull, ahead/behind, rejected pushes, and safe force-pushing. A local bare repository plays GitHub, so everything runs offline.

## Lessons

Every lesson runs real Git commands in a throwaway sandbox and prints them with their output. Your own repositories are never touched.

| Lesson | File | Key idea |
|---|---|---|
| clone, push, pull | [`01_clone_push_pull.py`](01_clone_push_pull.py) | remotes, origin, push -u, pull; SSH vs HTTPS |
| fetch vs pull | [`02_fetch_vs_pull.py`](02_fetch_vs_pull.py) | origin/main, ahead/behind, pull --rebase |
| Rejected pushes & force | [`03_rejected_push_and_force.py`](03_rejected_push_and_force.py) | non-fast-forward, --force vs --force-with-lease |

```bash
python 06_remotes_github/01_clone_push_pull.py
```

## Exercise: Sync with your team

Your push is rejected because a teammate pushed first. Integrate their work and push with a linear history.

```bash
python exercises/ex06_sync_with_team.py setup
```

```bash
python exercises/ex06_sync_with_team.py check
```

- Solution: [`solutions/ex06_sync_with_team.py`](../solutions/ex06_sync_with_team.py)

## Knowledge check

Test yourself with the [Module 6 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 7 · Team workflows](../07_team_workflows/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
