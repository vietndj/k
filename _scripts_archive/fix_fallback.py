import json
import re
import random

manifest_file = "/Users/vietmac/Documents/CODE/k/generate_manifest.py"
unique_file = "/Users/vietmac/Documents/CODE/k/all_unique_posters.json"

# Read generate_manifest.py
with open(manifest_file, "r", encoding="utf-8") as f:
    code = f.read()

# Extract cover_mapping values to avoid using them as fallback
used_covers = set()
match = re.search(r'cover_mapping\s*=\s*\{([^}]+)\}', code)
if match:
    mapping_str = match.group(1)
    for line in mapping_str.split('\n'):
        if ':' in line:
            parts = line.split(':')
            val = parts[1].strip().strip(',').strip('"').strip("'")
            used_covers.add(val)

# Read unique posters
with open(unique_file, "r", encoding="utf-8") as f:
    data = json.load(f)

available_covers = []
for item in data:
    path = item.get("path")
    if path and path not in used_covers:
        available_covers.append(path)

# Pick 200 random covers
random.seed(42) # fixed seed
if len(available_covers) > 200:
    new_fallback = random.sample(available_covers, 200)
else:
    new_fallback = available_covers

# Replace the fallback_images list in generate_manifest.py
# Using regex to find the list definition
fallback_list_str = "fallback_images = [\n" + ",\n".join([f'                "{url}"' for url in new_fallback]) + "\n            ]"

code = re.sub(r'fallback_images\s*=\s*\[[\s\S]*?\]', fallback_list_str, code)

with open(manifest_file, "w", encoding="utf-8") as f:
    f.write(code)

print(f"Updated generate_manifest.py with {len(new_fallback)} fallback images.")
