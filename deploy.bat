@echo off
echo ========================================================
echo   LOTUS HUT DRIVE-IN CAFE - GITHUB PAGES DEPLOYER
echo ========================================================
echo.
echo [1/3] Staging all files...
git add .
echo.
echo [2/3] Committing changes...
git commit -m "Deploy Lotus Hut Drive-In Digital Menu and Staff Portal"
echo.
echo [3/3] Pushing to GitHub (main)...
git push -u origin main --force
echo.
echo [DONE] Deployed successfully to https://hospitalityqr.github.io/shree-driving/
pause
