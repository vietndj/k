import json
import re

with open("generate_manifest.py", "r", encoding="utf-8") as f: content = f.read()
mapping = dict(re.findall(r'"([^"]+\.html)"\s*:\s*"([^"]+)"', content))

with open("master_poster_tasks.json", "r", encoding="utf-8") as f:
    master_tasks = json.load(f)

remaining = []
for t in master_tasks:
    html = t["target_html"]
    url = mapping.get(html, "")
    if not (url.startswith("./assets/covers/") or url.startswith("assets/covers/")):
        remaining.append(t)

for i, t in enumerate(remaining):
    t["index"] = i + 1

with open("remaining_poster_tasks.json", "w", encoding="utf-8") as f:
    json.dump(remaining, f, indent=2, ensure_ascii=False)

print(f"Total master tasks: {len(master_tasks)}")
print(f"Remaining tasks to process: {len(remaining)}")
