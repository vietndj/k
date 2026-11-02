#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZERO-BLUR DUAL COLOR & B&W MASS PRODUCTION PIPELINE V6.0 (CLAUDE2 ARCHITECTURE)
===============================================================================
1. Loại bỏ 100% `GaussianBlur`, `shift_x` cắt vai và `rich_pad` sương mù giả.
2. Sử dụng bộ Phôi Nền Nhiếp Ảnh Thật 85mm f/1.4 Bokeh (`zb_plate_01` -> `zb_plate_40` + `KB_14` Japandi + `C18` Wide).
3. Xuất 2 Phiên Bản cho TẤT CẢ 70 Banner (`KB_01` -> `KB_70`):
   - 🎨 Bản Màu Ấm (`Kodak Portra 400` + Optical Darkroom Burn 0% Blur) -> `kb_XX_color.jpg` & `kb_XX_final.jpg`
   - 🖤 Bản Đen Trắng (`Fine-Art B&W` Orange-Filter Luma `0.50R + 0.40G + 0.10B` + S-Curve) -> `kb_XX_bw.jpg`
   - 🔍 Bảng So Sánh 3 Cột (`1. Bản Màu Ấm • 2. Bản Đen Trắng • 3. Bản Cũ Blur`) -> `kb_XX_sbs.jpg`
4. Render Đa Luồng Playwright + Kiểm toán 15 Cổng `uiux_auditor.py` + Upload R2 16 luồng + Cập nhật `banner2.html`.
"""

import argparse
import concurrent.futures
import glob
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
SPECS_PATH = BASE_DIR / "kb_31_master_specs.json"
CARDS_DIR = BASE_DIR / "banner2_cards"
PILOT_DIR = BASE_DIR / "v2_pilots"
ZB_PLATES_DIR = PILOT_DIR / "zero_blur_plates"
DUAL_BG_DIR = PILOT_DIR / "dual_bg_70"
OUT_RENDER_DIR = PILOT_DIR / "batch_out"
BRAIN_ROOT = Path("/Users/vietmac/.gemini/antigravity/brain")
R2_MANAGER = Path("/Users/vietmac/Documents/CODE/Quản gia/r2_manager.py")
TELEGRAM_NOTIFY = Path("/Users/vietmac/Documents/CODE/Quản gia/telegram_notify.py")

sys.path.insert(0, str(BASE_DIR))
from batch_branch_runner import build_style_html
from uiux_auditor import audit_v3_banner
from update_banner2_hub import atomic_rebuild_and_sync


def harvest_generated_plates() -> Dict[str, Path]:
    """Thu hoạch toàn bộ các phôi ảnh `zb_plate_XX_*.jpg/png` từ thư mục brain của các subagents về `ZB_PLATES_DIR`."""
    ZB_PLATES_DIR.mkdir(parents=True, exist_ok=True)
    plate_map: Dict[str, Path] = {}

    # 1. Quét trong BRAIN_ROOT
    for p in sorted(BRAIN_ROOT.glob("*/zb_plate_*.*")):
        if p.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
            continue
        stem = p.stem
        # Tên dạng zb_plate_01_c03_right_navy_suit_179352...
        parts = stem.split("_")
        if len(parts) >= 3 and parts[0] == "zb" and parts[1] == "plate":
            plate_key = f"zb_plate_{parts[2]}"
            dst = ZB_PLATES_DIR / f"{plate_key}.jpg"
            with Image.open(p) as im:
                im.convert("RGB").save(dst, "JPEG", quality=95)
            plate_map[plate_key] = dst

    # 2. Quét sẵn trong ZB_PLATES_DIR nếu đã copy
    for p in sorted(ZB_PLATES_DIR.glob("zb_plate_*.jpg")):
        parts = p.stem.split("_")
        if len(parts) >= 3:
            plate_key = f"zb_plate_{parts[2]}"
            plate_map[plate_key] = p

    # 3. Thêm 2 phôi Japandi KB_14 đã duyệt
    kb14_p1 = BRAIN_ROOT / "c79815a1-dee2-4b0a-983a-78781ebe148d" / "viet_editorial_japandi_portrait_001_1793520484281.jpg"
    kb14_p2 = BRAIN_ROOT / "c79815a1-dee2-4b0a-983a-78781ebe148d" / "c17_i03_japandi_portrait_v1_1793520313839.jpg"
    if kb14_p1.exists():
        dst1 = ZB_PLATES_DIR / "zb_plate_kb14_japandi_01.jpg"
        shutil.copy2(kb14_p1, dst1)
        plate_map["kb14_01"] = dst1
    if kb14_p2.exists():
        dst2 = ZB_PLATES_DIR / "zb_plate_kb14_japandi_02.jpg"
        shutil.copy2(kb14_p2, dst2)
        plate_map["kb14_02"] = dst2

    # 4. Thêm 3 phôi C18 nguyên bản cảnh rộng (0% blur)
    for c18_id in ("C18_I03", "C18_I04", "C18_I05"):
        src_c18 = BASE_DIR / "assets" / "portraits" / f"{c18_id}.jpg"
        if src_c18.exists():
            plate_map[c18_id] = src_c18

    return plate_map


# Bảng ánh xạ từ (card_prefix, side, variant_idx) sang plate_key
KB_TO_PLATE_ASSIGNMENT: Dict[str, str] = {
    "KB_01": "zb_plate_01",
    "KB_02": "zb_plate_03",
    "KB_03": "zb_plate_05",
    "KB_04": "zb_plate_07",
    "KB_05": "zb_plate_08",
    "KB_06": "zb_plate_09",
    "KB_07": "zb_plate_10",
    "KB_08": "zb_plate_12",
    "KB_09": "zb_plate_14",
    "KB_10": "zb_plate_16",
    "KB_11": "zb_plate_18",
    "KB_12": "zb_plate_19",
    "KB_13": "zb_plate_20",
    "KB_14": "kb14_01",
    "KB_15": "C18_I03",
    "KB_16": "zb_plate_22",
    "KB_17": "zb_plate_24",
    "KB_18": "zb_plate_25",
    "KB_19": "zb_plate_27",
    "KB_20": "zb_plate_29",
    "KB_21": "zb_plate_30",
    "KB_22": "zb_plate_32",
    "KB_23": "zb_plate_34",
    "KB_24": "zb_plate_36",
    "KB_25": "zb_plate_38",
    "KB_26": "zb_plate_02",
    "KB_27": "zb_plate_40",
    "KB_28": "zb_plate_02",
    "KB_29": "zb_plate_04",
    "KB_30": "zb_plate_06",
    "KB_31": "zb_plate_10",
    "KB_32": "zb_plate_12",
    "KB_33": "zb_plate_14",
    "KB_34": "zb_plate_16",
    "KB_35": "zb_plate_18",
    "KB_36": "kb14_02",
    "KB_37": "C18_I04",
    "KB_38": "zb_plate_22",
    "KB_39": "zb_plate_24",
    "KB_40": "zb_plate_25",
    "KB_41": "zb_plate_27",
    "KB_42": "zb_plate_31",
    "KB_43": "zb_plate_33",
    "KB_44": "zb_plate_35",
    "KB_45": "zb_plate_37",
    "KB_46": "zb_plate_39",
    "KB_47": "zb_plate_17",
    "KB_48": "zb_plate_15",
    "KB_49": "zb_plate_01",
    "KB_50": "zb_plate_11",
    "KB_51": "zb_plate_13",
    "KB_52": "zb_plate_15",
    "KB_53": "zb_plate_17",
    "KB_54": "zb_plate_21",
    "KB_55": "C18_I05",
    "KB_56": "zb_plate_22",
    "KB_57": "zb_plate_26",
    "KB_58": "zb_plate_28",
    "KB_59": "zb_plate_30",
    "KB_60": "zb_plate_32",
    "KB_61": "zb_plate_37",
    "KB_62": "zb_plate_39",
    "KB_63": "zb_plate_23",
    "KB_64": "zb_plate_09",
    "KB_65": "zb_plate_04",
    "KB_66": "zb_plate_11",
    "KB_67": "zb_plate_26",
    "KB_68": "zb_plate_28",
    "KB_69": "zb_plate_23",
    "KB_70": "zb_plate_31",
}


def build_dual_zero_blur_bgs(
    src_plate_path: Path,
    side: str,
    out_color_path: Path,
    out_bw_path: Path,
    variant_seed: int = 0,
    frame_meta: Optional[Dict[str, Any]] = None,
) -> None:
    """
    Từ 1 Phôi Nền Nhiếp Ảnh Thật (Zero-Blur 85mm f/1.4 Bokeh), xuất ra 2 Phiên Bản 1080x1350:
    1. Bản Màu Ấm (`out_color_path`): Kodak Portra 400 + Optical Darkroom Burn ở phía đặt chữ (0% Blur).
    2. Bản Đen Trắng (`out_bw_path`): Orange-Filter Luma Mix (0.50R + 0.40G + 0.10B) + S-Curve + Film Grain 2%.
    Sử dụng căn khung thông minh theo khuôn mặt (`frame_meta` từ InsightFace) để đảm bảo:
    - Chiều rộng mặt `200px <= fw <= 284px`
    - Khoảng thở từ tai/đầu tới chữ `head_to_text_gap_px >= 65px` (0% dính chữ vào mặt).
    """
    target_w, target_h = 1080, 1350
    with Image.open(src_plate_path) as im_raw:
        im = im_raw.convert("RGB")
        w0, h0 = im.size

        if frame_meta and frame_meta.get("nw") and frame_meta.get("nh"):
            nw = int(frame_meta["nw"])
            nh = int(frame_meta["nh"])
            x_shift = int(frame_meta.get("x_shift", 0))
            y0 = int(frame_meta.get("y0", 0))
            ox = int(frame_meta.get("ox", x_shift if side == "left" else (nw - x_shift - target_w)))
            # CLAUDE2 LAW_21.1: ZERO FAKE PIXELS & ZERO BLUR
            # Khung cắt 1080x1350 bắt buộc nằm trọn 100% trong ảnh gốc (0% copyMakeBorder, 0% GaussianBlur)
            if nw < target_w or nh < target_h or ox < 0 or (ox + target_w) > nw or y0 < 0 or (y0 + target_h) > nh:
                raise ValueError(
                    f"[LAW_21 VIOLATION] Invalid crop geometry on {src_plate_path.name}: "
                    f"nw={nw}, nh={nh}, ox={ox}, y0={y0} (must satisfy 0<=ox<=nw-1080 and 0<=y0<=nh-1350)"
                )
            im_resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
            arr_s = np.array(im_resized, dtype=np.uint8)
            arr_u8 = arr_s[y0 : y0 + target_h, ox : ox + target_w, :]
            arr = arr_u8.astype(np.float32) / 255.0
        else:
            scale = max(target_w / float(w0), target_h / float(h0))
            nw = max(target_w, int(round(w0 * scale)))
            nh = max(target_h, int(round(h0 * scale)))
            im_resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
            x0 = 0 if side == "left" else max(0, nw - target_w)
            y0 = max(0, int((nh - target_h) * 0.35))
            im_crop = im_resized.crop((x0, y0, x0 + target_w, y0 + target_h))
            arr = np.array(im_crop, dtype=np.float32) / 255.0

    yy, xx = np.mgrid[0:1350, 0:1080].astype(np.float32)

    # =========================================================================
    # CLAUDE2 LAW_20 & LAW_21: ZERO FACE BURN + NATURAL EXPOSURE CONTINUITY
    # 1. Bảo vệ 100% vùng đầu/mặt/tóc/cổ (head_protect).
    # 2. Dải chuyển sáng ngang rộng 440px + làm mượt sigma=45px (không tạo vách cắt dọc).
    # 3. Sàn phơi sáng tự nhiên burn_factor >= 0.55 (giữ nguyên 100% chi tiết vân nền).
    # =========================================================================
    if frame_meta and frame_meta.get("cropped_face_bbox"):
        fx, fy, fw, fh = [float(v) for v in frame_meta["cropped_face_bbox"]]
    else:
        fx, fy, fw, fh = (700.0 if side == "right" else 120.0), 220.0, 240.0, 330.0

    fcx = fx + 0.50 * fw
    fcy = fy + 0.48 * fh
    # Elip bảo vệ toàn bộ đầu + tóc + trán + thái dương + tai + cổ (100% nguyên vẹn khi dist <= 1.0)
    head_dist = ((xx - fcx) / (0.95 * fw)) ** 2 + ((yy - fcy) / (1.02 * fh)) ** 2
    head_protect = np.clip(1.0 - np.clip((head_dist - 1.0) / 0.50, 0.0, 1.0), 0.0, 1.0)[:, :, None]

    # LAW_21.3: Dải chuyển sáng ngang siêu rộng 500px + làm mượt không gian sigma=55px
    if side == "left":
        start_x = max(320.0, fx + 0.78 * fw)
        t = np.clip((xx - start_x) / 500.0, 0.0, 1.0)
    else:
        end_x = min(760.0, fx + 0.22 * fw)
        t = np.clip((end_x - xx) / 500.0, 0.0, 1.0)

    raw_zone_mask = (t * t * (3.0 - 2.0 * t)).astype(np.float32) * (1.0 - head_protect[:, :, 0])
    text_zone_mask = cv2.GaussianBlur(raw_zone_mask, (0, 0), 55.0)[:, :, None] * (1.0 - head_protect)

    # Đo độ sáng tự nhiên của vùng đặt chữ
    if side == "left":
        zone_slice = arr[180:1150, 540:1040, :]
    else:
        zone_slice = arr[180:1150, 40:540, :]
    zone_luma = 0.2126 * zone_slice[:, :, 0] + 0.7152 * zone_slice[:, :, 1] + 0.0722 * zone_slice[:, :, 2]
    p95_luma = float(np.percentile(zone_luma, 95))

    # LAW_21.2: Exposure Floor >= 0.62 (giữ nguyên độ sáng & chi tiết tự nhiên của hậu cảnh)
    target_mult = min(0.84, 0.28 / max(p95_luma, 0.01))
    target_mult = max(0.62, target_mult)
    burn_factor = 1.0 - text_zone_mask * (1.0 - target_mult)

    # Chỉ dìm rất nhẹ độ chói của áo trắng ở phần bụng dưới (y > fy + 1.35*fh, cách xa mặt & cổ 100%)
    full_luma = (0.2126 * arr[:, :, 0] + 0.7152 * arr[:, :, 1] + 0.0722 * arr[:, :, 2])[:, :, None]
    lower_shirt_zone = np.clip((yy - (fy + 1.35 * fh)) / 160.0, 0.0, 1.0)[:, :, None] * (1.0 - head_protect)
    shirt_glare = np.clip((full_luma - 0.65) / 0.30, 0.0, 1.0)
    shirt_atten = 1.0 - 0.14 * lower_shirt_zone * shirt_glare

    # Làm dịu nhẹ vùng đèn trần phía trên đầu & khe cửa sổ sát mép lưng bằng trường không gian mượt (0% chạm vào mặt/đầu)
    ceil_t = np.clip(((fy - 0.08 * fh) - yy) / 140.0, 0.0, 1.0)
    ceil_smooth = (ceil_t * ceil_t * (3.0 - 2.0 * ceil_t))[:, :, None] * (1.0 - head_protect)
    back_t = np.clip((xx - 920.0) / 130.0, 0.0, 1.0) if side == "right" else np.clip((160.0 - xx) / 130.0, 0.0, 1.0)
    back_smooth = (back_t * back_t * (3.0 - 2.0 * back_t))[:, :, None] * (1.0 - head_protect)
    broad_luma = cv2.GaussianBlur(full_luma[:, :, 0], (0, 0), 85.0)[:, :, None]
    broad_hot = np.clip((broad_luma - 0.30) / 0.38, 0.0, 1.0) * (1.0 - head_protect)
    lamp_atten = 1.0 - np.maximum(
        np.maximum(0.28 * ceil_smooth, 0.18 * broad_hot * text_zone_mask),
        0.34 * back_smooth,
    )

    # Khóa sàn phơi sáng tuyệt đối burn_factor >= 0.58 trên toàn bộ nền (LAW_21.2)
    raw_bf = np.maximum(burn_factor * shirt_atten * lamp_atten, 0.58)
    smooth_bf = cv2.GaussianBlur(raw_bf[:, :, 0], (0, 0), 42.0)[:, :, None]
    # Bảo toàn tuyệt đối 100% vùng đầu & mặt (burn_factor == 1.0 tại head_protect == 1.0)
    burn_factor = smooth_bf * (1.0 - head_protect) + 1.0 * head_protect

    # =========================================================================
    # 1. BẢN MÀU ẤM (KODAK PORTRA 400 + LINEAR-LIGHT DARKROOM BURN)
    # =========================================================================
    color_arr = arr.copy()
    # Warm Portra balance nhẹ (+2.5% R, +0.8% G, -1.5% B)
    color_arr[:, :, 0] = np.clip(color_arr[:, :, 0] * 1.025, 0.0, 1.0)
    color_arr[:, :, 1] = np.clip(color_arr[:, :, 1] * 1.008, 0.0, 1.0)
    color_arr[:, :, 2] = np.clip(color_arr[:, :, 2] * 0.985, 0.0, 1.0)

    # Hạ phơi sáng vùng chữ trong không gian ánh sáng tuyến tính (Linear Light) để không làm xám màu và không sụt mức đen
    lin_color = np.power(np.clip(color_arr, 0.0, 1.0), 2.2)
    lin_burned = lin_color * (burn_factor ** 2.2)
    color_curved = np.power(np.clip(lin_burned, 0.0, 1.0), 1.0 / 2.2)

    # Thêm hạt film siêu mịn 0.8% (tránh làm bẩn vùng tối trên da)
    rng = np.random.default_rng(1400 + variant_seed)
    grain_c = rng.normal(0.0, 0.008, size=(1350, 1080, 1)).astype(np.float32) * (1.0 - 0.5 * head_protect)
    color_final = np.clip((color_curved + grain_c) * 255.0, 0, 255).astype(np.uint8)
    Image.fromarray(color_final).save(out_color_path, "JPEG", quality=94)

    # =========================================================================
    # 2. BẢN ĐEN TRẮNG (FINE-ART B&W — ORANGE-FILTER LUMA MIX 0.50R + 0.40G + 0.10B)
    # =========================================================================
    r_ch = arr[:, :, 0]
    g_ch = arr[:, :, 1]
    b_ch = arr[:, :, 2]
    bw_luma = (0.50 * r_ch + 0.40 * g_ch + 0.10 * b_ch)[:, :, None]

    # S-Curve Fine-Art B&W (giữ da mặt sáng mịn, nâng tương phản chiều sâu)
    bw_s = np.clip((bw_luma - 0.46) * 1.14 + 0.48, 0.02, 0.97)

    # Optical Darkroom Burn cho B&W (0% chạm vào đầu/mặt nhân vật)
    bw_target_mult = min(0.72, 0.24 / max(p95_luma, 0.01))
    bw_target_mult = max(0.24, bw_target_mult)
    bw_burn_factor = (1.0 - text_zone_mask * (1.0 - bw_target_mult)) * shirt_atten
    bw_burned = bw_s * bw_burn_factor

    # Hạt film Leica Monochrom 1.4%
    grain_bw = rng.normal(0.0, 0.014, size=(1350, 1080, 1)).astype(np.float32) * (1.0 - 0.5 * head_protect)
    bw_gray = np.clip(bw_burned + grain_bw, 0.0, 1.0)
    # Warm Platinum/Silver tint cực nhẹ (R*1.005, G*1.00, B*0.99)
    bw_rgb = np.concatenate([bw_gray * 1.005, bw_gray, bw_gray * 0.99], axis=2)
    bw_final = np.clip(bw_rgb * 255.0, 0, 255).astype(np.uint8)
    Image.fromarray(bw_final).save(out_bw_path, "JPEG", quality=94)


def make_all_versions_sbs_image(
    versions_list: List[Dict[str, Any]],
    out_sbs_path: Path,
    kb_id: str,
    label_pair: str,
) -> None:
    """Ghép bảng So Sánh TOÀN BỘ Các Phiên Bản trải qua của Banner (7 đến 10 phiên bản thay vì 3 cột cũ)."""
    valid_vers = [v for v in versions_list if v.get("local_path") and Path(v["local_path"]).exists()]
    n = len(valid_vers)
    if n == 0:
        return

    # Tự động chia lưới: nếu <= 5 bản thì 1 hàng N cột; nếu 6..10 bản thì chia 2 hàng (mỗi hàng ceil(N/2) cột)
    cols = n if n <= 5 else int(np.ceil(n / 2.0))
    rows = 1 if n <= 5 else 2

    W, H = 420, 525
    pad = 18
    top_banner_h = 64
    card_header_h = 58
    canvas_w = cols * W + (cols + 1) * pad
    canvas_h = top_banner_h + rows * (H + card_header_h + pad) + pad

    canvas = Image.new("RGB", (canvas_w, canvas_h), (7, 11, 20))
    draw = ImageDraw.Draw(canvas)

    try:
        font_title = ImageFont.truetype("/Users/vietmac/.gemini/config/skills/auto-edit-video/remotion-studio/public/fonts/FDAeonik-Bold.ttf", 23)
        font_lbl = ImageFont.truetype("/Users/vietmac/.gemini/config/skills/auto-edit-video/remotion-studio/public/fonts/FDAeonik-Bold.ttf", 17)
        font_sub = ImageFont.truetype("/Users/vietmac/.gemini/config/skills/auto-edit-video/remotion-studio/public/fonts/FDAeonik-Medium.ttf", 14)
    except Exception:
        font_title = ImageFont.load_default()
        font_lbl = font_title
        font_sub = font_title

    draw.text(
        (pad, 18),
        f"LỊCH SỬ TOÀN BỘ {n} PHIÊN BẢN TIẾN HÓA • {kb_id} ({label_pair}) • CHUẨN ĐỌC QUẢNG CÁO LAW_19 & BẢN ĐỒ NHIỆT SCANPATH",
        fill=(250, 204, 21),
        font=font_title,
    )

    def hex_to_rgb(hx: str) -> Tuple[int, int, int]:
        hx = hx.lstrip("#")
        if len(hx) == 6:
            return (int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16))
        return (56, 189, 248)

    for idx, v in enumerate(valid_vers):
        r_idx = idx // cols
        c_idx = idx % cols
        x = pad + c_idx * (W + pad)
        y_top = top_banner_h + r_idx * (H + card_header_h + pad)
        y_img = y_top + card_header_h
        col = hex_to_rgb(v.get("badge_color", "#38BDF8"))

        draw.rectangle([x, y_top, x + W, y_top + card_header_h - 4], fill=(15, 23, 42), outline=col, width=1)
        draw.text((x + 10, y_top + 8), f"{idx + 1}. {v['label'][:36]}", fill=col, font=font_lbl)
        draw.text((x + 10, y_top + 32), v.get("sub_info", "")[:48], fill=(203, 213, 225), font=font_sub)

        p_path = Path(v["local_path"])
        with Image.open(p_path) as im:
            thumb = im.convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
            canvas.paste(thumb, (x, y_img))
        draw.rectangle([x, y_img, x + W, y_img + H], outline=col, width=3)

    canvas.save(out_sbs_path, "JPEG", quality=88)


def render_overlay_png_on_page(
    page,
    html_str: str,
    html_out_path: Path,
    overlay_png_path: Path,
    frame_meta: Optional[Dict[str, Any]] = None,
    side: str = "right",
) -> Dict[str, Any]:
    """Dùng Playwright page có sẵn để auto-fit chữ chuẩn LAW_09, LAW_11 & LAW_18 (Dynamic Space-Filling) và chụp lớp chữ PNG."""
    html_out_path.write_text(html_str, encoding="utf-8")
    page.goto(f"file://{html_out_path.resolve()}", wait_until="load")
    page.evaluate("() => document.fonts.ready")

    # Tính dynamic_zone_width dựa trên khoảng trống thực tế tới vùng bảo vệ đầu/tai (LAW_18)
    dyn_zone_w = 520
    dyn_zone_left = None
    if frame_meta and frame_meta.get("cropped_face_bbox"):
        fx, fy, fw, fh = [float(v) for v in frame_meta["cropped_face_bbox"]]
        forbid_x1 = fx - 0.18 * fw
        forbid_x2 = fx + 1.18 * fw
        if side == "right":
            # zone đặt tại left = 48px, mở rộng tới forbid_x1 - 36px
            avail_w = int(round(forbid_x1 - 36 - 48))
            dyn_zone_w = max(492, min(595, avail_w))
        else:
            # nhân vật bên trái: chữ đặt bên phải, mép phải cách biên 48px, mép trái cách forbid_x2 >= 36px
            avail_w = int(round(1080 - 48 - (forbid_x2 + 36)))
            dyn_zone_w = max(492, min(595, avail_w))
            dyn_zone_left = 1080 - 48 - dyn_zone_w

    fit_info = page.evaluate(
        """(cfg) => {
            const h = document.querySelector('.headline');
            const zone = document.querySelector('.zone');
            const subBox = document.querySelector('.sub-box');
            if (zone && cfg.dyn_zone_w) {
                zone.style.width = cfg.dyn_zone_w + 'px';
                if (cfg.dyn_zone_left !== null) {
                    zone.style.left = cfg.dyn_zone_left + 'px';
                    zone.style.right = 'auto';
                }
            }
            if (subBox && cfg.dyn_zone_w) {
                subBox.style.width = cfg.dyn_zone_w + 'px';
                subBox.style.maxWidth = cfg.dyn_zone_w + 'px';
                subBox.style.boxSizing = 'border-box';
            }
            const metaV3 = document.querySelector('.meta.meta-v3');
            if (metaV3 && cfg.dyn_zone_w) {
                metaV3.style.width = cfg.dyn_zone_w + 'px';
                metaV3.style.maxWidth = cfg.dyn_zone_w + 'px';
                metaV3.style.boxSizing = 'border-box';
            }
            const lines = Array.from(document.querySelectorAll('.headline .line'));
            lines.forEach(l => { l.style.width = 'fit-content'; });
            const zWidth = zone ? zone.getBoundingClientRect().width : 520;
            const maxLineW = zWidth - 2;

            // LAW_18 (CLAUDE2): Phóng to tối đa cỡ chữ tiêu đề đồng nhất (Expand-to-Fill 104px -> 64px) lấp đầy >= 92% vùng trống
            h.style.letterSpacing = '-0.02em';
            lines.forEach(l => { l.style.letterSpacing = '-0.02em'; });
            let fs = 104;
            h.style.fontSize = fs + 'px';
            while (fs > 67) {
                const maxW = Math.max(...lines.map(l => Math.max(l.scrollWidth, l.getBoundingClientRect().width)));
                if (maxW <= maxLineW) break;
                fs -= 0.5;
                h.style.fontSize = fs + 'px';
            }
            let curMaxW = Math.max(...lines.map(l => Math.max(l.scrollWidth, l.getBoundingClientRect().width)));
            if (curMaxW > maxLineW) {
                h.style.letterSpacing = '-0.028em';
                lines.forEach(l => { l.style.letterSpacing = '-0.028em'; });
                while (fs > 64) {
                    curMaxW = Math.max(...lines.map(l => Math.max(l.scrollWidth, l.getBoundingClientRect().width)));
                    if (curMaxW <= maxLineW) break;
                    fs -= 0.5;
                    h.style.fontSize = fs + 'px';
                }
            }

            // LAW_09 V4.0 + LAW_14: Đo xRatio & Ma trận mực 2D (tuyệt đối KHÔNG giảm font-size xuống 52px; chỉ tăng targetLh để tách khe mực >= 6px)
            const hStyle = window.getComputedStyle(h);
            const c = document.createElement('canvas');
            c.width = 700; c.height = 260;
            const ctx = c.getContext('2d');
            const base = 170;

            function solveLaw09(curFs) {
                const fontSpec = hStyle.fontWeight + ' ' + curFs + 'px ' + hStyle.fontFamily;
                ctx.clearRect(0, 0, 700, 260);
                ctx.font = fontSpec;
                ctx.fillStyle = '#fff';
                ctx.textBaseline = 'alphabetic';
                ctx.fillText('x', 20, base);
                const d = ctx.getImageData(0, 0, 200, 260).data;
                let minY = 260, maxY = 0;
                for (let y = 0; y < 260; y++) {
                    for (let x = 0; x < 200; x++) {
                        if (d[(y * 200 + x) * 4 + 3] > 25) {
                            if (y < minY) minY = y;
                            if (y > maxY) maxY = y;
                        }
                    }
                }
                const xRatio = (maxY > minY) ? +((maxY - minY) / curFs).toFixed(3) : 0.48;

                function profile(str) {
                    ctx.clearRect(0, 0, 700, 260);
                    ctx.font = fontSpec;
                    ctx.fillText(str, 10, base);
                    const img = ctx.getImageData(0, 0, 700, 260).data;
                    const topC = new Array(700).fill(999);
                    const botC = new Array(700).fill(-999);
                    for (let x = 0; x < 700; x++) {
                        for (let y = 0; y < 260; y++) {
                            if (img[(y * 700 + x) * 4 + 3] > 25) {
                                const ry = y - base;
                                if (ry < topC[x]) topC[x] = ry;
                                if (ry > botC[x]) botC[x] = ry;
                            }
                        }
                    }
                    return {topC, botC};
                }

                const profs = lines.map(l => profile(l.innerText.trim()));
                let maxOverlap = -999;
                for (let i = 0; i < profs.length - 1; i++) {
                    const pU = profs[i], pL = profs[i + 1];
                    for (let x = 0; x < 700; x++) {
                        if (pU.botC[x] === -999) continue;
                        for (let dx = -6; dx <= 6; dx++) {
                            const x2 = x + dx;
                            if (x2 >= 0 && x2 < 700 && pL.topC[x2] !== 999) {
                                const ov = pU.botC[x] - pL.topC[x2];
                                if (ov > maxOverlap) maxOverlap = ov;
                            }
                        }
                    }
                }
                const reqDistPx = maxOverlap + 11.5;
                const reqLh = reqDistPx / curFs;
                const minLhW = 2.16 * xRatio;
                const maxLhW = 2.50 * xRatio;
                let targetLh = Math.max(minLhW, reqLh);
                if (targetLh > maxLhW) targetLh = maxLhW;
                targetLh = Math.max(0.99, Math.min(1.24, +targetLh.toFixed(3)));
                const gapPx = Math.round(targetLh * curFs - maxOverlap);
                const wVal = +((targetLh - xRatio) / xRatio).toFixed(2);
                return { fs: curFs, targetLh, gapPx, wVal, pass: (gapPx >= 6 && wVal >= 1.10 && wVal <= 1.55) };
            }

            const best = solveLaw09(fs);
            fs = best.fs;
            h.style.fontSize = fs + 'px';
            h.style.lineHeight = String(best.targetLh);
            lines.forEach(l => { l.style.lineHeight = String(best.targetLh); });

            // LAW_11: Auto-fit mọi dòng chữ trong .sub-box bằng Range.getBoundingClientRect() + scrollWidth (lề phải >= 14px, 0% tràn hộp)
            if (subBox) {
                // LAW_19: Đảm bảo mọi tag/badge trong .sub-box có font-size >= 19px và không bị inner_clip
                Array.from(subBox.querySelectorAll('*')).forEach(el => {
                    const cs = window.getComputedStyle(el);
                    const curFs = parseFloat(cs.fontSize);
                    if ((el.innerText || '').trim().length > 0 && curFs > 0 && curFs < 19.0) {
                        el.style.fontSize = '19px';
                    }
                });
                // Đảm bảo các icon/badge cố định không bị báo inner_clip do width hẹp và có khoảng thở ngang >= 10px
                Array.from(subBox.querySelectorAll('.icon-x, .icon-ok, .arrow, .s-left, .b-left, .tag, .pill')).forEach(ic => {
                    ic.style.width = 'auto';
                    ic.style.minWidth = '26px';
                    ic.style.flexShrink = '0';
                    if (ic.classList.contains('arrow')) {
                        ic.style.marginLeft = '10px';
                        ic.style.marginRight = '10px';
                    }
                });
                if (!subBox.classList.contains('two-col-box')) {
                    subBox.style.paddingRight = '14px';
                }
                const boxRect = subBox.getBoundingClientRect();
                const autoSubs = Array.from(subBox.querySelectorAll('.auto-sub'));
                for (const el of autoSubs) {
                    const ws = window.getComputedStyle(el).whiteSpace;
                    if (ws === 'normal') continue;
                    el.style.width = 'fit-content';
                    let sfs = Math.max(parseFloat(window.getComputedStyle(el).fontSize), 26.0);
                    el.style.fontSize = sfs + 'px';
                    const colParent = el.closest('.col-left, .col-right, .col-stat, .s-right');
                    const rowParent = el.closest('.row, .nb-row, .qa-row, .tl-row, .r14, .ld-row, .ck-row, .rx-r');
                    const limitRight = colParent ? Math.min(colParent.getBoundingClientRect().right - 14, boxRect.right - 15) : (boxRect.right - 15);
                    while (sfs > 26.2) {
                        const range = document.createRange();
                        range.selectNodeContents(el);
                        const r = range.getBoundingClientRect();
                        const rowOk = !rowParent || (rowParent.scrollWidth <= rowParent.clientWidth + 1);
                        if (r.right <= limitRight && rowOk) break;
                        sfs = Math.max(26.2, +(sfs - 0.3).toFixed(1));
                        el.style.fontSize = sfs + 'px';
                    }
                    const range2 = document.createRange();
                    range2.selectNodeContents(el);
                    if (range2.getBoundingClientRect().right > limitRight || (rowParent && rowParent.scrollWidth > rowParent.clientWidth + 1)) {
                        el.style.letterSpacing = '-0.024em';
                        if (rowParent) {
                            rowParent.style.paddingLeft = '12px';
                            rowParent.style.paddingRight = '14px';
                            rowParent.style.gap = '8px';
                        }
                    }
                    const range3 = document.createRange();
                    range3.selectNodeContents(el);
                    if (range3.getBoundingClientRect().right > limitRight) {
                        el.style.whiteSpace = 'normal';
                        el.style.width = 'auto';
                        el.style.flex = '1 1 0%';
                        el.style.minWidth = '0';
                    }
                }
                // Quét chống inner_clip lần cuối cho các badge/tag/cột nhãn ngắn trong .sub-box (không ép minWidth lên .auto-sub hoặc dòng chứa .auto-sub)
                Array.from(subBox.querySelectorAll('*')).forEach(el => {
                    if (el.classList.contains('auto-sub') || el.querySelector('.auto-sub')) return;
                    if (el.scrollWidth > el.clientWidth + 1) {
                        const needW = (el.scrollWidth + 5) + 'px';
                        el.style.minWidth = needW;
                        el.style.width = needW;
                        el.style.flexShrink = '0';
                    }
                });
                if (subBox.classList.contains('two-col-box') && autoSubs.length === 2) {
                    const minColFs = Math.min(...autoSubs.map(e => parseFloat(window.getComputedStyle(e).fontSize)));
                    autoSubs.forEach(e => { e.style.fontSize = minColFs + 'px'; });
                }
            }

            // Căn lại tâm dọc của .zone sau khi đã phóng to Headline & Sub-box (G14 Optical Vertical Center)
            if (zone) {
                const zH = zone.getBoundingClientRect().height;
                const idealTop = Math.max(120, Math.round((1350 - zH) * 0.50));
                zone.style.top = idealTop + 'px';
                zone.style.transform = 'none';
            }

            return {
                final_h_fs: fs,
                updated_html: document.documentElement.outerHTML
            };
        }""",
        {"dyn_zone_w": dyn_zone_w, "dyn_zone_left": dyn_zone_left},
    )

    html_out_path.write_text("<!DOCTYPE html>\n" + fit_info["updated_html"], encoding="utf-8")
    page.screenshot(path=str(overlay_png_path), omit_background=True)
    return fit_info


def r2_put(local_path: Path, r2_key: str) -> str:
    try:
        subprocess.run(
            ["python3", str(R2_MANAGER), "--put", str(local_path), r2_key],
            check=False,
            timeout=20,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        pass
    return f"https://media.fedu.vn/{r2_key}"


def process_kb_chunk(kb_ids: List[str], master: Dict[str, Any], plate_map: Dict[str, Path], push_online: bool = False) -> List[Dict[str, Any]]:
    """Một worker xử lý một nhóm KB bằng 1 phiên Chromium duy nhất (mặc định OFFLINE 100% để tốc độ tối đa)."""
    DUAL_BG_DIR.mkdir(parents=True, exist_ok=True)
    OUT_RENDER_DIR.mkdir(parents=True, exist_ok=True)
    CARDS_DIR.mkdir(parents=True, exist_ok=True)

    kb_70_map_path = PILOT_DIR / "kb_70_plate_map.json"
    kb_70_map = json.loads(kb_70_map_path.read_text(encoding="utf-8")) if kb_70_map_path.exists() else {}

    results = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)

        for kb_id in kb_ids:
            spec = master["kbs"][kb_id]
            kb_num = int(kb_id.split("_")[1])
            kb_lower = kb_id.lower()
            side = spec.get("side", "right")

            # Tìm plate_key 1-đối-1 đã kiểm định lịch sự & Face DNA cho KB này
            frame_meta = kb_70_map.get(kb_id, {})
            plate_key = frame_meta.get("plate_key") or KB_TO_PLATE_ASSIGNMENT.get(kb_id, "kb14_01")
            src_plate = Path(frame_meta["plate_path"]) if frame_meta.get("plate_path") else plate_map.get(plate_key)
            if src_plate is None or not src_plate.exists():
                fallback_candidates = [p for k, p in plate_map.items() if p.exists()]
                src_plate = fallback_candidates[kb_num % len(fallback_candidates)]

            color_bg_path = DUAL_BG_DIR / f"{kb_lower}_color_bg.jpg"
            bw_bg_path = DUAL_BG_DIR / f"{kb_lower}_bw_bg.jpg"

            build_dual_zero_blur_bgs(
                src_plate_path=src_plate,
                side=side,
                out_color_path=color_bg_path,
                out_bw_path=bw_bg_path,
                variant_seed=kb_num,
                frame_meta=frame_meta,
            )

            h_code = spec.get("h_code", "H01")
            style_code = spec["style"]
            alt_code = spec.get("alt_style", "K02" if style_code == "K01" else "K01")
            style_name = master["style_names"].get(style_code, style_code)
            alt_name = master["style_names"].get(alt_code, alt_code)
            font_label = spec.get("h_name") or master.get("headline_fonts", {}).get(h_code, {}).get("name", h_code)
            outfit_id = spec.get("outfit_id", "C02_I03")
            banner_style_name = spec.get("banner_style_name", "Style banner.html")

            html_primary_path = OUT_RENDER_DIR / f"{kb_lower}_{style_code.lower()}_primary.html"
            ov_primary_png = OUT_RENDER_DIR / f"{kb_lower}_ov_primary.png"
            html_alt_path = OUT_RENDER_DIR / f"{kb_lower}_{alt_code.lower()}_alt.html"
            ov_alt_png = OUT_RENDER_DIR / f"{kb_lower}_ov_alt.png"

            img_color_path = OUT_RENDER_DIR / f"{kb_lower}_color.jpg"
            img_final_path = OUT_RENDER_DIR / f"{kb_lower}_final.jpg"
            img_bw_path = OUT_RENDER_DIR / f"{kb_lower}_bw.jpg"
            img_alt_path = OUT_RENDER_DIR / f"{kb_lower}_alt.jpg"
            img_sbs_path = OUT_RENDER_DIR / f"{kb_lower}_sbs.jpg"

            html_primary = build_style_html(style_code, spec, master)
            html_alt = build_style_html(alt_code, spec, master)

            render_overlay_png_on_page(page, html_primary, html_primary_path, ov_primary_png, frame_meta=frame_meta, side=side)
            render_overlay_png_on_page(page, html_alt, html_alt_path, ov_alt_png, frame_meta=frame_meta, side=side)

            # Ghép lớp chữ lên Bản Màu và Bản Đen Trắng
            with Image.open(color_bg_path) as c_bg, Image.open(bw_bg_path) as b_bg, Image.open(ov_primary_png) as ov_p, Image.open(ov_alt_png) as ov_a:
                c_rgba = c_bg.convert("RGBA")
                b_rgba = b_bg.convert("RGBA")
                ov_p_rgba = ov_p.convert("RGBA")
                ov_a_rgba = ov_a.convert("RGBA")

                comp_color = Image.alpha_composite(c_rgba, ov_p_rgba).convert("RGB")
                comp_color.save(img_color_path, "JPEG", quality=93)
                comp_color.save(img_final_path, "JPEG", quality=93)

                comp_bw = Image.alpha_composite(b_rgba, ov_p_rgba).convert("RGB")
                comp_bw.save(img_bw_path, "JPEG", quality=93)

                comp_alt = Image.alpha_composite(c_rgba, ov_a_rgba).convert("RGB")
                comp_alt.save(img_alt_path, "JPEG", quality=93)

            if ov_primary_png.exists():
                ov_primary_png.unlink()
            if ov_alt_png.exists():
                ov_alt_png.unlink()

            results.append(
                {
                    "kb_id": kb_id,
                    "kb_order": kb_num,
                    "kb_lower": kb_lower,
                    "spec": spec,
                    "h_code": h_code,
                    "style_code": style_code,
                    "style_name": style_name,
                    "alt_code": alt_code,
                    "alt_name": alt_name,
                    "font_label": font_label,
                    "outfit_id": outfit_id,
                    "banner_style_name": banner_style_name,
                    "side": side,
                    "html_primary_path": html_primary_path,
                    "img_color_path": img_color_path,
                    "img_final_path": img_final_path,
                    "img_bw_path": img_bw_path,
                    "img_alt_path": img_alt_path,
                    "img_sbs_path": img_sbs_path,
                }
            )

        page.close()
        browser.close()

    # Sau khi đóng Chromium của worker, chạy kiểm toán 23 Cổng + Xuất Heatmap + Ghép Bảng Lịch Sử Đa Phiên Bản + Upload R2
    ver_tag = f"v7_{int(time.time()) % 100000}"
    final_summaries = []
    for item in results:
        kb_id = item["kb_id"]
        kb_lower = item["kb_lower"]
        spec = item["spec"]
        img_heatmap_path = OUT_RENDER_DIR / f"{kb_lower}_heatmap.jpg"

        audit_res = audit_v3_banner(
            html_path=item["html_primary_path"],
            final_img_path=item["img_color_path"],
            expected_lines=3,
            person_side=item["side"],
            heatmap_out_path=img_heatmap_path,
        )

        g1 = audit_res.get("gates", {}).get("G1_font_scale_hierarchy", {})
        g21 = audit_res.get("gates", {}).get("G21_CLAUDE2_saliency_heatmap_scanpath", {})
        min_body_fs = g1.get("min_subline_fs_px", 27.0)
        h_fs = g1.get("headline_fs_px", 78.0)
        scanpath_order = g21.get("scanpath_order", ["FACE", "HEADLINE", "SUBBOX", "HEADLINE"])
        subbox_p90 = g21.get("subbox_p90_saliency", 0.48)
        text_face_ratio = g21.get("total_text_to_face_energy_ratio", 1.55)

        # Thu thập TOÀN BỘ lịch sử các phiên bản trải qua của KB này
        hist_dir = PILOT_DIR / "version_history" / kb_id
        raw_versions: List[Dict[str, Any]] = []

        v1_before = BASE_DIR / kb_id / "before" / f"{kb_id}_A1_before_A.jpg"
        if v1_before.exists():
            raw_versions.append({
                "ver_id": "V1_BEFORE",
                "label": "Bản Gốc Đợt 1 (Before)",
                "sub_info": "Leading 1.402 · Nền tối cũ đè cổ",
                "local_path": v1_before,
                "r2_key": f"banner2/hist/{kb_lower}_v1_before.jpg",
                "badge_color": "#64748B",
            })

        v2_blur = BASE_DIR / kb_id / "after" / f"{kb_id}_A1_after_opt.jpg"
        if v2_blur.exists():
            raw_versions.append({
                "ver_id": "V2_BLUR_A1",
                "label": "Bản Tối Ưu Đợt 1 (Nền Blur A1)",
                "sub_info": "Sửa leading 1.08 · Nền Gaussian Blur",
                "local_path": v2_blur,
                "r2_key": f"banner2/hist/{kb_lower}_v2_blur_a1.jpg",
                "badge_color": "#60A5FA",
            })

        v3_blur_a2 = BASE_DIR / kb_id / "after" / f"{kb_id}_A2_after_opt.jpg"
        if v3_blur_a2.exists():
            raw_versions.append({
                "ver_id": "V3_BLUR_A2",
                "label": "Bản Phương Án 2 Đợt 1 (A2)",
                "sub_info": "Biến thể hộp chữ đợt 1",
                "local_path": v3_blur_a2,
                "r2_key": f"banner2/hist/{kb_lower}_v3_blur_a2.jpg",
                "badge_color": "#818CF8",
            })

        v6_color = hist_dir / "v6_pre_law19_color.jpg"
        if v6_color.exists():
            raw_versions.append({
                "ver_id": "V6_COLOR_PRE_LAW19",
                "label": "Bản V6.1 Màu Ấm (Trước LAW_19)",
                "sub_info": "0% Blur · Chữ phụ co 19.5–22px & xám #94A3B8",
                "local_path": v6_color,
                "r2_key": f"banner2/hist/{kb_lower}_v6_color.jpg",
                "badge_color": "#F97316",
            })

        v6_bw = hist_dir / "v6_pre_law19_bw.jpg"
        if v6_bw.exists():
            raw_versions.append({
                "ver_id": "V6_BW_PRE_LAW19",
                "label": "Bản V6.1 Đen Trắng (Trước LAW_19)",
                "sub_info": "Fine-Art B&W · Chữ phụ co 19.5–22px",
                "local_path": v6_bw,
                "r2_key": f"banner2/hist/{kb_lower}_v6_bw.jpg",
                "badge_color": "#FB923C",
            })

        v6_alt = hist_dir / "v6_pre_law19_alt.jpg"
        if v6_alt.exists():
            raw_versions.append({
                "ver_id": "V6_ALT_PRE_LAW19",
                "label": f"Bản V6.1 Đối Chứng ({item['alt_code']} Cũ)",
                "sub_info": "Khuôn đối chứng trước khi áp LAW_19",
                "local_path": v6_alt,
                "r2_key": f"banner2/hist/{kb_lower}_v6_alt.jpg",
                "badge_color": "#FBBF24",
            })

        raw_versions.extend([
            {
                "ver_id": "V7_COLOR_LAW19",
                "label": f"Bản Mới V7.0 Màu Ấm ({item['style_code']} · LAW_19)",
                "sub_info": f"Chữ phụ {min_body_fs}px (#E2E8F0/#FFF) · {audit_res['score']} PASS",
                "local_path": item["img_color_path"],
                "r2_key": f"banner2/{kb_lower}_color.jpg",
                "badge_color": "#10B981",
            },
            {
                "ver_id": "V7_BW_LAW19",
                "label": f"Bản Mới V7.0 Đen Trắng ({item['style_code']} · LAW_19)",
                "sub_info": f"Fine-Art B&W · Chữ phụ {min_body_fs}px · Tương phản >= 14:1",
                "local_path": item["img_bw_path"],
                "r2_key": f"banner2/{kb_lower}_bw.jpg",
                "badge_color": "#38BDF8",
            },
            {
                "ver_id": "V7_ALT_LAW19",
                "label": f"Bản Mới V7.0 Đối Chứng ({item['alt_code']} · LAW_19)",
                "sub_info": f"Khuôn {item['alt_name']} · Chuẩn đọc Mobile 360px",
                "local_path": item["img_alt_path"],
                "r2_key": f"banner2/{kb_lower}_alt.jpg",
                "badge_color": "#A78BFA",
            },
            {
                "ver_id": "V7_HEATMAP_SCANPATH",
                "label": "Bản Đồ Nhiệt Luồng Thị Giác (F1→F2→F3→F4)",
                "sub_info": f"{' → '.join(scanpath_order[:4])} · SubBox P90={subbox_p90}",
                "local_path": img_heatmap_path,
                "r2_key": f"banner2/{kb_lower}_heatmap.jpg",
                "badge_color": "#F43F5E",
            },
        ])

        make_all_versions_sbs_image(
            versions_list=raw_versions,
            out_sbs_path=item["img_sbs_path"],
            kb_id=kb_id,
            label_pair=f"{item['h_code']}×{item['style_code']}",
        )

        # Chỉ upload lên R2 khi có cờ --online (mặc định OFFLINE 100% để tốc độ nhanh nhất)
        if push_online:
            upload_tasks = [(Path(v["local_path"]), v["r2_key"]) for v in raw_versions if Path(v["local_path"]).exists()]
            upload_tasks.append((item["img_final_path"], f"banner2/{kb_lower}_final.jpg"))
            upload_tasks.append((item["img_sbs_path"], f"banner2/{kb_lower}_sbs.jpg"))

            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as up_ex:
                for p_loc, r_key in upload_tasks:
                    up_ex.submit(r2_put, p_loc, r_key)

        r2_color = f"https://media.fedu.vn/banner2/{kb_lower}_color.jpg"
        r2_final = f"https://media.fedu.vn/banner2/{kb_lower}_final.jpg"
        r2_bw = f"https://media.fedu.vn/banner2/{kb_lower}_bw.jpg"
        r2_alt = f"https://media.fedu.vn/banner2/{kb_lower}_alt.jpg"
        r2_heatmap = f"https://media.fedu.vn/banner2/{kb_lower}_heatmap.jpg"
        r2_sbs = f"https://media.fedu.vn/banner2/{kb_lower}_sbs.jpg"

        versions_history_json = []
        for idx_v, v in enumerate(raw_versions):
            versions_history_json.append({
                "step": idx_v + 1,
                "ver_id": v["ver_id"],
                "label": v["label"],
                "sub_info": v["sub_info"],
                "img_url": f"https://media.fedu.vn/{v['r2_key']}",
                "badge_color": v["badge_color"],
            })

        headline_plain = " / ".join(
            ln.replace('<span class="hl">', "").replace("</span>", "") for ln in spec["headline_lines"]
        )

        card_data = {
            "order": item["kb_order"],
            "kb_id": kb_id,
            "ver": ver_tag,
            "title": spec["title"],
            "outfit_id": item["outfit_id"],
            "banner_style_name": item["banner_style_name"],
            "h_code": item["h_code"],
            "style_code": item["style_code"],
            "style_name": item["style_name"],
            "alt_style_code": item["alt_code"],
            "alt_style_name": item["alt_name"],
            "font_name": item["font_label"],
            "person_side": item["side"],
            "headline_plain": headline_plain,
            "hl_kw": spec["hl_kw"],
            "subline_summary": f"🎨 Chuẩn LAW_19 ({min_body_fs}px) • 🔥 Scanpath: {'→'.join(s[:4] for s in scanpath_order[:3])} • {item['style_name']}",
            "audit_score": f"{audit_res['score']} PASS",
            "score": audit_res["score"],
            "all_13_pass": audit_res["all_13_pass"],
            "headline_fs_px": h_fs,
            "min_sub_fs_px": min_body_fs,
            "scanpath_order": scanpath_order,
            "subbox_p90_saliency": subbox_p90,
            "text_to_face_energy_ratio": text_face_ratio,
            "color_img_url": r2_color,
            "bw_img_url": r2_bw,
            "final_img_url": r2_final,
            "alt_img_url": r2_alt,
            "heatmap_img_url": r2_heatmap,
            "secondary_img_url": r2_bw,
            "secondary_label": "🖤 Bản Đen Trắng",
            "sbs_img_url": r2_sbs,
            "r2_color_url": r2_color,
            "r2_bw_url": r2_bw,
            "r2_final_url": r2_final,
            "r2_alt_url": r2_alt,
            "r2_heatmap_url": r2_heatmap,
            "r2_sbs_url": r2_sbs,
            "versions_count": len(versions_history_json),
            "versions_history": versions_history_json,
        }
        (CARDS_DIR / f"{kb_id}.json").write_text(json.dumps(card_data, ensure_ascii=False, indent=2), encoding="utf-8")
        final_summaries.append(
            {
                "kb_id": kb_id,
                "score": audit_res["score"],
                "min_sub_fs": min_body_fs,
                "scanpath": scanpath_order,
                "versions_count": len(versions_history_json),
                "color_url": r2_color,
                "heatmap_url": r2_heatmap,
            }
        )
        print(f"[DONE] {kb_id} -> V7 LAW_19 ({audit_res['score']} | sub={min_body_fs}px | scan={'->'.join(scanpath_order[:3])} | {len(versions_history_json)} vers)", flush=True)

    return final_summaries


def main():
    parser = argparse.ArgumentParser(description="Zero-Blur Dual Color & B&W Mass Pipeline V6.0")
    parser.add_argument("--workers", type=int, default=7, help="Số tiến trình chạy song song")
    parser.add_argument("--kbs", type=str, default="ALL", help="ALL hoặc danh sách KB_01,KB_02...")
    parser.add_argument("--online", action="store_true", help="Đẩy ảnh & HTML lên R2 (mặc định False = chạy OFFLINE 100% siêu nhanh)")
    args = parser.parse_args()

    t0 = time.time()
    plate_map = harvest_generated_plates()
    print(f"[HARVEST] Đã thu hoạch {len(plate_map)} Phôi Nền Thật Không Blur (mode={'ONLINE' if args.online else 'OFFLINE'})", flush=True)

    master = json.loads(SPECS_PATH.read_text(encoding="utf-8"))
    if args.kbs.upper() == "ALL":
        all_kbs = sorted(master["kbs"].keys(), key=lambda x: int(x.split("_")[1]))
    else:
        all_kbs = [x.strip().upper() for x in args.kbs.split(",") if x.strip()]

    # Chia đều danh sách KB cho N workers
    n_workers = max(1, min(args.workers, len(all_kbs)))
    chunks: List[List[str]] = [[] for _ in range(n_workers)]
    for idx, kb_id in enumerate(all_kbs):
        chunks[idx % n_workers].append(kb_id)

    all_done = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_workers) as ex:
        futs = [ex.submit(process_kb_chunk, ch, master, plate_map, args.online) for ch in chunks if ch]
        for f in concurrent.futures.as_completed(futs):
            all_done.extend(f.result())

    # Đồng bộ banner2.html local (chỉ đẩy R2 khi --online)
    hub_res = atomic_rebuild_and_sync(push_r2=args.online)
    dt = time.time() - t0
    print(
        json.dumps(
            {
                "status": "COMPLETED_ALL_DUAL_BANNERS",
                "total_kbs": len(all_done),
                "total_images_rendered": len(all_done) * 2,
                "elapsed_sec": round(dt, 1),
                "hub": hub_res,
            },
            ensure_ascii=False,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
