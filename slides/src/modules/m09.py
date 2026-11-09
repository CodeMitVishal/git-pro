"""Slides · Module 9 · Git internals"""
from teach_kit import cover, interview, job, mistake, picture, recap, terminal, trace, why

M = "Module 9 · Git internals"
REPO = '''
git init
echo "hello" > a.txt
echo "hello" > copy-of-a.txt
mkdir src
echo "print('shop')" > src/app.py
git add .
git commit -m "First snapshot"
'''


def plumbing(sb):
    blob = sb.git("hash-object", "-w", "hand.txt")
    sb.git("update-index", "--add", "--cacheinfo", f"100644,{blob},hand.txt")


SLIDES = [
 cover("09", "Git internals", "Open the hood: objects, trees, refs and HEAD. After this, Git stops being magic.",
       [("Objects", "01_objects.py"), ("Refs &amp; HEAD", "02_refs_and_head.py"), ("A commit by hand", "03_commit_by_hand.py"),
        ("Exercise: plumbing commit", "ex09_commit_by_hand.py"), ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "Internals", "Why look inside .git?",
     "Why does a rebase change commit IDs? Why is creating a branch instant? How can reflog bring back \"deleted\" commits? "
     "Memorising commands without the model behind them makes Git feel random.",
     "Git is a small <b>database of objects</b> plus <b>name tags</b> (refs). Learn the 4 object types and everything else follows."),

 picture(M, "Objects", "Four kinds of objects",
     "&#128218; A library where every item is filed under a <b>fingerprint</b> (hash) of its content: identical content gets the "
     "same fingerprint and is stored once. Change one letter and you get a new fingerprint.",
     [("blob", "file CONTENT (no name)"), ("tree", "a folder: names &#8594; blobs / trees"),
      ("commit", "tree + parent(s) + author + message"), ("tag", "annotated name for an object")]),

 terminal(M, "Objects", "Walk from a commit down to a blob", '''
git cat-file -p HEAD
git cat-file -p HEAD^{tree}
git ls-tree -r HEAD
git cat-file -p HEAD:a.txt
''', ["The commit points to ONE tree (the snapshot).", "Two files, same content: <b>one blob</b>.",
      "Snapshots, not diffs; unchanged files are reused."], setup=REPO),

 trace(M, "Hashes", "Why IDs change after rebase and amend", ["A commit's ID is a hash of...", "Changed by"],
       [["its tree (the snapshot)", "any file change"],
        ["its parent ID(s)", "<b>rebase</b> (new parent)"],
        ["author + date", "--reset-author, rebasing (committer date)"],
        ["the message", "<b>amend</b>, reword"]],
       "Change anything &#8594; a new hash &#8594; a new commit. That's why rewritten history is \"different\" history."),

 terminal(M, "Refs and HEAD", "Branches and HEAD are tiny text files", '''
cat .git/HEAD
cat .git/refs/heads/main
git show-ref
git switch --detach HEAD~0
cat .git/HEAD
''', ["A branch = a file with one commit ID.", "HEAD = \"ref: refs/heads/main\" (symbolic).",
      "Detached HEAD = HEAD holds a commit ID directly."], setup='''
git init
echo "v1" > app.txt
git add app.txt
git commit -m "Version 1"
git tag v1.0.0
'''),

 trace(M, "Refs and HEAD", "Naming commits", ["Expression", "Means"],
       [["<span class=\"m\">HEAD~1</span> = <span class=\"m\">HEAD~</span> = <span class=\"m\">HEAD^</span>", "the (first) parent"],
        ["<span class=\"m\">HEAD~3</span>", "three generations back (first parents)"],
        ["<span class=\"m\">HEAD^2</span>", "the SECOND parent of a merge commit"],
        ["<span class=\"m\">main@{1}</span>", "where main was one move ago (reflog)"],
        ["<span class=\"m\">v1.0.0^{tree}</span>", "the tree of the commit a tag points to"],
        ["<span class=\"m\">HEAD:src/app.py</span>", "a file's blob in a commit"]]),

 terminal(M, "Plumbing", "A commit built by hand", '''
git hash-object -w hand.txt
git write-tree
git commit-tree 6090a53 -p HEAD -m "Built by hand"
''', ["<b>hash-object -w</b>: store the content &#8594; blob.", "<b>update-index</b> + <b>write-tree</b>: index &#8594; tree.",
      "<b>commit-tree</b> &#8594; commit; <b>update-ref</b> moves the branch."],
     setup='''
git init
echo "# Shop" > README.md
git add README.md
git commit -m "Initial commit"
echo "made with plumbing" > hand.txt
''', before=plumbing),

 mistake(M, "Detached HEAD", "Committing in detached HEAD, then leaving",
     '''
git switch --detach v1.0.0
# ...two commits of experiments...
git switch main
# warning: you are leaving 2 commits behind''',
     "Those commits belong to no branch. They're not deleted yet, but they're easy to lose and will be garbage-collected.",
     '''
git switch --detach v1.0.0
# ...commits...
git switch -c experiment     # keep them on a branch
# already left? git reflog -> git branch rescue <id>''',
     "Create a branch before leaving, or rescue the commits with the reflog."),

 job(M, "Internals", "Where internals help at work", [
     ("Scripts and CI", '''
git rev-parse --short HEAD   # image tag
git rev-parse --abbrev-ref HEAD'''),
     ("Inspect without checking out", '''
git show v1.2.0:config/settings.py
git ls-tree -r --name-only v1.2.0'''),
     ("Repo size problems", '''
git count-objects -vH
git gc'''),
     ("Understand \"weird\" history", '''
git cat-file -p <merge-commit>  # 2 parents'''),
 ]),

 interview(M, "How does Git store data internally?",
     ["A content-addressable <b>object database</b>: blobs (content), trees (folders), commits, annotated tags.",
      "Each object is named by the <b>hash of its content</b>; identical content is stored once.",
      "Commits are <b>snapshots</b>: a tree + parent(s) + metadata.",
      "Branches, tags and HEAD are <b>refs</b>: tiny files pointing at object IDs.",
      "That's why branches are cheap and rebased commits get new IDs."],
     None,
     "\"What is a detached HEAD?\" (HEAD points at a commit, not a branch; create a branch to keep new commits)."),

 recap(M, "Module 9 in 5 lines",
     ["4 objects: <b>blob</b>, <b>tree</b>, <b>commit</b>, <b>tag</b>, named by content hash.",
      "Commits are snapshots that point to a tree and parent(s).",
      "Refs (branches, tags) are files with IDs; HEAD points to a ref.",
      "<b>HEAD~n</b> first parents, <b>HEAD^2</b> second parent.",
      "git commit = write-tree + commit-tree + update-ref."],
     "Do <b>exercises/ex09_commit_by_hand.py</b>: a real commit with plumbing only."),
]
