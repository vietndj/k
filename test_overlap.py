import json

with open("anime_updates.json", "r") as f:
    a = set(json.load(f))
with open("game_updates.json", "r") as f:
    g = set(json.load(f))
with open("movie_updates.json", "r") as f:
    m = set(json.load(f))

print("Anime:", len(a))
print("Game:", len(g))
print("Movie:", len(m))

union = a | g | m
print("Total Unique:", len(union))

print("Overlap A & G:", len(a & g))
print("Overlap A & M:", len(a & m))
print("Overlap G & M:", len(g & m))
