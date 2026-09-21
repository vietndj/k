import json
import html

with open("all_unique_posters.json", "r") as f:
    items = json.load(f)

unique_clean = set()
duplicates = 0
for item in items:
    # Decode html entities (like &#x27;) and normalize spaces
    clean_p = html.unescape(item["prompt"]).strip()
    if clean_p in unique_clean:
        duplicates += 1
    else:
        unique_clean.add(clean_p)

print(f"Total items: {len(items)}")
print(f"Duplicates after HTML unescape: {duplicates}")
print(f"Real unique items: {len(unique_clean)}")
