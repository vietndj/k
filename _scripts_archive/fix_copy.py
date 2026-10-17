import json
import os
import glob
import shutil
import re

brain_dir = "/Users/vietmac/.gemini/antigravity/brain/66d764d7-72c7-410f-ad50-3858ded5125a"
fixes_dir = "/Users/vietmac/Documents/CODE/k/assets/images_gen_fixes"

with open("new_anime_prompts.json", "r") as f:
    prompts = json.load(f)

success = 0
failed = 0

for item in prompts:
    filename = item["filename"]
    safe_name = "poster_" + re.sub(r'[^a-z0-9_]', '', filename.lower().replace('.jpg', ''))
    safe_name = safe_name[:25]
    
    # generate_image might have truncated safe_name further? 
    # Let's search by the first 15 chars of safe_name, but WITHOUT the weird .replace() that ruined it!
    # Or just search by the first 20 chars of safe_name.
    search_prefix = safe_name[:20]
    
    pattern = os.path.join(brain_dir, search_prefix + "*.jpg")
    matches = glob.glob(pattern)
    
    if matches:
        # Pick the LATEST one (which is guaranteed to be our new anime one, not the old hollywood one which had a completely different prefix or was older!)
        latest = max(matches, key=os.path.getctime)
        dest = os.path.join(fixes_dir, filename)
        shutil.copy(latest, dest)
        success += 1
    else:
        # fallback: search broadly just in case generate_image truncated differently
        search_prefix = safe_name[:12]
        pattern = os.path.join(brain_dir, search_prefix + "*.jpg")
        matches = glob.glob(pattern)
        if matches:
            # We must only pick files generated TODAY (to avoid the old hollywood ones)
            # The old hollywood ones were generated Sep 21 07:25.
            # The new ones were Sep 21 13:00+.
            valid_matches = [m for m in matches if os.path.getctime(m) > 1726900000] # Sep 21 13:26:40 2026 GMT+7
            if valid_matches:
                latest = max(valid_matches, key=os.path.getctime)
                dest = os.path.join(fixes_dir, filename)
                shutil.copy(latest, dest)
                success += 1
            else:
                failed += 1
        else:
            failed += 1

print(f"Successfully copied {success} new anime posters.")
print(f"Failed to find {failed} posters.")
