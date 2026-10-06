import json
import os
import shutil
from PIL import Image
import subprocess
from datetime import datetime

tho_dir = "/Users/vietmac/Documents/CODE/tho.fedu.vn"
k_dir = "/Users/vietmac/Documents/CODE/k"
covers_dir = os.path.join(tho_dir, "public/assets/covers")

# 1. Read existing database.json
db_path = os.path.join(k_dir, "database.json")
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

existing_ids = {p["id"] for p in db["posters"]}

# 2. Read tho.fedu.vn/data/poems.json
with open(os.path.join(tho_dir, "data/poems.json"), "r", encoding="utf-8") as f:
    poems = json.load(f)

new_entries = []
files_to_convert = []

# Create a temporary directory for webp
os.makedirs("/tmp/k_covers_webp", exist_ok=True)

for poem in poems:
    pid = poem["id"]
    if pid not in existing_ids and poem.get("thumbnail"):
        # We need to process this poem
        img_name = os.path.basename(poem["thumbnail"]) # e.g. poster_tho-0387.jpg
        src_path = os.path.join(covers_dir, img_name)
        if os.path.exists(src_path):
            base_name = os.path.splitext(img_name)[0]
            webp_name = f"{base_name}.webp"
            webp_path = os.path.join("/tmp/k_covers_webp", webp_name)
            
            # Convert to WebP
            if not os.path.exists(webp_path):
                img = Image.open(src_path).convert('RGB')
                img.save(webp_path, 'webp', quality=80)
            
            files_to_convert.append(webp_path)
            
            # Add to database.json
            new_entries.append({
                "id": pid,
                "image": f"https://media.fedu.vn/k_covers/{webp_name}",
                "title": poem.get("suite", "Không có tiêu đề"),
                "poem": poem.get("poem", ""),
                "prompt": poem.get("prompt", ""),
                "has_prompt": bool(poem.get("prompt")),
                "movie_reference": poem.get("category_name", "Thơ / Văn Học"),
                "category": poem.get("category_name", "Thơ / Văn Học"),
                "style": "Cinematic / Default"
            })

print(f"Found {len(new_entries)} new entries to sync.")

if new_entries:
    # 3. Upload to R2
    print("Uploading to R2...")
    rclone_cmd = ["rclone", "copy", "/tmp/k_covers_webp", "r2:vietndjmedia/k_covers", "--progress"]
    subprocess.run(rclone_cmd)
    
    # 4. Update database.json
    db["posters"] = new_entries + db["posters"]
    db["metadata"]["total_images"] = len(db["posters"])
    db["metadata"]["last_updated"] = datetime.now().isoformat()
    
    # sort by ID descending
    db["posters"].sort(key=lambda x: x["id"], reverse=True)
    
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    
    print("Updated database.json")
else:
    print("No new images to sync.")
