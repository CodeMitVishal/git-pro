# Module 4 · Branches & merging

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-04.pdf) · [Interview Q&A](INTERVIEW.md)

Work in parallel without breaking main: branches as pointers, fast-forward vs three-way merges, and calmly resolving conflicts.

## Lessons

Every lesson runs real Git commands in a throwaway sandbox and prints them with their output. Your own repositories are never touched.

| Lesson | File | Key idea |
|---|---|---|
| Branches are pointers | [`01_branches_are_pointers.py`](01_branches_are_pointers.py) | branch, switch -c, HEAD, what a branch really is |
| Fast-forward vs three-way | [`02_fast_forward_and_three_way.py`](02_fast_forward_and_three_way.py) | merge, --no-ff, merge commits with two parents |
| Merge conflicts | [`03_merge_conflicts.py`](03_merge_conflicts.py) | conflict markers, resolve, add, commit, --abort |

```bash
python 04_branches_merging/01_branches_are_pointers.py
```

## Exercise: Merge a feature and resolve the conflict

Merge a branch that changed the same line as main, resolve the conflict exactly, and clean up the branch.

```bash
python exercises/ex04_merge_conflict.py setup
```

```bash
python exercises/ex04_merge_conflict.py check
```

- Solution: [`solutions/ex04_merge_conflict.py`](../solutions/ex04_merge_conflict.py)

## Knowledge check

Test yourself with the [Module 4 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 5 · Rebase & rewriting history](../05_rebase_history/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
