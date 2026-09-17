import glob
import os
import shutil
import json
import subprocess

brain_dir = "/Users/vietmac/.gemini/antigravity/brain/432cfc5a-d34b-4005-9ce2-f6d3b5655fb7"
repo_dir = "/Users/vietmac/Documents/CODE/k"
covers_dir = os.path.join(repo_dir, "assets", "covers")

targets = {
    "poster_272_ozark": "so-tay-xay-kenh-thuat-toan-mentor-nguyen-duc-viet-podcast.html",
    "poster_273_fate_stay_night": "mo-gawdat-giai-ma-hanh-phuc-ky-nguyen-ai-podcast.html",
    "poster_274_kim_possible": "hau-het-met-moi-suong-mu-nao-lao-hoa-va-con-them-an-khong-phai-do-ban-thieu-y-chi-ma-do-tau-luon-sieu-toc-cua-glucose-trong-mau-khong-can.html",
    "poster_275_chi_chi_em_em": "ky-luat-khac-ky-lam-chu-ban-than-giai-phong-tu-do-science-long-form.html",
    "poster_276_itaewon_class": "tu-duy-ai-tu-dong-hoa-science.html"
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
    subprocess.run(["git", "commit", "-m", f"feat: add posters 272-276"])
    subprocess.run(["git", "push"])
    print(f"Processed and pushed {len(mapping)} images.")
