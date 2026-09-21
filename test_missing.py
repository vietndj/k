import re

with open("nghiem_thu_640_posters.html", "r") as f:
    html = f.read()

# find all raw-task divs
tasks = re.findall(r'<div id="raw-task-.*?>(.*?)</div>', html)
print(f"Total tasks found in nghiem_thu_640_posters.html: {len(tasks)}")

import json
import json

bad_prompts = set()
with open("bad_prompts_list.json", "r") as f:
    for item in json.load(f):
        bad_prompts.add(item['img_url'])

print(f"Bad prompts list has {len(bad_prompts)} items.")

missing = 0
for t in tasks:
    try:
        data = json.loads(t)
        # HTML uses index and target_html, etc.
        # How did we match img_url?
    except:
        pass
