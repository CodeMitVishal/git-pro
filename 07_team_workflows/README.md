# Module 7 · Team workflows

[← Back to the course](../README.md) · [Slides](../slides/modules/Module-07.pdf) · [Interview Q&A](INTERVIEW.md)

How real teams use Git: GitHub flow, the three merge buttons, commit messages tools can read, branching strategies (GitHub flow, Git flow, trunk-based), pull requests and code review.

## Lessons

Every lesson runs real Git commands in a throwaway sandbox and prints them with their output. Your own repositories are never touched.

| Lesson | File | Key idea |
|---|---|---|
| GitHub flow | [`01_github_flow.py`](01_github_flow.py) | branch → PR → review → merge; merge vs squash vs rebase merge |
| Conventional Commits | [`02_conventional_commits.py`](02_conventional_commits.py) | feat/fix/docs, semantic versions, generated release notes |
| Branching strategies | [`03_branching_strategies.md`](03_branching_strategies.md) | GitHub flow vs Git flow vs trunk-based, feature flags |
| Pull requests & reviews | [`04_pull_requests_and_reviews.md`](04_pull_requests_and_reviews.md) | good PRs, reviewing, branch protection, CODEOWNERS |

```bash
python 07_team_workflows/01_github_flow.py
```

## Exercise: Commits a reviewer will love

Split three unrelated changes into three Conventional Commits (feat, fix, docs).

```bash
python exercises/ex07_conventional_commits.py setup
```

```bash
python exercises/ex07_conventional_commits.py check
```

- Solution: [`solutions/ex07_conventional_commits.py`](../solutions/ex07_conventional_commits.py)

## Knowledge check

Test yourself with the [Module 7 quiz](QUIZ.md), then practise the [interview questions](INTERVIEW.md) out loud.

**Next up:** [Module 8 · Stash, tags & releases](../08_stash_tags_releases/README.md) →

---

## ☕ Enjoyed this module?

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
