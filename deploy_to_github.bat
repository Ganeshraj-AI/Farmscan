@echo off
echo ========================================
echo   FarmScan - GitHub Setup Helper
echo ========================================
echo.

echo This script will help you push FarmScan to GitHub
echo.

echo Step 1: Create a new repository on GitHub
echo -----------------------------------------
echo 1. Go to https://github.com/new
echo 2. Repository name: farmscan
echo 3. Description: AI-Powered Crop Disease Detection
echo 4. Keep it PUBLIC (or private if you prefer)
echo 5. DO NOT initialize with README (we already have one)
echo 6. Click "Create repository"
echo.

pause

echo.
echo Step 2: Enter your GitHub repository URL
echo -----------------------------------------
set /p REPO_URL="Paste your repository URL (e.g., https://github.com/username/farmscan.git): "

echo.
echo Step 3: Pushing to GitHub...
echo -----------------------------------------

git remote add origin %REPO_URL%
git branch -M main
git push -u origin main

echo.
echo ========================================
echo   SUCCESS! Code pushed to GitHub
echo ========================================
echo.
echo Next steps:
echo 1. Go to https://render.com
echo 2. Sign up/Login with GitHub
echo 3. Click "New +" then "Web Service"
echo 4. Connect your farmscan repository
echo 5. Click "Create Web Service"
echo.
echo Your app will be live in ~5 minutes!
echo.
pause
