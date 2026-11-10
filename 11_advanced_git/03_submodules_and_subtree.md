# Module 11 · Reusing another repository: submodules (and subtree)

A SUBMODULE is a pointer from your repo to a specific commit of another repo, checked out in a sub-folder.

```text
git submodule add <url> libs/logger         add it (creates .gitmodules)
git clone --recurse-submodules <url>        clone with submodules
git submodule update --init --recursive     fetch them after a normal clone
git submodule update --remote               move to the library's newest commit
```

Alternatives: a git SUBTREE copies the other repo's files (and optionally history) into a folder: simpler for users, harder to send changes back. Usually best of all: a normal package (pip, npm) with a version number.

> 🧠 **Picture it:** A submodule is a bookmark to page N of someone else's book, glued into your book; it doesn't follow their later pages until you move it.

**Why it matters:** Shared code (design systems, SDKs, infra modules) has to live somewhere.

## See it

```mermaid
flowchart LR
    S["shop repo"] -- "libs/logger points to commit b78ae7c" --> L["logger repo"]
```

## Try it yourself

Open **Git Bash** (Windows) or a terminal (macOS/Linux) in an empty practice folder and type along. Lines starting with `$` are commands; the lines below them are what Git prints.

```bash
mkdir project && cd project
```

**Setup** (copy and paste this first):

```bash
git init ../logger
cd ../logger
echo "def log(msg): print(msg)" > logger.py
git add logger.py
git commit -m "Logger v1"
cd ../project
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
```

### 1. Add the logger repository as a submodule

```console
$ git submodule add ../logger libs/logger
Cloning into '~/project/libs/logger'...
done.
$ cat .gitmodules
[submodule "libs/logger"]
	path = libs/logger
	url = ../logger
$ git status --short
A  .gitmodules
A  libs/logger
$ git commit -qm "Add logger submodule"
$ git submodule status
 86f312dde326d19e9da4b9f5dd7726db9597d4fa libs/logger (heads/main)
```

### 2. The library moves on; your repo stays pinned until you update it

```console
$ cd ../logger
$ echo "def warn(msg): print('WARN', msg)" >> logger.py
$ git commit -qam "Logger v2: add warn"
$ cd ../project
$ git submodule status
 86f312dde326d19e9da4b9f5dd7726db9597d4fa libs/logger (heads/main)
$ git submodule update --remote libs/logger
Submodule path 'libs/logger': checked out 'b78ae7c91e8e988580a92f1c76327894f8743497'
From ~/logger
   86f312d..b78ae7c  main       -> origin/main
$ git status --short
 M libs/logger
$ git commit -qam "Update logger to v2"
$ git submodule status
 b78ae7c91e8e988580a92f1c76327894f8743497 libs/logger (remotes/origin/HEAD)
```

### 3. Clone a project that has submodules

```console
$ cd ..
$ git clone -q --recurse-submodules project shop-copy
$ cd shop-copy
$ git submodule status
 b78ae7c91e8e988580a92f1c76327894f8743497 libs/logger (heads/main)
$ cat libs/logger/logger.py
def log(msg): print(msg)
def warn(msg): print('WARN', msg)
```

> ⚠️ **Watch out:** Forgetting --recurse-submodules gives you empty folders; and a submodule sits in detached HEAD at the pinned commit.

**In real jobs:** Pinned Terraform modules or a shared protocol definitions repo.

## Interview question

**Submodule vs subtree vs package?**

Submodule = a pinned pointer to another repo; subtree = a copy merged into yours; a package = versioned dependency, usually the cleanest.

[← Back to the module](README.md)
