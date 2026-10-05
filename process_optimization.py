import os
import hashlib
from PIL import Image
import json
import subprocess

covers_dir = 'assets/covers'

# 1. Dedup
hashes = {}
duplicates = []
unique = []
print("1. Hashing and finding duplicates...")
for f in os.listdir(covers_dir):
    if not f.endswith(('.jpg', '.jpeg', '.png')): continue
    path = os.path.join(covers_dir, f)
    with open(path, 'rb') as file:
        file_hash = hashlib.md5(file.read()).hexdigest()
    if file_hash in hashes:
        duplicates.append(path)
    else:
        hashes[file_hash] = path
        unique.append(path)

print(f"Found {len(duplicates)} duplicates. Deleting them...")
for dup in duplicates:
    os.remove(dup)

# 2. Compress to WebP
webp_dir = 'assets/covers_webp'
os.makedirs(webp_dir, exist_ok=True)
print(f"2. Compressing {len(unique)} files to WebP...")
compressed_count = 0
for i, path in enumerate(unique):
    filename = os.path.basename(path)
    base_name = os.path.splitext(filename)[0]
    webp_path = os.path.join(webp_dir, f"{base_name}.webp")
    
    if not os.path.exists(webp_path):
        try:
            img = Image.open(path)
            img = img.convert('RGB')
            img.save(webp_path, 'webp', quality=80)
            compressed_count += 1
        except Exception as e:
            print(f"Error compressing {path}: {e}")
            
    if i % 100 == 0 and i > 0:
        print(f"  Processed {i}/{len(unique)}")

print(f"Successfully compressed {compressed_count} new files.")

# 3. Check what's missing on Drive
print("3. Checking missing files on Google Drive...")
try:
    with open("drive_lsjson.json", "r") as f:
        drive_files = json.load(f)
    drive_names = {item["Name"] for item in drive_files}
except Exception:
    drive_names = set()

missing_drive = []
for path in unique:
    filename = os.path.basename(path)
    if filename not in drive_names:
        missing_drive.append(path)

print(f"Missing on Drive: {len(missing_drive)} files.")
with open("missing_drive.txt", "w") as f:
    for p in missing_drive:
        f.write(p + "\n")

print("Done. Ready for rclone upload.")
