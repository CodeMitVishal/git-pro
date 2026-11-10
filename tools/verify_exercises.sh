#!/usr/bin/env bash
# Maintainer check: every exercise must FAIL before solving and PASS with its solution.
#   bash tools/verify_exercises.sh
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
status=0
for dir in "$ROOT"/exercises/ex*/; do
  name=$(basename "$dir"); n=${name:2:2}
  bash "$dir/setup.sh" >/dev/null 2>&1 || { echo "SETUP FAILED  $name"; status=1; continue; }
  if bash "$dir/check.sh" >/dev/null 2>&1; then echo "STARTER PASSES (should fail)  $name"; status=1; fi
  solution=$(awk '/^```bash$/{n++; next} /^```$/{inblk=0} n==1 && !/^```/{print}' "$ROOT/solutions/$name.md")
  (cd "$ROOT/playground/ex$n" && bash -c "$solution") >/dev/null 2>&1
  if bash "$dir/check.sh" >/dev/null 2>&1; then echo "ok  $name"; else echo "SOLUTION FAILS  $name"; bash "$dir/check.sh"; status=1; fi
done
exit $status
