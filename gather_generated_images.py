import json
import os
import glob
import shutil
import time

brain_root = "/Users/vietmac/.gemini/antigravity/brain"
covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"

# Search files from the last 24 hours
cutoff_time = time.time() - 86400 

with open("cotrang_progress.json", "r") as f:
    progress = json.load(f)

with open("new_cotrang_prompts.json", "r") as f:
    all_prompts = json.load(f)

pending = [p for p in all_prompts if p["filename"] not in progress]

success = []
for p in pending:
    filename = p["filename"]
    # The image generation tool sanitizes hyphens into underscores
    prefix = filename.replace(".jpg", "").replace("-", "_")
    
    pattern = os.path.join(brain_root, "*", prefix + "_*.jpg")
    matches = glob.glob(pattern)
    
    valid_matches = [m for m in matches if os.path.getctime(m) > cutoff_time]
    if valid_matches:
        latest = max(valid_matches, key=os.path.getctime)
        dest = os.path.join(covers_dir, filename)
        shutil.copy(latest, dest)
        success.append(filename)
        print(f"Found and copied {filename}")

progress.extend(success)
with open("cotrang_progress.json", "w") as f:
    json.dump(progress, f)

print(f"\nProgress: {len(progress)} / 220")
