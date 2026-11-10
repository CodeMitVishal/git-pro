# Module 4 · Branches & merging

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-04.pdf) · [Interview Q&A](INTERVIEW.md)

Work in parallel without breaking main: branches as pointers, fast-forward vs three-way merges, and calmly resolving conflicts.

## Lessons

Every lesson is a page to read: an everyday picture, a commit-graph diagram, then real Git commands with their real output. Each lesson ends with **Try it yourself**: type the same commands in Git Bash, in a new empty folder.

| Lesson | File | Key idea |
|---|---|---|
| Branches are pointers | [`01_branches_are_pointers.md`](01_branches_are_pointers.md) | branch, switch -c, HEAD, what a branch really is |
| Fast-forward vs three-way | [`02_fast_forward_and_three_way.md`](02_fast_forward_and_three_way.md) | merge, --no-ff, merge commits with two parents |
| Merge conflicts | [`03_merge_conflicts.md`](03_merge_conflicts.md) | conflict markers, resolve, add, commit, --abort |

## Exercise: Merge a feature and resolve the conflict

Merge a branch that changed the same line as main, resolve the conflict exactly, and clean up the branch.

Open **Git Bash** (Windows) or any terminal in the course folder. The full task is in [`exercises/ex04_merge_conflict/README.md`](../exercises/ex04_merge_conflict/README.md).

```bash
bash exercises/ex04_merge_conflict/setup.sh
```

```bash
bash exercises/ex04_merge_conflict/check.sh
```

- Solution: [`solutions/ex04_merge_conflict.md`](../solutions/ex04_merge_conflict.md)

## Knowledge check

Test yourself with the [Module 4 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 5 · Rebase & rewriting history](../05_rebase_history/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
