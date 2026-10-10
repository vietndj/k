import json
import os

k_dir = "/Users/vietmac/Documents/CODE/k"
db_path = os.path.join(k_dir, "database.json")

with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

anime_ids = []
game_ids = []
movie_ids = []

if os.path.exists("anime_updates.json"):
    with open("anime_updates.json", "r") as f:
        anime_ids = json.load(f)

if os.path.exists("game_updates.json"):
    with open("game_updates.json", "r") as f:
        game_ids = json.load(f)

if os.path.exists("movie_updates.json"):
    with open("movie_updates.json", "r") as f:
        movie_ids = json.load(f)

updated_count = 0

for p in db["posters"]:
    pid = p["id"]
    if pid in anime_ids:
        p["category"] = "Anime"
        p["movie_reference"] = "Anime"
        updated_count += 1
    elif pid in game_ids:
        p["category"] = "Game"
        p["movie_reference"] = "Game"
        updated_count += 1
    elif pid in movie_ids:
        p["category"] = "Phim Điện Ảnh"
        p["movie_reference"] = "Phim Điện Ảnh"
        updated_count += 1

print(f"Updated {updated_count} posters with new categories.")

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)
