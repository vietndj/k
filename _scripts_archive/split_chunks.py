import json

with open("cotrang_progress.json", "r") as f:
    progress = json.load(f)

with open("new_cotrang_prompts.json", "r") as f:
    all_prompts = json.load(f)

pending = [p for p in all_prompts if p["filename"] not in progress]

chunk_size = len(pending) // 4 + 1
for i in range(4):
    chunk = pending[i*chunk_size : (i+1)*chunk_size]
    with open(f"chunk_{i}.json", "w") as f:
        json.dump(chunk, f, ensure_ascii=False, indent=2)
    print(f"Chunk {i}: {len(chunk)} items")

