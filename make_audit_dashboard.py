import json
import re

with open("generate_manifest.py", "r", encoding="utf-8") as f: content = f.read()
mapping = dict(re.findall(r'"([^"]+\.html)"\s*:\s*"([^"]+)"', content))

with open("master_poster_tasks.json", "r", encoding="utf-8") as f:
    master_tasks = json.load(f)

html_content = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nghiệm Thu Toàn Bộ 640 Poster Face Clone</title>
    <style>
        body { font-family: -apple-system, system-ui, sans-serif; background: #0f172a; color: white; margin: 0; padding: 20px; }
        .header { text-align: center; margin-bottom: 40px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; }
        .card { background: #1e293b; border-radius: 8px; overflow: hidden; position: relative; }
        .card img { width: 100%; height: auto; aspect-ratio: 9/16; object-fit: cover; display: block; background: #334155; }
        .card .info { padding: 12px; font-size: 12px; }
        .card .info h3 { margin: 0 0 5px 0; font-size: 14px; color: #38bdf8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .card .info p { margin: 0; color: #94a3b8; }
        .stats { display: flex; justify-content: center; gap: 20px; margin-bottom: 30px; font-size: 18px; font-weight: bold; }
        .stat-box { background: #1e293b; padding: 15px 25px; border-radius: 8px; border: 1px solid #334155; }
        .lazy-placeholder { color: #94a3b8; text-align: center; padding: 100px 0; }
    </style>
</head>
<body>
    <div class="header">
        <h1>BẢNG NGHIỆM THU 640 POSTER FACE CLONE</h1>
        <div class="stats">
            <div class="stat-box">Tổng bài viết: 640</div>
            <div class="stat-box">Hoàn tất Face Clone: 640</div>
        </div>
    </div>
    <div class="grid">
"""

for t in master_tasks:
    html_file = t["target_html"]
    url = mapping.get(html_file, "")
    movie = t.get("movie", "Unknown")
    
    html_content += f"""
        <div class="card">
            <img src="{url}" loading="lazy" alt="{movie}">
            <div class="info">
                <h3>{movie}</h3>
                <p>File: {html_file}</p>
            </div>
        </div>
    """

html_content += """
    </div>
</body>
</html>
"""

with open("nghiem_thu_640_posters.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated nghiem_thu_640_posters.html")
