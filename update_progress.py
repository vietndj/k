import json
import os
import shutil
import glob

brain_dir = "/Users/vietmac/.gemini/antigravity/brain/66d764d7-72c7-410f-ad50-3858ded5125a"
fixes_dir = "/Users/vietmac/Documents/CODE/k/assets/images_gen_fixes"
os.makedirs(fixes_dir, exist_ok=True)

with open("fix_progress.json", "r") as f:
    progress = json.load(f)

# The batch we just processed
processed_files = [
    "poster_584_1789623091715.jpg",
    "poster_585_1789623105539.jpg",
    "poster_586_1789623122371.jpg",
    "poster_527_1789623099959.jpg",
    "poster_528_1789623113054.jpg"
]

urls = [
    "https://media.fedu.vn/images_gen/" + f for f in processed_files
]

for filename in processed_files:
    prefix = filename.split("_")[1] # e.g., 584
    # find poster_584_*.jpg in brain_dir
    matches = glob.glob(os.path.join(brain_dir, f"poster_{prefix}_*.jpg"))
    if matches:
        latest = max(matches, key=os.path.getctime)
        dest = os.path.join(fixes_dir, filename)
        shutil.copy(latest, dest)
        print(f"✅ Saved {dest}")

# update progress
progress.extend(urls)
with open("fix_progress.json", "w") as f:
    json.dump(progress, f)

print(f"Total progress: {len(progress)}/486")
