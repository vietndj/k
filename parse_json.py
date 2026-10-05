import json

with open('/Users/vietmac/Documents/CODE/k/remaining_poster_tasks.json', 'r') as f:
    data = json.load(f)

for item in data:
    if 28 <= item['index'] <= 54:
        print(f"Index: {item['index']}")
        print(f"Target: {item['target_html']}")
        print(f"Prompt: {item['prompt']}")
        print("---")
