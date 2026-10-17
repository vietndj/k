import json
import re

with open("duplicate_report.json", "r") as f: faulty_data = json.load(f)
faulty_htmls = set([item["html"] for item in faulty_data])

with open("generate_manifest.py", "r") as f: content = f.read()
mapping_block = re.search(r'cover_mapping\s*=\s*\{([\s\S]*?)\}', content)
mapping_text = mapping_block.group(1)
pattern = re.compile(r'"([^"]+\.html)"\s*:\s*"([^"]+)"')
current_covers = dict(pattern.findall(mapping_text))

for html in faulty_htmls:
    if html in current_covers:
        del current_covers[html]

new_mapping_text = ",\n".join([f'        "{k}": "{v}"' for k, v in current_covers.items()])
new_mapping_text += ",\n"
new_content = content[:mapping_block.start(1)] + "\n" + new_mapping_text + "    " + content[mapping_block.end(1):]

with open("generate_manifest.py", "w") as f:
    f.write(new_content)

print(f"Removed {len(faulty_htmls)} faulty mappings from manifest.")
