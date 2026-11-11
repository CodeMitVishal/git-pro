# Git Pro

[![YouTube: CodeMitVishal](https://img.shields.io/badge/YouTube-CodeMitVishal-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/@CodeMitVishal)
[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-support%20us-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/codemitvishal)

**Git from zero to hero: deep, but simple.**

Learn Git the way professional teams use it: commits, branches, rebase, GitHub teamwork, releases, internals and debugging. Learn the answers to the questions every interview asks, too. No experience needed.

**Only Git, no programming.** Every lesson shows an everyday picture, a **commit-graph diagram**, then real Git commands with their real output, and ends with *Try it yourself* commands you type in Git Bash. Every exercise gives you a **broken practice repository** to fix, plus a checker that tells you when you got it right.

## What's inside every module

| | |
|---|---|
| 📊 **Slides** | teaching-first slides: why → picture → real commands with real output → common mistake → real job → interview answer. One PDF per module in [`slides/modules/`](slides/modules/), or the [full course PDF](slides/git-pro-slides.pdf) |
| 📖 **Lessons** | Markdown pages with diagrams, real commands + real output, *Try it yourself*, common mistakes, real-job use and an interview question |
| 🧪 **Exercise + solution** | `setup.sh` builds a practice repo, you fix it with Git, `check.sh` verifies it (solutions are plain Git commands) |
| 🧩 **Quiz** | test yourself; every answer tells you which lesson to revisit |
| 🎤 **Interview Q&A** | an `INTERVIEW.md` in every module, plus the [interview prep](interview_prep/README.md) section (Top 50, cheat sheet) |

## Course map

| # | Module | You'll be able to… |
|---|---|---|
| 01 | [Git basics](01_git_basics/README.md) | explain version control, install and configure Git |
| 02 | [Your first repository](02_first_repository/README.md) | add, commit, diff, read history, use .gitignore |
| 03 | [Undoing things](03_undoing_things/README.md) | restore, amend, reset, revert, rescue with reflog |
| 04 | [Branches & merging](04_branches_merging/README.md) | branch, merge, resolve conflicts |
| 05 | [Rebase & rewriting history](05_rebase_history/README.md) | rebase, squash, reword, cherry-pick |
| 06 | [Remotes & GitHub](06_remotes_github/README.md) | clone, push, pull, fetch, force-push safely |
| 07 | [Team workflows](07_team_workflows/README.md) | GitHub flow, PRs, reviews, Conventional Commits |
| 08 | [Stash, tags & releases](08_stash_tags_releases/README.md) | stash, tag, SemVer, release notes |
| 09 | [Git internals](09_git_internals/README.md) | explain blobs, trees, commits, refs, HEAD |
| 10 | [Debugging with history](10_debugging_history/README.md) | log, blame, pickaxe, bisect |
| 11 | [Advanced Git](11_advanced_git/README.md) | hooks, worktrees, submodules, line endings, secrets, LFS |
| 12 | [Capstone: rescue a messy repo](12_capstone/README.md) | fix any broken repository and ship a release |

## Quick start

You only need **Git**. On Windows use **Git Bash** (it comes with Git for Windows); on macOS and Linux any terminal works.

```bash
git clone https://github.com/CodeMitVishal/git-pro.git
```

```bash
cd git-pro
```

Start with the first lesson: [`01_git_basics/01_why_version_control.md`](01_git_basics/01_why_version_control.md).

Exercises work in three steps. First, create the practice repository in `playground/ex01`:

```bash
bash exercises/ex01_first_repo/setup.sh
```

Then `cd playground/ex01` and use Git to solve the task in [`exercises/ex01_first_repo/README.md`](exercises/ex01_first_repo/README.md). Finally, check your work (from the course folder):

```bash
bash exercises/ex01_first_repo/check.sh
```

## How to study

1. **Read the slides** for the module (or watch the video when it's out).
2. **Read each lesson** and type its *Try it yourself* commands in a new empty folder.
3. **Do the exercise** until it says *All checks passed!* (solutions are in [`solutions/`](solutions/)).
4. **Take the quiz**, then answer the module's interview questions out loud.

## Support the channel

If this course helps you:

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it ⭐
- Next course: **[Python Pro](https://github.com/CodeMitVishal/python-pro)**
