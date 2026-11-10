#!/usr/bin/env bash
# Shared helpers for the exercise scripts (Git Bash on Windows, any shell on macOS/Linux).

# Setup commits are made as "Git Pro" so the scripts work even before you set user.name.
export GIT_AUTHOR_NAME="Git Pro" GIT_AUTHOR_EMAIL="setup@git-pro.local"
export GIT_COMMITTER_NAME="Git Pro" GIT_COMMITTER_EMAIL="setup@git-pro.local"
export GIT_EDITOR=true

# start_playground ex03  -> fresh, empty playground/ex03, and cd into it
start_playground() {
  PLAY="$ROOT/playground/$1"
  rm -rf "$PLAY"
  mkdir -p "$PLAY"
  cd "$PLAY"
}

# finish_setup ex03  -> print the task and the next steps
finish_setup() {
  unset GIT_AUTHOR_NAME GIT_AUTHOR_EMAIL GIT_COMMITTER_NAME GIT_COMMITTER_EMAIL
  echo
  echo "Practice repository ready:  playground/$1"
  echo "Read the task:              exercises/*${1#ex}*/README.md"
  echo "Then:  cd playground/$1   ...use Git...   bash exercises/<this exercise>/check.sh"
}

# ---- checking -----------------------------------------------------------------
PROBLEMS=()
problem() { PROBLEMS+=("$1"); }

# open_playground ex03 -> cd into it, or stop if setup wasn't run
open_playground() {
  PLAY="$ROOT/playground/$1"
  if [ ! -d "$PLAY" ]; then
    echo "Run the setup first:  bash exercises/<exercise>/setup.sh"
    exit 1
  fi
  cd "$PLAY"
}

# g <args...>  -> git output with errors hidden (for checks)
g() { git "$@" 2>/dev/null; }

report() {
  if [ ${#PROBLEMS[@]} -eq 0 ]; then
    echo "All checks passed!"
    exit 0
  fi
  echo "Not yet:"
  for p in "${PROBLEMS[@]}"; do echo "  - $p"; done
  exit 1
}
