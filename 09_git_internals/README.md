# Module 9 · Git internals

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-09.pdf) · [Interview Q&A](INTERVIEW.md)

Open the hood: blobs, trees, commits and tags in the object database; refs, HEAD and detached HEAD; and a commit built by hand with plumbing commands.

## Lessons

Every lesson runs real Git commands in a throwaway sandbox and prints them with their output. Your own repositories are never touched.

| Lesson | File | Key idea |
|---|---|---|
| Objects | [`01_objects.py`](01_objects.py) | blob, tree, commit, tag; cat-file, hash-object; snapshots not diffs |
| Refs & HEAD | [`02_refs_and_head.py`](02_refs_and_head.py) | branches as files, symbolic HEAD, HEAD~ vs HEAD^, detached HEAD |
| A commit by hand | [`03_commit_by_hand.py`](03_commit_by_hand.py) | hash-object → update-index → write-tree → commit-tree → update-ref |

```bash
python 09_git_internals/01_objects.py
```

## Exercise: Make a commit without git add or git commit

Create a real commit using only plumbing commands, then inspect the objects you made.

```bash
python exercises/ex09_commit_by_hand.py setup
```

```bash
python exercises/ex09_commit_by_hand.py check
```

- Solution: [`solutions/ex09_commit_by_hand.py`](../solutions/ex09_commit_by_hand.py)

## Knowledge check

Test yourself with the [Module 9 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 10 · Debugging with history](../10_debugging_history/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
