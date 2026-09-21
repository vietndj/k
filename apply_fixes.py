import json
import os
import shutil
import re
import glob

# Mappings of movie prefix to HTML file
target_updates = {
    "gundam": "ai-changed-marketing-forever-agencies-dead-podcast.html",
    "hai_phuong": "giai-phong-chan-nga-ban-do-thuc-tinh-chua-lanh-tam-thuc.html",
    "stranger_things": "lam-chu-ngon-tu-khong-nam-o-viec-gianh-phan-thang.html",
    "how_to_train_your_dragon": "thanh-cong-kinh-doanh-khong-dinh-hinh-tu-viec-ban-gioi-moi-thu-ma-tu-viec-ban-ru-bo-cai-toi-am-anh-voi-chat-luong-va-muon-suc-nhung-khoi-oc.html",
    "rezero": "y-hoc-30-chu-dong-can-thiep-tu-som-coi-tap-luyen-la-loai-thuoc-manh-nhat-va-muc-tieu-la-keo-dai-tuoi-tho-khoe-manh-healthspan-thay-vi-chi.html",
    "trang_quynh": "khoi-nghiep-ky-nguyen-moi-science.html",
    "money_heist": "hay-ngung-dua-vao-y-chi-hay-cam-tinh-de-ra-quyet-dinh-song-bang-cach-thiet-lap-thuat-toan-ky-luat-blueprint-va-de-du-lieu-len-tieng-ban-co.html",
    "psychopass": "system-7-the-3-ways-pressure-breaks-you.html"
}

brain_dir = "/Users/vietmac/.gemini/antigravity/brain/66d764d7-72c7-410f-ad50-3858ded5125a"
covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
os.makedirs(covers_dir, exist_ok=True)

updates = {}

for prefix, html_file in target_updates.items():
    # Find the generated image in brain_dir
    search_pattern = os.path.join(brain_dir, f"poster_{prefix}_*.jpg")
    matches = glob.glob(search_pattern)
    if matches:
        latest = max(matches, key=os.path.getctime)
        new_filename = f"poster_fix_{prefix}.jpg"
        dest_path = os.path.join(covers_dir, new_filename)
        shutil.copy(latest, dest_path)
        print(f"✅ Copied {prefix} -> {new_filename}")
        updates[html_file] = f"./assets/covers/{new_filename}"
    else:
        print(f"❌ Missing generated image for {prefix}")

# Now update generate_manifest.py
manifest_path = "/Users/vietmac/Documents/CODE/k/generate_manifest.py"
with open(manifest_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the lines in cover_mapping
for html_file, new_url in updates.items():
    # regex to find the exact line in cover_mapping
    # e.g. "ai-changed...html": "./assets/covers/poster_61.jpg",
    pattern = r'("' + re.escape(html_file) + r'"\s*:\s*)"([^"]+)"'
    content = re.sub(pattern, r'\g<1>"' + new_url + '"', content)

with open(manifest_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Updated generate_manifest.py with {len(updates)} new mappings.")
