import json
import subprocess
import time
import os
import shutil

with open("/Users/vietmac/Documents/CODE/k/remaining_poster_tasks.json") as f:
    data = json.load(f)
items = [x for x in data if 163 <= x["index"] <= 243]

# This script will print the prompt and details for the next items
for item in items[:5]:
    print(item['index'])
    print(item['prompt'])
