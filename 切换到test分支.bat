@echo off
chcp 65001 >nul
echo ========================================
echo 正在切换到test分支...
echo ========================================
echo.

git fetch origin
git checkout test
git branch

echo.
echo ========================================
echo 操作完成！当前分支信息已显示
echo ========================================
pause

