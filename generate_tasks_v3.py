import json
import re
import os
import random
from bs4 import BeautifulSoup

def extract_title(html_path):
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            title = soup.title.string if soup.title else ""
            if not title:
                h1 = soup.find("h1")
                if h1: title = h1.text
            if title:
                return title.replace(" - fedu.vn", "").replace("\n", " ").strip()
    except:
        pass
    return "Khám Phá Tri Thức - Mentor Nguyễn Đức Việt"

# Load existing tasks to check what's already used
with open("movie_posters_tasks_355.json", "r") as f: old_tasks = json.load(f)
used_movies = set([t["movie"].lower().strip() for t in old_tasks])

with open("failed_r2.txt", "r") as f: failed_urls = set([l.strip() for l in f if l.strip()])
with open("generate_manifest.py", "r", encoding="utf-8") as f: content = f.read()
mapping = dict(re.findall(r"\"([^\"]+\.html)\"\s*:\s*\"([^\"]+)\"", content))

# Also add the ones from R2 mapping to used_movies (except failed ones)
for html, url in mapping.items():
    if url not in failed_urls:
        basename = url.split("/")[-1].replace("poster_", "").replace(".jpg", "").replace("_", " ").title().strip()
        used_movies.add(basename.lower())

with open("missing_posters_report.json", "r") as f: missing = set(json.load(f))
tasks_htmls = set([t["target_html"] for t in old_tasks])
missing_not_in_tasks = list(missing - tasks_htmls)

# Combine all htmls that need new tasks
htmls_to_process = []
for html, url in mapping.items():
    if url in failed_urls:
        htmls_to_process.append(html)
htmls_to_process.extend(missing_not_in_tasks)

# Generate a large pool of unique fresh movies/series (285 items)
fresh_movies_pool = [
    "Dune Part Two", "Furiosa A Mad Max Saga", "Civil War", "Godzilla Minus One", "Spider-Man Across the Spider-Verse",
    "The Batman", "Everything Everywhere All at Once", "Poor Things", "The Boy and the Heron", 
    "Avatar The Way of Water", "Top Gun Maverick", "Nope", "Challengers", "Megalopolis", 
    "Kalki 2898 AD", "Kingdom of the Planet of the Apes", "Alien Romulus", "Inside Out 2",
    "The Creator", "Society of the Snow", "Ferrari", "Killers of the Flower Moon", "Napoleon",
    "The Killer", "Saltburn", "Anatomy of a Fall", "Past Lives", "Spider-Man No Way Home",
    "Asteroid City", "Beau Is Afraid", "Talk to Me", "Mission Impossible Dead Reckoning",
    "John Wick Chapter 4", "The Super Mario Bros Movie", "Creed III", "Air", "Tetris",
    "Dungeons and Dragons Honor Among Thieves", "Guardians of the Galaxy Vol 3", "Fast X",
    "Indiana Jones and the Dial of Destiny", "Barbie Movie", "The Marvels", "The Hunger Games Ballad of Songbirds and Snakes",
    "Wonka", "Aquaman and the Lost Kingdom", "Blue Beetle", "Transformers Rise of the Beasts",
    "The Flash", "Elemental", "Teenage Mutant Ninja Turtles Mutant Mayhem", "The Nun II",
    "Saw X", "Five Nights at Freddys", "The Equalizer 3", "A Haunting in Venice", "The Exorcist Believer",
    "Killers of the Flower Moon", "The Holdovers", "American Fiction", "The Zone of Interest",
    "Maestro", "Rustin", "Nyad", "The Color Purple", "The Iron Claw", "Ferrari", "The Boys Series",
    "Gen V", "Loki Season 2", "Secret Invasion", "Ahsoka", "The Mandalorian Season 3", "Andor",
    "The Last of Us HBO", "Succession", "The Bear", "Beef", "Severance", "Silo", "Foundation",
    "The Witcher", "Stranger Things", "Black Mirror", "Peaky Blinders", "Better Call Saul",
    "House of the Dragon", "The Lord of the Rings The Rings of Power", "The Wheel of Time",
    "Shadow and Bone", "The Sandman", "Wednesday", "Squid Game", "Alice in Borderland",
    "All of Us Are Dead", "Hellbound", "Sweet Home", "Money Heist", "Lupin", "Dark",
    "1899", "The Queen's Gambit", "The Crown", "Bridgerton", "The Marvelous Mrs Maisel",
    "Ted Lasso", "Shrinking", "The Morning Show", "For All Mankind", "Severance", "Silo",
    "Foundation", "Invasion", "Monarch Legacy of Monsters", "The Continental", "Fargo",
    "True Detective Night Country", "The White Lotus", "Euphoria", "Yellowstone", "1923",
    "1883", "Tulsa King", "Mayor of Kingstown", "Special Ops Lioness", "Halo", "Star Trek Strange New Worlds",
    "Star Trek Picard", "Star Trek Discovery", "Doctor Who", "Black Mirror", "Love Death and Robots",
    "Arcane", "Cyberpunk Edgerunners", "Castlevania", "Blood of Zeus", "Invincible",
    "The Legend of Vox Machina", "Blue Eye Samurai", "Pluto", "Attack on Titan", "Demon Slayer",
    "Jujutsu Kaisen", "Chainsaw Man", "Spy x Family", "My Hero Academia", "One Piece Live Action",
    "Cowboy Bebop", "Neon Genesis Evangelion", "Akira", "Ghost in the Shell", "Princess Mononoke",
    "Spirited Away", "Howl's Moving Castle", "Your Name", "Weathering with You", "Suzume",
    "A Silent Voice", "Grave of the Fireflies", "The Wind Rises", "Ponyo", "My Neighbor Totoro",
    "Kiki's Delivery Service", "Castle in the Sky", "Nausicaa of the Valley of the Wind",
    "Porco Rosso", "Whisper of the Heart", "The Secret World of Arrietty", "When Marnie Was There",
    "The Tale of the Princess Kaguya", "Only Yesterday", "Ocean Waves", "Pom Poko", "My Neighbors the Yamadas",
    "The Cat Returns", "Tales from Earthsea", "From Up on Poppy Hill", "The Red Turtle",
    "Earwig and the Witch", "The Boy and the Heron", "Dragon Ball Super Super Hero", "One Piece Film Red",
    "Jujutsu Kaisen 0", "Demon Slayer Mugen Train", "Evangelion 3.0+1.0 Thrice Upon a Time",
    "Belle", "Josee the Tiger and the Fish", "Words Bubble Up Like Soda Pop", "A Whisker Away",
    "Children of the Sea", "Promare", "Mirai", "Maquia When the Promised Flower Blooms",
    "I Want to Eat Your Pancreas", "A Silent Voice", "Your Name", "The Boy and the Beast",
    "Wolf Children", "Summer Wars", "The Girl Who Leapt Through Time", "Paprika", "Tokyo Godfathers",
    "Millennium Actress", "Perfect Blue", "Memories", "Robot Carnival", "Neo Tokyo",
    "Angel's Egg", "Vampire Hunter D Bloodlust", "Ninja Scroll", "Redline", "Dead Leaves",
    "Mind Game", "Tekkonkinkreet", "The Animatrix", "Batman Gotham Knight", "Halo Legends",
    "Star Wars Visions", "Love Death and Robots Volume 3", "Spider-Man Into the Spider-Verse",
    "The Mitchells vs the Machines", "Puss in Boots The Last Wish", "The Bad Guys", "Guillermo del Toro's Pinocchio",
    "Nimona", "Teenage Mutant Ninja Turtles Mutant Mayhem", "Spider-Man Across the Spider-Verse",
    "The Super Mario Bros Movie", "Elemental", "Ruby Gillman Teenage Kraken", "Trolls Band Together",
    "Wish", "Migration", "Kung Fu Panda 4", "Despicable Me 4", "Inside Out 2", "Garfield",
    "Transformers One", "Spider-Man Beyond the Spider-Verse", "Sonic the Hedgehog 3", "Mufasa The Lion King",
    "Moana 2", "Zootopia 2", "Frozen 3", "Toy Story 5", "Shrek 5", "The Incredibles 3",
    "Finding Nemo 3", "Monsters Inc 3", "Cars 4", "Up 2", "Ratatouille 2", "WALL-E 2",
    "Brave 2", "Inside Out 3", "The Good Dinosaur 2", "Coco 2", "Onward 2", "Soul 2",
    "Luca 2", "Turning Red 2", "Lightyear 2", "Elemental 2", "Elio", "Hoppers",
    "A Bug's Life 2", "Antz 2", "The Prince of Egypt 2", "The Road to El Dorado 2",
    "Chicken Run Dawn of the Nugget", "Wallace & Gromit Vengeance Most Fowl", "Early Man",
    "Shaun the Sheep Movie Farmageddon", "Flushed Away 2", "Over the Hedge 2", "Shark Tale 2",
    "Madagascar 4", "Kung Fu Panda 5", "How to Train Your Dragon 4", "Megamind 2",
    "Monsters vs Aliens 2", "The Croods 3", "Turbo 2", "Mr Peabody & Sherman 2",
    "Penguins of Madagascar 2", "Home 2", "Trolls 3", "The Boss Baby 3", "Captain Underpants 2",
    "The Bad Guys 2", "Puss in Boots 3", "Shrek 6", "The SpongeBob Movie Search for SquarePants",
    "The Simpsons Movie 2", "The Peanuts Movie 2", "Ice Age 6", "Rio 3", "Ferdinand 2",
    "Spies in Disguise 2", "The Emoji Movie 2", "Hotel Transylvania 5", "Cloudy with a Chance of Meatballs 3",
    "The Smurfs 4", "Arthur Christmas 2", "The Pirates Band of Misfits 2", "Surf's Up 3",
    "Open Season 5", "Spider-Man Into the Spider-Verse 3"
]

# Ensure uniqueness
fresh_movies_pool = list(set([m for m in fresh_movies_pool if m.lower() not in used_movies]))
random.shuffle(fresh_movies_pool)

# If we need more, just generate generic descriptive concepts
while len(fresh_movies_pool) < len(htmls_to_process):
    fresh_movies_pool.append(f"Cinematic Concept {random.randint(1000, 9999)}")

new_tasks = []
index = 356

for html in htmls_to_process:
    movie = fresh_movies_pool.pop()
    title = extract_title(html)
    prompt = f"Movie poster style, {movie} aesthetic, highly detailed, cinematic lighting, 8k resolution, photorealistic, dramatic atmosphere, typography layout, concept art for '{title}'."
    new_tasks.append({"index": index, "movie": movie, "target_html": html, "prompt": prompt})
    index += 1

with open("movie_posters_tasks_285.json", "w", encoding="utf-8") as f:
    json.dump(new_tasks, f, indent=2, ensure_ascii=False)

