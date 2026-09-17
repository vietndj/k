import json
import os
import shutil
import glob

with open('batches.json', 'r') as f:
    batches = json.load(f)

batch = batches[11]
mapping = {}
first_index = batch[0]['index']

artifact_dir = "/Users/vietmac/.gemini/antigravity/brain/7c9a2d58-eb39-4c85-85f1-3c1d34037341"

for task in batch:
    idx = task['index']
    target_html = task['target_html']
    target_name = target_html.replace('.html', '')
    
    # find image
    pattern = os.path.join(artifact_dir, f"poster_{idx}_*.jpg")
    files = glob.glob(pattern)
    if not files:
        print(f"Error: no file found for index {idx}")
        continue
        
    src_file = files[0]
    dst_file = f"assets/covers/{target_name}.jpg"
    
    shutil.copy(src_file, dst_file)
    print(f"Copied {src_file} to {dst_file}")
    
    mapping[target_html] = dst_file

mapping_file = f"temp_mapping_{first_index}.json"
with open(mapping_file, 'w') as f:
    json.dump(mapping, f, indent=2)

print(f"Mapping saved to {mapping_file}")
