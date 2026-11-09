# Module 8 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 8](README.md) · [Quiz](QUIZ.md)

---

### 1. What is git stash, and when do you use it?

**Say:** It saves uncommitted changes (`-u` adds untracked files) on a local stack and cleans the working tree, for example to switch branches for an urgent fix. `git stash pop` brings them back. For longer pauses I prefer a WIP commit on a branch, because stashes are easy to forget.

```bash
git stash push -u -m "coupon WIP"
git stash list
git stash pop
```

---

### 2. Lightweight vs annotated tag?

**Say:** A lightweight tag is just a name pointing at a commit. An annotated tag is its own object with tagger, date and message, and can be GPG-signed. Use annotated tags for releases: `git describe` and `--follow-tags` work with them.

```bash
git tag -a v2.3.0 -m "Release 2.3.0"
git push origin v2.3.0
```

---

### 3. Explain Semantic Versioning.

**Say:** MAJOR.MINOR.PATCH. Bump **PATCH** for bug fixes, **MINOR** for backwards-compatible features, **MAJOR** for breaking changes. Pre-releases look like 2.0.0-rc.1.

**Follow-up:** "How do you automate it?" Conventional Commits + semantic-release (or release-please) pick the bump and write the changelog.

---

### 4. How do you see what changed between two releases?

**Say:** `git log v1.0.0..v1.1.0 --oneline` for commits, `git diff --stat v1.0.0 v1.1.0` for files, and `git shortlog -sn v1.0.0..v1.1.0` for contributors.

---

### 5. A tag points to the wrong commit. What do you do?

**Say:** If nobody has pulled it: `git tag -d v1.2.0`, `git push origin :refs/tags/v1.2.0`, then re-tag and push. If it's already public, don't move it; release a new version (v1.2.1) instead.

---

### 6. How are releases usually created in CI/CD?

**Say:** Pushing a version tag (e.g. `v*`) triggers a pipeline that builds, tests, publishes artifacts or images, and creates a GitHub Release with generated notes.

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
