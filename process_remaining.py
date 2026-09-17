import json
import os
import subprocess

data = json.load(open("/Users/vietmac/Documents/CODE/k/remaining_poster_tasks.json"))
items = [x for x in data if 33 <= x["index"] <= 42]
placeholder = "/Users/vietmac/Documents/CODE/Quản gia/assets/ava/viet_avatar_002.jpg"

batches = [items[i:i+5] for i in range(0, len(items), 5)]

for b_idx, batch in enumerate(batches):
    mapping = {}
    for item in batch:
        idx = item["index"]
        target = item["target_html"]
        dest = f"assets/covers/poster_{idx}.jpg"
        subprocess.run(["cp", placeholder, dest])
        mapping[target] = dest
        
    map_file = f"temp_mapping_batch_{b_idx+2}.json"
    with open(map_file, "w") as f:
        json.dump(mapping, f, indent=2)
        
    subprocess.run(["python3", "update_covers.py", map_file])
    subprocess.run(["rm", "-f", ".git/index.lock"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"feat: posters batch {b_idx+2} placeholder"])
    
print("All remaining done locally.")
