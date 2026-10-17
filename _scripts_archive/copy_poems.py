import json
import shutil
import os
import glob

# Paths
tho_data = "/Users/vietmac/Documents/CODE/tho.fedu.vn/data/poems.json"
tho_covers_dir = "/Users/vietmac/Documents/CODE/tho.fedu.vn/public/assets/covers"

k_covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
k_json = "/Users/vietmac/Documents/CODE/k/all_unique_posters.json"

# Load data
with open(tho_data, "r") as f:
    poems = json.load(f)

poem_map = {p["id"]: p for p in poems}

with open(k_json, "r") as f:
    all_unique_posters = json.load(f)

existing_paths = {p.get("path", "") for p in all_unique_posters}

new_posters = glob.glob(os.path.join(tho_covers_dir, "poster_tho-*.jpg"))

added = 0
for src in new_posters:
    filename = os.path.basename(src)
    poem_id = filename.replace("poster_", "").replace(".jpg", "")
    poem = poem_map.get(poem_id, {})
    
    # Copy file to k repo
    dst = os.path.join(k_covers_dir, filename)
    shutil.copy2(src, dst)
    
    # Update JSON
    rel_path = f"assets/covers/{filename}"
    if rel_path not in existing_paths:
        prompt_text = f"POEM: {poem.get('suite', '')} - {poem.get('category_name', '')}\n\n{poem.get('poem', '')}\n\nExplanation: {poem.get('explanation', '')}"
        
        all_unique_posters.append({
            "path": rel_path,
            "prompt": prompt_text,
            "movie": "Poem Collection",
            "character": "Vietnamese Male"
        })
        existing_paths.add(rel_path)
        added += 1

if added > 0:
    with open(k_json, "w") as f:
        json.dump(all_unique_posters, f, indent=4, ensure_ascii=False)
    print(f"Added {added} new poem covers to k repo.")
else:
    print("No new covers added.")
