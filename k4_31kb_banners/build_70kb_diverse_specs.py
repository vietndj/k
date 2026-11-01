#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BUILD 70 DIVERSE AD BANNERS SPECS & 70 UNIQUE OUTFIT/STYLE BACKGROUNDS
======================================================================
1. Chọn 70 trang phục khác nhau 100% từ 32 Card phong cách chuẩn trong `banner.html` (`outfit_registry.json`).
2. Dựng 70 ảnh nền 1080x1350 đa phong cách (Zero-Ghost, Zero-Top-Seam, Wide-Feather 260px) giữ trọn bối cảnh,
   ánh sáng và bảng màu đặc trưng của từng Style trong `banner.html`.
3. Áp dụng trọn vẹn Bộ Chọn Chữ `bo-chon-chu-banner.html`:
   - Lớp 1: Xoay vòng toàn bộ 20 Font Tiêu Đề Có Chân (`H01` -> `H20`) kèm Focal Italic/Stencil (`LAW_09` + `LAW_10`).
   - Lớp 2: Xoay vòng toàn bộ 21 Khuôn Khung Chữ Bé (`K01` -> `K21`) thuộc 5 Họ Logic (`KA`..`KE`).
4. Xuất `kb_31_master_specs.json` (chứa toàn bộ 70 kịch bản `KB_01` -> `KB_70`).
"""

import concurrent.futures
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple
import cv2
import numpy as np
from PIL import Image

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
PILOT_DIR = BASE_DIR / "v2_pilots"
BG_POOL_70_DIR = PILOT_DIR / "bg_pool_70"
BG_POOL_70_DIR.mkdir(parents=True, exist_ok=True)

OUTFIT_REG_PATH = BASE_DIR / "outfit_registry.json"
OLD_SPECS_PATH = BASE_DIR / "kb_31_master_specs.json"

# 1. 20 Font Tiêu Đề Có Chân (H01 -> H20) từ bo-chon-chu-banner.html + Focal Font đồng bộ
HEADLINE_20_FONTS: Dict[str, Dict[str, Any]] = {
    "H01": {"file": "FDTiemposHeadline-Bold.woff2", "focal_file": "FDTiemposHeadline-BoldItalic.woff2", "focal_style": "italic", "name": "H01 · Tiempos Headline Bold", "base_fs": 80, "base_lh": 1.13},
    "H02": {"file": "FDOrlando-Bold.woff2", "focal_file": "FDOrlando-BoldItalic.woff2", "focal_style": "italic", "name": "H02 · Orlando Bold (Flare)", "base_fs": 84, "base_lh": 1.13},
    "H03": {"file": "FDLockSerif-Bold.woff2", "focal_file": "FDLockSerifStencil-Bold.woff2", "focal_style": "normal", "name": "H03 · Lock Serif + Stencil", "base_fs": 81, "base_lh": 1.13},
    "H04": {"file": "GRSuperDisplay-Bold.woff2", "focal_file": "GRSuperDisplay-Bold.woff2", "focal_style": "normal", "name": "H04 · Super Display Bold", "base_fs": 82, "base_lh": 1.12},
    "H05": {"file": "FDFeijoa-Bold.woff2", "focal_file": "FDFeijoa-Bold.woff2", "focal_style": "normal", "name": "H05 · Klim Feijoa Bold", "base_fs": 80, "base_lh": 1.12},
    "H06": {"file": "GRCanonLStandardBold.woff2", "focal_file": "GRCanonLStandardBoldItalic.woff2", "focal_style": "italic", "name": "H06 · Canon Standard Bold", "base_fs": 80, "base_lh": 1.12},
    "H07": {"file": "FDActa-ExtraBold.woff2", "focal_file": "FDActa-ExtraBoldItalic.woff2", "focal_style": "italic", "name": "H07 · Acta ExtraBold", "base_fs": 82, "base_lh": 1.10},
    "H08": {"file": "FDNoeDisplay-Bold.ttf", "focal_file": "FDNoeDisplay-BoldItalic.ttf", "focal_style": "italic", "name": "H08 · Noe Display Bold", "base_fs": 83, "base_lh": 1.10},
    "H09": {"file": "FDDomaineDisplay-Bold.woff2", "focal_file": "FDDomaineDisplay-BoldItalic.woff2", "focal_style": "italic", "name": "H09 · Domaine Display Bold", "base_fs": 81, "base_lh": 1.10},
    "H10": {"file": "FDMartinaPlantijn-Bold.woff2", "focal_file": "FDMartinaPlantijn-BoldItalic.woff2", "focal_style": "italic", "name": "H10 · Martina Plantijn Bold", "base_fs": 84, "base_lh": 1.09},
    "H11": {"file": "FDEpiceneDisplay-Bold.woff2", "focal_file": "FDEpiceneDisplay-BoldItalic.woff2", "focal_style": "italic", "name": "H11 · Epicene Display Bold", "base_fs": 86, "base_lh": 1.07},
    "H12": {"file": "GRSectraDisplay-Bold.woff2", "focal_file": "GRSectraDisplay-BoldItalic.woff2", "focal_style": "italic", "name": "H12 · GT Sectra Display Bold", "base_fs": 84, "base_lh": 1.06},
    "H13": {"file": "GRAlpinaFine-Bold.woff2", "focal_file": "GRAlpinaFine-BoldItalic.woff2", "focal_style": "italic", "name": "H13 · GT Alpina Fine Bold", "base_fs": 84, "base_lh": 1.06},
    "H14": {"file": "FDUntitledSerif-Bold.woff2", "focal_file": "FDUntitledSerif-BoldItalic.woff2", "focal_style": "italic", "name": "H14 · Untitled Serif Bold", "base_fs": 82, "base_lh": 1.05},
    "H15": {"file": "FDHeldaneDisplay-Bold.woff2", "focal_file": "FDHeldaneDisplay-BoldItalic.woff2", "focal_style": "italic", "name": "H15 · Heldane Display Bold", "base_fs": 90, "base_lh": 1.03},
    "H16": {"file": "FDSignifier-Bold.woff2", "focal_file": "FDSignifier-BoldItalic.woff2", "focal_style": "italic", "name": "H16 · Klim Signifier Bold", "base_fs": 85, "base_lh": 1.06},
    "H17": {"file": "FDFinancierDisplay-Bold.woff2", "focal_file": "FDFinancierDisplay-BoldItalic.woff2", "focal_style": "italic", "name": "H17 · Financier Display Bold", "base_fs": 90, "base_lh": 1.02},
    "H18": {"file": "FDAddingtonCF-Bold.otf", "focal_file": "FDAddingtonCF-Bold.otf", "focal_style": "normal", "name": "H18 · Addington CF Bold", "base_fs": 84, "base_lh": 1.03},
    "H19": {"file": "FDNewzald-Bold.woff2", "focal_file": "FDNewzald-BoldItalic.woff2", "focal_style": "italic", "name": "H19 · Klim Newzald Bold", "base_fs": 88, "base_lh": 1.02},
    "H20": {"file": "FDFinancierText-Bold.woff2", "focal_file": "FDFinancierText-BoldItalic.woff2", "focal_style": "italic", "name": "H20 · Financier Text Bold", "base_fs": 86, "base_lh": 1.02},
}

# 2. 21 Khuôn Khung Chữ Bé (K01 -> K21) từ bo-chon-chu-banner.html
STYLE_21_NAMES: Dict[str, str] = {
    "K01": "K01 (Họ KA) · Hai Vế Đối Lập (× / ✓)",
    "K02": "K02 (Họ KE) · Khối Trích Dẫn Tối Sâu (Viền Đỉnh)",
    "K03": "K03 (Họ KB) · Con Số Bằng Chứng Lớn (→)",
    "K04": "K04 (Họ KE) · Nhãn Tab Gắn Đỉnh Hộp",
    "K05": "K05 (Họ KC) · Chuỗi Mũi Tên Nhân Quả (A → B)",
    "K06": "K06 (Họ KA) · Định Nghĩa Âm Bản (KHÔNG PHẢI / MÀ LÀ)",
    "K07": "K07 (Họ KA) · Chia 2 Ngăn Trái–Phải (50/50)",
    "K08": "K08 (Họ KE) · Gạch Chân Quang Học & Đáy Liền",
    "K09": "K09 (Họ KD) · Bong Bóng Tin Nhắn Khách Hàng",
    "K10": "K10 (Họ KB) · Thanh Đo Độ Nhớ (10% vs 95%)",
    "K11": "K11 (Họ KD) · Hỏi Xoáy – Đáp Gọn ([HỎI] / [ĐÁP])",
    "K12": "K12 (Họ KE) · Khung Ngắm 4 Góc & Bút Dạ Quang",
    "K13": "K13 (Họ KB) · Trục Thời Gian 2 Nấc (○ → ●)",
    "K14": "K14 (Họ KA) · Thay Thói Quen Cũ ([CŨ] → [MỚI])",
    "K15": "K15 (Họ KB) · Lịch Tuần 7 Ô (T2–CN)",
    "K16": "K16 (Họ KE) · Chữ Bóng Chìm Nền (Watermark)",
    "K17": "K17 (Họ KA) · Đường Chấm Dẫn Đối Chiếu (.......)",
    "K18": "K18 (Họ KC) · Phương Trình Đóng Khung ([A] + [B] = C)",
    "K19": "K19 (Họ KC) · Bảng Kiểm 2 Ô Tích Vàng ([✓])",
    "K20": "K20 (Họ KA) · Thẻ Chẩn Đoán ([BỆNH] → [THUỐC])",
    "K21": "K21 (Họ KB) · Bộ Lọc 3 Giây Đầu (03s LƯỚT XEM)",
}

# 3. 32 Phong cách hình ảnh, môi trường, ánh sáng & bảng màu từ banner.html
CARD_STYLE_PROFILES: Dict[str, Tuple[str, Tuple[int, int, int], str]] = {
    "C02": ("Kiểu 01 · Tech Keynote Neon (Cyan/Purple)", (16, 26, 58), "#38BDF8"),
    "C03": ("Kiểu 02 · Sản Phẩm Cao Cấp Huawei XT2 (Royal Navy)", (14, 34, 68), "#FACC15"),
    "C04": ("Kiểu 03 · Chuyên Gia Trắng Đen (Resort & Studio B&W)", (24, 26, 30), "#FACC15"),
    "C05": ("Kiểu 04 · Thư Giãn Ngoài Trời (Nắng Ấm Golden Hour)", (48, 30, 14), "#FDE047"),
    "C06": ("Kiểu 05 · Diễn Giả Sân Khấu (Pink/Purple Vibe)", (46, 16, 58), "#F472B6"),
    "C07": ("Kiểu 06 · Thanh Lịch Tối Giản (Beige & Royal Blue)", (18, 42, 76), "#FACC15"),
    "C08": ("Kiểu 07 · Kiến Trúc Đương Đại (Hard Shadows Terracotta)", (48, 28, 18), "#FB923C"),
    "C09": ("Kiểu 08 · Nội Thất Tân Cổ Điển (Warm Mahogany)", (44, 24, 16), "#FACC15"),
    "C10": ("Kiểu 09 · Văn Phòng Tech Startup (Modern Teal)", (12, 42, 52), "#38BDF8"),
    "C11": ("Kiểu 10 · Sân Khấu Màn Hình LED Khổng Lồ (Cobalt)", (12, 28, 68), "#38BDF8"),
    "C12": ("Kiểu 11 · Cafe Sáng Đọc Báo (Phong Cách Denim)", (42, 28, 20), "#FACC15"),
    "C13": ("Kiểu 12 · Đường Phố Châu Âu (Tường Đá Chạm Khắc)", (38, 32, 26), "#FDE047"),
    "C14": ("Kiểu 13 · Thuyết Trình Siêu Xe (Crimson Stage)", (54, 14, 20), "#FACC15"),
    "C15": ("Kiểu 14 · Tiệc Chiều Hoàng Hôn Venice (Sunset)", (56, 22, 22), "#FB923C"),
    "C16": ("Kiểu 15 · Studio Phông Trơn Doanh Nhân (Slate)", (20, 28, 42), "#FACC15"),
    "C17": ("Kiểu 16 · Bàn Gỗ Làm Việc Tập Trung (Deep Work Forest)", (16, 38, 30), "#34D399"),
    "C18": ("Kiểu 17 · Cảnh Rộng Trầm Tĩnh (Moody Emerald Room)", (18, 34, 28), "#34D399"),
    "C19": ("Kiểu 18 · Đồ Họa Mảng Khối 3D (Teal/Cyan Studio)", (10, 46, 56), "#38BDF8"),
    "C21": ("Kiểu 19 · Apple Minimalist Daylight (Silver Slate)", (24, 32, 44), "#38BDF8"),
    "C22": ("Kiểu 20 · Kiến Trúc Đá Cát Nắng Chiều (Warm Bronze)", (46, 32, 20), "#FACC15"),
    "C23": ("Kiểu 21 · Tòa Nhà Kính Skyline (Steel Blue)", (16, 36, 58), "#38BDF8"),
    "C24": ("Kiểu 22 · Resort Linen & Navy (Warm Indigo)", (22, 30, 52), "#FDE047"),
    "C26": ("Kiểu 23 · Chiaroscuro Studio (Obsidian & Gold)", (20, 18, 16), "#FACC15"),
    "C27": ("Kiểu 24 · Đỉnh Núi Tuyết Daylight (Glacier Blue)", (16, 36, 62), "#38BDF8"),
    "C28": ("Kiểu 25 · Tatler CEO Sofa Da Nâu (Rich Cognac)", (46, 26, 16), "#FACC15"),
    "C29": ("Kiểu 26 · Phòng Họp Đá Đen Phản Chiếu (Deep Jade)", (10, 38, 34), "#34D399"),
    "C30": ("Kiểu 27 · Bục Diễn Giả Đỏ Ruby (Ruby Podium)", (58, 12, 18), "#FACC15"),
    "C34": ("Kiểu 28 · Streetwear Kiến Trúc Bê Tông (Urban Mint)", (22, 34, 36), "#34D399"),
    "C35": ("Kiểu 29 · Cầu Đêm Ánh Đèn Thành Phố (Midnight Indigo)", (16, 24, 52), "#FACC15"),
    "C36": ("Kiểu 30 · Sảnh Sân Bay Quốc Tế (Titanium Sky)", (24, 34, 48), "#38BDF8"),
    "C37": ("Kiểu 31 · Lounge Tối Ánh Vàng Ấm (Espresso Gold)", (40, 28, 18), "#FDE047"),
    "C39": ("Kiểu 32 · Studio Áo Len Cổ Lọ (Warm Graphite)", (28, 26, 24), "#FB923C"),
}


def select_70_unique_outfits(reg: Dict[str, Any]) -> List[Tuple[str, Dict[str, Any]]]:
    """Lọc ra đúng 70 bức chân dung đơn với 70 trang phục khác nhau 100%, xoay vòng qua 32 Card phong cách."""
    by_card: Dict[str, List[Tuple[str, Dict[str, Any]]]] = {}
    for oid, info in sorted(reg.items()):
        card_prefix = oid[:3]
        if card_prefix not in CARD_STYLE_PROFILES:
            continue
        p = Path(info["local_path"])
        if not p.exists() or info.get("has_baked_text"):
            continue
        src = info.get("src", "").lower()
        if "composite" in src or "triptych" in src or "merged" in src:
            continue
        with Image.open(p) as im:
            w, h = im.size
        if h < w:
            continue
        fx, fy, fw, fh = info["face_bbox"]
        if fw <= w * 0.405:
            by_card.setdefault(card_prefix, []).append((oid, info))

    # Round-robin across the 32 style cards so consecutive banners always have completely different styles AND outfits
    selected: List[Tuple[str, Dict[str, Any]]] = []
    round_idx = 0
    card_keys = sorted(by_card.keys())
    while len(selected) < 70:
        added_in_round = 0
        for ck in card_keys:
            items = by_card[ck]
            if round_idx < len(items):
                selected.append(items[round_idx])
                added_in_round += 1
                if len(selected) >= 70:
                    break
        if added_in_round == 0:
            break
        round_idx += 1
    return selected[:70]


def build_seamless_diverse_bg(
    outfit_id: str,
    info: Dict[str, Any],
    side: str,
    tint_rgb: Tuple[int, int, int],
    out_path: Path,
) -> None:
    """
    Dựng ảnh nền 1080x1350 từ ảnh chân dung gốc trong banner.html:
    - Chiều cao luôn >= 1350px (0% vết cắt trên đỉnh đầu, tỷ lệ đầu/thân >= 5.2x).
    - Nửa bên chữ mở rộng mượt từ chính rìa hậu cảnh 14% của ảnh gốc (0% bóng mờ mặt thứ 2)
      kết hợp bảng màu đặc trưng của từng Style trong banner.html.
    """
    if out_path.exists():
        return
    with Image.open(info["local_path"]) as im_raw:
        im = im_raw.convert("RGB")
        w0, h0 = im.size
        fx, fy, fw, fh = info["face_bbox"]

        scale = 1350.0 / float(h0)
        nw = int(round(w0 * scale))
        nh = 1350
        im_s = im.resize((nw, nh), Image.Resampling.LANCZOS)
        arr_s = np.array(im_s, dtype=np.float32)

    fcx = (fx + fw * 0.5) * scale
    target_cx = 790.0 if side == "right" else 290.0
    shift_x = int(round(target_cx - fcx))

    # Lấy dải hậu cảnh thuần túy ở phía đối diện nhân vật
    if side == "right":
        env_strip = arr_s[:, : max(24, int(nw * 0.14)), :]
    else:
        env_strip = arr_s[:, min(nw - 24, int(nw * 0.86)) :, :]
    env_full = cv2.resize(env_strip, (1080, 1350), interpolation=cv2.INTER_CUBIC)
    env_blur = cv2.GaussianBlur(env_full, (95, 95), 0)

    canvas = env_blur.copy()
    src_x1 = max(0, -shift_x)
    src_x2 = min(nw, 1080 - shift_x)
    dst_x1 = max(0, shift_x)
    dst_x2 = dst_x1 + (src_x2 - src_x1)

    if dst_x2 > dst_x1:
        subj_slice = arr_s[:, src_x1:src_x2, :]
        slice_w = dst_x2 - dst_x1
        xx_s = np.arange(slice_w, dtype=np.float32)[None, :, None]
        if side == "right" and dst_x1 > 0:
            feather = np.clip(xx_s / 240.0, 0.0, 1.0)
            feather = feather * feather * (3.0 - 2.0 * feather)
            canvas[:, dst_x1:dst_x2, :] = canvas[:, dst_x1:dst_x2, :] * (1.0 - feather) + subj_slice * feather
        elif side == "left" and dst_x2 < 1080:
            feather = np.clip((slice_w - 1.0 - xx_s) / 240.0, 0.0, 1.0)
            feather = feather * feather * (3.0 - 2.0 * feather)
            canvas[:, dst_x1:dst_x2, :] = canvas[:, dst_x1:dst_x2, :] * (1.0 - feather) + subj_slice * feather
        else:
            canvas[:, dst_x1:dst_x2, :] = subj_slice

    yy, xx = np.mgrid[0:1350, 0:1080].astype(np.float32)
    if side == "right":
        t = np.clip((665.0 - xx) / 250.0, 0.0, 1.0)
    else:
        t = np.clip((xx - 415.0) / 250.0, 0.0, 1.0)
    mask = (t * t * (3.0 - 2.0 * t))[:, :, None]

    tint = np.array(tint_rgb, dtype=np.float32)[None, None, :]
    gx = 260.0 if side == "right" else 820.0
    gy = 470.0
    glow = np.exp(-((xx - gx) ** 2 + (yy - gy) ** 2) / (2.0 * 430.0**2))[:, :, None]
    # Hòa trộn chất liệu môi trường thật (24%) với màu chủ đạo của Style (76%) để giữ màu sắc phong cách rõ nét mà vẫn đạt WCAG >= 9.0
    rich_pad = np.clip(env_blur, 0, 145) * 0.24 + tint * (0.76 + 0.20 * glow)

    out = canvas * (1.0 - mask * 0.88) + rich_pad * (mask * 0.88)
    out_u8 = np.clip(out, 0, 255).astype(np.uint8)
    Image.fromarray(out_u8).save(out_path, "JPEG", quality=93)


# 4. Danh sách 39 Kịch bản Quảng Cáo mới (KB_32 -> KB_70)
NEW_39_KB_COPY: Dict[str, Dict[str, Any]] = {
    "KB_32": {
        "title": "Tay Khoanh Trước Ngực — Khách Lướt Khi Chưa Kịp Bật Tiếng",
        "headline_lines": ["Tay khoanh trước ngực,", "khách đã <span class=\"hl\">lướt qua</span>", "trước khi bật tiếng."],
        "hl_kw": "lướt qua",
        "sub_old": "Đứng khoanh tay phòng thủ: khách vuốt bỏ",
        "sub_new": "Đôi tay đang làm nghề thật: khách dừng xem",
        "eyebrow": "NGÔN NGỮ CƠ THỂ 3 GIÂY ĐẦU",
        "n1": "0.5s", "l1": "nhìn dáng khoanh tay", "n2": "80%", "l2": "vuốt qua chưa bật tiếng",
    },
    "KB_33": {
        "title": "Đừng Đi Chép Câu Lệnh AI — Kho Nguyên Liệu Ở Quầy Nhà Bạn",
        "headline_lines": ["Đừng chép văn mẫu,", "kho kịch bản nằm", "ngay <span class=\"hl\">quầy nhà bạn.</span>"],
        "hl_kw": "quầy nhà bạn.",
        "sub_old": "Xin câu lệnh AI trên mạng: chữ rỗng tuếch",
        "sub_new": "Ghi lại câu khách hỏi ở quầy: ra đơn thật",
        "eyebrow": "MỎ VÀNG NỘI DUNG TẠI TIỆM",
        "n1": "100", "l1": "bài văn mẫu AI giống hệt", "n2": "01", "l2": "câu hỏi thật tại quầy",
    },
    "KB_34": {
        "title": "Đứng Tiệm Từ Sáng Đến Tối — Ốm Ba Hôm Là Tiệm Vắng",
        "headline_lines": ["Đứng tiệm cả ngày,", "chủ ốm ba hôm", "là <span class=\"hl\">tiệm vắng tanh.</span>"],
        "hl_kw": "tiệm vắng tanh.",
        "sub_old": "Bán sức mặt đối mặt: nghỉ làm là đứt khách",
        "sub_new": "Đóng gói tay nghề lên video: khách tự tìm",
        "eyebrow": "THOÁT BẪY TỰ LÀM KHỔ CHỦ",
        "n1": "12h", "l1": "đứng tiệm rạc cả chân", "n2": "24/7", "l2": "video đón khách thay bạn",
    },
    "KB_35": {
        "title": "Ngành Khô Như Ngói Lại Là Chỗ Một Mình Một Chợ",
        "headline_lines": ["Ngành khô như ngói", "lại là mảnh đất", "một mình <span class=\"hl\">một chợ.</span>"],
        "hl_kw": "một chợ.",
        "sub_old": "Sợ ngành kỹ thuật khô khan: không dám quay",
        "sub_new": "Đối thủ đều ngại nói: bạn lên là độc chiếm",
        "eyebrow": "LỢI THẾ NGÀNH KỸ THUẬT KHÓ",
        "n1": "99%", "l1": "đối thủ cùng ngành im lặng", "n2": "01", "l2": "mình bạn đứng đầu thị trường",
    },
    "KB_36": {
        "title": "Xe Siêu Sang Đắp Đất Sét Bằng Tay, Bạn Lại Đọc Thông Số",
        "headline_lines": ["Hãng xe triệu đô", "khoe bàn tay thợ,", "bạn đọc <span class=\"hl\">thông số.</span>"],
        "hl_kw": "thông số.",
        "sub_old": "Đọc thông số kỹ thuật khô cứng: khách ngáp",
        "sub_new": "Quay cận cảnh độ tỉ mỉ đôi tay: giữ giá cao",
        "eyebrow": "BÍ MẬT ĐỊNH GIÁ HÀNG CAO CẤP",
        "n1": "0đ", "l1": "cảm xúc khi đọc thông số", "n2": "3x", "l2": "giá trị khi thấy tay nghề",
    },
    "KB_37": {
        "title": "Câu Mở Đầu Hay Nhất Là Tiếng Thở Dài Của Khách Ở Quầy",
        "headline_lines": ["Câu mở đầu đắt nhất", "là tiếng <span class=\"hl\">thở dài</span>", "của khách ở quầy."],
        "hl_kw": "thở dài",
        "sub_old": "Vò đầu nghĩ câu giật tít: nghe đầy mùi quảng cáo",
        "sub_new": "Nhắc đúng câu khách vừa than: chạm trúng tim",
        "eyebrow": "NGHỆ THUẬT MỞ MÀN 3 GIÂY",
        "n1": "03s", "l1": "nhắc đúng nỗi đau thật", "n2": "90%", "l2": "khách dừng lại nghe tiếp",
    },
    "KB_38": {
        "title": "Đầu Óc Người Xem Không Phải Cái Ổ Cứng",
        "headline_lines": ["Đầu óc người xem", "lướt mạng tối ngày", "không phải <span class=\"hl\">ổ cứng.</span>"],
        "hl_kw": "ổ cứng.",
        "sub_old": "Nhồi 5–7 ý vào 1 clip: khách quên sạch trơn",
        "sub_new": "Mỗi bài găm đúng 1 hình ảnh: nhớ cả năm",
        "eyebrow": "QUY LUẬT ĐỘ NÉN NHẬN THỨC",
        "n1": "05 ý", "l1": "nhồi nhét: nhớ bằng không", "n2": "01 ý", "l2": "sắc lẹm: khách tự nhắn",
    },
    "KB_39": {
        "title": "Tắt Quảng Cáo Hai Hôm — Hộp Thư Im Như Chùa Bà Đanh",
        "headline_lines": ["Tắt quảng cáo hai hôm,", "hộp thư tiệm bạn", "<span class=\"hl\">im bặt</span> tin nhắn."],
        "hl_kw": "im bặt",
        "sub_old": "Chạy bài bán hàng sỗ sàng: tắt tiền là tắt thở",
        "sub_new": "Xây kho video giải mã nghề: khách tự đổ về",
        "eyebrow": "TÀI SẢN KÊNH VS TIỀN THUÊ CHỖ",
        "n1": "0đ", "l1": "tài sản khi chỉ chạy rác", "n2": "100%", "l2": "khách ấm từ kho bài nghề",
    },
    "KB_40": {
        "title": "Quy Tắc 20 Giây — Để Máy Ngồi Sẵn Ở Góc Bàn Chờ Bạn",
        "headline_lines": ["Đừng cất chân máy,", "hãy để nó <span class=\"hl\">ngồi sẵn</span>", "ngay góc bàn làm."],
        "hl_kw": "ngồi sẵn",
        "sub_old": "Mỗi lần quay mất 30 phút lắp đồ: nản bỏ cuộc",
        "sub_new": "Bấm nút trong 20 giây lúc làm: đều đặn mỗi tuần",
        "eyebrow": "QUY TẮC 20 GIÂY CHỐNG LƯỜI",
        "n1": "30p", "l1": "bày đồ nghề: 3 bữa bỏ", "n2": "20s", "l2": "bấm máy ngay: bền cả năm",
    },
    "KB_41": {
        "title": "Đọc Lại Vỏ Hộp Thì Khách Đem Lên Sàn So Giá",
        "headline_lines": ["Chỉ đọc vỏ hộp", "thì khách chụp lại", "lên sàn <span class=\"hl\">so giá rẻ.</span>"],
        "hl_kw": "so giá rẻ.",
        "sub_old": "Đọc thành phần in sẵn trên bao bì: mất khách",
        "sub_new": "Chỉ cách khám đúng bệnh & liều dùng: chốt đơn",
        "eyebrow": "GIÁ TRỊ CỦA NGƯỜI KÊ ĐƠN",
        "n1": "100%", "l1": "so giá nếu chỉ đọc nhãn", "n2": "01", "l2": "lời khuyên nghề giữ chân khách",
    },
    "KB_42": {
        "title": "Đem Mạ Non Ba Hôm Đi Đo Với Cây Đa Đầu Làng",
        "headline_lines": ["Mới quay ba bài", "đừng đem so với", "<span class=\"hl\">cây đa</span> năm năm."],
        "hl_kw": "cây đa",
        "sub_old": "Nhìn kênh lớn rồi tự ti xóa bài: đứt gánh sớm",
        "sub_new": "Nói chuẩn từng bài cho 50 khách thật: ra tiền",
        "eyebrow": "TÂM THẾ NGƯỜI MỚI XÂY KÊNH",
        "n1": "03", "l1": "bài đầu làm quen ống kính", "n2": "30", "l2": "bài chuẩn nghề tạo uy tín",
    },
    "KB_43": {
        "title": "Bình Luận Toàn Hữu Ích Quá Mà Chẳng Ai Biết Bước Tiếp Theo",
        "headline_lines": ["Khách khen hữu ích", "rồi đi mất hút", "vì thiếu <span class=\"hl\">lối rẽ.</span>"],
        "hl_kw": "lối rẽ.",
        "sub_old": "Chia sẻ xong chào tạm biệt: khách xem chùa",
        "sub_new": "Mở đúng nút thắt kế tiếp: khách nhắn hỏi mua",
        "eyebrow": "CẦU NỐI TỪ HỮU ÍCH SANG ĐƠN HÀNG",
        "n1": "100", "l1": "lời khen xã giao không mua", "n2": "01", "l2": "câu dẫn mở đường vào hộp thư",
    },
    "KB_44": {
        "title": "Hàng Mới Bóng Như Nhau — Đồ Cũ Quay Lại Tiệm Mới Nói Thật",
        "headline_lines": ["Lúc mới mua về", "hàng nào cũng bóng,", "ba năm mới <span class=\"hl\">biết mặt.</span>"],
        "hl_kw": "biết mặt.",
        "sub_old": "Chỉ khoe hàng mới khui hộp: ai cũng nói được",
        "sub_new": "Quay món đồ khách dùng 3 năm đem bảo dưỡng: tin ngay",
        "eyebrow": "BẰNG CHỨNG THỜI GIAN ĐẮT GIÁ",
        "n1": "01", "l1": "món đồ bền sau 3 năm dùng", "n2": "10", "l2": "lời quảng cáo có cánh",
    },
    "KB_45": {
        "title": "Áp Mẫu Giật Đùng Đùng Lên Cái Tủ Vài Chục Triệu",
        "headline_lines": ["Đồ tiền chục triệu", "đừng ghép nhạc giật", "như <span class=\"hl\">hàng chợ chiều.</span>"],
        "hl_kw": "hàng chợ chiều.",
        "sub_old": "Hiệu ứng chớp giật, nhạc ầm ĩ: đuổi khách sang",
        "sub_new": "Khung hình tĩnh, giọng điềm đạm: hút khách giàu",
        "eyebrow": "ĐỒNG ĐIỆU KHÍ CHẤT SẢN PHẨM",
        "n1": "50tr", "l1": "đồ cao cấp cần sự tĩnh lặng", "n2": "0%", "l2": "nhạc giật đùng đùng rẻ tiền",
    },
    "KB_46": {
        "title": "Đợi Dọn Bàn Sạch Mới Quay Là Quay Muộn Mất Rồi",
        "headline_lines": ["Đợi dọn bàn sạch", "rồi mới bấm máy", "là <span class=\"hl\">nguội mất rồi.</span>"],
        "hl_kw": "nguội mất rồi.",
        "sub_old": "Dọn sạch hết đồ nghề mới ngồi nói: giống diễn",
        "sub_new": "Quay ngay lúc trên bàn đang ngổn ngang việc: thật",
        "eyebrow": "SỨC HÚT CỦA HIỆN TRƯỜNG SỐNG",
        "n1": "0%", "l1": "niềm tin ở bàn trống trơn", "n2": "100%", "l2": "sự thật lúc đang làm dở tay",
    },
    "KB_47": {
        "title": "Cái Quạt Nhỏ 2 Triệu Lượt Xem, Không Ai Nhớ Người Cầm Quạt",
        "headline_lines": ["Hai triệu lượt xem", "nhưng không ai nhớ", "<span class=\"hl\">khuôn mặt</span> của bạn."],
        "hl_kw": "khuôn mặt",
        "sub_old": "Đu trend vô thưởng vô phạt: view cao túi rỗng",
        "sub_new": "Gắn chặt góc nhìn nghề với tên bạn: khách tìm",
        "eyebrow": "VIEW RỖNG VS NHẬN DIỆN CHỦ NGHỀ",
        "n1": "2M", "l1": "view xem vui rồi quên mặt", "n2": "500", "l2": "khách nhớ tên và chuyển khoản",
    },
    "KB_48": {
        "title": "Bán Khay Đá Phát Sáng Mà Chén Trà Chiếm Hết Khung Hình",
        "headline_lines": ["Quay thứ định bán", "hay đang quay nhầm", "<span class=\"hl\">đạo cụ</span> xung quanh?"],
        "hl_kw": "đạo cụ",
        "sub_old": "Bối cảnh rườm rà nuốt chửng sản phẩm chính",
        "sub_new": "Đưa điểm ăn tiền nhất vào đúng tâm mắt 3 giây",
        "eyebrow": "TIÊU ĐIỂM THỊ GIÁC TRONG VIDEO",
        "n1": "80%", "l1": "khung hình bị đạo cụ lấn", "n2": "01", "l2": "điểm sáng duy nhất hút mắt",
    },
    "KB_49": {
        "title": "Cầm Tờ Rơi Đọc Thì Người Mới Hai Tuần Cũng Đọc Được",
        "headline_lines": ["Đọc tờ rơi hãng", "thì nhân viên mới", "hai tuần <span class=\"hl\">cũng thuộc.</span>"],
        "hl_kw": "cũng thuộc.",
        "sub_old": "Nói lại chữ trên brochure: không thấy chất chuyên gia",
        "sub_new": "Chỉ ra giới hạn mà tờ rơi giấu nhẹm: khách nể",
        "eyebrow": "RANH GIỚI THỢ LÂU NĂM & NGƯỜI MỚI",
        "n1": "14", "l1": "ngày học thuộc lòng tờ rơi", "n2": "10", "l2": "năm kinh nghiệm nhìn ra lỗi",
    },
    "KB_50": {
        "title": "Thử Máy Lau Nhà Trên Cái Sàn Đã Lau Sạch Sẵn",
        "headline_lines": ["Đừng thử máy khỏe", "trên cái sàn nhà", "đã <span class=\"hl\">lau sạch bóng.</span>"],
        "hl_kw": "lau sạch bóng.",
        "sub_old": "Quay cảnh thử hàng êm ru giả tạo: khách nghi ngờ",
        "sub_new": "Đưa vào ca khó và bẩn thật: thuyết phục tuyệt đối",
        "eyebrow": "PHÉP THỬ ÁP LỰC CAO TRƯỚC ỐNG KÍNH",
        "n1": "0%", "l1": "thuyết phục trên sàn sạch sẵn", "n2": "100%", "l2": "tin tưởng khi xử lý ca khó",
    },
    "KB_51": {
        "title": "Bán Đai Gối Cho Người Sáu Mươi Mà Đưa Chân Hai Mươi Ra Thử",
        "headline_lines": ["Bán cho người già", "sao lại lấy chân", "tuổi <span class=\"hl\">hai mươi</span> thử?"],
        "hl_kw": "hai mươi",
        "sub_old": "Lấy mẫu trẻ khỏe diễn thử: khách thật thấy xa lạ",
        "sub_new": "Đặt đúng hình ảnh người dùng thật: gật đầu mua",
        "eyebrow": "ĐÚNG CHÂN DUNG NGƯỜI MUA THẬT",
        "n1": "20t", "l1": "mẫu diễn: khách 60t lướt qua", "n2": "60t", "l2": "đúng bệnh thật: con cái đặt mua",
    },
    "KB_52": {
        "title": "Miệng Khuyên Vận Động Mà Ngồi Im Trong Phòng Tối Ba Phút",
        "headline_lines": ["Miệng khuyên năng động", "mà người ngồi im", "trong <span class=\"hl\">phòng tối om.</span>"],
        "hl_kw": "phòng tối om.",
        "sub_old": "Hình ảnh trái ngược hoàn toàn với lời khuyên",
        "sub_new": "Bối cảnh và nhịp thở khớp 100% thông điệp nghề",
        "eyebrow": "SỰ NHẤT QUÁN HÌNH ẢNH & LỜI NÓI",
        "n1": "0%", "l1": "năng lượng khi ngồi phòng tối", "n2": "3x", "l2": "sức truyền cảm ngoài hiện trường",
    },
    "KB_53": {
        "title": "Một Bài Ăn Hồng Dẫn Nhầm Cả Đoàn Khách Vào Kênh Sửa Nhà",
        "headline_lines": ["Một clip lạc đề", "dẫn nhầm tệp khách", "làm <span class=\"hl\">hỏng thuật toán.</span>"],
        "hl_kw": "hỏng thuật toán.",
        "sub_old": "Thấy gì đăng nấy: AI phân phối loạn tệp người xem",
        "sub_new": "Giữ đúng trục chuyên môn: AI tìm chuẩn khách mua",
        "eyebrow": "KỶ LUẬT TỆP KHÁCH HÀNG CHO AI",
        "n1": "01", "l1": "clip lệch tệp phá hỏng kênh", "n2": "100%", "l2": "đồng nhất chủ đề hút khách sộp",
    },
    "KB_54": {
        "title": "Đồ Ăn Uống Vào Bụng Mà Chỉ Quay Cái Bình, Khách Xin Công Thức Tự Ngâm",
        "headline_lines": ["Đồ uống vào người", "chỉ quay cái bình", "khách về <span class=\"hl\">tự ngâm.</span>"],
        "hl_kw": "tự ngâm.",
        "sub_old": "Chỉ khoe nguyên liệu thô: khách tự mua về làm",
        "sub_new": "Cho thấy tiêu chuẩn khử độc & tay nghề: khách đặt",
        "eyebrow": "BÁN QUY TRÌNH AN TOÀN CHỨ KHÔNG BÁN THÔ",
        "n1": "0đ", "l1": "nếu khách chỉ xin công thức", "n2": "95%", "l2": "chốt đơn vì độ sạch & kỹ",
    },
    "KB_55": {
        "title": "Ảnh Hãng Phát Cho Trăm Đại Lý, Đoạn Tự Đi Công Trường Thì Cất Trong Máy",
        "headline_lines": ["Đăng ảnh của hãng", "trăm nơi giống hệt,", "phí <span class=\"hl\">công trường</span> thật."],
        "hl_kw": "công trường",
        "sub_old": "Đăng ảnh bóng bẩy hãng cấp: chìm nghỉm giữa chợ",
        "sub_new": "Mở máy lấy 15 giây lội công trường: khách chọn bạn",
        "eyebrow": "KHO BÁU NẰM TRONG CUỘN CAMERA",
        "n1": "100", "l1": "đại lý đăng chung 1 tấm ảnh", "n2": "01", "l2": "clip công trường thật ăn đứt",
    },
    "KB_56": {
        "title": "Tả Đúng Lúc Khách Đứng Cọ Nồi — Khách Tự Hiểu Bạn Làm Nghề Lâu",
        "headline_lines": ["Tả trúng cảnh khách", "đứng <span class=\"hl\">cọ đáy nồi,</span>", "khách biết thợ sâu."],
        "hl_kw": "cọ đáy nồi,",
        "sub_old": "Khen inox 304 sáng bóng: khách nghe nhàm tai",
        "sub_new": "Nói đúng cảnh cọ vết khét mỏi lưng: khách mua ngay",
        "eyebrow": "LÁT CẮT VẬT LÝ ĐỜI THƯỜNG 3 GIÂY",
        "n1": "03s", "l1": "gọi đúng cảnh mỏi lưng ở bếp", "n2": "10x", "l2": "sức thuyết phục hơn chữ inox",
    },
    "KB_57": {
        "title": "Lật Ngửa Cái Gầm Bàn Lên — Vừa Khỏi Tự Khen Vừa Đỡ Ngượng",
        "headline_lines": ["Đừng tự khen mình,", "hãy lật ngửa", "<span class=\"hl\">cái gầm bàn</span> lên."],
        "hl_kw": "cái gầm bàn",
        "sub_old": "Ngồi trước máy tự khen hàng tốt: ngượng cứng miệng",
        "sub_new": "Soi thẳng vào góc khuất kỹ thuật: tự tin tuyệt đối",
        "eyebrow": "CÁCH CHỮA NGƯỢNG CHO NGƯỜI LÀM NGHỀ",
        "n1": "0%", "l1": "phải tự khen mình câu nào", "n2": "100%", "l2": "mối ghép gầm bàn tự lên tiếng",
    },
    "KB_58": {
        "title": "Ngại Đàn Anh Bảo Múa Rìu Qua Mắt Thợ, Nên Nói Giọng Báo Cáo",
        "headline_lines": ["Sợ đồng nghiệp chê", "nên bạn nói giọng", "<span class=\"hl\">báo cáo</span> cuối năm."],
        "hl_kw": "báo cáo",
        "sub_old": "Cố dùng từ hàn lâm cho đồng nghiệp nể: mất khách",
        "sub_new": "Nói giản dị như chỉ cho em út trong nhà: ra đơn",
        "eyebrow": "THOÁT ÁM ẢNH ĐỒNG NGHIỆP PHÁN XÉT",
        "n1": "0đ", "l1": "từ lời khen của đồng nghiệp", "n2": "100%", "l2": "doanh thu từ khách hàng hiểu bài",
    },
    "KB_59": {
        "title": "Tảng Băng Chìm 90% Khách Tàu Ngầm & Hợp Đồng Lớn Từ Bài 0 Like",
        "headline_lines": ["Bài chuyên môn sâu", "ít người bấm thích", "nhưng ra <span class=\"hl\">đơn lớn.</span>"],
        "hl_kw": "đơn lớn.",
        "sub_old": "Thấy bài chuyên môn ít like vội xóa đi: sai lầm",
        "sub_new": "90% khách giàu tàu ngầm đọc kỹ rồi nhắn riêng",
        "eyebrow": "TẢNG BĂNG CHÌM 90% KHÁCH TÀU NGẦM",
        "n1": "90%", "l1": "khách lớn không bao giờ thả tim", "n2": "01", "l2": "tin nhắn chốt hợp đồng trăm triệu",
    },
    "KB_60": {
        "title": "Bẫy Đóng Cửa Rèn Kiếm 6 Tháng vs Cánh Cửa Sơn Giả 30 Phút",
        "headline_lines": ["Đừng đóng cửa tiệm", "rèn kiếm sáu tháng", "khi chưa <span class=\"hl\">thử chợ.</span>"],
        "hl_kw": "thử chợ.",
        "sub_old": "Ôm ấp dự án kín mít 6 tháng: ra chợ không ai cần",
        "sub_new": "Đăng 1 bài 30 phút đo phản ứng thật: trúng đích",
        "eyebrow": "PHÉP THỬ CÁNH CỬA SƠN GIẢ (PRIESTLEY)",
        "n1": "06th", "l1": "đóng cửa đoán mò một mình", "n2": "30p", "l2": "lên bài biết ngay khách cần gì",
    },
    "KB_61": {
        "title": "Phòng Trà 7 Tiếng & Lời Cầu Hôn Ngoài Ngã Tư",
        "headline_lines": ["Chưa đủ bảy tiếng", "đừng vội cầu hôn", "giữa <span class=\"hl\">ngã tư đường.</span>"],
        "hl_kw": "ngã tư đường.",
        "sub_old": "Gặp khách lạ giây đầu đã đòi chốt đơn: khách chạy",
        "sub_new": "Nuôi đủ 7 giờ tin cậy qua chuỗi bài: khách tự mua",
        "eyebrow": "QUY LUẬT 7 GIỜ – 11 ĐIỂM CHẠM",
        "n1": "07h", "l1": "xem kênh tạo niềm tin sâu", "n2": "01p", "l2": "chốt đơn nhẹ nhàng không ép",
    },
    "KB_62": {
        "title": "Giải Oan Sự Lười Biếng — Cú Lừa Phí Ship 40 Nghìn Cho Ly Nước 20 Nghìn",
        "headline_lines": ["Bạn không hề lười,", "chỉ vì phí sức", "đắt gấp <span class=\"hl\">hai lần</span> lời."],
        "hl_kw": "hai lần",
        "sub_old": "Quay 1 clip mất 4 tiếng dựng: não tự động đình công",
        "sub_new": "Hạ phí sức xuống 15 phút/bài: làm nhẹ như hơi thở",
        "eyebrow": "KINH TẾ HỌC HÀNH VI TRƯỚC ỐNG KÍNH",
        "n1": "04h", "l1": "dựng 1 bài: não sợ bỏ cuộc", "n2": "15p", "l2": "quy trình gọn: duy trì mỗi tuần",
    },
    "KB_63": {
        "title": "Tự Tin Là Tờ Biên Lai Kế Toán & Đạp Phanh Trên Mặt Băng",
        "headline_lines": ["Đợi có tự tin", "mới dám bấm máy", "là <span class=\"hl\">đợi cả đời.</span>"],
        "hl_kw": "đợi cả đời.",
        "sub_old": "Chờ hết ngại mới làm: giống đợi biên lai trước khi mua",
        "sub_new": "Bấm máy xong 5 bài tự khắc có tờ biên lai tự tin",
        "eyebrow": "TỰ TIN LÀ KẾT QUẢ, KHÔNG PHẢI ĐIỀU KIỆN",
        "n1": "0%", "l1": "ai tự tin ngay từ clip số 1", "n2": "05", "l2": "bài làm thật sinh ra bản lĩnh",
    },
    "KB_64": {
        "title": "Nghịch Lý Bục Giảng & Bàn Trà — Nói 3 Tiếng Rất Cuốn, Bật Máy Lại Khớp",
        "headline_lines": ["Ở bàn nói cuốn,", "sao bật máy lên", "lại thành <span class=\"hl\">bục giảng?</span>"],
        "hl_kw": "bục giảng?",
        "sub_old": "Đổi sang giọng phát biểu trang trọng: mất hồn nghề",
        "sub_new": "Giữ nguyên nhịp thủ thỉ bên bàn trà: khách mê nghe",
        "eyebrow": "NGHỊCH LÝ BỤC GIẢNG VÀ BÀN TRÀ",
        "n1": "03h", "l1": "nói chuyện bàn trà khách quý", "n2": "01", "l2": "tông giọng thật giữ trọn lên hình",
    },
    "KB_65": {
        "title": "Chiếc Nhẫn Vàng Trong Túi Nilon & Kính Lúp Tay Nghề",
        "headline_lines": ["Tay nghề vàng ròng", "đừng gói sơ sài", "trong <span class=\"hl\">túi nilon.</span>"],
        "hl_kw": "túi nilon.",
        "sub_old": "Làm nghề cực kỳ có tâm nhưng kênh nhìn nhếch nhác",
        "sub_new": "Đặt kính lúp đúng chỗ tinh xảo nhất: xứng tầm giá",
        "eyebrow": "ĐÓNG GÓI XỨNG TẦM CHẤT LƯỢNG THẬT",
        "n1": "9999", "l1": "vàng thật cần hộp nhung xứng tầm", "n2": "2x", "l2": "tỷ lệ chốt khách phân khúc cao",
    },
    "KB_66": {
        "title": "Tiếc 30 Phút Làm Video — Mất Cả Ngày Ngồi Chờ Khách",
        "headline_lines": ["Tiếc ba mươi phút", "quay bài mỗi tuần,", "mất <span class=\"hl\">cả ngày</span> chờ."],
        "hl_kw": "cả ngày",
        "sub_old": "Kêu bận không quay bài rồi ngồi bấm điện thoại chờ khách",
        "sub_new": "Dành 30 phút đóng gói 1 bài: khách hẹn kín lịch tuần",
        "eyebrow": "NGHỊCH LÝ THỜI GIAN CỦA CHỦ TIỆM",
        "n1": "30p", "l1": "tập trung làm 1 video chuẩn", "n2": "08h", "l2": "khỏi ngồi ngóng khách vãng lai",
    },
    "KB_67": {
        "title": "Khi Người Có Nghề Tự Tựa Vào Hữu Xạ Tự Nhiên Hương",
        "headline_lines": ["Giỏi nghề mà giấu", "trong hẻm thời nay", "hương <span class=\"hl\">chẳng bay xa.</span>"],
        "hl_kw": "chẳng bay xa.",
        "sub_old": "Đợi hữu xạ tự nhiên hương: đối thủ kém nghề lấy hết khách",
        "sub_new": "Bật quạt gió nội dung đưa tay nghề tới đúng người cần",
        "eyebrow": "HỮU XẠ CẦN THÊM GIÓ THỜI SỐ",
        "n1": "10", "l1": "năm giỏi nghề trong im lặng", "n2": "01", "l2": "kênh chuẩn đưa hương bay xa",
    },
    "KB_68": {
        "title": "Đóng Gói Bài Tư Vấn Tại Bàn Thành Video 1 Phút",
        "headline_lines": ["Mỗi lần tư vấn", "là một kịch bản", "<span class=\"hl\">một phút</span> ăn tiền."],
        "hl_kw": "một phút",
        "sub_old": "Tư vấn xong cho 1 người rồi lời nói bay theo gió",
        "sub_new": "Tóm đúng 3 câu đắt nhất thành clip 1 phút: ngàn người nghe",
        "eyebrow": "NHÂN BẢN BUỔI TƯ VẤN LÊN 1000 LẦN",
        "n1": "01", "l1": "buổi tư vấn trực tiếp tại bàn", "n2": "1000", "l2": "khách cùng nghe qua clip 60s",
    },
    "KB_69": {
        "title": "Chuyên Môn Vững Nhưng Vắng Khách — Thiếu Cây Cầu Phiên Dịch",
        "headline_lines": ["Chuyên môn rất vững", "mà tiệm vắng khách", "vì thiếu <span class=\"hl\">phiên dịch.</span>"],
        "hl_kw": "phiên dịch.",
        "sub_old": "Nói bằng ngôn ngữ thợ: khách nghe không hiểu giá trị",
        "sub_new": "Phiên dịch tay nghề ra lợi ích sát sườn: khách gật đầu",
        "eyebrow": "CÂY CẦU NỐI TAY NGHỀ VỚI VÍ TIỀN KHÁCH",
        "n1": "10/10", "l1": "tay nghề giỏi trong xưởng", "n2": "100%", "l2": "khách hiểu ngay sau 3 câu ví von",
    },
    "KB_70": {
        "title": "Bất Động Sản & Nghề Vốn Lớn — 30 Phút Đập Tan Sự Trì Hoãn",
        "headline_lines": ["Nghề đơn tiền tỷ", "chần chừ một tháng", "mất cả <span class=\"hl\">mùa khách.</span>"],
        "hl_kw": "mùa khách.",
        "sub_old": "Đợi rảnh, đợi đẹp, đợi hoàn hảo: lỡ sóng thị trường",
        "sub_new": "Ra hiện trường quay 30 phút: đón trọn tệp nhà đầu tư",
        "eyebrow": "TỐC ĐỘ THỰC THI NGÀNH GIÁ TRỊ CAO",
        "n1": "30p", "l1": "bấm máy phân tích tại thực địa", "n2": "01", "l2": "nhà đầu tư lớn nhắn tin riêng",
    },
}


def populate_all_21_subbox_fields(entry: Dict[str, Any]) -> Dict[str, Any]:
    """Đảm bảo mọi kịch bản (KB_01 -> KB_70) đều có đủ dữ liệu cho toàn bộ 21 khuôn K01 -> K21."""
    k01 = entry.get("k01", {})
    k02 = entry.get("k02", {})
    k03 = entry.get("k03", {})
    old_txt = entry.get("sub_old") or k01.get("old") or "Làm theo thói quen cũ: khách xem rồi lướt"
    new_txt = entry.get("sub_new") or k01.get("new") or "Làm đúng chuẩn nghề: khách nhớ & tự nhắn"
    eyebrow = entry.get("eyebrow") or k02.get("eyebrow") or "ĐÚC KẾT THỰC CHIẾN K4"
    n1 = entry.get("n1") or k03.get("n1") or "10x"
    l1 = entry.get("l1") or k03.get("l1") or "tốn sức kiểu cũ"
    n2 = entry.get("n2") or k03.get("n2") or "01"
    l2 = entry.get("l2") or k03.get("l2") or "bài chuẩn khách nhắn"

    entry["k01"] = {"old": old_txt, "new": new_txt}
    entry["k02"] = {"eyebrow": eyebrow, "l1": old_txt + ".", "l2": new_txt + "."}
    entry["k03"] = {"n1": n1, "l1": l1, "n2": n2, "l2": l2}
    entry["k04"] = {"tab": eyebrow[:22], "l1": old_txt, "l2": new_txt}
    entry["k05"] = {"l1": old_txt, "s1": "đổi cách làm", "s2": new_txt}
    entry["k06"] = {"not": old_txt, "but": new_txt}
    entry["k07"] = {"lh": "CÁCH CŨ TỐN SỨC", "lb": old_txt, "rh": "CHUẨN NGHỀ K4", "rb": new_txt}
    entry["k08"] = {"l1": old_txt + ".", "l2_pre": "→ ", "l2_ul": new_txt}
    entry["k09"] = {"meta": "Khách hàng · vừa nhắn", "msg1": "“Xem đúng bài phân tích này,", "msg2": new_txt.lower() + "!”"}
    entry["k10"] = {"lbl1": "Cách làm cũ", "val1": "10% nhớ", "lbl2": "Chuẩn nghề K4", "val2": "95% nhắn"}
    entry["k11"] = {"q": old_txt + "?", "a": new_txt}
    entry["k12"] = {"l1": old_txt, "l2": new_txt}
    entry["k13"] = {"t1": "Bước 1: Bỏ " + old_txt.split(":")[0].lower(), "t2": "Bước 2: " + new_txt}
    entry["k14"] = {"old": old_txt, "new": new_txt}
    entry["k15"] = {"caption": new_txt}
    entry["k16"] = {"l1": old_txt, "l2": new_txt}
    parts_old = old_txt.split(":") if ":" in old_txt else [old_txt[:22], "khách lướt"]
    parts_new = new_txt.split(":") if ":" in new_txt else [new_txt[:22], "khách nhắn"]
    entry["k17"] = {
        "l_old": parts_old[0].strip(), "r_old": parts_old[1].strip(),
        "l_new": parts_new[0].strip(), "r_new": parts_new[1].strip(),
    }
    entry["k18"] = {"p1": "Đúng nỗi đau", "p2": "Chất nghề thật", "res": new_txt}
    entry["k19"] = {"c1": "Dừng ngay: " + old_txt, "c2": new_txt}
    entry["k20"] = {"benh": old_txt, "thuoc": new_txt}
    entry["k21"] = {"l1": old_txt, "l2": new_txt}
    return entry


def main():
    reg = json.loads(OUTFIT_REG_PATH.read_text(encoding="utf-8"))
    old_master = json.loads(OLD_SPECS_PATH.read_text(encoding="utf-8"))
    old_kbs = old_master.get("kbs", {})

    selected_70 = select_70_unique_outfits(reg)
    print(f"Selected {len(selected_70)} unique single-portrait outfits across 32 banner.html styles.")

    h_codes = [f"H{i:02d}" for i in range(1, 21)]
    k_codes = [f"K{i:02d}" for i in range(1, 22)]

    bg_pool: Dict[str, str] = {}
    all_kbs: Dict[str, Any] = {}
    bg_tasks = []

    for idx in range(70):
        kb_num = idx + 1
        kb_id = f"KB_{kb_num:02d}"
        oid, oinfo = selected_70[idx]
        card_prefix = oid[:3]
        style_label, tint_rgb, accent_hex = CARD_STYLE_PROFILES[card_prefix]
        side = "right" if (idx % 2 == 0) else "left"

        bg_key = f"BG_{kb_id}_{oid}_{side.upper()}"
        bg_path = BG_POOL_70_DIR / f"{bg_key.lower()}.jpg"
        bg_pool[bg_key] = str(bg_path)
        bg_tasks.append((oid, oinfo, side, tint_rgb, bg_path))

        # Gán xoay vòng 20 Font H01..H20 & 21 Khuôn K01..K21
        h_code = h_codes[idx % len(h_codes)]
        k_code = k_codes[idx % len(k_codes)]
        alt_k_code = k_codes[(idx + 7) % len(k_codes)]

        if kb_id in old_kbs:
            entry = dict(old_kbs[kb_id])
        elif kb_id == "KB_01":
            entry = {
                "title": "Giỏi Mà Tàng Hình — Tắt Chế Độ Tàng Hình",
                "headline_lines": ["Làm nghề mười năm", "sao trên mạng vẫn", "<span class=\"hl\">tàng hình</span> hoàn toàn?"],
                "hl_kw": "tàng hình",
                "sub_old": "Giỏi nghề nhưng im lặng: khách vào tay đối thủ",
                "sub_new": "Đóng gói uy tín lên kênh: khách tự tìm đến",
                "eyebrow": "TẮT CHẾ ĐỘ TÀNG HÌNH K4",
                "n1": "10 năm", "l1": "làm nghề giỏi trong bóng tối", "n2": "01", "l2": "kênh chuẩn hút khách tự nhiên",
            }
        elif kb_id == "KB_15":
            entry = {
                "title": "Đừng Ép Mình Đăng Bài Vội Vã Mỗi Ngày",
                "headline_lines": ["Đừng ép mình", "đăng bài <span class=\"hl\">vội vã</span>", "mỗi ngày."],
                "hl_kw": "vội vã",
                "sub_old": "10 clip quay vội: khách xem rồi lướt qua",
                "sub_new": "1 bài trúng việc: khách nhớ & tự nhắn",
                "eyebrow": "CHẤT LƯỢNG THẮNG SỐ LƯỢNG",
                "n1": "10", "l1": "clip quay vội khách lướt", "n2": "01", "l2": "bài trúng việc khách nhắn",
            }
        else:
            entry = dict(NEW_39_KB_COPY[kb_id])

        entry["bg"] = bg_key
        entry["side"] = side
        entry["outfit_id"] = oid
        entry["banner_style_name"] = style_label
        entry["accent_color"] = accent_hex
        entry["h_code"] = h_code
        entry["h_name"] = HEADLINE_20_FONTS[h_code]["name"]
        entry["style"] = k_code
        entry["alt_style"] = alt_k_code
        entry = populate_all_21_subbox_fields(entry)
        all_kbs[kb_id] = entry

    print(f"Building {len(bg_tasks)} seamless 1080x1350 diverse backgrounds in parallel...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        futs = [ex.submit(build_seamless_diverse_bg, t[0], t[1], t[2], t[3], t[4]) for t in bg_tasks]
        for f in concurrent.futures.as_completed(futs):
            f.result()

    # Map style_fonts compatibility + h_fonts dictionary
    style_fonts_compat = {}
    for i, kc in enumerate(k_codes):
        hc = h_codes[i % len(h_codes)]
        hf = HEADLINE_20_FONTS[hc]
        style_fonts_compat[kc] = [hf["file"], hf["name"], hf["base_fs"], hf["base_lh"]]

    master_out = {
        "version": "5.0-70kb-diverse",
        "total_kbs": 70,
        "bg_pool": bg_pool,
        "headline_fonts": HEADLINE_20_FONTS,
        "style_names": STYLE_21_NAMES,
        "style_fonts": style_fonts_compat,
        "kbs": all_kbs,
    }
    OLD_SPECS_PATH.write_text(json.dumps(master_out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Saved 70 KB Master Specs + 70 Unique Outfit/Style BGs to {OLD_SPECS_PATH}")


if __name__ == "__main__":
    main()
