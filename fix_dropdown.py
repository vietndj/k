with open("rebuild_anh_ui.py", "r") as f:
    content = f.read()

import re

new_dropdown = """<select id="categoryFilter">
            <option value="all">Tất cả thể loại</option>
            <option value="Phim Điện Ảnh">Phim Điện Ảnh</option>
            <option value="Anime">Anime</option>
            <option value="Game">Game</option>
            <option value="Triết Lý / Văn Học">Triết Lý / Văn Học</option>
            <option value="Chưa phân loại">Khác / Chưa phân loại</option>
        </select>"""

content = re.sub(r'<select id="categoryFilter">.*?</select>', new_dropdown, content, flags=re.DOTALL)

with open("rebuild_anh_ui.py", "w") as f:
    f.write(content)
