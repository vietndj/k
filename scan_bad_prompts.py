import re
import json

with open("anh.html", "r", encoding="utf-8") as f:
    html = f.read()

# Each card has <img src="..."> then a <div class="prompt-text" id="...">...</div>
cards = re.findall(r'<div class="card">.*?<img src="([^"]+)".*?<div class="prompt-text"[^>]*>(.*?)</div>', html, re.DOTALL)

bad_list = []
for img_url, prompt in cards:
    if "Vietnamese man" not in prompt:
        bad_list.append({
            "img_url": img_url,
            "old_prompt": prompt.strip()
        })

print(f"Tổng số ảnh trong anh.html: {len(cards)}")
print(f"Số ảnh KHÔNG có Face DNA trong prompt: {len(bad_list)}")

with open("bad_prompts_list.json", "w", encoding="utf-8") as f:
    json.dump(bad_list, f, indent=4, ensure_ascii=False)
