import json

path = "/Users/vietmac/Documents/CODE/k/all_unique_posters.json"

with open(path, "r") as f:
    posters = json.load(f)

# The new ones were appended to the end. They have "url" like "https://media.fedu.vn/k_covers/concept_XXX.webp"
# We want them at the front.
new_posters = []
old_posters = []

for p in posters:
    url = p.get("url", p.get("image", ""))
    if url.startswith("assets/covers/concept_") and url.endswith(".webp"):
        new_posters.append(p)
    else:
        old_posters.append(p)

# We want the newest generated at the top? Or just all 'concept_*.webp' at the top.
# Let's sort the new_posters by concept ID in descending order.
import re
def get_id(p):
    url = p.get("url", p.get("image", ""))
    match = re.search(r'concept_(\d+)', url)
    return int(match.group(1)) if match else 0

new_posters.sort(key=get_id, reverse=True)

# Recombine
reordered = new_posters + old_posters

with open(path, "w") as f:
    json.dump(reordered, f, indent=4, ensure_ascii=False)

print(f"Moved {len(new_posters)} new images to the top.")
