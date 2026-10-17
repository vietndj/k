import os
import re
import subprocess
from PIL import Image

# 1. Convert images
imgs = [
    {
        "src": "/Users/vietmac/.gemini/antigravity/brain/5305392f-ab19-4e41-9f63-54f3b898f080/dustin_poirier_fall_1791730550674.jpg",
        "dst_name": "poster_dustin_fall.webp",
        "html_file": "dustin-poirier-khoang-trong-sau-dinh-cao-podcast.html"
    },
    {
        "src": "/Users/vietmac/.gemini/antigravity/brain/5305392f-ab19-4e41-9f63-54f3b898f080/neil_degrasse_cosmos_1791730563479.jpg",
        "dst_name": "poster_neil_cosmos.webp",
        "html_file": "neil-degrasse-tyson-giai-ma-vu-tru-podcast.html"
    }
]

target_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
insertion = ""

for img_info in imgs:
    dst_path = os.path.join(target_dir, img_info["dst_name"])
    if os.path.exists(img_info["src"]):
        img = Image.open(img_info["src"])
        img.save(dst_path, "webp", quality=80)
        print(f"Saved {dst_path}")
        insertion += f'        "{img_info["html_file"]}": "https://media.fedu.vn/k_covers/{img_info["dst_name"]}",\n'
    else:
        print(f"File not found: {img_info['src']}")

# 2. Update generate_manifest.py
manifest_file = "/Users/vietmac/Documents/CODE/k/generate_manifest.py"
with open(manifest_file, "r", encoding="utf-8") as f:
    content = f.read()

# Insert into cover_mapping
content = content.replace('cover_mapping = {', f'cover_mapping = {{\n{insertion}')

with open(manifest_file, "w", encoding="utf-8") as f:
    f.write(content)

# 3. Generate and push
subprocess.run(["python3", "generate_manifest.py"])
subprocess.run(["git", "add", "assets/covers/poster_dustin_fall.webp", "assets/covers/poster_neil_cosmos.webp", "generate_manifest.py", "posts-manifest.json"])
subprocess.run(["git", "commit", "-m", "feat(covers): Update unique 1:1 posters for Dustin and Neil articles"])
subprocess.run(["git", "push"])

print("All done!")
