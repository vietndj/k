import json
import os
import shutil
import glob
import re
import subprocess

# Load tasks
with open('/Users/vietmac/Documents/CODE/k/master_poster_tasks.json', 'r') as f:
    tasks = json.load(f)

task_map = {t['index']: t['target_html'] for t in tasks}

# Find all generated posters in the brain directory
search_pattern = '/Users/vietmac/.gemini/antigravity/brain/**/poster_*.jpg'
found_files = glob.glob(search_pattern, recursive=True)

mapping = {}

for file_path in found_files:
    filename = os.path.basename(file_path)
    match = re.search(r'poster_(\d+)_?', filename)
    if match:
        index = int(match.group(1))
        if index in task_map:
            target_html = task_map[index]
            target_jpg = target_html.replace('.html', '.jpg')
            dest_path = f'/Users/vietmac/Documents/CODE/k/assets/covers/{target_jpg}'
            
            # Copy file
            shutil.copy2(file_path, dest_path)
            
            mapping[target_html] = f'assets/covers/{target_jpg}'

if mapping:
    with open('/Users/vietmac/Documents/CODE/k/temp_mapping_collected.json', 'w') as f:
        json.dump(mapping, f, indent=2)
    
    print(f"Collected {len(mapping)} posters.")
    
    # Run update_covers.py
    subprocess.run(['python3', '/Users/vietmac/Documents/CODE/k/update_covers.py', '/Users/vietmac/Documents/CODE/k/temp_mapping_collected.json'])
    
    # Git commit and push
    subprocess.run('rm -f /Users/vietmac/Documents/CODE/k/.git/index.lock', shell=True)
    subprocess.run('git add .', cwd='/Users/vietmac/Documents/CODE/k', shell=True)
    subprocess.run('git commit -m "feat: collect generated posters before quota hit" || true', cwd='/Users/vietmac/Documents/CODE/k', shell=True)
    subprocess.run('while ! git push; do git pull --rebase; sleep 2; done', cwd='/Users/vietmac/Documents/CODE/k', shell=True)
else:
    print("No new posters found.")
