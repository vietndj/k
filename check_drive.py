import json

with open("database.json", "r") as f:
    db = json.load(f)

with open("drive_lsjson.json", "r") as f:
    drive = json.load(f)

drive_files = {item["Name"]: item["ID"] for item in drive}

missing = 0
found = 0
for p in db["posters"]:
    local_path = p.get("image", "")
    filename = local_path.split("/")[-1]
    if filename in drive_files:
        found += 1
    else:
        missing += 1

print(f"Found in Drive: {found}")
print(f"Missing in Drive: {missing}")
