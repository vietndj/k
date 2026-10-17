import json

with open("cotrang_progress.json", "r") as f:
    progress = json.load(f)

with open("new_cotrang_prompts.json", "r") as f:
    all_prompts = json.load(f)

pending = [p for p in all_prompts if p["filename"] not in progress]

for p in pending[:10]:
    filename = p["filename"]
    prompt = p["prompt"].replace('"', '\\"')
    print(f'\\u1202call:default_api:generate_image{{AspectRatio:"9:16",ImageName:"{filename.replace(".jpg","")}",Prompt:"{prompt}",toolAction:"Generate image",toolSummary:"Gen {filename}"}}\\u1203', end="")
print()
