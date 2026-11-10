# Solution · Exercise 11: A pre-commit hook that stops leaked secrets

Run these commands inside `playground/ex11` (after `bash exercises/ex11_secret_guard_hook/setup.sh`). Try it yourself first!

```bash
cat > .git/hooks/pre-commit <<'EOF'
#!/bin/sh
if git diff --cached | grep -qE "^\+.*(PASSWORD|API_KEY)="; then
  echo "pre-commit: secret found in staged changes. Commit blocked."
  exit 1
fi
EOF
chmod +x .git/hooks/pre-commit
```

Then check:

```bash
bash exercises/ex11_secret_guard_hook/check.sh
```

[← Exercise](../exercises/ex11_secret_guard_hook/README.md)
