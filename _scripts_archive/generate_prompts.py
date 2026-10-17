import json
import re

champions = [
    ("Garen", "Demacian knight armor"), ("Darius", "Noxian commander armor"), 
    ("Xin Zhao", "Seneschal spearman armor"), ("Jarvan IV", "Demacian royal golden armor"),
    ("Lee Sin", "Monk martial arts attire"), ("Yasuo", "Wandering samurai armor"),
    ("Yone", "Demon hunter dual sword armor"), ("Shen", "Twilight ninja armor"),
    ("Zed", "Shadow assassin armor"), ("Talon", "Noxian assassin cloak"),
    ("Rengar", "Primal hunter bone armor"), ("Kha'Zix", "Void reaver carapace"),
    ("Lucian", "Purifier gunslinger coat"), ("Graves", "Outlaw mercenary gear"),
    ("Twisted Fate", "Gambler suit and magical hat"), ("Sylas", "Demacian rebellion chains"),
    ("Pyke", "Bloodharbor ripper spectral gear"), ("Thresh", "Chain warden spectral robes"),
    ("Viego", "Ruined King spectral armor"), ("Aatrox", "Darkin warlord demonic armor"),
    ("Mordekaiser", "Iron revenant warlord armor"), ("Sett", "Ionian pit boss vest"),
    ("Jayce", "Piltover inventor hextech suit"), ("Viktor", "Zaunite machine herald augments"),
    ("Ekko", "Zaunite time-breaker street gear"), ("Heimerdinger", "Piltover scientist lab coat"),
    ("Ezreal", "Piltover explorer jacket"), ("Taric", "Targonian protector crystal armor"),
    ("Pantheon", "Targonian spartan warrior armor"), ("Braum", "Freljordian winter shieldbearer gear")
]

with open('database_loi.json', 'r') as f:
    data = json.load(f)
    
with open('/Users/vietmac/Documents/CODE/tho.fedu.vn/data/poems.json', 'r') as f:
    poems = {p['id']: p for p in json.load(f)}

batch = data['posters'][:30]

import sys
subagents = []

for i, p in enumerate(batch):
    id = p['id']
    champ, outfit = champions[i % len(champions)]
    poem_data = poems.get(id, {})
    concept = poem_data.get('explanation', '').replace('\n', ' ')[:150]
    concept = re.sub(r'[^a-zA-Z0-9\sÀ-ỹ]', '', concept) # Remove special chars to avoid breaking JSON
    if not concept: concept = "Standing powerfully in a cinematic environment, glowing with intense energy and mastery"
    
    prompt = f"A 35-year-old Vietnamese man cosplay as {champ} from League of Legends. OUTFIT: {outfit}. ACTION: {concept}. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads '{champ.upper()}' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k."
    
    with open(f"/tmp/prompt_{id}.txt", "w") as pf:
        pf.write(prompt)
        
    subagents.append({
        "Model": "flash",
        "Role": f"Gen {id}",
        "TypeName": "self",
        "Prompt": f"Generate a movie poster for ID `{id}`.\n1. Call `generate_image` tool with:\nImageName: `poster_{id.replace('-', '_')}`\nImagePaths: `['/Users/vietmac/Documents/CODE/Quản gia/assets/ava/viet_real_master_crop_005.jpg', '/Users/vietmac/Documents/CODE/Quản gia/assets/ava/viet_avatar_005.jpg']`\nPrompt: `{prompt}`\n2. Run bash: `cwebp -q 80 <generated_jpg> -o /tmp/poster_{id}.webp`\n3. Run bash: `rclone copyto /tmp/poster_{id}.webp r2:vietndjmedia/k_covers/poster_{id}.webp`\n4. Use send_message to reply to me with 'DONE'."
    })

# Output JSON string that can be used directly for invoke_subagent tool
print(json.dumps(subagents))
