import os
import re
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

src_dir = "/Users/vietmac/Documents/CODE/tho.fedu.vn/public/assets/covers/"
dest_dir = "/Users/vietmac/Documents/CODE/k/assets/covers/"
html_file = "/Users/vietmac/Documents/CODE/k/anh.html"

os.makedirs(dest_dir, exist_ok=True)

with open(html_file, "r") as f:
    content = f.read()

# Extract jpg names
jpg_files = list(set(re.findall(r'poster_tho-[0-9]*\.jpg', content)))

def process_file(jpg):
    src_path = os.path.join(src_dir, jpg)
    if os.path.exists(src_path):
        webp = jpg.replace('.jpg', '.webp')
        dest_path = os.path.join(dest_dir, webp)
        if not os.path.exists(dest_path):
            try:
                with Image.open(src_path) as img:
                    img.save(dest_path, "WEBP", quality=80)
            except Exception as e:
                print(f"Error {jpg}: {e}")

print(f"Found {len(jpg_files)} files to convert.")
with ThreadPoolExecutor(max_workers=8) as executor:
    executor.map(process_file, jpg_files)

# Update HTML
print("Updating HTML paths...")
content = content.replace("https://tho.fedu.vn/assets/covers/", "/assets/covers/")
content = content.replace(".jpg", ".webp")

with open(html_file, "w") as f:
    f.write(content)

print("Done")
