import json

manifest_file = "generate_manifest.py"
mapping_file = "new_30_covers.json"

with open(mapping_file, 'r', encoding='utf-8') as f:
    new_covers = json.load(f)

with open(manifest_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

end_idx = -1
for i, line in enumerate(lines):
    if line.strip() == "}":
        end_idx = i
        break

if end_idx != -1:
    # Add comma to the line before if missing
    if not lines[end_idx-1].strip().endswith(","):
        lines[end_idx-1] = lines[end_idx-1].rstrip('\n') + ",\n"

    additions = []
    for html_file, r2_url in new_covers.items():
        additions.append(f'        "{html_file}": "{r2_url}",\n')
    
    new_lines = lines[:end_idx] + additions + lines[end_idx:]
    with open(manifest_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

