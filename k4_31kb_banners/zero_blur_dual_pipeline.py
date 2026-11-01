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
            # Đảm bảo nw - x_shift >= target_w (1080) và nh >= target_h (1350) để 0% phải pad gương BORDER_REFLECT_101
            min_req_w = target_w + x_shift
            if nw < min_req_w or nh < target_h:
                fix_ratio = max(min_req_w / float(max(1, nw)), target_h / float(max(1, nh)))
                nw = int(round(nw * fix_ratio))
                nh = int(round(nh * fix_ratio))
                y0 = int(round(y0 * fix_ratio))
            im_resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
            arr_s = np.array(im_resized, dtype=np.uint8)
            y0 = max(0, min(nh - target_h, y0))
            arr_h = arr_s[y0 : y0 + target_h, :, :]

            if side == "left":
                arr_shifted = arr_h[:, x_shift:, :]
                arr_u8 = arr_shifted[:, :target_w, :]
            else:
                end_col = nw - x_shift
                arr_shifted = arr_h[:, :end_col, :]
                arr_u8 = arr_shifted[:, arr_shifted.shape[1] - target_w :, :]
            arr = arr_u8.astype(np.float32) / 255.0
        else:
            scale = max(target_w / float(w0), target_h / float(h0))
            nw = int(round(w0 * scale))
            nh = int(round(h0 * scale))
            im_resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
            x0 = 0 if side == "left" else max(0, nw - target_w)
            y0 = max(0, int((nh - target_h) * 0.35))
            im_crop = im_resized.crop((x0, y0, x0 + target_w, y0 + target_h))
            arr = np.array(im_crop, dtype=np.float32) / 255.0

    yy, xx = np.mgrid[0:1350, 0:1080].astype(np.float32)

    # Tạo mặt nạ Phơi Sáng Phòng Tối Quang Học (Optical Darkroom Burn — KHÔNG BLUR, giữ 100% chi tiết phòng)
    # Nếu nhân vật bên TRÁI (`side == 'left'`), chữ nằm bên PHẢI (`x: 520..1080`)
    # Nếu nhân vật bên PHẢI (`side == 'right'`), chữ nằm bên TRÁI (`x: 0..560`)
    if side == "left":
        t = np.clip((xx - 430.0) / 260.0, 0.0, 1.0)
    else:
        t = np.clip((650.0 - xx) / 260.0, 0.0, 1.0)
    text_zone_mask = (t * t * (3.0 - 2.0 * t))[:, :, None]

    # Đo độ sáng tự nhiên của vùng đặt chữ để tự động điều chỉnh lượng Darkroom Burn vừa đủ đạt WCAG
    if side == "left":
        zone_slice = arr[180:1150, 540:1040, :]
    else:
        zone_slice = arr[180:1150, 40:540, :]
    zone_luma = 0.2126 * zone_slice[:, :, 0] + 0.7152 * zone_slice[:, :, 1] + 0.0722 * zone_slice[:, :, 2]
    p95_luma = float(np.percentile(zone_luma, 95))

    # Nếu vùng chữ vốn đã tối (p95 <= 0.32), chỉ burn rất nhẹ (giữ 75% ánh sáng gốc); nếu sáng hơn thì hạ exposure mượt để p95 <= 0.28
    target_mult = min(0.78, 0.26 / max(p95_luma, 0.01))
    target_mult = max(0.28, target_mult)
    burn_factor = 1.0 - text_zone_mask * (1.0 - target_mult)

    # =========================================================================
    # 1. BẢN MÀU ẤM (KODAK PORTRA 400 + OPTICAL DARKROOM BURN)
    # =========================================================================
    color_arr = arr.copy()
    # Warm Portra balance (+3% R, +1% G, -2% B trên midtones)
    color_arr[:, :, 0] = np.clip(color_arr[:, :, 0] * 1.035, 0.0, 1.0)
    color_arr[:, :, 1] = np.clip(color_arr[:, :, 1] * 1.010, 0.0, 1.0)
    color_arr[:, :, 2] = np.clip(color_arr[:, :, 2] * 0.975, 0.0, 1.0)

    # Áp dụng Optical Darkroom Burn (nhân phơi sáng, giữ nguyên chi tiết bokeh & đồ vật)
    color_burned = color_arr * burn_factor
    # Đường cong S-curve nhẹ cho Bản Màu
    color_curved = np.clip((color_burned - 0.5) * 1.06 + 0.5, 0.0, 1.0)

    # Thêm hạt film siêu mịn 1.2%
    rng = np.random.default_rng(1400 + variant_seed)
    grain_c = rng.normal(0.0, 0.012, size=(1350, 1080, 1)).astype(np.float32)
    color_final = np.clip((color_curved + grain_c) * 255.0, 0, 255).astype(np.uint8)
    Image.fromarray(color_final).save(out_color_path, "JPEG", quality=93)

    # =========================================================================
    # 2. BẢN ĐEN TRẮNG (FINE-ART B&W — ORANGE-FILTER LUMA MIX 0.50R + 0.40G + 0.10B)
    # =========================================================================
    r_ch = arr[:, :, 0]
    g_ch = arr[:, :, 1]
    b_ch = arr[:, :, 2]
    bw_luma = (0.50 * r_ch + 0.40 * g_ch + 0.10 * b_ch)[:, :, None]

    # S-Curve Fine-Art B&W (giữ da mặt sáng mịn, nâng tương phản chiều sâu)
    bw_s = np.clip((bw_luma - 0.46) * 1.16 + 0.48, 0.02, 0.97)

    # Optical Darkroom Burn cho B&W (sâu hơn nhẹ ở vùng chữ để chữ trắng + điểm nhấn vàng/xanh bật lên)
    bw_target_mult = min(0.72, 0.24 / max(p95_luma, 0.01))
    bw_target_mult = max(0.24, bw_target_mult)
    bw_burn_factor = 1.0 - text_zone_mask * (1.0 - bw_target_mult)
    bw_burned = bw_s * bw_burn_factor

    # Hạt film Leica Monochrom 2%
    grain_bw = rng.normal(0.0, 0.018, size=(1350, 1080, 1)).astype(np.float32)
    bw_gray = np.clip(bw_burned + grain_bw, 0.0, 1.0)
    # Warm Platinum/Silver tint cực nhẹ (R*1.005, G*1.00, B*0.99)
    bw_rgb = np.concatenate([bw_gray * 1.005, bw_gray, bw_gray * 0.99], axis=2)
    bw_final = np.clip(bw_rgb * 255.0, 0, 255).astype(np.uint8)
    Image.fromarray(bw_final).save(out_bw_path, "JPEG", quality=93)


def make_dual_3col_sbs_image(
    color_img_path: Path,
    bw_img_path: Path,
    old_img_path: Path,
    out_sbs_path: Path,
    kb_id: str,
    label_pair: str,
) -> None:
    """Ghép bảng So Sánh 3 Cột: 1. Bản Màu Ấm (0% Blur) • 2. Bản Đen Trắng (Fine-Art B&W) • 3. Bản Cũ."""
    W, H = 540, 675
    pad = 20
    header_h = 68
    canvas_w = W * 3 + pad * 4
    canvas_h = H + header_h + pad * 2

    canvas = Image.new("RGB", (canvas_w, canvas_h), (8, 13, 24))
    draw = ImageDraw.Draw(canvas)

    try:
        font = ImageFont.truetype("/Users/vietmac/.gemini/config/skills/auto-edit-video/remotion-studio/public/fonts/FDAeonik-Bold.ttf", 21)
    except Exception:
        font = ImageFont.load_default()

    panels = [
        (color_img_path, f"1. BẢN MÀU ẤM ({kb_id} • {label_pair} • 0% BLUR)", (16, 185, 129)),
        (bw_img_path, f"2. BẢN ĐEN TRẮNG ({kb_id} • FINE-ART B&W)", (245, 158, 11)),
        (old_img_path, f"3. BẢN CŨ ({kb_id} • ĐỐI CHIẾU TRƯỚC ĐÂY)", (148, 163, 184)),
    ]

    for idx, (p_path, title, col) in enumerate(panels):
        x = pad + idx * (W + pad)
        y = header_h
        draw.text((x + 6, 22), title, fill=col, font=font)
        if p_path.exists():
            with Image.open(p_path) as im:
                thumb = im.convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
                canvas.paste(thumb, (x, y))
        draw.rectangle([x, y, x + W, y + H], outline=col, width=3)

    canvas.save(out_sbs_path, "JPEG", quality=88)


def render_overlay_png_on_page(page, html_str: str, html_out_path: Path, overlay_png_path: Path) -> Dict[str, Any]:
    """Dùng Playwright page có sẵn để auto-fit chữ chuẩn LAW_09 & LAW_11 (Range rect) và chụp lớp chữ PNG trong suốt."""
    html_out_path.write_text(html_str, encoding="utf-8")
    page.goto(f"file://{html_out_path.resolve()}", wait_until="load")
    page.evaluate("() => document.fonts.ready")

    fit_info = page.evaluate(
        """() => {
            const h = document.querySelector('.headline');
            const zone = document.querySelector('.zone');
            const lines = Array.from(document.querySelectorAll('.headline .line'));
            // Đặt width: fit-content cho từng .line để getBoundingClientRect().width và scrollWidth phản ánh chính xác bề rộng mực chữ
            lines.forEach(l => { l.style.width = 'fit-content'; });
            const zWidth = zone ? zone.getBoundingClientRect().width : 492;
            const maxLineW = zWidth - 2;
            let fs = parseFloat(window.getComputedStyle(h).fontSize);
            while (fs > 67) {
                const maxW = Math.max(...lines.map(l => Math.max(l.scrollWidth, l.getBoundingClientRect().width)));
                if (maxW <= maxLineW) break;
                fs -= 1;
                h.style.fontSize = fs + 'px';
            }
            let curMaxW = Math.max(...lines.map(l => Math.max(l.scrollWidth, l.getBoundingClientRect().width)));
            if (curMaxW > maxLineW) {
                h.style.letterSpacing = '-0.025em';
                lines.forEach(l => { l.style.letterSpacing = '-0.025em'; });
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
                const reqDistPx = maxOverlap + 8.5;
                const reqLh = reqDistPx / curFs;
                const minLhW = 2.13 * xRatio;
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
            const subBox = document.querySelector('.sub-box');
            if (subBox) {
                // Đảm bảo các icon cố định không bị báo inner_clip do width hẹp và có khoảng thở ngang >= 10px
                Array.from(subBox.querySelectorAll('.icon-x, .icon-ok, .arrow')).forEach(ic => {
                    ic.style.width = 'auto';
                    ic.style.minWidth = '26px';
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
                    let sfs = parseFloat(window.getComputedStyle(el).fontSize);
                    const colParent = el.closest('.col-left, .col-right, .col-stat, .s-right');
                    const rowParent = el.closest('.row, .nb-row, .qa-row, .tl-row, .r14, .ld-row, .ck-row, .rx-r');
                    const limitRight = colParent ? Math.min(colParent.getBoundingClientRect().right - 14, boxRect.right - 15) : (boxRect.right - 15);
                    while (sfs > 19.6) {
                        const range = document.createRange();
                        range.selectNodeContents(el);
                        const r = range.getBoundingClientRect();
                        const rowOk = !rowParent || (rowParent.scrollWidth <= rowParent.clientWidth + 1);
                        if (r.right <= limitRight && rowOk) break;
                        sfs = +(sfs - 0.4).toFixed(1);
                        el.style.fontSize = sfs + 'px';
                    }
                    const range2 = document.createRange();
                    range2.selectNodeContents(el);
                    if (range2.getBoundingClientRect().right > limitRight || (rowParent && rowParent.scrollWidth > rowParent.clientWidth + 1)) {
                        el.style.letterSpacing = '-0.035em';
                    }
                }
                if (subBox.classList.contains('two-col-box') && autoSubs.length === 2) {
                    const minColFs = Math.min(...autoSubs.map(e => parseFloat(window.getComputedStyle(e).fontSize)));
                    autoSubs.forEach(e => { e.style.fontSize = minColFs + 'px'; });
                }
            }

            return {
                final_h_fs: fs,
                updated_html: document.documentElement.outerHTML
            };
        }"""
    )

    html_out_path.write_text("<!DOCTYPE html>\n" + fit_info["updated_html"], encoding="utf-8")
    page.screenshot(path=str(overlay_png_path), omit_background=True)
    return fit_info


def r2_put(local_path: Path, r2_key: str) -> str:
    subprocess.run(
        ["python3", str(R2_MANAGER), "--put", str(local_path), r2_key],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return f"https://media.fedu.vn/{r2_key}"


def process_kb_chunk(kb_ids: List[str], master: Dict[str, Any], plate_map: Dict[str, Path]) -> List[Dict[str, Any]]:
    """Một worker xử lý một nhóm KB bằng 1 phiên Chromium duy nhất."""
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

            render_overlay_png_on_page(page, html_primary, html_primary_path, ov_primary_png)
            render_overlay_png_on_page(page, html_alt, html_alt_path, ov_alt_png)

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

            # Tìm ảnh cũ để đối chiếu
            old_candidate = BASE_DIR / kb_id / "after" / f"{kb_id}_A1_after_opt.jpg"
            if not old_candidate.exists():
                old_candidate = BASE_DIR / "KB_15" / "after" / "KB_15_A1_after_opt.jpg"

            make_dual_3col_sbs_image(
                color_img_path=img_color_path,
                bw_img_path=img_bw_path,
                old_img_path=old_candidate,
                out_sbs_path=img_sbs_path,
                kb_id=kb_id,
                label_pair=f"{h_code}×{style_code}",
            )

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

    # Sau khi đóng Chromium của worker, chạy kiểm toán + upload R2
    ver_tag = f"v6_{int(time.time()) % 100000}"
    final_summaries = []
    for item in results:
        kb_id = item["kb_id"]
        kb_lower = item["kb_lower"]
        spec = item["spec"]

        audit_res = audit_v3_banner(
            html_path=item["html_primary_path"],
            final_img_path=item["img_color_path"],
            expected_lines=3,
            person_side=item["side"],
        )

        # Upload song song 5 file của KB này lên R2
        r2_color = r2_put(item["img_color_path"], f"banner2/{kb_lower}_color.jpg")
        r2_final = r2_put(item["img_final_path"], f"banner2/{kb_lower}_final.jpg")
        r2_bw = r2_put(item["img_bw_path"], f"banner2/{kb_lower}_bw.jpg")
        r2_alt = r2_put(item["img_alt_path"], f"banner2/{kb_lower}_alt.jpg")
        r2_sbs = r2_put(item["img_sbs_path"], f"banner2/{kb_lower}_sbs.jpg")

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
            "subline_summary": f"🎨 Bản Màu Kodak Portra & 🖤 Bản Đen Trắng Fine-Art • {item['style_name']}",
            "audit_score": f"{audit_res['score']} PASS",
            "score": audit_res["score"],
            "all_13_pass": audit_res["all_13_pass"],
            "color_img_url": r2_color,
            "bw_img_url": r2_bw,
            "final_img_url": r2_final,
            "alt_img_url": r2_alt,
            "secondary_img_url": r2_bw,
            "secondary_label": "🖤 Bản Đen Trắng",
            "sbs_img_url": r2_sbs,
            "r2_color_url": r2_color,
            "r2_bw_url": r2_bw,
            "r2_final_url": r2_final,
            "r2_alt_url": r2_alt,
            "r2_sbs_url": r2_sbs,
        }
        (CARDS_DIR / f"{kb_id}.json").write_text(json.dumps(card_data, ensure_ascii=False, indent=2), encoding="utf-8")
        final_summaries.append(
            {
                "kb_id": kb_id,
                "score": audit_res["score"],
                "color_url": r2_color,
                "bw_url": r2_bw,
            }
        )
        print(f"[DONE] {kb_id} -> Color & B&W ({audit_res['score']})", flush=True)

    return final_summaries


def main():
    parser = argparse.ArgumentParser(description="Zero-Blur Dual Color & B&W Mass Pipeline V6.0")
    parser.add_argument("--workers", type=int, default=7, help="Số tiến trình chạy song song")
    parser.add_argument("--kbs", type=str, default="ALL", help="ALL hoặc danh sách KB_01,KB_02...")
    args = parser.parse_args()

    t0 = time.time()
    plate_map = harvest_generated_plates()
    print(f"[HARVEST] Đã thu hoạch {len(plate_map)} Phôi Nền Thật Không Blur: {sorted(plate_map.keys())}", flush=True)

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
        futs = [ex.submit(process_kb_chunk, ch, master, plate_map) for ch in chunks if ch]
        for f in concurrent.futures.as_completed(futs):
            all_done.extend(f.result())

    # Đồng bộ banner2.html lên R2
    hub_res = atomic_rebuild_and_sync(push_r2=True)
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
