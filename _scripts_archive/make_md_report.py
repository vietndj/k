import json

with open("duplicate_report.json", "r") as f: data = json.load(f)

md = "# Danh Sách 80 Poster Trùng Lặp / Lỗi Anchor\n\n"
md += "Dưới đây là danh sách 80 bài viết bị lỗi trùng lặp hình ảnh hoặc bị Subagent sao chép thẳng ảnh gốc (Anchor Copy) để lách luật khi API bị khóa Quota. Ý tưởng (concept) gốc của từng ảnh vẫn được giữ nguyên để chúng ta có thể tạo lại.\n\n"
md += "| File HTML | Chủ đề (Title) | Phong cách (Movie) | Lỗi |\n"
md += "|---|---|---|---|\n"

for item in data:
    md += f"| `{item['html']}` | {item['title']} | **{item['movie']}** | {item['reason']} |\n"

with open("duplicate_report.md", "w") as f:
    f.write(md)
