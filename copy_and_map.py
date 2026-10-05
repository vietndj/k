import json
import os
import glob
import shutil

tasks = json.load(open('/tmp/tasks_1_27.json'))
brain_dir = "/Users/vietmac/.gemini/antigravity/brain/e4392290-c4c3-44a0-9b3e-f12db2673386"
covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"

os.makedirs(covers_dir, exist_ok=True)
mapping = {}

for task in tasks:
    idx = task['index']
    target_html = task['target_html']
    
    # find image
    pattern = os.path.join(brain_dir, f"poster_{idx}_*.jpg")
    files = glob.glob(pattern)
    if files:
        src = files[0]
        # using the target html name as prefix for the image to avoid conflict? Or just poster_X.jpg
        dst_name = f"poster_w1_{idx}.jpg"
        dst = os.path.join(covers_dir, dst_name)
        shutil.copy2(src, dst)
        mapping[target_html] = f"assets/covers/{dst_name}"

with open("/Users/vietmac/Documents/CODE/k/temp_mapping_w1.json", "w") as f:
    json.dump(mapping, f, indent=4)

