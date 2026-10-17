import json
import os
import shutil
import glob
import re

brain_dir = "/Users/vietmac/.gemini/antigravity/brain/66d764d7-72c7-410f-ad50-3858ded5125a"
fixes_dir = "/Users/vietmac/Documents/CODE/k/assets/images_gen_fixes"
os.makedirs(fixes_dir, exist_ok=True)

with open("fix_progress.json", "r") as f:
    progress = json.load(f)

# The current chunk we just generated
if os.path.exists("current_chunk.json"):
    with open("current_chunk.json", "r") as f:
        current_chunk = json.load(f)
else:
    current_chunk = []

# Map filenames to their original URLs from bad_prompts_list to update progress correctly
with open("bad_prompts_list.json", "r") as f:
    bad_list = json.load(f)
url_map = {item["img_url"].split("/")[-1]: item["img_url"] for item in bad_list}

def find_latest_artifact(pattern):
    matches = glob.glob(os.path.join(brain_dir, pattern))
    if matches:
        return max(matches, key=os.path.getctime)
    return None

urls = []
for item in current_chunk:
    # Handle the fact that some items in current_chunk might still be the old movie formats.
    # The image_name could be truncated.
    short_name = item["image_name"][:15].replace("poster_poster_", "poster_") 
    pattern = short_name + "*.jpg"
    latest = find_latest_artifact(pattern)
    if latest:
        dest = os.path.join(fixes_dir, item["filename"])
        shutil.copy(latest, dest)
        urls.append(url_map[item["filename"]])
        print(f"✅ Saved {item['filename']}")
    else:
        print(f"❌ Could not find output for {item['image_name']} using pattern {pattern}")

# update progress
progress.extend(urls)
# Deduplicate just in case
progress = list(set(progress))
with open("fix_progress.json", "w") as f:
    json.dump(progress, f)

print(f"Total progress: {len(progress)}/486")

# Now prepare NEXT chunk using the NEW Anime Prompts pool!
processed_urls = set(progress)

with open("new_anime_prompts.json", "r") as f:
    new_anime_prompts = json.load(f)

next_chunk = []
for item in new_anime_prompts:
    # Map back to original URL to check if it's processed
    original_url = url_map[item["filename"]]
    if original_url not in processed_urls:
        filename = item["filename"]
        # Make a safe short name for the agent to use
        safe_name = "poster_" + re.sub(r'[^a-z0-9_]', '', filename.lower().replace('.jpg', ''))
        safe_name = safe_name[:25]
        
        next_chunk.append({
            "image_name": safe_name,
            "prompt": item["prompt"],
            "filename": filename
        })
        
        if len(next_chunk) >= 10:
            break

with open("current_chunk.json", "w") as f:
    json.dump(next_chunk, f, ensure_ascii=False, indent=2)

print(f"Prepared next chunk of {len(next_chunk)} items (ANIME STYLE).")
