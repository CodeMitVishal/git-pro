# Git Pro – Module 12 Knowledge Check
**Final exam: Modules 1–12**

The answer key is at the bottom, and each answer says which lesson file to revisit.

---

**1. Which command shows staged changes?**
- A) git diff
- B) git diff --staged
- C) git status -s
- D) git show

**2. A bad commit is on shared main. Undo it how?**
- A) git reset --hard HEAD~1 + force push
- B) git revert <commit>
- C) git commit --amend
- D) Delete the branch

**3. You reset --hard by mistake. What brings the commits back?**
- A) git fsck
- B) git reflog + reset/branch
- C) git stash pop
- D) Nothing

**4. When does a merge create no merge commit?**
- A) Never
- B) When it's a fast-forward
- C) With conflicts
- D) With --no-ff

**5. The golden rule of rebase?**
- A) Rebase main daily
- B) Never rebase commits others already have
- C) Always force push
- D) Only rebase tags

**6. Squash 3 local commits into 1:**
- A) git merge --squash HEAD~3
- B) git rebase -i HEAD~3 (fixup) or git reset --soft HEAD~3 + commit
- C) git revert HEAD~3
- D) git stash

**7. fetch vs pull?**
- A) Identical
- B) fetch updates origin/* only; pull = fetch + merge/rebase
- C) pull only downloads
- D) fetch pushes

**8. Safest way to push a rebased feature branch?**
- A) git push --force
- B) git push --force-with-lease
- C) git push --mirror
- D) Delete and recreate it

**9. 'Squash and merge' gives main...**
- A) every commit + a merge commit
- B) one commit per PR
- C) no commits
- D) a tag

**10. Which tag type for releases?**
- A) lightweight
- B) annotated
- C) branch
- D) stash

**11. Which object stores a file's content?**
- A) tree
- B) blob
- C) commit
- D) ref

**12. Find the commit that introduced a bug fastest:**
- A) git log -p
- B) git bisect
- C) git blame on every file
- D) git stash

**13. When was 'discount' added to the code?**
- A) git log -S discount
- B) git log --grep discount
- C) git status
- D) git tag

**14. First step after pushing an API key?**
- A) git filter-repo
- B) Rotate the key
- C) Make the repo private
- D) Force push

**15. You committed to main by mistake (unpushed). Fix:**
- A) git revert
- B) git branch feature/x; git reset --hard origin/main
- C) git push --force
- D) git stash

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Revisit |
|---|--------|---------|
| 1 | B | `02_first_repository/02_diff_and_log.md` |
| 2 | B | `03_undoing_things/03_revert_and_reflog.md` |
| 3 | B | `03_undoing_things/03_revert_and_reflog.md` |
| 4 | B | `04_branches_merging/02_fast_forward_and_three_way.md` |
| 5 | B | `05_rebase_history/01_rebase_basics.md` |
| 6 | B | `05_rebase_history/02_interactive_rebase.md` |
| 7 | B | `06_remotes_github/02_fetch_vs_pull.md` |
| 8 | B | `06_remotes_github/03_rejected_push_and_force.md` |
| 9 | B | `07_team_workflows/01_github_flow.md` |
| 10 | B | `08_stash_tags_releases/02_tags_and_semver.md` |
| 11 | B | `09_git_internals/01_objects.md` |
| 12 | B | `10_debugging_history/03_bisect.md` |
| 13 | A | `10_debugging_history/02_blame_and_pickaxe.md` |
| 14 | B | `11_advanced_git/05_secrets_big_files_and_signing.md` |
| 15 | B | `01_rescue_walkthrough.md` |

</details>

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
