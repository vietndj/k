import json
with open('/Users/vietmac/Documents/CODE/k/remaining_poster_tasks.json', 'r') as f:
    data = json.load(f)

for item in data:
    if 189 <= item.get('index', 0) <= 193:
        print(f"INDEX: {item['index']}")
        print(f"HTML: {item['target_html']}")
        print(f"PROMPT: {item['prompt']}")
        print("---")
