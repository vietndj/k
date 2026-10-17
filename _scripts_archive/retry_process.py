import os
import glob
from PIL import Image
import json

temp_dir = "/Users/vietmac/Documents/CODE/k/assets/temp_covers"
covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
manifest_file = "/Users/vietmac/Documents/CODE/k/generate_manifest.py"
queue_file = "/Users/vietmac/Documents/CODE/k/retry_queue.json"

insertion = ""
processed_files = []

for filepath in glob.glob(os.path.join(temp_dir, "*.jpg")):
    filename = os.path.basename(filepath)
    html_name = filename[:-4] # remove .jpg
    webp_name = f"poster_batch_{html_name.replace('.html', '')}.webp"
    webp_path = os.path.join(covers_dir, webp_name)
    
    # Check if empty (110 byte case) or valid
    if os.path.getsize(filepath) < 500:
        print(f"Skipping empty image: {filepath}")
        os.remove(filepath)
        continue
        
    try:
        img = Image.open(filepath)
        img.save(webp_path, "webp", quality=80)
        
        insertion += f'        "{html_name}": "https://media.fedu.vn/k_covers/{webp_name}",\n'
        processed_files.append(html_name)
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)

if processed_files:
    # Update generate_manifest.py
    with open(manifest_file, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace('cover_mapping = {', f'cover_mapping = {{\n{insertion}')

    with open(manifest_file, "w", encoding="utf-8") as f:
        f.write(content)

    # Update queue
    with open(queue_file, "r", encoding="utf-8") as f:
        queue = json.load(f)

    new_queue = [q for q in queue if q["filename"] not in processed_files]

    with open(queue_file, "w", encoding="utf-8") as f:
        json.dump(new_queue, f, ensure_ascii=False, indent=2)

    print(f"Processed {len(processed_files)} covers. Remaining: {len(new_queue)}")
else:
    print("No valid images processed.")
