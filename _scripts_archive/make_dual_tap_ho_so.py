import os
from bs4 import BeautifulSoup

# Đọc HTML bài gốc
with open("/Users/vietmac/Documents/CODE/k/bill-ackman-kich-ban-dau-tu.html", "r", encoding="utf-8") as f:
    original_html = f.read()

soup = BeautifulSoup(original_html, "html.parser")
container = soup.find("div", class_="container")

# Xây dựng Mục lục (TOC)
all_headings = container.find_all(["h2", "h3"])
toc_items = []
for i, tag in enumerate(all_headings):
    heading_id = f"section-{i}"
    tag["id"] = heading_id
    if tag.name == "h2":
        toc_items.append(f'<li class="toc-h2"><a href="#{heading_id}">{tag.get_text()}</a></li>')
    else:
        text = tag.get_text()
        if "📌 Insight" in text:
            text = text.split(":", 1)[-1].strip()
        toc_items.append(f'<li class="toc-h3"><a href="#{heading_id}">{text}</a></li>')

content_html = "".join(str(c) for c in container.contents)
toc_html = "".join(toc_items)

# Tải Template Chuẩn
with open("/Users/vietmac/Documents/CODE/k/templates/tap_ho_so_template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Bơm dữ liệu vào Template
out_html = template.replace("{title}", "Bill Ackman: Kịch Bản Đầu Tư Ngược Đám Đông Xây Dựng Đế Chế 36 Tỷ Đô")
out_html = out_html.replace("{toc_html}", toc_html)
out_html = out_html.replace("{content_html}", content_html)

out_path = "/Users/vietmac/Documents/CODE/k/Bill_Ackman_Full_Tap_Ho_So.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(out_html)

print("Đã xuất bản thành công dựa trên Template:", out_path)
