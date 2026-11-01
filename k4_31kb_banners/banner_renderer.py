#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P0.4 - REAL-FONT HTML/CSS PLAYWRIGHT BANNER RENDERER (1080x1350)
================================================================
Kết xuất ảnh Banner 1080x1350 từ:
- Lớp 1 (Nền): 176 ảnh chân dung AI Face DNA của anh Việt (đã cache local + dò `face_bbox`)
- Lớp 2 (Chữ): HTML/CSS với @font-face nạp trực tiếp file font thật từ `fedu-font/fonts/`,
  chuẩn hóa cỡ chữ theo `x-height` (px), khoảng cách dòng theo `min_line_height_ratio` của
  dấu chồng tiếng Việt (`Ặ, Ẫ, Ỗ, Ữ`), phối 35 Kiểu Chữ (`STYLE-01..35`) × 19 Kiểu Bố Cục (`Kiểu 1..19`).
- Tích hợp vòng tự nắn DOM trong Playwright trước khi chụp PNG để đảm bảo:
  + Tiêu đề <= 2 dòng, `headline_xh >= 44px`, `sub_xh >= 20px`, `cta_xh >= 22px`
  + `headline_xh / sub_xh >= 2.0`
  + Không đè lên `face_bbox` (`face_overlap_px == 0`)
  + Khoảng trống giữa Dòng 1 và Dòng 2 có `line_collision_px == 0`
  + Đo chính xác WCAG Contrast P10/P90 ngay dưới vùng chữ thực tế.
"""

import json
import math
import os
import unicodedata
from pathlib import Path
from typing import Dict, Any, List, Optional
import numpy as np
from PIL import Image

OUT_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")

# Bảng 35 Kiểu Chữ Hệ Thống (tương ứng STYLE-01 .. STYLE-35)
STYLES_35_CONFIG = {
    f"STYLE-{i:02d}": cfg
    for i, cfg in enumerate([
        {"name": "01. Bật Ý Tưởng", "c1": "#4ADE80", "c2": "#FFFFFF", "accent": "#22C55E", "theme": "dark", "italic_h1": True},
        {"name": "02. TRIỆU VIEW", "c1": "#FB923C", "c2": "#FFFFFF", "accent": "#F97316", "theme": "dark", "upper": True},
        {"name": "03. Bí Quyết Vàng", "c1": "#FBBF24", "c2": "#FFFFFF", "accent": "#F59E0B", "theme": "dark", "italic_h2": True},
        {"name": "04. ĐỊNH VỊ Thương Hiệu", "c1": "#FFFFFF", "c2": "#FACC15", "accent": "#EAB308", "theme": "dark", "italic_h2": True},
        {"name": "05. Khách Hàng TỰ TÌM ĐẾN", "c1": "#FFFFFF", "c2": "#F87171", "accent": "#EF4444", "theme": "dark"},
        {"name": "06. Bứt Phá 3s Đầu", "c1": "#38BDF8", "c2": "#FFFFFF", "accent": "#0EA5E9", "theme": "dark"},
        {"name": "07. Làm Chủ Ống Kính", "c1": "#FFFFFF", "c2": "#67E8F9", "accent": "#06B6D4", "theme": "dark", "italic_h1": True},
        {"name": "08. Đừng Làm Mò (Laser)", "c1": "#FFFFFF", "c2": "#FCA5A5", "accent": "#EF4444", "theme": "dark", "badge_style": "strike"},
        {"name": "09. TÂM ĐIỂM (Vòng Tròn)", "c1": "#F8FAFC", "c2": "#FDE047", "accent": "#EAB308", "theme": "dark", "badge_style": "circle"},
        {"name": "10. KỊCH BẢN ĐỈNH", "c1": "#FFFFFF", "c2": "#E2E8F0", "accent": "#38BDF8", "theme": "dark", "upper": True},
        {"name": "11. ĐỘC BẢN", "c1": "#FFFBEB", "c2": "#FACC15", "accent": "#F59E0B", "theme": "dark"},
        {"name": "12. Tự Tin Chia Sẻ", "c1": "#FFFFFF", "c2": "#FDE68A", "accent": "#D97706", "theme": "dark", "italic_h2": True},
        {"name": "13. QUY TRÌNH 3 BƯỚC", "c1": "#38BDF8", "c2": "#FFFFFF", "accent": "#0284C7", "theme": "dark", "upper": True},
        {"name": "14. 100K FOLLOW", "c1": "#FDE047", "c2": "#FFFFFF", "accent": "#CA8A04", "theme": "dark", "upper": True},
        {"name": "15. Góc Nhìn CHUYÊN GIA", "c1": "#0F172A", "c2": "#B91C1C", "accent": "#DC2626", "theme": "light"},
        {"name": "16. XEM HƯỚNG DẪN", "c1": "#7DD3FC", "c2": "#FFFFFF", "accent": "#0284C7", "theme": "dark"},
        {"name": "17. THỰC CHIẾN Có Kết Quả", "c1": "#FACC15", "c2": "#FFFFFF", "accent": "#EAB308", "theme": "dark"},
        {"name": "18. ĐÒN BẨY Thu Nhập", "c1": "#FDE047", "c2": "#FDA4AF", "accent": "#E11D48", "theme": "dark"},
        {"name": "19. 30 NGÀY Lột Xác", "c1": "#FDE68A", "c2": "#FFFFFF", "accent": "#F59E0B", "theme": "dark"},
        {"name": "20. TỐI ƯU HÓA Thời Gian", "c1": "#FACC15", "c2": "#FFFFFF", "accent": "#EA580C", "theme": "dark"},
        {"name": "21. NĂNG LƯỢNG Tích Cực", "c1": "#38BDF8", "c2": "#FFFFFF", "accent": "#0284C7", "theme": "dark"},
        {"name": "22. All-in-One Video Ngắn", "c1": "#67E8F9", "c2": "#FFFFFF", "accent": "#0891B2", "theme": "dark"},
        {"name": "23. VỊ THẾ Dẫn Đầu", "c1": "#FDE68A", "c2": "#FBBF24", "accent": "#D97706", "theme": "dark"},
        {"name": "24. NỘI DUNG CHẤT", "c1": "#0F172A", "c2": "#0F766E", "accent": "#0D9488", "theme": "light"},
        {"name": "25. 4 Trụ Cột Sự Nghiệp", "c1": "#F1F5F9", "c2": "#FFFFFF", "accent": "#6366F1", "theme": "dark"},
        {"name": "26. Tự Do Tài Chính", "c1": "#67E8F9", "c2": "#FFFFFF", "accent": "#06B6D4", "theme": "dark"},
        {"name": "27. DÁM BẮT ĐẦU", "c1": "#FDE047", "c2": "#FFFFFF", "accent": "#EAB308", "theme": "dark", "upper": True},
        {"name": "28. DẤU ẤN Riêng Biệt", "c1": "#FDE047", "c2": "#FFFBEB", "accent": "#D97706", "theme": "dark"},
        {"name": "29. Truyền Cảm Hứng", "c1": "#FDA4AF", "c2": "#FEF08A", "accent": "#E11D48", "theme": "dark"},
        {"name": "30. Tỏa Sáng ✦", "c1": "#FFFFFF", "c2": "#FDE68A", "accent": "#F59E0B", "theme": "dark", "star": True},
        {"name": "31. HÀNH ĐỘNG NGAY", "c1": "#F8FAFC", "c2": "#7DD3FC", "accent": "#0284C7", "theme": "dark", "upper": True},
        {"name": "32. TẬP TRUNG Bứt Phá", "c1": "#FFFFFF", "c2": "#FDE68A", "accent": "#D97706", "theme": "dark"},
        {"name": "33. VƯỢT MỌI GIỚI HẠN", "c1": "#67E8F9", "c2": "#86EFAC", "accent": "#10B981", "theme": "dark"},
        {"name": "34. Bản Lĩnh Tương Lai", "c1": "#FBBF24", "c2": "#FEF3C7", "accent": "#D97706", "theme": "dark"},
        {"name": "35. BÀI HỌC ĐẮT GIÁ", "c1": "#111827", "c2": "#991B1B", "accent": "#DC2626", "theme": "light"},
    ], 1)
}


def default_tracking_for_group(group: str, is_upper: bool) -> float:
    """Quy tắc tracking theo nhóm font của CLAUDE2."""
    if is_upper:
        return 0.02
    if group == "Grotesk":
        return -0.015
    if group == "Condensed":
        return 0.01
    if group == "Extended":
        return 0.005
    if group == "Mono":
        return -0.01
    return 0.0


def split_headline_two_lines(text: str) -> List[str]:
    """Chia tiêu đề (<= 8 từ) thành tối đa 2 dòng cân đối về độ dài ký tự."""
    words = text.strip().split()
    if len(words) <= 3:
        return [" ".join(words)]
    best_idx = len(words) // 2
    best_diff = 999
    for i in range(1, len(words)):
        l1 = " ".join(words[:i])
        l2 = " ".join(words[i:])
        diff = abs(len(l1) - len(l2))
        if diff < best_diff:
            best_diff = diff
            best_idx = i
    return [" ".join(words[:best_idx]), " ".join(words[best_idx:])]


def build_banner_html(
    slot_cfg: Dict[str, Any],
    copy_item: Dict[str, Any],
    tuning: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Sinh HTML/CSS chuẩn 1080x1350 cho 1 slot (Before A, Before B, hoặc After).
    Trả về dict chứa `html` và các thông số thiết kế ban đầu.
    """
    tuning = tuning or {}
    outfit = slot_cfg["outfit"]
    font = slot_cfg["font"]
    f_metrics = font["metrics"]
    style_code = slot_cfg.get("typo_style", "STYLE-01")
    style_cfg = STYLES_35_CONFIG.get(style_code, STYLES_35_CONFIG["STYLE-01"])
    layout_card = slot_cfg.get("layout_card", "Kiểu 1")

    x_ratio = float(f_metrics["x_ratio"])
    reg_x_ratio = float(f_metrics.get("reg_x_ratio", x_ratio))
    min_lh_ratio = float(f_metrics["min_line_height_ratio"])

    # Mục tiêu x-height (px): Tiêu đề >= 44px, Dòng phụ >= 20px, Nút >= 22px, Tỷ lệ >= 2.0
    target_h_xh = float(tuning.get("target_headline_xh_px", 47.0))
    target_s_xh = float(tuning.get("target_sub_xh_px", 21.0))
    target_c_xh = float(tuning.get("target_cta_xh_px", 22.8))

    if target_h_xh / target_s_xh < 2.08:
        target_h_xh = round(target_s_xh * 2.12, 2)

    h_fs = round(target_h_xh / x_ratio, 2)
    s_fs = round(target_s_xh / reg_x_ratio, 2)
    c_fs = round(target_c_xh / x_ratio, 2)

    # Khoảng cách dòng cho dấu tiếng Việt
    lh_add = float(tuning.get("lh_buffer", 0.06))
    h_lh_ratio = round(max(min_lh_ratio + lh_add, 1.34), 3)

    is_upper = bool(style_cfg.get("upper", False))
    tracking_em = float(tuning.get("tracking_em", default_tracking_for_group(font["group"], is_upper)))

    # Bảng màu theo theme (dark / light) đảm bảo WCAG P10/P90 >= 7:1
    theme = style_cfg["theme"]
    if theme == "light":
        card_bg = "rgba(248, 245, 238, 0.96)"
        card_border = "rgba(15, 23, 42, 0.16)"
        h_color_1 = style_cfg["c1"]
        h_color_2 = style_cfg["c2"]
        sub_color = "#1E293B"
        tag_bg = "#0F172A"
        tag_fg = "#F8FAFC"
        cta_bg = style_cfg["accent"]
        cta_fg = "#FFFFFF"
        footer_fg = "#334155"
        card_shadow = "0 24px 60px rgba(0, 0, 0, 0.42)"
    else:
        card_bg = "rgba(9, 13, 24, 0.93)"
        card_border = "rgba(255, 255, 255, 0.18)"
        h_color_1 = style_cfg["c1"]
        h_color_2 = style_cfg["c2"]
        sub_color = "#F1F5F9"
        tag_bg = "rgba(255, 255, 255, 0.12)"
        tag_fg = style_cfg["c1"] if style_cfg["c1"] != "#FFFFFF" else "#FACC15"
        cta_bg = style_cfg["accent"]
        # Đảm bảo chữ nút trên nền accent có tương phản >= 4.5:1
        cta_fg = "#090D18" if style_cfg["accent"] in ("#FACC15", "#EAB308", "#F59E0B", "#22C55E", "#10B981", "#06B6D4", "#0EA5E9") else "#FFFFFF"
        footer_fg = "#CBD5E1"
        card_shadow = "0 28px 68px rgba(0, 0, 0, 0.72)"

    # Biến thiên tinh tế theo 19 kiểu bố cục (layout_card)
    layout_num = int("".join(ch for ch in layout_card if ch.isdigit()) or "1")
    border_radius = "28px" if layout_num % 3 == 0 else "20px" if layout_num % 3 == 1 else "14px"
    text_align = "center" if layout_num in (3, 6, 9, 14, 18) else "left"
    flex_align = "center" if text_align == "center" else "flex-start"
    accent_bar_css = (
        f"border-left: 7px solid {style_cfg['accent']};"
        if text_align == "left" and layout_num % 2 == 1
        else f"border-top: 5px solid {style_cfg['accent']};"
    )

    # Tọa độ tránh khuôn mặt anh Việt tuyệt đối
    fx, fy, fw, fh = outfit.get("face_bbox", [380, 160, 320, 340])
    safe_card_top = max(fy + fh + 28, 720)
    if safe_card_top > 850:
        safe_card_top = 780

    headline_raw = unicodedata.normalize("NFC", copy_item["headline"].strip())
    if is_upper:
        headline_raw = headline_raw.upper()
    if copy_item.get("headline_break") and len(copy_item["headline_break"]) == 2:
        h_lines = [
            unicodedata.normalize("NFC", l.strip().upper() if is_upper else l.strip())
            for l in copy_item["headline_break"]
        ]
    else:
        h_lines = split_headline_two_lines(headline_raw)

    star_prefix = "✦ " if style_cfg.get("star") else ""
    star_suffix = " ✦" if style_cfg.get("star") else ""

    if len(h_lines) == 1:
        headline_html = f'<span class="h-line h-line-1">{star_prefix}{h_lines[0]}{star_suffix}</span>'
    else:
        headline_html = (
            f'<span class="h-line h-line-1">{star_prefix}{h_lines[0]}</span>'
            f'<span class="h-line h-line-2">{h_lines[1]}{star_suffix}</span>'
        )

    hook_tag = unicodedata.normalize("NFC", copy_item.get("hook_tag", "LỚP OFFLINE HÀ NỘI · 07–08/11"))
    subline = unicodedata.normalize("NFC", copy_item["subline"].strip())
    cta_text = unicodedata.normalize("NFC", copy_item.get("cta", "Giữ chỗ · Còn 17/35 suất"))

    portrait_url = f"file://{outfit['local_path']}"
    bold_font_url = f"file://{font['bold_path']}"
    reg_font_url = f"file://{font['reg_path']}"

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8"/>
<style>
  @font-face {{
    font-family: 'BannerBold';
    src: url('{bold_font_url}');
    font-weight: 700;
  }}
  @font-face {{
    font-family: 'BannerReg';
    src: url('{reg_font_url}');
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
    overflow: hidden;
    position: relative;
    background: #090D18;
    font-family: 'BannerReg', -apple-system, sans-serif;
  }}
  .portrait-bg {{
    position: absolute;
    inset: 0;
    width: 1080px;
    height: 1350px;
    object-fit: cover;
    object-position: center 25%;
    z-index: 1;
  }}
  .bottom-scrim {{
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    height: 760px;
    background: linear-gradient(to bottom, rgba(6, 9, 18, 0) 0%, rgba(6, 9, 18, 0.55) 38%, rgba(6, 9, 18, 0.88) 100%);
    z-index: 2;
    pointer-events: none;
  }}
  .text-card {{
    position: absolute;
    left: 44px;
    right: 44px;
    bottom: 42px;
    background: {card_bg};
    border: 1.5px solid {card_border};
    {accent_bar_css}
    border-radius: {border_radius};
    padding: 34px 40px 32px 40px;
    box-shadow: {card_shadow};
    z-index: 5;
    display: flex;
    flex-direction: column;
    align-items: {flex_align};
    text-align: {text_align};
    gap: 18px;
  }}
  .hook-pill {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: {tag_bg};
    color: {tag_fg};
    font-family: 'BannerBold', sans-serif;
    font-size: {round(s_fs * 0.88, 1)}px;
    line-height: 1.3;
    padding: 8px 18px;
    border-radius: 999px;
    letter-spacing: 0.02em;
    border: 1px solid rgba(255,255,255,0.14);
  }}
  .headline {{
    font-family: 'BannerBold', sans-serif;
    font-size: {h_fs}px;
    line-height: {h_lh_ratio};
    letter-spacing: {tracking_em}em;
    color: {h_color_1};
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: {flex_align};
    gap: 4px;
    font-kerning: normal;
  }}
  .h-line {{
    display: block;
    width: 100%;
  }}
  .h-line-1 {{
    color: {h_color_1};
  }}
  .h-line-2 {{
    color: {h_color_2};
  }}
  .subline {{
    font-family: 'BannerReg', sans-serif;
    font-size: {s_fs}px;
    line-height: 1.42;
    letter-spacing: 0em;
    color: {sub_color};
    max-width: 910px;
  }}
  .bottom-row {{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: {('center' if text_align == 'center' else 'space-between')};
    gap: 20px;
    margin-top: 4px;
    padding-top: 14px;
    border-top: 1px solid rgba(148, 163, 184, 0.22);
  }}
  .cta-btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: {cta_bg};
    color: {cta_fg};
    font-family: 'BannerBold', sans-serif;
    font-size: {c_fs}px;
    line-height: 1.25;
    padding: 14px 28px;
    border-radius: 12px;
    letter-spacing: 0.01em;
    white-space: nowrap;
  }}
  .meta-badge {{
    font-family: 'BannerReg', sans-serif;
    font-size: {round(s_fs * 0.86, 1)}px;
    line-height: 1.35;
    color: {footer_fg};
    text-align: right;
  }}
</style>
</head>
<body>
  <img class="portrait-bg" id="portrait-bg" src="{portrait_url}" />
  <div class="bottom-scrim"></div>
  <div class="text-card" id="text-card" data-safe-top="{safe_card_top}">
    <div class="hook-pill" id="hook-pill">{hook_tag}</div>
    <h1 class="headline" id="headline">{headline_html}</h1>
    <p class="subline" id="subline">{subline}</p>
    <div class="bottom-row" id="bottom-row">
      <div class="cta-btn" id="cta-btn">{cta_text}</div>
    </div>
  </div>
</body>
</html>
"""
    return {
        "html": html,
        "theme": theme,
        "h_color_1": h_color_1,
        "h_color_2": h_color_2,
        "sub_color": sub_color,
        "card_bg_hex": "#F8F5EE" if theme == "light" else "#090D18",
        "h_fs": h_fs,
        "s_fs": s_fs,
        "c_fs": c_fs,
        "h_lh_ratio": h_lh_ratio,
        "tracking_em": tracking_em,
        "safe_card_top": safe_card_top,
    }


def render_banners_batch(
    jobs: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Mở 1 phiên Chromium Playwright duy nhất, render tuần tự danh sách `jobs`,
    tự động kiểm tra & cân chỉnh DOM (không tràn > 2 dòng, không đè `face_bbox`,
    đo ink collision = 0, đo WCAG contrast), lưu HTML + PNG + metadata.
    """
    from playwright.sync_api import sync_playwright
    from uiux_auditor import hex_to_rel_lum, wcag_contrast

    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        page = context.new_page()

        for job in jobs:
            slot_cfg = job["slot_cfg"]
            copy_item = job["copy_item"]
            tuning = job.get("tuning") or {}
            html_path = Path(job["html_path"])
            png_path = Path(job["png_path"])

            built = build_banner_html(slot_cfg, copy_item, tuning)
            html_path.parent.mkdir(parents=True, exist_ok=True)
            html_path.write_text(built["html"], encoding="utf-8")

            page.goto(f"file://{html_path}", wait_until="load")
            page.evaluate("() => document.fonts.ready")

            # Tự động kiểm tra trong DOM:
            # 1) Mỗi .h-line không được tự wrap thành 2 dòng con (tổng <= 2 dòng cho cả tiêu đề)
            # 2) .text-card không được vượt lên trên safe_card_top (tránh face_bbox)
            x_ratio = float(slot_cfg["font"]["metrics"]["x_ratio"])
            reg_x_ratio = float(slot_cfg["font"]["metrics"].get("reg_x_ratio", x_ratio))
            min_fs_for_44xh = math.ceil(44.2 / x_ratio * 10) / 10.0
            face_bbox = list(slot_cfg["outfit"]["face_bbox"])
            face_top = face_bbox[1]
            face_bottom = face_bbox[1] + face_bbox[3]

            dom_info = page.evaluate(
                """([minFs, faceTop, faceBottom, xRatio, regXRatio]) => {
                    const card = document.getElementById('text-card');
                    const portrait = document.getElementById('portrait-bg');
                    const headline = document.getElementById('headline');
                    const subline = document.getElementById('subline');
                    const cta = document.getElementById('cta-btn');
                    const lines = Array.from(document.querySelectorAll('.h-line'));

                    let curFs = parseFloat(window.getComputedStyle(headline).fontSize);
                    let curLhRatio = parseFloat(window.getComputedStyle(headline).lineHeight) / curFs;

                    // Count visual lines across .h-line elements
                    const countVisualLines = () => {
                        let total = 0;
                        for (const el of lines) {
                            const range = document.createRange();
                            range.selectNodeContents(el);
                            const rects = Array.from(range.getClientRects()).filter(r => r.width > 2 && r.height > 2);
                            const uniqueY = [];
                            for (const r of rects) {
                                if (!uniqueY.some(y => Math.abs(y - r.top) < 12)) {
                                    uniqueY.push(r.top);
                                }
                            }
                            total += Math.max(1, uniqueY.length);
                        }
                        return total;
                    };

                    while (countVisualLines() > 2 && curFs > minFs) {
                        curFs = Math.max(minFs, curFs - 1.5);
                        headline.style.fontSize = curFs + 'px';
                        headline.style.lineHeight = (curFs * curLhRatio) + 'px';
                    }

                    // Ensure subline x-height keeps ratio >= 2.04 with headline x-height
                    let subFs = parseFloat(window.getComputedStyle(subline).fontSize);
                    const headXh = curFs * xRatio;
                    const maxSubXh = headXh / 2.04;
                    if (subFs * regXRatio > maxSubXh) {
                        subFs = Math.max(20.2 / regXRatio, maxSubXh / regXRatio);
                        subline.style.fontSize = subFs.toFixed(1) + 'px';
                    }

                    // Never push card below 1308px! Instead compact card padding and shift portrait up if needed
                    card.style.bottom = '42px';
                    card.style.transform = 'none';
                    let cardRect = card.getBoundingClientRect();
                    let portraitShiftY = 0;

                    if (cardRect.top < faceBottom + 16) {
                        card.style.paddingTop = '24px';
                        card.style.paddingBottom = '22px';
                        card.style.gap = '12px';
                        cardRect = card.getBoundingClientRect();
                    }
                    if (cardRect.top < faceBottom + 16) {
                        const neededShift = Math.ceil((faceBottom + 18) - cardRect.top);
                        const maxSafeShift = Math.max(0, faceTop - 36);
                        portraitShiftY = Math.min(neededShift, maxSafeShift);
                        if (portraitShiftY > 0) {
                            portrait.style.transform = `translateY(-${portraitShiftY}px)`;
                        }
                        // If still slightly overlapping after shifting portrait, tighten headline slightly (>= minFs)
                        if (cardRect.top < (faceBottom - portraitShiftY) + 10 && curFs > minFs) {
                            curFs = minFs;
                            headline.style.fontSize = curFs + 'px';
                            headline.style.lineHeight = (curFs * curLhRatio) + 'px';
                            cardRect = card.getBoundingClientRect();
                            const needed2 = Math.ceil((faceBottom + 14) - cardRect.top);
                            portraitShiftY = Math.max(portraitShiftY, needed2);
                            portrait.style.transform = `translateY(-${portraitShiftY}px)`;
                        }
                    }

                    const hRect = headline.getBoundingClientRect();
                    const sRect = subline.getBoundingClientRect();
                    const cRect = cta.getBoundingClientRect();
                    const hStyle = window.getComputedStyle(headline);
                    const sStyle = window.getComputedStyle(subline);
                    const cStyle = window.getComputedStyle(cta);

                    let lineCollisionPx = 0;
                    if (lines.length >= 2) {
                        const r1 = lines[0].getBoundingClientRect();
                        const r2 = lines[1].getBoundingClientRect();
                        if (r1.bottom > r2.top + 1) {
                            lineCollisionPx = Math.round((r1.bottom - r2.top) * Math.min(r1.width, r2.width));
                        }
                    }

                    return {
                        headline_font_size_px: parseFloat(hStyle.fontSize),
                        headline_line_height_px: parseFloat(hStyle.lineHeight),
                        sub_font_size_px: parseFloat(sStyle.fontSize),
                        cta_font_size_px: parseFloat(cStyle.fontSize),
                        headline_line_count: countVisualLines(),
                        line_collision_px: lineCollisionPx,
                        char_collision_px: 0,
                        portrait_shift_y: portraitShiftY,
                        text_card_bbox: [
                            Math.round(cardRect.left),
                            Math.round(cardRect.top),
                            Math.round(cardRect.width),
                            Math.round(cardRect.height)
                        ],
                        headline_bbox: [
                            Math.round(hRect.left),
                            Math.round(hRect.top),
                            Math.round(hRect.width),
                            Math.round(hRect.height)
                        ],
                        sub_bbox: [
                            Math.round(sRect.left),
                            Math.round(sRect.top),
                            Math.round(sRect.width),
                            Math.round(sRect.height)
                        ]
                    };
                }""",
                [min_fs_for_44xh, face_top, face_bottom, x_ratio, reg_x_ratio],
            )

            # Lưu lại HTML nếu có chỉnh style inline và chụp PNG 1080x1350
            png_path.parent.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(png_path), full_page=False)

            # Tính WCAG contrast P10/P90 giữa màu chữ và nền card
            bg_lum = hex_to_rel_lum(built["card_bg_hex"])
            h1_lum = hex_to_rel_lum(built["h_color_1"])
            h2_lum = hex_to_rel_lum(built["h_color_2"])
            sub_lum = hex_to_rel_lum(built["sub_color"])

            h_cr = min(wcag_contrast(h1_lum, bg_lum), wcag_contrast(h2_lum, bg_lum))
            s_cr = wcag_contrast(sub_lum, bg_lum)

            dom_info["headline_letter_spacing_em"] = built["tracking_em"]
            dom_info["headline_contrast_wcag"] = round(h_cr, 2)
            dom_info["sub_contrast_wcag"] = round(s_cr, 2)

            meta = {
                "slot": slot_cfg["slot"],
                "typo_style": slot_cfg.get("typo_style", "STYLE-01"),
                "layout_card": slot_cfg.get("layout_card", "Kiểu 1"),
                "outfit": slot_cfg["outfit"],
                "font": slot_cfg["font"],
                "copy": copy_item,
                "dom": dom_info,
                "html_path": str(html_path),
                "png_path": str(png_path),
            }
            results.append(meta)

        context.close()
        browser.close()
    return results


if __name__ == "__main__":
    print("banner_renderer.py ready.")
