"""Git Pro · The sandbox every lesson and exercise uses.

A Sandbox is a throwaway Git repository in a temporary folder with its own Git
settings, so the lessons never touch your real repositories or your global config.
Commit dates are fixed, so commit IDs (hashes) are the same on every run, and the
output you see matches the slides.

    sb = Sandbox()
    sb.script('''
    git init
    echo "hello" > README.md
    git add README.md
    git commit -m "First commit"
    git log --oneline
    ''')

The script understands git commands plus a few shell basics that also work on
Windows: echo "text" > file, echo "text" >> file, cat file, mkdir dir, rm file,
cd dir, chmod +x file, and # comments. NAME=value before a command sets an environment variable.
"""
from __future__ import annotations

import atexit
import os
import shlex
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE_TIME = 1_793_088_000          # a fixed moment in late Oct 2026, so hashes never change


def _rmtree(path: Path) -> None:
    def unlock(func, p, _exc):     # Git marks object files read-only on Windows
        os.chmod(p, stat.S_IWRITE)
        func(p)
    shutil.rmtree(path, onerror=unlock)


class Sandbox:
    def __init__(self, path: str | Path | None = None, name: str = "project", keep: bool = False):
        if path is None:
            self.base = Path(tempfile.mkdtemp(prefix="gitpro_"))
            self.root = self.base / name
            self.root.mkdir()
            if not keep:
                atexit.register(_rmtree, self.base)
        else:
            self.base = Path(path).resolve().parent
            self.root = Path(path).resolve()
            if self.root.exists():
                _rmtree(self.root)
            self.root.mkdir(parents=True)
        self.cwd = self.root
        self.tick = 0
        config = self.base / f".gitconfig_{self.root.name}"
        config.write_text(
            "[user]\n\tname = Vishal\n\temail = vishal@example.com\n"
            "[init]\n\tdefaultBranch = main\n"
            "[core]\n\tpager = cat\n\tautocrlf = false\n\tquotepath = false\n"
            "[color]\n\tui = false\n"
            "[advice]\n\tdetachedHead = false\n\tskippedCherryPicks = false\n"
            "[pull]\n\trebase = false\n"
            "[merge]\n\tconflictStyle = merge\n"
            '[protocol "file"]\n\tallow = always\n',
            encoding="utf-8")
        self.env = {**os.environ, "GIT_CONFIG_GLOBAL": str(config), "GIT_CONFIG_NOSYSTEM": "1",
                    "GIT_EDITOR": "true", "GIT_TERMINAL_PROMPT": "0", "LANG": "C", "LC_ALL": "C"}
        self.env.pop("GIT_DIR", None)

    # ---------------------------------------------------------------- helpers
    def path(self, rel: str = "") -> Path:
        return self.cwd / rel

    def write(self, rel: str, text: str) -> None:
        p = self.path(rel)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8", newline="\n")

    def append(self, rel: str, text: str) -> None:
        with self.path(rel).open("a", encoding="utf-8", newline="\n") as f:
            f.write(text)

    def read(self, rel: str) -> str:
        return self.path(rel).read_text(encoding="utf-8")

    def git(self, *args: str) -> str:
        """Run git quietly and return its output (for checks and setup)."""
        return self._exec(["git", *args], {}).stdout.strip()

    def tidy(self, text: str) -> str:
        """Replace temporary folder paths with friendly ones."""
        for sep in ("/", "\\"):                          # project/../x  ->  ~/x
            for form in (str(self.root), self.root.as_posix()):
                text = text.replace(form + sep + "..", "~")
        for p, nice in ((self.root, "~/project"), (self.base, "~")):
            for form in (str(p), p.as_posix()):
                text = text.replace(form, nice)
        return text

    # ---------------------------------------------------------------- running
    def _exec(self, argv: list[str], extra_env: dict[str, str]) -> subprocess.CompletedProcess:
        self.tick += 1
        stamp = f"{BASE_TIME + self.tick * 60} +0000"
        env = {**self.env, "GIT_AUTHOR_DATE": stamp, "GIT_COMMITTER_DATE": stamp, **extra_env}
        return subprocess.run(argv, cwd=self.cwd, env=env, capture_output=True, text=True,
                              encoding="utf-8", errors="replace")

    def run(self, line: str, env: dict | None = None) -> str:
        """Run ONE command line and return its output (stdout + stderr)."""
        line = line.strip()
        if not line or line.startswith("#"):
            return ""
        if line.startswith("echo ") and (">>" in line or ">" in line):
            op = ">>" if ">>" in line else ">"
            left, target = line[5:].split(op, 1)
            text = " ".join(shlex.split(left)) + "\n"
            (self.append if op == ">>" else self.write)(target.strip(), text)
            return ""
        parts = shlex.split(line)
        cmd = parts[0]
        if cmd == "cd":
            self.cwd = (self.cwd / parts[1]).resolve()
            return ""
        if cmd == "mkdir":
            self.path(parts[-1]).mkdir(parents=True, exist_ok=True)
            return ""
        if cmd == "rm":
            target = self.path(parts[-1])
            _rmtree(target) if target.is_dir() else target.unlink()
            return ""
        if cmd == "chmod":
            target = self.path(parts[-1])
            target.chmod(target.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
            return ""
        if cmd == "cat":
            return self.read(parts[1]).rstrip(chr(10))
        extra = dict(env or {})
        while "=" in parts[0] and not parts[0].startswith("-"):
            key, value = parts.pop(0).split("=", 1)
            extra[key] = value
        r = self._exec(parts, extra)
        return self.tidy((r.stdout + r.stderr).rstrip("\n"))

    def script(self, text: str, show: bool = True, env: dict | None = None) -> str:
        """Run several lines; return (and print) a transcript with $ prompts.
        env: extra environment variables for every command (e.g. GIT_SEQUENCE_EDITOR)."""
        out = []
        for raw in text.strip("\n").splitlines():
            line = raw.strip()
            if not line:
                continue
            if line.startswith("#"):
                out.append(line)
                continue
            out.append(f"$ {line}")
            result = self.run(line, env)
            if result:
                out.append(result)
        transcript = "\n".join(out)
        if show:
            print(transcript)
            print()
        return transcript

    def fake_editor(self, new_todo: str) -> str:
        """A tiny 'editor' for git rebase -i: it replaces the todo list with new_todo.
        Use it as:  sb.script("git rebase -i HEAD~3", env={"GIT_SEQUENCE_EDITOR": editor})"""
        helper = self.base / f"editor_{self.tick}.py"
        helper.write_text(
            "import sys\nopen(sys.argv[1], 'w').write(" + repr(new_todo.strip() + "\n") + ")\n",
            encoding="utf-8")
        return f'"{Path(sys.executable).as_posix()}" "{helper.as_posix()}"'


# ==================================================================== exercises
def exercise(number: int, title: str, task: str, setup, check) -> None:
    """Command-line wrapper for every exercise file.

    python exercises/exNN_name.py setup   -> build the practice repo in playground/exNN
    python exercises/exNN_name.py check   -> check your work
    """
    folder = ROOT / "playground" / f"ex{number:02d}"
    action = sys.argv[1] if len(sys.argv) > 1 else "help"
    if action == "setup":
        sb = Sandbox(folder)
        setup(sb)
        print(f"Exercise {number}: {title}\n\nYour practice repository is ready:\n    cd playground/ex{number:02d}\n")
        print(task.strip())
        print(f"\nWhen you're done:\n    python exercises/{Path(sys.argv[0]).name} check")
    elif action == "check":
        if not folder.exists():
            sys.exit("Run 'setup' first.")
        problems = run_check(folder, check)
        if problems:
            print("Not yet:")
            for p in problems:
                print("  -", p)
            sys.exit(1)
        print("All checks passed!")
    else:
        print(f"Exercise {number}: {title}\n\n{task.strip()}\n\nStart with:\n    python exercises/{Path(sys.argv[0]).name} setup")


def run_check(folder: Path, check) -> list[str]:
    sb = Sandbox.__new__(Sandbox)              # reuse helpers on an existing folder
    sb.root = sb.cwd = Path(folder).resolve()
    sb.base = sb.root.parent
    sb.tick = 10_000
    sb.env = {**os.environ, "GIT_EDITOR": "true", "LANG": "C", "LC_ALL": "C",
              "GIT_CONFIG_GLOBAL": str(sb.base / f".gitconfig_{sb.root.name}"), "GIT_CONFIG_NOSYSTEM": "1"}
    try:
        return list(check(sb))
    except Exception as e:                     # a check that crashes means "not solved yet"
        return [f"{type(e).__name__}: {e}"]


def solve(exercise_file: str, commands) -> None:
    """Used by solutions/: fresh setup, run the solution commands, then check."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("ex", ROOT / "exercises" / exercise_file)
    mod = importlib.util.module_from_spec(spec)
    sys.argv = [exercise_file, "none"]
    spec.loader.exec_module(mod)
    folder = ROOT / "playground" / f"ex{mod.NUMBER:02d}"
    sb = Sandbox(folder)
    mod.setup(sb)
    sb.cwd = folder
    if callable(commands):                     # a Python solution (e.g. plumbing that needs IDs)
        commands(sb)
    else:
        print(sb.script(commands, show=False))
    problems = run_check(folder, mod.check)
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("\nAll checks passed!")
