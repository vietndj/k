import glob
import os
import hashlib
import json
import re

covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
manifest_file = "/Users/vietmac/Documents/CODE/k/generate_manifest.py"
bang_md = "/Users/vietmac/Documents/CODE/Quản gia/bang.md"

ERROR_MD5 = "cb7dcd0abfd677456c788374f1e829b0"

def get_md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

error_webps = set()
for filepath in glob.glob(os.path.join(covers_dir, "poster_batch_*.webp")):
    if get_md5(filepath) == ERROR_MD5:
        error_webps.add(os.path.basename(filepath))

with open(manifest_file, "r", encoding="utf-8") as f:
    content = f.read()

error_htmls = set()
match = re.search(r'cover_mapping\s*=\s*\{([^}]+)\}', content)
if match:
    mapping_str = match.group(1)
    for line in mapping_str.split('\n'):
        if ':' in line:
            parts = line.split(':')
            html_key = parts[0].strip().strip('"').strip("'")
            val = parts[1].strip().strip(',').strip('"').strip("'")
            cover_filename = val.split('/')[-1]
            if cover_filename in error_webps:
                error_htmls.add(html_key)

with open(bang_md, "w", encoding="utf-8") as f:
    f.write("# Thống Kê Các Banner Lỗi (Trống Ảnh)\n\n")
    f.write("Do chạy quá nhanh, API sinh ảnh bị giới hạn (Rate Limit) khiến các file bị trả về rỗng (chỉ 110 byte). Dưới đây là danh sách các file HTML bị ảnh hưởng:\n\n")
    f.write("| STT | File HTML | Trạng thái |\n")
    f.write("|---|---|---|\n")
    for i, html_file in enumerate(list(error_htmls), 1):
        f.write(f"| {i} | {html_file} | Lỗi 110 Byte |\n")

print(f"Saved bang.md with {len(error_htmls)} items.")

new_mapping_lines = []
for line in mapping_str.split('\n'):
    if ':' in line:
        parts = line.split(':')
        html_key = parts[0].strip().strip('"').strip("'")
        if html_key not in error_htmls:
            new_mapping_lines.append(line)
    else:
        if line.strip() != "":
            new_mapping_lines.append(line)
            
new_mapping_str = '\n'.join(new_mapping_lines)
content = content.replace(mapping_str, "\n" + new_mapping_str + "\n")

with open(manifest_file, "w", encoding="utf-8") as f:
    f.write(content)
print("Cleaned up generate_manifest.py")
