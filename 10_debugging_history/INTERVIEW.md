# Module 10 · Interview questions (with answers)

Short answers you can say out loud, with commands and the usual follow-up.

[← Module 10](README.md) · [Quiz](QUIZ.md)

---

### 1. How do you find which commit introduced a bug?

**Say:** `git bisect`: mark a known bad commit (often HEAD) and a known good one (the last release tag). Git checks out the middle and I mark it good or bad, so it finds the culprit in about log2(n) steps. With a script that reproduces the bug, `git bisect run` does it all automatically. Finish with `git bisect reset`.

```bash
git bisect start HEAD v2.3.0
git bisect run pytest tests/test_prices.py -x
git bisect reset
```

**Follow-up:** "What if a commit can't be tested (doesn't build)?" git bisect skip, or exit code 125 from the script.

---

### 2. How do you find who changed a line and why?

**Say:** `git blame -L 40,60 file` shows the last commit per line. Then `git show <commit>` and the linked PR or ticket explain why. If a reformat commit hides the real change, use `--ignore-rev` (or `.git-blame-ignore-revs`) or the pickaxe.

---

### 3. How do you find when some code was added or removed?

**Say:** The pickaxe: `git log -S "text"` lists commits where the number of occurrences changed (added or removed). `-G "regex"` matches diffs by regex. Add `-p` to see the changes.

```bash
git log -S "min(discount" --oneline -p
```

---

### 4. What are useful git log filters?

**Say:** `--author`, `--grep` (message), `--since`/`--until`, `-- path`, `--follow`, `A..B` ranges, `--no-merges`, `--first-parent`, plus `--format` for custom output and `--graph --all` for the big picture.

---

### 5. git grep vs regular grep?

**Say:** `git grep` searches only tracked files (skipping node_modules, venvs and ignored files), it's fast, and it can search any commit or tag: `git grep TODO v1.0.0`.

---

### 6. What does git log --first-parent do?

**Say:** It follows only the first parent of merge commits, so on main you see one entry per merged PR, a clean release-level history.

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
