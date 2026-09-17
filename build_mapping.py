import json
import os
import glob
import re

with open("remaining_poster_tasks.json", "r") as f:
    tasks = json.load(f)

index_to_html = {t["index"]: t["target_html"] for t in tasks}

mapping = {}
for filepath in glob.glob("assets/covers/poster_*.jpg"):
    filename = os.path.basename(filepath)
    match = re.match(r'poster_(\d+)', filename)
    if match:
        idx = int(match.group(1))
        if idx in index_to_html:
            mapping[index_to_html[idx]] = filename

with open("temp_mapping_w3.json", "w") as f:
    json.dump(mapping, f, indent=4)

print(f"Created mapping with {len(mapping)} items")
