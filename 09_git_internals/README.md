# Module 9 · Git internals

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-09.pdf) · [Interview Q&A](INTERVIEW.md)

Open the hood: blobs, trees, commits and tags in the object database; refs, HEAD and detached HEAD; and a commit built by hand with plumbing commands.

## Lessons

Every lesson is a page to read: an everyday picture, a commit-graph diagram, then real Git commands with their real output. Each lesson ends with **Try it yourself**: type the same commands in Git Bash, in a new empty folder.

| Lesson | File | Key idea |
|---|---|---|
| Objects | [`01_objects.md`](01_objects.md) | blob, tree, commit, tag; cat-file, hash-object; snapshots not diffs |
| Refs & HEAD | [`02_refs_and_head.md`](02_refs_and_head.md) | branches as files, symbolic HEAD, HEAD~ vs HEAD^, detached HEAD |
| A commit by hand | [`03_commit_by_hand.md`](03_commit_by_hand.md) | hash-object → update-index → write-tree → commit-tree → update-ref |

## Exercise: Make a commit without git add or git commit

Create a real commit using only plumbing commands, then inspect the objects you made.

Open **Git Bash** (Windows) or any terminal in the course folder. The full task is in [`exercises/ex09_commit_by_hand/README.md`](../exercises/ex09_commit_by_hand/README.md).

```bash
bash exercises/ex09_commit_by_hand/setup.sh
```

```bash
bash exercises/ex09_commit_by_hand/check.sh
```

- Solution: [`solutions/ex09_commit_by_hand.md`](../solutions/ex09_commit_by_hand.md)

## Knowledge check

Test yourself with the [Module 9 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 10 · Debugging with history](../10_debugging_history/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
