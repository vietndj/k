import json
import os

with open("new_anime_prompts.json", "r") as f:
    prompts_data = json.load(f)

html = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nghiệm Thu Anime</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #f8fafc; padding: 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; }
        .card { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
        .img-container img { width: 100%; height: auto; display: block; }
        .card-body { padding: 20px; }
        .prompt-text { font-size: 0.875rem; color: #475569; background: #f1f5f9; padding: 12px; border-radius: 8px; margin-bottom: 16px; word-break: break-word; }
    </style>
</head>
<body>
    <h1>Nghiệm Thu Ảnh Mới (Anime/Manga)</h1>
    <p>Tất cả ảnh đã được tạo với chuỗi Face DNA chuẩn. Tổng: """ + str(len(prompts_data)) + """ ảnh.</p>
    <div class="grid">
"""

for item in prompts_data:
    filename = item["filename"]
    # Check if file exists in the fixes dir
    path = f"assets/images_gen_fixes/{filename}"
    
    html += f"""
        <div class="card">
            <div class="img-container">
                <img src="{path}" loading="lazy" alt="Generated Image">
            </div>
            <div class="card-body">
                <div class="prompt-text">{item['prompt']}</div>
            </div>
        </div>
    """

html += """
    </div>
</body>
</html>
"""

with open("anh_nghiem_thu_moi.html", "w") as f:
    f.write(html)
print("Created anh_nghiem_thu_moi.html")
