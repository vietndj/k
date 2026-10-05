import json
from collections import Counter

with open("all_unique_posters.json", "r") as f:
    items = json.load(f)

# check duplicate paths
paths = [item["path"] for item in items]
path_counts = Counter(paths)

duplicate_paths = {k:v for k,v in path_counts.items() if v > 1}
print(f"Duplicate paths found: {len(duplicate_paths)}")

if duplicate_paths:
    for k, v in duplicate_paths.items():
        print(f"{k}: {v} times")
