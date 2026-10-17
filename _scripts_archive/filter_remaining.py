import json
import re

# Read manifest
with open("generate_manifest.py", "r", encoding="utf-8") as f: content = f.read()
mapping = dict(re.findall(r"\"([^\"]+\.html)\"\s*:\s*\"([^\"]+)\"", content))

# Read master tasks
with open("master_poster_tasks.json", "r", encoding="utf-8") as f:
    master_tasks = json.load(f)

remaining = []
completed_count = 0
for t in master_tasks:
    html = t["target_html"]
    url = mapping.get(html, "")
    # If the URL points to our newly generated local covers directory, it's done
    if url.startswith("./assets/covers/"):
        completed_count += 1
    else:
        remaining.append(t)

# Re-index remaining to make it easy to slice
for i, t in enumerate(remaining):
    t["index"] = i + 1

with open("remaining_poster_tasks.json", "w", encoding="utf-8") as f:
    json.dump(remaining, f, indent=2, ensure_ascii=False)

print(f"Total tasks: {len(master_tasks)}")
print(f"Completed (mapped to ./assets/covers/): {completed_count}")
print(f"Remaining tasks: {len(remaining)}")
