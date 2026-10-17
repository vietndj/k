import glob
import os
import hashlib
import json

covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
manifest_file = "/Users/vietmac/Documents/CODE/k/generate_manifest.py"
posts_file = "/Users/vietmac/Documents/CODE/k/posts-manifest.json"

# MD5 của file webp hỏng 110 bytes
ERROR_MD5 = "cb7dcd0abfd677456c788374f1e829b0"

def get_md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

error_webps = set()
for filepath in glob.glob(os.path.join(covers_dir, "poster_batch_*.webp")):
    if get_md5(filepath) == ERROR_MD5:
        error_webps.add(os.path.basename(filepath))

with open(posts_file, "r", encoding="utf-8") as f:
    posts = json.load(f)["posts"]

error_items = []
for p in posts:
    cover = p.get("cover_image", "")
    if cover.split('/')[-1] in error_webps:
        error_items.append({
            "title": p.get("title", ""),
            "filename": p.get("filename", ""),
            "cover": cover
        })

with open("/Users/vietmac/Documents/CODE/Quản gia/bang.md", "w", encoding="utf-8") as f:
    f.write("# Thống Kê Các Banner Bị Trống / Lỗi Generate\n\n")
    f.write("Do chạy quá nhanh, API sinh ảnh bị giới hạn (Rate Limit) khiến 150/203 bức ảnh trả về file rỗng (chỉ 110 byte). Dưới đây là danh sách các bài viết bị ảnh hưởng:\n\n")
    f.write("| STT | Tên bài viết | Trạng thái |\n")
    f.write("|---|---|---|\n")
    for i, item in enumerate(error_items, 1):
        f.write(f"| {i} | {item['title']} | Lỗi 110 Byte (Trống) |\n")

print(f"Found {len(error_items)} error banners.")
