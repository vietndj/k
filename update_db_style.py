import json

with open("database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

count = 0
for p in db["posters"]:
    if p["id"].startswith("tho-"):
        p["style"] = "Google Flow"
        count += 1

with open("database.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"Updated {count} items to style Google Flow.")
