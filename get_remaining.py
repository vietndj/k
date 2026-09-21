import json
import os
import hashlib
from collections import defaultdict

with open("all_unique_posters.json", "r") as f:
    items = json.load(f)

# Group items by their file hash
hash_to_items = defaultdict(list)
missing_items = []

for item in items:
    path = item["path"]
    if not path.startswith("http") and not path.startswith("assets") and not path.startswith("/"):
        path = "assets/covers/" + path
        
    if os.path.exists(path):
        with open(path, "rb") as file:
            file_hash = hashlib.md5(file.read()).hexdigest()
            hash_to_items[file_hash].append(item)
    else:
        missing_items.append(item)

# Items to regenerate:
# 1. Missing items (the 11 missing files)
# 2. Items that share a hash with at least one other item (because they are placeholders)
to_regenerate = list(missing_items)
for h, group in hash_to_items.items():
    if len(group) > 1:
        to_regenerate.extend(group)

print(f"Total missing: {len(missing_items)}")
print(f"Total duplicate-hash items: {len(to_regenerate) - len(missing_items)}")
print(f"Total to regenerate: {len(to_regenerate)}")

with open("to_regenerate.json", "w") as f:
    json.dump(to_regenerate, f, ensure_ascii=False, indent=2)

