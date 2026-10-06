import json

prompts = {
    'tho-0835': "A 35-year-old Vietnamese man cosplay as Lee Sin from League of Legends. OUTFIT: Monk martial arts attire. ACTION: Peacefully meditating with panoramic vision (180 degrees) activated to lower heart rate and reduce stress. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads 'LEE SIN' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k.",
    'tho-0834': "A 35-year-old Vietnamese man cosplay as Caitlyn from League of Legends. OUTFIT: Piltover sniper uniform. ACTION: Intensely focused, aiming through a sniper scope to physically lock visual target and activate sharp focus. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads 'CAITLYN' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k.",
    'tho-0833': "A 35-year-old Vietnamese man cosplay as Amumu from League of Legends. OUTFIT: Mummy bandages. ACTION: Sitting sadly in a dark corner, waiting for 15 minutes of extreme boredom as a ritual to enter the flow state. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads 'AMUMU' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k.",
    'tho-0832': "A 35-year-old Vietnamese man cosplay as Master Yi from League of Legends. OUTFIT: Ionian swordsman armor. ACTION: Glowing with intense focus in the ultimate Flow State, completely immersed in the moment with heightened dopamine. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads 'MASTER YI' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k.",
    'tho-0831': "A 35-year-old Vietnamese man cosplay as Shen from League of Legends. OUTFIT: Twilight ninja armor. ACTION: Balancing dual glowing energy swords in perfect harmony, saving brain energy to reach ultimate concentration. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads 'SHEN' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k.",
    'tho-0830': "A 35-year-old Vietnamese man cosplay as Rengar from League of Legends. OUTFIT: Primal hunter bone armor. ACTION: Hunting invisible digital prey in a cybernetic jungle, desperately seeking a climax of dopamine but finding emptiness. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads 'RENGAR' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k.",
    'tho-0829': "A 35-year-old Vietnamese man cosplay as Twisted Fate from League of Legends. OUTFIT: Gambler suit and magical hat. ACTION: Throwing glowing magical cards in a casino of endless scrolling videos, representing the addictive reward prediction error. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads 'TWISTED FATE' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k.",
    'tho-0828': "A 35-year-old Vietnamese man cosplay as Jhin from League of Legends. OUTFIT: Theatrical assassin armor. ACTION: Standing at the absolute pinnacle of perfection on a grand stage, realizing that reaching the climax makes dopamine instantly vanish. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads 'JHIN' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k.",
    'tho-0827': "A 35-year-old Vietnamese man cosplay as Tahm Kench from League of Legends. OUTFIT: River King swamp mafia coat. ACTION: Sitting at a lavish banquet, devouring infinite food with a bottomless craving, representing that dopamine is endless hunger, not the reward itself. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads 'TAHM KENCH' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k.",
    'tho-0826': "A 35-year-old Vietnamese man cosplay as Yasuo from League of Legends. OUTFIT: Wandering samurai armor. ACTION: Standing peacefully in a gentle breeze, letting go of all emotional burdens without forcefully suppressing them, achieving true mastery. TYPOGRAPHY: Huge bold glowing cinematic movie poster text that reads 'YASUO' at the bottom of the image. BIOMETRIC LOCK: Oval face shape, high cheekbones, soulful Asian monolid eyes. Face MUST perfectly match reference images. DO NOT morph. HAIR & BEARD LOCK: clean-shaven, NO beard, NO mustache. STYLE: Hyper-realistic cinematic photography, movie poster style, 8k."
}

# Update database.json
with open('database.json', 'r') as f:
    data = json.load(f)

for p in data['posters']:
    if p['id'] in prompts:
        p['prompt'] = prompts[p['id']]
        p['has_prompt'] = True

with open('database.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Remove the 10 fixed images from database_loi.json
with open('database_loi.json', 'r') as f:
    data_loi = json.load(f)

new_posters = [p for p in data_loi['posters'] if p['id'] not in prompts]
data_loi['posters'] = new_posters
data_loi['metadata']['total_images'] = len(new_posters)

with open('database_loi.json', 'w') as f:
    json.dump(data_loi, f, indent=2, ensure_ascii=False)

print(f"Fixed {len(prompts)} images. Remaining bad images: {len(new_posters)}")
