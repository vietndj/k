import glob
import os
import shutil
import json
import subprocess

brain_dir = "/Users/vietmac/.gemini/antigravity/brain/432cfc5a-d34b-4005-9ce2-f6d3b5655fb7"
repo_dir = "/Users/vietmac/Documents/CODE/k"
covers_dir = os.path.join(repo_dir, "assets", "covers")
os.makedirs(covers_dir, exist_ok=True)

# Define the targets for this batch
targets = {
    "poster_257_my_hero_academia": "youtube-masterclass-highest-paid-strategist.html",
    "poster_258_ice_age": "boc-tran-cu-lua-diet-vong.html",
    "poster_259_thien_menh_anh_hung": "banner.html",
    "poster_260_halt_and_catch_fire": "banner-phan-tich-2-mau-poster-tatler-va-ket-qua-hinh-anh.html",
    "poster_261_made_in_abyss": "kichbanoffline-phau-thuat-kich-ban-5.html"
}

mapping = {}

for prefix, html_file in targets.items():
    pattern = os.path.join(brain_dir, f"{prefix}*.jpg")
    matches = glob.glob(pattern)
    if matches:
        src = matches[0]
        # remove timestamp suffix for cleaner naming if desired, but here we just use the name
        dest_filename = f"{prefix}.jpg"
        dest = os.path.join(covers_dir, dest_filename)
        shutil.copy2(src, dest)
        mapping[html_file] = f"./assets/covers/{dest_filename}"

if mapping:
    with open("temp_mapping.json", "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2)
    
    subprocess.run(["python3", "update_covers.py", "temp_mapping.json"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"feat: add posters 257-261"])
    subprocess.run(["git", "push"])
    print(f"Processed and pushed {len(mapping)} images.")
else:
    print("No images found to process.")
