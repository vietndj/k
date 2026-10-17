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
    "zone_of_interest_1789623079794.jpg",
    "wish_1789623106092.jpg",
    "poster_346_monsters_inc_1789613441010.jpg",
    "poster_354_cars_1789613336615.jpg",
    "poster_349_kengan_ashura_1789613196888.jpg"
]

urls = [
    "https://media.fedu.vn/images_gen/" + f for f in processed_files
]

def find_latest_artifact(pattern):
    matches = glob.glob(os.path.join(brain_dir, pattern))
    if matches:
        return max(matches, key=os.path.getctime)
    return None

for filename in processed_files:
    if "zone_of_interest" in filename:
        latest = find_latest_artifact("poster_zone_of_interest_*.jpg")
    elif "wish" in filename:
        latest = find_latest_artifact("poster_wish_*.jpg")
    elif "monsters_inc" in filename:
        latest = find_latest_artifact("poster_346_monsters_inc_*.jpg")
    elif "cars" in filename:
        latest = find_latest_artifact("poster_354_cars_*.jpg")
    elif "kengan_ashura" in filename:
        latest = find_latest_artifact("poster_349_kengan_ashura_*.jpg")
    else:
        latest = None

    if latest:
        dest = os.path.join(fixes_dir, filename)
        shutil.copy(latest, dest)
        print(f"✅ Saved {dest}")

# update progress
progress.extend(urls)
with open("fix_progress.json", "w") as f:
    json.dump(progress, f)

print(f"Total progress: {len(progress)}/486")
