import re
import json

with open("nghiem_thu_640_posters.html", "r") as f:
    html = f.read()

# Find all blocks like:
# <img src="./assets/covers/poster_351_co_hau_gai.jpg" loading="lazy" alt="Star Trek Picard" onclick="toggleError(585)">
# <div id="prompt-data-585" style="display:none;">...</div>

img_pattern = re.compile(r'<img src="\.(/assets/covers/.*?)" loading="lazy" alt="(.*?)" onclick="toggleError\((\d+)\)">.*?<div id="prompt-data-\3" style="display:none;">(.*?)</div>', re.DOTALL)
matches = img_pattern.findall(html)

print(f"Found {len(matches)} posters in nghiem_thu_640_posters.html")

# Now, we also need to load the mapping of bad ones.
# The `fix_progress.json` and `new_anime_prompts.json` tell us about the fixed ones.
# Let's map original img_url to the new filename and new prompt.
with open("bad_prompts_list.json", "r") as f:
    bad_list = json.load(f)

# old_url -> old_filename (like poster_351_co_hau_gai.jpg)
bad_url_to_old_filename = {}
for b in bad_list:
    # b["img_url"] is like https://pub-.../poster_351_co_hau_gai.jpg
    filename = b["img_url"].split("/")[-1]
    bad_url_to_old_filename[b["img_url"]] = filename

# We also know bad_prompts_list has the same length as new_anime_prompts?
# Yes, they were 1:1 mapping in the script that generated them.
with open("new_anime_prompts.json", "r") as f:
    new_prompts = json.load(f)

old_filename_to_new_data = {}
for i, new_item in enumerate(new_prompts):
    old_url = bad_list[i]["img_url"]
    old_filename = old_url.split("/")[-1]
    old_filename_to_new_data[old_filename] = new_item

final_items = []
unique_prompts = set()

for match in matches:
    original_path, alt_text, idx, old_prompt = match
    old_filename = original_path.split("/")[-1]
    
    # If this was one of the bad ones, use the fixed version
    if old_filename in old_filename_to_new_data:
        new_data = old_filename_to_new_data[old_filename]
        path = f"assets/images_gen_fixes/{new_data['filename']}"
        prompt = new_data['prompt']
    else:
        # Keep the original
        path = original_path.lstrip("/") # remove leading /
        prompt = old_prompt.strip()

    if prompt not in unique_prompts:
        unique_prompts.add(prompt)
        final_items.append({
            "path": path,
            "prompt": prompt
        })

print(f"Total unique concepts across ALL 640 posters after merge: {len(final_items)}")

with open("all_unique_posters.json", "w") as f:
    json.dump(final_items, f, ensure_ascii=False, indent=2)

