import os
from bs4 import BeautifulSoup
import datetime

# Read template
with open("/Users/vietmac/Documents/CODE/k/temp_template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Read the original article
with open("/Users/vietmac/Documents/CODE/k/bill-ackman-kich-ban-dau-tu.html", "r", encoding="utf-8") as f:
    original_html = f.read()

soup = BeautifulSoup(original_html, "html.parser")
container = soup.find("div", class_="container")

# Extract insights for TOC
h3_tags = container.find_all("h3")
takeaways_list = []
turn_pills_list = []
floating_nav_list = []

for i, h3 in enumerate(h3_tags):
    text = h3.get_text().strip()
    idx = i + 1
    takeaways_list.append(f"<li>{text.replace('📌 Insight ' + str(idx) + ':', '').strip()}</li>")
    
    # We will wrap the h3 and its following content in a turn block
    # Actually, it's easier to just wrap the whole container in one turn block
    # OR we can wrap each section in a turn block. For a standard article, wrapping everything in one turn block is fine.

# Let's wrap everything in ONE turn block
content_html = str(container)
# Remove the container div itself to just get inner html
content_html = "".join(str(c) for c in container.contents)

turns_html = f"""
<div id="turn-1" class="turn-block">
    <div class="turn-header agent">
        <div class="turn-role">Bài Viết Hoàn Chỉnh</div>
    </div>
    <div class="turn-content prose">
        {content_html}
    </div>
</div>
"""

takeaways_html = "\n".join(takeaways_list)

semantic_tags_html = """
<span class="vault-tag">#BillAckman</span>
<span class="vault-tag">#Investment</span>
<span class="vault-tag">#Activism</span>
"""

turn_pills = """<a href="#turn-1" class="toc-pill agent-pill">#1. Đọc Chuyên Sâu</a>"""
floating_nav = """<a href="#turn-1" class="f-link agent-link">#1. Đọc Chuyên Sâu</a>"""

out_html = template.format(
    title="Bill Ackman: Kịch Bản Đầu Tư",
    clean_goal="Bill Ackman: Kịch Bản Đầu Tư Ngược Đám Đông Xây Dựng Đế Chế 36 Tỷ Đô",
    created_date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
    project="BILL ACKMAN",
    short_id="BA-FULL",
    total_turns="1",
    turn_pills=turn_pills,
    floating_nav_html=floating_nav,
    semantic_tags_html=semantic_tags_html,
    takeaways_html=takeaways_html,
    turns_html=turns_html
)

out_path = "/Users/vietmac/Desktop/Bill_Ackman_Full_Tap_Ho_So.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(out_html)

print("Đã tạo file:", out_path)
