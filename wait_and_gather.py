import time
import os
import subprocess
import json

while True:
    subprocess.run(["python3", "gather_generated_images.py"])
    
    with open("cotrang_progress.json") as f:
        progress = json.load(f)
    
    if len(progress) >= 220:
        print("All 220 images generated! Updating HTML and pushing...")
        subprocess.run(["python3", "update_anh_html_hash_dedup.py"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "feat: Finalize all 220 historical drama posters"])
        subprocess.run(["git", "push", "origin", "main"])
        break
        
    time.sleep(30)
