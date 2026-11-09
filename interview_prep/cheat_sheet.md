# Git cheat sheet

[← Interview prep](README.md)

## Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

## Everyday
| Do | Command |
|---|---|
| Start | `git init` · `git clone <url>` |
| See | `git status -sb` · `git diff` · `git diff --staged` |
| Save | `git add <file>` · `git add -p` · `git commit -m "msg"` |
| History | `git log --oneline --graph --all` · `git show <id>` |
| Ignore | `.gitignore` · `git rm --cached <file>` |

## Branches
| Do | Command |
|---|---|
| Create + switch | `git switch -c feature/x` |
| Switch | `git switch main` · `git switch -` (previous) |
| Merge | `git merge feature/x` · `--no-ff` · `--squash` |
| Rebase | `git rebase main` · `git rebase -i HEAD~3` · `--continue` / `--abort` |
| Copy a commit | `git cherry-pick -x <id>` |
| Delete | `git branch -d x` · `git push origin --delete x` |

## Remotes
| Do | Command |
|---|---|
| Inspect | `git remote -v` · `git branch -vv` |
| Get | `git fetch --prune` · `git pull --rebase` |
| Send | `git push -u origin feature/x` · `git push --force-with-lease` |
| Compare | `git log --oneline main..origin/main` |

## Undo
| Situation | Command |
|---|---|
| Discard file edits | `git restore <file>` |
| Unstage | `git restore --staged <file>` |
| Fix last commit | `git commit --amend` |
| Undo local commits | `git reset --soft/--mixed/--hard HEAD~N` |
| Undo shared commit | `git revert <id>` · merge: `git revert -m 1 <id>` |
| Find lost work | `git reflog` → `git branch rescue <id>` |

## Releases & interruptions
| Do | Command |
|---|---|
| Stash | `git stash push -u -m "msg"` · `git stash pop` · `git stash list` |
| Tag | `git tag -a v1.2.0 -m "msg"` · `git push origin v1.2.0` |
| Describe | `git describe --tags` |
| Release notes | `git log --oneline v1.1.0..v1.2.0` · `git shortlog -sn A..B` |

## Investigate
| Question | Command |
|---|---|
| Commits touching a file | `git log --follow -- path` |
| Who changed these lines | `git blame -L 10,20 file` |
| When was text added/removed | `git log -S "text" -p` |
| Search any version | `git grep -n TODO v1.0.0` |
| First bad commit | `git bisect start HEAD v1.0.0` · `git bisect run <test>` · `git bisect reset` |

## Advanced
| Do | Command |
|---|---|
| Second checkout | `git worktree add ../hotfix hotfix/x` |
| Submodules | `git submodule add <url> path` · `git clone --recurse-submodules` |
| Line endings | `.gitattributes`: `* text=auto eol=lf` · `git add --renormalize .` |
| Big files | `git lfs track "*.mp4"` |
| Huge repos | `git clone --depth 1` · `--filter=blob:none` · `git sparse-checkout set dir` |
| Remove a secret | rotate it! then `git filter-repo --replace-text expressions.txt` |

## Plumbing (internals)
`git cat-file -p <id>` · `git ls-tree -r HEAD` · `git hash-object -w f` · `git write-tree` · `git commit-tree` · `git update-ref` · `git rev-parse HEAD`

---

☕ [Buy me a coffee](https://buymeacoffee.com/codemitvishal) · ▶️ [Subscribe to CodeMitVishal](https://www.youtube.com/@CodeMitVishal)
