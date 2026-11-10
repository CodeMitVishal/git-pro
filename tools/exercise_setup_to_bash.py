"""Maintainer tool: turn the Python exercise setups into Git Bash setup.sh scripts.

    python tools/exercise_setup_to_bash.py

Reads tools/exercise_sources/exNN_*.py, records every git command and file write
their setup() makes, and writes exercises/exNN_*/setup.sh.
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import sandbox  # noqa: E402

HEADER = """#!/usr/bin/env bash
# Exercise {n}: builds the practice repository in playground/{folder}
# Run from anywhere:  bash exercises/{name}/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground {folder}
"""


def record(setup):
    events = []
    orig_script, orig_write, orig_append = sandbox.Sandbox.script, sandbox.Sandbox.write, sandbox.Sandbox.append

    def script(self, text, show=True, env=None):
        self._depth = getattr(self, "_depth", 0) + 1
        out = orig_script(self, text, show=False, env=env)
        self._depth -= 1
        events.extend(("cmd", l[2:]) for l in out.splitlines() if l.startswith("$ "))
        return out

    def write(self, rel, text):
        if getattr(self, "_depth", 0) == 0:
            events.append(("write", rel, text))
        orig_write(self, rel, text)

    def append(self, rel, text):
        if getattr(self, "_depth", 0) == 0:
            events.append(("append", rel, text))
        orig_append(self, rel, text)

    sandbox.Sandbox.script, sandbox.Sandbox.write, sandbox.Sandbox.append = script, write, append
    try:
        setup(sandbox.Sandbox())
    finally:
        sandbox.Sandbox.script, sandbox.Sandbox.write, sandbox.Sandbox.append = orig_script, orig_write, orig_append
    return events


def to_bash(events):
    lines = []
    for ev in events:
        if ev[0] == "cmd":
            cmd = ev[1]
            if cmd == "git init":
                cmd = "git init -q -b main"
            elif cmd.startswith("git init --bare"):
                cmd = cmd.replace("git init --bare", "git init -q --bare -b main")
            lines.append(cmd)
        else:
            arrow = ">>" if ev[0] == "append" else ">"
            lines.append(f"cat {arrow} {ev[1]} <<'EOF'\n{ev[2].rstrip(chr(10))}\nEOF")
    return "\n".join(lines)


if __name__ == "__main__":
    for src in sorted((ROOT / "tools" / "exercise_sources").glob("ex*.py")):
        spec = importlib.util.spec_from_file_location("ex", src)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        folder = f"ex{mod.NUMBER:02d}"
        out_dir = ROOT / "exercises" / src.stem
        out_dir.mkdir(parents=True, exist_ok=True)
        body = getattr(mod, "SETUP_SH", None) or to_bash(record(mod.setup))
        text = HEADER.format(n=mod.NUMBER, folder=folder, name=src.stem) + body.strip("\n") + "\n\nfinish_setup " + folder + "\n"
        (out_dir / "setup.sh").write_text(text, encoding="utf-8", newline="\n")
        print("wrote", (out_dir / "setup.sh").relative_to(ROOT))
