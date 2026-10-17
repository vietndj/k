import json
import sys

def main():
    with open('master_poster_tasks.json', 'r') as f:
        tasks = json.load(f)
    
    # Filter 1-128
    tasks = [t for t in tasks if 1 <= t.get('index', 0) <= 128]
    
    # Read state
    try:
        with open('current_batch.txt', 'r') as f:
            current_index = int(f.read().strip())
    except:
        current_index = 0
        
    if current_index >= len(tasks):
        print("ALL DONE")
        return
        
    batch = tasks[current_index:current_index+5]
    print(f"BATCH STARTING AT {current_index+1}")
    for i, t in enumerate(batch):
        idx = t['index']
        target_html = t['target_html']
        prompt = t['prompt']
        name = f"poster_{idx}"
        print(f"--- ITEM {idx} ---")
        print(f"Target HTML: {target_html}")
        print(f"Prompt: {prompt}")
        print(f"ImageName: {name}")

    with open('current_batch.txt', 'w') as f:
        f.write(str(current_index + 5))
        
    with open('current_targets.json', 'w') as f:
        json.dump({f"poster_{t['index']}": t['target_html'] for t in batch}, f)

if __name__ == "__main__":
    main()
