import json
import re

def clean_id(raw_id):
    cleaned = raw_id.lower()
    prefixes = ['poster_', 'concept_', 'cover_']
    for p in prefixes:
        if cleaned.startswith(p):
            cleaned = cleaned[len(p):]
    return cleaned

def classify_movie(poster):
    text_to_search = (poster.get('id', '') + " " + poster.get('image', '') + " " + poster.get('title', '')).lower()
    
    mapping = {
        'peaky': 'Peaky Blinders',
        'stevejobs': 'Steve Jobs',
        'ironman': 'Iron Man',
        'inception': 'Inception',
        'batman': 'Batman',
        'naruto': 'Naruto',
        'matrix': 'The Matrix',
        'avatar': 'Avatar',
        'oppenheimer': 'Oppenheimer',
        'interstellar': 'Interstellar',
        'joker': 'Joker',
        'godfather': 'The Godfather',
        'breakingbad': 'Breaking Bad',
        'cyberpunk': 'Cyberpunk 2077',
        'witcher': 'The Witcher',
        'harrypotter': 'Harry Potter',
        'starwars': 'Star Wars',
        'avengers': 'Avengers',
        'spiderman': 'Spider-Man',
        'tho-': 'Thơ Giáo Dục / Triết Lý',
        'suc-manh-thao-tung': 'Social Media / Algorithm',
        'any_given_sunday': 'Any Given Sunday',
        'john_wick': 'John Wick',
        'moneyball': 'Moneyball',
        'wolf_of_wall_street': 'Wolf of Wall Street',
        'fight_club': 'Fight Club',
        'gladiator': 'Gladiator',
        'social_network': 'The Social Network'
    }
    
    for key, name in mapping.items():
        if key in text_to_search:
            return name
            
    return 'Chưa phân loại'

def classify_category(poster):
    title = poster.get('title', '').lower()
    prompt = poster.get('prompt', '').lower()
    _id = poster.get('id', '').lower()
    
    if 'anime' in prompt or 'manga' in prompt or 'naruto' in _id:
        return 'Anime / Manga'
    if 'game' in prompt or 'cyberpunk' in _id or 'witcher' in _id:
        return 'Game'
    if 'phim' in prompt or 'cinematic' in prompt or 'movie' in prompt:
        return 'Phim Điện Ảnh'
    if 'tho-' in _id or 'thơ' in title or 'lục bát' in title:
        return 'Thơ / Văn Học'
    
    # Check for specific scientific/business themes in title
    if 'não bộ' in title or 'thần kinh' in title or 'biohack' in title:
        return 'Khoa Học / Sinh Học'
    if 'kinh doanh' in title or 'dòng tiền' in title or 'hệ thống' in title:
        return 'Kinh Doanh / Hệ Thống'
        
    return 'Khác'

def classify_style(poster):
    prompt = poster.get('prompt', '').lower()
    if '3d' in prompt or 'render' in prompt or 'octane' in prompt or 'unreal' in prompt:
        return '3D Render'
    if 'anime' in prompt or 'manga' in prompt or 'ghibli' in prompt:
        return 'Anime Style'
    if 'cinematic' in prompt or 'movie' in prompt or 'photography' in prompt or 'photorealistic' in prompt:
        return 'Cinematic'
    if 'vector' in prompt or 'illustration' in prompt or 'flat' in prompt:
        return 'Illustration / 2D'
    if 'painting' in prompt or 'oil' in prompt or 'watercolor' in prompt:
        return 'Painting / Art'
        
    return 'Cinematic / Default'

with open('/Users/vietmac/Documents/CODE/k/database.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for poster in data['posters']:
    poster['movie_reference'] = classify_movie(poster)
    poster['category'] = classify_category(poster)
    poster['style'] = classify_style(poster)

with open('/Users/vietmac/Documents/CODE/k/database.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Audit and classification completed.")
