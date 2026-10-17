import json
import os
import sys

def get_next_10():
    with open("database_loi.json", "r") as f:
        db = json.load(f)
    items = db["posters"][:10]
    if not items:
        print("NO_ITEMS_LEFT")
        return

    with open("../tho.fedu.vn/data/poems.json", "r") as f:
        poems = {p["id"]: p for p in json.load(f)}

    champions = ["Darius (Noxian commander armor)", "Garen (Demacian knight armor)", "Xin Zhao (Seneschal spear armor)", "Jarvan IV (Demacian royal armor)", "Lee Sin (Blind monk martial arts garb)", "Yasuo (Wandering samurai armor)", "Yone (Demon hunter dual-sword armor)", "Shen (Twilight ninja armor)", "Zed (Shadow assassin armor)", "Talon (Noxian assassin hood and blades)", "Rengar (Primal hunter bone armor)", "KhaZix (Void predator carapace - humanoid adaptation)", "Lucian (Sentinel of Light trenchcoat)", "Graves (Outlaw shotgun mercenary gear)", "Twisted Fate (Gambler suit and magical hat)", "Sylas (Demacian rebellion chains)", "Pyke (Bloodharbor ripper spectral gear)", "Thresh (Chain warden spectral robes)", "Viego (Ruined King spectral armor)", "Aatrox (Darkin blade corrupted armor)", "Mordekaiser (Iron revenant massive armor)", "Sett (Ionian pit boss vest)", "Jayce (Piltover hextech inventor suit)", "Viktor (Zaunite machine herald augments)", "Ekko (Zaunite timeboy punk gear)", "Heimerdinger (Piltover eccentric inventor lab coat)", "Ezreal (Piltover explorer jacket)", "Taric (Aspect of the Protector crystalline armor)", "Pantheon (Targonian spartan armor)", "Braum (Freljordian muscular shield bearer gear)"]

    print("Please emit concurrent `generate_image` tool calls for the following 10 items:")
    for i, item in enumerate(items):
        poem = poems.get(item["id"])
        concept = poem.get("explanation", "") if poem else "Extreme focus and discipline"
        champ = champions[(hash(item["id"]) % len(champions))]
        champ_name = champ.split(" (")[0]
        champ_outfit = champ.split("(")[1].replace(")", "")
        
        prompt = f"A 35-year-old Vietnamese man cosplay as {champ_name} from League of Legends. OUTFIT: {champ_outfit}. ACTION: {concept[:120].strip()}. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads '{champ_name.upper()}' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k."
        
        print(f"\nItem ID: {item['id']}")
        print(f"ImageName: poster_{item['id'].replace('-', '_')}")
        print("ImagePaths: ['/Users/vietmac/Documents/CODE/Quản gia/assets/ava/viet_real_master_crop_005.jpg', '/Users/vietmac/Documents/CODE/Quản gia/assets/ava/viet_avatar_005.jpg']")
        print(f"Prompt: {prompt}")
        
        # Save prompt to temp
        with open(f"/tmp/prompt_{item['id']}.txt", "w") as f:
            f.write(prompt)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "get":
        get_next_10()
