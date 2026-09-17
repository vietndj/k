import json
import sys

def get_batch():
    with open('/Users/vietmac/Documents/CODE/k/movie_posters_tasks_355.json', 'r') as f:
        data = json.load(f)
    
    batch = [item for item in data if 301 <= item['index'] <= 330]
    
    for item in batch:
        image_name = item['target_html'].replace('.html', '')
        print(f"Index: {item['index']}")
        print(f"Name: {image_name}")
        print(f"Prompt: {item['prompt']}\n")

if __name__ == "__main__":
    get_batch()
