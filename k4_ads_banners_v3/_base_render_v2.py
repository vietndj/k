import os
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

OUT_DIR = "/Users/vietmac/Documents/CODE/k/k4_ads_banners_v2"
os.makedirs(OUT_DIR, exist_ok=True)

FONT_DIR = "/Users/vietmac/Documents/CODE/k/fonts"
F_BLACK = os.path.join(FONT_DIR, "FDAeonik-Black.ttf")
F_BOLD = os.path.join(FONT_DIR, "FDAeonik-Bold.ttf")
F_MED = os.path.join(FONT_DIR, "FDAeonik-Medium.ttf")
F_REG = os.path.join(FONT_DIR, "FDAeonik-Regular.ttf")

SRC_DIR = "/tmp/k4_clean_portraits"

def font(path, size):
    return ImageFont.truetype(path, size)

def draw_mixed_line(draw, x, y, segments, fnt):
    cur_x = x
    for text, color in segments:
        draw.text((cur_x, y), text, font=fnt, fill=color)
        bbox = draw.textbbox((cur_x, y), text, font=fnt)
        cur_x = bbox[2]
    return cur_x

def draw_dashed_rect(draw, box, radius, color, width=2, dash_len=10, gap_len=7):
    x1, y1, x2, y2 = box
    # Top and bottom horizontal dashed lines
    for x in range(x1 + radius, x2 - radius, dash_len + gap_len):
        ex = min(x + dash_len, x2 - radius)
        draw.line([(x, y1), (ex, y1)], fill=color, width=width)
        draw.line([(x, y2), (ex, y2)], fill=color, width=width)
    # Left and right vertical dashed lines
    for y in range(y1 + radius, y2 - radius, dash_len + gap_len):
        ey = min(y + dash_len, y2 - radius)
        draw.line([(x1, y), (x1, ey)], fill=color, width=width)
        draw.line([(x2, y), (x2, ey)], fill=color, width=width)

def prepare_portrait_canvas(img_name, centering=(0.5, 0.42), grad_start=580, top_h=840, panel_rgb=(15, 20, 30), mode="fit"):
    W, H = 1080, 1350
    src = Image.open(os.path.join(SRC_DIR, img_name)).convert("RGBA")
    canvas = Image.new("RGBA", (W, H), (*panel_rgb, 255))

    if mode == "studio_full":
        # Scale 896x1200 -> 800x1071 so full head + torso + hands + phone fit within y=0..730!
        target_w = 800
        target_h = int(src.height * (target_w / float(src.width)))
        scaled = src.resize((target_w, target_h), Image.Resampling.LANCZOS)
        # Fill full 1080x900 background by stretching left/right 20px studio wall strips smoothly
        bg_top = Image.new("RGBA", (W, target_h))
        pad_left = (W - target_w) // 2
        pad_right = W - target_w - pad_left
        left_strip = scaled.crop((0, 0, 12, target_h)).resize((pad_left, target_h), Image.Resampling.BICUBIC)
        right_strip = scaled.crop((target_w - 12, 0, target_w, target_h)).resize((pad_right, target_h), Image.Resampling.BICUBIC)
        bg_top.paste(left_strip, (0, 0))
        bg_top.paste(scaled, (pad_left, 0))
        bg_top.paste(right_strip, (pad_left + target_w, 0))
        canvas.paste(bg_top, (0, -18))
        top_h = 820
        grad_start = 630
    else:
        bg_top = ImageOps.fit(src, (W, top_h), method=Image.Resampling.LANCZOS, centering=centering)
        canvas.paste(bg_top, (0, 0))

    # Smooth gradient from grad_start to top_h
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for y in range(grad_start, top_h):
        t = (y - grad_start) / float(top_h - grad_start)
        alpha = int(min(255, (t ** 1.15) * 255))
        od.line([(0, y), (W, y)], fill=(*panel_rgb, alpha))
    od.rectangle((0, top_h, W, H), fill=(*panel_rgb, 255))
    canvas = Image.alpha_composite(canvas, overlay)

    draw = ImageDraw.Draw(canvas)
    # Top-left badge (Consistent across all banners)
    draw.rounded_rectangle((44, 36, 520, 92), radius=28, fill=(13, 18, 28, 215), outline=(251, 191, 36, 200), width=2)
    draw.ellipse((68, 56, 84, 72), fill=(251, 191, 36, 255))
    draw.text((98, 49), "LỚP LÀM VIDEO 2 NGÀY · HÀ NỘI", font=font(F_BOLD, 24), fill=(248, 250, 252, 255))
    return canvas, draw

def draw_footer_bar(draw, W, card_bottom=1314):
    y_bar = card_bottom - 76
    draw.line([(72, y_bar - 14), (W - 72, y_bar - 14)], fill=(51, 65, 85, 210), width=2)
    draw.rounded_rectangle((72, y_bar, 412, y_bar + 56), radius=12, fill=(251, 191, 36, 255))
    draw.text((92, y_bar + 14), "THỨ 7 & CN · 07–08/11", font=font(F_BLACK, 24), fill=(15, 23, 42, 255))
    draw.text((432, y_bar + 14), "Tại Hà Nội · Ngày 1 không hợp, hoàn 100% học phí", font=font(F_BOLD, 24), fill=(241, 245, 249, 255))

# ==============================================================================
# BANNER 1 - PA1: THẺ GIẢI PHẪU (k2_charcoal.jpg)
# ==============================================================================
def build_b1_pa1():
    W, H = 1080, 1350
    canvas, draw = prepare_portrait_canvas("k2_charcoal.jpg", panel_rgb=(14, 18, 26), mode="studio_full")

    card_top = 730
    draw.rounded_rectangle((36, card_top, W - 36, 1318), radius=28, fill=(20, 26, 38, 246), outline=(251, 191, 36, 130), width=2)
    draw.rounded_rectangle((76, card_top, 340, card_top + 6), radius=3, fill=(251, 191, 36, 255))

    # Title
    draw_mixed_line(draw, 72, card_top + 28, [
        ("68 NGƯỜI HỎI HỌC. ", (255, 255, 255, 255)),
        ("KHÔNG AI NHẮN TIN.", (251, 191, 36, 255)),
    ], font(F_BLACK, 45))

    # Subtitle
    draw.text((72, card_top + 88), "Video làm bánh kem 200.000 người xem. Vì sao không ai nhắn?", font=font(F_MED, 27), fill=(148, 163, 184, 255))

    # 3 Diagnostic Rows
    rows = [
        ("MỞ ĐẦU", (239, 68, 68, 255), (69, 26, 30, 230), "3 giây đầu:", "Không nói mình là ai, dạy cho ai."),
        ("Ở GIỮA", (52, 211, 153, 255), (16, 58, 48, 230), "Phần làm bánh:", "Đôi tay bắt bông kem rất đẹp."),
        ("CUỐI", (251, 191, 36, 255), (66, 48, 18, 230), "Câu kết:", "Tắt phụp, không dặn nhắn vào đâu."),
    ]
    ry = card_top + 140
    for badge_txt, b_col, bg_col, bold_lbl, desc_txt in rows:
        draw.rounded_rectangle((72, ry, W - 72, ry + 78), radius=16, fill=(30, 41, 59, 210), outline=(51, 65, 85, 200), width=1)
        # Status pill
        draw.rounded_rectangle((88, ry + 16, 234, ry + 62), radius=10, fill=bg_col, outline=b_col, width=2)
        draw.text((108, ry + 26), badge_txt, font=font(F_BLACK, 22), fill=b_col)
        # Label + explanation
        end_x = draw_mixed_line(draw, 254, ry + 23, [
            (bold_lbl + " ", (255, 255, 255, 255)),
            (desc_txt, (226, 232, 240, 255))
        ], font(F_MED, 27))
        ry += 92

    # Diagnostic conclusion line
    draw.text((72, ry + 6), "→ Sáng ngày 1: mình xem video của bạn, chỉ đúng chỗ hở và sửa ngay.", font=font(F_BOLD, 25), fill=(251, 191, 36, 255))

    draw_footer_bar(draw, W, 1318)
    out = os.path.join(OUT_DIR, "k4_v2_b1_pa1_giaiphau.jpg")
    canvas.convert("RGB").save(out, quality=95)
    print("Saved:", out)

# ==============================================================================
# BANNER 1 - PA2: TRỤC 3 NẤC (k2_charcoal.jpg)
# ==============================================================================
def build_b1_pa2():
    W, H = 1080, 1350
    canvas, draw = prepare_portrait_canvas("k2_charcoal.jpg", panel_rgb=(14, 18, 26), mode="studio_full")

    card_top = 730
    draw.rounded_rectangle((36, card_top, W - 36, 1318), radius=28, fill=(20, 26, 38, 246), outline=(251, 191, 36, 130), width=2)
    draw.rounded_rectangle((76, card_top, 340, card_top + 6), radius=3, fill=(251, 191, 36, 255))

    draw_mixed_line(draw, 72, card_top + 28, [
        ("ĐƯỢC XEM ", (255, 255, 255, 255)),
        ("CHƯA PHẢI ", (148, 163, 184, 255)),
        ("ĐƯỢC HỎI MUA", (251, 191, 36, 255)),
    ], font(F_BLACK, 46))

    draw.text((72, card_top + 88), "Video 2,6 triệu lượt xem vẫn trôi tuột nếu thiếu nấc 2 và nấc 3:", font=font(F_MED, 27), fill=(148, 163, 184, 255))

    steps = [
        ("NẤC 1 · ĐƯỢC XEM", "Tay nghề đẹp hoặc quay 1 mạch trôi chảy", "Phần lớn kênh dừng ở đây", (148, 163, 184, 255)),
        ("NẤC 2 · ĐƯỢC NHỚ", "Câu neo 3 giây đầu + khoảng lặng 1,5 giây", "Khách nhớ rõ bạn là ai", (56, 189, 248, 255)),
        ("NẤC 3 · ĐƯỢC HỎI MUA", "Điểm đậu 5 giây cuối + cảnh bằng chứng", "Khách chủ động nhắn riêng", (251, 191, 36, 255)),
    ]
    ry = card_top + 140
    for st_title, st_desc, st_tag, col in steps:
        draw.rounded_rectangle((72, ry, W - 72, ry + 78), radius=16, fill=(30, 41, 59, 215), outline=col, width=2)
        draw.text((92, ry + 12), st_title, font=font(F_BLACK, 22), fill=col)
        draw.text((92, ry + 42), st_desc, font=font(F_MED, 25), fill=(241, 245, 249, 255))
        # Right tag pill
        tw = draw.textbbox((0, 0), st_tag, font=font(F_BOLD, 21))[2] + 32
        draw.rounded_rectangle((W - 92 - tw, ry + 20, W - 92, ry + 58), radius=10, fill=(15, 23, 42, 230))
        draw.text((W - 92 - tw + 16, ry + 27), st_tag, font=font(F_BOLD, 21), fill=col)
        ry += 92

    draw.text((72, ry + 6), "→ Chuyển từ phép cộng (quay 1 vạch) sang phép nhân Hình – Lời – Âm.", font=font(F_BOLD, 25), fill=(251, 191, 36, 255))

    draw_footer_bar(draw, W, 1318)
    out = os.path.join(OUT_DIR, "k4_v2_b1_pa2_banac.jpg")
    canvas.convert("RGB").save(out, quality=95)
    print("Saved:", out)

# ==============================================================================
# BANNER 2 - PA1: THANG 3 BẬC LỘ MẶT (k16_deepwork1.jpg)
# ==============================================================================
def build_b2_pa1():
    W, H = 1080, 1350
    canvas, draw = prepare_portrait_canvas("k16_deepwork1.jpg", centering=(0.5, 0.08), grad_start=600, top_h=820, panel_rgb=(15, 20, 28), mode="fit")

    card_top = 720
    draw.rounded_rectangle((36, card_top, W - 36, 1318), radius=28, fill=(21, 28, 40, 248), outline=(52, 211, 153, 140), width=2)
    draw.rounded_rectangle((76, card_top, 360, card_top + 6), radius=3, fill=(52, 211, 153, 255))

    draw_mixed_line(draw, 72, card_top + 24, [
        ("BẬT CAMERA LÀ ", (255, 255, 255, 255)),
        ("CỨNG MẶT, QUÊN LỜI?", (251, 191, 36, 255)),
    ], font(F_BLACK, 44))
    draw_mixed_line(draw, 72, card_top + 76, [
        ("NGÀY 1 ", (52, 211, 153, 255)),
        ("CHƯA CẦN LỘ MẶT.", (255, 255, 255, 255)),
    ], font(F_BLACK, 44))

    rows = [
        ("NGÀY 1", (52, 211, 153, 255), "Chỉ quay đôi tay làm nghề:", "Đọc lời bình ghép sau. Hết ngày 1 có ngay 1 video."),
        ("NGÀY 2", (251, 191, 36, 255), "Ngồi nói trước 2 điện thoại:", "Nói từng câu ngắn, đổi góc máy là che hết chỗ vấp."),
        ("VỀ NHÀ", (56, 189, 248, 255), "Quên nút bấm CapCut?", "Mở video hướng dẫn xem lại, có nhóm Zalo kèm tiếp."),
    ]
    ry = card_top + 142
    for badge_txt, col, b_lbl, desc_txt in rows:
        draw.rounded_rectangle((72, ry, W - 72, ry + 82), radius=16, fill=(30, 41, 59, 220), outline=(51, 65, 85, 200), width=1)
        draw.rounded_rectangle((88, ry + 18, 222, ry + 64), radius=10, fill=(15, 23, 42, 240), outline=col, width=2)
        draw.text((106, ry + 28), badge_txt, font=font(F_BLACK, 22), fill=col)
        draw.text((242, ry + 14), b_lbl, font=font(F_BOLD, 25), fill=col)
        draw.text((242, ry + 45), desc_txt, font=font(F_MED, 24), fill=(241, 245, 249, 255))
        ry += 96

    draw.text((72, ry + 4), "→ Giỏi nghề mà ngại ống kính: đi từng bậc, không ép học thuộc.", font=font(F_BOLD, 25), fill=(52, 211, 153, 255))

    draw_footer_bar(draw, W, 1318)
    out = os.path.join(OUT_DIR, "k4_v2_b2_pa1_thang3bac.jpg")
    canvas.convert("RGB").save(out, quality=95)
    print("Saved:", out)

# ==============================================================================
# BANNER 2 - PA2: ĐỐI CHIẾU NGOÀI ĐỜI vs TRƯỚC CAMERA (k3_black_suit.jpg)
# ==============================================================================
def build_b2_pa2():
    W, H = 1080, 1350
    canvas, draw = prepare_portrait_canvas("k16_deepwork2.jpg", centering=(0.5, 0.08), grad_start=600, top_h=820, panel_rgb=(13, 19, 32), mode="fit")

    card_top = 720
    draw.rounded_rectangle((36, card_top, W - 36, 1318), radius=28, fill=(19, 28, 46, 248), outline=(251, 191, 36, 140), width=2)
    draw.rounded_rectangle((76, card_top, 360, card_top + 6), radius=3, fill=(251, 191, 36, 255))

    draw.text((72, card_top + 24), "TƯ VẤN 2 TIẾNG KHÔNG VẤP.", font=font(F_BLACK, 44), fill=(255, 255, 255, 255))
    draw.text((72, card_top + 76), "BẬT CAMERA 30 GIÂY LÀ CỨNG MẶT.", font=font(F_BLACK, 44), fill=(251, 191, 36, 255))

    # 2 Columns comparison (y = card_top + 142 .. card_top + 382)
    col_y = card_top + 142
    col_h = 236
    # Left col: Ngoài đời
    draw.rounded_rectangle((72, col_y, 524, col_y + col_h), radius=18, fill=(20, 48, 44, 210), outline=(52, 211, 153, 180), width=2)
    draw.text((96, col_y + 18), "NGOÀI ĐỜI TƯ VẤN KHÁCH", font=font(F_BLACK, 23), fill=(52, 211, 153, 255))
    left_pts = [
        "• Có khách thật ngồi đối diện",
        "• Nói theo từng câu hỏi cụ thể",
        "• Mỗi nhịp thở chỉ 5–7 chữ",
    ]
    ly = col_y + 64
    for p in left_pts:
        draw.text((96, ly), p, font=font(F_MED, 25), fill=(241, 245, 249, 255))
        ly += 52

    # Right col: Trước camera
    draw.rounded_rectangle((556, col_y, W - 72, col_y + col_h), radius=18, fill=(58, 24, 32, 210), outline=(248, 113, 113, 180), width=2)
    draw.text((580, col_y + 18), "TRƯỚC CAMERA BỊ ĐƠ", font=font(F_BLACK, 23), fill=(248, 113, 113, 255))
    right_pts = [
        "• Nhìn vào ống kính vô tri",
        "• Cố học thuộc lòng cả đoạn",
        "• Vấp 1 chữ là xóa quay lại",
    ]
    ry = col_y + 64
    for p in right_pts:
        draw.text((580, ry), p, font=font(F_MED, 25), fill=(241, 245, 249, 255))
        ry += 52

    # Solution strip below columns
    sol_y = col_y + col_h + 18
    draw.rounded_rectangle((72, sol_y, W - 72, sol_y + 66), radius=14, fill=(30, 41, 59, 240), outline=(251, 191, 36, 160), width=1)
    draw_mixed_line(draw, 94, sol_y + 18, [
        ("Cách gỡ tại K4: ", (251, 191, 36, 255)),
        ("Mỗi câu một dòng · Đếm nhịp 1-2 · Cắt đổi 2 góc máy", (255, 255, 255, 255)),
    ], font(F_BOLD, 26))

    draw_footer_bar(draw, W, 1318)
    out = os.path.join(OUT_DIR, "k4_v2_b2_pa2_doichieu.jpg")
    canvas.convert("RGB").save(out, quality=95)
    print("Saved:", out)

# ==============================================================================
# BANNER 3 - PA1: MẶT CẮT VIDEO THÂN RỖNG (k2_slate.jpg)
# ==============================================================================
def build_b3_pa1():
    W, H = 1080, 1350
    canvas, draw = prepare_portrait_canvas("k2_slate.jpg", panel_rgb=(15, 21, 31), mode="studio_full")

    card_top = 720
    draw.rounded_rectangle((36, card_top, W - 36, 1318), radius=28, fill=(21, 29, 42, 248), outline=(251, 191, 36, 140), width=2)
    draw.rounded_rectangle((76, card_top, 360, card_top + 6), radius=3, fill=(251, 191, 36, 255))

    draw_mixed_line(draw, 72, card_top + 26, [
        ("VIDEO ĐẸP, ", (255, 255, 255, 255)),
        ("KHÁCH VẪN HỎI GIÁ", (251, 191, 36, 255)),
    ], font(F_BLACK, 50))

    draw.text((72, card_top + 90), "Điểm chung khi thuê đội quay 15 triệu · Làm AI hàng loạt · Quay sa bàn:", font=font(F_MED, 26), fill=(148, 163, 184, 255))

    # 3 Horizontal Anatomy Blocks (y = card_top + 142 .. card_top + 366)
    by = card_top + 142
    bh = 224
    # Block 1: Mở (x=72..348)
    draw.rounded_rectangle((72, by, 344, by + bh), radius=18, fill=(30, 41, 59, 220), outline=(100, 116, 139, 200), width=2)
    draw.text((96, by + 20), "1. MỞ ĐẦU (CÓ)", font=font(F_BLACK, 22), fill=(148, 163, 184, 255))
    draw.text((96, by + 66), "Câu chào, nhạc,", font=font(F_MED, 25), fill=(226, 232, 240, 255))
    draw.text((96, by + 102), "hình ảnh mở màn", font=font(F_MED, 25), fill=(226, 232, 240, 255))
    draw.text((96, by + 138), "bắt mắt.", font=font(F_MED, 25), fill=(226, 232, 240, 255))

    # Block 2: Thân Rỗng (x=364..716) - Dashed highlight box!
    draw.rounded_rectangle((364, by, 716, by + bh), radius=18, fill=(58, 24, 30, 210))
    draw_dashed_rect(draw, (364, by, 716, by + bh), radius=18, color=(251, 191, 36, 255), width=3)
    draw.text((388, by + 20), "2. PHẦN THÂN (RỖNG)", font=font(F_BLACK, 23), fill=(251, 191, 36, 255))
    draw.text((388, by + 66), "Lời khen chung chung.", font=font(F_BOLD, 25), fill=(255, 255, 255, 255))
    draw.text((388, by + 102), "Che logo đi, gắn tên", font=font(F_MED, 24), fill=(254, 202, 202, 255))
    draw.text((388, by + 136), "cơ sở khác vào vẫn đúng.", font=font(F_MED, 24), fill=(254, 202, 202, 255))

    # Block 3: Kết (x=736..1008)
    draw.rounded_rectangle((736, by, W - 72, by + bh), radius=18, fill=(30, 41, 59, 220), outline=(100, 116, 139, 200), width=2)
    draw.text((760, by + 20), "3. ĐOẠN KẾT (CÓ)", font=font(F_BLACK, 22), fill=(148, 163, 184, 255))
    draw.text((760, by + 66), "Số điện thoại,", font=font(F_MED, 25), fill=(226, 232, 240, 255))
    draw.text((760, by + 102), "địa chỉ cửa tiệm,", font=font(F_MED, 25), fill=(226, 232, 240, 255))
    draw.text((760, by + 138), "lời mời mua.", font=font(F_MED, 25), fill=(226, 232, 240, 255))

    # Conclusion strip
    sol_y = by + bh + 20
    draw.rounded_rectangle((72, sol_y, W - 72, sol_y + 66), radius=14, fill=(30, 41, 59, 240), outline=(251, 191, 36, 160), width=1)
    draw_mixed_line(draw, 94, sol_y + 18, [
        ("Thân rỗng → khách chỉ so giá. ", (251, 191, 36, 255)),
        ("K4 viết tay kịch bản 4 bước trước khi đưa vào AI.", (255, 255, 255, 255)),
    ], font(F_BOLD, 24))

    draw_footer_bar(draw, W, 1318)
    out = os.path.join(OUT_DIR, "k4_v2_b3_pa1_thanrong.jpg")
    canvas.convert("RGB").save(out, quality=95)
    print("Saved:", out)

# ==============================================================================
# BANNER 3 - PA2: TẢNG BĂNG 90-9-1 & DARK SOCIAL (k2_slate.jpg)
# ==============================================================================
def build_b3_pa2():
    W, H = 1080, 1350
    canvas, draw = prepare_portrait_canvas("k2_slate.jpg", panel_rgb=(12, 22, 34), mode="studio_full")

    card_top = 720
    draw.rounded_rectangle((36, card_top, W - 36, 1318), radius=28, fill=(16, 28, 44, 248), outline=(56, 189, 248, 150), width=2)
    draw.rounded_rectangle((76, card_top, 360, card_top + 6), radius=3, fill=(56, 189, 248, 255))

    draw_mixed_line(draw, 72, card_top + 26, [
        ("100 NGƯỜI XEM. ", (255, 255, 255, 255)),
        ("1 NGƯỜI BÌNH LUẬN.", (251, 191, 36, 255)),
    ], font(F_BLACK, 43))

    draw.text((72, card_top + 86), "Đăng video thấy ít bình luận, đừng vội nản. Khách thật nằm ở đây:", font=font(F_MED, 26), fill=(148, 163, 184, 255))

    # Top of Iceberg (Above water: 1% + 9%)
    y1 = card_top + 136
    draw.rounded_rectangle((72, y1, W - 72, y1 + 88), radius=16, fill=(30, 41, 59, 210), outline=(100, 116, 139, 180), width=1)
    draw.rounded_rectangle((90, y1 + 18, 290, y1 + 70), radius=10, fill=(51, 65, 85, 255))
    draw.text((108, y1 + 30), "BẠN THẤY ĐƯỢC", font=font(F_BLACK, 20), fill=(226, 232, 240, 255))
    draw.text((312, y1 + 16), "1 người bình luận · 9 người thả tim", font=font(F_BOLD, 26), fill=(255, 255, 255, 255))
    draw.text((312, y1 + 48), "Khách mua dịch vụ vài triệu không hỏi giá công khai.", font=font(F_MED, 23), fill=(148, 163, 184, 255))

    # Waterline Divider (Dark Social 84%)
    yw = y1 + 104
    draw.line([(72, yw + 16), (W - 72, yw + 16)], fill=(56, 189, 248, 220), width=3)
    draw.rounded_rectangle((220, yw, W - 220, yw + 34), radius=17, fill=(14, 116, 144, 255), outline=(56, 189, 248, 255), width=1)
    draw.text((254, yw + 6), "BẠN CHỈ THẤY PHẦN NỔI. PHẦN CHÌM LÀ KHÁCH THẬT", font=font(F_BLACK, 19), fill=(255, 255, 255, 255))

    # Bottom of Iceberg (Below water: 90% Lurkers)
    y2 = yw + 48
    draw.rounded_rectangle((72, y2, W - 72, y2 + 122), radius=18, fill=(15, 42, 62, 240), outline=(251, 191, 36, 220), width=2)
    draw.rounded_rectangle((90, y2 + 22, 290, y2 + 98), radius=12, fill=(251, 191, 36, 255))
    draw.text((110, y2 + 36), "BẠN KHÔNG THẤY", font=font(F_BLACK, 18), fill=(15, 23, 42, 255))
    draw.text((117, y2 + 64), "90 XEM IM LẶNG", font=font(F_BLACK, 18), fill=(15, 23, 42, 255))
    draw.text((312, y2 + 18), "Khách có tiền nằm ở nhóm 90 người này:", font=font(F_BOLD, 26), fill=(251, 191, 36, 255))
    draw.text((312, y2 + 54), "Xem liền 10–15 video xem bạn làm nghề thật không,", font=font(F_MED, 24), fill=(241, 245, 249, 255))
    draw.text((312, y2 + 84), "gửi link Zalo cho vợ/chồng bàn rồi mới nhắn đặt lịch.", font=font(F_MED, 24), fill=(241, 245, 249, 255))

    draw.text((72, y2 + 146), "→ Khách thật hiếm khi bình luận. Kênh cần đủ video để họ xem thầm.", font=font(F_BOLD, 25), fill=(56, 189, 248, 255))

    draw_footer_bar(draw, W, 1318)
    out = os.path.join(OUT_DIR, "k4_v2_b3_pa2_tangbang.jpg")
    canvas.convert("RGB").save(out, quality=95)
    print("Saved:", out)

if __name__ == "__main__":
    build_b1_pa1()
    build_b1_pa2()
    build_b2_pa1()
    build_b2_pa2()
    build_b3_pa1()
    build_b3_pa2()
