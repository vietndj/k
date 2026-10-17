import json
import random
import html
import re
import os

with open("to_regenerate.json", "r") as f:
    items = json.load(f)

aesthetics = [
    "Wuxia martial arts (Võ Hiệp)",
    "Xianxia fantasy (Tiên Hiệp)",
    "Joseon Dynasty historical drama",
    "Goryeo Dynasty epic",
    "Tang Dynasty imperial court",
    "Ming Dynasty detective drama",
    "The Untamed (Trần Tình Lệnh)",
    "Joy of Life (Khánh Dư Niên)",
    "Kingdom (Korean zombie historical)",
    "Moon Lovers (Bộ Bộ Kinh Tâm)",
    "Empresses in the Palace (Chân Hoàn Truyện)",
    "Nirvana in Fire (Lang Nha Bảng)",
    "Mr. Sunshine (Joseon transition era)",
    "Alchemy of Souls (Hoàn Hồn)",
    "Ten Miles of Peach Blossoms (Tam Sinh Tam Thế)",
    "Story of Minglan (Minh Lan Truyện)"
]

attires = [
    "elegant traditional flowing Hanfu robes with intricate embroidery",
    "noble Joseon Dynasty Hanbok with a gat (traditional hat) and majestic colors",
    "rugged Wuxia martial artist robes with leather bracers and a sword",
    "majestic Tang Dynasty imperial court attire in gold and crimson",
    "mystical Xianxia cultivator robes in pure white and pale blue",
    "dark Royal Guard (Cẩm Y Vệ) uniform with detailed armor plates"
]

dna_en = "Featuring a Vietnamese man with an oval face, high cheekbones, expressive Asian monolids, a radiant smile with upper teeth showing, and a signature spiky brush-up hairstyle."
dna_vi = "Khóa dáng mặt Oval, gò má cao, đuôi mắt mí lót Á Đông có hồn, kiểu tóc spiky brush-up đặc trưng."

new_items = []
markdown_rows = []

for idx, item in enumerate(items):
    old_prompt = html.unescape(item["prompt"])
    
    # Extract title
    title_match = re.search(r"concept art for ['\"](.*?)['\"]", old_prompt)
    if title_match:
        title = title_match.group(1)
    else:
        # Fallback if no concept art tag
        title = "Chuyên Đề Kịch Bản " + str(idx)
        
    aes = random.choice(aesthetics)
    attire = random.choice(attires)
    
    new_prompt = f"Movie poster style, {dna_en} He is wearing {attire}. {aes} aesthetic, highly detailed, cinematic lighting, 8k resolution, photorealistic, dramatic atmosphere, typography layout, concept art for '{title}'. {dna_vi}"
    
    filename = item["path"].split("/")[-1]
    
    new_items.append({
        "old_path": item["path"],
        "filename": filename,
        "title": title,
        "prompt": new_prompt
    })
    
    # Create markdown table row
    if idx < 220: # Do all of them
        markdown_rows.append(f"| {idx+1} | **{title}**<br/>*{aes}* | {new_prompt} |")

# Save to JSON
with open("new_cotrang_prompts.json", "w") as f:
    json.dump(new_items, f, ensure_ascii=False, indent=2)

# Save to Markdown
md_content = """# Danh Sách Prompt Cổ Trang (220 Bài)

Dưới đây là bảng 220 prompt được chuyển thể sang phong cách **Phim Cổ Trang Trung Quốc / Hàn Quốc**, kết hợp trang phục Hanfu/Hanbok/Kiếm Khách nhưng vẫn giữ nguyên vẹn mã Face DNA của anh Việt.

| STT | Chủ Đề & Style | Chi Tiết Prompt |
|:---:|:---|:---|
"""
md_content += "\n".join(markdown_rows)

artifact_path = "/Users/vietmac/.gemini/antigravity/brain/66d764d7-72c7-410f-ad50-3858ded5125a/bang_prompt_co_trang.md"
with open(artifact_path, "w") as f:
    f.write(md_content)

print(f"Generated 220 prompts. Markdown saved to {artifact_path}")
