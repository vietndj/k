import json
import os
from PIL import Image

queue_file = 'queue.json'
with open(queue_file, 'r', encoding='utf-8') as f:
    queue = json.load(f)

for item in queue:
    filename = item['filename'].replace('.html', '.jpg')
    img_path = f"assets/temp_covers/{filename}"
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save(img_path)
    print(f"Created {img_path}")
