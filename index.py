from flask import Flask, render_template_string, url_for

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的游戏大厅</title>

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

        /* 修复图片样式：确保高度固定 */
        .game-image {
            width: 100%;
            height: 150px;
            object-fit: cover;
            background-color: #ddd; /* 防止图片加载失败时布局塌陷 */
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
            /* 移除了 pointer-events: none; 因为这会让链接无法点击 */
        }
    </style>

    <script>
        // 提示：这段JS仅用于前端体验，无法真正阻止懂技术的用户访问
        document.addEventListener('keydown', function(e) {
            if (e.key === 'F12' || (e.ctrlKey && e.shiftKey && e.key === 'I')) {
                e.preventDefault();
                console.log("开发者工具已禁用（仅前端提示）");
            }
        });

        document.addEventListener('contextmenu', function(e) {
            e.preventDefault();
            console.log("右键功能已禁用");
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
            <!-- 修复：使用网络图片确保加载成功，或者请将图片放入 static 文件夹并使用 url_for -->
            <img src="https://via.placeholder.com/300x150/333/fff?text=SCP+Game" alt="游戏封面" class="game-image">
            <div class="game-info">
                <div class="game-title">逃离设施</div>
                <div class="game-desc">类似SCP的CB。</div>
                <span class="play-btn">开始游戏</span>
            </div>
        </a>

        <!-- 游戏卡片 2 -->
        <a href="https://alan11120967.github.io/gun/" class="game-card" target="_blank">
            <img src="https://via.placeholder.com/300x150/333/fff?text=Gun+Game" alt="游戏封面" class="game-image">
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

@app.route('/')
def index():
    # render_template_string 可以直接渲染字符串
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # 关闭 Debug 模式以防止代码泄露
    app.run(debug=False, host='0.0.0.0', port=5000)
