#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hệ thống sinh Logo Monogram vuông chuẩn brand.html cho 38 tài khoản Gmail của anh Việt.
Sử dụng trực tiếp font FD Anguita Sans Black trích xuất vector path chính xác từng glyph.
Tọa độ quang học: 64x64, rx=16, Signature Dot cx=52.0, cy=13.0, r=4.2.
"""

import os
import json
import re
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONT_PATH = '/Users/vietmac/Library/Fonts/FDAnguitaSans-Black.ttf'
OUT_SVG_DIR = '/Users/vietmac/Documents/CODE/k/assets/logos/gmail'
OUT_JSON_PATH = '/Users/vietmac/Documents/CODE/k/gmail_assets.json'
OUT_HTML_PATH = '/Users/vietmac/Documents/CODE/k/gmail_brand.html'
OUT_PNG_DIR = '/Users/vietmac/Documents/CODE/k/assets/logos/gmail/png'

os.makedirs(OUT_SVG_DIR, exist_ok=True)
os.makedirs(OUT_PNG_DIR, exist_ok=True)

# Nạp font
font = TTFont(FONT_PATH)
cmap = font.getBestCmap()
glyph_set = font.getGlyphSet()
hmtx = font['hmtx']

# 38 Tài khoản theo dữ liệu của anh Việt
ACCOUNTS = [
    {
        "id": "vietndj",
        "email": "vietndj@gmail.com",
        "pass": "(Master Account)",
        "code": "VJ",
        "color": "#EF4444",
        "color_name": "Crimson Master",
        "name": "vietndj",
        "desc": "Tài khoản Master Cốt Lõi • Nguyễn Việt (Quản Trị Hệ Thống)",
        "category": "core",
        "status": "active",
        "note": "Tài khoản chính điều hành toàn bộ hệ sinh thái fedu.vn, GitHub, Drive."
    },
    {
        "id": "vietnd4",
        "email": "vietnd4@gmail.com",
        "pass": "bongbong3",
        "code": "04",
        "color": "#38BDF8",
        "color_name": "Sky Blue Neon",
        "name": "vietnd4",
        "desc": "Tài khoản Vệ Tinh Số 04",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "vietnd5",
        "email": "vietnd5@gmail.com",
        "pass": "bongbong2",
        "code": "05",
        "color": "#10B981",
        "color_name": "Emerald Green",
        "name": "vietnd5",
        "desc": "Tài khoản Vệ Tinh Số 05",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong2"
    },
    {
        "id": "vietnd6",
        "email": "vietnd6@gmail.com",
        "pass": "bongbong2",
        "code": "06",
        "color": "#FB923C",
        "color_name": "Flame Orange",
        "name": "vietnd6",
        "desc": "Tài khoản Vệ Tinh Số 06",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong2"
    },
    {
        "id": "vietnd7",
        "email": "vietnd7@gmail.com",
        "pass": "bongbong",
        "code": "07",
        "color": "#A855F7",
        "color_name": "Neon Purple",
        "name": "vietnd7",
        "desc": "Tài khoản Vệ Tinh Số 07",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong"
    },
    {
        "id": "vietnd8",
        "email": "vietnd8@gmail.com",
        "pass": "bongbong",
        "code": "08",
        "color": "#EAB308",
        "color_name": "Cyber Gold",
        "name": "vietnd8",
        "desc": "Tài khoản Vệ Tinh Số 08 (Xác minh số Nga macOS)",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong -> Xác minh bằng số Nga trên Mac"
    },
    {
        "id": "vietnd9",
        "email": "vietnd9@gmail.com",
        "pass": "bongbong",
        "code": "09",
        "color": "#EC4899",
        "color_name": "Hot Pink",
        "name": "vietnd9",
        "desc": "Tài khoản Vệ Tinh Số 09 (Xác minh bằng SĐT)",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong -> Xác minh bằng số ĐT"
    },
    {
        "id": "vietnd10",
        "email": "vietnd10@gmail.com",
        "pass": "bongbong",
        "code": "10",
        "color": "#06B6D4",
        "color_name": "Cyan Teal",
        "name": "vietnd10",
        "desc": "Tài khoản Vệ Tinh Số 10",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong"
    },
    {
        "id": "vietnd011",
        "email": "vietnd011@gmail.com",
        "pass": "Chưa có",
        "code": "11",
        "color": "#64748B",
        "color_name": "Slate Muted",
        "name": "vietnd011",
        "desc": "Tài khoản Số 11 (Chưa khởi tạo)",
        "category": "satellite",
        "status": "inactive",
        "note": "Hiện tại không có tài khoản này"
    },
    {
        "id": "vietnd012",
        "email": "vietnd012@gmail.com",
        "pass": "bongbong3",
        "code": "12",
        "color": "#8B5CF6",
        "color_name": "Electric Violet",
        "name": "vietnd012",
        "desc": "Tài khoản Vệ Tinh Số 12",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "vietnd013",
        "email": "vietnd013@gmail.com",
        "pass": "bongbong2",
        "code": "13",
        "color": "#14B8A6",
        "color_name": "Mint Teal",
        "name": "vietnd013",
        "desc": "Tài khoản Vệ Tinh Số 13",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong2"
    },
    {
        "id": "vietnd014",
        "email": "vietnd014@gmail.com",
        "pass": "bongbong2",
        "code": "14",
        "color": "#F43F5E",
        "color_name": "Rose Coral",
        "name": "vietnd014",
        "desc": "Tài khoản Vệ Tinh Số 14",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong2"
    },
    {
        "id": "vietnd015",
        "email": "vietnd015@gmail.com",
        "pass": "Đã bị xóa",
        "code": "15",
        "color": "#475569",
        "color_name": "Dark Slate",
        "name": "vietnd015",
        "desc": "Tài khoản Số 15 (Đã xóa / Mất SIM)",
        "category": "satellite",
        "status": "inactive",
        "note": "Tài khoản bị xóa, SĐT đuôi 42 không còn nữa"
    },
    {
        "id": "vietnd016",
        "email": "vietnd016@gmail.com",
        "pass": "bongbong2",
        "code": "16",
        "color": "#84CC16",
        "color_name": "Lime Green",
        "name": "vietnd016",
        "desc": "Tài khoản Vệ Tinh Số 16",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong2"
    },
    {
        "id": "vietnd017",
        "email": "vietnd017@gmail.com",
        "pass": "bongbong2",
        "code": "17",
        "color": "#6366F1",
        "color_name": "Indigo Electric",
        "name": "vietnd017",
        "desc": "Tài khoản Vệ Tinh Số 17",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong2"
    },
    {
        "id": "vietnd018",
        "email": "vietnd018@gmail.com",
        "pass": "bongbong2",
        "code": "18",
        "color": "#F97316",
        "color_name": "Bright Orange",
        "name": "vietnd018",
        "desc": "Tài khoản Vệ Tinh Số 18",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong2"
    },
    {
        "id": "vietnd019",
        "email": "vietnd019@gmail.com",
        "pass": "bongbong3",
        "code": "19",
        "color": "#3B82F6",
        "color_name": "Royal Blue",
        "name": "Vietnd019",
        "desc": "Tài khoản Vệ Tinh Số 19",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "vietnd020",
        "email": "vietnd020@gmail.com",
        "pass": "bongbong3",
        "code": "20",
        "color": "#22C55E",
        "color_name": "Vibrant Green",
        "name": "vietnd020",
        "desc": "Tài khoản Vệ Tinh Số 20",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "vietnd021",
        "email": "vietnd021@gmail.com",
        "pass": "Chưa có",
        "code": "21",
        "color": "#64748B",
        "color_name": "Slate Muted",
        "name": "Vietnd021",
        "desc": "Tài khoản Số 21 (Chưa khởi tạo)",
        "category": "satellite",
        "status": "inactive",
        "note": "Hiện tại không có tài khoản này"
    },
    {
        "id": "vietnd022",
        "email": "vietnd022@gmail.com",
        "pass": "bongbong3",
        "code": "22",
        "color": "#D946EF",
        "color_name": "Neon Fuchsia",
        "name": "Vietnd022",
        "desc": "Tài khoản Vệ Tinh Số 22",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "vietnd023",
        "email": "vietnd023@gmail.com",
        "pass": "Chưa có",
        "code": "23",
        "color": "#64748B",
        "color_name": "Slate Muted",
        "name": "Vietnd023",
        "desc": "Tài khoản Số 23 (Chưa khởi tạo)",
        "category": "satellite",
        "status": "inactive",
        "note": "Hiện tại không có tài khoản này"
    },
    {
        "id": "vietnd024",
        "email": "vietnd024@gmail.com",
        "pass": "bongbong3",
        "code": "24",
        "color": "#0EA5E9",
        "color_name": "Deep Ocean",
        "name": "Vietnd024",
        "desc": "Tài khoản Vệ Tinh Số 24",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "vietnd025",
        "email": "vietnd025@gmail.com",
        "pass": "bongbong3",
        "code": "25",
        "color": "#E11D48",
        "color_name": "Ruby Red",
        "name": "vietnd025",
        "desc": "Tài khoản Vệ Tinh Số 25",
        "category": "satellite",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "nddviet",
        "email": "nddviet@gmail.com",
        "pass": "bongbong2",
        "code": "ND",
        "color": "#F59E0B",
        "color_name": "Amber Gold",
        "name": "nddviet",
        "desc": "Nguyễn Đắc Doãn Việt • Profile Cá Nhân Master",
        "category": "core",
        "status": "active",
        "note": "Pass: bongbong2 • Đầy đủ họ tên NDD Việt"
    },
    {
        "id": "aidesginforwork",
        "email": "aidesginforwork@gmail.com",
        "pass": "aidesginforwork01@",
        "code": "AI",
        "color": "#A855F7",
        "color_name": "AI Intelligence",
        "name": "aidesginforwork",
        "desc": "AI Design For Work • Tooling & Tự Động Hóa Đồ Họa",
        "category": "specialized",
        "status": "active",
        "note": "Pass: aidesginforwork01@ • Chuyên thiết kế AI & Automation"
    },
    {
        "id": "poiu861004",
        "email": "poiu861004@gmail.com",
        "pass": "bongbong3",
        "code": "PO",
        "color": "#64748B",
        "color_name": "Slate Steel",
        "name": "poiu861004",
        "desc": "Tài khoản Dự Phòng Cá Nhân (04/10/1986)",
        "category": "personal",
        "status": "active",
        "note": "Pass: bongbong3 • Backup & Security"
    },
    {
        "id": "vocuaviet01",
        "email": "vocuaviet01@gmail.com",
        "pass": "bongbong3",
        "code": "VV",
        "color": "#FB7185",
        "color_name": "Rose Blossom",
        "name": "vocuaviet01",
        "desc": "Vợ Của Việt 01 • Tài Khoản Gia Đình",
        "category": "personal",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "milkkiuti01",
        "email": "milkkiuti01@gmail.com",
        "pass": "bongbong3",
        "code": "M1",
        "color": "#F472B6",
        "color_name": "Pastel Pink",
        "name": "milkkiuti01",
        "desc": "Milkkiuti 01 • Channel & Profile Sáng Tạo",
        "category": "personal",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "milkkiuti02",
        "email": "milkkiuti02@gmail.com",
        "pass": "bongbong3",
        "code": "M2",
        "color": "#EC4899",
        "color_name": "Vibrant Pink",
        "name": "milkkiuti02",
        "desc": "Milkkiuti 02 • Channel & Profile Sáng Tạo Phụ",
        "category": "personal",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "autumnnn2016",
        "email": "autumnnn2016@gmail.com",
        "pass": "bongbong3",
        "code": "AU",
        "color": "#D97706",
        "color_name": "Warm Autumn",
        "name": "autumnnn2016",
        "desc": "Autumn 2016 • Kỷ Niệm Mùa Thu",
        "category": "personal",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "nguyengiahan0715",
        "email": "nguyengiahan0715@gmail.com",
        "pass": "bongbong3",
        "code": "GH",
        "color": "#C084FC",
        "color_name": "Soft Lavender",
        "name": "nguyengiahan0715",
        "desc": "Nguyễn Gia Hân (15/07) • Tài Khoản Gia Đình",
        "category": "personal",
        "status": "active",
        "note": "Pass: bongbong3"
    },
    {
        "id": "vietndluutruanh",
        "email": "vietndluutruanh@gmail.com",
        "pass": "bongbong3",
        "code": "VA",
        "color": "#10B981",
        "color_name": "Photos Green",
        "name": "vietndluutruanh",
        "desc": "Việt Lưu Trữ Ảnh • Google Photos & Drive Master",
        "category": "specialized",
        "status": "active",
        "note": "Pass: bongbong3 • Lưu trữ ảnh tư liệu & gia đình"
    },
    {
        "id": "vietndseo01",
        "email": "vietndseo01@gmail.com",
        "pass": "bongbong",
        "code": "S1",
        "color": "#2563EB",
        "color_name": "Search Royal Blue",
        "name": "vietndseo01",
        "desc": "Việt ND SEO 01 • Tối Ưu Hóa Tìm Kiếm Google",
        "category": "specialized",
        "status": "active",
        "note": "Pass: bongbong • Chuyên quản trị SEO Google Search"
    },
    {
        "id": "vietndseo02",
        "email": "vietndseo02@gmail.com",
        "pass": "bongbong",
        "code": "S2",
        "color": "#1D4ED8",
        "color_name": "Deep Sea Blue",
        "name": "vietndseo02",
        "desc": "Việt ND SEO 02 • Tối Ưu Hóa Tìm Kiếm Vệ Tinh",
        "category": "specialized",
        "status": "active",
        "note": "Pass: bongbong • SEO vệ tinh & index"
    },
    {
        "id": "vietnd0410",
        "email": "vietnd0410@gmail.com",
        "pass": "bongbong",
        "code": "41",
        "color": "#0D9488",
        "color_name": "Dark Teal",
        "name": "vietnd0410",
        "desc": "Việt ND 0410 • Kỷ Niệm Ngày Sinh Nhật (04/10)",
        "category": "personal",
        "status": "active",
        "note": "Pass: bongbong"
    },
    {
        "id": "edumallweb05",
        "email": "edumallweb05@gmail.com",
        "pass": "bongbong2",
        "code": "ED",
        "color": "#EA580C",
        "color_name": "Edumall Orange",
        "name": "edumallweb05",
        "desc": "Edumall Web 05 • Kênh Đào Tạo Khóa Học Trực Tuyến",
        "category": "specialized",
        "status": "active",
        "note": "Pass: bongbong2 • Nền tảng Edumall khóa học"
    },
    {
        "id": "feduvn",
        "email": "feduvn@gmail.com",
        "pass": "(Liên kết Fedu)",
        "code": "FD",
        "color": "#EF4444",
        "color_name": "FEDU Crimson",
        "name": "feduvn",
        "desc": "FEDU VN • Cổng Chính Video Studio & Học Viện",
        "category": "specialized",
        "status": "active",
        "note": "Cổng Fedu.vn chính thức"
    },
    {
        "id": "deisgn",
        "email": "deisgn@gmail.com",
        "pass": "(Liên kết Studio)",
        "code": "DS",
        "color": "#8B5CF6",
        "color_name": "Design Violet",
        "name": "deisgn",
        "desc": "Design Studio • Kênh Đồ Họa, Mockup & Typography",
        "category": "specialized",
        "status": "active",
        "note": "Profile thiết kế & sáng tạo đồ họa"
    }
]

def render_vector_path(text):
    """Trích xuất vector path chính xác từ FDAnguitaSans-Black.ttf và căn giữa quang học"""
    glyph_records = []
    total_advance = 0
    
    for ch in text:
        if ord(ch) not in cmap:
            continue
        gid = cmap[ord(ch)]
        glyph = glyph_set[gid]
        bp = BoundsPen(glyph_set)
        glyph.draw(bp)
        adv, lsb = hmtx[gid]
        bounds = bp.bounds if bp.bounds else (0, 0, adv, 706)
        glyph_records.append({
            'char': ch,
            'gid': gid,
            'glyph': glyph,
            'bounds': bounds,
            'adv': adv,
            'x_offset': total_advance
        })
        total_advance += adv
        
    if not glyph_records:
        return ""
        
    min_x = glyph_records[0]['bounds'][0] + glyph_records[0]['x_offset']
    max_x = glyph_records[-1]['bounds'][2] + glyph_records[-1]['x_offset']
    min_y = min(r['bounds'][1] for r in glyph_records)
    max_y = max(r['bounds'][3] for r in glyph_records)
    
    font_w = max_x - min_x
    font_h = max_y - min_y
    
    # Chuẩn kích thước theo độ dài ký tự
    if len(text) == 1:
        target_h = 43.5
        target_w = 44.0
        target_cx = 28.0
        target_cy = 32.5
    elif len(text) == 2:
        target_h = 42.5
        target_w = 46.5
        target_cx = 29.5
        target_cy = 32.5
    else:
        target_h = 40.0
        target_w = 46.0
        target_cx = 30.5
        target_cy = 32.5
        
    scale_y = target_h / font_h
    scale_x = target_w / font_w
    scale = min(scale_x, scale_y)
    
    # Giới hạn scale tối đa
    if scale > 43.5 / 706:
        scale = 43.5 / 706
        
    actual_w = font_w * scale
    actual_h = font_h * scale
    
    tx = target_cx - (min_x + font_w / 2.0) * scale
    ty = target_cy + (max_y + min_y) / 2.0 * scale
    
    combined = []
    for r in glyph_records:
        spen = SVGPathPen(glyph_set)
        gx = tx + r['x_offset'] * scale
        tpen = TransformPen(spen, (scale, 0, 0, -scale, gx, ty))
        r['glyph'].draw(tpen)
        cmd = spen.getCommands()
        if cmd:
            combined.append(cmd)
            
    return " ".join(combined)

# Tiến hành sinh toàn bộ 38 tài khoản
processed_data = []

print(f"🚀 Bắt đầu sinh logo Monogram cho {len(ACCOUNTS)} tài khoản Gmail...")

for acc in ACCOUNTS:
    code = acc['code']
    color = acc['color']
    slug = acc['id']
    
    path_d = render_vector_path(code)
    
    # 1. Dark mode SVG (Chuẩn Y Hacker News)
    svg_dark = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect width="64" height="64" rx="16" fill="#07090E"/>
  <path d="{path_d}" fill="{color}"/>
  <circle cx="52.0" cy="13.0" r="4.2" fill="{color}"/>
</svg>"""

    # 2. Solid mode SVG (Chuẩn Adobe)
    svg_solid = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect width="64" height="64" rx="16" fill="{color}"/>
  <path d="{path_d}" fill="#FFFFFF"/>
  <circle cx="52.0" cy="13.0" r="4.2" fill="#FFFFFF"/>
</svg>"""

    # Data URI
    from urllib.parse import quote
    uri_dark = "data:image/svg+xml," + quote(svg_dark.strip())
    uri_solid = "data:image/svg+xml," + quote(svg_solid.strip())
    
    # Ghi tệp SVG cục bộ
    svg_dark_path = os.path.join(OUT_SVG_DIR, f"{slug}_dark.svg")
    svg_solid_path = os.path.join(OUT_SVG_DIR, f"{slug}_solid.svg")
    
    with open(svg_dark_path, "w", encoding="utf-8") as f:
        f.write(svg_dark)
    with open(svg_solid_path, "w", encoding="utf-8") as f:
        f.write(svg_solid)
        
    item = dict(acc)
    item['path_d'] = path_d
    item['svg_dark'] = svg_dark
    item['svg_solid'] = svg_solid
    item['uri_dark'] = uri_dark
    item['uri_solid'] = uri_solid
    item['file_dark'] = f"assets/logos/gmail/{slug}_dark.svg"
    item['file_solid'] = f"assets/logos/gmail/{slug}_solid.svg"
    
    processed_data.append(item)
    print(f"  ✓ {acc['id']:16} | Code: {code:3} | {acc['color_name']} | Dark & Solid SVG")

# Lưu JSON database
with open(OUT_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(processed_data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Đã lưu cơ sở dữ liệu tài nguyên: {OUT_JSON_PATH}")
