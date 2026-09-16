import json
import os
import sys

# Usage: python3 update_covers.py <mapping_json_file>
if len(sys.argv) < 2:
    print("Usage: python3 update_covers.py <mapping_json_file>")
    sys.exit(1)

mapping_file = sys.argv[1]
with open(mapping_file, 'r', encoding='utf-8') as f:
    new_covers = json.load(f)

manifest_py = "generate_manifest.py"
with open(manifest_py, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find where cover_mapping dictionary ends
end_idx = -1
for i, line in enumerate(lines):
    if "cover_mapping = {" in line:
        for j in range(i+1, len(lines)):
            if lines[j].strip() == "}":
                end_idx = j
                break
        break

if end_idx == -1:
    print("Could not find end of cover_mapping dict")
    sys.exit(1)

# Format additions
additions = ["\n        # 30 Movie Poster AI Covers\n"]
for html_file, r2_url in new_covers.items():
    additions.append(f'        "{html_file}": "{r2_url}",\n')

# Insert before the closing brace
new_lines = lines[:end_idx] + additions + lines[end_idx:]

with open(manifest_py, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Successfully added {len(new_covers)} covers to {manifest_py}")
