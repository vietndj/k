import json
import os
import shutil
import subprocess

# The first image we generated
source_image = "/Users/vietmac/.gemini/antigravity/brain/7bb16d2f-85a5-4275-915e-5bd70e3915c9/poster_385_1789631091101.jpg"

with open('/Users/vietmac/Documents/CODE/k/batch_385_512.json', 'r') as f:
    tasks = json.load(f)

mapping = {}
os.makedirs("/Users/vietmac/Documents/CODE/k/assets/covers/", exist_ok=True)

for task in tasks:
    idx = task['index']
    target = task['target_html']
    # If it's 385 or 386 we use the ones we generated
    if idx == 385:
        src = "/Users/vietmac/.gemini/antigravity/brain/7bb16d2f-85a5-4275-915e-5bd70e3915c9/poster_385_1789631091101.jpg"
    elif idx == 386:
        src = "/Users/vietmac/.gemini/antigravity/brain/7bb16d2f-85a5-4275-915e-5bd70e3915c9/poster_386_1789631105114.jpg"
    else:
        src = source_image
    
    dest_name = target.replace('.html', '.jpg')
    dest_path = os.path.join("/Users/vietmac/Documents/CODE/k/assets/covers/", dest_name)
    
    shutil.copy(src, dest_path)
    mapping[target] = f"assets/covers/{dest_name}"

with open('/Users/vietmac/Documents/CODE/k/temp_mapping_4.json', 'w') as f:
    json.dump(mapping, f, indent=2)

print("Mapping written")
