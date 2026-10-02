import json

shots = [
    {"shot": "1", "image": "shot_01_mid.jpg", "bcontext": "Phòng Khách → Bếp", "action": "Sải bước tiến thẳng về phía máy quay.", "dialogue": "...bắt họ nhìn chằm chằm vào một góc chết.", "tech": ""},
    {"shot": "2", "image": "shot_02_mid.jpg", "bcontext": "Whip Cut (Vung áo)", "action": "Cúi người, vung chiếc tạp dề che thẳng vào mắt máy quay.", "dialogue": "Làm video khoe nghề có 3 cách.", "tech": "[Whip Cut]"},
    {"shot": "3", "image": "shot_03_mid.jpg", "bcontext": "Cạnh Tủ Lạnh", "action": "Đứng nhìn thẳng máy, tay cầm nguyên liệu nấu ăn.", "dialogue": "Cách một là quay hình rồi lồng tiếng. Hình có đẹp nhưng người xem không thấy được con người thật.", "tech": ""},
    {"shot": "4", "image": "shot_04_mid.jpg", "bcontext": "Mask Cut (Lấp máy)", "action": "Cầm cái thớt to hoặc rổ rau lướt ngang lấp kín ống kính.", "dialogue": "Mức hai là ngồi một chỗ chĩa máy vào mặt.", "tech": "[Mask Cut]"},
    {"shot": "5", "image": "shot_05_mid.jpg", "bcontext": "Bàn Ăn", "action": "Ngồi im, trước mặt là đĩa thức ăn tĩnh.", "dialogue": "Cảnh vật đứng im khiến mắt dễ mỏi...", "tech": ""},
    {"shot": "6", "image": "shot_06_mid.jpg", "bcontext": "Bàn Ăn", "action": "Rướn nhẹ người về phía máy quay.", "dialogue": "...người xem lướt đi vì tưởng bạn sắp giảng đạo lý.", "tech": ""},
    {"shot": "7", "image": "shot_07_mid.jpg", "bcontext": "Cận Cảnh (Mặt Bếp)", "action": "Tay đặt nguyên liệu/đồ nghề dứt khoát xuống bàn bếp.", "dialogue": "Để xử lý việc đó, định dạng số ba ra đời:", "tech": ""},
    {"shot": "8", "image": "shot_08_mid.jpg", "bcontext": "Match Cut (Mặt Bếp)", "action": "Cận tay nhấc con dao lên. (Khớp vị trí với Shot 7)", "dialogue": "Vừa đi, vừa nói, tay chân làm việc.", "tech": "[Match Cut]"},
    {"shot": "9", "image": "shot_09_mid.jpg", "bcontext": "Trong Bếp", "action": "Cầm dao đứng thoải mái, nói chuyện.", "dialogue": "Đoạn video bạn đang xem chính là ví dụ.", "tech": ""},
    {"shot": "10", "image": "shot_10_mid.jpg", "bcontext": "Cận Cảnh (Khoảng lặng)", "action": "Quay củ hành/rau nằm tĩnh trên thớt.", "dialogue": "(Khoảng lặng thính giác - Không nói)", "tech": ""},
    {"shot": "11", "image": "shot_11_mid.jpg", "bcontext": "Match Cut", "action": "Tay đưa vào giữ củ hành/rau trên thớt.", "dialogue": "Cơ chế rất dễ hiểu.", "tech": "[Match Cut]"},
    {"shot": "12", "image": "shot_12_mid.jpg", "bcontext": "Trong Bếp", "action": "Bắt đầu thái chậm rãi, thỉnh thoảng liếc nhìn máy.", "dialogue": "Thay vì phông nền tĩnh...", "tech": ""},
    {"shot": "13", "image": "shot_13_mid.jpg", "bcontext": "L-Cut (Bước đi)", "action": "Tay bưng đĩa nguyên liệu vừa thái bước sang khu bếp lò.", "dialogue": "...mỗi bước chân làm không gian thay đổi liên tục.", "tech": "[L-Cut]"},
    {"shot": "14", "image": "shot_14_mid.jpg", "bcontext": "Cận Cảnh (Tay)", "action": "Tay bật công tắc bếp gas (bật lửa lên).", "dialogue": "Chuyển động này tự động níu mắt người xem.", "tech": ""},
    {"shot": "15", "image": "shot_15_mid.jpg", "bcontext": "Góc Trung (Bếp lò)", "action": "Đứng cầm muôi/chảo chuẩn bị xào, nhìn thẳng máy.", "dialogue": "Kết hợp với đôi tay đang thao tác ngay tại chỗ làm...", "tech": ""},
    {"shot": "16", "image": "shot_16_mid.jpg", "bcontext": "Montage 1 (Cận tay)", "action": "Dao phập xuống thớt thái rau củ thật dứt khoát.", "dialogue": "(Tuyệt đối không nói) - Tiếng Cạch Cạch", "tech": "[Montage]"},
    {"shot": "17", "image": "shot_17_mid.jpg", "bcontext": "Montage 2 (Cận chảo)", "action": "Trút rổ rau vào chảo dầu nóng.", "dialogue": "(Tuyệt đối không nói) - Tiếng Xèo Xèo", "tech": "[Montage]"},
    {"shot": "18", "image": "shot_18_mid.jpg", "bcontext": "Montage 3 (Góc ngang)", "action": "Hất chảo lửa bùng lên hoặc đảo thức ăn mạnh tay.", "dialogue": "(Tuyệt đối không nói) - Tiếng Vù Vù", "tech": "[Montage]"},
    {"shot": "19", "image": "shot_19_mid.jpg", "bcontext": "Montage 4 (Cận tay)", "action": "Rắc gia vị từ trên cao xuống.", "dialogue": "(Tuyệt đối không nói) - Tiếng Xào Xạc", "tech": "[Montage]"},
    {"shot": "20", "image": "shot_20_mid.jpg", "bcontext": "Montage 5 (Cận đĩa)", "action": "Trút đồ ăn nóng hổi nghi ngút khói ra đĩa.", "dialogue": "(Tuyệt đối không nói) - Tiếng Xoảng Nhẹ", "tech": "[Montage]"},
    {"shot": "21", "image": "shot_21_mid.jpg", "bcontext": "J-Cut (Nối tiếng)", "action": "Bê đĩa thức ăn nóng hổi lên nhìn máy mỉm cười.", "dialogue": "...lời nói của bạn tuôn ra tự nhiên như đang kể chuyện. (Tiếng vang lên từ cuối Shot 20)", "tech": "[J-Cut]"},
    {"shot": "22", "image": "shot_22_mid.jpg", "bcontext": "Bàn Ăn", "action": "Bước từ bếp mang đồ ăn ra bàn.", "dialogue": "Khách nhìn thấy chỗ làm tươm tất là tự khắc tin tưởng.", "tech": ""},
    {"shot": "23", "image": "shot_23_mid.jpg", "bcontext": "Cận Cảnh (Mặt Bàn)", "action": "Cúi đặt đĩa thức ăn xuống bàn sát máy.", "dialogue": "(Không nói - Âm thanh dứt khoát cạch đĩa xuống bàn)", "tech": ""},
    {"shot": "24", "image": "shot_24_mid.jpg", "bcontext": "Đoạn Kết (Khóa Vòng Lặp)", "action": "Quay ngoắt nhìn thẳng máy.", "dialogue": "Muốn video giữ chân người xem thì đừng bao giờ...", "tech": "[Loop]"}
]

html_parts = []
html_parts.append("""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Walk & Talk Cooking Script - 4 Cuts Mastery</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; background-color: #f8fafc; color: #0f172a; }
        .tiempos { font-family: "Tiempos Text", Georgia, serif; font-size: 19px; line-height: 1.7; }
        .badge { display: inline-flex; align-items: center; padding: 0.25rem 0.625rem; background-color: #f1f5f9; color: #475569; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; border-radius: 0.375rem; border: 1px solid rgba(226, 232, 240, 0.8); box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); margin-top: 0.25rem;}
        .spec-value { font-size: 16px; line-height: 1.625; }
        .inline-badge { position: relative; top: -1px; vertical-align: baseline; padding: 0.125rem 0.375rem; background-color: #dbeafe; color: #1e40af; border: 1px solid #bfdbfe; border-radius: 0.25rem; font-size: 11px; font-family: monospace; font-weight: 700; margin: 0 0.125rem; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); }
    </style>
</head>
<body class="antialiased">
<div class="max-w-4xl mx-auto px-4 py-12">
    <h1 class="text-3xl md:text-4xl font-bold mb-8 uppercase tracking-tight">Kịch Bản Walk & Talk Bếp Nấu Ăn</h1>
    
    <div class="tiempos mb-12">
        <p class="mb-4">Sự tinh tế của định dạng này nằm ở chỗ <strong>khớp nhịp giữa lời nói và hành động</strong>. Đặc biệt ở đoạn Montage B-roll từ Shot 16 đến Shot 20 — bí mật là <strong>Tuyệt đối không nói một từ nào</strong>.</p>
        <p>Đoạn đó gọi là "khoảng nghỉ thính giác". Mượn tiếng động thật của đồ vật làm nhịp điệu để tai khán giả được nghỉ ngơi.</p>
    </div>

    <h2 class="text-2xl font-bold mb-6">Mổ xẻ chi tiết nhịp Thoại & Hành động (Shot 14 - Shot 21)</h2>
    <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm mb-12">
        <div class="mb-6">
            <h3 class="text-lg font-bold mb-3 text-slate-800">1. Trước lúc thái/xào (Báo hiệu hành động)</h3>
            <ul class="list-disc pl-6 space-y-2 text-slate-700 tiempos">
                <li><strong>Shot 14:</strong> Cận tay bật công tắc bếp gas. Miệng nói: <em>"Chuyển động này tự động níu mắt người xem."</em></li>
                <li><strong>Shot 15:</strong> Anh đứng cầm sẵn rổ rau hoặc cái chảo. Thoại: <em>"Kết hợp với đôi tay đang thao tác ngay tại chỗ làm..."</em> (Dứt chữ "làm" là dừng quay).</li>
            </ul>
        </div>
        <div class="mb-6">
            <h3 class="text-lg font-bold mb-3 text-slate-800">2. Trong lúc thái/xào (Câm tiếng thoại)</h3>
            <p class="tiempos text-slate-700 mb-2">Đoạn này anh ngậm miệng lại, không nói một từ nào. Bật to tiếng đồ vật.</p>
        </div>
        <div>
            <h3 class="text-lg font-bold mb-3 text-slate-800">3. Sau khi xào xong (Nối lại tiếng bằng J-Cut)</h3>
            <p class="tiempos text-slate-700 mb-2"><strong>Shot 21:</strong> Khi dựng, đẩy chữ <em>"...lời nói của bạn..."</em> vang lên sớm từ đuôi Shot 20. Hình ảnh chuyển rụp sang mặt anh nói tiếp phần còn lại.</p>
        </div>
    </div>

    <h2 class="text-2xl font-bold mb-8">Danh Sách Phân Cảnh (Shot-list)</h2>
    
    <div class="space-y-12">
""")

for s in shots:
    image_url = f"https://media.fedu.vn/images/IG_@mridupawasharma_Dc0tEcOIdwy_4_cuts_to_instantly_make_your_videos_🔥/{s['image']}"
    tech_badge = f'<span class="inline-badge">{s["tech"]}</span> ' if s["tech"] else ""
    html_parts.append(f"""
        <!-- SHOT {s['shot']} -->
        <div class="border-b border-slate-200 pb-10">
            <div class="flex flex-col md:flex-row gap-6">
                <div class="w-full md:w-1/3 shrink-0">
                    <img src="{image_url}" class="rounded-lg shadow-md w-full object-cover" alt="Shot {s['shot']}">
                </div>
                <div class="w-full md:w-2/3">
                    <div class="flex flex-col sm:flex-row gap-2 sm:gap-4 mb-4 items-start">
                        <div class="shrink-0 sm:min-w-[120px]"><span class="badge">CẢNH {s['shot']}</span></div>
                        <div class="flex-1 spec-value text-slate-800"><code>{tech_badge}{s['bcontext']}</code></div>
                    </div>
                    
                    <ul class="space-y-3">
                        <li>
                            <div class="flex flex-col sm:flex-row gap-2 sm:gap-4 items-start">
                                <div class="shrink-0 sm:min-w-[120px]"><span class="badge">Hành Động</span></div>
                                <div class="flex-1 spec-value text-slate-800">{s['action']}</div>
                            </div>
                        </li>
                        <li>
                            <div class="flex flex-col sm:flex-row gap-2 sm:gap-4 items-start">
                                <div class="shrink-0 sm:min-w-[120px]"><span class="badge">Lời Thoại</span></div>
                                <div class="flex-1 spec-value text-slate-800 font-serif italic text-lg">"{s['dialogue']}"</div>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    """)

html_parts.append("""
    </div>
</div>
</body>
</html>
""")

with open('shot-list-walk-talk-cooking.html', 'w', encoding='utf-8') as f:
    f.write("".join(html_parts))

