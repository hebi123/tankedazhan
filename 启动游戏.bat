@echo off
echo 正在启动坦克大战游戏...
echo.
echo 游戏链接：
echo 首页: http://127.0.0.1:5000/
echo 游戏: http://127.0.0.1:5000/game
echo 关卡: http://127.0.0.1:5000/levels
echo 健康: http://127.0.0.1:5000/health
echo.
echo 按任意键打开游戏页面...
pause >nul
start http://127.0.0.1:5000/game
echo 正在启动服务器...
python -m web.app
