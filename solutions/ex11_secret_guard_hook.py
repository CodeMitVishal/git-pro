r"""Solution · Exercise 11: A pre-commit hook that stops leaked secrets

Run it:  python solutions/ex11_secret_guard_hook.py

The hook (.git/hooks/pre-commit):

    #!/bin/sh
    if git diff --cached | grep -qE "^\+.*(PASSWORD|API_KEY)="; then
      echo "pre-commit: secret found in staged changes. Commit blocked."
      exit 1
    fi

Then: chmod +x .git/hooks/pre-commit
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from sandbox import solve  # noqa: E402

HOOK = r"""#!/bin/sh
if git diff --cached | grep -qE "^\+.*(PASSWORD|API_KEY)="; then
  echo "pre-commit: secret found in staged changes. Commit blocked."
  exit 1
fi
"""


def install(sb):
    sb.write(".git/hooks/pre-commit", HOOK)
    print(sb.script("chmod +x .git/hooks/pre-commit\ncat .git/hooks/pre-commit", show=False))


if __name__ == "__main__":
    solve("ex11_secret_guard_hook.py", install)
