# Module 11 · Secrets in history, big files, signed commits, huge repos

[← Module 11](README.md)

## 1. You pushed a secret. What now?

**Step 1 is not Git.** The moment a password or API key reaches a remote, assume it's stolen: **rotate (revoke) it first.** Bots scan public GitHub for keys within minutes.

Then clean the history, if you need to:

```bash
# remove a file from ALL history
git filter-repo --path config/secrets.env --invert-paths

# replace the leaked text everywhere (expressions.txt contains: sk_live_123==>REMOVED)
git filter-repo --replace-text expressions.txt

git push --force --all && git push --force --tags
```

- `git filter-repo` (`pip install git-filter-repo`) is the recommended tool. The older `git filter-branch` is slow and deprecated. **BFG Repo-Cleaner** is a popular alternative.
- Rewriting history changes every commit ID after that point, so everyone must **re-clone**. Coordinate with the team.
- GitHub keeps cached views and forks: contact support for sensitive leaks.
- If the commit was **never pushed**, it's much easier: `git reset`, `git commit --amend`, or `git rebase -i`, then commit without the secret.

**Prevent it:** keep `.env` in `.gitignore`, use a pre-commit hook (`detect-secrets`, `gitleaks`), turn on **GitHub secret scanning and push protection**, and keep secrets in a vault (Azure Key Vault, AWS Secrets Manager).

## 2. Big files: Git LFS

Git keeps **every version** of every file forever. A 200 MB video changed 10 times means 2 GB in every clone.

```bash
git lfs install
git lfs track "*.psd" "*.mp4"      # writes .gitattributes
git add .gitattributes design.psd
git commit -m "Track design files with LFS"
```

Git stores a tiny **pointer file**, and the real content lives on the LFS server. Use LFS for large binaries (media, datasets, models). Don't commit build outputs or `node_modules` at all.

## 3. Signed commits

Anyone can set `user.email` to your address. **Signing** proves a commit really came from you, and GitHub shows **Verified**.

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git log --show-signature -1
```

Branch protection can **require signed commits** on `main`.

## 4. Huge repositories (monorepos)

| Need | Command |
|---|---|
| Only the latest snapshot (CI) | `git clone --depth 1 <url>` (shallow clone) |
| History, but blobs on demand | `git clone --filter=blob:none <url>` (partial clone) |
| Only some folders | `git sparse-checkout set services/payments libs/common` |
| Faster status in big repos | `git config core.fsmonitor true` / `git maintenance start` |

## Interview answers

> **"You committed a password. What do you do?"** *"Rotate the credential immediately. If it wasn't pushed, amend or rebase it out. If it was pushed, remove it from history with git filter-repo, force-push, and have everyone re-clone. Then prevent it next time with .gitignore, pre-commit secret scanning and GitHub push protection."*

> **"How do you handle large binary files?"** *"Git LFS: Git stores small pointers and the content lives on an LFS server, so clones stay small."*

---

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
