# Git Pro – Module 9 Knowledge Check
**Git internals**

The answer key is at the bottom, and each answer says which lesson file to revisit.

---

**1. Which object stores a file's content?**
- A) tree
- B) blob
- C) commit
- D) ref

**2. What does a tree object contain?**
- A) File contents
- B) Names pointing to blobs and other trees
- C) The commit message
- D) Branch names

**3. Two files with identical content in a commit are stored as...**
- A) two blobs
- B) one blob
- C) a diff
- D) a tag

**4. Does Git store diffs or snapshots?**
- A) Diffs between commits
- B) Snapshots (trees); diffs are computed on demand
- C) Only the latest version
- D) Zip files

**5. What is a branch, physically?**
- A) A folder of files
- B) A ref: a small file holding a commit ID
- C) A database table
- D) A tag object

**6. What's in .git/HEAD normally?**
- A) A commit ID
- B) ref: refs/heads/main
- C) The remote URL
- D) The last message

**7. HEAD^2 means...**
- A) two commits back
- B) the second parent of a merge commit
- C) the second branch
- D) HEAD twice

**8. Which plumbing command turns the index into a tree?**
- A) git write-tree
- B) git commit-tree
- C) git hash-object
- D) git update-ref

**9. What does git update-ref refs/heads/main <id> do?**
- A) Creates a tag
- B) Moves the main branch to that commit
- C) Pushes main
- D) Deletes main

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Revisit |
|---|--------|---------|
| 1 | B | `01_objects.md` |
| 2 | B | `01_objects.md` |
| 3 | B | `01_objects.md` |
| 4 | B | `01_objects.md` |
| 5 | B | `02_refs_and_head.md` |
| 6 | B | `02_refs_and_head.md` |
| 7 | B | `02_refs_and_head.md` |
| 8 | A | `03_commit_by_hand.md` |
| 9 | B | `03_commit_by_hand.md` |

</details>

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
