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
current_batch = pending[:10] # Process the 10 we just generated

success = []
for p in current_batch:
    filename = p["filename"]
    prefix = filename.replace(".jpg", "")
    pattern = os.path.join(brain_dir, prefix + "_*.jpg")
    matches = glob.glob(pattern)
    
    valid_matches = [m for m in matches if os.path.getctime(m) > 1726940000]
    if valid_matches:
        latest = max(valid_matches, key=os.path.getctime)
        dest = os.path.join(covers_dir, filename)
        shutil.copy(latest, dest)
        success.append(filename)
    else:
        print(f"Warning: No valid match for {filename}")

progress.extend(success)
with open("cotrang_progress.json", "w") as f:
    json.dump(progress, f)

print(f"Progress: {len(progress)} / 220")

# Generate next batch of 20!
pending_next = [p for p in all_prompts if p["filename"] not in progress]
for p in pending_next[:20]:
    filename = p["filename"]
    prompt = p["prompt"].replace('"', '\\"')
    print(f'\\u1202call:default_api:generate_image{{AspectRatio:"9:16",ImageName:"{filename.replace(".jpg","")}",Prompt:"{prompt}",toolAction:"Generate image",toolSummary:"Gen {filename}"}}\\u1203', end="")
print()

