import os
import glob
import subprocess
import json

base_dir = "/Users/vietmac/.gemini/antigravity/brain/3efc28f7-777c-4909-82f0-d3c1b9c5b7aa"
ids = [
    "tho-0825", "tho-0824", "tho-0823", "tho-0822", "tho-0821", "tho-0820", "tho-0819", "tho-0818", "tho-0817", "tho-0816",
    "tho-0815", "tho-0814", "tho-0813", "tho-0812", "tho-0811", "tho-0810", "tho-0809", "tho-0808", "tho-0782", "tho-0781",
    "tho-0780", "tho-0779", "tho-0778", "tho-0777", "tho-0776", "tho-0775", "tho-0774", "tho-0773", "tho-0772", "tho-0771"
]

webps_to_upload = []

for item_id in ids:
    # Find latest generated image for this id
    pattern = f"{base_dir}/poster_{item_id.replace('-', '_')}*.jpg"
    files = glob.glob(pattern)
    if not files:
        print(f"Missing {item_id}")
        continue
    
    # Sort by creation time to get latest
    latest_file = max(files, key=os.path.getctime)
    webp_path = f"/tmp/poster_{item_id}.webp"
    
    # Convert
    subprocess.run(["cwebp", "-q", "80", latest_file, "-o", webp_path], check=True)
    webps_to_upload.append(webp_path)
    
print(f"Converted {len(webps_to_upload)} files.")

# Upload in parallel with rclone
for w in webps_to_upload:
    subprocess.run(["rclone", "copyto", w, f"r2:vietndjmedia/k_covers/{os.path.basename(w)}"])

print("Uploaded to R2.")

# Update database.json
with open("database.json", "r") as f:
    db = json.load(f)

for p in db["posters"]:
    if p["id"] in ids:
        prompt_path = f"/tmp/prompt_{p['id']}.txt"
        if os.path.exists(prompt_path):
            with open(prompt_path, "r") as pf:
                p["prompt"] = pf.read()
            p["has_prompt"] = True

with open("database.json", "w") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("Updated database.json")

# Remove from database_loi.json
with open("database_loi.json", "r") as f:
    db_loi = json.load(f)

db_loi["posters"] = [p for p in db_loi["posters"] if p["id"] not in ids]

with open("database_loi.json", "w") as f:
    json.dump(db_loi, f, indent=2, ensure_ascii=False)

print("Updated database_loi.json")
