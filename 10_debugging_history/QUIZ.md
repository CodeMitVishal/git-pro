# Git Pro – Module 10 Knowledge Check
**Debugging with history**

The answer key is at the bottom, and each answer says which lesson file to revisit.

---

**1. Which command lists commits whose message mentions 'coupon'?**
- A) git log -S coupon
- B) git log --grep=coupon
- C) git grep coupon
- D) git blame coupon

**2. How do you list commits that touched cart.py, even across renames?**
- A) git log cart.py --all
- B) git log --follow -- cart.py
- C) git show cart.py
- D) git diff cart.py

**3. What does git shortlog -sn HEAD show?**
- A) Short commit IDs
- B) Number of commits per author
- C) Stashes
- D) Tags

**4. What does git blame show for each line?**
- A) Who wrote it first
- B) The last commit and author that changed it
- C) Every change ever
- D) Bugs

**5. Which option finds commits that added or removed the text 'discount'?**
- A) git log --grep=discount
- B) git log -S discount
- C) git blame discount
- D) git log -p

**6. How do you search 'rate' in the code of an old version?**
- A) git grep -n rate v1.0.0
- B) git log rate
- C) git find rate
- D) grep rate .git

**7. What does git bisect do?**
- A) Splits a commit in two
- B) Binary-searches history for the first bad commit
- C) Deletes bad commits
- D) Compares two branches

**8. With git bisect run <cmd>, what does exit code 0 mean?**
- A) bad
- B) good
- C) skip
- D) abort

**9. About how many steps does bisect need for 1,000 commits?**
- A) 1000
- B) about 10
- C) 100
- D) 2

**10. How do you finish a bisect session?**
- A) git bisect stop
- B) git bisect reset
- C) git reset --hard
- D) git bisect done

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Revisit |
|---|--------|---------|
| 1 | B | `01_log_like_a_pro.md` |
| 2 | B | `01_log_like_a_pro.md` |
| 3 | B | `01_log_like_a_pro.md` |
| 4 | B | `02_blame_and_pickaxe.md` |
| 5 | B | `02_blame_and_pickaxe.md` |
| 6 | A | `02_blame_and_pickaxe.md` |
| 7 | B | `03_bisect.md` |
| 8 | B | `03_bisect.md` |
| 9 | B | `03_bisect.md` |
| 10 | B | `03_bisect.md` |

</details>

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
