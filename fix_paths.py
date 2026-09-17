import json
import re
import os

with open("generate_manifest.py", "r") as f: content = f.read()
mapping_block = re.search(r'cover_mapping\s*=\s*\{([\s\S]*?)\}', content)
mapping_text = mapping_block.group(1)
pattern = re.compile(r'"([^"]+\.html)"\s*:\s*"([^"]+)"')
current_covers = dict(pattern.findall(mapping_text))

fixed_count = 0
for html, url in list(current_covers.items()):
    if url.endswith(".jpg") and not url.startswith("http") and not "/" in url:
        current_covers[html] = "./assets/covers/" + url
        fixed_count += 1
    elif url.startswith("assets/covers/"):
        current_covers[html] = "./" + url
        fixed_count += 1

new_mapping_text = ",\n".join([f'        "{k}": "{v}"' for k, v in current_covers.items()])
new_mapping_text += ",\n"
new_content = content[:mapping_block.start(1)] + "\n" + new_mapping_text + "    " + content[mapping_block.end(1):]

with open("generate_manifest.py", "w") as f:
    f.write(new_content)

print(f"Fixed {fixed_count} paths.")
