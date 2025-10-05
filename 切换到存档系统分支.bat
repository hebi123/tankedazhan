@echo off
chcp 65001 >nul
echo ========================================
echo 正在从GitHub获取存档系统分支...
echo ========================================
echo.

git fetch origin
git checkout -b 存档系统 origin/存档系统

echo.
echo ========================================
echo 已切换到存档系统分支！
echo ========================================
pause

