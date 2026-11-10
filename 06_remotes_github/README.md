# Module 6 · Remotes & GitHub

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-06.pdf) · [Interview Q&A](INTERVIEW.md)

Work with a shared repository: clone, push and pull, the difference between fetch and pull, ahead/behind, rejected pushes, and safe force-pushing. A local bare repository plays GitHub, so everything runs offline.

## Lessons

Every lesson is a page to read: an everyday picture, a commit-graph diagram, then real Git commands with their real output. Each lesson ends with **Try it yourself**: type the same commands in Git Bash, in a new empty folder.

| Lesson | File | Key idea |
|---|---|---|
| clone, push, pull | [`01_clone_push_pull.md`](01_clone_push_pull.md) | remotes, origin, push -u, pull; SSH vs HTTPS |
| fetch vs pull | [`02_fetch_vs_pull.md`](02_fetch_vs_pull.md) | origin/main, ahead/behind, pull --rebase |
| Rejected pushes & force | [`03_rejected_push_and_force.md`](03_rejected_push_and_force.md) | non-fast-forward, --force vs --force-with-lease |

## Exercise: Sync with your team

Your push is rejected because a teammate pushed first. Integrate their work and push with a linear history.

Open **Git Bash** (Windows) or any terminal in the course folder. The full task is in [`exercises/ex06_sync_with_team/README.md`](../exercises/ex06_sync_with_team/README.md).

```bash
bash exercises/ex06_sync_with_team/setup.sh
```

```bash
bash exercises/ex06_sync_with_team/check.sh
```

- Solution: [`solutions/ex06_sync_with_team.md`](../solutions/ex06_sync_with_team.md)

## Knowledge check

Test yourself with the [Module 6 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 7 · Team workflows](../07_team_workflows/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
