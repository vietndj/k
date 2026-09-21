import json

with open("fix_progress.json", "r") as f:
    progress = json.load(f)

# Get the last 50 items (or all if less than 50)
last_50 = progress[-50:]

html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nghiệm Thu 50 Ảnh Vừa Xong</title>
    <style>
        body { font-family: sans-serif; background: #000; color: #fff; margin: 0; padding: 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px; }
        img { width: 100%; height: auto; border-radius: 8px; }
        .card { background: #111; padding: 10px; border-radius: 8px; text-align: center; }
        .filename { font-size: 0.8em; margin-top: 10px; word-break: break-all; color: #aaa; }
    </style>
</head>
<body>
    <h1>Nghiệm Thu 50 Ảnh Vừa Xong</h1>
    <div class="grid">
"""

for url in last_50:
    # URL format is like: k/assets/images_gen_fixes/filename.jpg
    # Make it relative so it works on GitHub pages
    filename = url.split("/")[-1]
    rel_url = f"assets/images_gen_fixes/{filename}"
    html_content += f'''
        <div class="card">
            <img src="{rel_url}" alt="{filename}" loading="lazy">
            <div class="filename">{filename}</div>
        </div>'''

html_content += """
    </div>
</body>
</html>
"""

with open("nghiem_thu.html", "w") as f:
    f.write(html_content)

print("Created nghiem_thu.html")
