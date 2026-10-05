rm -rf .git
git init
git branch -m main
git remote add origin https://github.com/vietndj/k.git
git add .
git commit -m "chore: optimize repository by removing 3GB of assets and history"
git push -f origin main
