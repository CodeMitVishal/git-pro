"""Slides · Course intro: cover, module index, how each module works"""
from teach_kit import foot

M = "Course intro"
BASICS = [("01", "Git basics", "why version control; install &amp; config"),
          ("02", "Your first repository", "add, commit, diff, log, .gitignore"),
          ("03", "Undoing things", "restore, amend, reset, revert, reflog"),
          ("04", "Branches &amp; merging", "branches, fast-forward, conflicts"),
          ("05", "Rebase &amp; history", "rebase, rebase -i, cherry-pick"),
          ("06", "Remotes &amp; GitHub", "clone, push, pull, force-with-lease")]
PRO = [("07", "Team workflows", "GitHub flow, PRs, reviews, commits"),
       ("08", "Stash, tags &amp; releases", "stash, SemVer, release notes"),
       ("09", "Git internals", "blobs, trees, commits, refs, HEAD"),
       ("10", "Debugging with history", "log, blame, pickaxe, bisect"),
       ("11", "Advanced Git", "hooks, worktrees, submodules, secrets"),
       ("12", "Capstone", "rescue a messy repo, ship a release")]


def table(rows):
    trs = "".join(f"<tr><td><b>{n}</b></td><td><b>{name}</b></td><td>{goal}</td></tr>" for n, name, goal in rows)
    return f'<table style="flex:1;font-size:25px"><tr><th>#</th><th>Module</th><th>You\'ll be able to…</th></tr>{trs}</table>'


SLIDES = [
 f"""<section class="dark cover" style="justify-content:center;gap:28px">
  <img class="brand-big" src="channel-icon.png" alt="CodeMitVishal logo">
  <p class="num">CODEMITVISHAL · FREE COURSE</p>
  <h1 style="font-size:110px">Git Pro</h1>
  <p style="font-size:38px;color:#E6E9F0;max-width:1300px;line-height:1.3">Git from <b style="color:#7EE2A8">zero to hero</b>:
     commits, branches, rebase, GitHub teamwork, internals, debugging, and the questions every interview asks.</p>
  <div style="display:flex;gap:70px;margin-top:30px">
    <div><p class="big" style="font-size:96px">12</p><p style="font-size:24px">modules</p></div>
    <div><p class="big" style="font-size:96px">12</p><p style="font-size:24px">hands-on exercises</p></div>
    <div><p class="big" style="font-size:96px">100+</p><p style="font-size:24px">interview answers</p></div>
    <div><p class="big" style="font-size:96px">0 €</p><p style="font-size:24px">always free</p></div>
  </div>
  <p class="foot-l">Git Pro · No experience needed</p>
  <p class="foot-r">github.com/CodeMitVishal/git-pro</p>
</section>""",

 f"""<section>
  <div><p class="eyebrow">Course map</p><h2>From your first commit to rescuing any repository</h2></div>
  <div class="row" style="gap:40px">{table(BASICS)}{table(PRO)}</div>
  {foot("Course map")}
</section>""",

 f"""<section>
  <div><p class="eyebrow">How every module works</p><h2>Real Git, real output, real practice</h2></div>
  <div class="row" style="gap:48px">
    <div class="steps" style="flex:1">
      <div class="step"><span>1</span><p><b>Why</b>: the real problem this solves</p></div>
      <div class="step"><span>2</span><p><b>Picture it</b>: an everyday analogy + a diagram</p></div>
      <div class="step"><span>3</span><p><b>Try it</b>: real Git commands with their <b>real output</b></p></div>
      <div class="step"><span>4</span><p><b>Common mistake</b>: wrong vs right, side by side</p></div>
      <div class="step"><span>5</span><p><b>In real jobs</b>: how teams use it</p></div>
      <div class="step"><span>6</span><p><b>Interview</b>: what to say + the follow-up</p></div>
      <div class="step"><span>7</span><p><b>Recap</b> + a hands-on exercise</p></div>
    </div>
    <div class="col" style="width:680px">
      <p class="label">IN EVERY MODULE FOLDER</p>
      <table class="tbig">
        <tr><td>Lessons</td><td>run real Git in a safe sandbox</td></tr>
        <tr><td>Exercise</td><td>setup &#8594; you fix it &#8594; check</td></tr>
        <tr><td>Quiz</td><td>QUIZ.md with an answer key</td></tr>
        <tr><td>Interview</td><td>INTERVIEW.md with model answers</td></tr>
        <tr><td>Slides</td><td>slides/modules/Module-NN.pdf</td></tr>
      </table>
    </div>
  </div>
  {foot("How it works")}
</section>""",

 f"""<section>
  <div><p class="eyebrow">How to study</p><h2>Get the most out of Git Pro</h2></div>
  <div class="row" style="gap:48px">
    <div class="steps" style="flex:1">
      <div class="step"><span>1</span><p>Watch or read the module's <b>slides</b>.</p></div>
      <div class="step"><span>2</span><p><b>Read every lesson</b> and type each command yourself in Git Bash.</p></div>
      <div class="step"><span>3</span><p>Do the <b>exercise</b> in its playground repo until <b>All checks passed!</b></p></div>
      <div class="step"><span>4</span><p>Take the <b>quiz</b>, then answer <b>INTERVIEW.md</b> out loud.</p></div>
      <div class="step"><span>5</span><p>Before an interview: read <b>interview_prep/</b>.</p></div>
    </div>
    <div class="code" style="width:780px;font-size:24px"><span class="c"># needs only Git (Git Bash on Windows)</span>
git clone https://github.com/
    CodeMitVishal/git-pro.git
cd git-pro
bash exercises/ex01_first_repo/setup.sh
cd playground/ex01   # do the task
bash ../../exercises/ex01_first_repo/check.sh</div>
  </div>
  {foot("How to study")}
</section>""",
]
