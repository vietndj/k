import hashlib
import os

folder = 'assets/covers'
hashes = {}
duplicates = 0
unique = 0

for f in os.listdir(folder):
    if not f.endswith(('.jpg', '.webp', '.png')): continue
    path = os.path.join(folder, f)
    with open(path, 'rb') as file:
        file_hash = hashlib.md5(file.read()).hexdigest()
    if file_hash in hashes:
        duplicates += 1
    else:
        hashes[file_hash] = f
        unique += 1

print(f"Unique files: {unique}")
print(f"Duplicates: {duplicates}")
