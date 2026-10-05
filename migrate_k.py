import json
import datetime
from bs4 import BeautifulSoup

file_path = '/Users/vietmac/Documents/CODE/k/anh.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

cards = soup.find_all('div', class_='card')
posters = []

for card in cards:
    img_tag = card.find('img')
    if not img_tag:
        continue
    image_src = img_tag.get('src')
    
    # Check for copy-btn to get data-prompt
    prompt = ""
    copy_btn = card.find('button', class_='copy-btn')
    if copy_btn and copy_btn.has_attr('data-prompt'):
        prompt = copy_btn['data-prompt']
        
    has_prompt = bool(prompt)
    
    # Try to find ID, title, poem
    poem_content = card.find('div', class_='poem-content')
    card_id = ""
    title = ""
    poem = ""
    if poem_content:
        divs = poem_content.find_all('div', recursive=False)
        if len(divs) >= 3:
            card_id = divs[0].text.strip()
            title = divs[1].text.strip()
            poem = divs[2].text.strip()
            
    # If no poem-content, maybe it's the old style
    if not card_id:
        id_tag = card.find('div', class_='card-id') or card.find('div', class_='card-label') or card.find('span')
        if id_tag:
            card_id = id_tag.text.strip()
            
    if not title:
        title_tag = card.find('h3', class_='card-title')
        if title_tag:
            title = title_tag.text.strip()
            
    if not poem:
        poem_tag = card.find('p', class_='card-poem')
        if poem_tag:
            poem = poem_tag.text.strip()

    posters.append({
        "id": card_id,
        "image": image_src,
        "title": title,
        "poem": poem,
        "prompt": prompt,
        "has_prompt": has_prompt,
        "movie_reference": "Chưa phân loại",
        "category": "Chưa phân loại",
        "style": "Chưa phân loại"
    })

print(f"Found {len(posters)} cards")

data = {
    "metadata": {
        "total_images": len(posters),
        "last_updated": datetime.datetime.now().isoformat()
    },
    "posters": posters
}

with open('/Users/vietmac/Documents/CODE/k/database.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved to /Users/vietmac/Documents/CODE/k/database.json")
