# Solution · Exercise 2: Clean commits and a .gitignore

Run these commands inside `playground/ex02` (after `bash exercises/ex02_clean_commits/setup.sh`). Try it yourself first!

```bash
echo ".env" > .gitignore
echo "*.log" >> .gitignore
git add .gitignore
git commit -m "Add gitignore"
git add cart.py coupon.py
git commit -m "Add coupons"
git add README.md
git commit -m "Document coupons"
git status --short
git log --oneline
```

Then check:

```bash
bash exercises/ex02_clean_commits/check.sh
```

[← Exercise](../exercises/ex02_clean_commits/README.md)
