import json
import random

dna_face = "Featuring a Vietnamese man with an oval face, high cheekbones, expressive Asian monolids, a radiant smile with upper teeth showing, and a signature spiky brush-up hairstyle. Khóa dáng mặt Oval, gò má cao, đuôi mắt mí lót Á Đông có hồn, kiểu tóc spiky brush-up đặc trưng."

anime_styles = [
    "Cyberpunk: Edgerunners Studio Trigger aesthetic", "Attack on Titan WIT Studio aesthetic", "Demon Slayer ufotable aesthetic",
    "Solo Leveling Webtoon aesthetic", "Akira 1988 classic anime aesthetic", "Ghost in the Shell Mamoru Oshii aesthetic",
    "JoJo's Bizarre Adventure Hirohiko Araki aesthetic", "Tokyo Ghoul Sui Ishida aesthetic", "Bleach Tite Kubo aesthetic",
    "One Punch Man Yusuke Murata aesthetic", "Neon Genesis Evangelion Hideaki Anno aesthetic", "Cowboy Bebop Shinichiro Watanabe aesthetic",
    "Dragon Ball Z Akira Toriyama aesthetic", "Naruto Shippuden Masashi Kishimoto aesthetic", "Hunter x Hunter Yoshihiro Togashi aesthetic",
    "Fullmetal Alchemist Brotherhood Hiromu Arakawa aesthetic", "Berserk Kentaro Miura aesthetic", "Vagabond Takehiko Inoue aesthetic",
    "Vinland Saga Makoto Yukimura aesthetic", "Fate/Stay Night ufotable aesthetic", "Sword Art Online A-1 Pictures aesthetic",
    "Mob Psycho 100 Studio Bones aesthetic", "Death Note Takeshi Obata aesthetic", "Code Geass Sunrise aesthetic",
    "Steins;Gate White Fox aesthetic", "Black Clover Yuki Tabata aesthetic", "Tengen Toppa Gurren Lagann Hiroyuki Imaishi aesthetic",
    "Hellsing Ultimate Kohta Hirano aesthetic", "Kill la Kill Studio Trigger aesthetic", "Promare Studio Trigger aesthetic",
    "Princess Mononoke Studio Ghibli aesthetic", "Your Name Makoto Shinkai aesthetic", "Nausicaa of the Valley of the Wind aesthetic",
    "Jin-Roh: The Wolf Brigade aesthetic", "Blame! Tsutomu Nihei aesthetic", "Gantz Hiroya Oku aesthetic", "Dorohedoro Q Hayashida aesthetic",
    "Gundam Mobile Suit aesthetic", "Samurai Champloo aesthetic", "Afro Samurai aesthetic", "Trigun Yasuhiro Nightow aesthetic",
    "Castlevania Netflix aesthetic", "Arcane Fortiche aesthetic", "Spider-Man: Into the Spider-Verse aesthetic"
]

outfits = [
    "wearing a sleek futuristic techwear jacket with glowing neon accents",
    "wearing a traditional Japanese samurai kimono with intricate golden embroidery",
    "wearing a heavy mechanical combat exo-suit with battle damage",
    "wearing an elegant gothic vampire aristocrat tailcoat",
    "wearing a post-apocalyptic scavenger leather duster with goggles",
    "wearing a tactical cyberpunk mercenary stealth suit",
    "wearing a high-fantasy knight's silver armor with a flowing cape",
    "wearing a dark academy student uniform with a mysterious crest",
    "wearing a minimalist sci-fi astronaut flight suit",
    "wearing a highly stylized yakuza boss tailored suit with an overcoat draped over the shoulders",
    "wearing a martial arts master's simple black gi with hand wraps",
    "wearing a steampunk inventor's brass-buttoned vest with leather holsters"
]

actions = [
    "standing defiantly amidst a crumbling city under a blood-red moon",
    "wielding a glowing energy katana while rain pours down in a cyberpunk alley",
    "floating in mid-air surrounded by shattered glass and anti-gravity debris",
    "unleashing a massive aura of blue flame that warps the air around him",
    "sitting on a gargoyle overlooking a sprawling futuristic megalopolis",
    "walking slowly away from a massive cinematic explosion in slow motion",
    "holding a mysterious glowing artifact that illuminates his face in the dark",
    "striking a dynamic, gravity-defying combat pose with dynamic perspective",
    "gazing confidently at a colossal mecha robot towering in the background",
    "standing in a serene zen garden where cherry blossoms are caught in a magical whirlwind"
]

lighting = [
    "dramatic chiaroscuro lighting", "neon synthwave lighting", "golden hour cinematic sunlight",
    "eerie bioluminescent glow", "harsh strobe lights", "ethereal moonlight", "moody volumetric fog lighting"
]

with open("fix_progress.json", "r") as f:
    progress = set(json.load(f))

with open("bad_prompts_list.json", "r") as f:
    bad_list = json.load(f)

remaining = [item for item in bad_list if item["img_url"] not in progress]
num_remaining = len(remaining)

# Generate unique combinations
generated = set()
prompts = []
random.seed(42) # For reproducibility

while len(prompts) < num_remaining:
    style = random.choice(anime_styles)
    outfit = random.choice(outfits)
    action = random.choice(actions)
    light = random.choice(lighting)
    
    combo = (style, outfit, action, light)
    if combo not in generated:
        generated.add(combo)
        
        prompt_text = f"{dna_face} {style}. {outfit}, {action}. {light}, highly detailed, 8k resolution, masterpiece, dynamic angle, vibrant colors. 9:16 vertical poster layout."
        title = style.split(' aesthetic')[0]
        prompts.append({
            "title": title,
            "prompt": prompt_text,
            "filename": remaining[len(prompts)]["img_url"].split("/")[-1]
        })

# Write to markdown
with open("298_anime_ideas.md", "w") as f:
    f.write(f"# 298 Ý Tưởng Concept Manga/Anime Mới\n\n")
    f.write(f"Dưới đây là {num_remaining} prompt siêu đa dạng, không trùng lặp, chuyên biệt cho Anime/Manga và đã được tích hợp Face DNA của anh.\n\n")
    
    for i, p in enumerate(prompts):
        f.write(f"## {i+1}. {p['title']}\n")
        f.write(f"**Tệp ảnh đích:** `{p['filename']}`\n\n")
        f.write(f"**Prompt:**\n```\n{p['prompt']}\n```\n\n")

# Also save to a JSON so we can easily swap it into our current workflow!
with open("new_anime_prompts.json", "w") as f:
    json.dump(prompts, f, indent=2, ensure_ascii=False)

print(f"Generated 298 ideas into 298_anime_ideas.md and new_anime_prompts.json")
