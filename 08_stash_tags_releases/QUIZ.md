# Git Pro – Module 8 Knowledge Check
**Stash, tags & releases**

The answer key is at the bottom, and each answer says which lesson file to revisit.

---

**1. What does git stash do?**
- A) Deletes your changes
- B) Saves uncommitted changes on a stack and cleans the working tree
- C) Commits to a hidden branch on GitHub
- D) Creates a tag

**2. Which option also stashes new, untracked files?**
- A) -a
- B) -u (--include-untracked)
- C) --new
- D) -f

**3. git stash pop vs git stash apply?**
- A) Same thing
- B) pop re-applies and removes the stash; apply keeps it
- C) apply deletes it
- D) pop pushes to GitHub

**4. Which tag type should you use for releases?**
- A) Lightweight
- B) Annotated (git tag -a)
- C) Either, it's identical
- D) A branch

**5. Are tags pushed by a plain git push?**
- A) Yes, always
- B) No: git push origin <tag>, --tags or --follow-tags
- C) Only annotated ones
- D) Only on GitHub

**6. v1.4.2 -> you add a backwards-compatible feature. Next version?**
- A) 1.4.3
- B) 1.5.0
- C) 2.0.0
- D) 1.4.2.1

**7. What does 'v1.0.1-1-g8690ec1' from git describe mean?**
- A) Version 1.0.1.1
- B) 1 commit after tag v1.0.1, at commit 8690ec1
- C) A broken tag
- D) Branch name

**8. Which command lists commits in v1.1.0 that are not in v1.0.0?**
- A) git log v1.1.0..v1.0.0
- B) git log v1.0.0..v1.1.0
- C) git diff v1.0.0
- D) git tag -l

**9. Who contributed to a release, and how much?**
- A) git blame
- B) git shortlog -sn A..B
- C) git status
- D) git stash list

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Revisit |
|---|--------|---------|
| 1 | B | `01_stash.md` |
| 2 | B | `01_stash.md` |
| 3 | B | `01_stash.md` |
| 4 | B | `02_tags_and_semver.md` |
| 5 | B | `02_tags_and_semver.md` |
| 6 | B | `02_tags_and_semver.md` |
| 7 | B | `02_tags_and_semver.md` |
| 8 | B | `03_release_notes.md` |
| 9 | B | `03_release_notes.md` |

</details>

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
