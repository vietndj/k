import json

with open("duplicate_report.json", "r") as f:
    dups = json.load(f)

with open("master_poster_tasks.json", "r") as f:
    master = json.load(f)

master_dict = {t["target_html"]: t for t in master}

tasks = []
for d in dups:
    html = d["html"]
    task = master_dict.get(html)
    if task:
        tasks.append({
            "html": html,
            "url": d["url"],
            "prompt": task.get("prompt", ""),
            "movie": task.get("movie", "")
        })

print(json.dumps(tasks, indent=2, ensure_ascii=False))
