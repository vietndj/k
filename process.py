import json
import glob
import os
import shutil

batch = json.load(open('batch17.json'))
artifact_dir = '/Users/vietmac/.gemini/antigravity/brain/515a158b-52ea-4aa5-9a4c-22e427c64fd1'
mapping = {}

for item in batch:
    idx = item['index']
    target_html = item['target_html']
    target_name = target_html.replace('.html', '.jpg')
    target_path = os.path.join('assets/covers', target_name)
    
    # find poster_17_{idx}_*.jpg
    pattern = os.path.join(artifact_dir, f'poster_17_{idx}_*.jpg')
    matches = glob.glob(pattern)
    if matches:
        src = matches[0]
        shutil.copy(src, target_path)
        mapping[target_html] = target_path
        print(f'Copied {src} to {target_path}')

with open('temp_mapping_346.json', 'w') as f:
    json.dump(mapping, f, indent=2)

print('Done creating mapping')
