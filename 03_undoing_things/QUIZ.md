# Git Pro – Module 3 Knowledge Check
**Undoing things**

The answer key is at the bottom, and each answer says which lesson file to revisit.

---

**1. Which command throws away unstaged changes to app.py?**
- A) git reset app.py
- B) git restore app.py
- C) git revert app.py
- D) git rm app.py

**2. How do you unstage a file but keep your edit?**
- A) git restore --staged file
- B) git reset --hard
- C) git rm file
- D) git commit --amend

**3. You forgot a file in your last (unpushed) commit. Best fix?**
- A) Make a new commit 'forgot file'
- B) git add file; git commit --amend --no-edit
- C) git revert HEAD
- D) Delete the repo

**4. Why shouldn't you amend a pushed commit?**
- A) It's slow
- B) Amending creates a new commit ID, rewriting history others already have
- C) Git forbids it
- D) It deletes the branch

**5. git reset --soft HEAD~3 keeps the changes...**
- A) deleted
- B) staged
- C) unstaged
- D) in a stash

**6. Which reset mode throws changes away?**
- A) --soft
- B) --mixed
- C) --hard
- D) --keep

**7. A bad commit is already on shared main. What do you use?**
- A) git reset --hard
- B) git revert <commit>
- C) git commit --amend
- D) git push --force

**8. You did git reset --hard and lost commits. What helps?**
- A) Nothing, they're gone
- B) git reflog, then reset or branch to the old commit
- C) git status
- D) git stash pop

**9. Can reflog recover changes you never committed?**
- A) Yes
- B) No, reflog only tracks where HEAD/branches pointed
- C) Only on Linux
- D) Only for 1 day

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Revisit |
|---|--------|---------|
| 1 | B | `01_restore_and_amend.py` |
| 2 | A | `01_restore_and_amend.py` |
| 3 | B | `01_restore_and_amend.py` |
| 4 | B | `01_restore_and_amend.py` |
| 5 | B | `02_reset_three_modes.py` |
| 6 | C | `02_reset_three_modes.py` |
| 7 | B | `03_revert_and_reflog.py` |
| 8 | B | `03_revert_and_reflog.py` |
| 9 | B | `03_revert_and_reflog.py` |

</details>

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
