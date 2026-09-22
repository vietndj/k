import json
import os
import glob
import shutil

brain_dir = "/Users/vietmac/.gemini/antigravity/brain/66d764d7-72c7-410f-ad50-3858ded5125a"
covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"

with open("cotrang_progress.json", "r") as f:
    progress = json.load(f)

with open("new_cotrang_prompts.json", "r") as f:
    all_prompts = json.load(f)

pending = [p for p in all_prompts if p["filename"] not in progress]

success = []
for p in pending:
    filename = p["filename"]
    prefix = filename.replace(".jpg", "")
    
    # Search only in the current brain directory to avoid pulling garbage from old chats
    pattern = os.path.join(brain_dir, prefix + "_*.jpg")
    matches = glob.glob(pattern)
    
    if matches:
        latest = max(matches, key=os.path.getctime)
        dest = os.path.join(covers_dir, filename)
        shutil.copy(latest, dest)
        success.append(filename)
        print(f"Found and copied {filename}")

progress.extend(success)
with open("cotrang_progress.json", "w") as f:
    json.dump(progress, f)

print(f"\nProgress: {len(progress)} / 220")
