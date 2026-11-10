# Module 5 · Interactive rebase: clean up your commits before a pull request

```text
git rebase -i HEAD~3      opens a "todo list" of your last 3 commits in the editor:
```

```text
pick a1b2c3d Add search
pick d4e5f6a fix typo
pick 0a1b2c3 WIP
```

```text
Change the word in front of each commit:
  pick    keep it
  reword  keep it, change the message
  squash  melt it into the commit above (combine the messages)
  fixup   melt it into the commit above (throw its message away)
  drop    delete the commit
You can also reorder the lines.
```

```text
git commit --fixup <commit> + git rebase -i --autosquash  does the squashing for you.
```

> 🧠 **Picture it:** Editing a draft before publishing: merge paragraphs, fix titles, delete the scribbles.

**Why it matters:** Reviewers want a few meaningful commits, not "wip", "fix", "fix again".

## See it

```mermaid
flowchart LR
    A["Add search"] --> B["WIP"] --> C["fix typo"]
    C -- "git rebase -i HEAD~3<br/>pick, fixup, fixup" --> D["Add search (one clean commit)"]
```

## Try it yourself

Open **Git Bash** (Windows) or a terminal (macOS/Linux) in an empty practice folder and type along. Lines starting with `$` are commands; the lines below them are what Git prints.

```bash
mkdir project && cd project
```

**Setup** (copy and paste this first):

```bash
git init
echo "shop" > shop.txt
git add shop.txt
git commit -m "Add shop"
echo "search box" > search.txt
git add search.txt
git commit -m "Add search"
echo "search boxx" > search.txt
git commit -qam "WIP"
echo "search box with results" > search.txt
git commit -qam "fix typo"
```

### 1. Messy history: three commits for one feature

```console
$ git log --oneline
4f5af1c fix typo
0a937f5 WIP
8510441 Add search
04f6802 Add shop
```

### 2. The todo list you would type in the editor:

pick 8510441 Add search  
fixup 0a937f5 WIP  
fixup 4f5af1c fix typo

```console
$ git rebase -i HEAD~3
Rebasing (2/3)
Rebasing (3/3)
Successfully rebased and updated refs/heads/main.
```

```console
$ git log --oneline
2799796 Add search
04f6802 Add shop
$ git show --stat HEAD
commit 279979608baf43a4092a4c09114c30567f91bf4d
Author: Vishal <vishal@example.com>
Date:   Tue Oct 27 08:05:00 2026 +0000

    Add search

 search.txt | 1 +
 1 file changed, 1 insertion(+)
```

### 3. Automatic version: commit --fixup + rebase --autosquash

```console
$ echo "search box with results and filters" > search.txt
$ git commit -q -a --fixup HEAD
$ git log --oneline
8fbeb79 fixup! Add search
2799796 Add search
04f6802 Add shop
$ GIT_SEQUENCE_EDITOR=true git rebase -i --autosquash HEAD~2
Rebasing (2/2)
Successfully rebased and updated refs/heads/main.
$ git log --oneline
f784c55 Add search
04f6802 Add shop
```

> ⚠️ **Watch out:** Only rewrite YOUR unpushed (or your own branch's) commits. If you already pushed the branch, you'll need git push --force-with-lease (Module 6).

**In real jobs:** Squash work-in-progress commits before review; or use "Squash and merge".

## Interview question

**How do you combine several commits into one?**

git rebase -i and mark them squash/fixup, or git reset --soft <base> and commit once.

[← Back to the module](README.md)
