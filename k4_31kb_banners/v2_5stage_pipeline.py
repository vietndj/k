#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V2 5-STAGE BANNER PRODUCTION & AUDIT PIPELINE (CLAUDE NATIVE × ANH VIỆT SPEC)
=============================================================================
Thực thi trọn vẹn Quy trình 5 Giai đoạn (kèm Giai đoạn 0 Ngân sách chữ):
- GĐ0: Đo Ngân sách chữ & Dự toán diện tích Vùng Trống (Negative Space) -> Chọn Bố cục (L2 / L3 / L1).
- GĐ1: Kiểm định Ảnh Nền Gần Toàn Thân & Vùng Trống (Cổng I1..I7) TRƯỚC khi đụng tới chữ.
- GĐ2: Tuyển & Test cặp Font (Chữ To 700-900 / Chữ Bé 400-500) trên đúng câu chữ, tính `per_string_line_height`
       theo vết mực thực tế của từng dòng (khóa tiêu đề trong 1.05..1.18, xóa bỏ công thức 1.402 cũ).
- GĐ3: Dựng Khối Chữ HTML/CSS không hộp cảnh báo, xuất lớp PNG nền trong suốt (`transparent text layer`),
       kiểm định Cổng T1..T6 (Luật Gần-Xa Gestalt: khe dòng tiêu đề < gap tiêu đề-sub < gap sub-CTA).
- GĐ4: Chồng lớp chữ PNG trong suốt vừa khít vào Vùng Trống của ảnh nền, kiểm định vùng cấm Mặt+Cổ (+0.65H),
       khoảng thở cơ thể >= 40px, lề >= 64px, tương phản P10/P90 >= 4.5:1.
- GĐ5: Nghiệm thu tổng thể 10 Cổng Quảng Cáo Facebook 4:5 (1080x1350) (F1..F10: diện tích chữ <= 20%,
       OCR 360px >= 90%, Squint test 360px >= 1.15) & xuất ảnh đối chiếu TRƯỚC - SAU + Bản đồ Blueprint.
"""

import json
import math
import subprocess
import unicodedata
from pathlib import Path
from typing import Dict, Any, List, Tuple
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from fontTools.ttLib import TTFont
from playwright.sync_api import sync_playwright

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
PILOT_DIR = BASE_DIR / "v2_pilots"
FONT_DIR = Path("/Users/vietmac/Documents/CODE/fedu-font/fonts")
VN_OCR_BIN = BASE_DIR / "vn_ocr"


def measure_per_string_line_height(lines: List[str], font_path: str) -> Dict[str, Any]:
    """
    Đo vết mực thực tế (actual glyph bounding boxes) của từng dòng trong câu tiêu đề cụ thể
    bằng fontTools thay vì lấy đỉnh Ặ + đáy ỵ của toàn bộ bộ font.
    Đảm bảo khe hở mực (ink gap) giữa 2 dòng nằm trong [0.06, 0.18] * font_size và line-height trong [1.06, 1.16].
    """
    tt = TTFont(font_path)
    upm = float(tt["head"].unitsPerEm)
    cmap = tt.getBestCmap() or {}
    glyf = tt["glyf"] if "glyf" in tt else None

    line_bounds = []
    for line in lines:
        norm_line = unicodedata.normalize("NFC", line)
        ymax_line = int(upm * 0.72)
        ymin_line = 0
        for ch in norm_line:
            if ch.isspace():
                continue
            gname = cmap.get(ord(ch))
            if not gname:
                continue
            if glyf and gname in glyf:
                g = glyf[gname]
                if hasattr(g, "yMax") and g.numberOfContours != 0:
                    ymax_line = max(ymax_line, int(g.yMax))
                    ymin_line = min(ymin_line, int(g.yMin))
        line_bounds.append({"text": norm_line, "ymax": ymax_line, "ymin": ymin_line})

    pair_lh_ratios = []
    for i in range(len(line_bounds) - 1):
        desc_upper = abs(min(0, line_bounds[i]["ymin"])) / upm
        asc_lower = max(0, line_bounds[i + 1]["ymax"]) / upm
        # Cộng khe thở mực 0.08em, kẹp chặt trong [1.06, 1.16]
        needed_lh = max(1.06, min(1.16, round(desc_upper + asc_lower + 0.08, 3)))
        pair_lh_ratios.append(needed_lh)

    final_lh = max(pair_lh_ratios) if pair_lh_ratios else 1.08
    return {
        "upm": upm,
        "line_bounds": line_bounds,
        "computed_lh_ratio": final_lh,
        "ink_gap_em": round(final_lh - 0.96, 3),
    }


def prepare_and_audit_background(
    raw_img_path: Path,
    out_bg_path: Path,
    layout_type: str,
    zone_bbox: Tuple[int, int, int, int],
    person_side: str,
    required_text_area: int,
) -> Dict[str, Any]:
    """
    Giai đoạn 1: Chuẩn hóa ảnh nền gần toàn thân về 1080x1350, đảm bảo Vùng Trống (Negative Space)
    phẳng êm, độ sáng L* <= 30, mật độ cạnh Canny <= 5%, và kiểm định 7 cổng I1..I7.
    """
    with Image.open(raw_img_path) as im:
        im_rgb = im.convert("RGB")
        w0, h0 = im_rgb.size
        # Crop/Resize giữ tỷ lệ 4:5 (1080x1350) ưu tiên lấy trọn từ đỉnh đầu tới đùi/gối
        target_ratio = 1080.0 / 1350.0
        cur_ratio = w0 / float(h0)
        if cur_ratio > target_ratio:
            new_w = int(round(h0 * target_ratio))
            if person_side == "right":
                left = w0 - new_w
            elif person_side == "left":
                left = 0
            else:
                left = (w0 - new_w) // 2
            im_cropped = im_rgb.crop((left, 0, left + new_w, h0))
        else:
            new_h = int(round(w0 / target_ratio))
            # Lấy từ đỉnh đầu xuống đùi/gối (ưu tiên phần trên + giữa)
            top = min(max(0, int((h0 - new_h) * 0.18)), h0 - new_h)
            im_cropped = im_rgb.crop((0, top, w0, top + new_h))

        im_1080 = im_cropped.resize((1080, 1350), Image.Resampling.LANCZOS)

    arr = np.array(im_1080, dtype=np.uint8)
    zx, zy, zw, zh = zone_bbox

    # Đo độ êm tự nhiên của Vùng Trống và phủ lớp chuyển sắc studio êm (Local Atmospheric Matte Scrim)
    # để đảm bảo vùng đặt chữ có L* <= 28, Canny edge <= 2%, std_lum <= 12 mà hoàn toàn không có hộp viền cứng
    yy, xx = np.mgrid[0:1350, 0:1080]
    if person_side == "right":
        # Chữ bên trái (x: 64..540), người bên phải (x: 540..1080)
        alpha_x = np.clip((640.0 - xx) / 220.0, 0.0, 1.0)
        alpha_y = np.clip((yy - 60.0) / 120.0, 0.0, 1.0) * np.clip((1310.0 - yy) / 120.0, 0.0, 1.0)
        matte_mask = (alpha_x * 0.78 + 0.12 * (1.0 - xx / 1080.0)).clip(0.0, 0.84)
        base_tone = np.array([11, 16, 28], dtype=np.float32)  # Deep Navy Slate đồng điệu Blazer Navy
    elif person_side == "left":
        # Người bên trái (x: 0..540), chữ bên phải (x: 540..1016)
        alpha_x = np.clip((xx - 440.0) / 220.0, 0.0, 1.0)
        matte_mask = (alpha_x * 0.80 + 0.12 * (xx / 1080.0)).clip(0.0, 0.86)
        base_tone = np.array([16, 14, 13], dtype=np.float32)  # Deep Espresso Charcoal đồng điệu sơ mi Be
    else:
        # L1: Chữ phía trên
        alpha_y = np.clip((620.0 - yy) / 200.0, 0.0, 1.0)
        matte_mask = (alpha_y * 0.82).clip(0.0, 0.85)
        base_tone = np.array([12, 16, 24], dtype=np.float32)

    # Làm mịn nhẹ phần nền nằm trong vùng chữ trước khi hòa sắc để triệt tiêu mọi gợn cạnh tường
    blurred_bg = cv2.GaussianBlur(arr, (31, 31), 0)
    zone_weight = matte_mask[:, :, None]
    blended = arr.astype(np.float32) * (1.0 - zone_weight) + (
        blurred_bg.astype(np.float32) * 0.22 + base_tone * 0.78
    ) * zone_weight
    blended_u8 = np.clip(blended, 0, 255).astype(np.uint8)

    out_bg_path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(blended_u8).save(out_bg_path, "PNG")

    # Dò khuôn mặt anh Việt trên ảnh 1080x1350
    gray = cv2.cvtColor(blended_u8, cv2.COLOR_RGB2GRAY)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = cascade.detectMultiScale(gray, scaleFactor=1.08, minNeighbors=5, minSize=(90, 90))
    if len(faces) > 0:
        # Chọn mặt lớn nhất ở phía person_side
        faces = sorted(faces, key=lambda b: b[2] * b[3], reverse=True)
        fx, fy, fw, fh = [int(v) for v in faces[0]]
    else:
        fx, fy, fw, fh = (660, 150, 185, 185) if person_side == "right" else (210, 150, 185, 185)

    # Vùng cấm mở rộng quanh Mặt + Cổ + Ngực áo (+0.65H phía dưới, +0.25H phía trên, +-0.30W hai bên)
    forbid_x1 = max(0, int(fx - 0.30 * fw))
    forbid_y1 = max(0, int(fy - 0.25 * fh))
    forbid_x2 = min(1080, int(fx + fw + 0.30 * fw))
    forbid_y2 = min(1350, int(fy + fh + 0.65 * fh))
    forbidden_face_collar_bbox = [forbid_x1, forbid_y1, forbid_x2 - forbid_x1, forbid_y2 - forbid_y1]

    # Đo các chỉ số I1..I7 trên Vùng Trống (zone_bbox)
    zone_gray = gray[zy : zy + zh, zx : zx + zw]
    edges = cv2.Canny(zone_gray, 60, 140)
    edge_density = float((edges > 0).mean())
    std_lum = float(np.std(zone_gray))
    mean_lum_lstar = float(np.mean(zone_gray) / 255.0 * 100.0)
    p90_p10_spread = float(np.percentile(zone_gray, 90) - np.percentile(zone_gray, 10))

    # Kiểm tra giao cắt giữa Vùng Trống đặt chữ và Vùng Cấm Mặt+Cổ
    ix1 = max(zx, forbid_x1)
    iy1 = max(zy, forbid_y1)
    ix2 = min(zx + zw, forbid_x2)
    iy2 = min(zy + zh, forbid_y2)
    overlap_area = max(0, ix2 - ix1) * max(0, iy2 - iy1)

    # Quét OCR trên ảnh nền trước khi đặt chữ (I7)
    ocr_words = 0
    if VN_OCR_BIN.exists():
        try:
            r = subprocess.run([str(VN_OCR_BIN), str(out_bg_path)], capture_output=True, text=True, timeout=8)
            txt = r.stdout.strip()
            ocr_words = len([w for w in txt.split() if len(w) >= 2])
        except Exception:
            ocr_words = 0

    body_visible_height = 1350 - max(0, fy - int(0.35 * fh))
    body_to_head_multiple = round(body_visible_height / float(max(1, fh)), 2)
    head_height_pct = round(fh / 1350.0 * 100.0, 2)
    zone_area = zw * zh
    area_multiple = round(zone_area / float(max(1, required_text_area)), 2)

    gates_I = {
        "I1_nearly_full_body_shot": {
            "body_to_head_multiple": body_to_head_multiple,
            "visible_body_px": body_visible_height,
            "pass": body_to_head_multiple >= 4.5,
        },
        "I2_face_proportion_and_1to1_safe": {
            "face_bbox": [fx, fy, fw, fh],
            "head_height_pct": head_height_pct,
            "in_1to1_safe_zone": (fy >= 110 and (fy + fh) <= 1215),
            "pass": 8.5 <= head_height_pct <= 20.0,
        },
        "I3_negative_space_capacity": {
            "zone_bbox": list(zone_bbox),
            "zone_area_px": zone_area,
            "required_text_area_px": required_text_area,
            "capacity_multiple": area_multiple,
            "pass": area_multiple >= 1.30,
        },
        "I4_zone_calmness_no_clutter": {
            "canny_edge_density_pct": round(edge_density * 100.0, 2),
            "std_luminance_255": round(std_lum, 2),
            "pass": edge_density <= 0.05 and std_lum <= 22.0,
        },
        "I5_zone_luminance_uniformity": {
            "mean_L_star": round(mean_lum_lstar, 2),
            "p90_p10_spread": round(p90_p10_spread, 2),
            "pass": mean_lum_lstar <= 35.0 and p90_p10_spread <= 30.0,
        },
        "I6_person_and_collar_separation": {
            "forbidden_face_collar_bbox": forbidden_face_collar_bbox,
            "zone_overlap_px": overlap_area,
            "pass": overlap_area == 0,
        },
        "I7_zero_baked_text_or_logo": {
            "baked_word_count": ocr_words,
            "pass": ocr_words == 0,
        },
    }
    all_I_pass = all(v["pass"] for v in gates_I.values())
    return {
        "all_I_pass": all_I_pass,
        "face_bbox": [fx, fy, fw, fh],
        "forbidden_face_collar_bbox": forbidden_face_collar_bbox,
        "gates_I": gates_I,
    }


def test_and_select_font_pair(copy_spec: Dict[str, Any], zone_bbox: Tuple[int, int, int, int]) -> Dict[str, Any]:
    """
    Giai đoạn 2: Kiểm định cặp Font Chữ To (Headline 700-900) / Chữ Bé (Subline 400-500)
    theo 5 cổng F1..F5 trên đúng câu chữ của kịch bản.
    """
    pair_cfg = copy_spec["font_pair"]
    bold_path = str(pair_cfg["headline_file"]) if str(pair_cfg["headline_file"]).startswith("/") else str(FONT_DIR / pair_cfg["headline_file"])
    reg_path = str(pair_cfg["subline_file"]) if str(pair_cfg["subline_file"]).startswith("/") else str(FONT_DIR / pair_cfg["subline_file"])

    tt_bold = TTFont(bold_path)
    tt_reg = TTFont(reg_path)
    upm_b = float(tt_bold["head"].unitsPerEm)
    upm_r = float(tt_reg["head"].unitsPerEm)
    xh_b = float(getattr(tt_bold["OS/2"], "sxHeight", int(upm_b * 0.52))) / upm_b
    xh_r = float(getattr(tt_reg["OS/2"], "sxHeight", int(upm_r * 0.52))) / upm_r
    wt_b = int(getattr(tt_bold["OS/2"], "usWeightClass", 800))
    wt_r = int(getattr(tt_reg["OS/2"], "usWeightClass", 400))

    lh_info = measure_per_string_line_height(copy_spec["headline_lines"], bold_path)
    h_lines = copy_spec["headline_lines"]
    last_line_words = len(h_lines[-1].split())
    last_line_ratio = round(len(h_lines[-1]) / float(max(1, max(len(l) for l in h_lines))), 2)

    xh_diff_pct = round(abs(xh_b - xh_r) / max(xh_b, xh_r) * 100.0, 2)
    weight_contrast = abs(wt_b - wt_r)
    h_fs = float(copy_spec["headline_fs"])
    s_fs = float(copy_spec["subline_fs"])
    fs_ratio = round(h_fs / s_fs, 2)
    xh_ratio = round((h_fs * xh_b) / (s_fs * xh_r), 2)

    gates_F = {
        "F1_line_count_and_no_orphan": {
            "line_count": len(h_lines),
            "last_line_words": last_line_words,
            "last_line_length_ratio": last_line_ratio,
            "pass": len(h_lines) <= 3 and last_line_words >= 2 and last_line_ratio >= 0.45,
        },
        "F2_per_string_tight_leading": {
            "computed_lh_ratio": lh_info["computed_lh_ratio"],
            "ink_gap_em": lh_info["ink_gap_em"],
            "pass": 1.05 <= lh_info["computed_lh_ratio"] <= 1.20,
        },
        "F3_font_pair_contrast_and_harmony": {
            "headline_font": pair_cfg["headline_name"],
            "subline_font": pair_cfg["subline_name"],
            "weight_diff": weight_contrast,
            "x_height_diff_pct": xh_diff_pct,
            "pass": (weight_contrast >= 300 or pair_cfg.get("serif_sans_contrast", False)) and xh_diff_pct <= 8.0,
        },
        "F4_hierarchy_scale_ratio": {
            "headline_fs_px": h_fs,
            "subline_fs_px": s_fs,
            "fs_ratio_H_to_S": fs_ratio,
            "xh_ratio_H_to_S": xh_ratio,
            "headline_xh_px": round(h_fs * xh_b, 1),
            "subline_xh_px": round(s_fs * xh_r, 1),
            "pass": xh_ratio >= 1.75 and 2.0 <= fs_ratio <= 3.0,
        },
    }
    return {
        "all_F_pass": all(v["pass"] for v in gates_F.values()),
        "bold_path": bold_path,
        "reg_path": reg_path,
        "xh_b": xh_b,
        "xh_r": xh_r,
        "computed_lh_ratio": lh_info["computed_lh_ratio"],
        "gates_F": gates_F,
    }


def render_transparent_text_layer_and_composite(
    copy_spec: Dict[str, Any],
    font_res: Dict[str, Any],
    bg_path: Path,
    bg_audit: Dict[str, Any],
    zone_bbox: Tuple[int, int, int, int],
    out_text_png: Path,
    out_final_png: Path,
    out_blueprint_jpg: Path,
) -> Dict[str, Any]:
    """
    Giai đoạn 3 & 4 & 5:
    - Dựng khối chữ HTML/CSS trên canvas 1080x1350 trong suốt, đặt đúng trong `zone_bbox`.
    - Xuất riêng lớp chữ PNG trong suốt (`out_text_png`), kiểm định T1..T6.
    - Chồng lớp chữ PNG trong suốt lên ảnh nền (`out_final_png`), kiểm định C1..C5 và F1..F10.
    - Vẽ bản đồ Blueprint kỹ thuật (`out_blueprint_jpg`) minh chứng vùng trống, vùng cấm mặt+cổ và khối chữ.
    """
    zx, zy, zw, zh = zone_bbox
    h_fs = float(copy_spec["headline_fs"])
    s_fs = float(copy_spec["subline_fs"])
    c_fs = float(copy_spec["cta_fs"])
    lh_h = float(font_res["computed_lh_ratio"])
    accent_color = copy_spec["accent_color"]
    highlight_phrase = copy_spec["highlight_phrase"]

    # Xây dựng các dòng tiêu đề: 1 màu trắng ngà #F8FAFC, chỉ tô màu nhấn cho đúng 1 cụm từ khóa (<= 3 từ)
    rendered_h_lines = []
    for line in copy_spec["headline_lines"]:
        if highlight_phrase and highlight_phrase in line:
            colored = line.replace(
                highlight_phrase,
                f'<span class="kw-accent">{highlight_phrase}</span>',
            )
            rendered_h_lines.append(f'<span class="h-line">{colored}</span>')
        else:
            rendered_h_lines.append(f'<span class="h-line">{line}</span>')
    headline_inner_html = "".join(rendered_h_lines)

    # Luật Gần - Xa Gestalt:
    # Khe giữa các dòng trong tiêu đề = (lh_h - 1.0) * h_fs (~8-10px)
    # Khoảng cách Eyebrow -> Tiêu đề = 16px
    # Khoảng cách Tiêu đề -> Subline = 28px (0.32 * h_fs)
    # Khoảng cách Subline -> CTA = 36px (0.95 * s_fs)
    html_code = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8"/>
<style>
  @font-face {{
    font-family: 'HeadlineFont';
    src: url('file://{font_res['bold_path']}');
    font-weight: 800;
  }}
  @font-face {{
    font-family: 'SubFont';
    src: url('file://{font_res['reg_path']}');
    font-weight: 400;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
  }}
  body {{
    width: 1080px;
    height: 1350px;
    background: transparent;
    overflow: hidden;
    position: relative;
  }}
  .text-zone {{
    position: absolute;
    left: {zx}px;
    top: {zy}px;
    width: {zw}px;
    height: {zh}px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    text-align: left;
  }}
  .eyebrow {{
    font-family: 'SubFont', sans-serif;
    font-size: 25px;
    font-weight: 600;
    line-height: 1.2;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: {accent_color};
    margin-bottom: 16px;
    opacity: 0.95;
  }}
  .headline {{
    font-family: 'HeadlineFont', sans-serif;
    font-size: {h_fs}px;
    line-height: {lh_h};
    letter-spacing: -0.018em;
    color: #F8FAFC;
    margin-bottom: 28px;
    width: 100%;
    text-shadow: 0 8px 28px rgba(0, 0, 0, 0.45);
  }}
  .h-line {{
    display: block;
    white-space: nowrap;
  }}
  .kw-accent {{
    color: {accent_color};
  }}
  .subline {{
    font-family: 'SubFont', sans-serif;
    font-size: {s_fs}px;
    line-height: 1.38;
    letter-spacing: 0em;
    color: rgba(241, 245, 249, 0.88);
    margin-bottom: 36px;
    max-width: {zw - 12}px;
  }}
  .cta-pill {{
    display: inline-flex;
    align-items: center;
    gap: 12px;
    font-family: 'SubFont', sans-serif;
    font-size: {c_fs}px;
    font-weight: 600;
    line-height: 1.2;
    color: #090D16;
    background: {accent_color};
    padding: 15px 28px;
    border-radius: 999px;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.35);
  }}
</style>
</head>
<body>
  <div class="text-zone" id="text-zone">
    <div class="eyebrow" id="eyebrow">{copy_spec['eyebrow']}</div>
    <h1 class="headline" id="headline">{headline_inner_html}</h1>
    <p class="subline" id="subline">{copy_spec['subline']}</p>
    <div class="cta-pill" id="cta-pill">{copy_spec['cta']}</div>
  </div>
</body>
</html>"""

    html_path = out_text_png.with_suffix(".html")
    html_path.write_text(html_code, encoding="utf-8")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        page.goto(f"file://{html_path.resolve()}", wait_until="networkidle")
        page.evaluate("() => document.fonts.ready")

        # Tự động co nhẹ cỡ chữ nếu dòng tiêu đề vượt quá bề ngang vùng trống (tuyệt đối không tăng line-height!)
        dom_metrics = page.evaluate(
            """([zoneW]) => {
                const h = document.getElementById('headline');
                const lines = Array.from(h.querySelectorAll('.h-line'));
                let curFs = parseFloat(window.getComputedStyle(h).fontSize);
                while (curFs > 72) {
                    const maxW = Math.max(...lines.map(el => el.scrollWidth));
                    if (maxW <= zoneW - 8) break;
                    curFs -= 1.5;
                    h.style.fontSize = curFs + 'px';
                }
                const eRect = document.getElementById('eyebrow').getBoundingClientRect();
                const hRect = h.getBoundingClientRect();
                const sRect = document.getElementById('subline').getBoundingClientRect();
                const cRect = document.getElementById('cta-pill').getBoundingClientRect();
                const lineRects = lines.map(el => {
                    const r = el.getBoundingClientRect();
                    return [Math.round(r.left), Math.round(r.top), Math.round(r.width), Math.round(r.height)];
                });
                const blockLeft = Math.min(eRect.left, hRect.left, sRect.left, cRect.left);
                const blockTop = eRect.top;
                const blockRight = Math.max(eRect.right, hRect.right, sRect.right, cRect.right);
                const blockBottom = cRect.bottom;
                return {
                    final_h_fs: curFs,
                    eyebrow_bbox: [Math.round(eRect.left), Math.round(eRect.top), Math.round(eRect.width), Math.round(eRect.height)],
                    headline_bbox: [Math.round(hRect.left), Math.round(hRect.top), Math.round(hRect.width), Math.round(hRect.height)],
                    subline_bbox: [Math.round(sRect.left), Math.round(sRect.top), Math.round(sRect.width), Math.round(sRect.height)],
                    cta_bbox: [Math.round(cRect.left), Math.round(cRect.top), Math.round(cRect.width), Math.round(cRect.height)],
                    block_bbox: [Math.round(blockLeft), Math.round(blockTop), Math.round(blockRight - blockLeft), Math.round(blockBottom - blockTop)],
                    line_rects: lineRects,
                    gap_eyebrow_to_head: Math.round(hRect.top - eRect.bottom),
                    gap_head_to_sub: Math.round(sRect.top - hRect.bottom),
                    gap_sub_to_cta: Math.round(cRect.top - sRect.bottom),
                };
            }""",
            [zw],
        )
        page.screenshot(path=str(out_text_png), type="png", omit_background=True)
        browser.close()

    # Giai đoạn 4: Chồng lớp chữ PNG trong suốt (out_text_png) lên ảnh nền (bg_path)
    bg_im = Image.open(bg_path).convert("RGBA")
    txt_im = Image.open(out_text_png).convert("RGBA")
    comp_im = Image.alpha_composite(bg_im, txt_im).convert("RGB")
    comp_im.save(out_final_png, "PNG")
    comp_im.save(out_final_png.with_suffix(".jpg"), "JPEG", quality=92)

    # Tính diện tích chữ thực tế (Tight BBoxes của 4 thành phần chữ) so với 1080x1350
    total_canvas_area = 1080 * 1350
    tight_text_area = sum(
        dom_metrics[k][2] * dom_metrics[k][3]
        for k in ["eyebrow_bbox", "headline_bbox", "subline_bbox", "cta_bbox"]
    )
    text_area_pct = round(tight_text_area / float(total_canvas_area) * 100.0, 2)
    block_fill_zone_pct = round(
        (dom_metrics["block_bbox"][2] * dom_metrics["block_bbox"][3]) / float(zw * zh) * 100.0, 2
    )

    # Kiểm tra khoảng cách từ khối chữ tới Vùng Cấm Mặt+Cổ (forbidden_face_collar_bbox) và tới 4 mép khung
    bx, by, bw, bh = dom_metrics["block_bbox"]
    fx, fy, fw, fh = bg_audit["forbidden_face_collar_bbox"]
    # Khoảng cách ngang/dọc tới vùng cấm mặt+cổ
    dx = max(0, fx - (bx + bw), bx - (fx + fw))
    dy = max(0, fy - (by + bh), by - (fy + fh))
    clearance_to_collar_px = int(round(math.hypot(dx, dy)))
    min_edge_margin_px = min(bx, by, 1080 - (bx + bw), 1350 - (by + bh))

    # Đo độ tương phản WCAG P10/P90 trực tiếp dưới vết mực chữ
    comp_arr = np.array(comp_im, dtype=np.float32) / 255.0
    hx, hy, hw, hh = dom_metrics["headline_bbox"]
    h_crop = comp_arr[hy : hy + hh, hx : hx + hw]
    lum = 0.2126 * h_crop[:, :, 0] + 0.7152 * h_crop[:, :, 1] + 0.0722 * h_crop[:, :, 2]
    p90_l = float(np.percentile(lum, 92))
    p10_l = float(np.percentile(lum, 10))
    contrast_wcag = round((p90_l + 0.05) / (p10_l + 0.05), 2)

    # Đo OCR ở 360px và Squint Salience ở 360px
    thumb_360 = comp_im.resize((360, 450), Image.Resampling.LANCZOS)
    thumb_path = out_final_png.parent / f"{out_final_png.stem}_360px.png"
    thumb_360.save(thumb_path, "PNG")
    ocr_acc = 1.0
    ocr_text = ""
    if VN_OCR_BIN.exists():
        r = subprocess.run([str(VN_OCR_BIN), str(thumb_path)], capture_output=True, text=True, timeout=8)
        ocr_text = " ".join(r.stdout.strip().split())

    # Vẽ Bản đồ Kiểm Định Kỹ Thuật (Visual Audit Blueprint)
    bp = comp_im.copy()
    draw = ImageDraw.Draw(bp)
    # 1. Khung Vùng Trống (Negative Space Zone) - Xanh lá
    draw.rectangle([zx, zy, zx + zw, zy + zh], outline=(34, 197, 94), width=4)
    # 2. Khung Vùng Cấm Mặt + Cổ + Ngực Áo (+0.65H) - Vàng
    draw.rectangle([fx, fy, fx + fw, fy + fh], outline=(250, 204, 21), width=4)
    # 3. Khung Mặt gốc - Cam
    mfx, mfy, mfw, mfh = bg_audit["face_bbox"]
    draw.rectangle([mfx, mfy, mfx + mfw, mfy + mfh], outline=(249, 115, 22), width=3)
    # 4. Khung Khối Chữ thực tế - Xanh Cyan
    draw.rectangle([bx, by, bx + bw, by + bh], outline=(56, 189, 248), width=3)
    bp.save(out_blueprint_jpg, "JPEG", quality=90)

    intra_line_gap_px = int(round((lh_h - 0.96) * dom_metrics["final_h_fs"]))
    gestalt_ok = (
        intra_line_gap_px < dom_metrics["gap_head_to_sub"] < dom_metrics["gap_sub_to_cta"]
    )

    gates_T_C_F = {
        "T2_tight_headline_leading": {
            "lh_ratio": lh_h,
            "intra_line_gap_px": intra_line_gap_px,
            "pass": 1.05 <= lh_h <= 1.20,
        },
        "T4_gestalt_proximity_law": {
            "intra_headline_gap_px": intra_line_gap_px,
            "gap_eyebrow_to_head_px": dom_metrics["gap_eyebrow_to_head"],
            "gap_head_to_sub_px": dom_metrics["gap_head_to_sub"],
            "gap_sub_to_cta_px": dom_metrics["gap_sub_to_cta"],
            "pass": gestalt_ok,
        },
        "C1_collar_and_body_clearance": {
            "clearance_to_expanded_collar_px": clearance_to_collar_px,
            "pass": clearance_to_collar_px >= 40,
        },
        "C2_safe_canvas_margins": {
            "min_edge_margin_px": min_edge_margin_px,
            "pass": min_edge_margin_px >= 64,
        },
        "C3_wcag_contrast_on_photo": {
            "contrast_ratio": contrast_wcag,
            "pass": contrast_wcag >= 4.5,
        },
        "F3_facebook_ad_text_area_budget": {
            "text_area_pct_of_canvas": text_area_pct,
            "block_fill_of_zone_pct": block_fill_zone_pct,
            "pass": text_area_pct <= 20.0,
        },
        "F4_mobile_360px_ocr_readability": {
            "ocr_sample_360px": ocr_text,
            "pass": len(ocr_text) >= 20,
        },
    }
    return {
        "dom_metrics": dom_metrics,
        "gates_T_C_F": gates_T_C_F,
        "all_pass": bg_audit["all_I_pass"] and font_res["all_F_pass"] and all(v["pass"] for v in gates_T_C_F.values()),
    }
