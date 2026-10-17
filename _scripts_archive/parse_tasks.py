import json

with open('/Users/vietmac/Documents/CODE/k/remaining_poster_tasks.json', 'r') as f:
    data = json.load(f)

for item in data:
    idx = item.get('index')
    if 21 <= idx <= 25:
        print(f"INDEX: {idx}")
        print(f"PROMPT: {item['prompt']}")
        print(f"TARGET_HTML: {item['target_html']}")
        print("---")
