"""Module 11 · Line endings and .gitattributes

Windows ends lines with CRLF (\\r\\n), macOS and Linux with LF (\\n). Without rules, a
mixed team produces diffs where EVERY line changed, and shell scripts break on Linux.

The fix is a .gitattributes file in the repository (shared with everyone):

  * text=auto eol=lf      normalise text files to LF in the repo and checkout
  *.bat text eol=crlf     Windows scripts keep CRLF
  *.png binary            never touch images
  *.lock -diff            don't show diffs for generated files

  git ls-files --eol           what's stored vs what's in your folder
  git add --renormalize .      apply new rules to existing files

TEACHING NOTES
  Why it matters  "I changed one line but the diff shows 500" is almost always line endings.
  Picture it      Two keyboards with different Enter keys; .gitattributes says which one
                  everybody's files use.
  Watch out       core.autocrlf is a personal setting; .gitattributes is the team rule and wins.
  In real jobs    Every cross-platform repo should have a .gitattributes on day one.
  Interview       Q: How do you handle line endings in a team with Windows and Linux?
                  A: A .gitattributes with "* text=auto eol=lf" (plus exceptions), and
                     git add --renormalize . once.

Run it:  python 11_advanced_git/04_line_endings_and_attributes.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))
from sandbox import Sandbox  # noqa: E402

SETUP_MD = r"""
git init
printf 'echo deploying\r\necho done\r\n' > deploy.sh
"""

sb = Sandbox()
sb.script("git init", show=False)

print("--- 1. Someone on Windows commits a CRLF file")
sb.path("deploy.sh").write_bytes(b"echo deploying\r\necho done\r\n")
sb.script('''
git add deploy.sh
git commit -qm "Add deploy script"
git ls-files --eol
''')

print("--- 2. Add .gitattributes and renormalise: the repo now stores LF")
sb.write(".gitattributes", "* text=auto eol=lf\n*.bat text eol=crlf\n*.png binary\n")
sb.script('''
cat .gitattributes
git add --renormalize .
git add .gitattributes
git commit -qm "Normalise line endings"
git ls-files --eol
git check-attr -a deploy.sh
''')

print("--- 3. Your folder still has the old CRLF copy; check it out again")
sb.script('''
rm deploy.sh
git restore deploy.sh
git ls-files --eol deploy.sh
''')
