import re
import html

# List of known bad images
bad_images = [
    "assets/covers/poster_62.jpg",
    "assets/covers/poster_w1_4.jpg",
    "assets/covers/tu-duy-ai-tu-dong-hoa-science.jpg",
    "assets/covers/poster_30.jpg",
    "assets/covers/poster_80.jpg",
    "assets/covers/co-dep-soleus-la-gi-va-tai-sao-no-dac-biet-science-podcast.jpg",
    "assets/covers/poster_220_fallback.jpg",
    "assets/covers/poster_246.jpg",
    "assets/covers/so-tay-sinh-ton-ky-nguyen-ai-2026-2027-mo-gawdat-podcast.jpg",
    "assets/covers/amcc-book-typo.jpg",
    "assets/covers/system-intelligence-architect-mo-gawdat.jpg",
    "assets/covers/giu-cho-duong-cong-glucose-cua-ban-phang-lang-podcast.jpg",
    "assets/covers/cover_151.jpg",
    "assets/covers/poster_66.jpg",
    "assets/covers/poster_67.jpg",
    "assets/covers/poster_72.jpg",
    "assets/covers/poster_75.jpg",
    "assets/covers/poster_76.jpg",
    "assets/covers/poster_77.jpg",
    "assets/covers/poster_81.jpg",
    "assets/covers/poster_1.jpg",
    "assets/covers/poster_2.jpg",
    "assets/covers/poster_3.jpg",
    "assets/covers/poster_4.jpg",
    "assets/covers/poster_5.jpg",
    "assets/covers/poster_1_severance_1789861213029.jpg",
    "assets/covers/poster_2_kill_la_kill_1789861221590.jpg"
]

with open('/Users/vietmac/Documents/CODE/k/anh.html', 'r', encoding='utf-8') as f:
    content = f.read()

cards = re.findall(r'<div class="card">.*?<img src="(.*?)".*?concept art for &#x27;(.*?)&#x27;.*?</div>', content, re.DOTALL)

# Map img_src to title
img_to_title = {}
for img_src, title_encoded in cards:
    try:
        title = html.unescape(title_encoded.replace(r'\u', '\\u').encode().decode('unicode_escape'))
    except:
        title = title_encoded
    img_to_title[img_src] = title

html_output = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Danh Sách Làm Lại Poster Sai Khuôn Mặt</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #0f172a; color: #f8fafc; padding: 24px; max-width: 1200px; margin: auto; }
        h1, h2 { color: #38bdf8; }
        .description { background-color: #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 24px; border-left: 4px solid #10b981; }
        code { background-color: #334155; padding: 2px 6px; border-radius: 4px; font-family: monospace; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #334155; padding: 12px; text-align: left; vertical-align: middle; }
        th { background-color: #1e293b; color: #94a3b8; }
        tr:nth-child(even) { background-color: #1e293b; }
        img { width: 120px; border-radius: 8px; object-fit: cover; aspect-ratio: 9/16; }
        .concept { color: #10b981; font-weight: 500; }
        .title { font-weight: 600; color: #e2e8f0; font-size: 1.1em; }
        .highlight { color: #facc15; }
    </style>
</head>
<body>
    <h1>Danh Sách Bóc Tách Ảnh Lỗi Cần Làm Lại</h1>
    
    <div class="description">
        <h2>Kế Hoạch & Kỹ Thuật Làm Lại (AI Face Clone)</h2>
        <p><strong>Công nghệ:</strong> Google Imagen 3 Multimodal Inpainting</p>
        <p><strong>Cơ chế Anchor:</strong> Ép nạp 2 ảnh mỏ neo <code>viet_real_master_crop_006.jpg</code> và <code>viet_avatar_002.jpg</code> cho mọi lần sinh ảnh để khóa 100% tỷ lệ khuôn mặt anh Việt.</p>
        <p><strong>Quy chuẩn Prompt:</strong> Sử dụng bộ thông số nhân trắc học: <i>"Vietnamese man, 30s, oval face, high defined cheekbones, expressive almond-shaped dark Asian eyes, radiant confident genuine smile showing upper teeth, signature spiky textured brush-up dark hair."</i></p>
        <p><strong>Áp dụng vũ trụ:</strong> Game of Thrones & Lord of the Rings (Các nhân vật: <span class="highlight">Jon Snow, Aragorn, Jaime Lannister, Legolas, Elrond</span>).</p>
    </div>

    <table>
        <thead>
            <tr>
                <th>STT</th>
                <th>Ảnh Sai Gương Mặt</th>
                <th>Nội Dung Gốc</th>
                <th>Định Hướng Làm Lại (Epic Fantasy Role)</th>
            </tr>
        </thead>
        <tbody>
"""

roles = [
    ("Jon Snow (Game of Thrones)", "Áo choàng lông sói đen khổng lồ, giáp da sờn, bối cảnh tuyết phương Bắc, cầm gươm thép Valyria."),
    ("Aragorn (Lord of the Rings)", "Giáp nhẹ Ranger phong trần, tay cầm kiếm Narsil, bối cảnh rừng rậm u ám."),
    ("Jaime Lannister (Game of Thrones)", "Giáp vàng hoàng gia (Kingsguard), áo choàng trắng tuyết, phong thái kiêu hãnh."),
    ("Legolas (Lord of the Rings)", "Giáp vảy ánh kim/xanh lá, cung tên trên vai, ánh sáng sương mù rừng thiêng."),
    ("Daemon Targaryen (House of the Dragon)", "Giáp vảy rồng đen-đỏ sắc lẹm, bối cảnh lâu đài đá núi lửa Dragonstone."),
    ("Elrond (Lord of the Rings)", "Áo choàng lụa nhung hoàng gia thêu chỉ vàng, uy nghi, thông thái.")
]

import random
for idx, img_src in enumerate(bad_images):
    title = img_to_title.get(img_src, "Không tìm thấy nội dung")
    role_name, role_desc = roles[idx % len(roles)]
    
    html_output += f"""
            <tr>
                <td>{idx + 1}</td>
                <td><a href="{img_src}" target="_blank"><img src="{img_src}" loading="lazy"></a></td>
                <td class="title">{title}</td>
                <td class="concept">
                    <strong>Vai diễn:</strong> {role_name}<br>
                    <strong>Trang phục & Bối cảnh:</strong> {role_desc}<br>
                    <strong>Khóa Mỏ Neo:</strong> Face DNA (Viet_Real_Master_Crop_006)
                </td>
            </tr>
    """

html_output += """
        </tbody>
    </table>
</body>
</html>
"""

with open('/Users/vietmac/Documents/CODE/k/rework_plan.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("Generated rework_plan.html")
