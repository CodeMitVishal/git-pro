# Module 3 · Undoing things

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-03.pdf) · [Interview Q&A](INTERVIEW.md)

Fix any mistake: throw away edits, unstage, fix the last commit, move a branch back, undo shared commits safely, and rescue "lost" work with the reflog.

## Lessons

Every lesson is a page to read: an everyday picture, a commit-graph diagram, then real Git commands with their real output. Each lesson ends with **Try it yourself**: type the same commands in Git Bash, in a new empty folder.

| Lesson | File | Key idea |
|---|---|---|
| restore & amend | [`01_restore_and_amend.md`](01_restore_and_amend.md) | discard edits, unstage, fix the last commit |
| reset: soft, mixed, hard | [`02_reset_three_modes.md`](02_reset_three_modes.md) | move the branch back, three ways |
| revert & reflog | [`03_revert_and_reflog.md`](03_revert_and_reflog.md) | safe undo on shared branches; the safety net |

## Exercise: Undo three mistakes

Discard a messy edit, undo a bad commit on a shared branch, and bring a deleted branch back.

Open **Git Bash** (Windows) or any terminal in the course folder. The full task is in [`exercises/ex03_undo_mistakes/README.md`](../exercises/ex03_undo_mistakes/README.md).

```bash
bash exercises/ex03_undo_mistakes/setup.sh
```

```bash
bash exercises/ex03_undo_mistakes/check.sh
```

- Solution: [`solutions/ex03_undo_mistakes.md`](../solutions/ex03_undo_mistakes.md)

## Knowledge check

Test yourself with the [Module 3 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 4 · Branches & merging](../04_branches_merging/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
