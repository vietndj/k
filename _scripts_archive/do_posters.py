import json
import os
import glob
import shutil
import re

batch_file = '/Users/vietmac/Documents/CODE/k/batch_tasks.json'
brain_dir = '/Users/vietmac/.gemini/antigravity/brain/33eb09a0-4f7c-4344-8b73-5a23fec30eaa'
covers_dir = '/Users/vietmac/Documents/CODE/k/assets/covers'

os.makedirs(covers_dir, exist_ok=True)

with open(batch_file) as f:
    data = json.load(f)

mapping = {}

for item in data:
    target_html = item['target_html']
    base_name = re.sub(r'[^a-z0-9]+', '_', target_html.replace('.html', '').lower())
    # find newest matching image
    search_pattern = os.path.join(brain_dir, f"{base_name}_*.jpg")
    matches = glob.glob(search_pattern)
    if not matches:
        # Fallback if the name is truncated or different
        search_pattern = os.path.join(brain_dir, f"*{base_name[:30]}*.jpg")
        matches = glob.glob(search_pattern)
    
    if matches:
        # get latest
        latest_file = max(matches, key=os.path.getctime)
        dest_filename = f"{target_html.replace('.html', '')}.jpg"
        dest_path = os.path.join(covers_dir, dest_filename)
        shutil.copy(latest_file, dest_path)
        print(f"Copied {latest_file} -> {dest_path}")
        mapping[target_html] = f"assets/covers/{dest_filename}"
    else:
        print(f"MISSING image for {base_name}")

with open('/Users/vietmac/Documents/CODE/k/temp_mapping_w3.json', 'w') as f:
    json.dump(mapping, f, indent=2)

print("Mapping created.")
