import json

with open("all_unique_posters.json", "r") as f:
    deduped_data = json.load(f)

html = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thư Viện Prompt - Toàn Tập</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            margin: 0;
            padding: 24px;
            line-height: 1.6;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
            padding: 40px 20px;
            background: #1e293b;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.5);
        }
        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin: 0 0 10px 0;
            color: #f8fafc;
        }
        .subtitle {
            color: #94a3b8;
            font-size: 1.1rem;
        }
        .fluid-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
            gap: 20px;
            align-items: start;
        }
        .card {
            background: #1e293b;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.3);
            transition: transform 0.2s;
            position: relative;
        }
        .card:hover {
            transform: translateY(-4px);
        }
        .img-container img {
            width: 100%;
            height: auto;
            display: block;
            aspect-ratio: 9/16;
            object-fit: cover;
        }
        
        /* Copy Button Icon over Image */
        .copy-btn {
            position: absolute;
            top: 12px;
            right: 12px;
            background-color: rgba(15, 23, 42, 0.7);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 8px 12px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            backdrop-filter: blur(4px);
            opacity: 0;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .card:hover .copy-btn {
            opacity: 1;
        }
        .copy-btn:hover {
            background-color: rgba(59, 130, 246, 0.9);
            transform: scale(1.05);
        }
        .copy-btn.copied {
            background-color: rgba(16, 185, 129, 0.9);
        }
        .copy-btn svg {
            width: 16px;
            height: 16px;
            fill: currentColor;
        }
    </style>
</head>
<body>
    <header>
        <h1>Thư Viện Prompt (Bộ Sưu Tập Đầy Đủ)</h1>
        <div class="subtitle">Tổng số: """ + str(len(deduped_data)) + """ concept độc bản (Đã lọc 100% trùng lặp)</div>
    </header>
    
    <div class="fluid-grid">
"""

copy_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M16 1H4C2.9 1 2 1.9 2 3v14h2V3h12V1zm3 4H8C6.9 5 6 5.9 6 7v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>"""

for i, item in enumerate(deduped_data):
    path = item["path"]
    
    # fix relative paths to ensure they load on fedu.vn/k
    if not path.startswith("http") and not path.startswith("assets") and not path.startswith("/"):
        path = "assets/covers/" + path # assuming root files are covers
        
    prompt_safe = json.dumps(item['prompt'])
    
    html += f"""
        <div class="card">
            <div class="img-container">
                <img src="{path}" loading="lazy" alt="Poster">
            </div>
            <button class="copy-btn" title="Copy Prompt" onclick='copyPrompt(this, {prompt_safe})'>
                {copy_svg}
                <span>Copy</span>
            </button>
        </div>
    """

html += """
    </div>

    <script>
        function copyPrompt(btn, text) {
            navigator.clipboard.writeText(text).then(() => {
                const span = btn.querySelector('span');
                const originalText = span.innerText;
                span.innerText = "Đã Copy!";
                btn.classList.add("copied");
                setTimeout(() => {
                    span.innerText = originalText;
                    btn.classList.remove("copied");
                }, 2000);
            });
        }
    </script>
</body>
</html>
"""

with open("anh.html", "w") as f:
    f.write(html)
print(f"Updated anh.html successfully. Now showing {len(deduped_data)} unique posters.")
