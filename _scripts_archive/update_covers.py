import json
import sys
import re
import fcntl

if len(sys.argv) < 2:
    print("Usage: python3 update_covers.py <mapping.json>")
    sys.exit(1)

mapping_file = sys.argv[1]
with open(mapping_file, "r") as f:
    new_mapping = json.load(f)

manifest_file = "generate_manifest.py"

with open(manifest_file, "r+") as f:
    fcntl.flock(f, fcntl.LOCK_EX)
    content = f.read()
    
    mapping_block = re.search(r'cover_mapping\s*=\s*\{([\s\S]*?)\}', content)
    if not mapping_block:
        print("Could not find cover_mapping")
        fcntl.flock(f, fcntl.LOCK_UN)
        sys.exit(1)
        
    mapping_text = mapping_block.group(1)
    pattern = re.compile(r'"([^"]+\.html)"\s*:\s*"([^"]+)"')
    current_covers = dict(pattern.findall(mapping_text))
    
    current_covers.update(new_mapping)
    
    new_mapping_text = ",\n".join([f'        "{k}": "{v}"' for k, v in current_covers.items()])
    if new_mapping_text:
        new_mapping_text += ",\n"
        
    new_content = content[:mapping_block.start(1)] + "\n" + new_mapping_text + "    " + content[mapping_block.end(1):]
    
    f.seek(0)
    f.write(new_content)
    f.truncate()
    fcntl.flock(f, fcntl.LOCK_UN)

print(f"Successfully added {len(new_mapping)} covers to generate_manifest.py")
