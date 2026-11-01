#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTO BANNER ENGINE V3.0 — SELF-LEARNING K4 AD BANNER GENERATOR & VERIFIER
=========================================================================
Đóng gói toàn bộ quy trình "Vừa Sửa Vừa Duyệt" đã chốt từ KB_01 và KB_15:
1. Đọc Sổ cái tự học `banner_laws.json` (Bước 0 bắt buộc).
2. Nhận đầu vào kịch bản (Headline 3 dòng + Từ khóa vàng + Cặp đối lập PA2 + Câu đúc kết PA3).
3. Tự động xuất song song 2 Phương Án Chuẩn Đã Duyệt:
   - Phương Án 2 (PA2_HAI_VE): FDFinancierDisplay-Bold (cỡ chuẩn 83px, tự co nhẹ nếu dòng dài để không bao giờ rớt chữ) + Hộp đối lập × / ✓.
   - Phương Án 3 (PA3_TRICH_DAN): FDNoeDisplay-Bold (cỡ chuẩn 77px) + Eyebrow tĩnh + Khối trích dẫn nền tối sâu viền đỉnh vàng.
4. Chạy cổng kiểm định `uiux_auditor.py` (13 Cổng Thực Chiến G1..G13).
5. Hỗ trợ `--learn` để ghi trực tiếp phản hồi sửa mới của anh Việt vào `banner_laws.json`.
"""

import argparse
import datetime
import json
from pathlib import Path
from typing import Dict, Any, List
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

from uiux_auditor import audit_v3_banner, load_banner_laws, LAWS_PATH

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
PILOT_DIR = BASE_DIR / "v2_pilots"
FONT_DIR = Path("/Users/vietmac/Documents/CODE/fedu-font/fonts")
AEONIK_DIR = Path("/Users/vietmac/.gemini/config/skills/auto-edit-video/remotion-studio/public/fonts")


def record_new_law(source_banner: str, user_feedback: str, rule: str, gate_id: str = "CUSTOM_LAW") -> Dict[str, Any]:
    """Ghi nhận xét/chỉ đạo sửa mới của anh Việt vào Sổ cái tự học `banner_laws.json`."""
    data = load_banner_laws()
    laws = data.setdefault("learned_laws", [])
    new_idx = len(laws) + 1
    law_entry = {
        "law_id": f"LAW_{new_idx:02d}_AUTO_LEARNED",
        "learned_at": datetime.datetime.now().isoformat(),
        "source_banner": source_banner,
        "user_feedback": user_feedback,
        "rule": rule,
        "gate_id": gate_id,
    }
    laws.append(law_entry)
    data["updated_at"] = datetime.datetime.now().isoformat()
    LAWS_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return law_entry


def build_pa2_html(
    headline_lines: List[str],
    highlight_kw: str,
    row_old: str,
    row_new: str,
    meta_text: str = "Offline Hà Nội · 07–08/11",
    zone_left: int = 48,
    zone_width: int = 485,
) -> str:
    rendered_lines = []
    for line in headline_lines:
        if highlight_kw and highlight_kw in line:
            line_html = line.replace(highlight_kw, f'<span class="hl">{highlight_kw}</span>')
        else:
            line_html = line
        rendered_lines.append(f'<span class="line">{line_html}</span>')
    lines_joined = "\n      ".join(rendered_lines)

    return f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"/>
<style>
  @font-face {{
    font-family: "HeadSerif";
    src: url("file://{FONT_DIR / 'FDFinancierDisplay-Bold.woff2'}");
    font-weight: 700;
  }}
  @font-face {{
    font-family: "SubMed";
    src: url("file://{AEONIK_DIR / 'FDAeonik-Medium.ttf'}");
    font-weight: 500;
  }}
  @font-face {{
    font-family: "SubBold";
    src: url("file://{AEONIK_DIR / 'FDAeonik-Bold.ttf'}");
    font-weight: 700;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
  body {{ width: 1080px; height: 1350px; background: transparent; overflow: hidden; position: relative; }}
  .zone {{
    position: absolute; left: {zone_left}px; top: 190px; width: {zone_width}px; height: 920px;
    display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
  }}
  .headline {{
    font-family: "HeadSerif", serif;
    font-size: 83px;
    line-height: 1.06;
    letter-spacing: -0.012em;
    color: #FFFFFF;
    margin-bottom: 36px;
    text-shadow: 0 12px 32px rgba(0, 0, 0, 0.55);
  }}
  .headline .line {{ display: block; white-space: nowrap; }}
  .headline .hl {{ color: #F59E0B; }}
  .contrast-panel {{
    background: rgba(6, 10, 19, 0.74);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 14px;
    padding: 20px 22px;
    margin-bottom: 42px;
    display: flex;
    flex-direction: column;
    gap: 15px;
  }}
  .row-old {{
    font-family: "SubMed", sans-serif;
    font-size: 29.5px;
    line-height: 1.2;
    color: #94A3B8;
    display: flex; align-items: center; gap: 12px;
    white-space: nowrap;
  }}
  .row-old .icon {{ color: #64748B; font-weight: 700; font-size: 27px; }}
  .divider {{ height: 1px; background: rgba(255, 255, 255, 0.12); width: 100%; }}
  .row-new {{
    font-family: "SubBold", sans-serif;
    font-size: 30.5px;
    line-height: 1.2;
    color: #FFFFFF;
    display: flex; align-items: center; gap: 12px;
    white-space: nowrap;
  }}
  .row-new .icon {{ color: #F59E0B; font-weight: 800; font-size: 29px; }}
  .meta {{
    font-family: "SubMed", sans-serif;
    font-size: 24px;
    color: #CBD5E1;
    letter-spacing: 0.03em;
    display: flex; align-items: center; gap: 12px;
  }}
  .dot {{ width: 9px; height: 9px; border-radius: 50%; background: #F59E0B; }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      {lines_joined}
    </h1>
    <div class="contrast-panel">
      <div class="row-old"><span class="icon">×</span><span>{row_old}</span></div>
      <div class="divider"></div>
      <div class="row-new"><span class="icon">✓</span><span>{row_new}</span></div>
    </div>
    <div class="meta"><span class="dot"></span><span>{meta_text}</span></div>
  </div>
</body></html>"""


def build_pa3_html(
    eyebrow: str,
    headline_lines: List[str],
    highlight_kw: str,
    sub_line1: str,
    sub_line2_bold: str,
    meta_text: str = "Offline Hà Nội · 07–08/11",
    zone_left: int = 48,
    zone_width: int = 485,
) -> str:
    rendered_lines = []
    for line in headline_lines:
        if highlight_kw and highlight_kw in line:
            line_html = line.replace(highlight_kw, f'<span class="hl">{highlight_kw}</span>')
        else:
            line_html = line
        rendered_lines.append(f'<span class="line">{line_html}</span>')
    lines_joined = "\n      ".join(rendered_lines)

    return f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"/>
<style>
  @font-face {{
    font-family: "HeadSerif";
    src: url("file://{FONT_DIR / 'FDNoeDisplay-Bold.ttf'}");
    font-weight: 700;
  }}
  @font-face {{
    font-family: "SubMed";
    src: url("file://{AEONIK_DIR / 'FDAeonik-Medium.ttf'}");
    font-weight: 500;
  }}
  @font-face {{
    font-family: "SubBold";
    src: url("file://{AEONIK_DIR / 'FDAeonik-Bold.ttf'}");
    font-weight: 700;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
  body {{ width: 1080px; height: 1350px; background: transparent; overflow: hidden; position: relative; }}
  .zone {{
    position: absolute; left: {zone_left}px; top: 190px; width: {zone_width}px; height: 920px;
    display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
  }}
  .eyebrow {{
    font-family: "SubBold", sans-serif;
    font-size: 20px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #94A3B8;
    margin-bottom: 16px;
  }}
  .headline {{
    font-family: "HeadSerif", serif;
    font-size: 77px;
    line-height: 1.08;
    letter-spacing: -0.015em;
    color: #FFFFFF;
    margin-bottom: 36px;
    text-shadow: 0 12px 32px rgba(0, 0, 0, 0.55);
  }}
  .headline .line {{ display: block; white-space: nowrap; }}
  .headline .hl {{ color: #F59E0B; }}
  .dark-callout {{
    display: inline-block;
    background: rgba(5, 9, 18, 0.76);
    border-top: 2px solid rgba(245, 158, 11, 0.65);
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    padding: 20px 22px;
    margin-bottom: 42px;
  }}
  .sub-text {{
    font-family: "SubMed", sans-serif;
    font-size: 30px;
    line-height: 1.42;
    color: #FFFFFF;
    white-space: nowrap;
  }}
  .sub-text strong {{
    font-family: "SubBold", sans-serif;
    color: #F59E0B;
  }}
  .meta {{
    font-family: "SubMed", sans-serif;
    font-size: 24px;
    color: #CBD5E1;
    letter-spacing: 0.03em;
    display: flex; align-items: center; gap: 12px;
  }}
  .dot {{ width: 9px; height: 9px; border-radius: 50%; background: #F59E0B; }}
</style></head>
<body>
  <div class="zone">
    <div class="eyebrow">{eyebrow}</div>
    <h1 class="headline">
      {lines_joined}
    </h1>
    <div class="dark-callout">
      <p class="sub-text">
        {sub_line1}<br/>
        <strong>{sub_line2_bold}</strong>
      </p>
    </div>
    <div class="meta"><span class="dot"></span><span>{meta_text}</span></div>
  </div>
</body></html>"""


def render_and_audit_variant(
    html_code: str,
    bg_path: Path,
    out_html_path: Path,
    out_text_png: Path,
    out_final_jpg: Path,
    zone_width: int = 485,
    expected_lines: int = 3,
    person_side: str = "right",
) -> Dict[str, Any]:
    out_html_path.write_text(html_code, encoding="utf-8")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        page.goto(f"file://{out_html_path.resolve()}", wait_until="networkidle")
        page.evaluate("() => document.fonts.ready")
        # Tự động kiểm tra nếu dòng chữ vượt zone_width thì giảm đồng nhất font-size để tuyệt đối không tràn / không rớt dòng
        adjusted_fs = page.evaluate(
            """([zw]) => {
                const h = document.querySelector('.headline');
                const lines = Array.from(document.querySelectorAll('.headline .line'));
                let fs = parseFloat(window.getComputedStyle(h).fontSize);
                while (fs > 68) {
                    const maxW = Math.max(...lines.map(el => el.scrollWidth));
                    if (maxW <= zw) break;
                    fs -= 1;
                    h.style.fontSize = fs + 'px';
                }
                return fs;
            }""",
            [zone_width],
        )
        # Lưu lại HTML nếu có điều chỉnh cỡ chữ đồng nhất
        if adjusted_fs:
            updated_html = page.content()
            out_html_path.write_text(updated_html, encoding="utf-8")
        page.screenshot(path=str(out_text_png), type="png", omit_background=True)
        browser.close()

    bg_im = Image.open(bg_path).convert("RGBA")
    txt_im = Image.open(out_text_png).convert("RGBA")
    comp_im = Image.alpha_composite(bg_im, txt_im).convert("RGB")
    comp_im.save(out_final_jpg, "JPEG", quality=93)

    audit_res = audit_v3_banner(
        html_path=out_html_path,
        final_img_path=out_final_jpg,
        expected_lines=expected_lines,
        person_side=person_side,
    )
    return audit_res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto Banner Engine V3.0 (PA 2 & PA 3 + Self-Learning Ledger)")
    parser.add_argument("--learn", type=str, help="Ghi nhận xét sửa mới của anh Việt vào Sổ cái banner_laws.json")
    parser.add_argument("--banner", type=str, default="GLOBAL", help="Mã kịch bản liên quan (vd: KB_15, KB_02)")
    parser.add_argument("--rule", type=str, help="Nội dung quy tắc kỹ thuật rút ra từ nhận xét của anh Việt")
    parser.add_argument("--status", action="store_true", help="Hiển thị trạng thái Sổ cái tự học và các khuôn đã duyệt")
    args = parser.parse_args()

    if args.learn:
        rule_text = args.rule or args.learn
        entry = record_new_law(args.banner, args.learn, rule_text)
        print(json.dumps({"recorded_law": entry, "laws_file": str(LAWS_PATH)}, ensure_ascii=False, indent=2))
    else:
        laws = load_banner_laws()
        print(
            json.dumps(
                {
                    "engine": "Auto Banner Engine V3.0",
                    "laws_file": str(LAWS_PATH),
                    "total_learned_laws": len(laws.get("learned_laws", [])),
                    "approved_archetypes": list(laws.get("approved_archetypes", {}).keys()),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
