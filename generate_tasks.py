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

with open("failed_r2.txt", "r") as f: failed_urls = set([l.strip() for l in f if l.strip()])
with open("generate_manifest.py", "r", encoding="utf-8") as f: content = f.read()
mapping = dict(re.findall(r"\"([^\"]+\.html)\"\s*:\s*\"([^\"]+)\"", content))
with open("missing_posters_report.json", "r") as f: missing = set(json.load(f))
with open("movie_posters_tasks_355.json", "r") as f: old_tasks = json.load(f)
tasks_htmls = set([t["target_html"] for t in old_tasks])

used_movies = set([t["movie"].lower().strip() for t in old_tasks])

# Fill random movies
random_movies = [
    "Dune", "Blade Runner", "Cyberpunk", "Oppenheimer", "The Dark Knight Rises",
    "John Wick", "Mad Max Fury Road", "Gladiator", "The Creator", "Ex Machina",
    "Arrival", "Her", "Annihilation", "Snowpiercer", "The Fifth Element",
    "Minority Report", "Edge of Tomorrow", "A.I. Artificial Intelligence", "Bicentennial Man"
]
random.shuffle(random_movies)

new_tasks = []
index = 356

for html, url in mapping.items():
    if url in failed_urls:
        basename = url.split("/")[-1].replace("poster_", "").replace(".jpg", "").replace("_", " ").title().strip()
        if "Cover" not in basename and "Ads" not in basename and "Offline" not in basename:
            movie = basename
        else:
            movie = random_movies.pop() if random_movies else "Sci-Fi Masterpiece"
            
        title = extract_title(html)
        prompt = f"Movie poster style, {movie} aesthetic, highly detailed, cinematic lighting, 8k resolution, photorealistic, dramatic atmosphere, typography layout, concept art for '{title}'."
        new_tasks.append({
            "index": index,
            "movie": movie,
            "target_html": html,
            "prompt": prompt
        })
        index += 1

missing_not_in_tasks = missing - tasks_htmls
for html in missing_not_in_tasks:
    movie = random_movies.pop() if random_movies else "Sci-Fi Masterpiece"
    title = extract_title(html)
    prompt = f"Movie poster style, {movie} aesthetic, highly detailed, cinematic lighting, 8k resolution, photorealistic, dramatic atmosphere, typography layout, concept art for '{title}'."
    new_tasks.append({
        "index": index,
        "movie": movie,
        "target_html": html,
        "prompt": prompt
    })
    index += 1

with open("movie_posters_tasks_285.json", "w", encoding="utf-8") as f:
    json.dump(new_tasks, f, indent=2, ensure_ascii=False)

print(f"Generated movie_posters_tasks_285.json with {len(new_tasks)} items.")
