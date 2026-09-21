import json
import os
import glob
import shutil

brain_root = "/Users/vietmac/.gemini/antigravity/brain"
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
    
    # Search across all subdirectories in brain_root
    pattern = os.path.join(brain_root, "*", prefix + "_*.jpg")
    matches = glob.glob(pattern)
    
    valid_matches = [m for m in matches if os.path.getctime(m) > 1726940000]
    if valid_matches:
        latest = max(valid_matches, key=os.path.getctime)
        dest = os.path.join(covers_dir, filename)
        shutil.copy(latest, dest)
        success.append(filename)
        print(f"Found and copied {filename}")
    else:
        print(f"Still waiting for {filename}")

progress.extend(success)
with open("cotrang_progress.json", "w") as f:
    json.dump(progress, f)

print(f"\nProgress: {len(progress)} / 220")
