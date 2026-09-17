import glob
import os
import shutil
import json
import subprocess

brain_dir = "/Users/vietmac/.gemini/antigravity/brain/432cfc5a-d34b-4005-9ce2-f6d3b5655fb7"
repo_dir = "/Users/vietmac/Documents/CODE/k"
covers_dir = os.path.join(repo_dir, "assets", "covers")

targets = {
    "poster_262_chicken_run": "kichbanoffline-phau-thuat-kich-ban-4.html",
    "poster_263_that_son_tam_linh": "kichbanoffline-phau-thuat-kich-ban-3.html",
    "poster_264_severance": "kichbanoffline-phau-thuat-kich-ban-2.html",
    "poster_265_kill_la_kill": "kichbanoffline-phau-thuat-kich-ban-1.html"
}

mapping = {}
for prefix, html_file in targets.items():
    pattern = os.path.join(brain_dir, f"{prefix}*.jpg")
    matches = glob.glob(pattern)
    if matches:
        src = matches[0]
        dest_filename = f"{prefix}.jpg"
        dest = os.path.join(covers_dir, dest_filename)
        shutil.copy2(src, dest)
        mapping[html_file] = f"./assets/covers/{dest_filename}"

if mapping:
    with open("temp_mapping.json", "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2)
    
    subprocess.run(["python3", "update_covers.py", "temp_mapping.json"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"feat: add posters 262-265"])
    subprocess.run(["git", "push"])
    print(f"Processed and pushed {len(mapping)} images.")
