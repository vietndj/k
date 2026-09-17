import json
import re
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

# Also add the ones from R2 mapping to used_movies
for html, url in mapping.items():
    if url not in failed_urls:
        basename = url.split("/")[-1].replace("poster_", "").replace(".jpg", "").replace("_", " ").title().strip()
        used_movies.add(basename.lower())

print("Dune used?", "dune" in used_movies)
print("Blade Runner used?", "blade runner" in used_movies)
print("Oppenheimer used?", "oppenheimer" in used_movies)

# New movies pool (recent / visually stunning)
new_movies_pool = [
    "Dune Part Two", "Furiosa", "Civil War", "Godzilla Minus One", "Spider-Verse", 
    "The Batman", "Everything Everywhere All at Once", "Poor Things", "The Boy and the Heron", 
    "Avatar The Way of Water", "Top Gun Maverick", "Nope", "Challengers", "Megalopolis", 
    "Kalki 2898 AD", "Kingdom of the Planet of the Apes", "Alien Romulus", "Inside Out 2"
]
# Filter out any that might be used
new_movies_pool = [m for m in new_movies_pool if m.lower() not in used_movies]
random.shuffle(new_movies_pool)

with open("missing_posters_report.json", "r") as f: missing = set(json.load(f))
tasks_htmls = set([t["target_html"] for t in old_tasks])
missing_not_in_tasks = missing - tasks_htmls

new_tasks = []
index = 356

for html, url in mapping.items():
    if url in failed_urls:
        basename = url.split("/")[-1].replace("poster_", "").replace(".jpg", "").replace("_", " ").title().strip()
        if "Cover" not in basename and "Ads" not in basename and "Offline" not in basename and basename.lower() not in used_movies:
            movie = basename
            used_movies.add(basename.lower())
        else:
            movie = new_movies_pool.pop() if new_movies_pool else "Cinematic Masterpiece"
            
        title = extract_title(html)
        prompt = f"Movie poster style, {movie} aesthetic, highly detailed, cinematic lighting, 8k resolution, photorealistic, dramatic atmosphere, typography layout, concept art for '{title}'."
        new_tasks.append({"index": index, "movie": movie, "target_html": html, "prompt": prompt})
        index += 1

for html in missing_not_in_tasks:
    movie = new_movies_pool.pop() if new_movies_pool else "Cinematic Masterpiece"
    title = extract_title(html)
    prompt = f"Movie poster style, {movie} aesthetic, highly detailed, cinematic lighting, 8k resolution, photorealistic, dramatic atmosphere, typography layout, concept art for '{title}'."
    new_tasks.append({"index": index, "movie": movie, "target_html": html, "prompt": prompt})
    index += 1

with open("movie_posters_tasks_285.json", "w", encoding="utf-8") as f:
    json.dump(new_tasks, f, indent=2, ensure_ascii=False)

