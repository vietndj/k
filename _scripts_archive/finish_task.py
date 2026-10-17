import json
import os
import glob
import subprocess
import shutil

brain_dir = "/Users/vietmac/.gemini/antigravity/brain/13638035-3214-48ad-a1c0-fd09dff51e7c"
covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers/"
os.makedirs(covers_dir, exist_ok=True)

# Move remaining
for f in glob.glob(f"{brain_dir}/*_poster_*.jpg"):
    shutil.move(f, os.path.join(covers_dir, os.path.basename(f)))

# Read tasks to get target html
tasks_path = "/Users/vietmac/Documents/CODE/k/remaining_poster_tasks.json"
with open(tasks_path, 'r') as f:
    tasks = json.load(f)

# Find generated covers
mapping = {}
generated_covers = glob.glob(f"{covers_dir}/*_poster_*.jpg")

for cover in generated_covers:
    filename = os.path.basename(cover)
    # Extract index, typically they look like "kieu_poster_28_1789...jpg" or similar
    parts = filename.split('_')
    # Try to find the index number from the parts
    idx_str = None
    for part in parts:
        if part.isdigit() and 28 <= int(part) <= 54:
            idx_str = part
            break
            
    if idx_str:
        idx = int(idx_str)
        # Find target HTML
        task = next((t for t in tasks if t['index'] == idx), None)
        if task:
            target = task['target_html']
            # Remove covers_dir prefix for mapping if update_covers.py expects relative path
            # Actually just put filename or "assets/covers/..."
            # Usually update_covers.py expects dict { target_html: cover_path }
            mapping[target] = f"assets/covers/{filename}"

mapping_file = "/Users/vietmac/Documents/CODE/k/temp_mapping_w2.json"
with open(mapping_file, 'w') as f:
    json.dump(mapping, f, indent=2)

print(f"Created mapping with {len(mapping)} items.")
