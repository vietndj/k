import re
import json

with open("nghiem_thu_640_posters.html", "r") as f:
    html = f.read()

with open("bad_prompts_list.json", "r") as f:
    bad_list = json.load(f)

# old_url -> old_filename (like poster_351_co_hau_gai.jpg)
bad_url_to_old_filename = {}
for b in bad_list:
    filename = b["img_url"].split("/")[-1]
    if filename: # avoid empty string issues
        bad_url_to_old_filename[b["img_url"]] = filename
        
# also map by alt text / prompt or index if possible
# bad_list doesn't have index, but it has img_url.

with open("new_anime_prompts.json", "r") as f:
    new_prompts = json.load(f)

old_filename_to_new_data = {}
for i, new_item in enumerate(new_prompts):
    old_url = bad_list[i]["img_url"]
    old_filename = old_url.split("/")[-1]
    if old_filename:
        old_filename_to_new_data[old_filename] = new_item

final_items = []
unique_prompts = set()
missing_src_count = 0
found_count = 0

for i in range(1, 641):
    # Find img tag for this index
    img_match = re.search(r'<img src="(.*?)" loading="lazy" alt="(.*?)" onclick="toggleError\(' + str(i) + r'\)">', html)
    prompt_match = re.search(r'<div id="prompt-data-' + str(i) + r'" style="display:none;">(.*?)</div>', html)
    
    if img_match and prompt_match:
        found_count += 1
        src = img_match.group(1)
        alt = img_match.group(2)
        old_prompt = prompt_match.group(1).strip()
        
        if not src:
            missing_src_count += 1
            continue # empty src, we didn't generate it earlier
            
        old_filename = src.split("/")[-1]
        
        if old_filename in old_filename_to_new_data:
            new_data = old_filename_to_new_data[old_filename]
            path = f"assets/images_gen_fixes/{new_data['filename']}"
            prompt = new_data['prompt']
        else:
            path = src.lstrip("./") 
            if src.startswith("poster_"):
                path = f"assets/covers/{src}" # fallback, earlier some were in root but actually should be somewhere? Wait, if they are in root, leave them.
                if not src.startswith("assets/covers"):
                    path = src
            prompt = old_prompt
            
        # Deduplicate
        if prompt not in unique_prompts:
            unique_prompts.add(prompt)
            final_items.append({
                "path": path,
                "prompt": prompt
            })

print(f"Total entries found: {found_count}")
print(f"Empty src skipped: {missing_src_count}")
print(f"Total unique concepts across ALL 640 posters after merge: {len(final_items)}")

with open("all_unique_posters.json", "w") as f:
    json.dump(final_items, f, ensure_ascii=False, indent=2)

