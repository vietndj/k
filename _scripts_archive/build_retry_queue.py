import glob
import os
import hashlib
import json

covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
posts_file = "/Users/vietmac/Documents/CODE/k/posts-manifest.json"

ERROR_MD5 = "cb7dcd0abfd677456c788374f1e829b0"

def get_md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

html_names = set()
for filepath in glob.glob(os.path.join(covers_dir, "poster_batch_*.webp")):
    if get_md5(filepath) == ERROR_MD5:
        basename = os.path.basename(filepath)
        html_name = basename.replace("poster_batch_", "").replace(".webp", ".html")
        html_names.add(html_name)

print(f"Found {len(html_names)} corrupted files.")

with open(posts_file, "r", encoding="utf-8") as f:
    posts = json.load(f)["posts"]

retry_queue = []
for p in posts:
    if p["filename"] in html_names:
        retry_queue.append({
            "filename": p["filename"],
            "title": p["title"],
            "excerpt": p.get("excerpt", "")
        })

with open("/Users/vietmac/Documents/CODE/k/retry_queue.json", "w", encoding="utf-8") as f:
    json.dump(retry_queue, f, ensure_ascii=False, indent=2)

with open("/Users/vietmac/Documents/CODE/Quản gia/bang.md", "w", encoding="utf-8") as f:
    f.write("# Thống Kê Các Banner Lỗi (Trống Ảnh 110 byte)\n\n")
    f.write("Do chạy quá nhanh, API sinh ảnh bị giới hạn (Rate Limit) khiến 150/203 bức ảnh trả về file rỗng (chỉ 110 byte). Dưới đây là danh sách các bài viết bị ảnh hưởng:\n\n")
    f.write("| STT | Tên bài viết | Trạng thái |\n")
    f.write("|---|---|---|\n")
    for i, item in enumerate(retry_queue, 1):
        f.write(f"| {i} | {item['title']} | Lỗi 110 Byte (Trống) |\n")

print(f"Created retry_queue.json with {len(retry_queue)} items.")
