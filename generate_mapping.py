import json
import os
import glob

with open('movie_posters_tasks.json', 'r') as f:
    tasks = json.load(f)

mapping = {}
for task in tasks:
    if task['index'] >= 26 and task['index'] <= 55:
        slug = task['slug']
        # find file in /tmp/k_covers/
        files = glob.glob(f"/tmp/k_covers/poster_{slug}_*.jpg")
        if files:
            filename = os.path.basename(files[0])
            mapping[task['target_html']] = f"https://khoai.fedu.vn/k_covers/{filename}"

with open('new_30_covers.json', 'w') as f:
    json.dump(mapping, f, indent=2)
