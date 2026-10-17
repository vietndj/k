import json
import os

with open("all_unique_posters.json", "r") as f:
    items = json.load(f)

missing = []
for item in items:
    path = item["path"]
    if not path.startswith("http") and not path.startswith("assets") and not path.startswith("/"):
        path = "assets/covers/" + path
        
    if not os.path.exists(path):
        missing.append(path)

print(f"Total missing: {len(missing)}")
for m in missing[:20]:
    print(m)
