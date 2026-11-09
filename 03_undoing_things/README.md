# Module 3 · Undoing things

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-03.pdf) · [Interview Q&A](INTERVIEW.md)

Fix any mistake: throw away edits, unstage, fix the last commit, move a branch back, undo shared commits safely, and rescue "lost" work with the reflog.

## Lessons

Every lesson runs real Git commands in a throwaway sandbox and prints them with their output. Your own repositories are never touched.

| Lesson | File | Key idea |
|---|---|---|
| restore & amend | [`01_restore_and_amend.py`](01_restore_and_amend.py) | discard edits, unstage, fix the last commit |
| reset: soft, mixed, hard | [`02_reset_three_modes.py`](02_reset_three_modes.py) | move the branch back, three ways |
| revert & reflog | [`03_revert_and_reflog.py`](03_revert_and_reflog.py) | safe undo on shared branches; the safety net |

```bash
python 03_undoing_things/01_restore_and_amend.py
```

## Exercise: Undo three mistakes

Discard a messy edit, undo a bad commit on a shared branch, and bring a deleted branch back.

```bash
python exercises/ex03_undo_mistakes.py setup
```

```bash
python exercises/ex03_undo_mistakes.py check
```

- Solution: [`solutions/ex03_undo_mistakes.py`](../solutions/ex03_undo_mistakes.py)

## Knowledge check

Test yourself with the [Module 3 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 4 · Branches & merging](../04_branches_merging/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
