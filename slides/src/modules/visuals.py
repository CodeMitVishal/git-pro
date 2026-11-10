"""Commit-graph picture slides, inserted after the slide whose title contains a given text."""
from teach_kit import G, graph


def V(n):
    M = {1: "Module 1 · Git basics", 2: "Module 2 · Your first repository", 3: "Module 3 · Undoing things",
         4: "Module 4 · Branches &amp; merging", 5: "Module 5 · Rebase &amp; history", 6: "Module 6 · Remotes &amp; GitHub",
         8: "Module 8 · Stash, tags &amp; releases", 9: "Module 9 · Git internals", 10: "Module 10 · Debugging with history",
         12: "Module 12 · Capstone"}[n]
    ML = ["main", "feature"]
    return {
    1: [("A photo album of your project", graph(M, "History", "History = a chain of snapshots", [
        ("Three commits on main", G([("A", 0), ("B", 0), ("C", 0)], refs={"main": "C"}, head="main",
                                    marks={"A": "price = 10", "B": "price = 12", "C": "with VAT"}))],
        steps=["Each circle is a <b>commit</b>: a full snapshot.", "Each commit points back to its <b>parent</b>.",
               "<b>main</b> is a label on the newest commit; <b>HEAD</b> says where you are."]))],
    2: [("Desk, box, shelf", graph(M, "Commits", "Every commit adds one snapshot", [
        ("Before", G([("A", 0), ("B", 0)], refs={"main": "B"}, head="main")),
        ("git commit -m \"Add cart\"", G([("A", 0), ("B", 0), ("C", 0)], refs={"main": "C"}, head="main", new=["C"]))],
        caption="The new commit <b>C</b> points to its parent <b>B</b>, and the branch label <b>main</b> (with HEAD) moves forward to it."))],
    3: [("Fix the last commit", graph(M, "amend", "amend replaces the last commit", [
            ("Before: typo in B", G([("A", 0), ("B", 0)], refs={"main": "B"}, head="main", marks={"B": "\"Add copuon\""})),
            ("git commit --amend", G([("A", 0), ("B", 1, "A"), ("B'", 0, "A")], refs={"main": "B'"}, head="main",
                                      new=["B'"], ghost=["B"], marks={"B'": "\"Add coupon\""}))],
            caption="<b>B'</b> is a brand-new commit (new ID). The old <b>B</b> is abandoned, so never amend what others already pulled.")),
        ("Same reset, three modes", graph(M, "reset", "reset moves the branch label back", [
            ("Before", G([("A", 0), ("B", 0), ("C", 0)], refs={"main": "C"}, head="main")),
            ("git reset HEAD~2", G([("A", 0), ("B", 0), ("C", 0)], refs={"main": "A"}, head="main", ghost=["B", "C"]))],
            caption="B and C are no longer on main (reflog still finds them). <b>--soft</b>, <b>--mixed</b>, <b>--hard</b> only decide what happens to their <b>changes</b>.")),
        ("Undo a shared commit safely", graph(M, "revert", "revert adds an \"undo\" commit", [
            ("B broke production", G([("A", 0), ("B", 0), ("C", 0)], refs={"main": "C"}, head="main", marks={"B": "bad"})),
            ("git revert B", G([("A", 0), ("B", 0), ("C", 0), ("B⁻¹", 0)], refs={"main": "B⁻¹"}, head="main", new=["B⁻¹"], marks={"B": "bad", "B⁻¹": "undoes B"}))],
            caption="Nothing is rewritten: history only moves <b>forward</b>. That's why revert is safe on main."))],
    4: [("A branch is a sticky note on a commit", graph(M, "Branches", "Creating a branch copies nothing", [
            ("git switch -c feature", G([("A", 0), ("B", 0)], refs={"main": "B", "feature": "B"}, head="feature")),
            ("git commit (on feature)", G([("A", 0), ("B", 0), ("C", 1, "B")], refs={"main": "B", "feature": "C"}, head="feature", new=["C"], lanes=ML))],
            caption="A branch is just a label. Only the branch HEAD points to moves when you commit.")),
        ("Fast-forward: main didn't move", graph(M, "Fast-forward", "Fast-forward merge", [
            ("Before", G([("A", 0), ("B", 0), ("C", 1, "B")], refs={"main": "B", "feature": "C"}, head="main", lanes=ML)),
            ("git merge feature", G([("A", 0), ("B", 0), ("C", 0)], refs={"main": "C", "feature": "C"}, head="main"))],
            caption="main had no new commits, so Git simply <b>slides the label forward</b>. No merge commit.")),
        ("Three-way: both branches moved", graph(M, "Three-way merge", "Three-way merge", [
            ("Before", G([("A", 0), ("B", 0), ("C", 1, "B"), ("D", 0, "B")], refs={"main": "D", "feature": "C"}, head="main", lanes=ML)),
            ("git merge feature", G([("A", 0), ("B", 0), ("C", 1, "B"), ("D", 0, "B"), ("M", 0, ("D", "C"))],
                                    refs={"main": "M", "feature": "C"}, head="main", new=["M"], lanes=ML))],
            caption="Both sides have new work, so Git creates <b>M</b>, a merge commit with <b>two parents</b>."))],
    5: [("Re-planting your branch", graph(M, "rebase", "rebase replays your commits", [
            ("Before", G([("A", 0), ("C", 1, "A"), ("D", 1), ("B", 0, "A")], refs={"main": "B", "feature": "D"}, head="feature", lanes=ML)),
            ("git rebase main", G([("A", 0), ("B", 0), ("C'", 1, "B"), ("D'", 1)], refs={"main": "B", "feature": "D'"}, head="feature", new=["C'", "D'"], lanes=ML))],
            caption="C and D are replayed on top of B as <b>new</b> commits C' and D'. Now main can fast-forward.")),
        ("edit your history like a draft", graph(M, "Interactive rebase", "Squash: many commits become one", [
            ("Before", G([("A", 0), ("B", 0), ("C", 0), ("D", 0)], refs={"main": "D"}, head="main", marks={"B": "Add search", "C": "WIP", "D": "fix typo"})),
            ("git rebase -i HEAD~3 (fixup)", G([("A", 0), ("S", 0)], refs={"main": "S"}, head="main", new=["S"], marks={"S": "Add search"}))],
            caption="Reviewers see one clear commit instead of three noisy ones.")),
        ("Copy ONE commit to another branch", graph(M, "cherry-pick", "cherry-pick copies one commit", [
            ("Before", G([("A", 0), ("B", 0), ("F", 0)], refs={"main": "F", "release/1.0": "A"}, head="release/1.0", marks={"B": "new feature", "F": "fix"})),
            ("git cherry-pick F", G([("A", 0), ("B", 0), ("F", 0), ("F'", 1, "A")], refs={"main": "F", "release/1.0": "F'"}, head="release/1.0",
                                    new=["F'"], lanes=["main", "release"]))],
            caption="Only the fix lands on the release branch, as a <b>copy</b> F' (new ID)."))],
    6: [("fetch first, look, then integrate", graph(M, "Remotes", "ahead 1, behind 1", [
            ("After git fetch", G([("A", 0), ("B", 0), ("Y", 0), ("P", 1, "B")], refs={"main": "Y", "origin/main": "P"}, head="main",
                                  lanes=["you", "GitHub"], marks={"Y": "yours", "P": "Priya's"})),
            ("git pull --rebase", G([("A", 0), ("B", 0), ("P", 0), ("Y'", 0)], refs={"origin/main": "P", "main": "Y'"}, head="main", new=["Y'"]))],
            caption="Your commit is replayed on top of Priya's. Now <b>git push</b> works and history stays a straight line."))],
    8: [("A tag is a bookmark that never moves", graph(M, "Tags", "Tags mark releases", [
            ("Tags vs branches", G([("A", 0), ("B", 0), ("C", 0)], refs={"v1.0.0": "A", "v1.0.1": "B", "main": "C"}, head="main"))],
            steps=["<b>v1.0.0</b> and <b>v1.0.1</b> stay where they are forever.", "<b>main</b> moves with every new commit.",
                   "<b>git describe</b>: v1.0.1-1-g&lt;id&gt; = 1 commit after v1.0.1."]))],
    9: [("Branches and HEAD are tiny text files", graph(M, "HEAD", "Attached vs detached HEAD", [
            ("Normal: HEAD → main", G([("A", 0), ("B", 0), ("C", 0)], refs={"v1.0.0": "A", "main": "C"}, head="main")),
            ("git switch --detach v1.0.0", G([("A", 0), ("B", 0), ("C", 0)], refs={"v1.0.0": "A", "main": "C"}, head="A"))],
            caption="Detached: HEAD points at a <b>commit</b>, not a branch. New commits here belong to no branch, so create one with <b>git switch -c</b>."))],
    10: [("bisect = the number-guessing game", graph(M, "bisect", "Binary search through history", [
            ("16 commits, 4 tests", G([(str(i), 0) for i in (1, 4, 8, 10, 11, 12, 16)], refs={"v1.0.0": "1", "main": "16"},
                                      marks={"1": "good", "8": "1: good", "12": "2: bad", "10": "3: good", "11": "4: bad", "16": "bad"}))],
            steps=["Test the middle, throw away half.", "16 commits &#8594; 4 tests; 1,000 &#8594; ~10.",
                   "<b>11</b> is the first bad commit."]))],
    12: [("Look, find, plan, act", graph(M, "Rescue", "The rescue, as a picture", [
            ("The mess", G([("A", 0), ("B", 0), ("W", 0), ("F", 1, "B")], refs={"main": "W", "origin/main": "F"}, head="main",
                           lanes=["you", "GitHub"], marks={"W": "wishlist", "F": "fix"})),
            ("After the rescue", G([("A", 0), ("B", 0), ("F", 0), ("W'", 1, "F")], refs={"main": "F", "origin/main": "F", "feature/wishlist": "W'"},
                                   head="feature/wishlist", new=["W'"], lanes=["main", "feature"]))],
            caption="main = origin/main again; your work sits on <b>feature/wishlist</b>, on top of the latest main."))],
    }.get(n, [])


def add_visuals(n, slides):
    """Insert each picture right after the slide whose HTML contains its anchor text."""
    for anchor, slide in V(n):
        idx = next((i for i, s in enumerate(slides) if anchor in s), None)
        if idx is None:
            raise ValueError(f"Module {n}: no slide contains {anchor!r}")
        slides.insert(idx + 1, slide)
    return slides
