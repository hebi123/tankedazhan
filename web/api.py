from __future__ import annotations

from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__, url_prefix="/api")


@api.get("/levels")
def list_levels():
    # 占位：后续从 game/data/levels 读取
    data = [
        {"id": 1, "name": "训练关", "enemies": 10},
        {"id": 2, "name": "城区", "enemies": 20},
    ]
    return jsonify(data)


@api.post("/progress")
def save_progress():
    body = request.get_json(silent=True) or {}
    # 占位：后续持久化到 JSON
    return jsonify({"ok": True, "echo": body})


@api.get("/level/<int:level_id>")
def get_level(level_id: int):
    # 加宽地图以容纳CURSOR字母：30x26 网格，外围钢板，内部分布砖块与草地
    W, H = 30, 26
    tiles = [["ground" for _ in range(W)] for _ in range(H)]
    for x in range(W):
        tiles[0][x] = tiles[H-1][x] = "steel"
    for y in range(H):
        tiles[y][0] = tiles[y][W-1] = "steel"
    # 用砖块拼成 "CURSOR" 字母 - 横向排列
    # 字母设计：每个字母 4x5 像素，字母间距 1 像素
    # 起始位置：x=3, y=4
    
    # 定义每个字母的像素图案（4x5尺寸）
    letters = {
        'C': [
            " ###",
            "#   ",
            "#   ",
            "#   ",
            " ###"
        ],
        'U': [
            "#  #",
            "#  #",
            "#  #",
            "#  #",
            " ## "
        ],
        'R': [
            "### ",
            "#  #",
            "### ",
            "# # ",
            "#  #"
        ],
        'S': [
            " ###",
            "#   ",
            " ## ",
            "   #",
            " ###"
        ],
        'O': [
            " ## ",
            "#  #",
            "#  #",
            "#  #",
            " ## "
        ]
    }
    
    # 横向排列字母：C-U-R-S-O-R
    word = "CURSOR"
    start_x, start_y = 2, 4  # 调整位置，确保完全显示
    letter_width = 5  # 每个字母宽度（4像素 + 1像素间距）
    
    for i, letter in enumerate(word):
        if letter in letters:
            letter_x = start_x + i * letter_width
            letter_pattern = letters[letter]
            
            # 绘制当前字母
            for row in range(len(letter_pattern)):
                for col in range(len(letter_pattern[row])):
                    if letter_pattern[row][col] == '#':
                        map_x = letter_x + col
                        map_y = start_y + row
                        if 0 <= map_x < W and 0 <= map_y < H:
                            tiles[map_y][map_x] = "brick"
    # 草地带（调整位置，避免与字母重叠）
    for x in range(5, 25):
        tiles[15][x] = "grass"
    
    # 基地防护钢板 - 在基地周围添加不可破坏的钢板
    base_x, base_y = W//2, H-2  # 基地位置 [13, 24]
    
    # 基地上方防护
    tiles[base_y-1][base_x-1] = "steel"  # 左上
    tiles[base_y-1][base_x] = "steel"    # 正上
    tiles[base_y-1][base_x+1] = "steel"  # 右上
    
    # 基地左右防护
    tiles[base_y][base_x-2] = "steel"    # 左左
    tiles[base_y][base_x-1] = "steel"    # 左
    tiles[base_y][base_x+1] = "steel"    # 右
    tiles[base_y][base_x+2] = "steel"    # 右右
    
    # 基地下方防护
    tiles[base_y+1][base_x-1] = "steel"  # 左下
    tiles[base_y+1][base_x] = "steel"    # 正下
    tiles[base_y+1][base_x+1] = "steel"  # 右下

    data = {
        "id": level_id,
        "size": [W, H],
        "tile_size": 16,
        "tiles": tiles,
        "player_spawn": [2, H-3],
        "enemy_spawns": [[1, 1], [W//2, 1], [W-2, 1]],
        "base": [W//2, H-2],
        "enemy_waves": [
            {"type": "normal", "count": 5, "interval": 2.0},
            {"type": "fast", "count": 3, "interval": 1.5},
            {"type": "heavy", "count": 2, "interval": 3.0},
            {"type": "special", "count": 1, "interval": 5.0}
        ],
        "max_enemies_on_screen": 4,
        "total_enemies": 11
    }
    return jsonify(data)


@api.get("/enemy_types")
def get_enemy_types():
    """获取敌人类型配置"""
    types = {
        "normal": {
            "name": "普通坦克",
            "speed": 60,
            "health": 1,
            "fire_rate": 1.0,
            "color": "#ef4444",
            "size": 16
        },
        "fast": {
            "name": "快速坦克", 
            "speed": 100,
            "health": 1,
            "fire_rate": 1.5,
            "color": "#f97316",
            "size": 14
        },
        "heavy": {
            "name": "重装坦克",
            "speed": 40,
            "health": 2,
            "fire_rate": 0.8,
            "color": "#6b7280",
            "size": 20
        },
        "special": {
            "name": "特殊坦克",
            "speed": 80,
            "health": 1,
            "fire_rate": 2.0,
            "color": "#8b5cf6",
            "size": 18
        }
    }
    return jsonify(types)


