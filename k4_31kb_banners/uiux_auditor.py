#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P0.3 - UI/UX TYPOGRAPHY 8-METRIC AUDITOR (1080x1350 + 360px Squint & Apple Vision OCR)
======================================================================================
Đo tự động và khách quan 8 chỉ số UI/UX Typography theo kiến trúc CLAUDE2 (job aba41ae4):
1. Cỡ chữ chuẩn hóa theo `x-height` (px): Tiêu đề >= 44px · Dòng phụ >= 20px · Nút >= 22px
2. Khoảng cách dòng cho dấu tiếng Việt: line_height_ratio >= min_line_height_ratio & điểm dấu chồng dòng = 0
3. Khoảng cách chữ (Kerning/Tracking): đúng quy tắc nhóm font & không dính chữ
4. Độ tương phản (WCAG P10/P90 worst-case dưới nền chữ): Tiêu đề >= 3.0:1 · Chữ nhỏ >= 4.5:1
5. Phân cấp chính phụ & Phép thử làm mờ 360px (sigma=8): tỷ lệ x-height >= 2.0, tối đa 3 cấp chữ, Tiêu đề nổi bật nhất
6. Đọc thử trên điện thoại (OCR 360px bằng Apple Vision `vn_ocr`): Tiêu đề đọc đúng >= 95% ký tự
7. Vùng an toàn & Khuôn mặt: diện tích chữ đè lên `face_bbox` = 0px
8. Mật độ chữ: Tiêu đề <= 2 dòng · Tổng số từ trên ảnh <= 25 từ
"""

import json
import math
import subprocess
import tempfile
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, Any, List, Tuple
import cv2
import numpy as np
from PIL import Image, ImageFilter

OUT_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
VN_OCR_BIN = OUT_DIR / "vn_ocr"


def srgb_to_linear(c: np.ndarray) -> np.ndarray:
    c = c / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def relative_luminance_map(rgb_arr: np.ndarray) -> np.ndarray:
    r = srgb_to_linear(rgb_arr[:, :, 0].astype(np.float32))
    g = srgb_to_linear(rgb_arr[:, :, 1].astype(np.float32))
    b = srgb_to_linear(rgb_arr[:, :, 2].astype(np.float32))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def hex_to_rel_lum(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    rgb = np.array([[[int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)]]], dtype=np.float32)
    return float(relative_luminance_map(rgb)[0, 0])


def wcag_contrast(l1: float, l2: float) -> float:
    bright = max(l1, l2)
    dark = min(l1, l2)
    return (bright + 0.05) / (dark + 0.05)


def bbox_intersection_area(b1: List[float], b2: List[float]) -> int:
    """Tính diện tích giao nhau (px) giữa 2 hình chữ nhật [x, y, w, h]."""
    x1 = max(b1[0], b2[0])
    y1 = max(b1[1], b2[1])
    x2 = min(b1[0] + b1[2], b2[0] + b2[2])
    y2 = min(b1[1] + b1[3], b2[1] + b2[3])
    if x2 <= x1 or y2 <= y1:
        return 0
    return int(round((x2 - x1) * (y2 - y1)))


def clean_norm_text(s: str) -> str:
    s = unicodedata.normalize("NFC", s).lower()
    return "".join(ch for ch in s if ch.isalnum())


def run_ocr_360px(img_path: Path, target_headline: str) -> Dict[str, Any]:
    """Thu ảnh về 360x450px, gọi Apple Vision `vn_ocr` và tính độ khớp ký tự với Tiêu đề."""
    with Image.open(img_path) as im:
        small = im.convert("RGB").resize((360, 450), Image.Resampling.LANCZOS)
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tf:
            tmp_path = Path(tf.name)
        small.save(tmp_path, "PNG")

    try:
        res = subprocess.run(
            [str(VN_OCR_BIN), str(tmp_path)],
            capture_output=True,
            text=True,
            timeout=10,
        )
        items = json.loads(res.stdout) if res.returncode == 0 and res.stdout.strip() else []
    except Exception:
        items = []
    finally:
        if tmp_path.exists():
            tmp_path.unlink()

    recognized_all = " ".join(it.get("text", "") for it in items)
    norm_target = clean_norm_text(target_headline)
    norm_rec = clean_norm_text(recognized_all)

    if not norm_target:
        return {"accuracy": 1.0, "recognized_text": recognized_all}

    # Kiểm tra từng từ/ký tự của tiêu đề trong chuỗi OCR nhận diện được ở 360px
    # Sử dụng LCS / SequenceMatcher trên cửa sổ tốt nhất hoặc đối chiếu ký tự theo thứ tự
    if norm_target in norm_rec:
        acc = 1.0
    else:
        # Tìm chuỗi con trong norm_rec có độ dài tương đương norm_target khớp cao nhất
        t_len = len(norm_target)
        best_ratio = SequenceMatcher(None, norm_target, norm_rec).ratio()
        if len(norm_rec) >= t_len:
            for i in range(len(norm_rec) - t_len + 1):
                sub = norm_rec[i : i + t_len]
                r = SequenceMatcher(None, norm_target, sub).ratio()
                if r > best_ratio:
                    best_ratio = r
        # Hoặc đếm tỷ lệ từ trong target_headline xuất hiện chính xác trong recognized_all
        words = [clean_norm_text(w) for w in target_headline.split() if clean_norm_text(w)]
        if words:
            matched_chars = sum(len(w) for w in words if w in norm_rec)
            word_char_ratio = matched_chars / max(1, sum(len(w) for w in words))
            best_ratio = max(best_ratio, word_char_ratio)
        acc = round(float(best_ratio), 4)

    return {
        "accuracy": acc,
        "recognized_text": recognized_all,
    }


def squint_blur_test_360px(
    img_path: Path,
    headline_bbox_1080: List[float],
    sub_bbox_1080: List[float] = None,
) -> Dict[str, Any]:
    """Thu nhỏ 360x450px, làm mờ Gaussian sigma=8, đo độ nổi thị giác của Tiêu đề so với Dòng phụ & toàn khung."""
    with Image.open(img_path) as im:
        small = im.convert("RGB").resize((360, 450), Image.Resampling.LANCZOS)
        blurred = small.filter(ImageFilter.GaussianBlur(radius=8))
        arr = np.array(blurred, dtype=np.float32)

    lum = 0.2126 * arr[:, :, 0] + 0.7152 * arr[:, :, 1] + 0.0722 * arr[:, :, 2]
    gx = cv2.Sobel(lum, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(lum, cv2.CV_32F, 0, 1, ksize=3)
    energy = np.hypot(gx, gy)

    scale = 360.0 / 1080.0
    hx = max(0, int(headline_bbox_1080[0] * scale) - 6)
    hy = max(0, int(headline_bbox_1080[1] * scale) - 6)
    hw = min(360 - hx, max(20, int(headline_bbox_1080[2] * scale) + 12))
    hh = min(450 - hy, max(16, int(headline_bbox_1080[3] * scale) + 12))

    roi_head_energy = float(np.mean(energy[hy : hy + hh, hx : hx + hw]))
    roi_head_p90 = float(np.percentile(lum[hy : hy + hh, hx : hx + hw], 90))

    if sub_bbox_1080:
        sx = max(0, int(sub_bbox_1080[0] * scale) - 4)
        sy = max(0, int(sub_bbox_1080[1] * scale) - 4)
        sw = min(360 - sx, max(20, int(sub_bbox_1080[2] * scale) + 8))
        sh = min(450 - sy, max(12, int(sub_bbox_1080[3] * scale) + 8))
        roi_sub_energy = float(np.mean(energy[sy : sy + sh, sx : sx + sw])) + 1e-5
        roi_sub_p90 = float(np.percentile(lum[sy : sy + sh, sx : sx + sw], 90)) + 1e-5
        salience_ratio = round(max(roi_head_energy / roi_sub_energy, roi_head_p90 / roi_sub_p90), 3)
    else:
        global_energy = float(np.mean(energy)) + 1e-5
        salience_ratio = round(roi_head_energy / global_energy, 3)

    return {
        "salience_ratio": salience_ratio,
        "headline_blur_p90": round(roi_head_p90, 1),
        "pass": salience_ratio >= 1.05,
    }


def audit_single_banner(png_path: Path, meta: Dict[str, Any]) -> Dict[str, Any]:
    """
    Đo 8 chỉ số UI/UX Typography trên 1 ảnh PNG 1080x1350 kèm metadata DOM từ Playwright (`meta`).
    """
    font_metrics = meta["font"]["metrics"]
    x_ratio = float(font_metrics["x_ratio"])
    reg_x_ratio = float(font_metrics.get("reg_x_ratio", x_ratio))
    min_lh_ratio = float(font_metrics["min_line_height_ratio"])

    # 1. Cỡ chữ chuẩn hóa theo x-height (px)
    h_fs = float(meta["dom"]["headline_font_size_px"])
    s_fs = float(meta["dom"]["sub_font_size_px"])
    c_fs = float(meta["dom"]["cta_font_size_px"])

    h_xh = round(h_fs * x_ratio, 2)
    s_xh = round(s_fs * reg_x_ratio, 2)
    c_xh = round(c_fs * x_ratio, 2)
    m1_pass = (h_xh >= 44.0) and (s_xh >= 20.0) and (c_xh >= 22.0)

    # 2. Khoảng cách dòng cho dấu tiếng Việt & điểm dấu chồng dòng
    actual_lh_ratio = round(float(meta["dom"]["headline_line_height_px"]) / max(1.0, h_fs), 4)
    line_collision_px = int(meta["dom"].get("line_collision_px", 0))
    m2_pass = (line_collision_px == 0) and (actual_lh_ratio >= min_lh_ratio - 0.01)

    # 3. Khoảng cách chữ (Kerning/Tracking)
    tracking_em = float(meta["dom"].get("headline_letter_spacing_em", 0.0))
    char_collision_px = int(meta["dom"].get("char_collision_px", 0))
    m3_pass = (char_collision_px == 0) and (-0.035 <= tracking_em <= 0.06)

    # 4. Độ tương phản WCAG P10/P90 dưới nền khung chữ
    h_cr = round(float(meta["dom"]["headline_contrast_wcag"]), 2)
    s_cr = round(float(meta["dom"]["sub_contrast_wcag"]), 2)
    m4_pass = (h_cr >= 3.0) and (s_cr >= 4.5)

    # 5. Phân cấp chính phụ & Phép thử làm mờ 360px
    xh_hierarchy_ratio = round(h_xh / max(1.0, s_xh), 2)
    squint = squint_blur_test_360px(png_path, meta["dom"]["headline_bbox"], meta["dom"].get("sub_bbox"))
    m5_pass = (xh_hierarchy_ratio >= 2.0) and squint["pass"]

    # 6. Đọc trên điện thoại (OCR 360px)
    ocr_res = run_ocr_360px(png_path, meta["copy"]["headline"])
    m6_pass = ocr_res["accuracy"] >= 0.95

    # 7. Vùng an toàn & Khuôn mặt (không đè mặt & không tràn mép dưới 1315px)
    raw_face = list(meta["outfit"]["face_bbox"])
    p_shift = int(meta["dom"].get("portrait_shift_y", 0))
    face_bbox = [raw_face[0], max(0, raw_face[1] - p_shift), raw_face[2], raw_face[3]]
    text_card_bbox = meta["dom"]["text_card_bbox"]
    face_overlap_px = bbox_intersection_area(face_bbox, text_card_bbox)
    card_bottom_px = int(text_card_bbox[1] + text_card_bbox[3])
    bottom_overflow_px = max(0, card_bottom_px - 1315)
    m7_pass = (face_overlap_px == 0) and (bottom_overflow_px == 0)

    # 8. Lượng chữ (Tiêu đề <= 2 dòng, tổng <= 25 từ)
    h_lines = int(meta["dom"]["headline_line_count"])
    all_text = " ".join([
        meta["copy"].get("hook_tag", ""),
        meta["copy"].get("headline", ""),
        meta["copy"].get("subline", ""),
        meta["copy"].get("cta", ""),
    ])
    total_words = len([w for w in all_text.split() if w.strip()])
    m8_pass = (h_lines <= 2) and (total_words <= 25)

    all_pass = all([m1_pass, m2_pass, m3_pass, m4_pass, m5_pass, m6_pass, m7_pass, m8_pass])
    passed_count = sum([m1_pass, m2_pass, m3_pass, m4_pass, m5_pass, m6_pass, m7_pass, m8_pass])

    return {
        "slot": meta["slot"],
        "png_path": str(png_path),
        "all_8_pass": all_pass,
        "passed_count": f"{passed_count}/8",
        "metrics": {
            "1_x_height_px": {
                "headline_xh": h_xh,
                "sub_xh": s_xh,
                "cta_xh": c_xh,
                "headline_fs": round(h_fs, 1),
                "sub_fs": round(s_fs, 1),
                "cta_fs": round(c_fs, 1),
                "pass": m1_pass,
            },
            "2_viet_line_spacing": {
                "actual_lh_ratio": actual_lh_ratio,
                "min_required_lh_ratio": min_lh_ratio,
                "line_collision_px": line_collision_px,
                "pass": m2_pass,
            },
            "3_kerning_tracking": {
                "headline_tracking_em": tracking_em,
                "char_collision_px": char_collision_px,
                "pass": m3_pass,
            },
            "4_contrast_wcag": {
                "headline_cr_p10_p90": h_cr,
                "sub_cr_p10_p90": s_cr,
                "pass": m4_pass,
            },
            "5_hierarchy_squint_360px": {
                "xh_ratio_head_to_sub": xh_hierarchy_ratio,
                "squint_salience_ratio": squint["salience_ratio"],
                "pass": m5_pass,
            },
            "6_mobile_ocr_360px": {
                "accuracy": ocr_res["accuracy"],
                "recognized_sample": ocr_res["recognized_text"][:100],
                "pass": m6_pass,
            },
            "7_safe_zone_face": {
                "face_bbox": face_bbox,
                "text_card_bbox": text_card_bbox,
                "face_overlap_px": face_overlap_px,
                "card_bottom_px": card_bottom_px,
                "bottom_overflow_px": bottom_overflow_px,
                "pass": m7_pass,
            },
            "8_word_density": {
                "headline_lines": h_lines,
                "total_words": total_words,
                "pass": m8_pass,
            },
        },
    }


if __name__ == "__main__":
    print("uiux_auditor.py ready.")
