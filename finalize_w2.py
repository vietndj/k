import os
import json
import shutil
import glob

# Paths
brain_dir = "/Users/vietmac/.gemini/antigravity/brain"
dest_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
tasks_file = "/Users/vietmac/Documents/CODE/k/scratch_tasks_w2.json"
mapping_file = "/Users/vietmac/Documents/CODE/k/temp_mapping_w2.json"

os.makedirs(dest_dir, exist_ok=True)

# Find all generated images
found_images = glob.glob(f"{brain_dir}/*/poster_*.jpg")

# Collect mapping
with open(tasks_file, "r") as f:
    tasks = json.load(f)

task_map = {t["index"]: t["target_html"] for t in tasks}
mapping = {}

count = 0
for img_path in found_images:
    basename = os.path.basename(img_path)
    # poster_123_456789.jpg
    parts = basename.split('_')
    if len(parts) >= 2 and parts[1].isdigit():
        index = int(parts[1])
        if index in task_map:
            # Copy file
            new_name = f"poster_{index}.jpg"
            dest_path = os.path.join(dest_dir, new_name)
            shutil.copy(img_path, dest_path)
            # Update mapping
            mapping[task_map[index]] = new_name
            count += 1

with open(mapping_file, "w") as f:
    json.dump(mapping, f, indent=2)

print(f"Collected and mapped {count} images.")
