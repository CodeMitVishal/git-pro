# Git Pro – Module 4 Knowledge Check
**Branches & merging**

The answer key is at the bottom, and each answer says which lesson file to revisit.

---

**1. What is a branch in Git?**
- A) A copy of all files
- B) A movable pointer to a commit
- C) A folder
- D) A remote server

**2. What does HEAD usually point to?**
- A) The first commit
- B) The current branch
- C) The remote
- D) The newest tag

**3. Which command creates a branch and switches to it?**
- A) git branch -s x
- B) git switch -c x
- C) git new x
- D) git merge -c x

**4. When does a fast-forward merge happen?**
- A) When there are conflicts
- B) When the target branch has no new commits since the branch was created
- C) Always
- D) Only with --no-ff

**5. How many parents does a merge commit have?**
- A) 0
- B) 1
- C) 2 (or more)
- D) It depends on the files

**6. What does git merge --no-ff do?**
- A) Refuses to merge
- B) Always creates a merge commit, even if a fast-forward is possible
- C) Deletes the branch
- D) Skips conflicts

**7. To merge feature into main you...**
- A) stay on feature, git merge main
- B) switch to main, git merge feature
- C) git merge feature main from anywhere
- D) git push feature

**8. git status shows 'UU banner.txt'. What does it mean?**
- A) Untracked twice
- B) Unmerged: the file has a conflict
- C) Updated upstream
- D) It was renamed

**9. How do you cancel a merge that has conflicts?**
- A) git reset --soft
- B) git merge --abort
- C) git revert
- D) Delete the file

**10. After editing the conflicted file, what's next?**
- A) git push
- B) git add the file, then git commit
- C) git merge again
- D) git stash

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Revisit |
|---|--------|---------|
| 1 | B | `01_branches_are_pointers.py` |
| 2 | B | `01_branches_are_pointers.py` |
| 3 | B | `01_branches_are_pointers.py` |
| 4 | B | `02_fast_forward_and_three_way.py` |
| 5 | C | `02_fast_forward_and_three_way.py` |
| 6 | B | `02_fast_forward_and_three_way.py` |
| 7 | B | `02_fast_forward_and_three_way.py` |
| 8 | B | `03_merge_conflicts.py` |
| 9 | B | `03_merge_conflicts.py` |
| 10 | B | `03_merge_conflicts.py` |

</details>

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
