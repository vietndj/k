import json
import os

with open("database_loi.json", "r") as f:
    db = json.load(f)

# Get top 30
items = db["posters"][:30]

print(f"Next 30 items: {len(items)}")

# We'll use the male champions list and poem data to build prompts
with open("../tho.fedu.vn/data/poems.json", "r") as f:
    poems = json.load(f)

poem_dict = {p["id"]: p for p in poems}

# Mapping champs
champions = [
    "Darius (Noxian commander armor)", "Garen (Demacian knight armor)", "Xin Zhao (Seneschal spear armor)", 
    "Jarvan IV (Demacian royal armor)", "Lee Sin (Blind monk martial arts garb)", "Yasuo (Wandering samurai armor)", 
    "Yone (Demon hunter dual-sword armor)", "Shen (Twilight ninja armor)", "Zed (Shadow assassin armor)", 
    "Talon (Noxian assassin hood and blades)", "Rengar (Primal hunter bone armor)", "KhaZix (Void predator carapace - humanoid adaptation)", 
    "Lucian (Sentinel of Light trenchcoat)", "Graves (Outlaw shotgun mercenary gear)", "Twisted Fate (Gambler suit and magical hat)", 
    "Sylas (Demacian rebellion chains)", "Pyke (Bloodharbor ripper spectral gear)", "Thresh (Chain warden spectral robes)", 
    "Viego (Ruined King spectral armor)", "Aatrox (Darkin blade corrupted armor)", "Mordekaiser (Iron revenant massive armor)", 
    "Sett (Ionian pit boss vest)", "Jayce (Piltover hextech inventor suit)", "Viktor (Zaunite machine herald augments)", 
    "Ekko (Zaunite timeboy punk gear)", "Heimerdinger (Piltover eccentric inventor lab coat)", "Ezreal (Piltover explorer jacket)", 
    "Taric (Aspect of the Protector crystalline armor)", "Pantheon (Targonian spartan armor)", "Braum (Freljordian muscular shield bearer gear)",
    "Tryndamere (Freljordian barbarian king fur)", "Olaf (Freljordian berserker axes)", "Udyr (Freljordian spirit walker shaman wraps)", 
    "Volibear (Freljordian demigod shamanic runic armor)", "Ornn (Freljordian forge god blacksmith apron)", 
    "Swain (Noxian grand general demonic coat)", "Vladimir (Noxian hemomancer aristocratic suit)", "Draven (Noxian executioner gladiator armor)", 
    "Sion (Noxian undead juggernaut brutal armor)", "Urgot (Zaunite dreadnought chemtech enhancements)"
]

out = []

for i, item in enumerate(items):
    poem = poem_dict.get(item["id"])
    concept = poem.get("explanation", "") if poem else "Extreme focus and discipline"
    champ = champions[i % len(champions)]
    champ_name = champ.split(" (")[0]
    champ_outfit = champ.split("(")[1].replace(")", "")
    
    prompt = f"A 35-year-old Vietnamese man cosplay as {champ_name} from League of Legends. OUTFIT: {champ_outfit}. ACTION: {concept[:120].strip()}. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads '{champ_name.upper()}' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k."
    
    # Save prompt to temp
    with open(f"/tmp/prompt_{item['id']}.txt", "w") as f:
        f.write(prompt)
        
    out.append({
        "id": item["id"],
        "champ": champ_name,
        "prompt": prompt
    })

with open("next_batch_data.json", "w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("Saved next_batch_data.json")
