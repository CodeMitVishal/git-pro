# Git Pro – Module 11 Knowledge Check
**Advanced Git**

The answer key is at the bottom, and each answer says which lesson file to revisit.

---

**1. Which hook can block a commit before it's created?**
- A) post-commit
- B) pre-commit
- C) post-merge
- D) pre-receive

**2. Why aren't hooks shared when you clone?**
- A) They're secret
- B) They live in .git/hooks, which isn't cloned; share via pre-commit or core.hooksPath
- C) GitHub deletes them
- D) They're shared

**3. Why must CI repeat the hook checks?**
- A) CI is faster
- B) Hooks can be skipped with --no-verify or not installed
- C) Hooks don't work on Linux
- D) It doesn't need to

**4. What does git worktree add ../hotfix hotfix/x do?**
- A) Copies the repo
- B) Checks out hotfix/x in a second folder sharing the same repository
- C) Creates a submodule
- D) Stashes changes

**5. A submodule points to...**
- A) the latest commit of another repo
- B) a specific (pinned) commit of another repo
- C) a zip file
- D) a branch name only

**6. How do you clone a repo including its submodules?**
- A) git clone --all
- B) git clone --recurse-submodules
- C) git submodule clone
- D) git pull --submodules

**7. Which .gitattributes line normalises text files to LF?**
- A) * binary
- B) * text=auto eol=lf
- C) eol=crlf *
- D) *.txt -diff

**8. You pushed an API key. First step?**
- A) git filter-repo
- B) Rotate/revoke the key
- C) Force push
- D) Delete the repo

**9. What is Git LFS for?**
- A) Faster merges
- B) Storing large binaries outside normal Git history via pointer files
- C) Encrypting secrets
- D) Signing commits

**10. Which clone downloads only the latest snapshot?**
- A) git clone --depth 1
- B) git clone --bare
- C) git clone --mirror
- D) git clone -b main

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Revisit |
|---|--------|---------|
| 1 | B | `01_hooks.py` |
| 2 | B | `01_hooks.py` |
| 3 | B | `01_hooks.py` |
| 4 | B | `02_worktrees.py` |
| 5 | B | `03_submodules_and_subtree.py` |
| 6 | B | `03_submodules_and_subtree.py` |
| 7 | B | `04_line_endings_and_attributes.py` |
| 8 | B | `05_secrets_big_files_and_signing.md` |
| 9 | B | `05_secrets_big_files_and_signing.md` |
| 10 | A | `05_secrets_big_files_and_signing.md` |

</details>

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
