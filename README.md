# 坦克大战游戏 (Tank Battle Game)

一个使用Python Flask和JavaScript开发的经典坦克大战游戏，支持Web浏览器游玩。

## 🎮 游戏特色

- **经典玩法**：重现经典坦克大战的核心玩法
- **Web技术**：使用Flask后端 + JavaScript前端，无需安装即可游玩
- **多种敌人**：4种不同类型的敌方坦克，各有特色
- **道具系统**：丰富的道具和升级系统
- **关卡设计**：程序化生成的地图和关卡
- **视觉效果**：现代化的UI设计和流畅的动画效果

## 🚀 快速开始

### 环境要求

- Python 3.7+
- 现代Web浏览器（Chrome、Firefox、Safari、Edge）

### 安装步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/yourusername/tankedazhan.git
   cd tankedazhan
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv .venv
   ```

3. **激活虚拟环境**
   - Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

5. **启动游戏**
   ```bash
   python -m web.app
   ```

6. **打开浏览器**
   访问 http://127.0.0.1:5000

## 🎯 游戏操作

### 基本控制
- **移动**：WASD 或 方向键
- **射击**：J 或 空格键
- **暂停**：ESC
- **重启**：R

### 游戏目标
- 消灭所有敌方坦克
- 保护我方基地（老鹰）
- 获得最高分数

## 🏗️ 技术架构

### 后端 (Python Flask)
- **框架**：Flask + Flask-CORS
- **API设计**：RESTful API
- **地图生成**：程序化生成关卡
- **数据管理**：JSON格式存储

### 前端 (JavaScript)
- **渲染引擎**：HTML5 Canvas
- **游戏循环**：固定时间步长
- **碰撞检测**：AABB算法
- **状态管理**：面向对象设计

### 核心功能
- **地图系统**：30×26瓦片地图，支持多种地形
- **物理引擎**：碰撞检测、边界限制
- **AI系统**：敌方坦克智能行为
- **音效系统**：背景音乐和音效（待实现）

## 📁 项目结构

```
tankedazhan/
├── web/                    # Flask应用
│   ├── app.py             # 主应用文件
│   ├── api.py             # API接口
│   ├── templates/         # HTML模板
│   │   ├── index.html     # 首页
│   │   ├── game.html      # 游戏页面
│   │   ├── main_menu.html # 主菜单
│   │   ├── levels.html    # 关卡选择
│   │   ├── settings.html  # 设置页面
│   │   ├── help.html      # 帮助页面
│   │   └── about.html     # 关于页面
│   └── static/
│       └── styles.css     # 样式文件
├── requirements.txt       # Python依赖
├── README.md             # 项目说明
├── 项目文件索引.txt       # 文件索引
├── 代码类与函数清单.txt   # 代码文档
└── 启动游戏.bat          # Windows启动脚本
```

## 🎨 游戏元素

### 地形类型
- **砖墙**：可被摧毁，不同耐久度
- **钢板**：不可摧毁
- **草地**：可通行，提供掩护
- **水面**：阻挡移动
- **冰面**：增加移动速度

### 敌方坦克类型
1. **普通坦克**：基础属性，平衡型
2. **快速坦克**：高速度，低血量
3. **重型坦克**：高血量，低速度
4. **特殊坦克**：特殊能力，稀有

### 道具系统（计划中）
- **星星**：提升坦克属性
- **头盔**：临时无敌
- **锹**：加固基地
- **炸弹**：全屏攻击
- **坦克**：额外生命
- **枪**：提升火力

## 🔧 开发计划

### 已完成功能 ✅
- [x] 基础游戏框架
- [x] 玩家坦克控制
- [x] 子弹发射系统
- [x] 碰撞检测
- [x] 地图生成
- [x] 敌方坦克AI
- [x] 游戏UI界面
- [x] 关卡系统
- [x] 基地保护机制

### 开发中功能 🚧
- [ ] 音效系统
- [ ] 道具系统
- [ ] 存档系统
- [ ] 特效系统

### 计划功能 📋
- [ ] 多人对战
- [ ] 关卡编辑器
- [ ] 成就系统
- [ ] 排行榜
- [ ] 移动端适配

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 👨‍💻 作者

- **开发者**：您的名字
- **GitHub**：[@yourusername](https://github.com/yourusername)

## 🙏 致谢

- 感谢所有贡献者的支持
- 灵感来源于经典坦克大战游戏
- 使用开源技术栈构建

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 创建 [Issue](https://github.com/yourusername/tankedazhan/issues)
- 发送邮件至：your.email@example.com

---

⭐ 如果这个项目对您有帮助，请给它一个星标！
