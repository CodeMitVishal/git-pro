# Git Pro – Module 6 Knowledge Check
**Remotes & GitHub**

The answer key is at the bottom, and each answer says which lesson file to revisit.

---

**1. What is 'origin'?**
- A) A special server
- B) The default name of the remote you cloned from
- C) The first commit
- D) The main branch

**2. What does push -u (--set-upstream) do?**
- A) Uploads faster
- B) Remembers the remote branch so later 'git push'/'git pull' need no arguments
- C) Updates Git
- D) Deletes the remote branch

**3. What does git fetch change?**
- A) Your current branch
- B) Only remote-tracking branches like origin/main
- C) Your working files
- D) Nothing at all

**4. git pull equals...**
- A) git fetch + git merge (or rebase with --rebase)
- B) git push + git fetch
- C) git clone
- D) git status

**5. 'ahead 1, behind 2' means...**
- A) You have 1 commit the remote lacks; it has 2 you lack
- B) The opposite
- C) You must delete 1 commit
- D) The repo is corrupted

**6. Which command lists commits on origin/main that you don't have?**
- A) git log origin/main..main
- B) git log main..origin/main
- C) git diff main
- D) git status

**7. Your push is rejected (fetch first). Best fix?**
- A) git push --force
- B) git pull --rebase, then git push
- C) Delete the remote
- D) git reset --hard

**8. Why --force-with-lease over --force?**
- A) It's faster
- B) It refuses if the remote has commits you haven't seen
- C) It also deletes tags
- D) It merges automatically

**9. Which branches must never be force-pushed?**
- A) Your own feature branches
- B) Shared branches like main
- C) Branches with one commit
- D) Tags

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Revisit |
|---|--------|---------|
| 1 | B | `01_clone_push_pull.py` |
| 2 | B | `01_clone_push_pull.py` |
| 3 | B | `02_fetch_vs_pull.py` |
| 4 | A | `02_fetch_vs_pull.py` |
| 5 | A | `02_fetch_vs_pull.py` |
| 6 | B | `02_fetch_vs_pull.py` |
| 7 | B | `03_rejected_push_and_force.py` |
| 8 | B | `03_rejected_push_and_force.py` |
| 9 | B | `03_rejected_push_and_force.py` |

</details>

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
