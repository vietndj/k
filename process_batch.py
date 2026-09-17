import json
import os
import glob
import shutil

artifact_dir = "/Users/vietmac/.gemini/antigravity/brain/fdf62876-04e0-48a2-b3a1-29bec68637bb/"
covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers/"

with open('/Users/vietmac/Documents/CODE/k/movie_posters_tasks_355.json', 'r') as f:
    data = json.load(f)

batch = [item for item in data if 301 <= item['index'] <= 330]

mapping = {}

for item in batch:
    html_file = item['target_html']
    image_name = html_file.replace('.html', '')
    image_name_underscores = image_name.replace('-', '_')
    
    # find matching generated image
    pattern = os.path.join(artifact_dir, f"{image_name_underscores}_*.jpg")
    matches = glob.glob(pattern)
    
    if not matches:
        print(f"Warning: No generated image found for {image_name}")
        continue
    
    # get the latest
    latest_img = max(matches, key=os.path.getmtime)
    
    dest_path = os.path.join(covers_dir, f"{image_name}.jpg")
    shutil.copy2(latest_img, dest_path)
    
    mapping[html_file] = f"./assets/covers/{image_name}.jpg"

with open('/Users/vietmac/Documents/CODE/k/temp_mapping.json', 'w') as f:
    json.dump(mapping, f, indent=4)

print("Created temp_mapping.json")
