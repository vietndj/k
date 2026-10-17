import json

with open("next_batch_data.json", "r") as f:
    data = json.load(f)

# Take first 15 for this batch to stay safe on quotas
data = data[:15]

subagents = []
for item in data:
    subagents.append({
        "TypeName": "self",
        "Role": f"{item['champ']} Generator",
        "Prompt": f"""You are generating a movie poster for ID `{item['id']}`.
1. Call `generate_image` tool with:
ImageName: `poster_{item['id'].replace('-', '_')}`
ImagePaths: `['/Users/vietmac/Documents/CODE/Quản gia/assets/ava/viet_real_master_crop_005.jpg', '/Users/vietmac/Documents/CODE/Quản gia/assets/ava/viet_avatar_005.jpg']`
Prompt: `{item['prompt']}`
2. Use send_message to reply to me with the exact prompt string used."""
    })

print(json.dumps(subagents, indent=2))
