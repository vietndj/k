import re
import urllib.request

html_file = "/Users/vietmac/Documents/CODE/k/anh.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

print("--- BẮT ĐẦU AUDIT ---")
# 1. Check counts
poem_cards = len(re.findall(r'poem-card', html))
normal_cards = len(re.findall(r'class="card has-prompt"', html))
no_prompt_cards = len(re.findall(r'class="card no-prompt"', html))

print(f"Tổng số ảnh Thơ (poem-card): {poem_cards}")
print(f"Tổng số ảnh Prompt (normal): {normal_cards}")
print(f"Tổng số ảnh không có prompt: {no_prompt_cards}")
print(f"Tổng cộng thẻ (Cards): {poem_cards + normal_cards + no_prompt_cards}")

# 2. Check image sources
img_srcs = re.findall(r'<img src="([^"]+)"', html)
print(f"Tổng số đường dẫn ảnh: {len(img_srcs)}")

# Phân tích nguồn ảnh
local_assets = sum(1 for src in img_srcs if src.startswith("assets/covers/"))
media_fedu = sum(1 for src in img_srcs if src.startswith("https://media.fedu.vn"))
other = len(img_srcs) - local_assets - media_fedu

print(f" - Ảnh từ local (assets/covers/): {local_assets}")
print(f" - Ảnh từ media.fedu.vn: {media_fedu}")
print(f" - Ảnh từ nguồn khác: {other}")

# 3. Check 3 random images to see if they are 200 OK
import random
sample_imgs = random.sample(img_srcs, 5)
print("\n--- Kiểm tra link ảnh (Sample 5 links) ---")
for src in sample_imgs:
    url = src if src.startswith("http") else f"https://fedu.vn/k/{src}"
    try:
        req = urllib.request.Request(url, method='HEAD')
        resp = urllib.request.urlopen(req, timeout=5)
        print(f"✅ [200 OK] {url}")
    except Exception as e:
        print(f"❌ [LỖI] {url} - {str(e)}")

print("\n--- HOÀN TẤT AUDIT ---")
