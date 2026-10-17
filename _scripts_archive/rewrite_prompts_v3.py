import json

with open("new_cotrang_prompts.json", "r") as f:
    prompts = json.load(f)

for p in prompts:
    old_prompt = p["prompt"]
    
    # Extract clothing
    import re
    match = re.search(r'He is wearing (.*?)\.', old_prompt)
    clothing = match.group(1).strip() if match else "traditional Asian historical drama attire"
    
    title = p["title"].upper()
    
    new_prompt = f"""a handsome 30s Vietnamese man with short neat textured modern fringe haircut, lean sculpted chiseled face, defined sharp jawline, slim lean cheeks with high cheekbones, athletic lean runner build, expressive almond-shaped dark Asian eyes, authentic Asian facial features. He is smiling radiantly. He is wearing {clothing}. Highly detailed, 8k, photorealistic.
TEXT ON POSTER: "{title}"
CRITICAL RULES:
1. DO NOT print any fake director or actor names.
2. DO NOT print any visual descriptions.
3. ONLY print the exact words in "TEXT ON POSTER"."""

    p["prompt"] = new_prompt

with open("new_cotrang_prompts_v3.json", "w") as f:
    json.dump(prompts, f, indent=4, ensure_ascii=False)

print(f"Rewrote {len(prompts)} prompts to V3.")
