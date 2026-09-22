import json
import re

with open("new_cotrang_prompts.json", "r") as f:
    prompts = json.load(f)

for p in prompts:
    old_prompt = p["prompt"]
    
    # Extract clothing and aesthetic
    match = re.search(r'He is wearing (.*?) highly detailed', old_prompt)
    clothing_aesthetic = match.group(1).strip().replace(" aesthetic,", "") if match else "traditional Asian historical drama attire"
    
    title = p["title"].upper()
    
    new_prompt = f"""A cinematic movie poster.
TEXT ON POSTER: "{title}"
VISUAL DESCRIPTION: A Vietnamese man with an oval face, high cheekbones, expressive Asian monolids, a radiant smile with upper teeth showing, and a signature spiky brush-up hairstyle. He is wearing {clothing_aesthetic}. Highly detailed, cinematic lighting, 8k resolution, photorealistic, dramatic atmosphere.
CRITICAL RULES:
1. DO NOT print the "VISUAL DESCRIPTION" text on the poster.
2. DO NOT print any fake director or actor names (No billing blocks).
3. ONLY print the exact words in "TEXT ON POSTER"."""

    p["prompt"] = new_prompt

with open("new_cotrang_prompts_v2.json", "w") as f:
    json.dump(prompts, f, indent=4, ensure_ascii=False)

print(f"Rewrote {len(prompts)} prompts.")
