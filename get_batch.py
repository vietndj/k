import json
import os

DNA = "Featuring a Vietnamese man with an oval face, high cheekbones, expressive Asian monolids, a radiant smile with upper teeth showing, and a signature spiky brush-up hairstyle. He is wearing a dark tailored suit. "

if not os.path.exists("fix_progress.json"):
    with open("fix_progress.json", "w") as f:
        json.dump([], f)

with open("bad_prompts_list.json", "r") as f:
    bad_list = json.load(f)

with open("fix_progress.json", "r") as f:
    progress = json.load(f)

processed_urls = set(progress)

batch = []
for item in bad_list:
    if item["img_url"] not in processed_urls:
        # Inject DNA after "Movie poster style," or at the beginning
        old = item["old_prompt"]
        if "Movie poster style," in old:
            new_prompt = old.replace("Movie poster style,", f"Movie poster style, {DNA}", 1)
        else:
            new_prompt = f"{DNA} {old}"
        
        filename = item["img_url"].split("/")[-1]
        
        batch.append({
            "url": item["img_url"],
            "filename": filename,
            "new_prompt": new_prompt
        })
        
        if len(batch) >= 5: # Batch of 5 for safety/concurrency limits
            break

print(json.dumps(batch, ensure_ascii=False))
