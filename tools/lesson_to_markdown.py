"""Maintainer tool: run a lesson script and turn it into a Markdown lesson.

    python tools/lesson_to_markdown.py tools/lesson_sources/03_undoing_things/01_restore_and_amend.py
    python tools/lesson_to_markdown.py --all

It records every Git command the lesson runs (hidden setup and visible steps),
every file it writes, and its printed headings, then writes
03_undoing_things/01_restore_and_amend.md with the real output of each command.
Learners never need Python: they read the Markdown and type the commands.
"""
import builtins
import importlib.util
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
SOURCES = ROOT / "tools" / "lesson_sources"
sys.path.insert(0, str(ROOT / "tools"))
import sandbox  # noqa: E402
from diagrams import DIAGRAMS  # noqa: E402

EVENTS = []


def record():
    real_print = builtins.print
    orig_script, orig_run = sandbox.Sandbox.script, sandbox.Sandbox.run
    orig_write, orig_append = sandbox.Sandbox.write, sandbox.Sandbox.append

    def script(self, text, show=True, env=None):
        self._depth = getattr(self, "_depth", 0) + 1
        out = orig_script(self, text, show=False, env=env)
        self._depth -= 1
        EVENTS.append(("script", show, out))
        return out

    def run(self, line, env=None):
        self._depth = getattr(self, "_depth", 0) + 1
        out = orig_run(self, line, env)
        self._depth -= 1
        if self._depth == 0:                                # called directly by the lesson
            EVENTS.append(("script", True, f"$ {self.tidy(line)}" + (f"\n{out}" if out else "")))
        return out

    def write(self, rel, text):
        if getattr(self, "_depth", 0) == 0:
            EVENTS.append(("write", rel, text))
        orig_write(self, rel, text)

    def append(self, rel, text):
        if getattr(self, "_depth", 0) == 0:
            EVENTS.append(("append", rel, text))
        orig_append(self, rel, text)

    def fake_print(*args, **kw):
        if kw.get("file") not in (None, sys.stdout):
            return real_print(*args, **kw)
        EVENTS.append(("print", " ".join(str(a) for a in args)))

    sandbox.Sandbox.script, sandbox.Sandbox.run = script, run
    sandbox.Sandbox.write, sandbox.Sandbox.append = write, append
    builtins.print = fake_print
    return real_print


def heredoc(op, rel, text):
    arrow = ">>" if op == "append" else ">"
    return f"cat {arrow} {rel} <<'EOF'\n{text.rstrip(chr(10))}\nEOF"


def split_doc(doc):
    head, _, rest = doc.partition("TEACHING NOTES")
    notes, _, _run = rest.partition("Run it:")
    title, _, body = head.strip().partition("\n")
    labels = ["Why it matters", "Picture it", "Watch out", "In real jobs", "Interview"]
    found, current = {}, None
    for line in notes.splitlines():
        m = re.match(r"\s{2}(" + "|".join(labels) + r")\s+(.*)", line)
        if m:
            current = m.group(1)
            found[current] = m.group(2).strip()
        elif current and line.strip():
            found[current] += " " + line.strip()
    return title.strip(), body.strip("\n"), found


def body_to_md(body):
    """Docstring body: prose paragraphs stay prose; indented command tables become code."""
    out, block = [], []
    for para in re.split(r"\n\s*\n", body):
        lines = para.splitlines()
        if all(l.startswith("  ") or not l.strip() for l in lines):
            out.append("```text\n" + textwrap.dedent(para).strip("\n") + "\n```")
        else:
            out.append(" ".join(l.strip() for l in lines))
    return "\n\n".join(out)


def convert(lesson: Path) -> str:
    EVENTS.clear()
    real_print = record()
    try:
        spec = importlib.util.spec_from_file_location("lesson", lesson)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        builtins.print = real_print
    title, body, notes = split_doc(mod.__doc__ or "")
    md = [f"# {title}", "", body_to_md(body), ""]
    if notes.get("Picture it"):
        md += [f"> 🧠 **Picture it:** {notes['Picture it']}", ""]
    if notes.get("Why it matters"):
        md += [f"**Why it matters:** {notes['Why it matters']}", ""]
    diagram = DIAGRAMS.get(f"{lesson.parent.name}/{lesson.stem}")
    if diagram:
        md += ["## See it", "", "```mermaid", diagram.strip(), "```", ""]
    md += ["## Try it yourself", "",
           "Open **Git Bash** (Windows) or a terminal (macOS/Linux) in an empty practice folder and type along. "
           "Lines starting with `$` are commands; the lines below them are what Git prints.", "",
           "```bash", "mkdir project && cd project", "```", ""]
    setup, started, used_setup_md = [], False, False
    for ev in EVENTS:
        kind = ev[0]
        if kind == "print":
            raw = ev[1]
            text = raw.strip()
            if not text:
                continue
            if raw.startswith("  "):                     # an indented cheat-sheet line
                md += ["```text", raw.rstrip(), "```", ""]
                continue
            m = re.match(r"^(?:---|===)\s*(.*?)\s*(?:===)?$", text)
            if m:
                if setup:
                    md += ["**Setup** (copy and paste this first):", "", "```bash", "\n".join(setup), "```", ""]
                    setup = []
                md += [f"### {m.group(1)}", ""]
            else:
                md += [text.replace("\n", "  \n"), ""]
            started = True
            continue
        if kind in ("write", "append"):
            if not started and getattr(mod, "SETUP_MD", None):    # the hand-written setup covers it
                continue
            block = heredoc(kind, ev[1], ev[2])
            (setup.append(block) if not started else md.extend(["```bash", block, "```", ""]))
            continue
        _, show, transcript = ev
        if not show and getattr(mod, "SETUP_MD", None):
            if not used_setup_md:
                setup.append(mod.SETUP_MD.strip(chr(10)))
                used_setup_md = True
            continue
        if not show:
            cmds = [l[2:] for l in transcript.splitlines() if l.startswith("$ ")]
            setup.extend(cmds)
            continue
        if setup:
            md += ["**Setup** (copy and paste this first):", "", "```bash", "\n".join(setup), "```", ""]
            setup = []
        md += ["```console", transcript.strip("\n"), "```", ""]
        started = True
    if notes.get("Watch out"):
        md += [f"> ⚠️ **Watch out:** {notes['Watch out']}", ""]
    if notes.get("In real jobs"):
        md += [f"**In real jobs:** {notes['In real jobs']}", ""]
    if notes.get("Interview"):
        q, _, a = notes["Interview"].partition(" A: ")
        md += ["## Interview question", "", f"**{q.replace('Q: ', '').strip()}**", "", a.strip(), ""]
    md += [f"[← Back to the module](README.md)", ""]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(md))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--all"]:                                  # one process per lesson keeps the hooks clean
        import subprocess
        for src in sorted(SOURCES.glob("*/*.py")):
            subprocess.run([sys.executable, __file__, str(src)], check=True)
        sys.exit()
    for arg in args:
        lesson = Path(arg).resolve()
        target = ROOT / lesson.parent.name / (lesson.stem + ".md")
        target.write_text(convert(lesson), encoding="utf-8", newline="\n")
        sys.__stdout__.write(f"wrote {target.relative_to(ROOT)}\n")
