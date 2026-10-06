import json

db_path = 'database.json'
with open(db_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

posters = data.get('posters', [])

# Deduplicate logic: keep the one with the most information
# Priority: has_prompt=True, has title, has poem
unique_posters = {}
for p in posters:
    pid = p.get('id')
    if not pid:
        # Use image URL as fallback ID
        pid = p.get('image')
    
    if pid not in unique_posters:
        unique_posters[pid] = p
    else:
        existing = unique_posters[pid]
        
        # Calculate a "score" for the existing and the new one
        def score(item):
            s = 0
            if item.get('has_prompt'): s += 10
            if item.get('prompt'): s += 10
            if item.get('title'): s += 5
            if item.get('poem'): s += 5
            # prefer ones where category is not 'Chưa phân loại'
            if item.get('category') and item.get('category') != 'Chưa phân loại' and item.get('category') != 'Khác': s += 2
            return s
            
        if score(p) > score(existing):
            unique_posters[pid] = p

new_posters_list = list(unique_posters.values())

data['posters'] = new_posters_list
data['metadata']['total_images'] = len(new_posters_list)

with open('database_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Original: {len(posters)}, Fixed: {len(new_posters_list)}")
