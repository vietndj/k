import re
import json

manifest_file = "/Users/vietmac/Documents/CODE/k/generate_manifest.py"
with open(manifest_file, "r", encoding="utf-8") as f:
    code = f.read()

used_covers = set()
match = re.search(r'cover_mapping\s*=\s*\{([^}]+)\}', code)
if match:
    mapping_str = match.group(1)
    for line in mapping_str.split('\n'):
        if ':' in line:
            parts = line.split(':')
            key = parts[0].strip().strip('"').strip("'")
            used_covers.add(key)

with open("/Users/vietmac/Documents/CODE/k/posts-manifest.json", "r", encoding="utf-8") as f:
    posts_data = json.load(f)

queue = []
for p in posts_data["posts"]:
    fname = p["filename"]
    if fname not in used_covers:
        queue.append({
            "filename": fname,
            "title": p["title"],
            "excerpt": p.get("excerpt", "")
        })

with open("/Users/vietmac/Documents/CODE/k/queue.json", "w", encoding="utf-8") as f:
    json.dump(queue, f, ensure_ascii=False, indent=2)

print(f"Total items in queue: {len(queue)}")
