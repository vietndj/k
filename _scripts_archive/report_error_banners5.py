import glob
import os
import hashlib

covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
bang_md = "/Users/vietmac/Documents/CODE/Quản gia/bang.md"

ERROR_MD5 = "cb7dcd0abfd677456c788374f1e829b0"

def get_md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

html_names = []
for filepath in glob.glob(os.path.join(covers_dir, "poster_batch_*.webp")):
    if get_md5(filepath) == ERROR_MD5:
        basename = os.path.basename(filepath)
        html_name = basename.replace("poster_batch_", "").replace(".webp", ".html")
        html_names.append(html_name)

with open(bang_md, "w", encoding="utf-8") as f:
    f.write("# Thống Kê Các Banner Lỗi (Trống Ảnh)\n\n")
    f.write("Do chạy quá nhanh, API sinh ảnh bị giới hạn (Rate Limit) khiến các file bị trả về rỗng (chỉ 110 byte). Dưới đây là danh sách các file HTML bị ảnh hưởng:\n\n")
    f.write("| STT | File HTML | Trạng thái |\n")
    f.write("|---|---|---|\n")
    for i, html_file in enumerate(html_names, 1):
        f.write(f"| {i} | {html_file} | Lỗi 110 Byte |\n")

print(f"Saved bang.md with {len(html_names)} items.")
