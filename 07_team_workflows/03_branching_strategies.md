# Module 7 · Branching strategies

[← Module 7](README.md)

Every team picks a strategy for how branches flow into production. You'll be asked about these in interviews: know all three and say which you'd choose and why.

## 1. GitHub flow (most common today)

```
main ──●────────●──────────●────  (always deployable, deployed on every merge)
        \      /  \       /
         ●──●─●    ●──●──●        feature branches, merged via pull requests
```

- One long-lived branch: `main`.
- Short-lived feature branches, pull requests, CI and review, then merge and deploy.
- **Best for:** web apps and services with continuous deployment.

## 2. Git flow (classic, release-based)

```
main     ──●──────────────●────────   tagged releases only (v1.0, v1.1)
develop  ──●──●───●───●───●──●─────   integration branch
feature/ ──────●─●/                   from and into develop
release/ ───────────●─●/              stabilise a version, then merge to main + develop
hotfix/  ──────────────────●/         urgent fix from main, merged to main + develop
```

- Two long-lived branches (`main`, `develop`) plus feature, release and hotfix branches.
- **Best for:** software with versioned releases (desktop apps, SDKs, embedded systems) and several supported versions.
- **Downside:** heavy process and long-lived branches mean more merge pain; it's overkill for continuous deployment.

## 3. Trunk-based development

```
main ──●─●─●─●─●─●─●─●──   everyone integrates at least daily
         \●/   \●/          tiny branches living a few hours
```

- Everyone commits to `main` (the trunk) very often, through tiny PRs or directly with pair programming.
- Unfinished features are hidden behind **feature flags**, not branches.
- **Best for:** experienced teams with strong automated tests, aiming for elite delivery speed (DORA metrics).

## Comparison

| | GitHub flow | Git flow | Trunk-based |
|---|---|---|---|
| Long-lived branches | main | main + develop | main |
| Branch lifetime | days | weeks | hours |
| Releases | every merge | planned versions | continuous |
| Unfinished work | stays on a branch | stays on a branch | feature flags |
| Merge conflicts | few | many | very few |

## Release branches and tags

Even with GitHub flow, you can cut `release/2.3` when you need to support an old version, **tag** each release (`v2.3.0`, Module 8), and **cherry-pick** hotfixes into it (Module 5).

## Interview answer

> *"We used GitHub flow: short-lived branches from `main`, pull requests with CI and one approval, squash merge, and automatic deployment from `main`. Unfinished features were behind feature flags. I'd choose Git flow only for products that ship versioned releases and must support several versions at once."*

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
