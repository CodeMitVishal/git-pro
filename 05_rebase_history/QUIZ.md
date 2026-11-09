# Git Pro – Module 5 Knowledge Check
**Rebase & rewriting history**

The answer key is at the bottom, and each answer says which lesson file to revisit.

---

**1. What does git rebase main do (on a feature branch)?**
- A) Merges main with a merge commit
- B) Replays the feature commits on top of main
- C) Deletes main
- D) Pushes to main

**2. After a rebase, the rebased commits have...**
- A) the same IDs
- B) new IDs (they are new commits)
- C) no IDs
- D) the IDs of main

**3. What is the golden rule of rebasing?**
- A) Always rebase main
- B) Never rebase commits others already have
- C) Rebase only on Fridays
- D) Never rebase locally

**4. You fixed a conflict during a rebase. Next command?**
- A) git commit
- B) git add file, then git rebase --continue
- C) git merge --continue
- D) git push

**5. In a rebase -i todo list, 'fixup' means...**
- A) drop the commit
- B) melt it into the commit above and discard its message
- C) rename it
- D) stop for editing

**6. Which word lets you change only a commit message?**
- A) pick
- B) reword
- C) squash
- D) exec

**7. What does git commit --fixup HEAD~1 prepare?**
- A) A revert
- B) A commit that --autosquash will melt into HEAD~1
- C) A new branch
- D) A tag

**8. When is cherry-pick the right tool?**
- A) To copy one specific commit (like a hotfix) to another branch
- B) To merge whole branches
- C) To undo a commit
- D) To delete a commit

**9. What does cherry-pick -x add?**
- A) Extra speed
- B) A line recording the original commit ID
- C) A tag
- D) A merge commit

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Revisit |
|---|--------|---------|
| 1 | B | `01_rebase_basics.py` |
| 2 | B | `01_rebase_basics.py` |
| 3 | B | `01_rebase_basics.py` |
| 4 | B | `01_rebase_basics.py` |
| 5 | B | `02_interactive_rebase.py` |
| 6 | B | `02_interactive_rebase.py` |
| 7 | B | `02_interactive_rebase.py` |
| 8 | A | `03_cherry_pick.py` |
| 9 | B | `03_cherry_pick.py` |

</details>

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
