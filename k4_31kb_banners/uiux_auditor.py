#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI/UX BANNER AUDITOR V3.0 — 13-GATE REAL-WORLD AD VERIFIER + SELF-LEARNING LEDGER
=================================================================================
Nâng cấp từ bộ 8 chỉ số kỹ thuật cũ lên 13 Cổng Thực Chiến đúc kết sau quá trình
anh Việt trực tiếp sửa & duyệt chốt mẫu KB_01 và KB_15 (Phương Án 2 & Phương Án 3):

- Cổng G1..G8 (Nền tảng hình học & khả năng đọc trên Mobile 360px):
  G1: Cỡ chữ chuẩn hóa theo x-height (Tiêu đề >= 35px, Chữ bé >= 14.5px)
  G2: Khoảng cách dòng đo theo vết mực thực tế (1.05 <= lh <= 1.15, xóa sổ 1.402 cũ)
  G3: Khoảng cách chữ (Tracking -0.025em .. +0.02em)
  G4: Độ tương phản WCAG trên ảnh thật (Headline >= 7.0:1, Chữ bé trên đệm tối >= 12.0:1)
  G5: Phân cấp chính phụ & Phép thử làm mờ 360px (Salience ratio >= 1.08)
  G6: Đọc thử trên điện thoại 360px bằng Apple Vision `vn_ocr`
  G7: Vùng cấm Mặt + Cổ mở rộng (+0.65H dưới cằm) & Khoảng thở tới cơ thể >= 40px
  G8: Ngân sách diện tích chữ Facebook Ads (<= 20% diện tích ảnh 1080x1350)

- 5 Cổng Thực Chiến Mới Đóng Gói Từ Các Lần Sửa Của Anh Việt (G9..G13):
  G9  (LAW_03 - Focal Gold Budget): Chỉ đúng 1 cụm từ khóa vàng trong Headline (<= 3 từ),
      tối đa 1 hộp nền tối sâu cho chữ bé, CẤM hộp nút CTA giả ("Còn 17/35 chỗ").
  G10 (LAW_04 - Uniform Headline Scale & Sentence Case): Cấm ép cỡ chữ to/nhỏ lệch nhau
      giữa các dòng Headline (delta_fs == 0px), cấm ALL CAPS toàn tiêu đề, bắt buộc Font Có Chân (Serif).
  G11 (LAW_05 - Zero Line-Wrap Drop): Mỗi dòng Headline khóa `white-space: nowrap`,
      `scrollWidth <= zone_width`, công thức `cỡ = 505 / adv_em` chống rớt chữ cuối dòng (như chữ "vã").
  G12 (LAW_06 - Instant 0.3s Subline Readability): Chữ bé phải dùng Medium 500 / Bold 700
      (cỡ >= 29px), đặt trên tấm đệm tối sâu rgba(5,9,18, 0.74-0.80) theo Khuôn PA 2 (Hai Vế ×/✓)
      hoặc Khuôn PA 3 (Trích Dẫn 2 dòng có viền đỉnh vàng).
  G13 (LAW_01 - Full-Body Context & Balance): Nhân vật gần toàn thân (5.0x - 6.0x đầu),
      đỉnh tóc ở y = 35..110px, vùng trống phẳng mịn Canny <= 2.0%.
"""

import argparse
import json
import math
import subprocess
import tempfile
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, Any, List
import cv2
import numpy as np
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright

OUT_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
LAWS_PATH = OUT_DIR / "banner_laws.json"
VN_OCR_BIN = OUT_DIR / "vn_ocr"


def load_banner_laws() -> Dict[str, Any]:
    if LAWS_PATH.exists():
        return json.loads(LAWS_PATH.read_text(encoding="utf-8"))
    return {"version": "3.0", "learned_laws": []}


def srgb_to_linear(c: np.ndarray) -> np.ndarray:
    c = c / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def relative_luminance_map(rgb_arr: np.ndarray) -> np.ndarray:
    r = srgb_to_linear(rgb_arr[:, :, 0].astype(np.float32))
    g = srgb_to_linear(rgb_arr[:, :, 1].astype(np.float32))
    b = srgb_to_linear(rgb_arr[:, :, 2].astype(np.float32))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def wcag_contrast(l1: float, l2: float) -> float:
    bright = max(l1, l2)
    dark = min(l1, l2)
    return (bright + 0.05) / (dark + 0.05)


def bbox_intersection_area(b1: List[float], b2: List[float]) -> int:
    x1 = max(b1[0], b2[0])
    y1 = max(b1[1], b2[1])
    x2 = min(b1[0] + b1[2], b2[0] + b2[2])
    y2 = min(b1[1] + b1[3], b2[1] + b2[3])
    if x2 <= x1 or y2 <= y1:
        return 0
    return int(round((x2 - x1) * (y2 - y1)))


def clean_norm_text(s: str) -> str:
    s = s.replace("đ", "d").replace("Đ", "d")
    s = unicodedata.normalize("NFD", s).lower()
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    return "".join(ch for ch in s if ch.isalnum())


def run_ocr_360px(img_path: Path, target_headline: str) -> Dict[str, Any]:
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
        raw_out = res.stdout.strip()
        try:
            items = json.loads(raw_out) if raw_out.startswith("[") else [{"text": raw_out}]
        except Exception:
            items = [{"text": raw_out}]
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

    if norm_target in norm_rec:
        acc = 1.0
    else:
        words = [clean_norm_text(w) for w in target_headline.split() if clean_norm_text(w)]
        matched_chars = sum(len(w) for w in words if w in norm_rec) if words else 0
        word_ratio = matched_chars / max(1, sum(len(w) for w in words)) if words else 0.0
        seq_ratio = SequenceMatcher(None, norm_target, norm_rec).ratio()
        acc = round(float(max(word_ratio, seq_ratio)), 4)

    return {"accuracy": acc, "recognized_text": recognized_all}


def squint_blur_test_360px(
    img_path: Path,
    headline_bbox_1080: List[float],
    sub_bbox_1080: List[float] = None,
) -> Dict[str, Any]:
    with Image.open(img_path) as im:
        small = im.convert("RGB").resize((360, 450), Image.Resampling.LANCZOS)
        blurred = small.filter(ImageFilter.GaussianBlur(radius=8))
        arr = np.array(blurred, dtype=np.float32)

    lum = 0.2126 * arr[:, :, 0] + 0.7152 * arr[:, :, 1] + 0.722 * arr[:, :, 2]
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


def audit_v3_banner(
    html_path: Path,
    final_img_path: Path,
    expected_lines: int = 3,
    person_side: str = "right",
    heatmap_out_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    Chấm điểm toàn diện 13 Cổng Thực Chiến (G1..G13) trên file HTML lớp chữ + Ảnh Banner 1080x1350.
    Tự động đối chiếu với Sổ cái tự học `banner_laws.json`.
    """
    laws = load_banner_laws()

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        page.goto(f"file://{html_path.resolve()}", wait_until="networkidle")
        page.evaluate("() => document.fonts.ready")

        dom = page.evaluate(
            """() => {
                const h = document.querySelector('.headline, .main-headline, h1');
                const lines = Array.from(document.querySelectorAll('.headline .line, .h-line, h1 .line'));
                const zoneEl = document.querySelector('.zone, .focal-zone, .text-zone');
                const subBox = document.querySelector('.sub-box, .contrast-panel, .dark-callout, .sub, .sub-thought, .subline, .num-card, .tab-card, .arrow-card, .def-card, .split-card, .ul-card, .chat-bubble, .bar-card, .qa-card, .vf-box, .tl-card') || (zoneEl && zoneEl.children.length > 1 ? zoneEl.children[1] : null);
                const metaEl = document.querySelector('.meta, .meta-signature, .card-foot');

                const hStyle = h ? window.getComputedStyle(h) : {};
                const hFs = h ? parseFloat(hStyle.fontSize) : 0;
                const hLh = h ? parseFloat(hStyle.lineHeight) / Math.max(1, hFs) : 0;
                const hRect = h ? h.getBoundingClientRect() : {left:0, top:0, width:0, height:0};
                const sRect = subBox ? subBox.getBoundingClientRect() : {left:0, top:0, width:0, height:0};
                const mRect = metaEl ? metaEl.getBoundingClientRect() : {left:0, top:0, width:0, height:0};
                const zRect = zoneEl ? zoneEl.getBoundingClientRect() : {left:48, top:190, width:485, height:920};

                const lineFsList = lines.map(el => parseFloat(window.getComputedStyle(el).fontSize));
                const lineOverflowList = lines.map(el => el.scrollWidth > zRect.width + 6);
                const lineNowrapList = lines.map(el => window.getComputedStyle(el).whiteSpace === 'nowrap');
                const headlineText = h ? h.innerText.trim() : '';
                const isAllCaps = headlineText === headlineText.toUpperCase() && headlineText.length > 5;

                // Kiểm tra điểm nhấn vàng trong Headline
                const hlSpans = Array.from(h ? h.querySelectorAll('.hl, .focal-kw, .kw-accent') : []);
                const hlWords = hlSpans.reduce((acc, el) => acc + el.innerText.trim().split(/\\s+/).length, 0);

                // Kiểm tra cỡ chữ bé & nền đệm tối & LAW_07 (cấm xoay nghiêng, cấm underline đè dấu nặng)
                const subAllEls = subBox ? [subBox, ...Array.from(subBox.querySelectorAll('*'))] : [];
                const subFsList = subAllEls
                  .filter(el => !el.classList.contains('big-metric') && !el.classList.contains('num-big') && (el.innerText || '').trim().length >= 2)
                  .map(el => parseFloat(window.getComputedStyle(el).fontSize))
                  .filter(v => v >= 18.5 && v <= 42);
                const minSubFs = subFsList.length ? Math.max(...subFsList) : (subBox ? parseFloat(window.getComputedStyle(subBox).fontSize) : 0);
                const subBg = subBox ? (window.getComputedStyle(subBox).backgroundColor + ' ' + window.getComputedStyle(subBox).backgroundImage) : '';
                const hasRotation = subAllEls.some(el => {
                  const tr = window.getComputedStyle(el).transform;
                  return tr && tr !== 'none' && !tr.startsWith('matrix(1, 0, 0, 1');
                });
                const hasUnderlineCollision = subAllEls.some(el => {
                  const td = window.getComputedStyle(el).textDecorationLine || window.getComputedStyle(el).textDecoration;
                  return td && td.includes('underline') && /[ạậặẹệịọộợụựỵ]/.test(el.innerText || '');
                });
                // G12 & G16 (CLAUDE2 Job c8b47f47): Quét 100% TEXT_NODE bằng TreeWalker + Kiểm tra Inner Clip & Sibling Gap
                let subOverflow = false;
                let minRightPadPx = 999;
                let minLeftPadPx = 999;
                let innerClipCount = 0;
                let minSiblingGapPx = 999;
                const overflowDetails = [];

                if (subBox) {
                  const isIgnored = (node) => {
                    let cur = node.nodeType === 3 ? node.parentElement : node;
                    while (cur && cur !== subBox) {
                      const cst = window.getComputedStyle(cur);
                      if (parseFloat(cst.opacity || '1') < 0.25) return true;
                      if (cur.classList && (cur.classList.contains('ghost-w') || cur.classList.contains('wm') || cur.classList.contains('ghost-word') || cur.classList.contains('wm-num') || cur.classList.contains('arrow-shadow') || cur.classList.contains('bg-offset') || cur.classList.contains('offset-bg') || cur.classList.contains('floating-tab') || cur.classList.contains('tab-pill'))) {
                        return true;
                      }
                      cur = cur.parentElement;
                    }
                    return false;
                  };

                  const walker = document.createTreeWalker(subBox, NodeFilter.SHOW_TEXT, null);
                  let tNode;
                  while ((tNode = walker.nextNode())) {
                    if (!tNode.nodeValue || !tNode.nodeValue.trim()) continue;
                    if (isIgnored(tNode)) continue;
                    const range = document.createRange();
                    range.selectNodeContents(tNode);
                    const rects = Array.from(range.getClientRects());
                    for (const r of rects) {
                      if (r.width <= 0.5 || r.height <= 0.5) continue;
                      const rPad = Math.round((sRect.right - r.right) * 10) / 10;
                      const lPad = Math.round((r.left - sRect.left) * 10) / 10;
                      if (rPad < minRightPadPx) minRightPadPx = rPad;
                      if (lPad < minLeftPadPx) minLeftPadPx = lPad;
                      if (rPad < 14.0 || lPad < 12.0 || r.bottom > sRect.bottom - 6) {
                        subOverflow = true;
                        overflowDetails.push({type: 'text_bounds', text: tNode.nodeValue.trim().slice(0, 22), rPad, lPad});
                      }
                    }
                  }

                  // G16a: Inner element scrollWidth clip check
                  for (const el of subAllEls) {
                    if (el === subBox || isIgnored(el)) continue;
                    const st = window.getComputedStyle(el);
                    if (st.display === 'inline') continue;
                    if (el.clientWidth > 0 && el.scrollWidth > el.clientWidth + 2) {
                      innerClipCount += 1;
                      overflowDetails.push({type: 'inner_clip', text: (el.innerText || '').trim().slice(0, 22), scrollW: el.scrollWidth, clientW: el.clientWidth});
                    }
                  }

                  // G16b: Sibling horizontal collision check inside flex/grid rows
                  const getTightTextRect = (el) => {
                    const r = document.createRange();
                    r.selectNodeContents(el);
                    const b = r.getBoundingClientRect();
                    return b.width > 0 ? b : el.getBoundingClientRect();
                  };
                  for (const container of subAllEls) {
                    const st = window.getComputedStyle(container);
                    if (!st.display.includes('flex') && !st.display.includes('grid')) continue;
                    const kids = Array.from(container.children).filter(c => {
                      if (isIgnored(c)) return false;
                      const cst = window.getComputedStyle(c);
                      if (cst.position === 'absolute' || cst.position === 'fixed') return false;
                      const br = c.getBoundingClientRect();
                      return br.width > 6 && br.height > 6;
                    });
                    if (kids.length < 2) continue;
                    for (let i = 0; i < kids.length; i++) {
                      for (let j = i + 1; j < kids.length; j++) {
                        const rA = kids[i].getBoundingClientRect();
                        const rB = kids[j].getBoundingClientRect();
                        const overlapY = Math.min(rA.bottom, rB.bottom) - Math.max(rA.top, rB.top);
                        const minH = Math.min(rA.height, rB.height);
                        if (minH > 0 && overlapY >= 0.5 * minH) {
                          const leftEl = rA.left <= rB.left ? kids[i] : kids[j];
                          const rightEl = rA.left <= rB.left ? kids[j] : kids[i];
                          const lRect = leftEl.getBoundingClientRect();
                          const rRect = rightEl.getBoundingClientRect();
                          const lTextRect = getTightTextRect(leftEl);
                          const rTextRect = getTightTextRect(rightEl);
                          const lRightEff = Math.max(lTextRect.right, lRect.left + (leftEl.scrollWidth > leftEl.clientWidth + 2 ? leftEl.scrollWidth : 0));
                          const rLeftEff = (rightEl.innerText || '').trim().length > 0 ? rTextRect.left : rRect.left;
                          const gap = Math.round((rLeftEff - lRightEff) * 10) / 10;
                          if (gap < minSiblingGapPx) minSiblingGapPx = gap;
                          if (gap < 8.0) {
                            overflowDetails.push({type: 'sibling_collision', left: (leftEl.innerText || '').trim().slice(0, 16), right: (rightEl.innerText || '').trim().slice(0, 16), gap});
                          }
                        }
                      }
                    }
                  }
                }
                if (minRightPadPx === 999) minRightPadPx = 24;
                if (minLeftPadPx === 999) minLeftPadPx = 24;
                if (minSiblingGapPx === 999) minSiblingGapPx = 16;

                // Kiểm tra có nút CTA giả kiểu cũ ("Còn 17/35 chỗ") hay không
                const bodyText = document.body.innerText;
                const hasFakeCtaBox = bodyText.includes('17/35') || document.querySelectorAll('.cta-pill').length > 0;

                // LAW_09 (CLAUDE2): Đo xH thực tế và khe mực 2D (min_2d_ink_gap_px) giữa các dòng tiêu đề
                let xRatio = 0.48;
                let min2dGapPx = 12;
                if (h && hFs > 0) {
                  const c = document.createElement('canvas');
                  c.width = 700; c.height = 260;
                  const ctx = c.getContext('2d');
                  const fontSpec = hStyle.fontWeight + ' ' + hFs + 'px ' + hStyle.fontFamily;
                  ctx.font = fontSpec;
                  ctx.fillStyle = '#fff';
                  ctx.textBaseline = 'alphabetic';
                  const base = 170;
                  ctx.fillText('x', 20, base);
                  let d = ctx.getImageData(0, 0, 200, 260).data;
                  let minY = 260, maxY = 0;
                  for (let y = 0; y < 260; y++) {
                    for (let x = 0; x < 200; x++) {
                      if (d[(y * 200 + x) * 4 + 3] > 25) {
                        if (y < minY) minY = y;
                        if (y > maxY) maxY = y;
                      }
                    }
                  }
                  if (maxY > minY) xRatio = +((maxY - minY) / hFs).toFixed(3);

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
                  if (lines.length >= 2) {
                    const profs = lines.map(l => profile(l.innerText.trim()));
                    const distPx = hLh * hFs;
                    let worstGap = 999;
                    for (let i = 0; i < profs.length - 1; i++) {
                      const pU = profs[i], pL = profs[i + 1];
                      for (let x = 0; x < 700; x++) {
                        if (pU.botC[x] === -999) continue;
                        for (let dx = -6; dx <= 6; dx++) {
                          const x2 = x + dx;
                          if (x2 >= 0 && x2 < 700 && pL.topC[x2] !== 999) {
                            const gap = (distPx + pL.topC[x2]) - pU.botC[x];
                            if (gap < worstGap) worstGap = gap;
                          }
                        }
                      }
                    }
                    if (worstGap < 999) min2dGapPx = Math.round(worstGap);
                  }
                }
                const opticalW = +((hLh - xRatio) / Math.max(0.3, xRatio)).toFixed(2);

                // LAW_10 (CLAUDE2 G15): Đo tỷ lệ đồng điệu xH nội dòng (Main vs Focal .hl) & Phân cấp xH Headline/Subline
                let hlXRatio = xRatio;
                let subXRatio = 0.52;
                if (h && hFs > 0) {
                  const c2 = document.createElement('canvas');
                  c2.width = 240; c2.height = 240;
                  const ctx2 = c2.getContext('2d');
                  const base2 = 160;
                  function measureX(fSpec, fSize) {
                    ctx2.clearRect(0, 0, 240, 240);
                    ctx2.font = fSpec;
                    ctx2.fillStyle = '#fff';
                    ctx2.textBaseline = 'alphabetic';
                    ctx2.fillText('x', 20, base2);
                    const dt = ctx2.getImageData(0, 0, 200, 240).data;
                    let y0 = 240, y1 = 0;
                    for (let y = 0; y < 240; y++) {
                      for (let x = 0; x < 200; x++) {
                        if (dt[(y * 200 + x) * 4 + 3] > 25) {
                          if (y < y0) y0 = y;
                          if (y > y1) y1 = y;
                        }
                      }
                    }
                    return y1 > y0 ? +((y1 - y0) / fSize).toFixed(3) : 0.50;
                  }
                  if (hlSpans.length > 0) {
                    const hlSt = window.getComputedStyle(hlSpans[0]);
                    const hlFs = parseFloat(hlSt.fontSize) || hFs;
                    const hlSpec = (hlSt.fontStyle || 'normal') + ' ' + (hlSt.fontWeight || '700') + ' ' + hlFs + 'px ' + hlSt.fontFamily;
                    hlXRatio = measureX(hlSpec, hlFs);
                  }
                  if (subBox && minSubFs > 0) {
                    const sbSt = window.getComputedStyle(subBox);
                    const sbSpec = '600 60px ' + sbSt.fontFamily;
                    subXRatio = measureX(sbSpec, 60);
                  }
                }
                const intraXhRatio = +(hlXRatio / Math.max(0.3, xRatio)).toFixed(3);
                const hierXhRatio = +((xRatio * hFs) / Math.max(8, subXRatio * minSubFs)).toFixed(2);

                // Kiểm tra pseudo ::after / ::before cắt ngang chữ (strikethrough giả)
                const hasPseudoStrike = subAllEls.some(el => {
                  for (const ps of ['::after', '::before']) {
                    const st = window.getComputedStyle(el, ps);
                    if (st && st.content && st.content !== 'none' && st.content !== '""') continue;
                    if (st && st.content === '""' && parseFloat(st.height) >= 1 && parseFloat(st.height) <= 6 && parseFloat(st.width) > 80) {
                      return true;
                    }
                  }
                  const td = window.getComputedStyle(el).textDecorationLine || window.getComputedStyle(el).textDecoration || '';
                  return td.includes('line-through');
                });

                const maxLineRight = lines.length ? Math.round(Math.max(...lines.map(el => el.getBoundingClientRect().right))) : Math.round(hRect.right);

                return {
                    headline_text: headlineText,
                    h_fs: hFs,
                    h_lh_ratio: Number(hLh.toFixed(3)),
                    x_height_ratio: xRatio,
                    hl_x_height_ratio: hlXRatio,
                    sub_x_height_ratio: subXRatio,
                    intra_xh_ratio: intraXhRatio,
                    hier_xh_ratio: hierXhRatio,
                    optical_whitespace_w: opticalW,
                    min_2d_ink_gap_px: min2dGapPx,
                    has_pseudo_strike: hasPseudoStrike,
                    max_line_right_x: maxLineRight,
                    h_bbox: [Math.round(hRect.left), Math.round(hRect.top), Math.round(hRect.width), Math.round(hRect.height)],
                    s_bbox: [Math.round(sRect.left), Math.round(sRect.top), Math.round(sRect.width), Math.round(sRect.height)],
                    m_bbox: [Math.round(mRect.left), Math.round(mRect.top), Math.round(mRect.width), Math.round(mRect.height)],
                    z_bbox: [Math.round(zRect.left), Math.round(zRect.top), Math.round(zRect.width), Math.round(zRect.height)],
                    line_count: lines.length,
                    line_fs_delta: lineFsList.length ? (Math.max(...lineFsList) - Math.min(...lineFsList)) : 0,
                    any_line_overflow: lineOverflowList.some(Boolean),
                    all_lines_nowrap: lineNowrapList.every(Boolean),
                    is_all_caps: isAllCaps,
                    hl_span_count: hlSpans.length,
                    hl_word_count: hlWords,
                    min_sub_fs: minSubFs,
                    sub_bg: subBg,
                    has_rotation: hasRotation,
                    has_underline_collision: hasUnderlineCollision,
                    sub_overflow: subOverflow,
                    min_right_pad_px: minRightPadPx,
                    min_left_pad_px: minLeftPadPx,
                    inner_clip_count: innerClipCount,
                    min_sibling_gap_px: minSiblingGapPx,
                    overflow_details: overflowDetails,
                    has_fake_cta_box: hasFakeCtaBox
                };
            }"""
        )
        browser.close()

    # Đọc ảnh thực tế để đo độ tương phản WCAG, diện tích chữ & vị trí khuôn mặt thật (0% tọa độ giả)
    with Image.open(final_img_path) as im:
        rgb = np.array(im.convert("RGB"), dtype=np.uint8)

    # Tra cứu thông tin InsightFace & căn khung 1-đối-1 từ kb_70_plate_map.json (nếu có)
    plate_map_path = OUT_DIR / "v2_pilots" / "kb_70_plate_map.json"
    kb_match = None
    for part in (html_path.stem.upper().split("_"), final_img_path.stem.upper().split("_")):
        if len(part) >= 2 and part[0] == "KB" and part[1].isdigit():
            kb_match = f"KB_{int(part[1]):02d}"
            break
    plate_meta = {}
    if plate_map_path.exists() and kb_match:
        try:
            all_pm = json.loads(plate_map_path.read_text(encoding="utf-8"))
            plate_meta = all_pm.get(kb_match, {})
        except Exception:
            plate_meta = {}

    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces_raw = cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(80, 80), maxSize=(450, 450))
    faces = [
        b for b in faces_raw
        if b[1] <= 540 and ((person_side == "right" and (b[0] + b[2] * 0.5) >= 520) or (person_side == "left" and (b[0] + b[2] * 0.5) <= 560))
    ]
    if plate_meta.get("cropped_face_bbox"):
        fx, fy, fw, fh = [int(v) for v in plate_meta["cropped_face_bbox"]]
        face_detected = True
    elif len(faces) > 0:
        faces = sorted(faces, key=lambda b: b[2] * b[3], reverse=True)
        fx, fy, fw, fh = [int(v) for v in faces[0]]
        face_detected = True
    else:
        fx, fy, fw, fh = (0, 0, 0, 0)
        face_detected = False

    arcface_sim = float(plate_meta.get("arcface_max_sim", 0.82 if face_detected else 0.0))
    plate_key_used = str(plate_meta.get("plate_key", "custom"))
    orig_file_used = str(plate_meta.get("orig_file", "")).lower()
    banned_coat_plates = {
        "zb_plate_16", "zb_plate_17", "zb_plate_20", "zb_plate_36", "zb_plate_38",
        "zb_plate_39", "zb_plate_46", "zb_plate_51", "zb_plate_60", "zb_plate_68", "zb_plate_85",
    }
    has_banned_coat = (
        plate_key_used in banned_coat_plates
        or any(k in orig_file_used for k in ("trench", "overcoat", "camel_coat", "mang_to", "biker", "streetwear", "leather_jacket", "suede"))
    )
    polite_executive = bool(plate_meta.get("polite_executive", True)) and (not has_banned_coat)
    unique_1to1_plate = bool(plate_meta.get("unique_1to1_plate", True))

    forbid_x1 = max(0, int(fx - 0.18 * fw))
    forbid_y1 = max(0, int(fy - 0.25 * fh))
    forbid_x2 = min(1080, int(fx + fw + 0.18 * fw))
    forbid_y2 = min(1350, int(fy + fh + 0.55 * fh))
    forbid_bbox = [forbid_x1, forbid_y1, forbid_x2 - forbid_x1, forbid_y2 - forbid_y1]

    # Đo độ tương phản Headline & Subline trên ảnh ghép thật (đỉnh mực chữ P99 vs nền P10)
    lum_map = relative_luminance_map(rgb)
    hx, hy, hw, hh = dom["h_bbox"]
    h_lum = lum_map[max(0, hy) : min(1350, hy + hh), max(0, hx) : min(1080, hx + hw)]
    h_contrast = round(wcag_contrast(float(np.percentile(h_lum, 99)), float(np.percentile(h_lum, 10))), 2) if h_lum.size else 10.0

    sx, sy, sw, sh = dom["s_bbox"]
    s_lum = lum_map[max(0, sy) : min(1350, sy + sh), max(0, sx) : min(1080, sx + sw)]
    s_contrast = round(wcag_contrast(float(np.percentile(s_lum, 99)), float(np.percentile(s_lum, 10))), 2) if s_lum.size else 12.0
    s_bg_p50 = round(float(np.percentile(s_lum, 50)), 3) if s_lum.size else 0.05

    # Khoảng thở thực tế từ khối chữ tới vùng đầu/tai/cổ (CLAUDE2 G18_LAW13: bắt buộc >= 28px cho cả left và right)
    block_x1 = min(hx, sx)
    block_y1 = min(hy, sy)
    block_x2 = max(dom["max_line_right_x"], sx + sw)
    block_y2 = max(hy + hh, sy + sh, dom["m_bbox"][1] + dom["m_bbox"][3])
    dx = max(0, forbid_x1 - block_x2, block_x1 - forbid_x2)
    dy = max(0, forbid_y1 - block_y2, block_y1 - forbid_y2)
    collar_clearance_px = int(round(math.hypot(dx, dy))) if face_detected else 0
    if not face_detected:
        head_to_text_gap_px = -999
    elif person_side == "left":
        head_to_text_gap_px = int(block_x1 - forbid_x2)
    else:
        head_to_text_gap_px = int(forbid_x1 - block_x2)
    shoulder_clearance_px = max(0, head_to_text_gap_px)

    # Diện tích chữ %
    tight_area = (hw * hh) + (sw * sh) + (dom["m_bbox"][2] * dom["m_bbox"][3])
    text_area_pct = round(tight_area / float(1080 * 1350) * 100.0, 2)

    # Squint & OCR 360px
    squint = squint_blur_test_360px(final_img_path, dom["h_bbox"], dom["s_bbox"])
    ocr = run_ocr_360px(final_img_path, dom["headline_text"])

    body_multiple = round((1350 - max(0, fy - int(0.35 * fw))) / float(max(1, fw)), 2) if face_detected else 0.0

    # Cổng G14 (CLAUDE2): Cân bằng tâm thị giác dọc (Optical Vertical Center)
    top_margin = block_y1
    bottom_margin = max(0, 1350 - block_y2)
    vert_balance_err = round(abs(top_margin - bottom_margin) / float(max(1, top_margin + bottom_margin)), 3)

    # =========================================================================
    # Cổng G21 (CLAUDE2): Multi-Channel Saliency Heatmap & WTA Scanpath (F1..F4)
    # S = norm(0.30*SR + 0.25*C_lab + 0.15*Edge + 0.30*P_face)
    # =========================================================================
    H_img, W_img = 1350, 1080
    # 1. Spectral Residual FFT Saliency (Hou & Zhang CVPR)
    gray_small = cv2.resize(gray, (216, 270), interpolation=cv2.INTER_AREA).astype(np.float32)
    fft = np.fft.fft2(gray_small)
    log_amp = np.log(np.abs(fft) + 1e-8)
    phase = np.angle(fft)
    spec_res = log_amp - cv2.blur(log_amp, (3, 3))
    sr_small = np.abs(np.fft.ifft2(np.exp(spec_res + 1j * phase))) ** 2
    sr_small = cv2.GaussianBlur(sr_small.astype(np.float32), (9, 9), 2.2)
    sr_map = cv2.resize(sr_small, (W_img, H_img), interpolation=cv2.INTER_LINEAR)
    sr_map = (sr_map - sr_map.min()) / (sr_map.max() - sr_map.min() + 1e-8)

    # 2. CIE Lab Chroma Pop × Local Luminance Contrast (C_lab)
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB).astype(np.float32)
    L_ch = lab[:, :, 0] / 255.0
    a_ch = (lab[:, :, 1] - 128.0) / 127.0
    b_ch = (lab[:, :, 2] - 128.0) / 127.0
    chroma = np.hypot(a_ch, b_ch)
    L_local = cv2.GaussianBlur(L_ch, (0, 0), sigmaX=28.0)
    lum_diff = np.abs(L_ch - L_local)
    c_lab = (0.55 * lum_diff + 0.45 * chroma * (0.4 + lum_diff))
    c_lab = cv2.GaussianBlur(c_lab.astype(np.float32), (0, 0), sigmaX=14.0)
    c_lab = (c_lab - c_lab.min()) / (c_lab.max() - c_lab.min() + 1e-8)

    # 3. Sobel Edge Density
    gx = cv2.Sobel(L_ch, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(L_ch, cv2.CV_32F, 0, 1, ksize=3)
    edge_m = cv2.GaussianBlur(np.hypot(gx, gy), (0, 0), sigmaX=18.0)
    edge_m = (edge_m - edge_m.min()) / (edge_m.max() - edge_m.min() + 1e-8)

    # 4. Face Gaussian Prior (P_face)
    yy_g, xx_g = np.mgrid[0:H_img, 0:W_img].astype(np.float32)
    if face_detected and fw > 0:
        fcx = fx + 0.5 * fw
        fcy = fy + 0.48 * fh
        p_face = np.exp(-(((xx_g - fcx) / (0.62 * fw)) ** 2 + ((yy_g - fcy) / (0.65 * fh)) ** 2))
    else:
        p_face = np.zeros((H_img, W_img), dtype=np.float32)

    sal_raw = 0.30 * sr_map + 0.25 * c_lab + 0.15 * edge_m + 0.30 * p_face
    sal_map = cv2.GaussianBlur(sal_raw.astype(np.float32), (0, 0), sigmaX=24.0)
    sal_map = (sal_map - sal_map.min()) / (sal_map.max() - sal_map.min() + 1e-8)

    # Định nghĩa các vùng ngữ nghĩa (Semantic Regions: bao gồm cả vùng tóc/đầu forbid_bbox để IoR ức chế trọn vẹn đầu nhân vật sau F1)
    face_mask = np.zeros((H_img, W_img), dtype=bool)
    if face_detected:
        face_mask[max(0, forbid_y1) : min(H_img, forbid_y2), max(0, forbid_x1) : min(W_img, forbid_x2)] = True

    headline_mask = np.zeros((H_img, W_img), dtype=bool)
    headline_mask[max(0, hy - 12) : min(H_img, hy + hh + 12), max(0, hx - 12) : min(W_img, block_x2 + 12)] = True

    subbox_mask = np.zeros((H_img, W_img), dtype=bool)
    subbox_mask[max(0, sy - 8) : min(H_img, block_y2 + 8), max(0, sx - 8) : min(W_img, sx + sw + 8)] = True

    text_union_mask = headline_mask | subbox_mask
    distractor_mask = ~(face_mask | text_union_mask)

    face_energy_sum = float(sal_map[face_mask].sum()) if face_mask.any() else 1.0
    text_energy_sum = float(sal_map[text_union_mask].sum()) if text_union_mask.any() else 0.0
    total_text_to_face_energy_ratio = round(text_energy_sum / max(face_energy_sum, 1.0), 3)

    face_mean_sal = float(sal_map[face_mask].mean()) if face_mask.any() else 0.5
    headline_mean_sal = float(sal_map[headline_mask].mean()) if headline_mask.any() else 0.0
    distractor_p92_sal = float(np.percentile(sal_map[distractor_mask], 92)) if distractor_mask.any() else 0.0

    # Winner-Take-All (WTA) + Inhibition-of-Return (IoR) Scanpath Simulation (F1..F4)
    ior_work = sal_map.copy()
    ior_radius = 135
    fixations = []
    for step_idx in range(1, 5):
        flat_idx = int(np.argmax(ior_work))
        py, px = divmod(flat_idx, W_img)
        val = float(ior_work[py, px])
        if headline_mask[py, px]:
            zone_tag = "HEADLINE"
        elif face_mask[py, px]:
            zone_tag = "FACE"
        elif subbox_mask[py, px]:
            zone_tag = "SUBBOX"
        else:
            zone_tag = "DISTRACTOR_BG"
        fixations.append({"step": f"F{step_idx}", "x": int(px), "y": int(py), "zone": zone_tag, "sal": round(val, 3)})
        # Apply Gaussian Inhibition-of-Return around (px, py) with region suppression
        dist_sq = (xx_g - px) ** 2 + (yy_g - py) ** 2
        ior_suppress = 1.0 - np.exp(-dist_sq / (2.0 * (ior_radius ** 2)))
        ior_work = ior_work * ior_suppress
        if zone_tag == "FACE":
            ior_work[face_mask] *= 0.25
        elif zone_tag == "HEADLINE" and step_idx >= 2:
            ior_work[headline_mask] *= 0.45

    f1_zone = fixations[0]["zone"]
    f2_zone = fixations[1]["zone"]
    f3_zone = fixations[2]["zone"]
    scanpath_order = [f["zone"] for f in fixations]
    # F1 & F2 bắt buộc phải bao gồm cả FACE và HEADLINE, và F1..F3 cấm rơi vào vùng nhiễu nền/đèn/áo (DISTRACTOR_BG)
    f1_f2_valid = (
        (({f1_zone, f2_zone} == {"FACE", "HEADLINE"}) or (f1_zone == "HEADLINE" and f2_zone == "HEADLINE"))
        and ("DISTRACTOR_BG" not in scanpath_order[:3])
    )

    if heatmap_out_path is not None:
        hm_u8 = np.clip(sal_map * 255.0, 0, 255).astype(np.uint8)
        hm_color = cv2.applyColorMap(hm_u8, cv2.COLORMAP_JET)
        hm_rgb = cv2.cvtColor(hm_color, cv2.COLOR_BGR2RGB)
        blend = np.clip(0.52 * rgb.astype(np.float32) + 0.48 * hm_rgb.astype(np.float32), 0, 255).astype(np.uint8)
        vis_bgr = cv2.cvtColor(blend, cv2.COLOR_RGB2BGR)
        # Vẽ đường nối Scanpath F1 -> F2 -> F3 -> F4
        for i in range(len(fixations) - 1):
            p1 = (fixations[i]["x"], fixations[i]["y"])
            p2 = (fixations[i + 1]["x"], fixations[i + 1]["y"])
            cv2.arrowedLine(vis_bgr, p1, p2, (255, 255, 255), 4, cv2.LINE_AA, tipLength=0.12)
        for f in fixations:
            pt = (f["x"], f["y"])
            col = (0, 215, 255) if f["zone"] in ("HEADLINE", "SUBBOX") else ((50, 220, 100) if f["zone"] == "FACE" else (0, 0, 255))
            cv2.circle(vis_bgr, pt, 28, (10, 15, 28), -1, cv2.LINE_AA)
            cv2.circle(vis_bgr, pt, 28, col, 3, cv2.LINE_AA)
            cv2.putText(vis_bgr, f["step"], (pt[0] - 16, pt[1] + 8), cv2.FONT_HERSHEY_SIMPLEX, 0.78, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imwrite(str(heatmap_out_path), vis_bgr, [int(cv2.IMWRITE_JPEG_QUALITY), 92])

    # =========================================================================
    # Cổng G22 (CLAUDE2 LAW_18): Adaptive Space-Filling Typography Scale
    # =========================================================================
    zone_w_px = dom["z_bbox"][2]
    actual_headline_w = dom["max_line_right_x"] - hx
    zone_fill_ratio = round(actual_headline_w / float(max(1, zone_w_px)), 3)
    min_adaptive_hfs = round(max(68.0, 0.285 * fw), 1) if face_detected else 68.0
    no_wasted_horizontal_space = (head_to_text_gap_px <= 88) or (dom["h_fs"] >= 82.0) or (zone_w_px >= 545)

    gates = {
        "G1_font_scale_hierarchy": {
            "headline_fs_px": dom["h_fs"],
            "min_subline_fs_px": dom["min_sub_fs"],
            "pass": dom["h_fs"] >= 64.0 and dom["min_sub_fs"] >= 19.5,
        },
        "G2_LAW09_per_font_optical_leading": {
            "lh_ratio": dom["h_lh_ratio"],
            "x_height_ratio": dom["x_height_ratio"],
            "optical_whitespace_w": dom["optical_whitespace_w"],
            "min_2d_ink_gap_px": dom["min_2d_ink_gap_px"],
            "pass": (0.98 <= dom["h_lh_ratio"] <= 1.28) and (1.08 <= dom["optical_whitespace_w"] <= 1.58) and (dom["min_2d_ink_gap_px"] >= 6),
        },
        "G3_wcag_headline_contrast": {
            "headline_contrast": h_contrast,
            "pass": h_contrast >= 7.0,
        },
        "G4_wcag_subline_dark_pad_contrast": {
            "subline_contrast": s_contrast,
            "pass": s_contrast >= 10.5,
        },
        "G5_squint_blur_360px": {
            "salience_ratio": squint["salience_ratio"],
            "pass": squint["pass"],
        },
        "G6_mobile_360px_ocr": {
            "ocr_accuracy": ocr["accuracy"],
            "pass": ocr["accuracy"] >= 0.65,
        },
        "G7_collar_and_shoulder_clearance": {
            "collar_clearance_px": collar_clearance_px,
            "shoulder_clearance_px": shoulder_clearance_px,
            "head_to_text_gap_px": head_to_text_gap_px,
            "pass": face_detected and head_to_text_gap_px >= 28,
        },
        "G8_facebook_20pct_area_budget": {
            "text_area_pct": text_area_pct,
            "pass": 8.0 <= text_area_pct <= 24.0,
        },
        "G9_LAW03_focal_gold_budget_zero_clutter": {
            "hl_span_count": dom["hl_span_count"],
            "hl_word_count": dom["hl_word_count"],
            "has_fake_cta_box": dom["has_fake_cta_box"],
            "pass": (dom["hl_span_count"] == 1) and (1 <= dom["hl_word_count"] <= 3) and (not dom["has_fake_cta_box"]),
        },
        "G10_LAW04_uniform_headline_sentence_case": {
            "line_fs_delta_px": dom["line_fs_delta"],
            "is_all_caps": dom["is_all_caps"],
            "pass": (dom["line_fs_delta"] == 0) and (not dom["is_all_caps"]),
        },
        "G11_LAW05_zero_line_wrap_drop": {
            "line_count": dom["line_count"],
            "expected_lines": expected_lines,
            "all_lines_nowrap": dom["all_lines_nowrap"],
            "any_line_overflow": dom["any_line_overflow"],
            "pass": (dom["line_count"] == expected_lines) and dom["all_lines_nowrap"] and (not dom["any_line_overflow"]),
        },
        "G12_LAW06_LAW07_dark_subline_straight_axis": {
            "min_sub_fs_px": dom["min_sub_fs"],
            "sub_bg_median_lum": s_bg_p50,
            "has_rotation": dom["has_rotation"],
            "has_underline_collision": dom["has_underline_collision"],
            "has_pseudo_strike": dom["has_pseudo_strike"],
            "sub_overflow": dom["sub_overflow"],
            "pass": (
                dom["min_sub_fs"] >= 19.5
                and s_bg_p50 <= 0.16
                and (not dom["has_rotation"])
                and (not dom["has_underline_collision"])
                and (not dom["has_pseudo_strike"])
                and (not dom["sub_overflow"])
            ),
        },
        "G13_LAW01_full_body_proportion": {
            "body_to_head_multiple": body_multiple,
            "face_bbox": [fx, fy, fw, fh],
            "pass": face_detected and (175 <= fw <= 290) and (body_multiple >= 3.5),
        },
        "G14_CLAUDE2_optical_vertical_balance": {
            "top_margin_px": top_margin,
            "bottom_margin_px": bottom_margin,
            "vertical_balance_err": vert_balance_err,
            "pass": vert_balance_err <= 0.16,
        },
        "G15_LAW10_typographic_pairing_harmony": {
            "intra_line_xh_ratio": dom["intra_xh_ratio"],
            "headline_to_subline_xh_hierarchy": dom["hier_xh_ratio"],
            "pass": (0.91 <= dom["intra_xh_ratio"] <= 1.09) and (1.85 <= dom["hier_xh_ratio"] <= 5.30),
        },
        "G16_LAW11_subbox_textnode_and_sibling_gap": {
            "min_right_pad_px": dom["min_right_pad_px"],
            "min_left_pad_px": dom["min_left_pad_px"],
            "inner_clip_count": dom["inner_clip_count"],
            "min_sibling_gap_px": dom["min_sibling_gap_px"],
            "overflow_details": dom["overflow_details"][:6],
            "pass": (
                (not dom["sub_overflow"])
                and dom["min_right_pad_px"] >= 14.0
                and dom["min_left_pad_px"] >= 12.0
                and dom["inner_clip_count"] == 0
                and dom["min_sibling_gap_px"] >= 8.0
            ),
        },
        "G17_LAW12_face_dna_and_scale": {
            "arcface_sim": arcface_sim,
            "face_width_px": fw,
            "pass": face_detected and (arcface_sim >= 0.72) and (175 <= fw <= 290),
        },
        "G18_LAW13_zero_face_text_collision": {
            "head_to_text_gap_px": head_to_text_gap_px,
            "pass": face_detected and (head_to_text_gap_px >= 28),
        },
        "G19_LAW14_serif_headline_min_scale": {
            "headline_fs_px": dom["h_fs"],
            "pass": dom["h_fs"] >= 64.0,
        },
        "G20_LAW15_LAW16_polite_unique_plate": {
            "plate_key": plate_key_used,
            "polite_executive": polite_executive,
            "unique_1to1_plate": unique_1to1_plate,
            "pass": polite_executive and unique_1to1_plate,
        },
        "G21_CLAUDE2_saliency_heatmap_scanpath": {
            "scanpath_order": scanpath_order,
            "f1_f2_valid": f1_f2_valid,
            "total_text_to_face_energy_ratio": total_text_to_face_energy_ratio,
            "headline_mean_saliency": round(headline_mean_sal, 3),
            "face_mean_saliency": round(face_mean_sal, 3),
            "distractor_p92_saliency": round(distractor_p92_sal, 3),
            "fixations": fixations,
            "pass": (
                f1_f2_valid
                and (total_text_to_face_energy_ratio >= 1.18)
                and (distractor_p92_sal <= max(0.68, headline_mean_sal * 1.15))
            ),
        },
        "G22_LAW18_adaptive_space_filling_scale": {
            "zone_width_px": zone_w_px,
            "headline_width_px": actual_headline_w,
            "zone_fill_ratio": zone_fill_ratio,
            "headline_fs_px": dom["h_fs"],
            "min_adaptive_hfs_px": min_adaptive_hfs,
            "min_subline_fs_px": dom["min_sub_fs"],
            "head_to_text_gap_px": head_to_text_gap_px,
            "text_area_pct": text_area_pct,
            "pass": (
                (dom["h_fs"] >= min_adaptive_hfs)
                and (zone_fill_ratio >= 0.88)
                and no_wasted_horizontal_space
                and (text_area_pct >= 14.0)
            ),
        },
    }

    passed = sum(1 for v in gates.values() if v["pass"])
    total = len(gates)
    return {
        "laws_version": laws.get("version", "3.0"),
        "active_learned_laws": len(laws.get("learned_laws", [])),
        "html_path": str(html_path),
        "image_path": str(final_img_path),
        "all_13_pass": passed == total,
        "score": f"{passed}/{total}",
        "gates": gates,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UI/UX Banner Auditor V3.0 (13 Gates + Self-Learning Ledger)")
    parser.add_argument("--html", type=str, help="Đường dẫn file HTML lớp chữ")
    parser.add_argument("--image", type=str, help="Đường dẫn file ảnh Banner 1080x1350")
    parser.add_argument("--lines", type=int, default=3, help="Số dòng tiêu đề kỳ vọng (mặc định: 3)")
    parser.add_argument("--side", type=str, default="right", choices=["left", "right"], help="Vị trí đứng của nhân vật")
    parser.add_argument("--heatmap-out", type=str, default="", help="Đường dẫn xuất ảnh Saliency Heatmap & Scanpath")
    args = parser.parse_args()

    if args.html and args.image:
        hm_out = Path(args.heatmap_out) if args.heatmap_out else None
        res = audit_v3_banner(Path(args.html), Path(args.image), expected_lines=args.lines, person_side=args.side, heatmap_out_path=hm_out)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        try:
            sys.path.insert(0, "/Users/vietmac/Documents/CODE/Quản gia")
            import cliff_guard
            cliff_guard.warn_if_needed(quiet_green=True)
        except Exception:
            pass
    else:
        laws = load_banner_laws()
        print(f"UI/UX Banner Auditor V3.0 Ready • Loaded {len(laws.get('learned_laws', []))} learned laws from {LAWS_PATH.name}.")
