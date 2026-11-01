import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

OUT_DIR = "/Users/vietmac/Documents/CODE/k/k4_ads_banners_v4"
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


def prepare_portrait_canvas(
    img_name,
    centering=(0.5, 0.42),
    grad_start=580,
    top_h=840,
    panel_rgb=(15, 20, 30),
    mode="fit",
):
    W, H = 1080, 1350
    src = Image.open(os.path.join(SRC_DIR, img_name)).convert("RGBA")
    canvas = Image.new("RGBA", (W, H), (*panel_rgb, 255))

    if mode == "studio_full":
        target_w = 800
        target_h = int(src.height * (target_w / float(src.width)))
        scaled = src.resize((target_w, target_h), Image.Resampling.LANCZOS)
        bg_top = Image.new("RGBA", (W, target_h))
        pad_left = (W - target_w) // 2
        pad_right = W - target_w - pad_left
        left_strip = scaled.crop((0, 0, 12, target_h)).resize(
            (pad_left, target_h), Image.Resampling.BICUBIC
        )
        right_strip = scaled.crop((target_w - 12, 0, target_w, target_h)).resize(
            (pad_right, target_h), Image.Resampling.BICUBIC
        )
        bg_top.paste(left_strip, (0, 0))
        bg_top.paste(scaled, (pad_left, 0))
        bg_top.paste(right_strip, (pad_left + target_w, 0))
        canvas.paste(bg_top, (0, -18))
        top_h = 820
        grad_start = 630
    else:
        bg_top = ImageOps.fit(
            src, (W, top_h), method=Image.Resampling.LANCZOS, centering=centering
        )
        canvas.paste(bg_top, (0, 0))

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for y in range(grad_start, top_h):
        t = (y - grad_start) / float(top_h - grad_start)
        alpha = int(min(255, (t**1.15) * 255))
        od.line([(0, y), (W, y)], fill=(*panel_rgb, alpha))
    od.rectangle((0, top_h, W, H), fill=(*panel_rgb, 255))
    canvas = Image.alpha_composite(canvas, overlay)

    draw = ImageDraw.Draw(canvas)
    # Top-left badge: HỌC TRỰC TIẾP 2 NGÀY · HÀ NỘI · CÒN 17 CHỖ
    badge_txt = "HỌC TRỰC TIẾP 2 NGÀY · HÀ NỘI · CÒN 17 CHỖ"
    f_badge = font(F_BOLD, 22)
    tw = draw.textbbox((0, 0), badge_txt, font=f_badge)[2]
    draw.rounded_rectangle(
        (40, 34, 96 + tw + 26, 90),
        radius=28,
        fill=(13, 18, 28, 225),
        outline=(251, 191, 36, 215),
        width=2,
    )
    draw.ellipse((64, 54, 80, 70), fill=(251, 191, 36, 255))
    draw.text((94, 48), badge_txt, font=f_badge, fill=(248, 250, 252, 255))
    return canvas, draw


def draw_footer_bar(draw, W, card_bottom=1318):
    y_bar = card_bottom - 84
    draw.line([(72, y_bar - 12), (W - 72, y_bar - 12)], fill=(51, 65, 85, 210), width=2)
    # Yellow CTA button
    btn_w = 316
    draw.rounded_rectangle(
        (72, y_bar, 72 + btn_w, y_bar + 64), radius=12, fill=(251, 191, 36, 255)
    )
    btn_txt = "07–08/11 · 4 TRIỆU"
    f_btn = font(F_BLACK, 25)
    bt_w = draw.textbbox((0, 0), btn_txt, font=f_btn)[2]
    draw.text(
        (72 + (btn_w - bt_w) // 2, y_bar + 17),
        btn_txt,
        font=f_btn,
        fill=(15, 23, 42, 255),
    )
    # Two clear lines next to button
    rx = 72 + btn_w + 22
    draw.text(
        (rx, y_bar + 4),
        "Đi 2 người: người thứ 2 chỉ 3,5 triệu · Tặng khóa Online",
        font=font(F_BOLD, 22),
        fill=(251, 191, 36, 255),
    )
    draw.text(
        (rx, y_bar + 35),
        "Green Hub Long Biên · Hết ngày 1 không hợp: hoàn 100%",
        font=font(F_MED, 21),
        fill=(226, 232, 240, 255),
    )


# ==============================================================================
# MẪU #1: VIDEO CÓ NGƯỜI XEM MÀ KHÔNG RA KHÁCH (k2_charcoal.jpg)
# ==============================================================================
def build_b1_pa1():
    W, H = 1080, 1350
    canvas, draw = prepare_portrait_canvas(
        "k2_charcoal.jpg", panel_rgb=(14, 18, 26), mode="studio_full"
    )

    card_top = 722
    draw.rounded_rectangle(
        (36, card_top, W - 36, 1318),
        radius=28,
        fill=(20, 26, 38, 246),
        outline=(251, 191, 36, 130),
        width=2,
    )
    draw.rounded_rectangle(
        (76, card_top, 340, card_top + 6), radius=3, fill=(251, 191, 36, 255)
    )

    # Title
    draw_mixed_line(
        draw,
        72,
        card_top + 24,
        [
            ("VIDEO CÓ NGƯỜI XEM ", (255, 255, 255, 255)),
            ("MÀ KHÔNG RA KHÁCH?", (251, 191, 36, 255)),
        ],
        font(F_BLACK, 40),
    )

    # Subtitle
    draw.text(
        (72, card_top + 80),
        "Thường thiếu 2 câu: câu đầu nói rõ cho ai, câu cuối bảo khách làm gì.",
        font=font(F_MED, 26),
        fill=(148, 163, 184, 255),
    )

    # 3 Rows: TRƯỚC / TẠI LỚP / MANG VỀ
    rows = [
        (
            "TRƯỚC",
            (239, 68, 68, 255),
            (69, 26, 30, 230),
            "Quay đẹp, nói hay:",
            "Người xem chỉ khen rồi lướt qua.",
        ),
        (
            "TẠI LỚP",
            (52, 211, 153, 255),
            (16, 58, 48, 230),
            "Sửa trực tiếp 1-1:",
            "Viết câu mở và câu kết cho tiệm mình.",
        ),
        (
            "MANG VỀ",
            (251, 191, 36, 255),
            (66, 48, 18, 230),
            "Không sợ quên bài:",
            "Khóa Online xem lại + 30 ngày sửa Zalo.",
        ),
    ]
    ry = card_top + 130
    for badge_txt, b_col, bg_col, bold_lbl, desc_txt in rows:
        draw.rounded_rectangle(
            (72, ry, W - 72, ry + 76),
            radius=16,
            fill=(30, 41, 59, 210),
            outline=(51, 65, 85, 200),
            width=1,
        )
        draw.rounded_rectangle(
            (88, ry + 15, 236, ry + 61), radius=10, fill=bg_col, outline=b_col, width=2
        )
        f_p = font(F_BLACK, 21)
        pw = draw.textbbox((0, 0), badge_txt, font=f_p)[2]
        draw.text((88 + (148 - pw) // 2, ry + 26), badge_txt, font=f_p, fill=b_col)
        draw_mixed_line(
            draw,
            256,
            ry + 23,
            [
                (bold_lbl + " ", (255, 255, 255, 255)),
                (desc_txt, (226, 232, 240, 255)),
            ],
            font(F_MED, 26),
        )
        ry += 88

    # Real Student Testimonial
    draw.text(
        (72, ry + 4),
        '→ "Thầy chân thành y như trên video. Sau 2 ngày có đủ kỹ thuật để làm ngay." — Chị Quỳnh Liên',
        font=font(F_BOLD, 21),
        fill=(251, 191, 36, 255),
    )

    draw_footer_bar(draw, W, 1318)
    out = os.path.join(OUT_DIR, "k4_v4_01_khong_ra_khach.jpg")
    canvas.convert("RGB").save(out, quality=95)
    print("Saved:", out)


# ==============================================================================
# MẪU #3: CHƯA TỪNG QUAY DỰNG? SỢ HỌC XONG VỀ QUÊN? (k16_deepwork1.jpg)
# ==============================================================================
def build_b2_pa1():
    W, H = 1080, 1350
    canvas, draw = prepare_portrait_canvas(
        "k16_deepwork1.jpg",
        centering=(0.5, 0.08),
        grad_start=600,
        top_h=820,
        panel_rgb=(15, 20, 28),
        mode="fit",
    )

    card_top = 714
    draw.rounded_rectangle(
        (36, card_top, W - 36, 1318),
        radius=28,
        fill=(21, 28, 40, 248),
        outline=(52, 211, 153, 140),
        width=2,
    )
    draw.rounded_rectangle(
        (76, card_top, 360, card_top + 6), radius=3, fill=(52, 211, 153, 255)
    )

    draw_mixed_line(
        draw,
        72,
        card_top + 22,
        [
            ("CHƯA TỪNG ", (255, 255, 255, 255)),
            ("QUAY DỰNG?", (52, 211, 153, 255)),
        ],
        font(F_BLACK, 43),
    )
    draw_mixed_line(
        draw,
        72,
        card_top + 74,
        [
            ("SỢ HỌC XONG ", (255, 255, 255, 255)),
            ("VỀ NHÀ QUÊN?", (251, 191, 36, 255)),
        ],
        font(F_BLACK, 43),
    )

    rows = [
        (
            "NGÀY 1",
            (52, 211, 153, 255),
            "Quay tay mình đang làm nghề:",
            "Chưa cần lộ mặt, đọc lời bình ghép sau → Xong 1 video.",
        ),
        (
            "NGÀY 2",
            (251, 191, 36, 255),
            "Ngồi nói từng câu ngắn:",
            "Quay 2 góc máy đổi qua lại, che hết chỗ ngập ngừng.",
        ),
        (
            "VỀ NHÀ",
            (56, 189, 248, 255),
            "Khóa Online quay sẵn từng bước:",
            "Quên nút bấm nào mở xem lại + 30 ngày sửa bài Zalo.",
        ),
    ]
    ry = card_top + 138
    for badge_txt, col, b_lbl, desc_txt in rows:
        draw.rounded_rectangle(
            (72, ry, W - 72, ry + 80),
            radius=16,
            fill=(30, 41, 59, 220),
            outline=(51, 65, 85, 200),
            width=1,
        )
        draw.rounded_rectangle(
            (88, ry + 17, 222, ry + 63),
            radius=10,
            fill=(15, 23, 42, 240),
            outline=col,
            width=2,
        )
        f_p = font(F_BLACK, 21)
        pw = draw.textbbox((0, 0), badge_txt, font=f_p)[2]
        draw.text((88 + (134 - pw) // 2, ry + 27), badge_txt, font=f_p, fill=col)
        draw.text((242, ry + 13), b_lbl, font=font(F_BOLD, 24), fill=col)
        draw.text(
            (242, ry + 43), desc_txt, font=font(F_MED, 24), fill=(241, 245, 249, 255)
        )
        ry += 92

    draw.text(
        (72, ry + 4),
        '→ "Nhiều kiến thức cần thiết, thầy nhiệt huyết kèm thực hành." — Chị Tâng Xinh, học viên khóa 3',
        font=font(F_BOLD, 21),
        fill=(52, 211, 153, 255),
    )

    draw_footer_bar(draw, W, 1318)
    out = os.path.join(OUT_DIR, "k4_v4_03_chua_biet_quay.jpg")
    canvas.convert("RGB").save(out, quality=95)
    print("Saved:", out)


# ==============================================================================
# MẪU #6: NGƯỜI MUA THƯỜNG KHÔNG BÌNH LUẬN (k2_slate.jpg)
# ==============================================================================
def build_b3_pa2():
    W, H = 1080, 1350
    canvas, draw = prepare_portrait_canvas(
        "k2_slate.jpg", panel_rgb=(12, 22, 34), mode="studio_full"
    )

    card_top = 716
    draw.rounded_rectangle(
        (36, card_top, W - 36, 1318),
        radius=28,
        fill=(16, 28, 44, 248),
        outline=(56, 189, 248, 150),
        width=2,
    )
    draw.rounded_rectangle(
        (76, card_top, 360, card_top + 6), radius=3, fill=(56, 189, 248, 255)
    )

    draw_mixed_line(
        draw,
        72,
        card_top + 24,
        [
            ("NGƯỜI MUA THƯỜNG ", (255, 255, 255, 255)),
            ("KHÔNG BÌNH LUẬN.", (251, 191, 36, 255)),
        ],
        font(F_BLACK, 42),
    )

    draw.text(
        (72, card_top + 80),
        "Họ xem lặng lẽ cả kênh cho đủ tin rồi mới nhắn đặt lịch:",
        font=font(F_MED, 26),
        fill=(148, 163, 184, 255),
    )

    # Top Box: BẠN THẤY
    y1 = card_top + 128
    draw.rounded_rectangle(
        (72, y1, W - 72, y1 + 86),
        radius=16,
        fill=(30, 41, 59, 210),
        outline=(100, 116, 139, 180),
        width=1,
    )
    draw.rounded_rectangle(
        (90, y1 + 17, 290, y1 + 69), radius=10, fill=(51, 65, 85, 255)
    )
    f_top = font(F_BLACK, 20)
    tw_top = draw.textbbox((0, 0), "BẠN THẤY ĐƯỢC", font=f_top)[2]
    draw.text(
        (90 + (200 - tw_top) // 2, y1 + 31),
        "BẠN THẤY ĐƯỢC",
        font=f_top,
        fill=(226, 232, 240, 255),
    )
    draw.text(
        (312, y1 + 14),
        "Video ít bình luận → tưởng không ai quan tâm",
        font=font(F_BOLD, 25),
        fill=(255, 255, 255, 255),
    )
    draw.text(
        (312, y1 + 46),
        "Khách mua dịch vụ vài triệu hiếm khi hỏi giá công khai.",
        font=font(F_MED, 23),
        fill=(148, 163, 184, 255),
    )

    # Waterline Divider
    yw = y1 + 98
    draw.line([(72, yw + 17), (W - 72, yw + 17)], fill=(56, 189, 248, 220), width=3)
    mid_txt = "THẬT RA: HỌ ĐANG XEM TIẾP VIDEO THỨ 2, THỨ 3 TRÊN KÊNH"
    f_mid = font(F_BLACK, 19)
    mw = draw.textbbox((0, 0), mid_txt, font=f_mid)[2]
    pad_m = 28
    bx1 = (W - mw) // 2 - pad_m
    bx2 = (W + mw) // 2 + pad_m
    draw.rounded_rectangle(
        (bx1, yw, bx2, yw + 34),
        radius=17,
        fill=(14, 116, 144, 255),
        outline=(56, 189, 248, 255),
        width=1,
    )
    draw.text(((W - mw) // 2, yw + 6), mid_txt, font=f_mid, fill=(255, 255, 255, 255))

    # Bottom Box: CHUYỆN CÓ THẬT (Anh Viên Thế Đức)
    y2 = yw + 46
    draw.rounded_rectangle(
        (72, y2, W - 72, y2 + 118),
        radius=18,
        fill=(15, 42, 62, 240),
        outline=(251, 191, 36, 220),
        width=2,
    )
    draw.rounded_rectangle(
        (90, y2 + 20, 290, y2 + 98), radius=12, fill=(251, 191, 36, 255)
    )
    f_b = font(F_BLACK, 20)
    w1 = draw.textbbox((0, 0), "CHUYỆN THẬT", font=f_b)[2]
    w2 = draw.textbbox((0, 0), "HỌC VIÊN CŨ", font=f_b)[2]
    draw.text(
        (90 + (200 - w1) // 2, y2 + 33), "CHUYỆN THẬT", font=f_b, fill=(15, 23, 42, 255)
    )
    draw.text(
        (90 + (200 - w2) // 2, y2 + 61), "HỌC VIÊN CŨ", font=f_b, fill=(15, 23, 42, 255)
    )
    draw.text(
        (312, y2 + 15),
        "Anh Viên Thế Đức (Học viên khóa 2, ngành Bán lẻ):",
        font=font(F_BOLD, 25),
        fill=(251, 191, 36, 255),
    )
    draw.text(
        (312, y2 + 49),
        '"Biết đến thầy qua 1 video ngẫu nhiên, sau đó mình',
        font=font(F_MED, 24),
        fill=(241, 245, 249, 255),
    )
    draw.text(
        (312, y2 + 79),
        'vào xem lại toàn bộ kênh rồi mới đăng ký học."',
        font=font(F_MED, 24),
        fill=(241, 245, 249, 255),
    )

    draw.text(
        (72, y2 + 128),
        "→ Lớp 2 ngày: làm bộ video đủ sức thuyết phục những khách xem thầm.",
        font=font(F_BOLD, 23),
        fill=(56, 189, 248, 255),
    )

    draw_footer_bar(draw, W, 1318)
    out = os.path.join(OUT_DIR, "k4_v4_06_xem_tham_ca_kenh.jpg")
    canvas.convert("RGB").save(out, quality=95)
    print("Saved:", out)


if __name__ == "__main__":
    build_b1_pa1()
    build_b2_pa1()
    build_b3_pa2()
