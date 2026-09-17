import json

with open('/Users/vietmac/Documents/CODE/k/remaining_poster_tasks.json', 'r') as f:
    tasks = json.load(f)

filtered = [t for t in tasks if 1 <= t.get("index", 0) <= 81]

for i in range(0, len(filtered), 5):
    batch = filtered[i:i+5]
    print(f"BATCH {i//5 + 1}")
    for t in batch:
        print(f"INDEX: {t['index']}")
        print(f"HTML: {t['target_html']}")
        print(f"PROMPT: {t['prompt']}")
        print("---")
