import json

path = "/Users/vietmac/Documents/CODE/k/all_unique_posters.json"
with open(path, "r") as f:
    data = json.load(f)

for item in data:
    if "url" in item:
        item["path"] = item.pop("url")
    if "image" in item:
        item["path"] = item.pop("image")

with open(path, "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
