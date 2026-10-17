import os
import subprocess
from PIL import Image

# Map posts to banner names
mappings = {
    "logic04.html": "banner_lego",
    "logic05.html": "banner_pokemon",
    "logic06.html": "banner_terraria",
    "logic07.html": "banner_scratch"
}

source_dir = "/Users/vietmac/.gemini/antigravity/brain/991be103-aeda-4b6b-b714-0dd38da21d20"
target_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"

# Convert and copy
for html_file, banner_name in mappings.items():
    src = os.path.join(source_dir, f"{banner_name}.jpg")
    dst = os.path.join(target_dir, f"{banner_name}.webp")
    if os.path.exists(src):
        try:
            img = Image.open(src)
            img.save(dst, "webp", quality=80)
            print(f"Saved {dst}")
        except Exception as e:
            print(f"Error converting {src}: {e}")

# Update generate_manifest.py
manifest_script = "/Users/vietmac/Documents/CODE/k/generate_manifest.py"
with open(manifest_script, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert cover mappings
insertion = ""
for html_file, banner_name in mappings.items():
    insertion += f'        "{html_file}": "assets/covers/{banner_name}.webp",\n'

content = content.replace('cover_mapping = {\n', f'cover_mapping = {{\n{insertion}')

with open(manifest_script, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated generate_manifest.py")

# Touch the HTML files to bump their modified date
for html_file in mappings.keys():
    filepath = os.path.join("/Users/vietmac/Documents/CODE/k", html_file)
    if os.path.exists(filepath):
        os.utime(filepath, None)

# Run generate_manifest.py
subprocess.run(["python3", "generate_manifest.py"], cwd="/Users/vietmac/Documents/CODE/k")
print("Ran generate_manifest.py")
