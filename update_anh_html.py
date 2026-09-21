import json
import os
import re

with open("new_anime_prompts.json", "r") as f:
    prompts_data = json.load(f)

html = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thư Viện Prompt - Anime Posters</title>
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
        .card-body {
            padding: 16px;
        }
        .copy-btn {
            width: 100%;
            padding: 12px;
            background-color: #3b82f6;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        .copy-btn:hover {
            background-color: #2563eb;
        }
        .copy-btn.copied {
            background-color: #10b981;
        }
    </style>
</head>
<body>
    <header>
        <h1>Thư Viện Prompt (Anime Collection)</h1>
        <div class="subtitle">Tổng số: """ + str(len(prompts_data)) + """ ảnh đã chuẩn hoá Face DNA</div>
    </header>
    
    <div class="fluid-grid">
"""

for i, item in enumerate(prompts_data):
    filename = item["filename"]
    # Path relative to the html file on fedu.vn/k
    path = f"assets/images_gen_fixes/{filename}"
    
    # Escape prompt string for JS
    prompt_safe = json.dumps(item['prompt'])
    
    html += f"""
        <div class="card">
            <div class="img-container">
                <img src="{path}" loading="lazy" alt="Anime Poster">
            </div>
            <div class="card-body">
                <button class="copy-btn" onclick='copyPrompt(this, {prompt_safe})'>Copy Prompt</button>
            </div>
        </div>
    """

html += """
    </div>

    <script>
        function copyPrompt(btn, text) {
            navigator.clipboard.writeText(text).then(() => {
                const originalText = btn.innerText;
                btn.innerText = "Đã Copy!";
                btn.classList.add("copied");
                setTimeout(() => {
                    btn.innerText = originalText;
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
print("Updated anh.html successfully.")
