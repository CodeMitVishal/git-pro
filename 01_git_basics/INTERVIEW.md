# Module 1 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 1](README.md) · [Quiz](QUIZ.md)

---

### 1. What is Git and why do teams use it?

**Say:** Git is a **distributed version control system**. It records snapshots (commits) of a project with who, when and why, lets you compare and restore any version, and lets many developers work in parallel on branches and merge their work.

**Follow-up:** "Centralised vs distributed?" Centralised (SVN) has one server with the history; in Git every clone has the full history, so you can commit, branch and view logs offline.

---

### 2. Git vs GitHub?

**Say:** Git is the tool on your machine. GitHub (or GitLab, Azure DevOps, Bitbucket) is a **hosting service** for Git repositories that adds pull requests, code review, issues and CI.

---

### 3. What is a commit?

**Say:** An immutable snapshot of the whole project plus metadata: author, committer, date, message, and a pointer to its parent commit(s). It's identified by a SHA hash of its content.

```bash
git log --oneline
git show <commit>
```

---

### 4. How do you configure Git on a new machine?

**Say:** Set name and email (stored in every commit), the default branch name and an editor. Use `--local` inside a work repository to use your work email there.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

**Follow-up:** "Where are these stored?" System (/etc/gitconfig), global (~/.gitconfig) and local (.git/config). The local one wins.

---

### 5. How do you see who you are committing as?

**Say:** Run `git config user.name` and `git config user.email`. Add `--show-origin` to see which file the value comes from.

```bash
git config --show-origin user.email
```

---

### 6. What's in the .git folder?

**Say:** The whole repository: the object database (commits, trees, blobs), refs (branches and tags), HEAD, config, hooks and the index. Deleting `.git` deletes the history; the files stay.

**Follow-up:** "Can you recover a project if .git is deleted?" Only from another clone or the remote. That's why pushing to a remote is your backup.

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
