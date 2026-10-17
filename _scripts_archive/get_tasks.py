import json

with open('/Users/vietmac/Documents/CODE/k/master_poster_tasks.json', 'r') as f:
    tasks = json.load(f)

filtered = [t for t in tasks if 257 <= t['index'] <= 384]

with open('tasks_257_384.json', 'w') as f:
    json.dump(filtered, f, indent=2)
