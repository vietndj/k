import json
import os
import glob
import subprocess

ARTIFACTS_DIR = "/Users/vietmac/.gemini/antigravity/brain/9f14cea5-45f3-4283-96c8-d2dc54be819c"
ASSETS_COVERS_DIR = "assets/covers"

with open("batches.json") as f:
    batches = json.load(f)

batch_index = 8
if batch_index >= len(batches):
    print("Batch index out of range")
    exit(1)

batch = batches[batch_index]

first_item_index = batch[0]['index']
mapping = {}
indices = []

os.makedirs(ASSETS_COVERS_DIR, exist_ok=True)

for task in batch:
    idx = task['index']
    target_html = task['target_html']
    target_name = target_html.replace(".html", ".jpg")
    target_path = os.path.join(ASSETS_COVERS_DIR, target_name)
    
    # find image
    pattern = f"poster_8_{idx}_*.jpg"
    matches = glob.glob(os.path.join(ARTIFACTS_DIR, pattern))
    if matches:
        os.rename(matches[0], target_path)
        mapping[target_html] = target_path
        indices.append(str(idx))

mapping_file = f"temp_mapping_{first_item_index}.json"
with open(mapping_file, "w") as f:
    json.dump(mapping, f, indent=2)

print(f"Created mapping: {mapping_file}")

# run python3 update_covers.py temp_mapping_...
subprocess.run(["python3", "update_covers.py", mapping_file], check=True)

# git commands
subprocess.run(["rm", "-f", ".git/index.lock"])
subprocess.run(["git", "add", "."])
indices_str = ",".join(indices)
subprocess.run(["git", "commit", "-m", f"feat: posters {indices_str}"], check=False)

# push
while True:
    res = subprocess.run(["git", "push"])
    if res.returncode == 0:
        break
    subprocess.run(["git", "pull", "--rebase"])
    import time
    time.sleep(2)
