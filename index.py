from flask import Flask, render_template_string

app = Flask(__name__)

# === 修复后的完整 HTML 模板 (包含防 F12/防右键代码) ===
# 关键点：这里使用了 ''' 三单引号，这样 HTML 内部就可以自由使用双引号 "
# 关键点：HTML 结构必须完整闭合，否则后面的 Python 代码会跑出来
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的游戏大厅</title>

    <!-- --- 样式 --- -->
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #1a1a2e;
            color: #ffffff;
            margin: 0;
            padding: 0;
            text-align: center;
        }

        header {
            background-color: #16213e;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }

        header h1 {
            margin: 0;
            color: #e94560;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .game-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 30px;
            padding: 40px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .game-card {
            background-color: #0f3460;
            border-radius: 15px;
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            text-decoration: none;
            color: inherit;
            display: block;
        }

        .game-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 20px rgba(233, 69, 96, 0.4);
        }

        .game-image {
            width: 100%;
            height: 150px;
            object-fit: cover;
        }

        .game-info {
            padding: 20px;
        }

        .game-title {
            font-size: 1.2em;
            margin: 10px 0;
            font-weight: bold;
        }

        .game-desc {
            font-size: 0.9em;
            color: #a0a0a0;
            margin-bottom: 15px;
        }

        .play-btn {
            display: inline-block;
            background-color: #e94560;
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
        }
    </style>

    <!-- 🔒 第一层防护：防 F12 和 右键 -->
    <script>
        // 1. 禁用 F12 和 Ctrl+Shift+I
        document.addEventListener('keydown', function(e) {
            if (e.key === 'F12' || (e.ctrlKey && e.shiftKey && e.key === 'I')) {
                e.preventDefault();
                alert("开发者工具已禁用");
            }
        });

        // 2. 禁用右键菜单
        document.addEventListener('contextmenu', function(e) {
            e.preventDefault();
            alert("右键功能已禁用");
        });
    </script>
</head>
<body>

    <header>
        <h1>游戏大厅</h1>
    </header>

    <main class="game-container">
        <!-- 游戏卡片 1 -->
        <a href="https://alan11120967.github.io/my-site/" class="game-card" target="_blank">
            <img src="Pic/OIP-C.webp" alt="游戏封面" class="game-image">
            <div class="game-info">
                <div class="game-title">逃离设施</div>
                <div class="game-desc">类似SCP的CB。</div>
                <span class="play-btn">开始游戏</span>
            </div>
        </a>

        <!-- 游戏卡片 2 -->
        <a href="https://alan11120967.github.io/gun/" class="game-card" target="_blank">
            <img src="Pic/gun.jpg" alt="游戏封面" class="game-image">
            <div class="game-info">
                <div class="game-title">轮盘赌:生与死</div>
                <div class="game-desc">用把左轮对战。</div>
                <span class="play-btn">开始游戏</span>
            </div>
        </a>
    </main>

</body>
</html>
'''

# === 路由逻辑 ===
@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

# 运行服务器
if __name__ == '__main__':
    app.run(debug=False)
