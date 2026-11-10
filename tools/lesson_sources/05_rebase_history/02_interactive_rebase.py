"""Module 5 · Interactive rebase: clean up your commits before a pull request

  git rebase -i HEAD~3      opens a "todo list" of your last 3 commits in the editor:

    pick a1b2c3d Add search
    pick d4e5f6a fix typo
    pick 0a1b2c3 WIP

  Change the word in front of each commit:
    pick    keep it
    reword  keep it, change the message
    squash  melt it into the commit above (combine the messages)
    fixup   melt it into the commit above (throw its message away)
    drop    delete the commit
  You can also reorder the lines.

  git commit --fixup <commit> + git rebase -i --autosquash  does the squashing for you.

TEACHING NOTES
  Why it matters  Reviewers want a few meaningful commits, not "wip", "fix", "fix again".
  Picture it      Editing a draft before publishing: merge paragraphs, fix titles,
                  delete the scribbles.
  Watch out       Only rewrite YOUR unpushed (or your own branch's) commits. If you already
                  pushed the branch, you'll need git push --force-with-lease (Module 6).
  In real jobs    Squash work-in-progress commits before review; or use "Squash and merge".
  Interview       Q: How do you combine several commits into one?
                  A: git rebase -i and mark them squash/fixup, or git reset --soft <base>
                     and commit once.

Run it:  python 05_rebase_history/02_interactive_rebase.py
(In this demo a tiny script plays you editing the todo list, so it runs without an editor.)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
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
''', show=False)

print("--- 1. Messy history: three commits for one feature")
sb.script("git log --oneline")

ids = sb.git("log", "--format=%h", "-3").split()[::-1]          # oldest first
todo = f"pick {ids[0]} Add search\nfixup {ids[1]} WIP\nfixup {ids[2]} fix typo"
print("--- 2. The todo list you would type in the editor:")
print(todo, "\n")
editor = sb.fake_editor(todo)
sb.script("git rebase -i HEAD~3", env={"GIT_SEQUENCE_EDITOR": editor})
sb.script('''
git log --oneline
git show --stat HEAD
''')

print("--- 3. Automatic version: commit --fixup + rebase --autosquash")
sb.script('''
echo "search box with results and filters" > search.txt
git commit -q -a --fixup HEAD
git log --oneline
GIT_SEQUENCE_EDITOR=true git rebase -i --autosquash HEAD~2
git log --oneline
''')
