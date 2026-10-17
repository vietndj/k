import json
import os
import re

# 1. Load database.json
with open('database.json', 'r') as f:
    data = json.load(f)

# 2. Extract mappings from nghiem_thu_batch*.md
md_dir = '/Users/vietmac/.gemini/antigravity/brain/3efc28f7-777c-4909-82f0-d3c1b9c5b7aa/'
champion_map = {}
for file in os.listdir(md_dir):
    if file.startswith('nghiem_thu_batch') and file.endswith('.md'):
        with open(os.path.join(md_dir, file), 'r') as f:
            content = f.read()
            # Look for lines like | **tho-0480** | **Hiệu ứng Hào quang (Halo Effect)**<br>Lux tỏa ra...
            lines = content.split('\n')
            for line in lines:
                if '| **tho-' in line:
                    match = re.search(r'\*\*tho-(\d{4})\*\*', line)
                    if match:
                        idx = match.group(1)
                        # Extract the text after <br> or in the same cell
                        parts = line.split('|')
                        if len(parts) > 2:
                            desc = parts[2].lower()
                            champion_map[f'tho-{idx}'] = desc

female_champions = ['female', 'woman', 'girl', 'lady', 'sorceress', 'witch', 'princess', 'queen', 'mermaid', 'goddess', 'enchantress', 'seductress', 'huntress', 'priestess', 'empress', 'nami', 'zoe', 'zyra', 'lux', 'ahri', 'jinx', 'katarina', 'miss fortune', 'vi', 'caitlyn', 'leona', 'diana', 'syndra', 'orianna', 'morgana', 'kayle', 'evelynn', 'akali', 'irelia', 'karma', 'cassiopeia', 'nidalee', 'soraka', 'sona', 'taric', 'ezreal', 'kalista', 'leblanc', 'neeko', 'qiyana', 'rell', 'samira', 'senna', 'seraphine', 'sivir', 'taliyah', 'tristana', 'vayne', 'xayah', 'yone', 'fiora', 'gwen', 'lillia', 'sejuani', 'janna', 'zeri']

bad_dna = []
for p in data['posters']:
    id = p.get('id', '')
    prompt = p.get('prompt', '').lower()
    
    is_bad = False
    
    if id in champion_map:
        desc = champion_map[id]
        if any(w in desc for w in female_champions):
            is_bad = True
    elif prompt:
        has_dna = 'vietnamese man' in prompt or 'vietnamese male' in prompt
        has_female = any(w in prompt for w in female_champions)
        if id.startswith('tho-') and (not has_dna or has_female):
            is_bad = True
    else:
        # If no prompt and no mapping, we can't be sure, but we know 0836 and 0835 are Zyra
        if id in ['tho-0835', 'tho-0836']:
            is_bad = True

    if is_bad:
        bad_dna.append(p)

print(f'Found {len(bad_dna)} bad DNA images.')

new_data = {
    'metadata': {'total_images': len(bad_dna)},
    'posters': bad_dna
}
with open('database_loi.json', 'w') as f:
    json.dump(new_data, f, indent=2, ensure_ascii=False)
