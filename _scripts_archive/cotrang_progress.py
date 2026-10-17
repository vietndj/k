import json
import os

if not os.path.exists("cotrang_progress.json"):
    with open("cotrang_progress.json", "w") as f:
        json.dump([], f)

with open("cotrang_progress.json", "r") as f:
    progress = json.load(f)

with open("new_cotrang_prompts.json", "r") as f:
    all_prompts = json.load(f)

pending = [p for p in all_prompts if p["filename"] not in progress]

print(f"Total: {len(all_prompts)}")
print(f"Completed: {len(progress)}")
print(f"Pending: {len(pending)}")

# Get next 5 to process
next_batch = pending[:5]
if next_batch:
    print("\n--- NEXT BATCH ---")
    for b in next_batch:
        print(f"FILENAME: {b['filename']}")
        print(f"PROMPT: {b['prompt']}")
        print("---")
