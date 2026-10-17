import json
import os

k_dir = "/Users/vietmac/Documents/CODE/k"
db_path = os.path.join(k_dir, "database.json")

with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

for p in db["posters"]:
    pid = p.get("id", "")
    if pid.startswith("tho-") or p.get("style") == "Google Flow":
        p["category"] = "Triết Lý / Văn Học"
        p["movie_reference"] = "Triết Lý / Văn Học"

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)
    
print("Fixed remaining tho-* items.")
