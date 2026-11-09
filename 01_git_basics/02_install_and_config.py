"""Module 1 · Install and configure Git

Install:
  Windows   https://git-scm.com/download/win   (includes Git Bash)
  macOS     xcode-select --install    or   brew install git
  Linux     sudo apt install git

Then tell Git who you are. Every commit stores this name and email:

  git config --global user.name  "Your Name"
  git config --global user.email "you@example.com"
  git config --global init.defaultBranch main
  git config --global core.editor "code --wait"     # VS Code as the editor

Settings live at three levels; the most specific one wins:
  --system  every user on the machine
  --global  you (~/.gitconfig)
  --local   one repository (.git/config)

TEACHING NOTES
  Why it matters  A wrong email means your commits aren't linked to your GitHub account.
  Picture it      Three layers of stickers: system, then global, then local on top.
  Watch out       Use your work email in work repos: set it with --local inside that repo.
  In real jobs    Day one: install Git, set name/email, add an SSH key to GitHub.
  Interview       Q: Where does Git store configuration?
                  A: System, global (~/.gitconfig) and local (.git/config); local wins.

Run it:  python 01_git_basics/02_install_and_config.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import Sandbox  # noqa: E402

sb = Sandbox()

print("--- 1. Which Git do you have?")
print("$ git --version")
print(sb.git("--version"))
print()

print("--- 2. Global settings (the sandbox uses its own config file, not yours)")
sb.script('''
git config --global user.name
git config --global user.email
git config --global init.defaultBranch
''')

print("--- 3. A LOCAL setting overrides the global one for this repository only")
sb.script('''
git init
git config --local user.email "vishal@company.com"
git config user.email
git config --show-scope --get-all user.email
''')

print("--- 4. Getting help")
print("  git help commit        full manual page")
print("  git commit -h          short summary of the options")
