#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RENDER V3 PRICE BANNERS PART 2 (KB_71 -> KB_140) WITH EDITORIAL META STRIP (M01 / M02) & 25/25 GATE AUTO-HEAL
==============================================================================================================
- Xử lý từ `KB_71` đến `KB_140`:
  + Đọc `banner2_cards/KB_XX.json` và `kb_31_master_specs.json` (nếu chưa có gọi `ensure_default_spec_for_new_kb`).
  + Lấy thông số `hook_1` từ `banner2_cards/KB_XX.json`, gắn `spec["meta_code"] = "M01"` hoặc `"M02"`.
  + Gọi `build_style_html(style_code, spec, master)` và `render_overlay_png_on_page(page, html_str, html_v3_path, ov_png_path, frame_meta=frame_meta, side=side)`.
  + Ghép lên nền `DUAL_BG_DIR / f"{kb_lower}_color_bg.jpg"` (nếu chưa có gọi `build_dual_zero_blur_bgs`), xuất ra `v2_pilots/batch_out/{kb_lower}_v3_price.jpg`.
  + Chạy `audit_v3_banner(html_path=html_v3_path, final_img_path=v3_jpg_path, expected_lines=3, person_side=side)` kiểm tra 25 cổng (`G1..G25`).
  + Cơ chế Auto-Heal tức thì nếu có cổng trượt (`G22`, `G7`, `G18`, `G6`, `G8`, `G14`, `G21`...) cho tới khi đạt `25/25 PASS`.
- Lưu báo cáo kết quả của `KB_71..KB_140` vào `/tmp/v3_render_part2.json` (không sửa `banner2_cards/KB_XX.json`).
"""

import argparse
import concurrent.futures
import copy
import json
import re
import sys
import time
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from PIL import Image
from playwright.sync_api import sync_playwright

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
SPECS_PATH = BASE_DIR / "kb_31_master_specs.json"
CARDS_DIR = BASE_DIR / "banner2_cards"
PILOT_DIR = BASE_DIR / "v2_pilots"
DUAL_BG_DIR = PILOT_DIR / "dual_bg_70"
OUT_RENDER_DIR = PILOT_DIR / "batch_out"
ZB_PLATES_DIR = PILOT_DIR / "zero_blur_plates"

sys.path.insert(0, str(BASE_DIR))
from batch_branch_runner import build_style_html
from uiux_auditor import audit_v3_banner
from zero_blur_dual_pipeline import (
    harvest_generated_plates,
    build_dual_zero_blur_bgs,
    render_overlay_png_on_page,
    KB_TO_PLATE_ASSIGNMENT,
)
from apply_claude2_stage import populate_hook_spec, ensure_default_spec_for_new_kb

# Bảng ánh xạ in-memory cho các KB trong KB_71..KB_140 mà kb_XX_color_bg.jpg được tạo từ zb_plate_XX.jpg
ZB_PLATE_OVERRIDE: Dict[str, str] = {
    "KB_71": "zb_plate_64.jpg",
    "KB_74": "zb_plate_40.jpg",
    "KB_85": "zb_plate_47.jpg",
    "KB_93": "zb_plate_81.jpg",
    "KB_100": "zb_plate_kb14_japandi_01.jpg",
    "KB_101": "zb_plate_30.jpg",
    "KB_102": "zb_plate_43.jpg",
    "KB_103": "zb_plate_34.jpg",
    "KB_104": "zb_plate_56.jpg",
    "KB_106": "zb_plate_06.jpg",
    "KB_111": "zb_plate_55.jpg",
    "KB_113": "zb_plate_53.jpg",
    "KB_116": "zb_plate_32.jpg",
    "KB_123": "zb_plate_59.jpg",
    "KB_128": "zb_plate_76.jpg",
    "KB_130": "zb_plate_52.jpg",
    "KB_138": "zb_plate_45.jpg",
    "KB_139": "zb_plate_87.jpg",
}

_ORIG_READ_TEXT = Path.read_text


def _patched_read_text(self: Path, *args, **kwargs) -> str:
    raw = _ORIG_READ_TEXT(self, *args, **kwargs)
    if self.name == "kb_70_plate_map.json":
        try:
            data = json.loads(raw)
            for k, zp_name in ZB_PLATE_OVERRIDE.items():
                if k in data:
                    zp_full = ZB_PLATES_DIR / zp_name
                    if zp_full.exists():
                        data[k]["plate_path"] = str(zp_full)
                        data[k]["plate_key"] = zp_full.stem
            return json.dumps(data, ensure_ascii=False)
        except Exception:
            return raw
    return raw


Path.read_text = _patched_read_text


def clean_sub_emoji(s: str) -> str:
    if not s:
        return ""
    return re.sub(r"^[❌✅✖✔✗✓\s]+", "", str(s)).strip()


def render_v3_overlay_with_cfg(
    page,
    html_str: str,
    html_out_path: Path,
    overlay_png_path: Path,
    frame_meta: Optional[Dict[str, Any]] = None,
    side: str = "right",
    override_zone_w: Optional[int] = None,
    override_zone_left: Optional[int] = None,
    override_forbid_x1: Optional[int] = None,
    override_forbid_x2: Optional[int] = None,
    target_gap_px: int = 42,
    compact_pad: bool = False,
    boost_subbox_sal: bool = False,
) -> Dict[str, Any]:
    """
    Gọi `render_overlay_png_on_page` chuẩn và áp dụng tinh chỉnh động `dyn_zone_w` / `dyn_zone_left`
    + căn tâm dọc 50/50 chuẩn G14/G22/G7/G18 ngay trên cùng `page`.
    """
    eff_frame_meta = copy.deepcopy(frame_meta) if frame_meta else {}
    if override_forbid_x1 is not None and side == "right" and eff_frame_meta.get("cropped_face_bbox"):
        fx, fy, fw, fh = [float(v) for v in eff_frame_meta["cropped_face_bbox"]]
        eff_frame_meta["cropped_face_bbox"] = [override_forbid_x1 + 0.18 * fw, fy, fw, fh]
    elif override_forbid_x2 is not None and side == "left" and eff_frame_meta.get("cropped_face_bbox"):
        fx, fy, fw, fh = [float(v) for v in eff_frame_meta["cropped_face_bbox"]]
        eff_frame_meta["cropped_face_bbox"] = [override_forbid_x2 - 1.18 * fw, fy, fw, fh]

    # Bước 1: Chạy render_overlay_png_on_page gốc theo đúng hợp đồng
    render_overlay_png_on_page(
        page,
        html_str,
        html_out_path,
        overlay_png_path,
        frame_meta=eff_frame_meta,
        side=side,
    )

    forbid_x1 = 0
    forbid_x2 = 0
    if frame_meta and frame_meta.get("cropped_face_bbox"):
        fx, fy, fw, fh = [float(v) for v in frame_meta["cropped_face_bbox"]]
        forbid_x1 = max(0, int(fx - 0.18 * fw))
        forbid_x2 = min(1080, int(fx + fw + 0.18 * fw))
    if override_forbid_x1 is not None:
        forbid_x1 = override_forbid_x1
    if override_forbid_x2 is not None:
        forbid_x2 = override_forbid_x2

    dyn_zone_w = override_zone_w
    dyn_zone_left = override_zone_left
    if dyn_zone_w is None:
        if forbid_x1 > 0 and side == "right":
            avail_w = int(round(forbid_x1 - target_gap_px - 44))
            dyn_zone_w = max(476, min(588, avail_w))
        elif forbid_x2 > 0 and side == "left":
            avail_w = int(round(1080 - 44 - (forbid_x2 + target_gap_px)))
            dyn_zone_w = max(476, min(588, avail_w))
        else:
            dyn_zone_w = 512

    # Bước 2: Tinh chỉnh chuẩn xác zone_w, zone_left, meta-v3 và optical vertical balance trên page
    fit_info = page.evaluate(
        """(cfg) => {
            const h = document.querySelector('.headline');
            const zone = document.querySelector('.zone');
            const subBox = document.querySelector('.sub-box');
            const metaV3 = document.querySelector('.meta.meta-v3');
            const lines = Array.from(document.querySelectorAll('.headline .line'));

            if (cfg.compact_pad) {
                if (h) h.style.marginBottom = '26px';
                if (subBox) {
                    subBox.style.marginBottom = '26px';
                    subBox.style.paddingTop = '15px';
                    subBox.style.paddingBottom = '15px';
                }
            }
            if (cfg.boost_subbox_sal && subBox) {
                subBox.style.border = '2.5px solid #FACC15';
                subBox.style.boxShadow = '0 0 0 1px rgba(250,204,21,0.35), 0 18px 40px rgba(0,0,0,0.65)';
            }

            let curZoneW = cfg.dyn_zone_w || 512;
            if (zone) {
                zone.style.width = curZoneW + 'px';
            }
            if (subBox) {
                subBox.style.width = curZoneW + 'px';
                subBox.style.maxWidth = curZoneW + 'px';
                subBox.style.boxSizing = 'border-box';
            }
            if (metaV3) {
                metaV3.style.width = curZoneW + 'px';
                metaV3.style.maxWidth = curZoneW + 'px';
                metaV3.style.boxSizing = 'border-box';
            }

            lines.forEach(l => { l.style.width = 'fit-content'; });

            function fitHeadlineForWidth(zW) {
                const maxLineW = zW - 2;
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
                curMaxW = Math.max(...lines.map(l => Math.max(l.scrollWidth, l.getBoundingClientRect().width)));
                if (curMaxW > maxLineW) {
                    h.style.letterSpacing = '-0.04em';
                    lines.forEach(l => { l.style.letterSpacing = '-0.04em'; });
                }
                return fs;
            }

            let fs = fitHeadlineForWidth(curZoneW);
            let actualHeadW = Math.ceil(Math.max(...lines.map(l => l.getBoundingClientRect().width)));

            // Khép nhẹ curZoneW nếu tiêu đề ngắn (đã đạt 104px) để zone_fill_ratio >= 0.935 (G22)
            if (!cfg.explicit_zone_w && actualHeadW < curZoneW * 0.935) {
                curZoneW = Math.max(464, Math.min(curZoneW, Math.ceil(actualHeadW / 0.95)));
                if (zone) zone.style.width = curZoneW + 'px';
                if (subBox) {
                    subBox.style.width = curZoneW + 'px';
                    subBox.style.maxWidth = curZoneW + 'px';
                }
                if (metaV3) {
                    metaV3.style.width = curZoneW + 'px';
                    metaV3.style.maxWidth = curZoneW + 'px';
                }
                fs = fitHeadlineForWidth(curZoneW);
                actualHeadW = Math.ceil(Math.max(...lines.map(l => l.getBoundingClientRect().width)));
            }

            // Đặt zone.style.left để head_to_text_gap_px rơi đúng vào [34..58]px (G7, G18, G22)
            if (cfg.dyn_zone_left !== null && cfg.dyn_zone_left !== undefined) {
                zone.style.left = cfg.dyn_zone_left + 'px';
                zone.style.right = 'auto';
            } else if (cfg.side === 'right' && cfg.forbid_x1 > 0) {
                let idealLeft = Math.round(cfg.forbid_x1 - cfg.target_gap_px - curZoneW);
                if (idealLeft < 28) {
                    idealLeft = 28;
                    const maxAllowedW = Math.max(448, cfg.forbid_x1 - cfg.target_gap_px - idealLeft);
                    if (curZoneW > maxAllowedW) {
                        curZoneW = maxAllowedW;
                        zone.style.width = curZoneW + 'px';
                        if (subBox) { subBox.style.width = curZoneW + 'px'; subBox.style.maxWidth = curZoneW + 'px'; }
                        if (metaV3) { metaV3.style.width = curZoneW + 'px'; metaV3.style.maxWidth = curZoneW + 'px'; }
                        fs = fitHeadlineForWidth(curZoneW);
                    }
                } else if (idealLeft > 88) {
                    idealLeft = 88;
                }
                zone.style.left = idealLeft + 'px';
                zone.style.right = 'auto';
            } else if (cfg.side === 'left' && cfg.forbid_x2 > 0) {
                let idealLeft = Math.round(cfg.forbid_x2 + cfg.target_gap_px);
                if (idealLeft + curZoneW > 1080 - 28) {
                    const maxAllowedW = Math.max(448, 1080 - 28 - idealLeft);
                    if (curZoneW > maxAllowedW) {
                        curZoneW = maxAllowedW;
                        zone.style.width = curZoneW + 'px';
                        if (subBox) { subBox.style.width = curZoneW + 'px'; subBox.style.maxWidth = curZoneW + 'px'; }
                        if (metaV3) { metaV3.style.width = curZoneW + 'px'; metaV3.style.maxWidth = curZoneW + 'px'; }
                        fs = fitHeadlineForWidth(curZoneW);
                    }
                    idealLeft = Math.min(idealLeft, 1080 - 24 - curZoneW);
                }
                zone.style.left = idealLeft + 'px';
                zone.style.right = 'auto';
            }

            // Giải LAW_09 Optical Leading cho cỡ fs mới
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
                const maxLhW = 2.55 * xRatio;
                let targetLh = Math.max(minLhW, reqLh);
                if (targetLh > maxLhW) targetLh = maxLhW;
                targetLh = Math.max(0.99, Math.min(1.27, +targetLh.toFixed(3)));
                return { fs: curFs, targetLh };
            }

            const best = solveLaw09(fs);
            h.style.fontSize = best.fs + 'px';
            h.style.lineHeight = String(best.targetLh);
            lines.forEach(l => { l.style.lineHeight = String(best.targetLh); });

            // Auto-fit lại .sub-box theo curZoneW mới (LAW_11 & LAW_19)
            if (subBox) {
                Array.from(subBox.querySelectorAll('*')).forEach(el => {
                    const cs = window.getComputedStyle(el);
                    const curFs = parseFloat(cs.fontSize);
                    if ((el.innerText || '').trim().length > 0 && curFs > 0 && curFs < 19.0) {
                        el.style.fontSize = '19px';
                    }
                });
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
                    el.style.letterSpacing = '0em';
                    let sfs = 27.5;
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

            // Auto-fit .meta-note và .meta-v3-main nếu curZoneW hẹp
            const metaNote = document.querySelector('.meta-note');
            if (metaNote && metaV3) {
                let mnFs = 19.5;
                metaNote.style.fontSize = mnFs + 'px';
                while (mnFs > 17.5 && metaNote.scrollWidth > metaV3.clientWidth) {
                    mnFs = +(mnFs - 0.5).toFixed(1);
                    metaNote.style.fontSize = mnFs + 'px';
                }
            }

            // Căn tâm thị giác dọc chính xác theo biên thực của khối chữ (G14 Optical Vertical Balance = 0.00)
            if (zone) {
                zone.style.top = '185px';
                zone.style.transform = 'none';
                const hR = h.getBoundingClientRect();
                const sR = subBox ? subBox.getBoundingClientRect() : hR;
                const mEl = document.querySelector('.meta');
                const mR = mEl ? mEl.getBoundingClientRect() : sR;
                const bTop = Math.min(hR.top, sR.top);
                const bBot = Math.max(hR.bottom, sR.bottom, mR.bottom);
                const bH = bBot - bTop;
                const idealTop = Math.round((1350 - bH) * 0.50);
                const shiftY = idealTop - Math.round(bTop);
                zone.style.top = (185 + shiftY) + 'px';
            }

            const hFinal = h.getBoundingClientRect();
            const sFinal = subBox ? subBox.getBoundingClientRect() : hFinal;
            const mElFinal = document.querySelector('.meta');
            const mFinal = mElFinal ? mElFinal.getBoundingClientRect() : sFinal;
            const tightArea = (hFinal.width * hFinal.height) + (sFinal.width * sFinal.height) + (mFinal.width * mFinal.height);
            const textAreaPct = +(tightArea / (1080 * 1350) * 100.0).toFixed(2);

            return {
                final_h_fs: best.fs,
                final_zone_w: curZoneW,
                text_area_pct: textAreaPct,
                updated_html: document.documentElement.outerHTML
            };
        }""",
        {
            "dyn_zone_w": dyn_zone_w,
            "dyn_zone_left": dyn_zone_left,
            "explicit_zone_w": override_zone_w is not None,
            "forbid_x1": forbid_x1,
            "forbid_x2": forbid_x2,
            "side": side,
            "target_gap_px": target_gap_px,
            "compact_pad": compact_pad,
            "boost_subbox_sal": boost_subbox_sal,
        },
    )

    html_out_path.write_text("<!DOCTYPE html>\n" + fit_info["updated_html"], encoding="utf-8")
    page.screenshot(path=str(overlay_png_path), omit_background=True)
    return fit_info


def composite_overlay_on_bg(bg_path: Path, ov_png_path: Path, out_jpg_path: Path) -> None:
    with Image.open(bg_path) as bg_im, Image.open(ov_png_path) as ov_im:
        comp = Image.alpha_composite(bg_im.convert("RGBA"), ov_im.convert("RGBA")).convert("RGB")
        comp.save(out_jpg_path, "JPEG", quality=93)


def prepare_kb_v3_spec(
    kb_id: str,
    kb_num: int,
    master: Dict[str, Any],
    kb_70_map: Dict[str, Any],
) -> Tuple[Dict[str, Any], str, str, Dict[str, Any]]:
    """
    Chuẩn bị `spec`, `style_code`, `side`, `frame_meta` cho `KB_XX` từ `banner2_cards/KB_XX.json` và `kb_31_master_specs.json`.
    """
    base_spec = copy.deepcopy(ensure_default_spec_for_new_kb(kb_id, master, kb_70_map))
    if "sub_old" in base_spec:
        base_spec["sub_old"] = clean_sub_emoji(base_spec["sub_old"])
    if "sub_new" in base_spec:
        base_spec["sub_new"] = clean_sub_emoji(base_spec["sub_new"])

    card_path = CARDS_DIR / f"{kb_id}.json"
    card_data = json.loads(card_path.read_text(encoding="utf-8")) if card_path.exists() else {}

    hook_obj = copy.deepcopy(card_data.get("hook_1") or {})
    if "sub_old" in hook_obj:
        hook_obj["sub_old"] = clean_sub_emoji(hook_obj["sub_old"])
    if "sub_new" in hook_obj:
        hook_obj["sub_new"] = clean_sub_emoji(hook_obj["sub_new"])

    spec = populate_hook_spec(base_spec, hook_obj)
    # Khử sạch từ cấm sổ đen trong các trường sub-box và headline
    spec["headline_lines"] = [
        ln.replace("bảo chứng", "bằng chứng").replace("chuyên gia", "người làm nghề").replace("nỗi đau", "chỗ vướng")
        for ln in spec.get("headline_lines", [])
    ]
    if "hl_kw" in spec and isinstance(spec["hl_kw"], str):
        spec["hl_kw"] = spec["hl_kw"].replace("bảo chứng", "bằng chứng").replace("chuyên gia", "người làm nghề")
    if "k18" in spec and isinstance(spec["k18"], dict):
        spec["k18"]["p1"] = "Đúng chỗ vướng"
    if "k03" in spec and isinstance(spec["k03"], dict):
        for k3_f in ("l1", "l2"):
            if k3_f in spec["k03"] and isinstance(spec["k03"][k3_f], str):
                spec["k03"][k3_f] = spec["k03"][k3_f].replace("chuyên gia", "người làm")

    if card_data.get("h_code"):
        spec["h_code"] = card_data["h_code"]
    if card_data.get("person_side"):
        spec["side"] = card_data["person_side"]

    style_code = card_data.get("style_code") or spec.get("style", "K01")
    if style_code == "K15":
        # K15 có 7 ô lịch T2..CN nhỏ trên 360px dễ làm giảm sub_ocr_accuracy; dùng K01/K02 rõ nét 100%
        style_code = "K01"

    # Gắn meta_code: lẻ dùng M01, chẵn dùng M02 (sẽ tự động chuyển M01 nếu G8/G14 sát ngưỡng)
    spec["meta_code"] = "M01" if (kb_num % 2 == 1) else "M02"

    side = spec.get("side", "right")
    frame_meta = copy.deepcopy(kb_70_map.get(kb_id, {}))
    if not frame_meta:
        ref_num = ((kb_num - 1) % 70) + 1
        frame_meta = copy.deepcopy(kb_70_map.get(f"KB_{ref_num:02d}", {}))

    return spec, style_code, side, frame_meta


def process_kb_chunk(
    kb_nums: List[int],
    master: Dict[str, Any],
    kb_70_map: Dict[str, Any],
    plate_map: Dict[str, Path],
) -> List[Dict[str, Any]]:
    DUAL_BG_DIR.mkdir(parents=True, exist_ok=True)
    OUT_RENDER_DIR.mkdir(parents=True, exist_ok=True)

    chunk_items = []
    # 1. Render lượt đầu cho tất cả các KB trong chunk trên 1 phiên Chromium
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)

        for kb_num in kb_nums:
            kb_id = f"KB_{kb_num:02d}"
            kb_lower = kb_id.lower()
            spec, style_code, side, frame_meta = prepare_kb_v3_spec(kb_id, kb_num, master, kb_70_map)

            color_bg_path = DUAL_BG_DIR / f"{kb_lower}_color_bg.jpg"
            bw_bg_path = DUAL_BG_DIR / f"{kb_lower}_bw_bg.jpg"
            if not color_bg_path.exists():
                plate_key = frame_meta.get("plate_key") or KB_TO_PLATE_ASSIGNMENT.get(kb_id, "kb14_01")
                src_plate = Path(frame_meta["plate_path"]) if frame_meta.get("plate_path") else plate_map.get(plate_key)
                if src_plate is None or not src_plate.exists():
                    fallback_candidates = [p for k, p in plate_map.items() if p.exists()]
                    src_plate = fallback_candidates[kb_num % len(fallback_candidates)]
                build_dual_zero_blur_bgs(
                    src_plate_path=src_plate,
                    side=side,
                    out_color_path=color_bg_path,
                    out_bw_path=bw_bg_path,
                    variant_seed=kb_num,
                    frame_meta=frame_meta,
                )

            html_v3_path = OUT_RENDER_DIR / f"{kb_lower}_v3_price.html"
            ov_png_path = OUT_RENDER_DIR / f"{kb_lower}_v3_ov.png"
            v3_jpg_path = OUT_RENDER_DIR / f"{kb_lower}_v3_price.jpg"

            html_str = build_style_html(style_code, spec, master)
            fit_info = render_v3_overlay_with_cfg(
                page,
                html_str,
                html_v3_path,
                ov_png_path,
                frame_meta=frame_meta,
                side=side,
            )

            # Nếu M02 làm diện tích chữ > 23.3% (sát trần 24.0% của G8), tự động chuyển sang M01 ngay trên page!
            if spec["meta_code"] == "M02" and fit_info.get("text_area_pct", 18.0) > 23.3:
                spec["meta_code"] = "M01"
                html_str = build_style_html(style_code, spec, master)
                fit_info = render_v3_overlay_with_cfg(
                    page,
                    html_str,
                    html_v3_path,
                    ov_png_path,
                    frame_meta=frame_meta,
                    side=side,
                )

            composite_overlay_on_bg(color_bg_path, ov_png_path, v3_jpg_path)
            if ov_png_path.exists():
                ov_png_path.unlink()

            chunk_items.append({
                "kb_id": kb_id,
                "kb_num": kb_num,
                "kb_lower": kb_lower,
                "spec": spec,
                "style_code": style_code,
                "side": side,
                "frame_meta": frame_meta,
                "color_bg_path": color_bg_path,
                "html_v3_path": html_v3_path,
                "ov_png_path": ov_png_path,
                "v3_jpg_path": v3_jpg_path,
            })

        page.close()
        browser.close()

    # 2. Chạy audit_v3_banner 25/25 cổng + Cơ chế Auto-Heal tức thì nếu có cổng trượt
    results = []
    for item in chunk_items:
        kb_id = item["kb_id"]
        spec = item["spec"]
        style_code = item["style_code"]
        side = item["side"]
        frame_meta = item["frame_meta"]
        color_bg_path = item["color_bg_path"]
        html_v3_path = item["html_v3_path"]
        ov_png_path = item["ov_png_path"]
        v3_jpg_path = item["v3_jpg_path"]

        audit_res = audit_v3_banner(
            html_path=html_v3_path,
            final_img_path=v3_jpg_path,
            expected_lines=3,
            person_side=side,
        )

        # Cơ chế Auto-Heal tối đa 5 vòng nếu chưa đạt 25/25 PASS
        heal_attempt = 0
        while not audit_res["all_13_pass"] and heal_attempt < 5:
            heal_attempt += 1
            gates = audit_res.get("gates", {})
            failed_keys = [k for k, v in gates.items() if not v.get("pass")]
            print(f"[AUTO-HEAL #{heal_attempt}] {kb_id} ({audit_res['score']}): failed={failed_keys}", flush=True)

            g13_fb = gates.get("G13_LAW01_full_body_proportion", {}).get("face_bbox", [0, 0, 0, 0])
            fx_live, fy_live, fw_live, fh_live = [float(v) for v in g13_fb]
            live_forbid_x1 = max(0, int(fx_live - 0.18 * fw_live)) if fw_live > 0 else None
            live_forbid_x2 = min(1080, int(fx_live + fw_live + 0.18 * fw_live)) if fw_live > 0 else None

            g22 = gates.get("G22_LAW18_adaptive_space_filling_scale", {})
            g8 = gates.get("G8_facebook_20pct_area_budget", {})
            cur_area_pct = g8.get("text_area_pct", 18.0)

            override_zone_w = None
            override_zone_left = None
            target_gap_px = 40
            compact_pad = False
            boost_subbox_sal = False

            # 1) Nếu G2 hoặc G15 trượt do đặc thù font -> chuyển h_code sang H01 chuẩn
            if any(k.startswith(("G2_", "G15_")) for k in failed_keys):
                spec["h_code"] = "H01"

            # 1b) Nếu G11 (line overflow) trượt -> mở rộng nhẹ zone_w thêm 18px
            if any(k.startswith("G11_") for k in failed_keys):
                override_zone_w = int(g22.get("headline_width_px", 500)) + 12

            # 1c) Nếu M02 làm G8 hoặc G14 trượt -> chuyển về M01
            if spec.get("meta_code") == "M02" and any(
                k.startswith(("G8_", "G14_")) for k in failed_keys
            ):
                spec["meta_code"] = "M01"

            # 2) Nếu G21 (Saliency Scanpath) trượt -> tăng độ nổi bật của sub-box (K03 hoặc viền vàng accent)
            if any(k.startswith("G21_") for k in failed_keys):
                boost_subbox_sal = True
                if style_code not in ("K03", "K01"):
                    style_code = "K03" if heal_attempt == 1 else "K01"

            # 3) Nếu G8 trượt do diện tích chữ > 24.0% -> bật compact_pad & M01
            if any(k.startswith("G8_") for k in failed_keys) and cur_area_pct > 24.0:
                spec["meta_code"] = "M01"
                compact_pad = True
                override_zone_w = max(464, int(g22.get("zone_width_px", 500)) - 20)

            # 4) Nếu G6 (OCR), G12, G16, G23, G4, G5 trượt -> chuyển style_code sang K01 (hoặc K02)
            if any(k.startswith(("G6_", "G12_", "G16_", "G23_", "G4_", "G5_")) for k in failed_keys):
                if style_code != "K01":
                    style_code = "K01"
                else:
                    style_code = "K02"

            # 5) Nếu G7, G18, G22 trượt -> tinh chỉnh dyn_zone_w & dyn_zone_left dựa trên live_forbid_x1/x2
            if any(k.startswith(("G7_", "G18_", "G22_")) for k in failed_keys):
                cur_zw = int(g22.get("zone_width_px", 500))
                cur_hw = int(g22.get("headline_width_px", 460))
                cur_gap = int(g22.get("head_to_text_gap_px", 40))
                cur_fill = float(g22.get("zone_fill_ratio", 0.92))
                cur_hfs = float(g22.get("headline_fs_px", 72.0))
                min_adap = float(g22.get("min_adaptive_hfs_px", 70.0))

                if cur_gap < 28:
                    target_gap_px = 38 + heal_attempt * 4
                elif cur_gap > 68:
                    target_gap_px = 42

                if cur_hfs < min_adap:
                    if live_forbid_x1 and side == "right":
                        avail_max = live_forbid_x1 - 34 - 28
                        override_zone_w = max(468, min(585, avail_max if heal_attempt == 1 else int(cur_hw / 0.945)))
                        override_zone_left = max(24, live_forbid_x1 - 38 - override_zone_w)
                    elif live_forbid_x2 and side == "left":
                        avail_max = 1080 - 28 - (live_forbid_x2 + 34)
                        override_zone_w = max(468, min(585, avail_max if heal_attempt == 1 else int(cur_hw / 0.945)))
                        override_zone_left = live_forbid_x2 + 38
                elif cur_fill < 0.92:
                    override_zone_w = max(448, int(cur_hw / 0.955))
                    if live_forbid_x1 and side == "right":
                        override_zone_left = max(28, min(92, live_forbid_x1 - 42 - override_zone_w))
                    elif live_forbid_x2 and side == "left":
                        override_zone_left = live_forbid_x2 + 42

                if cur_area_pct < 11.0:
                    override_zone_w = max(override_zone_w or cur_zw, 535)

            html_str = build_style_html(style_code, spec, master)
            with sync_playwright() as pw:
                browser = pw.chromium.launch(headless=True)
                page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
                render_v3_overlay_with_cfg(
                    page,
                    html_str,
                    html_v3_path,
                    ov_png_path,
                    frame_meta=frame_meta,
                    side=side,
                    override_zone_w=override_zone_w,
                    override_zone_left=override_zone_left,
                    override_forbid_x1=live_forbid_x1,
                    override_forbid_x2=live_forbid_x2,
                    target_gap_px=target_gap_px,
                    compact_pad=compact_pad,
                    boost_subbox_sal=boost_subbox_sal,
                )
                page.close()
                browser.close()

            composite_overlay_on_bg(color_bg_path, ov_png_path, v3_jpg_path)
            if ov_png_path.exists():
                ov_png_path.unlink()

            audit_res = audit_v3_banner(
                html_path=html_v3_path,
                final_img_path=v3_jpg_path,
                expected_lines=3,
                person_side=side,
            )

        failed_final = [k for k, v in audit_res.get("gates", {}).items() if not v.get("pass")]
        res_entry = {
            "kb_id": kb_id,
            "order": item["kb_num"],
            "style_code": style_code,
            "meta_code": spec["meta_code"],
            "v3_score": audit_res["score"],
            "v3_pass": bool(audit_res["all_13_pass"]),
            "v3_img_path": str(v3_jpg_path),
            "v3_html_path": str(html_v3_path),
            "failed_gates": failed_final,
        }
        results.append(res_entry)
        print(
            f"[V3 PART2 DONE] {kb_id} ({style_code} · {spec['meta_code']}) -> {audit_res['score']} PASS={audit_res['all_13_pass']}",
            flush=True,
        )

    return results


def main():
    parser = argparse.ArgumentParser(description="Render V3 Price Banners Part 2 (KB_71..KB_140) with 25/25 Gate Audit")
    parser.add_argument("--start", type=int, default=71, help="KB bắt đầu (mặc định: 71)")
    parser.add_argument("--end", type=int, default=140, help="KB kết thúc (mặc định: 140)")
    parser.add_argument("--workers", type=int, default=4, help="Số tiến trình chạy song song")
    parser.add_argument("--out-json", type=str, default="/tmp/v3_render_part2.json", help="Đường dẫn file JSON báo cáo kết quả")
    args = parser.parse_args()

    t0 = time.time()
    out_json_path = Path(args.out_json)

    plate_map = harvest_generated_plates()
    master = json.loads(SPECS_PATH.read_text(encoding="utf-8"))
    kb_70_map_path = PILOT_DIR / "kb_70_plate_map.json"
    kb_70_map = json.loads(kb_70_map_path.read_text(encoding="utf-8")) if kb_70_map_path.exists() else {}

    all_nums = list(range(args.start, args.end + 1))
    n_workers = max(1, min(args.workers, len(all_nums)))
    chunks: List[List[int]] = [[] for _ in range(n_workers)]
    for idx, num in enumerate(all_nums):
        chunks[idx % n_workers].append(num)

    all_results: List[Dict[str, Any]] = []
    if n_workers == 1:
        all_results = process_kb_chunk(all_nums, master, kb_70_map, plate_map)
    else:
        with concurrent.futures.ProcessPoolExecutor(max_workers=n_workers) as ex:
            futs = [ex.submit(process_kb_chunk, ch, master, kb_70_map, plate_map) for ch in chunks if ch]
            for f in concurrent.futures.as_completed(futs):
                all_results.extend(f.result())

    all_results.sort(key=lambda x: x["order"])
    passed_count = sum(1 for r in all_results if r["v3_pass"])
    report = {
        "range": f"KB_{args.start:02d}..KB_{args.end:02d}",
        "total": len(all_results),
        "passed_25_25": passed_count,
        "all_pass": passed_count == len(all_results),
        "elapsed_sec": round(time.time() - t0, 1),
        "items": all_results,
    }
    out_json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"=== COMPLETED V3 PRICE BANNERS PART 2 ({passed_count}/{len(all_results)} 25/25 PASS in {report['elapsed_sec']}s) -> {out_json_path} ===",
        flush=True,
    )


if __name__ == "__main__":
    main()
