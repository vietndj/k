import json

with open('/Users/vietmac/Documents/CODE/k/movie_posters_tasks_285.json', 'r') as f:
    data = json.load(f)

tasks = [t for t in data if 470 <= t["index"] <= 526]
print(json.dumps(tasks, indent=2))
