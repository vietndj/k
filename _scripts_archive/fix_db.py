import json
import os

k_dir = "/Users/vietmac/Documents/CODE/k"
tho_dir = "/Users/vietmac/Documents/CODE/tho.fedu.vn"

with open(os.path.join(k_dir, "database.json"), "r", encoding="utf-8") as f:
    db = json.load(f)

existing_ids = {p["id"] for p in db["posters"]}

with open(os.path.join(tho_dir, "data/poems.json"), "r", encoding="utf-8") as f:
    poems = json.load(f)

added = 0
for poem in poems:
    pid = poem["id"]
    if pid not in existing_ids:
        # Check if the thumbnail is like poster_tho-xxxx.jpg
        base_name = os.path.basename(poem.get("thumbnail", ""))
        webp_name = base_name.replace(".jpg", ".webp").replace(".png", ".webp")
        if not webp_name:
            webp_name = f"poster_{pid}.webp"
            
        db["posters"].append({
            "id": pid,
            "image": f"https://media.fedu.vn/k_covers/{webp_name}",
            "title": poem.get("suite", "Không có tiêu đề"),
            "poem": poem.get("poem", ""),
            "prompt": poem.get("prompt", ""),
            "has_prompt": bool(poem.get("prompt")),
            "movie_reference": poem.get("category_name", "Thơ / Văn Học"),
            "category": poem.get("category_name", "Thơ / Văn Học"),
            "style": "Google Flow"
        })
        added += 1

db["metadata"]["total_images"] = len(db["posters"])

with open(os.path.join(k_dir, "database.json"), "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)
    
print(f"Added {added} missing items.")
