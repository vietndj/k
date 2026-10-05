import json
import random

# Load the json
with open('/Users/vietmac/Documents/CODE/k/missing_thumbnails_355.json', 'r') as f:
    articles = json.load(f)

# Define the lists
netflix = [
    "Squid Game", "Stranger Things", "Peaky Blinders", "Breaking Bad", "Better Call Saul",
    "Money Heist", "Black Mirror", "Dark", "Queen's Gambit", "Narcos",
    "Mindhunter", "The Witcher", "Lucifer", "Ozark", "Wednesday",
    "Arcane", "Love Death & Robots", "The Crown", "Bridgerton", "House of Cards",
    "The Boys", "Game of Thrones", "Succession", "True Detective", "Westworld",
    "The Mandalorian", "Loki", "WandaVision", "Chernobyl", "Band of Brothers",
    "Fargo", "The Sopranos", "The Wire", "Mad Men", "Sherlock",
    "Black Sails", "Vikings", "The Last Kingdom", "Spartacus", "Rome",
    "The Expanse", "Altered Carbon", "Sense8", "Orphan Black", "Fringe",
    "Mr. Robot", "Silicon Valley", "Halt and Catch Fire", "Severance", "Ted Lasso",
    "Yellowstone", "Billions", "Suits", "White Collar", "Dexter",
    "Hannibal", "Bates Motel", "You", "The Fall", "Broadchurch",
    "Mare of Easttown", "True Blood", "The Walking Dead", "The Last of Us", "Fallout",
    "Silo", "Foundation", "The Wheel of Time", "Rings of Power", "Shadow and Bone",
    "Umbrella Academy", "Doom Patrol", "Daredevil", "Punisher", "Jessica Jones",
    "Sense8", "The OA", "1899", "Snowpiercer", "Alice in Borderland",
    "Sweet Home", "All of Us Are Dead", "Hellbound", "Kingdom", "My Name",
    "Vincenzo", "Crash Landing on You", "Itaewon Class", "Reply 1988"
]

anime = [
    "Dragon Ball", "One Piece", "Naruto", "Bleach", "Attack on Titan",
    "Death Note", "Fullmetal Alchemist", "Hunter x Hunter", "Demon Slayer", "Jujutsu Kaisen",
    "Chainsaw Man", "Berserk", "Slam Dunk", "Monster", "Vinland Saga",
    "Cowboy Bebop", "Steins;Gate", "Tokyo Ghoul", "One Punch Man", "My Hero Academia",
    "Haikyuu", "Kuroko no Basket", "Blue Lock", "Sword Art Online", "Re:Zero",
    "Mushoku Tensei", "No Game No Life", "Code Geass", "Evangelion", "Gundam",
    "Mob Psycho 100", "Spy x Family", "Kaguya-sama", "Frieren", "Oshi no Ko",
    "Solo Leveling", "Tower of God", "God of High School", "Tokyo Revengers", "Erased",
    "Parasyte", "Psycho-Pass", "Ghost in the Shell", "Akira", "Perfect Blue",
    "Paprika", "Your Name", "Weathering With You", "Suzume", "A Silent Voice",
    "Violet Evergarden", "Clannad", "Your Lie in April", "Angel Beats", "Anohana",
    "Fate/Stay Night", "Fate/Zero", "Black Clover", "Fairy Tail", "Seven Deadly Sins",
    "Gintama", "JoJo's Bizarre Adventure", "Dr. Stone", "Fire Force", "Soul Eater",
    "D.Gray-man", "Inuyasha", "Yu Yu Hakusho", "Rurouni Kenshin", "Shaman King",
    "Yu-Gi-Oh!", "Pokemon", "Digimon", "Beyblade", "Bakugan",
    "Sailor Moon", "Cardcaptor Sakura", "Madoka Magica", "Kill la Kill", "Gurren Lagann",
    "Promare", "Cyberpunk: Edgerunners", "Devilman Crybaby", "Castlevania", "Blood of Zeus",
    "Dorohedoro", "Beastars", "Baki", "Kengan Ashura", "Record of Ragnarok",
    "Made in Abyss", "The Promised Neverland", "Death Parade", "Terror in Resonance"
]

animation = [
    "Wall-E", "Up", "Coco", "Spider-Man: Into the Spider-Verse", "Ratatouille",
    "Kung Fu Panda", "How to Train Your Dragon", "Shrek", "Toy Story", "The Lion King",
    "Finding Nemo", "The Incredibles", "Inside Out", "Zootopia", "Moana",
    "Frozen", "Tangled", "Big Hero 6", "Wreck-It Ralph", "Aladdin",
    "Beauty and the Beast", "Mulan", "Tarzan", "Hercules", "The Little Mermaid",
    "Spider-Man: Across the Spider-Verse", "Puss in Boots: The Last Wish", "The Bad Guys", "The Mitchells vs. the Machines", "Klaus",
    "Soul", "Luca", "Turning Red", "Encanto", "Raya and the Last Dragon",
    "Brave", "Monsters, Inc.", "A Bug's Life", "Cars", "The Good Dinosaur",
    "Despicable Me", "Minions", "Sing", "The Secret Life of Pets", "Ice Age",
    "Rio", "Ferdinand", "Spies in Disguise", "Epic", "Robots",
    "Megamind", "Madagascar", "Over the Hedge", "Bee Movie", "Shark Tale",
    "Chicken Run", "Wallace & Gromit", "Coraline", "Kubo and the Two Strings", "ParaNorman",
    "The Boxtrolls", "Missing Link", "The Nightmare Before Christmas", "Corpse Bride", "Frankenweenie",
    "Spider-Man", "Batman: The Animated Series", "Justice League", "Teen Titans", "Avatar: The Last Airbender",
    "The Legend of Korra", "Samurai Jack", "The Powerpuff Girls", "Dexter's Laboratory", "Johnny Bravo",
    "Courage the Cowardly Dog", "Ed, Edd n Eddy", "Regular Show", "Adventure Time", "Steven Universe",
    "The Amazing World of Gumball", "Gravity Falls", "Phineas and Ferb", "Kim Possible", "Danny Phantom",
    "SpongeBob SquarePants", "The Fairly OddParents", "Jimmy Neutron", "Avatar", "Ben 10"
]

vietnamese = [
    "Bố Già", "Mai", "Hai Phượng", "Mắt Biếc", "Em Chưa 18",
    "Lật Mặt", "Tôi Thấy Hoa Vàng Trên Cỏ Xanh", "Đất Rừng Phương Nam", "Người Phán Xử", "Đêm Tối Rực Rỡ",
    "Tro Tàn Rực Rỡ", "Tiệc Trăng Máu", "Nhà Bà Nữ", "Cua Lại Vợ Bầu", "Gái Già Lắm Chiêu",
    "Chị Chị Em Em", "Mùi Đu Đủ Xanh", "Áo Lụa Hà Đông", "Dòng Máu Anh Hùng", "Bẫy Rồng",
    "Thiên Mệnh Anh Hùng", "Quả Tim Máu", "Scandal", "Cô Gái Đến Từ Hôm Qua", "Tháng Năm Rực Rỡ",
    "Trạng Tí", "Bằng Chứng Vô Hình", "Bóng Đè", "Thất Sơn Tâm Linh", "Kẻ Ăn Hồn",
    "Tết Ở Làng Địa Ngục", "Hương Ga", "Hài Tết", "Táo Quân", "Chuyện Xóm Tui",
    "Nắng", "Trạng Quỳnh", "Siêu Sao Siêu Ngố", "Chàng Vợ Của Em", "Hồn Papa Da Con Gái",
    "Ông Ngoại Tuổi 30", "Em Là Bà Nội Của Anh", "Cô Ba Sài Gòn", "Song Lang", "Sài Gòn Yo!",
    "Bụi Đời Chợ Lớn", "Ròm", "Vị", "Bi, Đừng Sợ", "Chơi Vơi",
    "Đập Cánh Giữa Không Trung", "Người Vợ Ba", "Cha Cõng Con", "Kiều", "Cậu Vàng",
    "Người Bất Tử", "Lôi Báo", "Mẹ Chồng", "Tấm Cám: Chuyện Chưa Kể", "Thanh Sói",
    "Furies", "Mười", "Oan Hồn", "Chung Cư Ma", "Lời Nguyền Huyết Ngải",
    "Đoạt Hồn", "Cô Hầu Gái", "Ngôi Nhà Trong Hẻm", "Quỷ Cẩu", "Kẻ Ẩn Danh",
    "Người Mặt Trời", "Chị Mười Ba", "Nghề Siêu Dễ", "Dân Chơi Không Sợ Con Rơi", "Siêu Lừa Gặp Siêu Lầy",
    "Con Nhót Mót Chồng", "Kẻ Độc Hành", "Biệt Đội Rất Ổn", "Vô Diện Sát Nhân", "Mười: Lời Nguyền Trở Lại",
    "Cô Gái Từ Quá Khứ", "Hạnh Phúc Máu", "Đảo Độc Đắc", "Trịnh Công Sơn", "Em Và Trịnh"
]

# Ensure uniqueness and sufficient length
all_movies = []
genres = ['Netflix/Series', 'Anime/Manga', 'Animation', 'Vietnamese Film']
pools = [netflix, anime, animation, vietnamese]

# Deduplicate
for i in range(4):
    pools[i] = list(set(pools[i]))
    random.shuffle(pools[i])

mapping = []
index = 256
for i, article in enumerate(articles):
    category_idx = i % 4
    movie = pools[category_idx].pop(0) if pools[category_idx] else f"Custom Idea {i}"
    
    # Generate generic visual script and prompt
    title = article.get('title', '')
    genre = genres[category_idx]
    
    visual_script = f"A cinematic poster inspired by {movie} blending with the theme of: '{title}'. The composition features dynamic lighting, striking typography, and a central metaphorical visual that captures the core essence of the article."
    prompt = f"Movie poster style, {movie} aesthetic, highly detailed, cinematic lighting, 8k resolution, photorealistic, dramatic atmosphere, typography layout, concept art for '{title}'."
    
    mapping.append({
        "index": index,
        "movie": movie,
        "genre": genre,
        "target_html": article.get("filename"),
        "target_title": title,
        "visual_script": visual_script,
        "prompt": prompt
    })
    index += 1

# Write JSON
with open('/Users/vietmac/Documents/CODE/k/movie_posters_tasks_355.json', 'w') as f:
    json.dump(mapping, f, indent=2, ensure_ascii=False)

# Write Markdown
md_content = "# Báo Cáo Ánh Xạ 355 Poster Bài Viết\n\n"
md_content += "Danh sách 355 bài viết đã được phân bổ đồng đều vào 4 nhóm chủ đề điện ảnh:\n\n"
md_content += "| Index | Tác Phẩm | Phân Loại | Bài Viết |\n"
md_content += "|---|---|---|---|\n"

for item in mapping:
    md_content += f"| {item['index']} | {item['movie']} | {item['genre']} | {item['target_title']} |\n"

with open('/Users/vietmac/.gemini/antigravity/brain/432cfc5a-d34b-4005-9ce2-f6d3b5655fb7/mapping_report.md', 'w') as f:
    f.write(md_content)

print("Done generating files!")
