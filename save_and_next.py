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

with open("current_chunk.json", "r") as f:
    current_chunk = json.load(f)

# we need to lookup url from bad_list
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
    # safe glob match because ImageName could have been truncated
    short_name = item["image_name"][:15].replace("poster_poster_", "poster_") # normalize to what we actually passed to the tool
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
with open("fix_progress.json", "w") as f:
    json.dump(progress, f)

print(f"Total progress: {len(progress)}/486")

# Now prepare NEXT chunk (Chunk 3)
processed_urls = set(progress)
DNA = "Featuring a Vietnamese man with an oval face, high cheekbones, expressive Asian monolids, a radiant smile with upper teeth showing, and a signature spiky brush-up hairstyle. He is wearing a dark tailored suit. "

next_chunk = []
for item in bad_list:
    if item["img_url"] not in processed_urls:
        old = item["old_prompt"]
        if "Movie poster style," in old:
            new_prompt = old.replace("Movie poster style,", f"Movie poster style, {DNA}", 1)
        else:
            new_prompt = f"{DNA} {old}"
        
        filename = item["img_url"].split("/")[-1]
        safe_name = "poster_" + re.sub(r'[^a-z0-9_]', '', filename.lower().replace('.jpg', ''))
        safe_name = safe_name[:25]
        
        next_chunk.append({
            "image_name": safe_name,
            "prompt": new_prompt,
            "filename": filename
        })
        
        if len(next_chunk) >= 10:
            break

with open("current_chunk.json", "w") as f:
    json.dump(next_chunk, f, ensure_ascii=False, indent=2)

print(f"Prepared next chunk of {len(next_chunk)} items.")
