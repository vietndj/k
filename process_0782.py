import os
import glob
import subprocess
import json

item_id = "tho-0782"
base_dir = "/Users/vietmac/.gemini/antigravity/brain/3efc28f7-777c-4909-82f0-d3c1b9c5b7aa"

# Find latest generated image for this id
pattern = f"{base_dir}/poster_{item_id.replace('-', '_')}*.jpg"
files = glob.glob(pattern)
if files:
    latest_file = max(files, key=os.path.getctime)
    webp_path = f"/tmp/poster_{item_id}.webp"
    
    # Convert
    subprocess.run(["cwebp", "-q", "80", latest_file, "-o", webp_path], check=True)
    subprocess.run(["rclone", "copyto", webp_path, f"r2:vietndjmedia/k_covers/{os.path.basename(webp_path)}"])

    # Update database.json
    with open("database.json", "r") as f:
        db = json.load(f)

    for p in db["posters"]:
        if p["id"] == item_id:
            prompt_path = f"/tmp/prompt_{item_id}.txt"
            if os.path.exists(prompt_path):
                with open(prompt_path, "r") as pf:
                    p["prompt"] = pf.read()
                p["has_prompt"] = True

    with open("database.json", "w") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    # Remove from database_loi.json
    with open("database_loi.json", "r") as f:
        db_loi = json.load(f)

    db_loi["posters"] = [p for p in db_loi["posters"] if p["id"] != item_id]

    with open("database_loi.json", "w") as f:
        json.dump(db_loi, f, indent=2, ensure_ascii=False)
