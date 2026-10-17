import json
import re

anchor_prompt = "Featuring a Vietnamese man with an oval face, high cheekbones, expressive Asian monolids, a radiant smile with upper teeth showing, and a signature spiky brush-up hairstyle. He is wearing a dark tailored suit. "

def update_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            tasks = json.load(f)
        
        for t in tasks:
            if anchor_prompt not in t["prompt"]:
                # insert after "Movie poster style, "
                t["prompt"] = t["prompt"].replace("Movie poster style, ", f"Movie poster style, {anchor_prompt}")
                
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
        print(f"Updated {filename} successfully.")
    except Exception as e:
        print(f"Error on {filename}: {e}")

update_file("movie_posters_tasks_355.json")
update_file("movie_posters_tasks_285.json")
