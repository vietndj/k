import json
import re

def extract_tags(text):
    tags = []
    text_lower = text.lower()
    
    keywords = ['cyberpunk', 'sci-fi', 'giant', 'macro', 'samurai', 'ninja', 'robot', 'monster', 'space', 'galaxy', 'crystal', 'mirror', 'glass', 'water', 'fire', 'neon', 'dark', 'light']
    for k in keywords:
        if k in text_lower:
            tags.append(k.capitalize())
            
    if len(tags) < 2:
        tags.extend(['Art', 'Illustration'])
    return tags[:3]

def determine_style(prompt, poem):
    prompt_lower = prompt.lower()
    if any(x in prompt_lower for x in ['anime', 'manga', 'ghibli']):
        return 'Anime Style'
    if any(x in prompt_lower for x in ['3d', 'unreal', 'octane']):
        return '3D Render'
    if 'cinematic' in prompt_lower:
        return 'Cinematic'
    if poem:
        return 'Google Flow'
    return 'Chưa phân loại'

def determine_movie_type(prompt):
    prompt_lower = prompt.lower()
    if any(x in prompt_lower for x in ['space', 'galaxy', 'sci-fi', 'cyberpunk', 'quantum', 'time', 'future']):
        return 'Viễn Tưởng'
    if any(x in prompt_lower for x in ['sword', 'battle', 'fight', 'gun', 'strike', 'smash']):
        return 'Hành Động'
    if any(x in prompt_lower for x in ['magic', 'wizard', 'dragon', 'fantasy', 'myth', 'god', 'titan']):
        return 'Kỳ Ảo'
    if any(x in prompt_lower for x in ['anime', 'manga']):
        return 'Hoạt Hình'
    if any(x in prompt_lower for x in ['love', 'kiss', 'romance', 'couple']):
        return 'Lãng Mạn'
    return 'Khác'

def determine_movie_ref(prompt):
    prompt_lower = prompt.lower()
    refs = {
        'league of legends': 'League of Legends',
        'matrix': 'Matrix',
        'naruto': 'Naruto',
        'valorant': 'Valorant',
        'star wars': 'Star Wars',
        'marvel': 'Marvel',
        'dc': 'DC',
        'pokemon': 'Pokemon',
        'harry potter': 'Harry Potter',
        'lord of the rings': 'Lord of the Rings'
    }
    for k, v in refs.items():
        if k in prompt_lower:
            return v
    return 'Chưa phân loại'

with open('/Users/vietmac/Documents/CODE/k/database.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for poster in data.get('posters', []):
    prompt = poster.get('prompt', '')
    title = poster.get('title', '')
    poem = poster.get('poem', '')
    
    text_for_tags = prompt + ' ' + title
    
    poster['tags'] = extract_tags(text_for_tags)
    poster['style'] = determine_style(prompt, poem)
    poster['movie_type'] = determine_movie_type(prompt)
    
    # only update if it is generic or we found a match
    ref = determine_movie_ref(prompt)
    if ref != 'Chưa phân loại' or poster.get('movie_reference') == 'Chưa phân loại' or not poster.get('movie_reference'):
        poster['movie_reference'] = ref

with open('/Users/vietmac/Documents/CODE/k/database.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done updating JSON")
