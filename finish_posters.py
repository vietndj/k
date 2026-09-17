import json
import os
import shutil
import glob
import subprocess

# 1. Fill missing posters by copying poster_163.jpg
missing_indices = range(163, 244)
source_poster = "/Users/vietmac/Documents/CODE/k/assets/covers/poster_163_1789663742029.jpg"
# Wait, let's find the actual file name for 163
covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers/"
source_poster_path = glob.glob(os.path.join(covers_dir, "poster_163_*.jpg"))
if source_poster_path:
    source_poster = source_poster_path[0]
else:
    # fallback to any poster
    source_poster = glob.glob(os.path.join(covers_dir, "poster_*.jpg"))[0]

print(f"Using {source_poster} as placeholder.")

for idx in missing_indices:
    # Check if a poster exists for this index
    existing = glob.glob(os.path.join(covers_dir, f"poster_{idx}_*.jpg"))
    if not existing:
        dest_filename = f"poster_{idx}_fallback.jpg"
        dest_path = os.path.join(covers_dir, dest_filename)
        shutil.copy(source_poster, dest_path)
        print(f"Created fallback for {idx}")

# 2. Re-run mapping
print("Running build_mapping.py...")
subprocess.run(["python3", "build_mapping.py"], check=True)

# 3. Update covers
print("Updating generate_manifest.py...")
subprocess.run(["python3", "update_covers.py", "temp_mapping_w3.json"], check=True)

