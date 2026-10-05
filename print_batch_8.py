import json
import sys

try:
    with open("batches.json") as f:
        batches = json.load(f)
    
    if 8 < len(batches):
        batch = batches[8]
        for t in batch:
            print(f"INDEX:{t['index']}")
            print(f"HTML:{t['target_html']}")
            print(f"PROMPT:{t['prompt']}")
except Exception as e:
    print(e)
