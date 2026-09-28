# Git cheat sheet
```bash
git init
git status
git add .
git commit -m "feat: add ticket model"
git switch -c feature/sla
git push -u origin feature/sla
git pull --rebase origin main
git merge feature/sla
git log --oneline --graph
```
Conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`. Edit, `git add`, `git commit`.

Commit message style: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`.
