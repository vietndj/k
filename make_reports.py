import re

# 1. Parse generate_manifest.py
manifest_file = "generate_manifest.py"
with open(manifest_file, "r", encoding="utf-8") as f:
    content = f.read()

mapping_block = re.search(r'cover_mapping\s*=\s*\{([\s\S]*?)\}', content)
mapping_text = mapping_block.group(1)
pattern = re.compile(r'"([^"]+\.html)"\s*:\s*"([^"]+)"')
mapped_covers = dict(pattern.findall(mapping_text))

# 2. Read failed_r2.txt
with open("failed_r2.txt", "r") as f:
    failed_urls = set([line.strip() for line in f if line.strip()])

duplicates_table = """# Báo cáo các Poster bị trùng (Lỗi hiển thị fallback Rear Window)

> [!WARNING]
> Các file HTML dưới đây được cấu hình trỏ tới Cloudflare R2, nhưng ảnh trên R2 bị lỗi 403 (không tồn tại). Hệ thống web tự động load ảnh mặc định (Rear Window) dẫn đến việc anh thấy trùng lặp hàng loạt.

| HTML File | R2 URL Bị Lỗi (Không tồn tại) |
| :--- | :--- |
"""

count = 0
for html, url in mapped_covers.items():
    if url in failed_urls:
        count += 1
        duplicates_table += f"| `{html}` | `{url.split('/')[-1]}` |\n"

with open("audit_duplicates_table.md", "w", encoding="utf-8") as f:
    f.write(duplicates_table)

print(f"Generated audit_duplicates_table.md with {count} items.")
