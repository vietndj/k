import os
import glob
from PIL import Image
import json
import subprocess

temp_dir = "/Users/vietmac/Documents/CODE/k/assets/temp_covers"
covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
manifest_file = "/Users/vietmac/Documents/CODE/k/generate_manifest.py"
queue_file = "/Users/vietmac/Documents/CODE/k/queue.json"

insertion = ""
processed_files = []

for filepath in glob.glob(os.path.join(temp_dir, "*.jpg")):
    filename = os.path.basename(filepath)
    html_name = filename[:-4] # remove .jpg
    webp_name = f"poster_batch_{html_name.replace('.html', '')}.webp"
    webp_path = os.path.join(covers_dir, webp_name)
    
    # Convert to webp
    img = Image.open(filepath)
    img.save(webp_path, "webp", quality=80)
    
    insertion += f'        "{html_name}": "https://media.fedu.vn/k_covers/{webp_name}",\n'
    processed_files.append(html_name)
    os.remove(filepath) # dọn dẹp temp

# Update generate_manifest.py
with open(manifest_file, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('cover_mapping = {', f'cover_mapping = {{\n{insertion}')

with open(manifest_file, "w", encoding="utf-8") as f:
    f.write(content)

# Update queue
with open(queue_file, "r", encoding="utf-8") as f:
    queue = json.load(f)

new_queue = [q for q in queue if q["filename"] not in [pf + ".html" for pf in processed_files]]

with open(queue_file, "w", encoding="utf-8") as f:
    json.dump(new_queue, f, ensure_ascii=False, indent=2)

print(f"Processed {len(processed_files)} covers. Remaining in queue: {len(new_queue)}")
