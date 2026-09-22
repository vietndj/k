import json
import os

covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"

with open("cotrang_progress.json", "r") as f:
    progress = json.load(f)

print(f"Deleting {len(progress)} contaminated images...")

for filename in progress:
    filepath = os.path.join(covers_dir, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Deleted {filename}")

# Reset progress
with open("cotrang_progress.json", "w") as f:
    json.dump([], f)

print("Cleanup complete. Progress reset to 0.")
