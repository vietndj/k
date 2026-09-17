import json
import re
import os
import datetime

cutoff = datetime.datetime.strptime("2026-09-17 14:00:00", "%Y-%m-%d %H:%M:%S").timestamp()

with open("generate_manifest.py", "r") as f: content = f.read()
mapping_block = re.search(r'cover_mapping\s*=\s*\{([\s\S]*?)\}', content)
mapping_text = mapping_block.group(1)
pattern = re.compile(r'"([^"]+\.html)"\s*:\s*"([^"]+)"')
current_covers = dict(pattern.findall(mapping_text))

faulty_count = 0
good_count = 0

for html, url in list(current_covers.items()):
    if url.startswith("./assets/covers/") or url.startswith("assets/covers/"):
        local_path = url.replace("./", "")
        if os.path.exists(local_path):
            mtime = os.path.getmtime(local_path)
            if mtime < cutoff:
                del current_covers[html]
                faulty_count += 1
            else:
                good_count += 1
        else:
            # path does not exist
            pass

print(f"Removed {faulty_count} faulty mappings.")
print(f"Kept {good_count} good mappings.")

new_mapping_text = ",\n".join([f'        "{k}": "{v}"' for k, v in current_covers.items()])
new_mapping_text += ",\n"
new_content = content[:mapping_block.start(1)] + "\n" + new_mapping_text + "    " + content[mapping_block.end(1):]
with open("generate_manifest.py", "w") as f:
    f.write(new_content)
