import json

with open('tasks_257_384.json', 'r') as f:
    tasks = json.load(f)

# The remaining tasks
remaining_tasks = [t for t in tasks if t['index'] == 259 or t['index'] >= 262]

batches = []
for i in range(0, len(remaining_tasks), 5):
    batches.append(remaining_tasks[i:i+5])

with open('batches.json', 'w') as f:
    json.dump(batches, f, indent=2)

print(f"Dumped {len(batches)} batches.")
