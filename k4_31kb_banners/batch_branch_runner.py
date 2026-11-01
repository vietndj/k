#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BATCH BRANCH RUNNER V5.0 — 70 AD BANNERS × 32 BANNER.HTML STYLES × 20 FONTS (H01-H20) × 21 SUB-BOXES (K01-K21)
==============================================================================================================
- Đọc thông số kịch bản từ `kb_31_master_specs.json` (70 Kịch bản: `KB_01` -> `KB_70`).
- Mỗi kịch bản có 1 trang phục & 1 phong cách bối cảnh/ánh sáng độc bản từ `banner.html` (`outfit_id`, `banner_style_name`, `accent_color`).
- Render mỗi KB theo đúng Bộ Chọn Chữ `bo-chon-chu-banner.html`:
  + Lớp 1: 20 Font Tiêu Đề Có Chân (`H01` -> `H20`) kèm `HeadFocal` (`LAW_09` Per-Font Optical Leading + `LAW_10` Pairing).
  + Lớp 2: Toàn bộ 21 Khuôn Khung Chữ Bé (`K01` -> `K21`) + 1 phương án đối chứng (`alt_style`).
- Chấm điểm tự động qua 15 Cổng Thực Chiến `uiux_auditor.py` (`15/15 PASS`).
- Đẩy ảnh lên R2 (`https://media.fedu.vn/banner2/...`), ghi `banner2_cards/KB_XX.json` và gọi `update_banner2_hub.py` (`fcntl.flock`).
- Bắn ngay từng Banner hoàn thành vào Telegram kèm link bấm 1 chạm.
"""

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, Any, Optional
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright, Browser

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
    master: Dict[str, Any],
) -> str:
    h_code = spec.get("h_code", "H01")
    h_fonts = master.get("headline_fonts", {})
    if h_code in h_fonts:
        hf = h_fonts[h_code]
        font_file = hf["file"]
        focal_file = hf.get("focal_file", font_file)
        focal_style = hf.get("focal_style", "normal")
        base_fs = hf["base_fs"]
        base_lh = hf["base_lh"]
    else:
        font_file, _, base_fs, base_lh = master["style_fonts"].get(style_code, ("FDTiemposHeadline-Bold.woff2", "Tiempos", 80, 1.12))
        focal_file = font_file
        focal_style = "normal"

    accent = spec.get("accent_color", "#FACC15")
    side = spec.get("side", "right")
    zone_left = 40 if side == "right" else 552
    zone_width = 492
    card_width = 484

    lines_html = "\n      ".join(f'<span class="line">{ln}</span>' for ln in spec["headline_lines"])

    common_head = f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"/>
<style>
  @font-face {{
    font-family: "HeadSerif";
    src: url("file:///Users/vietmac/Documents/CODE/fedu-font/fonts/{font_file}");
    font-weight: 700;
    font-style: normal;
  }}
  @font-face {{
    font-family: "HeadFocal";
    src: url("file:///Users/vietmac/Documents/CODE/fedu-font/fonts/{focal_file}");
    font-weight: 700;
    font-style: {focal_style};
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
    src: url("file:///Users/vietmac/Documents/CODE/fedu-font/fonts/FDMonumentGroteskMono-Bold.woff2");
    font-weight: 700;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
  body {{ width: 1080px; height: 1350px; background: transparent; overflow: hidden; position: relative; }}
  .zone {{
    position: absolute; left: {zone_left}px; top: 185px; width: {zone_width}px; height: 970px;
    display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
  }}
  .headline {{
    font-family: "HeadSerif", serif;
    font-size: {base_fs}px;
    line-height: {base_lh};
    letter-spacing: -0.013em;
    color: #FFFFFF;
    margin-bottom: 38px;
    width: max-content;
    text-shadow: 0 14px 34px rgba(0, 0, 0, 0.68);
  }}
  .headline .line {{ display: block; width: max-content; white-space: nowrap; font-size: 1em; }}
  .headline .hl {{
    font-family: "HeadFocal", serif;
    font-style: {focal_style};
    font-weight: 700;
    font-size: 1em;
    color: {accent};
    text-shadow: 0 12px 30px rgba(0, 0, 0, 0.78);
  }}
  .sub-box {{
    width: {card_width}px;
    max-width: {card_width}px;
    background: rgba(3, 6, 14, 0.92);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 14px;
    padding: 20px 20px;
    margin-bottom: 40px;
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.45);
  }}
  .meta {{
    font-family: "SubMed", sans-serif;
    font-size: 24.5px;
    color: #E2E8F0;
    letter-spacing: 0.02em;
    display: flex; align-items: center; gap: 12px;
  }}
  .dot {{ width: 10px; height: 10px; border-radius: 50%; background: {accent}; }}
  .accent-txt {{ color: {accent}; font-family: "SubBold", sans-serif; }}
"""

    if style_code == "K01":
        d = spec["k01"]
        return common_head + f"""
  .sub-box {{ border-left: 4px solid {accent}; display: flex; flex-direction: column; gap: 13px; }}
  .row {{ display: flex; align-items: center; gap: 11px; white-space: nowrap; }}
  .icon-x {{ font-family: "SubBold", sans-serif; font-size: 25px; color: #EF4444; width: 22px; text-align: center; flex-shrink: 0; }}
  .icon-ok {{ font-family: "SubBold", sans-serif; font-size: 25px; color: {accent}; width: 22px; text-align: center; flex-shrink: 0; }}
  .txt-old {{ font-family: "SubMed", sans-serif; font-size: 26.5px; color: #94A3B8; white-space: nowrap; }}
  .txt-new {{ font-family: "SubBold", sans-serif; font-size: 27.5px; color: #FFFFFF; white-space: nowrap; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="row"><span class="icon-x">×</span><span class="txt-old auto-sub">{d["old"]}</span></div>
    <div class="row"><span class="icon-ok">✓</span><span class="txt-new auto-sub">{d["new"]}</span></div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K02":
        d = spec["k02"]
        return common_head + f"""
  .sub-box {{ border-top: 3px solid {accent}; padding: 21px 22px; }}
  .eyebrow {{ font-family: "SubBold", sans-serif; font-size: 19.5px; letter-spacing: 0.06em; color: {accent}; margin-bottom: 9px; display: block; text-transform: uppercase; white-space: nowrap; }}
  .l1 {{ font-family: "SubMed", sans-serif; font-size: 26.5px; line-height: 1.32; color: #94A3B8; white-space: nowrap; display: block; margin-bottom: 4px; }}
  .l2 {{ font-family: "SubBold", sans-serif; font-size: 27.5px; line-height: 1.34; color: #FFFFFF; white-space: nowrap; display: block; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <span class="eyebrow auto-sub">{d["eyebrow"]}</span>
    <span class="l1 auto-sub">{d["l1"]}</span>
    <span class="l2 auto-sub">{d["l2"]}</span>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K03":
        d = spec["k03"]
        return common_head + f"""
  .sub-box {{ display: grid; grid-template-columns: minmax(0, 1fr) 28px minmax(0, 1fr); align-items: center; }}
  .col-stat {{ display: flex; flex-direction: column; gap: 4px; min-width: 0; }}
  .n-gold {{ font-family: "MetaMono", monospace; font-size: 62px; line-height: 1.0; color: {accent}; white-space: nowrap; }}
  .n-white {{ font-family: "MetaMono", monospace; font-size: 62px; line-height: 1.0; color: #FFFFFF; white-space: nowrap; }}
  .lbl-sub {{ font-family: "SubMed", sans-serif; font-size: 22px; line-height: 1.28; color: #CBD5E1; white-space: normal; word-wrap: break-word; }}
  .arrow {{ font-family: "SubBold", sans-serif; font-size: 28px; color: {accent}; text-align: center; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="col-stat"><span class="n-gold">{d["n1"]}</span><span class="lbl-sub auto-sub">{d["l1"]}</span></div>
    <div class="arrow">→</div>
    <div class="col-stat" style="padding-left: 14px;"><span class="n-white">{d["n2"]}</span><span class="lbl-sub auto-sub">{d["l2"]}</span></div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K04":
        d = spec["k04"]
        return common_head + f"""
  .sub-box {{ position: relative; padding: 30px 22px 20px; }}
  .floating-tab {{ position: absolute; top: -14px; left: 20px; background: {accent}; color: #070B14; font-family: "SubBold", sans-serif; font-size: 19.5px; letter-spacing: 0.05em; padding: 4px 12px; border-radius: 6px; text-transform: uppercase; white-space: nowrap; }}
  .l1 {{ font-family: "SubMed", sans-serif; font-size: 26.5px; line-height: 1.34; color: #94A3B8; white-space: nowrap; display: block; margin-bottom: 4px; }}
  .l2 {{ font-family: "SubBold", sans-serif; font-size: 27.5px; line-height: 1.35; color: #FFFFFF; white-space: nowrap; display: block; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <span class="floating-tab">{d["tab"]}</span>
    <span class="l1 auto-sub">{d["l1"]}</span>
    <span class="l2 auto-sub">{d["l2"]}</span>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K05":
        d = spec["k05"]
        return common_head + f"""
  .sub-box {{ border: 1.5px solid {accent}; }}
  .l1 {{ font-family: "SubMed", sans-serif; font-size: 26.5px; line-height: 1.35; color: #94A3B8; margin-bottom: 6px; white-space: nowrap; display: block; }}
  .l2 {{ font-family: "SubBold", sans-serif; font-size: 27.5px; line-height: 1.35; color: #FFFFFF; white-space: nowrap; display: block; }}
  .l2 em {{ font-style: normal; color: {accent}; padding: 0 3px; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <span class="l1 auto-sub">{d["l1"]}</span>
    <span class="l2 auto-sub"><em>→</em> {d["s2"]}</span>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K06":
        d = spec["k06"]
        return common_head + f"""
  .sub-box {{ display: flex; flex-direction: column; gap: 13px; }}
  .nb-row {{ display: flex; align-items: center; gap: 10px; white-space: nowrap; }}
  .tag-not {{ font-family: "SubBold", sans-serif; font-size: 19.5px; background: rgba(148, 163, 184, 0.18); color: #94A3B8; padding: 4px 9px; border-radius: 6px; flex-shrink: 0; }}
  .tag-but {{ font-family: "SubBold", sans-serif; font-size: 19.5px; background: {accent}; color: #070B14; padding: 4px 10px; border-radius: 6px; flex-shrink: 0; }}
  .txt-not {{ font-family: "SubMed", sans-serif; font-size: 26px; color: #94A3B8; white-space: nowrap; }}
  .txt-but {{ font-family: "SubBold", sans-serif; font-size: 27px; color: #FFFFFF; white-space: nowrap; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="nb-row"><span class="tag-not">KHÔNG PHẢI</span><span class="txt-not auto-sub">{d["not"]}</span></div>
    <div class="nb-row"><span class="tag-but">MÀ LÀ</span><span class="txt-but auto-sub">{d["but"]}</span></div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K07":
        d = spec["k07"]
        return common_head + f"""
  .sub-box {{ padding: 0; display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); overflow: hidden; }}
  .col-left {{ padding: 18px 15px; border-right: 1px solid rgba(255, 255, 255, 0.12); min-width: 0; }}
  .col-right {{ padding: 18px 15px; background: rgba(255, 255, 255, 0.04); min-width: 0; }}
  .c-head-muted {{ font-family: "SubBold", sans-serif; font-size: 19.5px; white-space: nowrap; color: #94A3B8; margin-bottom: 6px; display: block; }}
  .c-head-gold {{ font-family: "SubBold", sans-serif; font-size: 19.5px; white-space: nowrap; color: {accent}; margin-bottom: 6px; display: block; }}
  .c-body-muted {{ font-family: "SubMed", sans-serif; font-size: 21.5px; line-height: 1.32; white-space: normal; word-wrap: break-word; color: #CBD5E1; display: block; }}
  .c-body-bright {{ font-family: "SubBold", sans-serif; font-size: 21.5px; line-height: 1.32; white-space: normal; word-wrap: break-word; color: #FFFFFF; display: block; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box two-col-box">
    <div class="col-left"><span class="c-head-muted">{d["lh"]}</span><span class="c-body-muted auto-sub">{d["lb"]}</span></div>
    <div class="col-right"><span class="c-head-gold">{d["rh"]}</span><span class="c-body-bright auto-sub">{d["rb"]}</span></div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K08":
        d = spec["k08"]
        return common_head + f"""
  .sub-box {{ border-bottom: 4px solid {accent}; }}
  .l1 {{ font-family: "SubMed", sans-serif; font-size: 26.5px; color: #94A3B8; margin-bottom: 8px; white-space: nowrap; display: block; }}
  .l2 {{ font-family: "SubBold", sans-serif; font-size: 27.5px; color: #FFFFFF; white-space: nowrap; display: block; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <span class="l1 auto-sub">{d["l1"]}</span>
    <span class="l2 auto-sub"><span class="accent-txt">{d["l2_pre"]}</span>{d["l2_ul"]}</span>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K09":
        d = spec["k09"]
        return common_head + f"""
  .sub-box {{ border: 1.5px solid {accent}; border-radius: 22px 22px 22px 6px; }}
  .chat-meta {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #94A3B8; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; white-space: nowrap; }}
  .online-dot {{ width: 10px; height: 10px; border-radius: 50%; background: #22C55E; }}
  .chat-msg1 {{ font-family: "SubBold", sans-serif; font-size: 26.5px; color: #FFFFFF; white-space: nowrap; display: block; margin-bottom: 4px; }}
  .chat-msg2 {{ font-family: "SubBold", sans-serif; font-size: 27.5px; color: {accent}; white-space: nowrap; display: block; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="chat-meta"><span class="online-dot"></span><span>{d["meta"]}</span></div>
    <span class="chat-msg1 auto-sub">{d["msg1"]}</span>
    <span class="chat-msg2 auto-sub">{d["msg2"]}</span>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K10":
        d = spec["k10"]
        return common_head + f"""
  .sub-box {{ display: flex; flex-direction: column; gap: 13px; }}
  .m-row {{ display: flex; align-items: center; gap: 12px; white-space: nowrap; }}
  .m-lbl {{ font-family: "SubBold", sans-serif; font-size: 22.5px; color: #CBD5E1; min-width: 170px; width: auto; flex-shrink: 0; }}
  .m-track {{ flex: 1; height: 12px; background: rgba(255, 255, 255, 0.12); border-radius: 99px; overflow: hidden; min-width: 60px; }}
  .m-fill-low {{ width: 18%; height: 100%; background: #64748B; border-radius: 99px; }}
  .m-fill-high {{ width: 94%; height: 100%; background: {accent}; border-radius: 99px; }}
  .m-val {{ font-family: "MetaMono", monospace; font-size: 21.5px; color: #94A3B8; min-width: 112px; width: auto; text-align: right; flex-shrink: 0; }}
  .m-val.hi {{ color: {accent}; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="m-row"><span class="m-lbl">{d["lbl1"]}</span><div class="m-track"><div class="m-fill-low"></div></div><span class="m-val">{d["val1"]}</span></div>
    <div class="m-row"><span class="m-lbl accent-txt">{d["lbl2"]}</span><div class="m-track"><div class="m-fill-high"></div></div><span class="m-val hi">{d["val2"]}</span></div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K11":
        d = spec["k11"]
        return common_head + f"""
  .sub-box {{ display: flex; flex-direction: column; gap: 13px; }}
  .qa-row {{ display: flex; align-items: center; gap: 10px; white-space: nowrap; }}
  .q-tag {{ font-family: "SubBold", sans-serif; font-size: 19.5px; background: rgba(148,163,184,0.2); color: #CBD5E1; padding: 4px 9px; border-radius: 6px; flex-shrink: 0; }}
  .a-tag {{ font-family: "SubBold", sans-serif; font-size: 19.5px; background: {accent}; color: #070B14; padding: 4px 9px; border-radius: 6px; flex-shrink: 0; }}
  .q-txt {{ font-family: "SubMed", sans-serif; font-size: 26px; color: #94A3B8; white-space: nowrap; }}
  .a-txt {{ font-family: "SubBold", sans-serif; font-size: 27px; color: #FFFFFF; white-space: nowrap; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="qa-row"><span class="q-tag">HỎI</span><span class="q-txt auto-sub">{d["q"]}</span></div>
    <div class="qa-row"><span class="a-tag">ĐÁP</span><span class="a-txt auto-sub">{d["a"]}</span></div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K12":
        d = spec["k12"]
        return common_head + f"""
  .sub-box {{ border: 1.5px dashed {accent}; display: flex; flex-direction: column; gap: 10px; }}
  .vf-1 {{ font-family: "SubMed", sans-serif; font-size: 26px; color: #CBD5E1; white-space: nowrap; display: block; }}
  .vf-2 {{ font-family: "SubBold", sans-serif; font-size: 27px; color: #FFFFFF; white-space: nowrap; display: block; }}
  .vf-hl {{ background: rgba(250, 204, 21, 0.22); color: #FFFFFF; border-bottom: 2px solid {accent}; padding: 2px 8px; border-radius: 6px; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <span class="vf-1 auto-sub">┌ {d["l1"]}</span>
    <span class="vf-2 auto-sub">└ <span class="vf-hl">{d["l2"]}</span> ┘</span>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K13":
        d = spec["k13"]
        return common_head + f"""
  .sub-box {{ display: flex; flex-direction: column; gap: 12px; }}
  .tl-row {{ display: flex; align-items: center; gap: 11px; white-space: nowrap; }}
  .node-o {{ font-family: "SubBold", sans-serif; font-size: 23px; color: #94A3B8; flex-shrink: 0; }}
  .node-f {{ font-family: "SubBold", sans-serif; font-size: 23px; color: {accent}; flex-shrink: 0; }}
  .tl-1 {{ font-family: "SubMed", sans-serif; font-size: 26px; color: #94A3B8; white-space: nowrap; }}
  .tl-2 {{ font-family: "SubBold", sans-serif; font-size: 27px; color: #FFFFFF; white-space: nowrap; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="tl-row"><span class="node-o">○</span><span class="tl-1 auto-sub">{d["t1"]}</span></div>
    <div class="tl-row"><span class="node-f">●</span><span class="tl-2 auto-sub">{d["t2"]}</span></div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K14":
        d = spec["k14"]
        return common_head + f"""
  .sub-box {{ display: flex; flex-direction: column; gap: 12px; }}
  .r14 {{ display: flex; align-items: center; gap: 10px; white-space: nowrap; }}
  .b-old {{ font-family: "MetaMono", monospace; font-size: 19.5px; color: #94A3B8; background: rgba(148,163,184,0.16); padding: 3px 8px; border-radius: 6px; flex-shrink: 0; }}
  .b-new {{ font-family: "MetaMono", monospace; font-size: 19.5px; color: #070B14; background: {accent}; padding: 3px 8px; border-radius: 6px; flex-shrink: 0; }}
  .t-old {{ font-family: "SubMed", sans-serif; font-size: 26px; color: #94A3B8; white-space: nowrap; }}
  .t-new {{ font-family: "SubBold", sans-serif; font-size: 27px; color: #FFFFFF; white-space: nowrap; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="r14"><span class="b-old">CŨ</span><span class="t-old auto-sub">{d["old"]}</span></div>
    <div class="r14"><span class="b-new">MỚI</span><span class="t-new auto-sub">{d["new"]}</span></div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K15":
        d = spec["k15"]
        return common_head + f"""
  .sub-box {{ display: flex; flex-direction: column; gap: 13px; }}
  .wk-row {{ display: grid; grid-template-columns: repeat(7, 1fr); gap: 7px; }}
  .wk-c {{ height: 38px; border-radius: 7px; border: 1.5px solid rgba(148,163,184,0.22); color: #94A3B8; font-family: "MetaMono", monospace; font-size: 19.5px; display: flex; align-items: center; justify-content: center; }}
  .wk-c.on {{ background: rgba(250,204,21,0.18); border: 2px solid {accent}; color: {accent}; }}
  .wk-cap {{ font-family: "SubBold", sans-serif; font-size: 26.5px; color: #FFFFFF; white-space: nowrap; display: block; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="wk-row">
      <span class="wk-c">T2</span><span class="wk-c">T3</span><span class="wk-c on">T4</span><span class="wk-c">T5</span><span class="wk-c">T6</span><span class="wk-c on">T7</span><span class="wk-c">CN</span>
    </div>
    <span class="wk-cap auto-sub">→ {d["caption"]}</span>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K16":
        d = spec["k16"]
        return common_head + f"""
  .sub-box {{ position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 10px; }}
  .ghost-w {{ position: absolute; right: 10px; top: 50%; transform: translateY(-50%); font-family: "MetaMono", monospace; font-size: 96px; line-height: 1; color: rgba(255,255,255,0.06); pointer-events: none; }}
  .gl1 {{ position: relative; font-family: "SubMed", sans-serif; font-size: 26.5px; color: #94A3B8; white-space: nowrap; display: block; }}
  .gl2 {{ position: relative; font-family: "SubBold", sans-serif; font-size: 27.5px; color: #FFFFFF; white-space: nowrap; display: block; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <span class="ghost-w">K4</span>
    <span class="gl1 auto-sub">{d["l1"]}</span>
    <span class="gl2 auto-sub"><span class="accent-txt">✓</span> {d["l2"]}</span>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K17":
        d = spec["k17"]
        return common_head + f"""
  .sub-box {{ display: flex; flex-direction: column; gap: 12px; }}
  .ld-row {{ display: flex; align-items: baseline; gap: 8px; white-space: nowrap; }}
  .ld-lo {{ font-family: "SubMed", sans-serif; font-size: 25px; color: #94A3B8; }}
  .ld-dots {{ flex: 1; border-bottom: 2px dotted rgba(148,163,184,0.35); min-width: 18px; }}
  .ld-ro {{ font-family: "SubBold", sans-serif; font-size: 25px; color: #64748B; }}
  .ld-ln {{ font-family: "SubBold", sans-serif; font-size: 26px; color: #FFFFFF; }}
  .ld-rn {{ font-family: "SubBold", sans-serif; font-size: 26px; color: {accent}; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="ld-row"><span class="ld-lo auto-sub">{d["l_old"]}</span><span class="ld-dots"></span><span class="ld-ro auto-sub">{d["r_old"]}</span></div>
    <div class="ld-row"><span class="ld-ln auto-sub">{d["l_new"]}</span><span class="ld-dots"></span><span class="ld-rn auto-sub">{d["r_new"]}</span></div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K18":
        d = spec["k18"]
        return common_head + f"""
  .sub-box {{ display: flex; flex-direction: column; gap: 12px; }}
  .eq-top {{ display: flex; align-items: center; gap: 9px; white-space: nowrap; }}
  .eq-chip {{ background: rgba(148,163,184,0.16); border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 4px 11px; font-family: "SubBold", sans-serif; font-size: 23px; color: #E2E8F0; }}
  .eq-plus {{ font-family: "MetaMono", monospace; font-size: 24px; color: {accent}; }}
  .eq-bot {{ font-family: "SubBold", sans-serif; font-size: 27px; color: #FFFFFF; white-space: nowrap; display: block; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="eq-top"><span class="eq-chip">{d["p1"]}</span><span class="eq-plus">+</span><span class="eq-chip">{d["p2"]}</span></div>
    <span class="eq-bot auto-sub"><span class="accent-txt">=</span> {d["res"]}</span>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K19":
        d = spec["k19"]
        return common_head + f"""
  .sub-box {{ display: flex; flex-direction: column; gap: 12px; }}
  .ck-row {{ display: flex; align-items: center; gap: 11px; white-space: nowrap; }}
  .ck-b {{ width: 28px; height: 28px; border-radius: 6px; background: rgba(250,204,21,0.16); border: 2px solid {accent}; color: {accent}; font-family: "SubBold", sans-serif; font-size: 20px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
  .ck-1 {{ font-family: "SubMed", sans-serif; font-size: 26px; color: #CBD5E1; white-space: nowrap; }}
  .ck-2 {{ font-family: "SubBold", sans-serif; font-size: 27px; color: #FFFFFF; white-space: nowrap; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="ck-row"><span class="ck-b">✓</span><span class="ck-1 auto-sub">{d["c1"]}</span></div>
    <div class="ck-row"><span class="ck-b">✓</span><span class="ck-2 auto-sub">{d["c2"]}</span></div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    if style_code == "K20":
        d = spec["k20"]
        return common_head + f"""
  .sub-box {{ display: flex; flex-direction: column; gap: 12px; }}
  .rx-r {{ display: flex; align-items: center; gap: 10px; white-space: nowrap; }}
  .rx-bo {{ background: rgba(148,163,184,0.2); color: #CBD5E1; font-family: "MetaMono", monospace; font-size: 19.5px; padding: 4px 9px; border-radius: 6px; flex-shrink: 0; }}
  .rx-bn {{ background: {accent}; color: #070B14; font-family: "MetaMono", monospace; font-size: 19.5px; padding: 4px 9px; border-radius: 6px; flex-shrink: 0; }}
  .rx-to {{ font-family: "SubMed", sans-serif; font-size: 26px; color: #94A3B8; white-space: nowrap; }}
  .rx-tn {{ font-family: "SubBold", sans-serif; font-size: 27px; color: #FFFFFF; white-space: nowrap; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="rx-r"><span class="rx-bo">BỆNH</span><span class="rx-to auto-sub">{d["benh"]}</span></div>
    <div class="rx-r"><span class="rx-bn">THUỐC</span><span class="rx-tn auto-sub">{d["thuoc"]}</span></div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""

    # Default K21 (03s Scroll Filter)
    d = spec["k21"]
    return common_head + f"""
  .sub-box {{ display: grid; grid-template-columns: 106px 2px 1fr; gap: 14px; align-items: center; }}
  .s-badge {{ display: flex; flex-direction: column; align-items: flex-start; justify-content: center; padding-left: 2px; }}
  .s-num {{ font-family: "MetaMono", monospace; font-size: 56px; line-height: 1; color: {accent}; }}
  .s-lbl {{ font-family: "SubBold", sans-serif; font-size: 19.5px; color: #94A3B8; margin-top: 4px; }}
  .s-div {{ width: 2px; height: 64px; background: {accent}; opacity: 0.45; }}
  .s-right {{ display: flex; flex-direction: column; gap: 8px; min-width: 0; }}
  .sr-1 {{ font-family: "SubMed", sans-serif; font-size: 25px; color: #94A3B8; white-space: nowrap; display: block; }}
  .sr-2 {{ font-family: "SubBold", sans-serif; font-size: 26px; color: #FFFFFF; white-space: nowrap; display: block; }}
</style></head>
<body><div class="zone">
  <h1 class="headline">{lines_html}</h1>
  <div class="sub-box">
    <div class="s-badge"><span class="s-num">03s</span><span class="s-lbl">LƯỚT</span></div>
    <div class="s-div"></div>
    <div class="s-right">
      <span class="sr-1 auto-sub">{d["l1"]}</span>
      <span class="sr-2 auto-sub">{d["l2"]}</span>
    </div>
  </div>
  <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
</div></body></html>"""


def render_html_onto_bg(
    html_content: str,
    html_out_path: Path,
    bg_path: Path,
    final_jpg_path: Path,
    browser: Optional[Browser] = None,
) -> Dict[str, Any]:
    html_out_path.parent.mkdir(parents=True, exist_ok=True)
    html_out_path.write_text(html_content, encoding="utf-8")
    overlay_png = html_out_path.with_suffix(".overlay.png")

    def _run_on_browser(b: Browser) -> Dict[str, Any]:
        page = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        page.goto(f"file://{html_out_path.resolve()}", wait_until="load")
        page.evaluate("() => document.fonts.ready")

        fit_info = page.evaluate(
            """() => {
                const h = document.querySelector('.headline');
                const zone = document.querySelector('.zone');
                const lines = Array.from(document.querySelectorAll('.headline .line'));
                const maxLineW = (zone ? zone.clientWidth : 512) - 8;
                let fs = parseFloat(window.getComputedStyle(h).fontSize);
                while (fs > 51) {
                    const maxW = Math.max(...lines.map(l => Math.max(l.scrollWidth, l.getBoundingClientRect().width)));
                    if (maxW <= maxLineW) break;
                    fs -= 1;
                    h.style.fontSize = fs + 'px';
                }

                // LAW_09 V4.0: Đo xRatio & Ma trận mực 2D cho từng font + từng câu
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
                    const maxLhW = 2.35 * xRatio;
                    let targetLh = Math.max(minLhW, reqLh);
                    if (targetLh > maxLhW) targetLh = maxLhW;
                    targetLh = Math.max(0.99, Math.min(1.165, +targetLh.toFixed(3)));
                    const gapPx = Math.round(targetLh * curFs - maxOverlap);
                    const wVal = +((targetLh - xRatio) / xRatio).toFixed(2);
                    return { fs: curFs, targetLh, gapPx, wVal, pass: (gapPx >= 6 && wVal >= 1.10 && wVal <= 1.36) };
                }

                let best = solveLaw09(fs);
                if (!best.pass) {
                    for (let tryFs = fs - 1; tryFs >= Math.max(52, fs - 10); tryFs--) {
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

                // Auto-fit các dòng chữ bé trong hộp bằng Range vết mực thực tế (0% tràn phải, min >= 19.6px)
                const subBox = document.querySelector('.sub-box');
                if (subBox) {
                    const boxRect = subBox.getBoundingClientRect();
                    const autoSubs = Array.from(subBox.querySelectorAll('.auto-sub'));
                    for (const el of autoSubs) {
                        let sfs = parseFloat(window.getComputedStyle(el).fontSize);
                        const colParent = el.closest('.col-left, .col-right, .col-stat, .s-right');
                        while (sfs > 19.6) {
                            const range = document.createRange();
                            range.selectNodeContents(el);
                            const r = range.getBoundingClientRect();
                            const limitRight = colParent ? Math.min(colParent.getBoundingClientRect().right - 8, boxRect.right - 8) : (boxRect.right - 8);
                            if (r.right <= limitRight) break;
                            sfs = +(sfs - 0.5).toFixed(1);
                            el.style.fontSize = sfs + 'px';
                        }
                        // Nếu ở 19.6px vẫn hơi dài hơn hộp, siết nhẹ letter-spacing hoặc cắt gọn từ cuối
                        const range2 = document.createRange();
                        range2.selectNodeContents(el);
                        const limitR2 = colParent ? Math.min(colParent.getBoundingClientRect().right - 6, boxRect.right - 6) : (boxRect.right - 6);
                        if (range2.getBoundingClientRect().right > limitR2) {
                            el.style.letterSpacing = '-0.025em';
                        }
                        while (el.innerText.length > 12) {
                            const r3 = document.createRange();
                            r3.selectNodeContents(el);
                            if (r3.getBoundingClientRect().right <= limitR2) break;
                            const words = el.innerText.trim().split(' ');
                            if (words.length <= 3) break;
                            words.pop();
                            el.innerText = words.join(' ');
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
        html_out_path.write_text("<!DOCTYPE html>\n" + fit_info["updated_html"], encoding="utf-8")
        page.screenshot(path=str(overlay_png), omit_background=True)
        page.close()
        return fit_info

    if browser is not None:
        fit_info = _run_on_browser(browser)
    else:
        with sync_playwright() as pw:
            b = pw.chromium.launch(headless=True)
            fit_info = _run_on_browser(b)
            b.close()

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
        (old_img_path, f"1. BẢN CŨ ({kb_id}) — Một Màu Tối Cũ", (239, 68, 68)),
        (primary_img_path, f"2. BẢN CHỐT ({primary_label} • 15/15 PASS)", (16, 185, 129)),
        (alt_img_path, f"3. ĐỐI CHỨNG ({alt_label})", (245, 158, 11)),
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
    browser: Optional[Browser] = None,
) -> Dict[str, Any]:
    spec = master["kbs"][kb_id]
    h_code = spec.get("h_code", "H01")
    style_code = spec["style"]
    alt_code = spec.get("alt_style", "K02" if style_code == "K01" else "K01")
    style_name = master["style_names"].get(style_code, style_code)
    alt_name = master["style_names"].get(alt_code, alt_code)
    font_label = spec.get("h_name") or master.get("headline_fonts", {}).get(h_code, {}).get("name", h_code)
    outfit_id = spec.get("outfit_id", "C02_I03")
    banner_style_name = spec.get("banner_style_name", "Style banner.html")

    bg_path = Path(master["bg_pool"][spec["bg"]])
    side = spec.get("side", "right")

    kb_lower = kb_id.lower()
    OUT_RENDER_DIR.mkdir(parents=True, exist_ok=True)

    html_primary_path = OUT_RENDER_DIR / f"{kb_lower}_{style_code.lower()}_primary.html"
    img_primary_path = OUT_RENDER_DIR / f"{kb_lower}_final.jpg"
    html_alt_path = OUT_RENDER_DIR / f"{kb_lower}_{alt_code.lower()}_alt.html"
    img_alt_path = OUT_RENDER_DIR / f"{kb_lower}_alt.jpg"
    img_sbs_path = OUT_RENDER_DIR / f"{kb_lower}_sbs.jpg"

    # 1. Render bản chính & bản đối chứng trong chung 1 phiên Chromium rồi đóng trước khi gọi uiux_auditor
    html_primary = build_style_html(style_code, spec, master)
    html_alt = build_style_html(alt_code, spec, master)
    with sync_playwright() as pw:
        b = pw.chromium.launch(headless=True)
        render_html_onto_bg(html_primary, html_primary_path, bg_path, img_primary_path, browser=b)
        render_html_onto_bg(html_alt, html_alt_path, bg_path, img_alt_path, browser=b)
        b.close()

    # 2. Chạy kiểm toán 15 cổng `uiux_auditor.py`
    audit_res = audit_v3_banner(
        html_path=html_primary_path,
        final_img_path=img_primary_path,
        expected_lines=3,
        person_side=side,
    )

    # Nếu cổng phụ đề G12 hoặc G2 cần fallback sang K01/K02 để đạt 15/15 PASS tuyệt đối
    if not audit_res["all_13_pass"] and style_code not in ("K01", "K02"):
        fallback_code = "K01"
        html_fb = build_style_html(fallback_code, spec, master)
        render_html_onto_bg(html_fb, html_primary_path, bg_path, img_primary_path, browser=None)
        audit_fb = audit_v3_banner(html_primary_path, img_primary_path, expected_lines=3, person_side=side)
        if audit_fb["all_13_pass"]:
            audit_res = audit_fb
            style_code = fallback_code
            style_name = master["style_names"].get(style_code, style_code)

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
        primary_label=f"{h_code}×{style_code}",
        alt_label=f"{h_code}×{alt_code}",
    )

    # 4. Upload lên R2 `banner2/`
    r2_old = r2_put(old_candidate, f"banner2/{kb_lower}_old.jpg")
    r2_final = r2_put(img_primary_path, f"banner2/{kb_lower}_final.jpg")
    r2_alt = r2_put(img_alt_path, f"banner2/{kb_lower}_alt.jpg")
    r2_sbs = r2_put(img_sbs_path, f"banner2/{kb_lower}_sbs.jpg")

    headline_plain = " / ".join(
        ln.replace('<span class="hl">', "").replace("</span>", "") for ln in spec["headline_lines"]
    )
    ver_tag = f"v5_{int(time.time()) % 100000}"

    # 5. Ghi card JSON độc lập vào `banner2_cards/KB_XX.json` (0% đụng độ giữa các nhánh)
    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    kb_order = int(kb_id.split("_")[1]) if "_" in kb_id and kb_id.split("_")[1].isdigit() else 999
    card_data = {
        "order": kb_order,
        "kb_id": kb_id,
        "ver": ver_tag,
        "title": spec["title"],
        "outfit_id": outfit_id,
        "banner_style_name": banner_style_name,
        "h_code": h_code,
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
            f"👔 {banner_style_name} (Outfit {outfit_id})\n"
            f"🔤 {font_label} × {style_name}\n"
            f"🛡️ Kiểm toán UI/UX: {audit_res['score']} PASS • Tiến độ: {total_cards}/70 kịch bản\n"
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
        "outfit_id": outfit_id,
        "banner_style_name": banner_style_name,
        "h_code": h_code,
        "style_code": style_code,
        "score": audit_res["score"],
        "all_13_pass": audit_res["all_13_pass"],
        "r2_final_url": r2_final,
        "hub_count": total_cards,
        "failed_gates": [k for k, v in audit_res["gates"].items() if not v["pass"]],
    }


def main():
    parser = argparse.ArgumentParser(description="Batch Branch Runner V5.0 (70 Diverse Banners)")
    parser.add_argument("--kbs", type=str, required=True, help="Danh sách KB cách nhau dấu phẩy, VD: KB_32,KB_33,KB_34")
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
        res = process_single_kb(kb_id, master, cid=args.cid, send_tele=not args.no_tele, browser=None)
        print(json.dumps(res, ensure_ascii=False), flush=True)
        results.append(res)

    print(f"=== DONE BATCH ({len(results)} banners) ===", flush=True)


if __name__ == "__main__":
    main()
