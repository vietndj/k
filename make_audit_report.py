import re
import os

manifest_file = "generate_manifest.py"
with open(manifest_file, "r", encoding="utf-8") as f:
    content = f.read()

# Extract the cover_mapping dictionary contents
mapping_block = re.search(r'cover_mapping\s*=\s*\{([\s\S]*?)\}', content)
if not mapping_block:
    print("Could not find cover_mapping in generate_manifest.py")
    exit(1)

mapping_text = mapping_block.group(1)
# Find all lines like "filename": "url"
pattern = re.compile(r'"([^"]+\.html)"\s*:\s*"([^"]+)"')
matches = pattern.findall(mapping_text)

html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Poster Audit Dashboard</title>
    <style>
        body {
            font-family: system-ui, -apple-system, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }
        .summary {
            text-align: center;
            font-size: 1.2rem;
            margin-bottom: 40px;
            color: #94a3b8;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }
        .card {
            background: #1e293b;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #334155;
            display: flex;
            flex-direction: column;
        }
        .card img {
            width: 100%;
            height: auto;
            aspect-ratio: 9/16;
            object-fit: cover;
            display: block;
        }
        .card-body {
            padding: 12px;
            font-size: 0.85rem;
        }
        .filename {
            font-weight: 600;
            margin-bottom: 8px;
            word-break: break-all;
            color: #e2e8f0;
        }
        .url {
            color: #64748b;
            word-break: break-all;
            font-size: 0.75rem;
        }
        .badge {
            display: inline-block;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.7rem;
            font-weight: bold;
            margin-bottom: 8px;
        }
        .badge.local { background: #3b82f6; color: #fff; }
        .badge.r2 { background: #10b981; color: #fff; }
    </style>
</head>
<body>
    <h1>🎬 Poster Audit Dashboard</h1>
    <div class="summary">Tổng số bài viết có Poster: <strong>{TOTAL_COUNT}</strong></div>
    <div class="grid">
"""

cards = ""
for filename, url in matches:
    badge_class = "local" if url.startswith("./") or url.startswith("/") else "r2"
    badge_text = "LOCAL/NEW" if badge_class == "local" else "CLOUDFLARE R2"
    
    cards += f"""
        <div class="card">
            <img src="{url}" loading="lazy" alt="{filename}">
            <div class="card-body">
                <span class="badge {badge_class}">{badge_text}</span>
                <div class="filename">{filename}</div>
                <div class="url">{url}</div>
            </div>
        </div>
    """

html_content = html_content.replace("{TOTAL_COUNT}", str(len(matches))) + cards + """
    </div>
</body>
</html>
"""

with open("poster_audit_dashboard.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated poster_audit_dashboard.html with {len(matches)} posters.")
