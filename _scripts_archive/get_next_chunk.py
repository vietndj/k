import json
import os
import re

DNA = "Featuring a Vietnamese man with an oval face, high cheekbones, expressive Asian monolids, a radiant smile with upper teeth showing, and a signature spiky brush-up hairstyle. He is wearing a dark tailored suit. "

with open("bad_prompts_list.json", "r") as f:
    bad_list = json.load(f)

with open("fix_progress.json", "r") as f:
    progress = json.load(f)

processed_urls = set(progress)

chunk = []
for item in bad_list:
    if item["img_url"] not in processed_urls:
        old = item["old_prompt"]
        if "Movie poster style," in old:
            new_prompt = old.replace("Movie poster style,", f"Movie poster style, {DNA}", 1)
        else:
            new_prompt = f"{DNA} {old}"
        
        filename = item["img_url"].split("/")[-1]
        
        # generate a safe ImageName
        safe_name = "poster_" + re.sub(r'[^a-z0-9_]', '', filename.lower().replace('.jpg', ''))
        # crop to 20 chars max for safety
        safe_name = safe_name[:25]
        
        chunk.append({
            "image_name": safe_name,
            "prompt": new_prompt,
            "filename": filename
        })
        
        if len(chunk) >= 10:
            break

print(json.dumps(chunk, ensure_ascii=False, indent=2))
