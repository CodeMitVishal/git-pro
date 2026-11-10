#!/usr/bin/env bash
# Exercise 10: builds the practice repository in playground/ex10
# Run from anywhere:  bash exercises/ex10_find_the_bug/setup.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
source "$ROOT/exercises/lib.sh"
start_playground ex10
git init -q -b main
printf '#!/bin/sh\ngrep -q "1.19" price.txt\n' > check_price.sh
printf 'answer.txt\n' > .gitignore
for i in $(seq 1 30); do
  if [ $i -ge 23 ]; then rate=1.18; else rate=1.19; fi
  echo "gross = net * $rate" > price.txt
  echo "change $i" >> CHANGELOG.txt
  git add . && git commit -q -m "Change $i"
done
git tag v1.0.0 HEAD~29

finish_setup ex10
