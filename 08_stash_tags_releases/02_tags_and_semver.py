"""Module 8 · Tags: name the commits you release

A tag is a permanent name for one commit, usually a version number.

  git tag v1.0.0                         lightweight tag: just a name
  git tag -a v1.0.0 -m "First release"   ANNOTATED tag: author, date, message (use this)
  git tag                                list tags
  git show v1.0.0                        the tag and its commit
  git push origin v1.0.0                 tags are NOT pushed automatically
  git push --follow-tags                 push commits + annotated tags
  git describe --tags                    "v1.0.0-2-g1a2b3c" = 2 commits after v1.0.0

Semantic Versioning: MAJOR.MINOR.PATCH
  PATCH  1.0.0 -> 1.0.1   bug fixes only
  MINOR  1.0.1 -> 1.1.0   new features, backwards compatible
  MAJOR  1.1.0 -> 2.0.0   breaking changes

TEACHING NOTES
  Why it matters  Releases, deployments and bug reports all refer to versions; a tag ties
                  a version to the exact code.
  Picture it      A bookmark with a printed label that never moves (unlike a branch).
  Watch out       Don't move or delete a tag others have pulled; make a new version instead.
  In real jobs    Pushing tag v2.3.0 triggers the CI release pipeline and a GitHub Release.
  Interview       Q: Lightweight vs annotated tag?
                  A: Lightweight is just a name for a commit; annotated is a full object with
                     tagger, date and message (and can be signed): use it for releases.

Run it:  python 08_stash_tags_releases/02_tags_and_semver.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()
sb.script('''
git init --bare ../github/shop.git
git init
git remote add origin ../github/shop.git
echo "shop 1.0" > shop.txt
git add shop.txt
git commit -m "First version of the shop"
''', show=False)

print("--- 1. Lightweight vs annotated")
sb.script('''
git tag before-launch
git tag -a v1.0.0 -m "First public release"
git tag
git cat-file -t before-launch
git cat-file -t v1.0.0
git show v1.0.0 --stat
''')

print("--- 2. More work, a patch release, and git describe")
sb.script('''
echo "fix" > fix.txt
git add fix.txt
git commit -qm "fix: rounding"
git tag -a v1.0.1 -m "Rounding fix"
echo "wishlist" > wishlist.txt
git add wishlist.txt
git commit -qm "feat: wishlist"
git describe --tags
''')

print("--- 3. Tags are not pushed with commits")
sb.script('''
git push -q -u origin main
git ls-remote --tags origin
git push origin --tags
git ls-remote --tags origin
''')
