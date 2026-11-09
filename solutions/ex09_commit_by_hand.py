"""Solution · Exercise 9: Make a commit without git add or git commit

Run it:  python solutions/ex09_commit_by_hand.py

The commands, as you'd type them (each prints an ID you paste into the next one):
    git hash-object -w hand.txt
    git update-index --add --cacheinfo 100644,<blob-id>,hand.txt
    git write-tree
    git commit-tree <tree-id> -p HEAD -m "Built by hand"
    git update-ref refs/heads/main <commit-id>
    git cat-file -t HEAD^{tree}        -> tree
    git rev-parse HEAD:hand.txt        -> the blob ID
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402


def plumbing(sb):
    blob = sb.git("hash-object", "-w", "hand.txt")
    sb.git("update-index", "--add", "--cacheinfo", f"100644,{blob},hand.txt")
    tree = sb.git("write-tree")
    commit = sb.git("commit-tree", tree, "-p", "HEAD", "-m", "Built by hand")
    sb.git("update-ref", "refs/heads/main", commit)
    sb.write("answers.txt", f"{sb.git('cat-file', '-t', 'HEAD^{tree}')}\n{sb.git('rev-parse', 'HEAD:hand.txt')}\n")
    print(sb.script("git log --oneline\ngit ls-tree HEAD\ncat answers.txt", show=False))


if __name__ == "__main__":
    solve("ex09_commit_by_hand.py", plumbing)
