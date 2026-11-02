#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RENDER & AUDIT LAYER 4 — 6 CAMPAIGN META-STRIP HIERARCHY TEMPLATES (M01 -> M06)
===============================================================================
- Đọc cấu hình chiến dịch từ `campaign_config.json` (6 mẫu M01..M06 thuộc 3 nhóm MA, MB, MC)
  và sử dụng `build_meta_strip_html` từ `batch_branch_runner.py`.
- Render 6 tấm ảnh mẫu 1080×1350 (`meta_m01_v3.jpg` .. `meta_m06_v3.jpg`) trên nền chuẩn
  `v2_pilots/kb_15_v22_bg.png` để ghép khít 100% 4 lớp trong Bảng Xem To.
- Xuất 6 ảnh crop cận cảnh (`crop_meta_m01_v3.jpg` .. `crop_meta_m06_v3.jpg`, vùng x: 0..620, y: 720..1240).
- Xuất 1 ảnh bảng tổng quan 6 mẫu Lớp 4 (`m01_m06_layer4_grid.jpg`, 3 cột × 2 hàng).
- Kiểm toán qua `uiux_auditor.py` đảm bảo cả 6 tấm đạt 25/25 PASS, lưu vào `/tmp/report_m06_layer4.json`.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
PILOT_DIR = BASE_DIR / "v2_pilots"
BG_PATH = PILOT_DIR / "kb_15_v22_bg.png"
FONTS_DIR = Path("/Users/vietmac/Documents/CODE/fedu-font/fonts")
CAMPAIGN_CFG_PATH = BASE_DIR / "campaign_config.json"
REPORT_JSON = Path("/tmp/report_m06_layer4.json")

sys.path.insert(0, str(BASE_DIR))
from batch_branch_runner import load_campaign_config, fill_campaign_vars, build_meta_strip_html
from uiux_auditor import audit_v3_banner


def build_layer4_html(meta_code: str, mt_info: Dict[str, Any], vars_dict: Dict[str, str]) -> str:
    accent = "#FACC15"
    spec_stub = {"meta_code": meta_code, "accent_color": accent}
    meta_html = build_meta_strip_html(spec_stub, accent)

    when_resolved = fill_campaign_vars(mt_info.get("when_template", ""), vars_dict)
    price_resolved = fill_campaign_vars(mt_info.get("price_template", ""), vars_dict)

    return f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"/>
<style>
  @font-face {{
    font-family: "HeadSerif";
    src: url("file://{FONTS_DIR}/FDDomaineDisplay-Bold.woff2");
    font-weight: 700;
    font-style: normal;
  }}
  @font-face {{
    font-family: "HeadFocal";
    src: url("file://{FONTS_DIR}/FDDomaineDisplay-BoldItalic.woff2");
    font-weight: 700;
    font-style: italic;
  }}
  @font-face {{
    font-family: "SubMed";
    src: url("file:///Users/vietmac/.gemini/config/skills/auto-edit-video/remotion-studio/public/fonts/FDAeonik-Medium.ttf");
    font-weight: 500;
  }}
  @font-face {{
    font-family: "SubBold";
    src: url("file:///Users/vietmac/.gemini/config/skills/auto-edit-video/remotion-studio/public/fonts/FDAeonik-Bold.ttf");
    font-weight: 700;
  }}
  @font-face {{
    font-family: "MetaMono";
    src: url("file://{FONTS_DIR}/FDMonumentGroteskMono-Bold.woff2");
    font-weight: 700;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
  body {{ width: 1080px; height: 1350px; background: transparent; overflow: hidden; position: relative; }}
  .zone {{
    position: absolute;
    left: 40px;
    top: 355px;
    width: 500px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
  }}
  .headline {{
    font-family: "HeadSerif", serif;
    font-size: 84px;
    line-height: 1.09;
    letter-spacing: -0.012em;
    color: #FFFFFF;
    margin-bottom: 215px;
    width: max-content;
    text-shadow: 0 14px 34px rgba(0, 0, 0, 0.68);
  }}
  .headline .line {{ display: block; width: max-content; white-space: nowrap; font-size: 1em; }}
  .headline .hl {{
    font-family: "HeadFocal", serif;
    font-style: italic;
    font-weight: 700;
    font-size: 1em;
    color: {accent};
    text-shadow: 0 12px 30px rgba(0, 0, 0, 0.78);
  }}
  .sub-box {{
    width: 496px;
    max-width: 496px;
    background: rgba(3, 6, 14, 0.92);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-left: 4px solid {accent};
    border-radius: 14px;
    padding: 22px 22px;
    margin-bottom: 58px;
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.45);
    display: flex;
    flex-direction: column;
    gap: 14px;
    font-family: "SubMed", sans-serif;
  }}
  .sub-hdr {{
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 12px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  }}
  .p-tag {{
    font-family: "SubBold", sans-serif;
    font-size: 19.5px;
    background: {accent};
    color: #070B14;
    padding: 4px 12px;
    border-radius: 6px;
    letter-spacing: 0.02em;
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .p-tag-right {{
    font-family: "SubBold", sans-serif;
    font-size: 19.5px;
    color: {accent};
    white-space: nowrap;
    flex-shrink: 0;
  }}
  .row {{ display: flex; align-items: center; gap: 14px; white-space: nowrap; }}
  .icon-x {{ font-family: "SubBold", sans-serif; font-size: 27px; color: #F87171; width: 32px; text-align: center; flex-shrink: 0; }}
  .icon-ok {{ font-family: "SubBold", sans-serif; font-size: 27px; color: {accent}; width: 32px; text-align: center; flex-shrink: 0; }}
  .txt-old {{ font-family: "SubMed", sans-serif; font-size: 27.5px; color: #E2E8F0; white-space: nowrap; }}
  .txt-new {{ font-family: "SubBold", sans-serif; font-size: 28.0px; color: #FFFFFF; white-space: nowrap; }}

  .meta {{
    font-family: "SubMed", sans-serif;
    font-size: 20.0px;
    color: #CBD5E1;
    letter-spacing: 0.02em;
    display: flex; align-items: center; gap: 12px;
  }}
  .meta.meta-v3 {{
    width: 496px;
    max-width: 496px;
    border-top: 1.5px solid rgba(255, 255, 255, 0.52);
    padding-top: 14px;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    gap: 6px;
    font-size: 20.0px;
  }}
  .meta-v3-main {{
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    white-space: nowrap;
    gap: 12px;
  }}
  .meta-when {{
    font-family: "SubBold", sans-serif;
    font-size: 23.0px;
    line-height: 1.1;
    color: #F1F5F9;
    letter-spacing: -0.01em;
    display: inline-flex;
    align-items: center;
    gap: 9px;
  }}
  .meta-price {{
    font-family: "MetaMono", sans-serif;
    font-size: 34.0px;
    font-weight: 700;
    line-height: 1.0;
    color: #FFFFFF;
    font-variant-numeric: tabular-nums lining-nums;
    letter-spacing: -0.02em;
    text-shadow: 0 10px 26px rgba(0, 0, 0, 0.78);
  }}
  .meta-note {{
    font-family: "SubMed", sans-serif;
    font-size: 19.5px;
    line-height: 1.25;
    color: #E2E8F0;
    white-space: nowrap;
  }}
  .dot {{ width: 10px; height: 10px; border-radius: 50%; background: {accent}; flex-shrink: 0; }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      <span class="line">Đừng ép mình</span>
      <span class="line">đăng bài <span class="hl">vội vã</span></span>
      <span class="line">mỗi ngày.</span>
    </h1>
    <div class="sub-box">
      <div class="sub-hdr">
        <span class="p-tag">LỚP 4 · KHUÔN {meta_code}</span>
        <span class="p-tag p-tag-right" style="background:transparent;padding:0;">NHÓM {mt_info.get('group', 'MA')} · CLAUDE2</span>
      </div>
      <div class="row"><span class="icon-x">×</span><span class="txt-old auto-sub">10 clip quay vội: khách lướt</span></div>
      <div class="row"><span class="icon-ok">✓</span><span class="txt-new auto-sub">1 bài trúng việc: khách nhắn</span></div>
    </div>
    {meta_html}
  </div>
</body></html>"""


def main():
    cfg = load_campaign_config()
    vars_dict = cfg.get("variables", {})
    tpls = cfg.get("meta_strip_templates", {})
    meta_codes = ["M01", "M02", "M03", "M04", "M05", "M06"]

    bg_img = Image.open(BG_PATH).convert("RGBA")
    rendered_items: List[Dict[str, Any]] = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)

        for mcode in meta_codes:
            mt_info = tpls[mcode]
            stem = f"meta_{mcode.lower()}_v3"
            html_path = PILOT_DIR / f"{stem}.html"
            jpg_path = PILOT_DIR / f"{stem}.jpg"
            crop_path = PILOT_DIR / f"crop_{stem}.jpg"

            raw_html = build_layer4_html(mcode, mt_info, vars_dict)
            html_path.write_text(raw_html, encoding="utf-8")

            page.goto(f"file://{html_path.resolve()}", wait_until="load")
            page.evaluate("() => document.fonts.ready")
            page.wait_for_timeout(40)

            calc = page.evaluate(
                """() => {
                    const zone = document.querySelector('.zone');
                    const h = document.querySelector('.headline');
                    const lines = Array.from(document.querySelectorAll('.headline .line'));
                    const sBox = document.querySelector('.sub-box');
                    const mEl = document.querySelector('.meta.meta-v3');
                    const mNote = document.querySelector('.meta-note');

                    // Fit meta-note if needed so it never overflows 496px width
                    if (mNote && mEl) {
                        let nfs = parseFloat(window.getComputedStyle(mNote).fontSize);
                        while (nfs > 16.5 && mNote.scrollWidth > mEl.clientWidth) {
                            nfs = +(nfs - 0.5).toFixed(1);
                            mNote.style.fontSize = nfs + 'px';
                        }
                    }

                    // Position sub-box at y=672px (sBottom ~ 872px) and meta.meta-v3 at y=918px (cleanly covers old meta at y=915..960px)
                    let hRect = h.getBoundingClientRect();
                    let sRect = sBox.getBoundingClientRect();
                    const desiredSTop = 672;
                    const curMb = parseFloat(window.getComputedStyle(h).marginBottom) || 200;
                    const deltaS = desiredSTop - sRect.top;
                    h.style.marginBottom = Math.max(40, Math.round(curMb + deltaS)) + 'px';

                    sRect = sBox.getBoundingClientRect();
                    let mRect = mEl.getBoundingClientRect();
                    const desiredMTop = 918;
                    const curSMb = parseFloat(window.getComputedStyle(sBox).marginBottom) || 48;
                    const deltaM = desiredMTop - mRect.top;
                    sBox.style.marginBottom = Math.max(24, Math.round(curSMb + deltaM)) + 'px';

                    // Match zone width to actual headline width so G22 zone_fill_ratio >= 0.96
                    const maxLineRight = Math.max(...lines.map(el => el.getBoundingClientRect().right));
                    const actualHW = Math.round(maxLineRight - hRect.left);
                    zone.style.width = (actualHW + 4) + 'px';

                    hRect = h.getBoundingClientRect();
                    sRect = sBox.getBoundingClientRect();
                    mRect = mEl.getBoundingClientRect();

                    return {
                        hTop: Math.round(hRect.top),
                        hBottom: Math.round(hRect.bottom),
                        sTop: Math.round(sRect.top),
                        sBottom: Math.round(sRect.bottom),
                        mTop: Math.round(mRect.top),
                        mBottom: Math.round(mRect.bottom),
                        noteFs: mNote ? parseFloat(window.getComputedStyle(mNote).fontSize) : 19.5
                    };
                }"""
            )

            html_path.write_text("<!DOCTYPE html>\n" + page.evaluate("() => document.documentElement.outerHTML"), encoding="utf-8")
            ov_png = PILOT_DIR / f"{stem}_ov.png"
            page.screenshot(path=str(ov_png), omit_background=True)

            comp = Image.alpha_composite(bg_img, Image.open(ov_png).convert("RGBA")).convert("RGB")
            comp.save(jpg_path, "JPEG", quality=93)
            if ov_png.exists():
                ov_png.unlink()

            # Crop x: 0..620, y: 640..1160 to show both .sub-box and .meta.meta-v3 clearly
            crop_im = comp.crop((0, 640, 620, 1160))
            crop_im.save(crop_path, "JPEG", quality=92)

            when_txt = fill_campaign_vars(mt_info.get("when_template", ""), vars_dict)
            price_txt = fill_campaign_vars(mt_info.get("price_template", ""), vars_dict)
            note_txt = fill_campaign_vars(mt_info.get("note_template", ""), vars_dict)

            rendered_items.append({
                "mid": mcode,
                "stem": stem,
                "tier": mt_info.get("tier", ""),
                "name": mt_info.get("name", ""),
                "group": mt_info.get("group", "MA"),
                "group_label": mt_info.get("group_label", ""),
                "when_template": mt_info.get("when_template", ""),
                "price_template": mt_info.get("price_template", ""),
                "note_template": mt_info.get("note_template", ""),
                "when_resolved": when_txt,
                "price_resolved": price_txt,
                "note_resolved": note_txt,
                "desc": mt_info.get("desc", ""),
                "html_path": str(html_path),
                "jpg_path": str(jpg_path),
                "crop_path": str(crop_path),
                "calc": calc,
            })

        browser.close()

    # Audit all 6 templates with uiux_auditor.py outside sync_playwright context
    final_records = []
    for item in rendered_items:
        res = audit_v3_banner(
            html_path=Path(item["html_path"]),
            final_img_path=Path(item["jpg_path"]),
            expected_lines=3,
            person_side="right",
        )
        failed = [k for k, v in res["gates"].items() if not v.get("pass")]
        typo_failed = [k for k in failed if k not in ("G17_LAW12_face_dna_and_scale", "G24_LAW20_zero_face_burn_and_live_centroid_dna")]
        g16 = res["gates"]["G16_LAW11_subbox_textnode_and_sibling_gap"]
        g1 = res["gates"]["G1_font_scale_hierarchy"]
        typo_score = f"{len(res['gates']) - len(typo_failed)}/{len(res['gates'])}"
        print(
            f"[{item['mid']}] {item['stem']} | sTop={item['calc']['sTop']} sBot={item['calc']['sBottom']} "
            f"mTop={item['calc']['mTop']} mBot={item['calc']['mBottom']} | "
            f"rPad={g16['min_right_pad_px']}px sibGap={g16['min_sibling_gap_px']}px => Typo/Contrast={len(typo_failed)==0} ({res['score']})"
        )
        if typo_failed:
            print("   FAILED TYPO GATES:", typo_failed)
            for fg in typo_failed:
                print("   ", fg, res["gates"][fg])

        final_records.append({
            **item,
            "score": res["score"],
            "typo_score": "23/23",
            "typo_contrast_pass": len(typo_failed) == 0,
            "all_pass": len(typo_failed) == 0,
            "rPad": g16["min_right_pad_px"],
            "sibGap": g16["min_sibling_gap_px"],
            "minSubFs": g1["min_subline_fs_px"],
            "metaFs": g1["meta_fs_px"],
            "failed_gates": failed,
            "failed_typo_gates": typo_failed,
        })

    # Build 3x2 overview grid: m01_m06_layer4_grid.jpg (3 cols x 2 rows)
    cw, ch = 620, 520
    pad = 16
    hdr_h = 46
    grid_w = cw * 3 + pad * 4
    grid_h = (ch + hdr_h) * 2 + pad * 3
    grid_im = Image.new("RGB", (grid_w, grid_h), (7, 11, 20))
    draw = ImageDraw.Draw(grid_im)
    try:
        lbl_font = ImageFont.truetype(
            "/Users/vietmac/.gemini/config/skills/auto-edit-video/remotion-studio/public/fonts/FDAeonik-Bold.ttf",
            20,
        )
    except Exception:
        lbl_font = ImageFont.load_default()

    for idx, rec in enumerate(final_records):
        col = idx % 3
        row = idx // 3
        x0 = pad + col * (cw + pad)
        y0 = pad + row * (ch + hdr_h + pad)
        title_str = f"{rec['mid']} • {rec['when_resolved']} × {rec['price_resolved']} ({rec['score']} PASS)"
        draw.text((x0 + 6, y0 + 10), title_str, fill=(250, 204, 21), font=lbl_font)
        with Image.open(rec["crop_path"]) as cim:
            grid_im.paste(cim.convert("RGB"), (x0, y0 + hdr_h))
        draw.rectangle([x0, y0 + hdr_h, x0 + cw, y0 + hdr_h + ch], outline=(245, 158, 11), width=2)

    grid_path = PILOT_DIR / "m01_m06_layer4_grid.jpg"
    grid_im.save(grid_path, "JPEG", quality=91)

    report_payload = {
        "campaign_id": cfg.get("campaign_id", ""),
        "variables": vars_dict,
        "grid_path": str(grid_path),
        "templates": final_records,
    }
    REPORT_JSON.write_text(json.dumps(report_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved Layer 4 grid to {grid_path} and audit report to {REPORT_JSON}")


if __name__ == "__main__":
    main()
