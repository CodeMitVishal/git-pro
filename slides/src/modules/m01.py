"""Slides · Module 1 · Git basics"""
from teach_kit import cover, interview, job, mistake, picture, recap, terminal, trace, why

M = "Module 1 · Git basics"
SLIDES = [
 cover("01", "Git basics", "What version control is, why every team uses Git, and how to set it up.",
       [("Why version control", "01_why_version_control.md"), ("Install &amp; configure", "02_install_and_config.md"),
        ("Exercise: first repository", "ex01_first_repo/"), ("Interview Q&amp;A", "INTERVIEW.md")], M),

 why(M, "Version control", "final_v2_REALLY_final.py",
     "Without version control, people copy files: <b>app_old.py, app_backup.py, app_final_v2.py</b>. Nobody knows which is current, "
     "what changed, or why, and two people editing the same file overwrite each other.",
     "Git saves <b>snapshots</b> of the whole project, called commits. Each one records <b>what</b> changed, <b>who</b>, <b>when</b> and <b>why</b>."),

 picture(M, "Version control", "A photo album of your project",
     "&#128247; Every <b>commit</b> is a photo of the whole project with a caption (the message). You can flip back to any photo, "
     "compare two photos, and the team can take photos in parallel on <b>branches</b>.",
     [("edit files", "your working folder"), ("git add", "choose what goes in the photo"),
      ("git commit", "take the photo + caption"), ("git log", "flip through the album")],
     "Git is <b>distributed</b>: every clone has the whole album, so you can work offline."),

 terminal(M, "Version control", "Three snapshots of one file", '''
git init
echo "price = 10" > shop.py
git add shop.py
git commit -m "Add shop with a fixed price"
echo "price = 12" > shop.py
git commit -qam "Raise the price to 12"
git log --oneline
git show HEAD~1:shop.py
''', ["Each commit has an ID (a hash) like <b>f8b0491</b>.", "<b>HEAD~1</b> = one commit before the current one.",
      "Old versions are always there: nothing is lost."]),

 trace(M, "Git vs GitHub", "Git is not GitHub", ["", "Git", "GitHub / GitLab / Azure DevOps"],
       [["What it is", "a program on your computer", "a website that hosts Git repositories"],
        ["Works offline?", "yes", "no"],
        ["Gives you", "commits, branches, history, merges", "pull requests, code review, issues, CI/CD"],
        ["Command", "<span class=\"m\">git commit</span>", "<span class=\"m\">git push</span> sends commits there"]]),

 trace(M, "Setup", "Configure Git once per machine", ["Command", "Why"],
       [["<span class=\"m\">git config --global user.name \"Your Name\"</span>", "stored in every commit"],
        ["<span class=\"m\">git config --global user.email \"you@example.com\"</span>", "links commits to your GitHub account"],
        ["<span class=\"m\">git config --global init.defaultBranch main</span>", "new repos start on <b>main</b>"],
        ["<span class=\"m\">git config --global core.editor \"code --wait\"</span>", "VS Code for commit messages"],
        ["<span class=\"m\">git config --local user.email \"you@company.com\"</span>", "a different email in ONE repo"]],
       "Three levels: <b>--system</b> &lt; <b>--global</b> (~/.gitconfig) &lt; <b>--local</b> (.git/config). The most specific wins."),

 terminal(M, "Setup", "Local beats global", '''
git init
git config --global user.email
git config --local user.email "vishal@company.com"
git config --show-scope --get-all user.email
git config user.email
''', ["The global value applies everywhere.", "The local value wins inside this repository.",
      "<b>--show-scope</b> shows where each value comes from."]),

 mistake(M, "Setup", "Committing with the wrong identity",
     '''
# fresh laptop, nothing configured
git commit -m "Fix login"
# Author: acer <acer@LAPTOP-123.local>''',
     "Your commits show a random machine name and aren't linked to your GitHub profile, so your contributions don't count.",
     '''
git config --global user.name "Vishal"
git config --global user.email "vishal@example.com"
git commit --amend --reset-author --no-edit''',
     "Configure once per machine. Fix the last commit with <b>--amend --reset-author</b>."),

 job(M, "Git", "Git on your first day at work", [
     ("Get the code", '''
git clone git@github.com:company/shop.git'''),
     ("Set your work identity", '''
git config --local user.email "you@company.com"'''),
     ("Daily loop", '''
git add -p
git commit -m "Fix coupon rounding"
git push'''),
     ("Everything is reviewed", '''
open a Pull Request -> review -> merge'''),
 ]),

 interview(M, "What is Git, and why do teams use it?",
     ["Git is a <b>distributed version control system</b>.",
      "It records snapshots (<b>commits</b>) with who, when and why, so you can compare and restore any version.",
      "Every clone has the <b>full history</b>, so you can work offline and every copy is a backup.",
      "<b>Branches</b> let many developers work in parallel and merge their work safely."],
     None,
     "\"Git vs GitHub?\" (Git is the tool; GitHub hosts repositories and adds pull requests, reviews and CI)."),

 recap(M, "Module 1 in 5 lines",
     ["A <b>commit</b> = a snapshot + who, when, why.",
      "Git is <b>distributed</b>: every clone has the full history.",
      "Git is the tool; GitHub hosts repositories.",
      "Set <b>user.name</b> and <b>user.email</b> once per machine.",
      "Config levels: system &lt; global &lt; local."],
     "Run <b>bash exercises/ex01_first_repo/setup.sh</b> and make your first commit."),
]

from visuals import add_visuals  # noqa: E402
SLIDES = add_visuals(1, SLIDES)
