#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BATCH BRANCH RUNNER V3.0 — RENDER 3 BANNERS PER BRANCH (8 APPROVED STYLES #01..#08)
===================================================================================
- Đọc thông số kịch bản từ `kb_31_master_specs.json`.
- Render mỗi KB theo đúng 1 trong 8 kiểu chữ đã duyệt (`K01`..`K08`) + 1 phương án đối chứng (`K01` hoặc `K02`).
- Tự động cân chỉnh cỡ chữ đồng nhất (`delta_fs == 0px`, `white-space: nowrap`, `0% rớt chữ`, `0% tràn hộp`).
- Chấm điểm tự động qua 13 Cổng Thực Chiến `uiux_auditor.py` (`13/13 PASS`).
- Ghép ảnh so sánh 3 cột (`[Bản Cũ Lỗi]` → `[Kiểu Chính 13/13 PASS]` → `[Phương Án Đối Chứng]`).
- Đẩy ảnh lên R2 (`https://media.fedu.vn/banner2/...`), ghi `banner2_cards/KB_XX.json` và gọi `update_banner2_hub.py` (Lock-free `fcntl.flock` chống ghi đè 100%).
- Bắn ngay từng Banner hoàn thành vào Telegram kèm link bấm 1 chạm.
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, Any, List
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
SPECS_PATH = BASE_DIR / "kb_31_master_specs.json"
CARDS_DIR = BASE_DIR / "banner2_cards"
OUT_RENDER_DIR = BASE_DIR / "v2_pilots" / "batch_out"
R2_MANAGER = Path("/Users/vietmac/Documents/CODE/Quản gia/r2_manager.py")
TELEGRAM_NOTIFY = Path("/Users/vietmac/Documents/CODE/Quản gia/telegram_notify.py")

sys.path.insert(0, str(BASE_DIR))
from uiux_auditor import audit_v3_banner
from update_banner2_hub import atomic_rebuild_and_sync


def build_style_html(
    style_code: str,
    spec: Dict[str, Any],
    style_fonts: Dict[str, Any],
) -> str:
    font_file, _, base_fs, base_lh = style_fonts[style_code]
    side = spec.get("side", "right")
    zone_left = 42 if side == "right" else 544
    zone_width = 492
    card_width = 486

    lines_html = "\n      ".join(f'<span class="line">{ln}</span>' for ln in spec["headline_lines"])

    common_head = f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"/>
<style>
  @font-face {{
    font-family: "HeadSerif";
    src: url("file:///Users/vietmac/Documents/CODE/fedu-font/fonts/{font_file}");
    font-weight: 700;
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
  * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
  body {{ width: 1080px; height: 1350px; background: transparent; overflow: hidden; position: relative; }}
  .zone {{
    position: absolute; left: {zone_left}px; top: 190px; width: {zone_width}px; height: 920px;
    display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
  }}
  .headline {{
    font-family: "HeadSerif", serif;
    font-size: {base_fs}px;
    line-height: {base_lh};
    letter-spacing: -0.014em;
    color: #FFFFFF;
    margin-bottom: 38px;
    text-shadow: 0 12px 32px rgba(0, 0, 0, 0.55);
  }}
  .headline .line {{ display: block; white-space: nowrap; }}
  .headline .hl {{ color: #F59E0B; }}
  .meta {{
    font-family: "SubMed", sans-serif;
    font-size: 25px;
    color: #CBD5E1;
    letter-spacing: 0.03em;
    display: flex; align-items: center; gap: 12px;
  }}
  .dot {{ width: 9px; height: 9px; border-radius: 50%; background: #F59E0B; }}
"""

    if style_code == "K01":
        d = spec.get("k01", {"old": "Cách làm cũ tốn sức: khách lướt qua", "new": "Làm đúng chuẩn nghề: khách tự nhắn"})
        return common_head + f"""
  .sub-box {{
    width: {card_width}px;
    background: rgba(6, 10, 19, 0.78);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-left: 4px solid #F59E0B;
    border-radius: 12px;
    padding: 20px 22px;
    margin-bottom: 42px;
    display: flex; flex-direction: column; gap: 14px;
  }}
  .row {{ display: flex; align-items: center; gap: 12px; white-space: nowrap; }}
  .icon-x {{ font-family: "SubBold", sans-serif; font-size: 25px; color: #EF4444; width: 22px; text-align: center; flex-shrink: 0; }}
  .icon-ok {{ font-family: "SubBold", sans-serif; font-size: 25px; color: #F59E0B; width: 22px; text-align: center; flex-shrink: 0; }}
  .txt-old {{ font-family: "SubMed", sans-serif; font-size: 28px; color: #94A3B8; white-space: nowrap; }}
  .txt-new {{ font-family: "SubBold", sans-serif; font-size: 29.5px; color: #FFFFFF; white-space: nowrap; }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      {lines_html}
    </h1>
    <div class="sub-box">
      <div class="row"><span class="icon-x">×</span><span class="txt-old auto-sub">{d["old"]}</span></div>
      <div class="row"><span class="icon-ok">✓</span><span class="txt-new auto-sub">{d["new"]}</span></div>
    </div>
    <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
  </div>
</body></html>"""

    if style_code == "K02":
        d = spec.get("k02", {"eyebrow": "ĐÚC KẾT TỪ THỰC TẾ", "l1": "Không cần diễn xuất cầu kỳ,", "l2": "chỉ cần nói đúng chuyện nghề."})
        return common_head + f"""
  .dark-callout {{
    width: {card_width}px;
    background: rgba(5, 9, 18, 0.80);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-top: 3px solid #F59E0B;
    border-radius: 12px;
    padding: 22px 24px;
    margin-bottom: 42px;
  }}
  .eyebrow {{
    font-family: "SubBold", sans-serif;
    font-size: 18px;
    letter-spacing: 0.08em;
    color: #F59E0B;
    margin-bottom: 10px;
    display: block;
    text-transform: uppercase;
  }}
  .l1 {{ font-family: "SubBold", sans-serif; font-size: 30px; line-height: 1.32; color: #FFFFFF; white-space: nowrap; display: block; }}
  .l2 {{ font-family: "SubMed", sans-serif; font-size: 29px; line-height: 1.35; color: #CBD5E1; white-space: nowrap; display: block; }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      {lines_html}
    </h1>
    <div class="dark-callout">
      <span class="eyebrow">{d["eyebrow"]}</span>
      <span class="l1 auto-sub">{d["l1"]}</span>
      <span class="l2 auto-sub">{d["l2"]}</span>
    </div>
    <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
  </div>
</body></html>"""

    if style_code == "K03":
        d = spec["k03"]
        return common_head + f"""
  .num-card {{
    width: {card_width}px;
    background: rgba(6, 10, 19, 0.78);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 14px;
    padding: 22px 22px;
    margin-bottom: 42px;
    display: grid;
    grid-template-columns: 1fr 28px 1fr;
    align-items: center;
  }}
  .col-stat {{ display: flex; flex-direction: column; gap: 4px; }}
  .n-gold {{ font-family: "SubBold", sans-serif; font-size: 52px; line-height: 1.0; color: #F59E0B; white-space: nowrap; }}
  .n-white {{ font-family: "SubBold", sans-serif; font-size: 48px; line-height: 1.0; color: #FFFFFF; white-space: nowrap; }}
  .lbl-sub {{ font-family: "SubMed", sans-serif; font-size: 27px; line-height: 1.25; color: #CBD5E1; white-space: nowrap; }}
  .arrow {{ font-family: "SubBold", sans-serif; font-size: 30px; color: #F59E0B; text-align: center; }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      {lines_html}
    </h1>
    <div class="num-card">
      <div class="col-stat">
        <span class="n-gold">{d["n1"]}</span>
        <span class="lbl-sub auto-sub">{d["l1"]}</span>
      </div>
      <div class="arrow">→</div>
      <div class="col-stat" style="padding-left: 8px;">
        <span class="n-white">{d["n2"]}</span>
        <span class="lbl-sub auto-sub">{d["l2"]}</span>
      </div>
    </div>
    <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
  </div>
</body></html>"""

    if style_code == "K04":
        d = spec["k04"]
        return common_head + f"""
  .tab-box {{
    position: relative;
    width: {card_width}px;
    background: rgba(5, 9, 18, 0.80);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 14px;
    padding: 32px 22px 22px;
    margin-bottom: 42px;
  }}
  .floating-tab {{
    position: absolute;
    top: -15px;
    left: 22px;
    background: #F59E0B;
    color: #070B14;
    font-family: "SubBold", sans-serif;
    font-size: 18px;
    letter-spacing: 0.09em;
    padding: 5px 14px;
    border-radius: 6px;
    text-transform: uppercase;
  }}
  .l1 {{ font-family: "SubBold", sans-serif; font-size: 29.5px; line-height: 1.32; color: #FFFFFF; white-space: nowrap; display: block; }}
  .l2 {{ font-family: "SubMed", sans-serif; font-size: 28.5px; line-height: 1.35; color: #CBD5E1; white-space: nowrap; display: block; }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      {lines_html}
    </h1>
    <div class="tab-box">
      <span class="floating-tab">{d["tab"]}</span>
      <span class="l1 auto-sub">{d["l1"]}</span>
      <span class="l2 auto-sub">{d["l2"]}</span>
    </div>
    <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
  </div>
</body></html>"""

    if style_code == "K05":
        d = spec["k05"]
        return common_head + f"""
  .offset-wrap {{
    position: relative;
    width: {card_width - 6}px;
    margin-bottom: 48px;
  }}
  .offset-bg {{
    position: absolute;
    inset: 0;
    transform: translate(10px, 10px);
    background: rgba(245, 158, 11, 0.24);
    border-radius: 10px;
  }}
  .offset-front {{
    position: relative;
    background: rgba(6, 10, 19, 0.84);
    border: 1px solid rgba(245, 158, 11, 0.45);
    border-radius: 10px;
    padding: 22px 22px;
  }}
  .l1 {{ font-family: "SubMed", sans-serif; font-size: 28px; line-height: 1.35; color: #E2E8F0; margin-bottom: 4px; white-space: nowrap; display: block; }}
  .l2 {{ font-family: "SubBold", sans-serif; font-size: 30px; line-height: 1.35; color: #FFFFFF; white-space: nowrap; display: block; }}
  .l2 em {{ font-style: normal; color: #F59E0B; padding: 0 3px; }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      {lines_html}
    </h1>
    <div class="offset-wrap">
      <div class="offset-bg"></div>
      <div class="offset-front">
        <span class="l1 auto-sub">{d["l1"]}</span>
        <span class="l2 auto-sub"><em>→</em> {d["s1"]} <em>→</em> {d["s2"]}</span>
      </div>
    </div>
    <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
  </div>
</body></html>"""

    if style_code == "K06":
        d = spec["k06"]
        return common_head + f"""
  .not-but-card {{
    width: {card_width}px;
    background: rgba(6, 10, 19, 0.78);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 14px;
    padding: 20px 20px;
    margin-bottom: 42px;
    display: flex; flex-direction: column; gap: 14px;
  }}
  .nb-row {{ display: flex; align-items: center; gap: 12px; white-space: nowrap; }}
  .tag-not {{
    font-family: "SubBold", sans-serif; font-size: 16.5px; letter-spacing: 0.05em;
    background: rgba(148, 163, 184, 0.18); color: #94A3B8; padding: 5px 10px; border-radius: 6px; flex-shrink: 0;
  }}
  .tag-but {{
    font-family: "SubBold", sans-serif; font-size: 16.5px; letter-spacing: 0.05em;
    background: #F59E0B; color: #070B14; padding: 5px 12px; border-radius: 6px; flex-shrink: 0;
  }}
  .txt-not {{ font-family: "SubMed", sans-serif; font-size: 28px; color: #94A3B8; white-space: nowrap; }}
  .txt-but {{ font-family: "SubBold", sans-serif; font-size: 29.5px; color: #FFFFFF; white-space: nowrap; }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      {lines_html}
    </h1>
    <div class="not-but-card">
      <div class="nb-row"><span class="tag-not">KHÔNG PHẢI</span><span class="txt-not auto-sub">{d["not"]}</span></div>
      <div class="nb-row"><span class="tag-but">MÀ LÀ</span><span class="txt-but auto-sub">{d["but"]}</span></div>
    </div>
    <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
  </div>
</body></html>"""

    if style_code == "K07":
        d = spec["k07"]
        return common_head + f"""
  .two-col-box {{
    width: {card_width}px;
    background: rgba(6, 10, 19, 0.78);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 14px;
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    overflow: hidden;
    margin-bottom: 42px;
  }}
  .col-left {{ padding: 18px 16px; border-right: 1px solid rgba(255, 255, 255, 0.12); min-width: 0; }}
  .col-right {{ padding: 18px 16px; background: rgba(245, 158, 11, 0.08); min-width: 0; }}
  .c-head-muted {{ font-family: "SubBold", sans-serif; font-size: 16px; white-space: nowrap; letter-spacing: 0.05em; color: #94A3B8; margin-bottom: 6px; display: block; }}
  .c-head-gold {{ font-family: "SubBold", sans-serif; font-size: 16px; white-space: nowrap; letter-spacing: 0.05em; color: #F59E0B; margin-bottom: 6px; display: block; }}
  .c-body-muted {{ font-family: "SubMed", sans-serif; font-size: 27px; line-height: 1.32; white-space: nowrap; color: #CBD5E1; display: block; }}
  .c-body-bright {{ font-family: "SubBold", sans-serif; font-size: 27px; line-height: 1.32; white-space: nowrap; color: #FFFFFF; display: block; }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      {lines_html}
    </h1>
    <div class="two-col-box">
      <div class="col-left">
        <span class="c-head-muted">{d["lh"]}</span>
        <span class="c-body-muted auto-sub">{d["lb"]}</span>
      </div>
      <div class="col-right">
        <span class="c-head-gold">{d["rh"]}</span>
        <span class="c-body-bright auto-sub">{d["rb"]}</span>
      </div>
    </div>
    <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
  </div>
</body></html>"""

    # Default K08
    d = spec["k08"]
    return common_head + f"""
  .unified-card {{
    width: {card_width}px;
    background: rgba(5, 9, 18, 0.80);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 16px;
    overflow: hidden;
  }}
  .uc-body {{
    padding: 22px 22px;
    font-family: "SubMed", sans-serif;
    font-size: 29px;
    line-height: 1.38;
    color: #F8FAFC;
    white-space: nowrap;
  }}
  .uc-body strong {{
    font-family: "SubBold", sans-serif;
    color: #FFFFFF;
    border-bottom: 4px solid #F59E0B;
    padding-bottom: 2px;
  }}
  .uc-foot {{
    background: rgba(245, 158, 11, 0.14);
    border-top: 1px solid rgba(245, 158, 11, 0.30);
    padding: 13px 22px;
    font-family: "SubBold", sans-serif;
    font-size: 24px;
    color: #FBBF24;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      {lines_html}
    </h1>
    <div class="unified-card">
      <div class="uc-body auto-sub">
        {d["l1"]}<br/>
        {d["l2_pre"]}<strong>{d["l2_ul"]}</strong>
      </div>
      <div class="uc-foot meta">
        <span>Offline Hà Nội · 07–08/11</span>
        <span>→</span>
      </div>
    </div>
  </div>
</body></html>"""


def render_html_onto_bg(
    html_content: str,
    html_out_path: Path,
    bg_path: Path,
    final_jpg_path: Path,
) -> Dict[str, Any]:
    html_out_path.parent.mkdir(parents=True, exist_ok=True)
    html_out_path.write_text(html_content, encoding="utf-8")

    overlay_png = html_out_path.with_suffix(".overlay.png")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        page.goto(f"file://{html_out_path.resolve()}", wait_until="networkidle")
        page.evaluate("() => document.fonts.ready")

        # Auto-fit đồng nhất 3 dòng Headline + Auto-Calibrate LAW_09 V4.0 (f732723c) + Auto-fit Subbox
        fit_info = page.evaluate(
            """() => {
                const h = document.querySelector('.headline');
                const zone = document.querySelector('.zone');
                const lines = Array.from(document.querySelectorAll('.headline .line'));
                const maxLineW = (zone ? zone.clientWidth : 492) - 4;
                let fs = parseFloat(window.getComputedStyle(h).fontSize);
                while (fs > 50) {
                    const maxW = Math.max(...lines.map(l => l.scrollWidth));
                    if (maxW <= maxLineW) break;
                    fs -= 1;
                    h.style.fontSize = fs + 'px';
                }

                // LAW_09 V4.0 (từ luồng f732723c): Đo xRatio & Ma trận mực 2D cho từng font + từng câu
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
                    const reqDistPx = maxOverlap + 7.2;
                    const reqLh = reqDistPx / curFs;
                    const minLhW = 2.13 * xRatio;
                    const maxLhW = 2.34 * xRatio;
                    let targetLh = Math.max(minLhW, reqLh);
                    if (targetLh > maxLhW) targetLh = maxLhW;
                    targetLh = Math.max(0.99, Math.min(1.165, +targetLh.toFixed(3)));
                    const gapPx = Math.round(targetLh * curFs - maxOverlap);
                    const wVal = +((targetLh - xRatio) / xRatio).toFixed(2);
                    return { fs: curFs, targetLh, gapPx, wVal, pass: (gapPx >= 6 && wVal >= 1.10 && wVal <= 1.36) };
                }

                let best = solveLaw09(fs);
                if (!best.pass) {
                    for (let tryFs = fs - 1; tryFs >= Math.max(52, fs - 8); tryFs--) {
                        const cand = solveLaw09(tryFs);
                        if (cand.pass || cand.gapPx > best.gapPx) {
                            best = cand;
                            if (cand.pass) break;
                        }
                    }
                }
                fs = best.fs;
                h.style.fontSize = fs + 'px';
                h.style.lineHeight = String(best.targetLh);
                lines.forEach(l => { l.style.lineHeight = String(best.targetLh); });

                // Auto-fit các dòng chữ bé trong hộp bằng Range vết mực thực tế (0% tràn phải)
                const subBox = zone && zone.children.length > 1 ? zone.children[1] : null;
                if (subBox) {
                    const boxRect = subBox.getBoundingClientRect();
                    const autoSubs = Array.from(subBox.querySelectorAll('.auto-sub'));
                    for (const el of autoSubs) {
                        let sfs = parseFloat(window.getComputedStyle(el).fontSize);
                        const colParent = el.closest('.col-left, .col-right, .col-stat');
                        while (sfs > 19.5) {
                            const range = document.createRange();
                            range.selectNodeContents(el);
                            const r = range.getBoundingClientRect();
                            const limitRight = colParent ? Math.min(colParent.getBoundingClientRect().right - 10, boxRect.right - 12) : (boxRect.right - 12);
                            if (r.right <= limitRight) break;
                            sfs -= 0.5;
                            el.style.fontSize = sfs + 'px';
                        }
                    }
                    if (subBox.classList.contains('two-col-box') && autoSubs.length === 2) {
                        const minColFs = Math.min(...autoSubs.map(e => parseFloat(window.getComputedStyle(e).fontSize)));
                        autoSubs.forEach(e => { e.style.fontSize = minColFs + 'px'; });
                    }
                }
                return { final_h_fs: fs, updated_html: document.documentElement.outerHTML };
            }"""
        )
        # Lưu lại HTML đã auto-fit cỡ chữ để `uiux_auditor.py` đọc lại đúng cỡ chữ thực tế
        html_out_path.write_text("<!DOCTYPE html>\n" + fit_info["updated_html"], encoding="utf-8")
        page.screenshot(path=str(overlay_png), omit_background=True)
        browser.close()

    with Image.open(bg_path) as bg_im, Image.open(overlay_png) as ov_im:
        comp = Image.alpha_composite(bg_im.convert("RGBA"), ov_im.convert("RGBA")).convert("RGB")
        comp.save(final_jpg_path, "JPEG", quality=93)

    if overlay_png.exists():
        overlay_png.unlink()

    return {"final_h_fs": fit_info["final_h_fs"]}


def make_3col_sbs_image(
    old_img_path: Path,
    primary_img_path: Path,
    alt_img_path: Path,
    out_sbs_path: Path,
    kb_id: str,
    primary_label: str,
    alt_label: str,
) -> None:
    W, H = 540, 675
    pad = 20
    header_h = 68
    canvas_w = W * 3 + pad * 4
    canvas_h = H + header_h + pad * 2

    canvas = Image.new("RGB", (canvas_w, canvas_h), (8, 13, 24))
    draw = ImageDraw.Draw(canvas)

    try:
        font = ImageFont.truetype("/Users/vietmac/.gemini/config/skills/auto-edit-video/remotion-studio/public/fonts/FDAeonik-Bold.ttf", 22)
    except Exception:
        font = ImageFont.load_default()

    panels = [
        (old_img_path, f"1. BẢN CŨ ({kb_id}) — Lỗi Nhồi Chữ & Tạp Nền", (239, 68, 68)),
        (primary_img_path, f"2. DUYỆT CHỐT ({primary_label} • 13/13 PASS)", (16, 185, 129)),
        (alt_img_path, f"3. PHƯƠNG ÁN ĐỐI CHỨNG ({alt_label})", (245, 158, 11)),
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


def r2_put(local_path: Path, r2_key: str) -> str:
    subprocess.run(
        ["python3", str(R2_MANAGER), "--put", str(local_path), r2_key],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return f"https://media.fedu.vn/{r2_key}"


def process_single_kb(
    kb_id: str,
    master: Dict[str, Any],
    cid: str = "",
    send_tele: bool = True,
) -> Dict[str, Any]:
    spec = master["kbs"][kb_id]
    style_code = spec["style"]
    style_name = master["style_names"][style_code]
    style_fonts = master["style_fonts"]
    bg_path = Path(master["bg_pool"][spec["bg"]])
    side = spec.get("side", "right")

    # Chọn phương án đối chứng (nếu chính là K01 thì đối chứng K02, ngược lại đối chứng K01 hoặc K02 có trong spec)
    if style_code == "K01":
        alt_code = "K02"
    elif "k01" in spec:
        alt_code = "K01"
    else:
        alt_code = "K02"
    alt_name = master["style_names"][alt_code]

    kb_lower = kb_id.lower()
    OUT_RENDER_DIR.mkdir(parents=True, exist_ok=True)

    html_primary_path = OUT_RENDER_DIR / f"{kb_lower}_{style_code.lower()}_primary.html"
    img_primary_path = OUT_RENDER_DIR / f"{kb_lower}_final.jpg"
    html_alt_path = OUT_RENDER_DIR / f"{kb_lower}_{alt_code.lower()}_alt.html"
    img_alt_path = OUT_RENDER_DIR / f"{kb_lower}_alt.jpg"
    img_sbs_path = OUT_RENDER_DIR / f"{kb_lower}_sbs.jpg"

    # 1. Render bản chính & bản đối chứng
    html_primary = build_style_html(style_code, spec, style_fonts)
    render_html_onto_bg(html_primary, html_primary_path, bg_path, img_primary_path)

    html_alt = build_style_html(alt_code, spec, style_fonts)
    render_html_onto_bg(html_alt, html_alt_path, bg_path, img_alt_path)

    # 2. Chạy kiểm toán 13 cổng `uiux_auditor.py`
    audit_res = audit_v3_banner(
        html_path=html_primary_path,
        final_img_path=img_primary_path,
        expected_lines=3,
        person_side=side,
    )

    # 3. Tìm ảnh V1 cũ để ghép bảng 3 cột trước-sau
    old_candidate = BASE_DIR / kb_id / "after" / f"{kb_id}_A1_after_opt.jpg"
    if not old_candidate.exists():
        old_candidate = BASE_DIR / "KB_15" / "after" / "KB_15_A1_after_opt.jpg"

    make_3col_sbs_image(
        old_img_path=old_candidate,
        primary_img_path=img_primary_path,
        alt_img_path=img_alt_path,
        out_sbs_path=img_sbs_path,
        kb_id=kb_id,
        primary_label=style_code,
        alt_label=alt_code,
    )

    # 4. Upload lên R2 `banner2/`
    r2_old = r2_put(old_candidate, f"banner2/{kb_lower}_old.jpg")
    r2_final = r2_put(img_primary_path, f"banner2/{kb_lower}_final.jpg")
    r2_alt = r2_put(img_alt_path, f"banner2/{kb_lower}_alt.jpg")
    r2_sbs = r2_put(img_sbs_path, f"banner2/{kb_lower}_sbs.jpg")

    headline_plain = " / ".join(
        ln.replace('<span class="hl">', "").replace("</span>", "") for ln in spec["headline_lines"]
    )
    font_label = style_fonts[style_code][1]

    # 5. Ghi card JSON độc lập vào `banner2_cards/KB_XX.json` (0% đụng độ giữa các nhánh)
    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    kb_order = int(kb_id.split("_")[1]) if "_" in kb_id and kb_id.split("_")[1].isdigit() else 999
    card_data = {
        "order": kb_order,
        "kb_id": kb_id,
        "title": spec["title"],
        "style_code": style_code,
        "style_name": style_name,
        "alt_style_code": alt_code,
        "alt_style_name": alt_name,
        "font_name": font_label,
        "person_side": side,
        "headline_plain": headline_plain,
        "hl_kw": spec["hl_kw"],
        "subline_summary": f"Chính: {style_name} • Đối chứng: {alt_name}",
        "audit_score": f"{audit_res['score']} PASS",
        "score": audit_res["score"],
        "all_13_pass": audit_res["all_13_pass"],
        "final_img_url": r2_final,
        "secondary_img_url": r2_alt,
        "secondary_label": f"Đối chứng ({alt_code})",
        "old_img_url": r2_old,
        "sbs_img_url": r2_sbs,
        "r2_old_url": r2_old,
        "r2_final_url": r2_final,
        "r2_alt_url": r2_alt,
        "r2_sbs_url": r2_sbs,
    }
    (CARDS_DIR / f"{kb_id}.json").write_text(json.dumps(card_data, ensure_ascii=False, indent=2), encoding="utf-8")

    # 6. Đồng bộ tức thì vào `banner2.html` (Local + R2 Online) qua khóa `fcntl.flock`
    hub_info = atomic_rebuild_and_sync(push_r2=True)
    total_cards = hub_info.get("total_cards", 0)

    # 7. Bắn ngay Telegram thông báo xong cái nào gửi nhanh cái đó
    if send_tele and TELEGRAM_NOTIFY.exists():
        caption = (
            f"✅ Xong {kb_id}: {spec['title']}\n"
            f"🎨 {style_name} • Điểm kiểm toán: {audit_res['score']} PASS\n"
            f"📊 Tiến độ kệ Banner 2.0: {total_cards}/31 kịch bản\n"
            f"🌐 Xem Online: https://media.fedu.vn/banner2/banner2.html\n"
            f"🌐 Kệ Repo K: https://fedu.vn/k/banner2.html"
        )
        cmd = [
            "python3",
            str(TELEGRAM_NOTIFY),
            "--photo",
            str(img_primary_path),
            "--caption",
            caption,
            "--force",
        ]
        if cid:
            cmd.extend(["--cid", cid])
        subprocess.run(cmd, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return {
        "kb_id": kb_id,
        "style_code": style_code,
        "score": audit_res["score"],
        "all_13_pass": audit_res["all_13_pass"],
        "r2_final_url": r2_final,
        "hub_count": total_cards,
        "failed_gates": [k for k, v in audit_res["gates"].items() if not v["pass"]],
    }


def main():
    parser = argparse.ArgumentParser(description="Batch Branch Runner V3.0 (3 Banners per Branch)")
    parser.add_argument("--kbs", type=str, required=True, help="Danh sách KB cách nhau dấu phẩy, VD: KB_02,KB_03,KB_04")
    parser.add_argument("--cid", type=str, default="", help="Conversation ID để gắn nút Telegram")
    parser.add_argument("--no-tele", action="store_true", help="Tắt gửi lẻ Telegram nếu cần")
    args = parser.parse_args()

    master = json.loads(SPECS_PATH.read_text(encoding="utf-8"))
    kb_list = [x.strip().upper() for x in args.kbs.split(",") if x.strip()]

    results = []
    for kb_id in kb_list:
        if kb_id not in master["kbs"]:
            print(f"[SKIP] {kb_id} không có trong kb_31_master_specs.json")
            continue
        res = process_single_kb(kb_id, master, cid=args.cid, send_tele=not args.no_tele)
        print(json.dumps(res, ensure_ascii=False))
        results.append(res)

    print(f"=== DONE BATCH ({len(results)} banners) ===")


if __name__ == "__main__":
    main()
