import re
import os

with open("generate_manifest.py", "r") as f: content = f.read()
mapping_block = re.search(r'cover_mapping\s*=\s*\{([\s\S]*?)\}', content)
pattern = re.compile(r'"([^"]+\.html)"\s*:\s*"([^"]+)"')
current_covers = dict(pattern.findall(mapping_block.group(1)))

missing_files = []
for html, url in current_covers.items():
    if url.startswith("./assets/covers/"):
        local_path = url.replace("./", "")
        if not os.path.exists(local_path):
            missing_files.append(local_path)

print(f"Missing files: {len(missing_files)}")
if missing_files:
    print(missing_files[:10])
