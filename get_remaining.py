import subprocess
import json
import math

cmd = "file /Users/vietmac/Documents/CODE/k/assets/covers/*.jpg | grep 'density 300x300' | awk -F: '{print $1}'"
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
bad_images = [line.strip().replace('/Users/vietmac/Documents/CODE/k/', '') for line in result.stdout.split('\n') if line.strip()]

roles = [
    ("Jon Snow", "King in the North, heavy black direwolf fur cloak, dark leather armor, snow falling, Game of Thrones aesthetic"),
    ("Aragorn", "Ranger armor, dark leather, holding a sword, dark forest background, Lord of the Rings aesthetic"),
    ("Jaime Lannister", "Golden Kingsguard armor, white cloak, proud posture, Game of Thrones aesthetic"),
    ("Legolas", "Elven archer, green and gold scale armor, bow on shoulder, misty forest, Lord of the Rings aesthetic"),
    ("Daemon Targaryen", "Dark red and black dragon scale armor, Dragonstone volcano background, House of the Dragon aesthetic"),
    ("Elrond", "Lord of Rivendell, elegant velvet silk robes embroidered with gold, wise and regal, Lord of the Rings aesthetic")
]

num_branches = 5
chunk_size = math.ceil(len(bad_images) / num_branches)
chunks = [bad_images[i:i + chunk_size] for i in range(0, len(bad_images), chunk_size)]

jobs = []
for i, chunk in enumerate(chunks):
    job_str = f"Execute this job list (Branch {i+1}):\n"
    for j, img in enumerate(chunk):
        idx = i * chunk_size + j
        role_name, role_desc = roles[idx % len(roles)]
        job_str += f"- Image: {img} | Role: {role_desc}\n"
    jobs.append(job_str)

with open('/Users/vietmac/Documents/CODE/k/remaining_jobs.json', 'w') as f:
    json.dump(jobs, f)
print(f"Created {len(jobs)} jobs. Total remaining: {len(bad_images)}")
