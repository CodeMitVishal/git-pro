# Top 50 Git interview questions

These are short answers you can say in one breath. Each section links to the module with commands, examples and follow-up questions.

[← Interview prep](README.md)

---

## Basics ([01](../01_git_basics/INTERVIEW.md) · [02](../02_first_repository/INTERVIEW.md))

1. **What is Git?** A distributed version control system: it tracks snapshots of a project with who, when and why, and every clone has the full history.
2. **Git vs GitHub?** Git is the tool. GitHub, GitLab and Azure DevOps host repositories and add PRs, reviews and CI.
3. **What is a commit?** An immutable snapshot (a tree) plus parent(s), author, date and message, identified by a hash.
4. **What are the three areas?** The working tree, the staging area (index) and the repository (.git).
5. **What does git add do?** Copies changes into the staging area for the next commit.
6. **git diff vs git diff --staged?** Unstaged changes vs staged changes.
7. **A file is in .gitignore but still tracked. Why?** It was committed before. Run `git rm --cached` and commit.
8. **What makes a good commit message?** A short imperative summary, a blank line, then why. One logical change per commit.

## Undoing ([03](../03_undoing_things/INTERVIEW.md))

9. **reset vs revert?** reset moves the branch (rewrites local history). revert adds an undo commit (safe on shared branches).
10. **reset --soft / --mixed / --hard?** Each keeps the changes differently: staged, unstaged, or discarded.
11. **How do you fix the last commit?** `git commit --amend`, only if it isn't pushed.
12. **How do you recover lost commits?** `git reflog`, then `git reset` or `git branch` to the old commit ID.
13. **restore vs reset vs checkout?** restore works on files, reset works on the branch, and checkout is the old all-in-one command (now switch + restore).
14. **How do you undo a pushed merge?** `git revert -m 1 <merge-commit>`.

## Branching & merging ([04](../04_branches_merging/INTERVIEW.md) · [05](../05_rebase_history/INTERVIEW.md))

15. **What is a branch?** A lightweight movable pointer to a commit. HEAD points to the current branch.
16. **Fast-forward vs three-way merge?** If the target hasn't moved, the pointer just moves. Otherwise you get a merge commit with two parents.
17. **How do you resolve a conflict?** Edit the file to the final content, remove the markers, `git add`, commit (or `--abort`), and test.
18. **merge vs rebase?** merge keeps true history with merge commits. rebase replays your commits for a linear history.
19. **The golden rule of rebase?** Never rebase commits that others already have.
20. **How do you squash commits?** `git rebase -i` with squash/fixup, `git reset --soft` + one commit, or Squash and merge.
21. **What is cherry-pick?** It copies specific commits to another branch, e.g. backporting a hotfix (`-x`).
22. **What is a detached HEAD?** HEAD points at a commit, not a branch. Create a branch to keep new commits.

## Remotes & collaboration ([06](../06_remotes_github/INTERVIEW.md) · [07](../07_team_workflows/INTERVIEW.md))

23. **fetch vs pull?** fetch updates origin/* only. pull = fetch + merge (or rebase).
24. **What is origin?** The default name for the remote you cloned from.
25. **Why is your push rejected?** The remote has commits you don't have. Run `pull --rebase`, then push.
26. **--force vs --force-with-lease?** with-lease refuses if the remote has commits you haven't seen.
27. **What is a remote-tracking branch?** A local read-only copy of a remote branch, such as origin/main.
28. **How do you work with a fork?** origin is your fork and upstream is the original: fetch upstream and rebase.
29. **Describe your workflow.** GitHub flow: short branches, PRs, CI, review, squash merge into a protected main.
30. **GitHub flow vs Git flow vs trunk-based?** Respectively: main + short branches; develop/release/hotfix branches; daily integration with feature flags.
31. **Merge commit vs squash vs rebase merge?** Full history, one commit per PR, or linear with every commit.
32. **What makes a good PR?** It's small, has a clear description, green CI and is self-reviewed.
33. **What is branch protection?** No direct or force pushes, required reviews and status checks, CODEOWNERS.
34. **What are Conventional Commits?** `type(scope): summary`, used to automate changelogs and SemVer.

## Releases ([08](../08_stash_tags_releases/INTERVIEW.md))

35. **What does git stash do?** It shelves uncommitted changes and cleans the tree (`-u` for untracked). `pop` restores them.
36. **Lightweight vs annotated tag?** A lightweight tag is just a name. An annotated tag is an object with tagger, date and message; use it for releases.
37. **What is SemVer?** MAJOR.MINOR.PATCH: breaking changes, features, fixes.
38. **What changed between two releases?** `git log v1.0.0..v1.1.0 --oneline`.

## Internals ([09](../09_git_internals/INTERVIEW.md))

39. **How does Git store data?** Content-addressed objects (blob, tree, commit, tag) plus refs.
40. **Snapshots or diffs?** Snapshots. Unchanged files reuse blobs, and packfiles compress.
41. **Why do IDs change after a rebase?** A commit's hash includes its parent, tree, metadata and message.
42. **What happens on git commit?** write-tree → commit-tree → update the branch ref.
43. **HEAD~ vs HEAD^?** `~n` goes n first-parents back. `^n` picks the n-th parent of a merge.

## Debugging & advanced ([10](../10_debugging_history/INTERVIEW.md) · [11](../11_advanced_git/INTERVIEW.md) · [12](../12_capstone/INTERVIEW.md))

44. **How do you find the commit that introduced a bug?** `git bisect` (with `run` and a reproduction script).
45. **When was some code added or removed?** `git log -S "text"` (the pickaxe), or `-G` for a regex.
46. **Who changed this line?** `git blame -L`, then `git show` the commit and read its PR.
47. **What are Git hooks?** Scripts on events (pre-commit, commit-msg, pre-push). Share them with pre-commit, and repeat the checks in CI.
48. **You pushed a secret. What now?** Rotate it, remove it with filter-repo, force-push, everyone re-clones, then prevent it next time.
49. **Submodule vs subtree?** A submodule is a pinned pointer to another repo. A subtree is a copy merged into yours.
50. **Committed to main by mistake?** `git branch feature/x`, `git reset --hard origin/main`, then continue on the branch.

---

☕ [Buy me a coffee](https://buymeacoffee.com/codemitvishal) · ▶️ [Subscribe to CodeMitVishal](https://www.youtube.com/@CodeMitVishal)
