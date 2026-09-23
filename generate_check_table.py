import re
import html
import random

with open('/Users/vietmac/Documents/CODE/k/anh.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all cards
cards = re.findall(r'<div class="card">.*?<img src="(.*?)".*?concept art for &#x27;(.*?)&#x27;.*?</div>', content, re.DOTALL)

movies = [
    "The Lord of the Rings (Chúa Tể Những Chiếc Nhẫn)",
    "Game of Thrones (Trò Chơi Vương Quyền)",
    "The Witcher (Thợ Săn Quái Vật)",
    "House of the Dragon (Gia Tộc Rồng)",
    "Dungeons & Dragons (Ngục Tối Và Rồng)",
    "The Hobbit (Người Hobbit)",
    "Warcraft (Đại Chiến Hai Thế Giới)"
]

html_output = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bảng Kiểm Tra Lỗi Khuôn Mặt & Kế Hoạch Epic Fantasy</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #0f172a; color: #f8fafc; padding: 24px; }
        h1 { text-align: center; color: #38bdf8; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #334155; padding: 12px; text-align: left; }
        th { background-color: #1e293b; color: #94a3b8; }
        tr:nth-child(even) { background-color: #1e293b; }
        img { width: 120px; border-radius: 8px; object-fit: cover; aspect-ratio: 9/16; }
        .concept { color: #10b981; font-weight: 500; }
        .title { font-weight: 600; color: #e2e8f0; font-size: 1.1em; }
    </style>
</head>
<body>
    <h1>Bảng Kiểm Tra Hàng Loạt & Kế Hoạch Làm Lại (Epic Fantasy)</h1>
    <p style="text-align: center;">Tổng số ảnh được quét: {total}</p>
    <table>
        <thead>
            <tr>
                <th>STT</th>
                <th>Hình Ảnh Hiện Tại</th>
                <th>Tiêu Đề / Nội Dung</th>
                <th>Kế Hoạch Làm Lại (Epic Fantasy)</th>
            </tr>
        </thead>
        <tbody>
"""

count = 1
for img_src, title_encoded in cards:
    title = html.unescape(title_encoded.replace(r'\u', '\\u').encode().decode('unicode_escape')) if r'\u' in title_encoded else html.unescape(title_encoded)
    
    # Assign a random fantasy concept for now to fill the plan
    film = random.choice(movies)
    concept = f"<strong>Style:</strong> {film}<br><strong>Concept:</strong> Áp dụng bối cảnh sử thi, trang phục giáp/lụa cổ đại, ánh sáng cinematic kịch tính. Nạp 2 mỏ neo Face DNA."
    
    html_output += f"""
            <tr>
                <td>{count}</td>
                <td><a href="{img_src}" target="_blank"><img src="{img_src}" loading="lazy"></a></td>
                <td class="title">{title}</td>
                <td class="concept">{concept}</td>
            </tr>
    """
    count += 1

html_output += """
        </tbody>
    </table>
</body>
</html>
"""

with open('/Users/vietmac/Documents/CODE/k/check_anh.html', 'w', encoding='utf-8') as f:
    f.write(html_output.replace('{total}', str(count - 1)))

print(f"Generated check_anh.html with {count - 1} images.")
