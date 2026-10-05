import os
import hashlib
from PIL import Image

folder_in = 'assets/anhloi'
folder_out = 'assets/anhloi_webp'
os.makedirs(folder_out, exist_ok=True)

hashes = {}
duplicates = []
unique = []

for f in os.listdir(folder_in):
    if not f.endswith(('.jpg', '.jpeg', '.png')): continue
    path = os.path.join(folder_in, f)
    with open(path, 'rb') as file:
        file_hash = hashlib.md5(file.read()).hexdigest()
    if file_hash in hashes:
        duplicates.append(path)
    else:
        hashes[file_hash] = path
        unique.append(path)

for dup in duplicates:
    os.remove(dup)

for i, path in enumerate(unique):
    filename = os.path.basename(path)
    base_name = os.path.splitext(filename)[0]
    webp_path = os.path.join(folder_out, f"{base_name}.webp")
    if not os.path.exists(webp_path):
        try:
            img = Image.open(path).convert('RGB')
            img.save(webp_path, 'webp', quality=80)
        except Exception as e:
            pass

print(f"Processed {folder_in}. Found {len(duplicates)} duplicates. Compressed {len(unique)} files.")
