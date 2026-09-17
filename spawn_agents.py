import json

with open('/Users/vietmac/Documents/CODE/k/batch_385_512.json', 'r') as f:
    tasks = json.load(f)

subagents = []
batch_size = 5
for i in range(0, len(tasks), batch_size):
    batch = tasks[i:i+batch_size]
    prompt = "You are a batch poster generator. Generate images for these tasks:\n"
    prompt += json.dumps(batch) + "\n"
    prompt += "For each task, call `generate_image` with AspectRatio '9:16', the provided prompt, and EXACTLY these ImagePaths: [\"/Users/vietmac/Documents/CODE/Quản gia/assets/ava/viet_real_master_crop_006.jpg\", \"/Users/vietmac/Documents/CODE/Quản gia/assets/ava/viet_avatar_002.jpg\"]. Name the image `poster_{index}`. After generating, move the images from your artifact directory to /Users/vietmac/Documents/CODE/k/assets/covers/ and rename them to `cover_index_{index}.jpg`. Finally, send a message back to me with a JSON string representing a dictionary mapping target_html to 'assets/covers/cover_index_{index}.jpg'."
    
    subagents.append({
        "TypeName": "self",
        "Role": f"Batch {i//batch_size}",
        "Prompt": prompt
    })

with open('subagents_args.json', 'w') as f:
    json.dump({"Subagents": subagents}, f)

print(len(subagents))
