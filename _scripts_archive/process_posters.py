import os
import glob
import json
import shutil

indices = {
    266: "dung-de-chiec-ghe-an-mon-tri-tue-cua-ban-science-long-form.html",
    267: "ky-nguyen-ai-tinh-nguoi-science.html",
    268: "dung-hy-sinh-su-can-bang-de-doi-lay-thanh-cong-podcast-science.html",
    269: "system-architecture-the-4-types-of-stress.html"
}

artifact_dir = "/Users/vietmac/.gemini/antigravity/brain/893dfd8f-78c0-46d4-803d-e295cadb93bf"
covers_dir = "assets/covers"
mapping = {}

for idx, target_html in indices.items():
    pattern = os.path.join(artifact_dir, f"poster_{idx}_*.jpg")
    files = glob.glob(pattern)
    if files:
        src = files[0]
        base_name = target_html.replace(".html", "") + ".jpg"
        dst = os.path.join(covers_dir, base_name)
        shutil.copy(src, dst)
        mapping[target_html] = dst

with open("temp_mapping_266.json", "w") as f:
    json.dump(mapping, f, indent=2)

