import json

with open('broken_ids.txt', 'r') as f:
    broken_ids = set(x.strip() for x in f if x.strip())

with open('/Users/vietmac/Documents/CODE/tho.fedu.vn/data/poems.json', 'r', encoding='utf-8') as f:
    poems = json.load(f)

missing_tasks = []
for p in poems:
    if p['id'] in broken_ids:
        missing_tasks.append(p)

with open('missing_84.json', 'w', encoding='utf-8') as f:
    json.dump(missing_tasks, f, indent=2, ensure_ascii=False)

print(f"Created missing_84.json with {len(missing_tasks)} tasks.")
