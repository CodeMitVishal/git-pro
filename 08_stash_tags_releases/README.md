# Module 8 · Stash, tags & releases

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-08.pdf) · [Interview Q&A](INTERVIEW.md)

Put unfinished work aside in seconds, give releases permanent names with tags and Semantic Versioning, and answer "what changed in this release?".

## Lessons

Every lesson is a page to read: an everyday picture, a commit-graph diagram, then real Git commands with their real output. Each lesson ends with **Try it yourself**: type the same commands in Git Bash, in a new empty folder.

| Lesson | File | Key idea |
|---|---|---|
| git stash | [`01_stash.md`](01_stash.md) | push -u, list, pop, apply, drop |
| Tags & SemVer | [`02_tags_and_semver.md`](02_tags_and_semver.md) | lightweight vs annotated, pushing tags, describe, MAJOR.MINOR.PATCH |
| Release notes | [`03_release_notes.md`](03_release_notes.md) | log A..B, diff --stat, shortlog between tags |

## Exercise: Interrupted: ship a hotfix release

Stash unfinished work, tag a hotfix release, and restore your work exactly as it was.

Open **Git Bash** (Windows) or any terminal in the course folder. The full task is in [`exercises/ex08_hotfix_release/README.md`](../exercises/ex08_hotfix_release/README.md).

```bash
bash exercises/ex08_hotfix_release/setup.sh
```

```bash
bash exercises/ex08_hotfix_release/check.sh
```

- Solution: [`solutions/ex08_hotfix_release.md`](../solutions/ex08_hotfix_release.md)

## Knowledge check

Test yourself with the [Module 8 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 9 · Git internals](../09_git_internals/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
