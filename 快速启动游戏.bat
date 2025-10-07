@echo off
chcp 65001 >nul
echo ========================================
echo 坦克大战游戏 - 启动中...
echo ========================================
echo.
echo 正在启动服务器...
start http://127.0.0.1:5000/game
echo 游戏页面已在浏览器中打开
echo.
echo 按 Ctrl+C 可停止服务器
echo ========================================
.\.venv\Scripts\python.exe -m web.app
