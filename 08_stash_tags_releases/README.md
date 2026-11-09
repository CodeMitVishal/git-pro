# Module 8 · Stash, tags & releases

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-08.pdf) · [Interview Q&A](INTERVIEW.md)

Put unfinished work aside in seconds, give releases permanent names with tags and Semantic Versioning, and answer "what changed in this release?".

## Lessons

Every lesson runs real Git commands in a throwaway sandbox and prints them with their output. Your own repositories are never touched.

| Lesson | File | Key idea |
|---|---|---|
| git stash | [`01_stash.py`](01_stash.py) | push -u, list, pop, apply, drop |
| Tags & SemVer | [`02_tags_and_semver.py`](02_tags_and_semver.py) | lightweight vs annotated, pushing tags, describe, MAJOR.MINOR.PATCH |
| Release notes | [`03_release_notes.py`](03_release_notes.py) | log A..B, diff --stat, shortlog between tags |

```bash
python 08_stash_tags_releases/01_stash.py
```

## Exercise: Interrupted: ship a hotfix release

Stash unfinished work, tag a hotfix release, and restore your work exactly as it was.

```bash
python exercises/ex08_hotfix_release.py setup
```

```bash
python exercises/ex08_hotfix_release.py check
```

- Solution: [`solutions/ex08_hotfix_release.py`](../solutions/ex08_hotfix_release.py)

## Knowledge check

Test yourself with the [Module 8 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 9 · Git internals](../09_git_internals/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
