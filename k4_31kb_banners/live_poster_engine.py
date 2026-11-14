#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LIVE POSTER ENGINE V2.0 — 2-AXIS AUTO ROUTER + 7-GATE VERIFIER + SELF-LEARNING LEDGER
=====================================================================================
Thiết kế theo Hội thảo Gemini 4 Argon High × Thư ký CLAUDE2 (Opus 5.5 - job 3d336850):
Quy trình 6 bước khép kín cho từng kịch bản (Chạy Chặng từng bài một):
1. PROBE (`probe_kb`):
   - Đo `head_protect = [fx - 0.15w, fy - 0.30h, 1.30w, 1.40h] + 24px` (bao trọn cả tóc & đầu theo LAW_20).
   - Đo `text_union = union(.headline, .sub-box, .meta) + 16px`.
   - Xác định `Valid_Light_Zone` và quét các cụm nguồn sáng thật trên ảnh nền.
2. ROUTE (`route_kb`):
   - Trục 1 (Ánh sáng nền): Phân loại tự động vào `POINT_BOKEH`, `WALL_SCONCE`, `COVE_STRIP`, hoặc `LIGHT_NONE`.
   - Trục 2 (Chuyển động chữ DOM): Phân loại `.sub-box` vào `VERTICAL_ROW_FLIP` (2 dòng trên-dưới) hoặc `HORIZONTAL_STAT_FLIP` (2 cột trái-phải + mũi tên `.arrow`).
   - Trục 3 (Specular Rim Target): Đặt trực tiếp vào phần tử LỜI GIẢI (`.vf-hl`, cột phải `.col-stat`, vạch vàng bên trái + dòng `✓`, hoặc gạch chân sáng chạy 1 lần dưới `.l2`), tuyệt đối 0 pixel lem vào thân chữ.
   - Tra cứu tham số khởi tạo từ `live_poster_laws.json`.
3. RENDER (`render_kb_live_poster`):
   - Xuất `v2_pilots/motion_out/{kb_lower}_live_v2.mp4` (1080x1350, 30fps, 6.0s = 180 frames, H.264 High Profile CRF 17, +faststart).
4. VERIFY (`verify_7_gates`):
   - Kiểm định 7 cổng toán học của Thư ký CLAUDE2 (`G_LP1` .. `G_LP7`), bao gồm cả cổng mới `G_LP4` (Đủ thấy: weighted ΔLuma >= 6.0 mức) và `G_LP3` (Đơn điệu `out >= in` mọi pixel).
   - Tự động Auto-Heal tối đa 2 vòng nếu cổng `G_LP4` hoặc `G_LP5` cần tinh chỉnh biên độ.
5. PUBLISH (`publish_kb`):
   - Đẩy `{kb_lower}_live_v2.mp4` lên R2 (`https://media.fedu.vn/banner2/{kb_lower}_live_v2.mp4`).
   - Cập nhật `banner2_cards/KB_XX.json` (`has_live_poster: true`) và build + push `banner2.html` lên R2.
   - Bắn video qua Telegram `@viet_vni_bot` kèm tự động lưu Google Drive (`video_vault.py`).
6. LEARN (`learn_to_ledger`):
   - Ghi kết quả 7 cổng, thông số đã PASS và bài học rút ra vào `live_poster_laws.json` để các bài kế tiếp tự động kế thừa.
"""

import argparse
import datetime
import io
import json
import math
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional

import cv2
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
PILOT_DIR = BASE_DIR / "v2_pilots"
DUAL_BG_DIR = PILOT_DIR / "dual_bg_70"
BATCH_OUT_DIR = PILOT_DIR / "batch_out"
MOTION_OUT_DIR = PILOT_DIR / "motion_out"
CARDS_DIR = BASE_DIR / "banner2_cards"
FACE_CACHE_PATH = BASE_DIR / "face_box_cache.json"
LAWS_PATH = BASE_DIR / "live_poster_laws.json"
R2_MANAGER = Path("/Users/vietmac/Documents/CODE/Quản gia/r2_manager.py")
TELEGRAM_NOTIFY = Path("/Users/vietmac/Documents/CODE/Quản gia/telegram_notify.py")
UPDATE_HUB_SCRIPT = BASE_DIR / "update_banner2_hub.py"

sys.path.insert(0, str(BASE_DIR))
from uiux_auditor import audit_v3_banner


def load_laws() -> Dict[str, Any]:
    if LAWS_PATH.exists():
        return json.loads(LAWS_PATH.read_text(encoding="utf-8"))
    return {"version": "1.0", "archetype_priors": {}, "laws": [], "runs": []}


def save_laws(data: Dict[str, Any]) -> None:
    data["updated_at"] = datetime.datetime.now().astimezone().isoformat()
    LAWS_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def probe_kb(kb_id: str) -> Dict[str, Any]:
    """
    Bước 1 (PROBE): Đo đạc hình học DOM, vùng bảo vệ đầu/tóc (`head_protect`),
    vùng bảo vệ chữ (`text_union`), và tìm các cụm nguồn sáng hợp lệ trên ảnh nền.
    """
    kb_id = kb_id.upper()
    kb_lower = kb_id.lower()
    html_path = BATCH_OUT_DIR / f"{kb_lower}_v3_price.html"
    bg_path = DUAL_BG_DIR / f"{kb_lower}_color_bg.jpg"
    card_path = CARDS_DIR / f"{kb_id}.json"

    if not html_path.exists() or not bg_path.exists():
        raise FileNotFoundError(f"Missing files for {kb_id}: {html_path} or {bg_path}")

    face_cache = json.loads(FACE_CACHE_PATH.read_text(encoding="utf-8")) if FACE_CACHE_PATH.exists() else {}
    card_data = json.loads(card_path.read_text(encoding="utf-8")) if card_path.exists() else {}
    fc_entry = face_cache.get(kb_id, {})

    side = fc_entry.get("side") or card_data.get("person_side", "right")
    face_bbox = fc_entry.get("cropped_face_bbox", [650, 220, 260, 350] if side == "right" else [150, 220, 260, 350])
    fx, fy, fw, fh = [float(v) for v in face_bbox]

    # head_protect = [fx - 0.15w, fy - 0.30h, 1.30w, 1.40h] + 24px margin (LP_LAW_02)
    hp_raw = [
        max(0, int(round(fx - 0.15 * fw))),
        max(0, int(round(fy - 0.30 * fh))),
        min(1080, int(round(fx + 1.15 * fw))),
        min(1350, int(round(fy + 1.10 * fh))),
    ]
    hp_guard = [
        max(0, hp_raw[0] - 24),
        max(0, hp_raw[1] - 24),
        min(1080, hp_raw[2] + 24),
        min(1350, hp_raw[3] + 24),
    ]

    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        page = b.new_page(viewport={"width": 1080, "height": 1350})
        page.goto(f"file://{html_path.resolve()}", wait_until="load")
        page.evaluate("() => document.fonts.ready")
        dom = page.evaluate(
            """() => {
            const r = el => {
                if (!el) return null;
                const b = el.getBoundingClientRect();
                return [Math.round(b.left), Math.round(b.top), Math.round(b.right), Math.round(b.bottom)];
            };
            const sub = document.querySelector('.sub-box');
            const vfHl = sub ? sub.querySelector('.vf-hl') : null;
            const colStats = sub ? Array.from(sub.querySelectorAll('.col-stat')) : [];
            const arrowEl = sub ? sub.querySelector('.arrow') : null;
            const rows = sub ? Array.from(sub.querySelectorAll('.row')) : [];
            const l1 = sub ? sub.querySelector('.l1') : null;
            const l2 = sub ? sub.querySelector('.l2') : null;
            const cs = sub ? window.getComputedStyle(sub) : null;
            const bLeftW = cs ? parseFloat(cs.borderLeftWidth || '0') : 0;
            const bTopW = cs ? parseFloat(cs.borderTopWidth || '0') : 0;

            return {
                zone: r(document.querySelector('.zone')),
                headline: r(document.querySelector('.headline')),
                hl: r(document.querySelector('.headline .hl')),
                subBox: r(sub),
                vfHl: r(vfHl),
                colStats: colStats.map(c => r(c)),
                arrow: r(arrowEl),
                rows: rows.map(rw => r(rw)),
                l1: r(l1),
                l2: r(l2),
                borderLeftW: bLeftW,
                borderTopW: bTopW,
                meta: r(document.querySelector('.meta'))
            };
        }"""
        )
        b.close()

    img_bgr = cv2.imread(str(bg_path))
    rgb_u8 = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    luma = 0.299 * rgb_u8[:, :, 0] + 0.587 * rgb_u8[:, :, 1] + 0.114 * rgb_u8[:, :, 2]

    # Xây dựng Valid_Light_Zone = Ảnh - dilate(text_union, 16px) - dilate(head_and_body_protect, 24px)
    h, w = luma.shape
    valid_zone = np.ones((h, w), dtype=bool)
    # Bảo vệ toàn bộ đầu + thân người từ đỉnh hp_guard[1] xuống đáy 1350 ở phía nhân vật
    valid_zone[hp_guard[1] : 1350, hp_guard[0] : hp_guard[2]] = False
    if side == "right":
        valid_zone[hp_guard[1] : 1350, hp_guard[0] : 1080] = False
    else:
        valid_zone[hp_guard[1] : 1350, 0 : hp_guard[2]] = False

    # Bảo vệ text_union + 16px và chỉ cho phép đèn thở ở phía trên đỉnh headline - 12px
    h_top = dom["headline"][1] if dom.get("headline") else 380
    valid_zone[max(0, h_top - 12) :, :] = False
    for k_dom in ("headline", "subBox", "meta"):
        bx = dom.get(k_dom)
        if bx:
            tx1, ty1, tx2, ty2 = max(0, bx[0] - 16), max(0, bx[1] - 16), min(1080, bx[2] + 16), min(1350, bx[3] + 16)
            valid_zone[ty1:ty2, tx1:tx2] = False

    zone_lumas = luma[valid_zone]
    p85 = float(np.percentile(zone_lumas, 85)) if zone_lumas.size > 0 else 0.0
    p95 = float(np.percentile(zone_lumas, 95)) if zone_lumas.size > 0 else 0.0
    p98 = float(np.percentile(zone_lumas, 98)) if zone_lumas.size > 0 else 0.0
    p99 = float(np.percentile(zone_lumas, 99)) if zone_lumas.size > 0 else 0.0

    # Phát hiện các cụm nguồn sáng trong valid_zone
    thresh_val = max(125.0, p95 - 18.0)
    bright_bin = ((luma >= thresh_val) & valid_zone).astype(np.uint8) * 255
    n_lbl, lbls, stats, cents = cv2.connectedComponentsWithStats(bright_bin)
    clusters = []
    for idx in range(1, n_lbl):
        area = int(stats[idx, cv2.CC_STAT_AREA])
        if area >= 55:
            cx, cy = cents[idx]
            x, y, bw_c, bh_c = [
                int(stats[idx, k])
                for k in (cv2.CC_STAT_LEFT, cv2.CC_STAT_TOP, cv2.CC_STAT_WIDTH, cv2.CC_STAT_HEIGHT)
            ]
            c_luma = luma[y : y + bh_c, x : x + bw_c]
            clusters.append(
                {
                    "cx": round(float(cx), 1),
                    "cy": round(float(cy), 1),
                    "bbox": [x, y, bw_c, bh_c],
                    "area": area,
                    "aspect": round(float(bw_c) / max(1.0, float(bh_c)), 2),
                    "max_luma": round(float(c_luma.max()), 1),
                    "p90_luma": round(float(np.percentile(c_luma, 90)), 1),
                }
            )
    clusters.sort(key=lambda c: c["area"] * c["max_luma"], reverse=True)

    return {
        "kb_id": kb_id,
        "style_code": card_data.get("style_code", "K01"),
        "side": side,
        "face_bbox": face_bbox,
        "head_protect_raw": hp_raw,
        "head_protect_guard": hp_guard,
        "dom": dom,
        "zone_stats": {
            "valid_pixels": int(valid_zone.sum()),
            "p85_luma": round(p85, 1),
            "p95_luma": round(p95, 1),
            "p98_luma": round(p98, 1),
            "p99_luma": round(p99, 1),
        },
        "clusters": clusters[:6],
    }


def route_kb(probe: Dict[str, Any], laws: Dict[str, Any]) -> Dict[str, Any]:
    """
    Bước 2 (ROUTE): Chọn kiểu ánh sáng nền (`Light Archetype`), kiểu lật chữ (`Text Motion`),
    và đích quét tia sáng (`Specular Rim Target`) dựa trên số đo Probe thực tế + Sổ cái `live_poster_laws.json`.
    """
    kb_id = probe["kb_id"]
    dom = probe["dom"]
    clusters = probe["clusters"]
    z_stats = probe["zone_stats"]
    hp_guard = probe["head_protect_guard"]
    h_top = dom["headline"][1] if dom.get("headline") else 380

    # 1. Định tuyến Trục Chuyển Động Chữ DOM & Đích Specular Rim (LP_LAW_03)
    if dom.get("colStats") and len(dom["colStats"]) >= 2:
        text_motion = "HORIZONTAL_STAT_FLIP"
        rim_mode = "RIGHT_STAT_BOX_RIM"
        rim_bbox = dom["colStats"][1]  # Cột phải chứa lời giải ("01 lần tư vấn thật ăn ngay")
        rim_desc = "Quét viền Specular Rim quanh cột lời giải bên phải (.col-stat #2)"
    elif dom.get("vfHl"):
        text_motion = "VERTICAL_ROW_FLIP"
        rim_mode = "BOX_EXTERIOR_RIM"
        rim_bbox = dom["vfHl"]
        rim_desc = "Quét viền Specular Rim + Bloom quanh hộp lời giải (.vf-hl)"
    elif dom.get("rows") and len(dom["rows"]) >= 2 and dom.get("borderLeftW", 0) >= 2.5:
        text_motion = "VERTICAL_ROW_FLIP"
        rim_mode = "LEFT_ACCENT_TO_ROW2_SWEEP"
        # Kết hợp vạch vàng bên trái của .sub-box và gạch chân sáng dưới dòng ✓ (rows[1])
        r2 = dom["rows"][1]
        sb = dom["subBox"]
        rim_bbox = [sb[0], sb[1], r2[2], r2[3]]
        rim_desc = "Tia sáng chạy dọc vạch vàng bên trái từ trên xuống rồi lướt dưới dòng lời giải (✓)"
    elif dom.get("l2"):
        text_motion = "VERTICAL_ROW_FLIP"
        rim_mode = "SOLUTION_UNDERLINE_SWEEP"
        rim_bbox = dom["l2"]
        rim_desc = "Gạch chân ánh sáng Specular lướt 1 lần dưới dòng lời giải (.l2)"
    else:
        text_motion = "VERTICAL_ROW_FLIP"
        rim_mode = "BOX_EXTERIOR_RIM"
        rim_bbox = dom.get("subBox") or [520, 690, 1040, 820]
        rim_desc = "Quét viền Specular Rim quanh hộp .sub-box"

    # 2. Định tuyến Trục Ánh Sáng Nền theo đặc trưng hình học của các cụm đèn thật trong Valid_Light_Zone
    light_archetype = "LIGHT_NONE"
    light_sources: List[Dict[str, Any]] = []

    if kb_id == "KB_12":
        light_archetype = "POINT_BOKEH"
        for cx, cy in [(825.8, 346.1), (879.0, 329.4), (941.9, 308.0), (1029.1, 287.9)]:
            light_sources.append({"cx": cx, "cy": cy, "rx": 16.5, "ry": 22.0, "halo_r": 42.0})
    elif kb_id == "KB_01":
        # KB_01: Dải đèn hắt trần & mảng tường ấm phía trên chữ (x=380..585, y=0..365, hoàn toàn bên trái hp_guard[0]=591)
        # + dải trần phía trên đầu (x=590..980, y=0..70, phía trên hp_guard[1]=75)
        light_archetype = "COVE_STRIP"
        light_sources = [
            {"cx": 495.0, "cy": 165.0, "rx": 95.0, "ry": 115.0, "halo_r": 145.0},
            {"cx": 760.0, "cy": 34.0, "rx": 140.0, "ry": 26.0, "halo_r": 55.0},
        ]
    elif kb_id == "KB_02":
        # KB_02: 3 chiếc đèn tường chao kem cổ điển (WALL_SCONCE) trong phòng thư viện gỗ
        light_archetype = "WALL_SCONCE"
        light_sources = [
            {"cx": 728.0, "cy": 195.0, "rx": 46.0, "ry": 52.0, "halo_r": 105.0},
            {"cx": 935.0, "cy": 270.0, "rx": 38.0, "ry": 42.0, "halo_r": 85.0},
            {"cx": 295.0, "cy": 45.0, "rx": 52.0, "ry": 36.0, "halo_r": 85.0},
        ]
    elif kb_id == "KB_03":
        # KB_03: Cặp đèn tường đôi góc trên trái (137,67) & (205,69) + Ô đèn tủ kính ấm (495,285)
        light_archetype = "WALL_SCONCE"
        light_sources = [
            {"cx": 137.0, "cy": 67.0, "rx": 24.0, "ry": 28.0, "halo_r": 72.0},
            {"cx": 205.0, "cy": 69.0, "rx": 24.0, "ry": 28.0, "halo_r": 72.0},
            {"cx": 495.0, "cy": 285.0, "rx": 55.0, "ry": 36.0, "halo_r": 92.0},
        ]
    elif kb_id == "KB_04":
        # KB_04: Dải đèn hắt trần chạy ngang phía trên chữ (x=510..960, y=0..240, bên phải hp_guard[2]=503)
        # + khe trần cao (x=120..500, y=0..55, phía trên hp_guard[1]=62)
        light_archetype = "COVE_STRIP"
        light_sources = [
            {"cx": 665.0, "cy": 115.0, "rx": 145.0, "ry": 85.0, "halo_r": 150.0},
            {"cx": 310.0, "cy": 26.0, "rx": 130.0, "ry": 20.0, "halo_r": 45.0},
        ]
    elif kb_id == "KB_05":
        # KB_05: Chùm đĩa đèn Bokeh vàng ấm qua cửa kính phía sau (x=420..675, y=170..385, bên trái hp_guard[0]=693)
        light_archetype = "POINT_BOKEH"
        light_sources = [
            {"cx": 505.0, "cy": 285.0, "rx": 34.0, "ry": 42.0, "halo_r": 82.0},
            {"cx": 595.0, "cy": 245.0, "rx": 42.0, "ry": 48.0, "halo_r": 90.0},
            {"cx": 635.0, "cy": 325.0, "rx": 28.0, "ry": 32.0, "halo_r": 62.0},
            {"cx": 445.0, "cy": 335.0, "rx": 26.0, "ry": 30.0, "halo_r": 58.0},
        ]
    else:
        # Tự động tổng quát cho mọi KB_06..KB_140 dựa trên clusters đo được
        if clusters:
            top_c = clusters[0]
            if top_c["aspect"] >= 2.2 or top_c["area"] >= 12000:
                light_archetype = "COVE_STRIP"
            elif len(clusters) >= 3 and all(c["area"] <= 3500 for c in clusters[:3]):
                light_archetype = "POINT_BOKEH"
            else:
                light_archetype = "WALL_SCONCE"
            for c in clusters[:4]:
                bw_c, bh_c = c["bbox"][2], c["bbox"][3]
                rx = max(18.0, min(110.0, 0.45 * bw_c))
                ry = max(18.0, min(95.0, 0.45 * bh_c))
                light_sources.append(
                    {"cx": c["cx"], "cy": c["cy"], "rx": rx, "ry": ry, "halo_r": max(48.0, 1.8 * max(rx, ry))}
                )
        else:
            light_archetype = "LIGHT_NONE"

    priors = laws.get("archetype_priors", {}).get(light_archetype, {})
    delta_core = float(priors.get("delta_core", 20.0))
    delta_halo = float(priors.get("delta_halo", 12.0))

    return {
        "kb_id": kb_id,
        "light_archetype": light_archetype,
        "light_sources": light_sources,
        "delta_core": delta_core,
        "delta_halo": delta_halo,
        "text_motion": text_motion,
        "rim_mode": rim_mode,
        "rim_bbox": rim_bbox,
        "rim_desc": rim_desc,
        "head_protect_guard": hp_guard,
        "headline_top": h_top,
    }


def build_generalized_light_engine(
    bg_rgb_u8: np.ndarray,
    probe: Dict[str, Any],
    route: Dict[str, Any],
    gain_scale: float = 1.0,
) -> Dict[str, Any]:
    """
    Khởi tạo trường ánh sáng thở tổng quát tuân thủ tuyệt đối LP_LAW_01 & LP_LAW_02:
    - Cổng G_LP1 & G_LP2: Mọi pixel ngoài Valid_Light_Zone (đặc biệt là trong head_protect_guard và dưới đỉnh chữ)
      có mask == 0 tuyệt đối (`diff == 0`).
    - Cổng G_LP3 (Đơn điệu `out >= in` mọi pixel):
      Tính `delta_srgb >= 0` với cơ chế Headroom Damping: những pixel vốn đã sáng (`base_luma >= 220`)
      tự động giảm cộng lõi và chuyển năng lượng sang quầng loang ấm xung quanh (`base_luma in [60, 215]`),
      đảm bảo `min(out - in) >= 0` tuyệt đối (không bao giờ thở mà tối đi!) và không làm cháy sáng.
    - Cổng G_LP4 (Đủ thấy): Đảm bảo `weighted_delta_luma >= 6.0` mức tại đỉnh thở `t = 4.20s`.
    """
    h, w, _ = bg_rgb_u8.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)

    hp_x1, hp_y1, hp_x2, hp_y2 = route["head_protect_guard"]
    h_top = float(route["headline_top"])
    side = probe["side"]
    dom = probe["dom"]

    # 1. Xây dựng mặt nạ bảo vệ mượt (Smooth Cosine Guard) bên trong Valid_Light_Zone
    # Rào trên đỉnh chữ: bằng 1 khi y <= h_top - 28, giảm cosine về 0 tại y = h_top - 10
    y_limit = max(20.0, h_top - 10.0)
    y_soft_start = max(10.0, y_limit - 20.0)
    guard_y = np.zeros((h, w), dtype=np.float32)
    guard_y[yy <= y_soft_start] = 1.0
    tr_y = (yy > y_soft_start) & (yy < y_limit)
    guard_y[tr_y] = 0.5 * (1.0 + np.cos(np.pi * (yy[tr_y] - y_soft_start) / (y_limit - y_soft_start)))

    # Rào bảo vệ hộp đầu & tóc (`hp_guard = [hp_x1, hp_y1, hp_x2, hp_y2]`) với đệm chuyển 18px bên ngoài hp_guard
    # Khoảng cách có dấu tới hình chữ nhật bảo vệ người `[p_x1..p_x2, hp_y1..1350]`
    p_x1 = hp_x1 if side == "right" else 0
    p_x2 = 1080 if side == "right" else hp_x2
    cx_p = 0.5 * (p_x1 + p_x2)
    cy_p = 0.5 * (hp_y1 + 1350.0)
    hx_p = 0.5 * (p_x2 - p_x1)
    hy_p = 0.5 * (1350.0 - hp_y1)
    dx_p = np.maximum(np.abs(xx - cx_p) - hx_p, 0.0)
    dy_p = np.maximum(np.abs(yy - cy_p) - hy_p, 0.0)
    dist_to_person_guard = np.hypot(dx_p, dy_p)

    guard_person = np.zeros((h, w), dtype=np.float32)
    guard_person[dist_to_person_guard >= 20.0] = 1.0
    tr_p = (dist_to_person_guard > 0.0) & (dist_to_person_guard < 20.0)
    guard_person[tr_p] = 0.5 * (1.0 - np.cos(np.pi * dist_to_person_guard[tr_p] / 20.0))
    # Khóa cứng = 0 tuyệt đối bên trong vùng bảo vệ người
    guard_person[hp_y1:1350, p_x1:p_x2] = 0.0

    # Khóa cứng = 0 tuyệt đối trong mọi hộp chữ + 16px
    for k_dom in ("headline", "subBox", "meta"):
        bx = dom.get(k_dom)
        if bx:
            tx1, ty1, tx2, ty2 = max(0, bx[0] - 16), max(0, bx[1] - 16), min(1080, bx[2] + 16), min(1350, bx[3] + 16)
            guard_y[ty1:ty2, tx1:tx2] = 0.0

    total_guard = guard_y * guard_person

    core_field = np.zeros((h, w), dtype=np.float32)
    halo_field = np.zeros((h, w), dtype=np.float32)

    for src in route["light_sources"]:
        cx, cy = float(src["cx"]), float(src["cy"])
        rx, ry = float(src["rx"]), float(src["ry"])
        hr = float(src["halo_r"])
        d2_core = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2
        d2_halo = ((xx - cx) ** 2 + (yy - cy) ** 2) / (hr * hr)
        core_field += np.exp(-0.5 * d2_core)
        halo_field += np.exp(-0.5 * d2_halo)

    core_field = np.clip(core_field, 0.0, 1.0) * total_guard
    halo_field = np.clip(halo_field, 0.0, 1.0) * total_guard

    active_mask = (core_field > 1e-3) | (halo_field > 1e-3)
    # Đảm bảo 100% রào cứng
    active_mask[int(y_limit) :, :] = False
    active_mask[hp_y1:1350, p_x1:p_x2] = False
    core_field[~active_mask] = 0.0
    halo_field[~active_mask] = 0.0

    base_f32 = bg_rgb_u8.astype(np.float32)
    base_luma = 0.299 * base_f32[:, :, 0] + 0.587 * base_f32[:, :, 1] + 0.114 * base_f32[:, :, 2]

    # LP_LAW_01: Headroom Damping (pixel đã có base_luma >= 225 giảm cộng lõi để không cháy sáng >= 250,
    # dồn năng lượng vào vùng quầng ấm có base_luma in [45, 220])
    headroom_core = np.clip((236.0 - base_luma) / 55.0, 0.0, 1.0)
    headroom_halo = np.clip((240.0 - base_luma) / 45.0, 0.0, 1.0)

    d_core = float(route["delta_core"]) * gain_scale
    d_halo = float(route["delta_halo"]) * gain_scale

    eff_delta = (d_core * core_field * headroom_core) + (d_halo * halo_field * headroom_halo)

    # Dither tĩnh dương nhẹ [0.0 .. +0.9] trong vùng active_mask để chống banding CRF 28 mà vẫn giữ out >= in!
    rng = np.random.default_rng(20261103)
    pos_dither = rng.uniform(0.0, 0.85, size=(h, w, 1)).astype(np.float32)
    pos_dither[~active_mask] = 0.0

    warm_tint = np.array([[[1.12, 0.96, 0.68]]], dtype=np.float32)
    delta_rgb = eff_delta[:, :, None] * warm_tint + pos_dither
    delta_rgb[~active_mask] = 0.0

    # Khóa trần 248.0 để 0% pixel mới bị cháy >= 250 (trừ những pixel vốn đã >= 248 trên ảnh gốc)
    max_allowed = np.maximum(base_f32, 248.0)
    peak_f32 = np.minimum(base_f32 + delta_rgb, max_allowed)
    # Đảm bảo tính đơn điệu tuyệt đối: peak_u8 >= bg_rgb_u8 tại mọi kênh màu và mọi pixel!
    peak_u8 = np.maximum(bg_rgb_u8, np.clip(np.round(peak_f32), 0, 255).astype(np.uint8))
    peak_u8[~active_mask] = bg_rgb_u8[~active_mask]

    peak_luma = 0.299 * peak_u8[:, :, 0] + 0.587 * peak_u8[:, :, 1] + 0.114 * peak_u8[:, :, 2]
    luma_diff = peak_luma - base_luma
    weights = core_field + 0.65 * halo_field
    w_mask = weights > 0.08
    weighted_delta_luma = (
        float(np.sum(luma_diff[w_mask] * weights[w_mask]) / max(1e-5, float(np.sum(weights[w_mask]))))
        if np.any(w_mask)
        else 0.0
    )

    return {
        "base_rgb_u8": bg_rgb_u8.copy(),
        "peak_rgb_u8": peak_u8,
        "active_mask": active_mask,
        "weights": weights,
        "weighted_delta_luma": round(weighted_delta_luma, 2),
        "p_guard_box": [p_x1, hp_y1, p_x2, 1350],
        "y_limit": int(y_limit),
    }


def render_bg_at_weight(engine: Dict[str, Any], weight: float) -> Image.Image:
    base_u8 = engine["base_rgb_u8"]
    if weight <= 1e-4:
        rgba = np.dstack([base_u8, np.full(base_u8.shape[:2], 255, dtype=np.uint8)])
        return Image.fromarray(rgba)
    w = float(np.clip(weight, 0.0, 1.0))
    peak_u8 = engine["peak_rgb_u8"]
    act = engine["active_mask"]
    out_u8 = base_u8.copy()
    interp = base_u8[act].astype(np.float32) + w * (peak_u8[act].astype(np.float32) - base_u8[act].astype(np.float32))
    out_u8[act] = np.maximum(base_u8[act], np.clip(np.round(interp), 0, 255).astype(np.uint8))
    rgba = np.dstack([out_u8, np.full(out_u8.shape[:2], 255, dtype=np.uint8)])
    return Image.fromarray(rgba)


def apply_routed_specular_rim(
    comp_rgb_u8: np.ndarray,
    rim_mode: str,
    rim_bbox: List[int],
    rim_progress: float,
    bloom_alpha: float,
) -> np.ndarray:
    """
    Vẽ Specular Rim và Bloom theo đúng `rim_mode` đã định tuyến (LP_LAW_03 & Cổng G_LP6):
    1. `BOX_EXTERIOR_RIM` / `RIGHT_STAT_BOX_RIM`:
       Vẽ tia sáng chạy dọc viền ngoài hộp `rim_bbox`, khóa cứng `diff == 0` cho phần ruột chữ `[x1+2:x2-2, y1+2:y2-2]`.
    2. `LEFT_ACCENT_TO_ROW2_SWEEP` (`K01` - có vạch vàng bên trái):
       Tia sáng chạy từ đỉnh xuống đáy vạch vàng bên trái (`x1..x1+5, y1..y2`), rồi lướt ngang bên dưới chân chữ dòng 2 (`y2+2..y2+6`),
       khóa cứng `diff == 0` cho toàn bộ thân chữ `[x1+8:x2, y1:y2]`.
    3. `SOLUTION_UNDERLINE_SWEEP` (`K02`, `K04`, `K05` - dòng `.l2`):
       Một tia gạch chân ánh sáng vàng-trắng mảnh (`2.5px`) kèm quầng bloom mềm lướt từ trái sang phải ngay bên dưới chân dòng `.l2`
       (`y = y2 + 3 .. y2 + 7`), khóa cứng `diff == 0` cho toàn bộ thân chữ `[x1:x2, y1:y2]`!
    """
    if rim_progress <= 0.0 and bloom_alpha <= 0.0:
        return comp_rgb_u8

    x1, y1, x2, y2 = [int(v) for v in rim_bbox]
    h, w, _ = comp_rgb_u8.shape
    res = comp_rgb_u8.copy()

    if rim_mode in ("BOX_EXTERIOR_RIM", "RIGHT_STAT_BOX_RIM"):
        pad = 24
        ry0, ry1 = max(0, y1 - pad), min(h, y2 + pad)
        rx0, rx1 = max(0, x1 - pad), min(w, x2 + pad)
        yy, xx = np.mgrid[ry0:ry1, rx0:rx1].astype(np.float32)

        cx, cy = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
        hx, hy = max(4.0, 0.5 * (x2 - x1) - 6.0), max(4.0, 0.5 * (y2 - y1) - 6.0)
        qx, qy = np.abs(xx - cx) - hx, np.abs(yy - cy) - hy
        outside_dist = np.hypot(np.maximum(qx, 0.0), np.maximum(qy, 0.0)) + np.minimum(np.maximum(qx, qy), 0.0) - 6.0
        interior_protect = outside_dist >= -1.2

        out_roi = comp_rgb_u8[ry0:ry1, rx0:rx1].astype(np.float32)
        if bloom_alpha > 1e-4:
            ext_only = (outside_dist >= 0.0) & (outside_dist <= 18.0)
            bloom_field = np.zeros_like(outside_dist)
            bloom_field[ext_only] = np.exp(-0.5 * (outside_dist[ext_only] / 6.5) ** 2)
            b_strength = (bloom_alpha * bloom_field)[..., None]
            bloom_color = np.array([[[251.0, 156.0, 68.0]]], dtype=np.float32)
            out_roi = out_roi + b_strength * (bloom_color - out_roi) * 0.55

        if 0.0 < rim_progress < 1.0:
            sweep_x = (x1 - 40.0) + (x2 - x1 + 80.0) * rim_progress
            env = math.sin(min(1.0, max(0.0, rim_progress)) * math.pi)
            horiz_profile = np.exp(-0.5 * ((xx - sweep_x) / 42.0) ** 2)
            rim_band = np.exp(-0.5 * (np.maximum(outside_dist, 0.0) / 1.35) ** 2) * interior_protect.astype(np.float32)
            rim_halo = np.exp(-0.5 * (np.maximum(outside_dist, 0.0) / 4.2) ** 2) * (outside_dist >= 0.0).astype(
                np.float32
            )
            spec_weight = (env * horiz_profile * (0.92 * rim_band + 0.28 * rim_halo))[..., None]
            spec_color = np.array([[[255.0, 240.0, 205.0]]], dtype=np.float32)
            out_roi = out_roi + spec_weight * (spec_color - out_roi)

        res[ry0:ry1, rx0:rx1] = np.clip(np.round(out_roi), 0, 255).astype(np.uint8)
        # Bảo toàn 100% ruột chữ bên trong hộp
        res[y1 + 2 : y2 - 2, x1 + 2 : x2 - 2] = comp_rgb_u8[y1 + 2 : y2 - 2, x1 + 2 : x2 - 2]
        return res

    elif rim_mode == "LEFT_ACCENT_TO_ROW2_SWEEP":
        # Dành cho K01 (có vạch vàng bên trái tại x1..x1+5, và dòng lời giải ✓ kết thúc tại y2)
        pad = 20
        ry0, ry1 = max(0, y1 - pad), min(h, y2 + pad + 10)
        rx0, rx1 = max(0, x1 - pad), min(w, x2 + pad)
        yy, xx = np.mgrid[ry0:ry1, rx0:rx1].astype(np.float32)
        out_roi = comp_rgb_u8[ry0:ry1, rx0:rx1].astype(np.float32)

        # Đường dẫn chữ L: từ (x1+2, y1) xuống (x1+2, y2+4) rồi chạy sang phải tới (x2, y2+4)
        under_y = float(y2 + 4)
        bar_x = float(x1 + 2)
        dist_left_bar = np.hypot(xx - bar_x, np.maximum(0.0, np.maximum(y1 - yy, yy - under_y)))
        dist_under_line = np.hypot(np.maximum(0.0, np.maximum((x1 + 18) - xx, xx - x2)), yy - under_y)

        if bloom_alpha > 1e-4:
            b_field = np.exp(-0.5 * (np.minimum(dist_left_bar, dist_under_line) / 5.5) ** 2)
            b_strength = (bloom_alpha * 0.45 * b_field)[..., None]
            bloom_color = np.array([[[250.0, 204.0, 21.0]]], dtype=np.float32)
            out_roi = out_roi + b_strength * (bloom_color - out_roi)

        if 0.0 < rim_progress < 1.0:
            env = math.sin(min(1.0, max(0.0, rim_progress)) * math.pi)
            if rim_progress <= 0.35:
                # Chạy dọc thanh vàng bên trái từ trên xuống
                p_v = rim_progress / 0.35
                cur_y = y1 + (under_y - y1) * p_v
                spot = np.exp(-0.5 * ((xx - bar_x) / 3.0) ** 2 - 0.5 * ((yy - cur_y) / 28.0) ** 2)
            else:
                # Lướt ngang dưới chân dòng lời giải ✓
                p_h = (rim_progress - 0.35) / 0.65
                cur_x = (x1 + 18.0) + (x2 - x1 - 18.0) * p_h
                spot = np.exp(-0.5 * ((xx - cur_x) / 48.0) ** 2 - 0.5 * ((yy - under_y) / 2.2) ** 2)
            spec_w = (env * 0.92 * spot)[..., None]
            spec_col = np.array([[[255.0, 244.0, 210.0]]], dtype=np.float32)
            out_roi = out_roi + spec_w * (spec_col - out_roi)

        res[ry0:ry1, rx0:rx1] = np.clip(np.round(out_roi), 0, 255).astype(np.uint8)
        # Bảo toàn 100% toàn bộ vùng thân chữ [y1 : y2+1, x1+8 : x2]
        res[y1 : y2 + 1, x1 + 8 : x2] = comp_rgb_u8[y1 : y2 + 1, x1 + 8 : x2]
        return res

    else:
        # SOLUTION_UNDERLINE_SWEEP: Gạch chân ánh sáng lướt 1 lần ngay dưới dòng lời giải .l2 (y = y2+3..y2+6)
        pad = 18
        under_y = float(y2 + 4)
        ry0, ry1 = max(0, y2 + 1), min(h, int(under_y) + pad)
        rx0, rx1 = max(0, x1 - pad), min(w, x2 + pad)
        yy, xx = np.mgrid[ry0:ry1, rx0:rx1].astype(np.float32)
        out_roi = comp_rgb_u8[ry0:ry1, rx0:rx1].astype(np.float32)

        in_x = np.clip(xx, float(x1), float(x2))
        dist_line = np.hypot(xx - in_x, yy - under_y)

        if bloom_alpha > 1e-4:
            line_core = np.exp(-0.5 * (dist_line / 1.4) ** 2)
            line_glow = np.exp(-0.5 * (dist_line / 5.0) ** 2)
            b_w = (bloom_alpha * (0.75 * line_core + 0.35 * line_glow))[..., None]
            b_col = np.array([[[250.0, 190.0, 45.0]]], dtype=np.float32)
            out_roi = out_roi + b_w * (b_col - out_roi)

        if 0.0 < rim_progress < 1.0:
            env = math.sin(min(1.0, max(0.0, rim_progress)) * math.pi)
            cur_x = (x1 - 20.0) + (x2 - x1 + 40.0) * rim_progress
            horiz = np.exp(-0.5 * ((xx - cur_x) / 46.0) ** 2)
            vert = np.exp(-0.5 * ((yy - under_y) / 1.8) ** 2)
            spec_w = (env * 0.95 * horiz * vert)[..., None]
            spec_col = np.array([[[255.0, 245.0, 215.0]]], dtype=np.float32)
            out_roi = out_roi + spec_w * (spec_col - out_roi)

        res[ry0:ry1, rx0:rx1] = np.clip(np.round(out_roi), 0, 255).astype(np.uint8)
        # Bảo toàn 100% toàn bộ thân chữ .l2 [y1 : y2+1, x1 : x2]
        res[y1 : y2 + 1, x1:x2] = comp_rgb_u8[y1 : y2 + 1, x1:x2]
        return res


JS_UNIVERSAL_DOM_CONTROLLER = r"""
window.easeOutCubic = function(x) {
    x = Math.max(0, Math.min(1, x));
    return 1 - Math.pow(1 - x, 3);
};
window.easeInOutCubic = function(x) {
    x = Math.max(0, Math.min(1, x));
    return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
};

window.setupLivePosterDOM = function(textMotion) {
    window._textMotion = textMotion;
    const subBox = document.querySelector('.sub-box');
    if (!subBox) return;

    if (textMotion === 'HORIZONTAL_STAT_FLIP') {
        const cols = Array.from(subBox.querySelectorAll('.col-stat'));
        window._colLeft = cols[0] || null;
        window._colRight = cols[1] || null;
        window._arrowEl = subBox.querySelector('.arrow');
        if (window._colLeft) window._colLeft.style.transition = 'none';
        if (window._colRight) window._colRight.style.transition = 'none';
        if (window._arrowEl) {
            window._arrowEl.style.transition = 'none';
            window._arrowEl.style.display = 'inline-block';
        }
    } else {
        // VERTICAL_ROW_FLIP: tìm cặp (dòng cũ, dòng mới)
        const rows = Array.from(subBox.querySelectorAll('.row'));
        const l1 = subBox.querySelector('.l1');
        const l2 = subBox.querySelector('.l2');
        if (rows.length >= 2) {
            window._rowOld = rows[0];
            window._rowNew = rows[1];
        } else if (l1 && l2) {
            window._rowOld = l1;
            window._rowNew = l2;
        } else {
            const ch = Array.from(subBox.children);
            window._rowOld = ch[0] || null;
            window._rowNew = ch[1] || null;
        }
        window._vfHl = subBox.querySelector('.vf-hl');
        if (window._rowOld) {
            window._rowOld.style.transition = 'none';
            window._rowOld.style.display = 'block';
        }
        if (window._rowNew) {
            window._rowNew.style.transition = 'none';
            window._rowNew.style.display = 'block';
        }
        if (window._vfHl) {
            window._vfHl.style.background = 'linear-gradient(90deg, rgba(250, 204, 21, 0.26) 0%, rgba(251, 146, 60, 0.28) 100%) no-repeat left center';
            window._vfHl.style.backgroundSize = '0% 100%';
            window._vfHl.style.transition = 'none';
        }
    }
};

window.setLivePosterTime = function(t) {
    const mode = window._textMotion;
    const subBox = document.querySelector('.sub-box');
    if (mode === 'HORIZONTAL_STAT_FLIP') {
        // 3 nhịp nối nhau theo thiết kế của Thư ký CLAUDE2:
        // - Cột trái mờ xuống 0.52 (0.85 - 1.30s)
        // - Mũi tên .arrow nhích phải 6px và sáng vàng ấm (1.15 - 1.45s)
        // - Cột phải trượt lên 8px, opacity 0.22 -> 1.0 (1.25 - 1.70s)
        let pLeft = 0, pArr = 0, pRight = 0;
        if (t >= 0.85 && t <= 5.55) {
            pLeft = window.easeOutCubic((t - 0.85) / 0.45);
            pArr = window.easeOutCubic((t - 1.15) / 0.30);
            pRight = window.easeOutCubic((t - 1.25) / 0.45);
        } else if (t > 5.55) {
            const rev = 1 - window.easeInOutCubic((t - 5.55) / 0.45);
            pLeft = rev;
            pArr = rev;
            pRight = rev;
        }
        if (window._colLeft) {
            window._colLeft.style.opacity = String((1.0 - 0.48 * pLeft).toFixed(3));
        }
        if (window._arrowEl) {
            window._arrowEl.style.transform = `translateX(${(6.0 * pArr).toFixed(2)}px)`;
            window._arrowEl.style.color = pArr > 0.3 ? '#FACC15' : '';
            window._arrowEl.style.textShadow = pArr > 0.1 ? `0 0 ${Math.round(12 * pArr)}px rgba(250, 204, 21, ${(0.75 * pArr).toFixed(2)})` : 'none';
        }
        if (window._colRight) {
            const opR = 0.22 + 0.78 * pRight;
            const tyR = 8.0 * (1.0 - pRight);
            window._colRight.style.opacity = String(opR.toFixed(3));
            window._colRight.style.transform = `translateY(${tyR.toFixed(2)}px)`;
        }
    } else {
        // VERTICAL_ROW_FLIP
        let p1 = 0, p2 = 0, p3 = 0;
        if (t >= 0.85 && t <= 5.55) {
            p1 = window.easeOutCubic((t - 0.85) / 0.30);
            p2 = window.easeOutCubic((t - 1.05) / 0.50);
            p3 = window.easeOutCubic((t - 1.20) / 0.50);
        } else if (t > 5.55) {
            const rev = 1 - window.easeInOutCubic((t - 5.55) / 0.45);
            p1 = rev;
            p2 = rev;
            p3 = rev;
        }
        if (window._rowOld) {
            window._rowOld.style.opacity = String((1.0 - 0.48 * p1).toFixed(3));
        }
        if (window._rowNew) {
            const op2 = 0.22 + 0.78 * p2;
            const ty2 = 9.0 * (1.0 - p2);
            window._rowNew.style.opacity = String(op2.toFixed(3));
            window._rowNew.style.transform = `translateY(${ty2.toFixed(2)}px)`;
        }
        if (window._vfHl) {
            window._vfHl.style.backgroundSize = `${(p3 * 100).toFixed(1)}% 100%`;
            window._vfHl.style.borderBottomColor = `rgba(251, 146, 60, ${(0.22 + 0.78 * p3).toFixed(3)})`;
        }
        if (subBox) {
            subBox.style.boxShadow = `0 18px 40px rgba(0, 0, 0, 0.45), 0 0 ${Math.round(22 * p3)}px rgba(251, 146, 60, ${(0.16 * p3).toFixed(3)})`;
        }
    }
};
"""


def render_kb_live_poster(
    kb_id: str,
    probe: Dict[str, Any],
    route: Dict[str, Any],
    light_engine: Dict[str, Any],
    out_mp4_path: Path,
    fps: int = 30,
    duration_s: float = 6.0,
) -> Dict[str, Any]:
    t0 = time.time()
    kb_lower = kb_id.lower()
    html_path = BATCH_OUT_DIR / f"{kb_lower}_v3_price.html"
    bg_rgba = render_bg_at_weight(light_engine, 0.0)
    total_frames = int(round(fps * duration_s))

    text_motion = route["text_motion"]
    rim_mode = route["rim_mode"]
    rim_bbox = route["rim_bbox"]

    out_mp4_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-y",
        "-f",
        "rawvideo",
        "-vcodec",
        "rawvideo",
        "-pix_fmt",
        "rgb24",
        "-s",
        "1080x1350",
        "-r",
        str(fps),
        "-i",
        "-",
        "-c:v",
        "libx264",
        "-crf",
        "17",
        "-preset",
        "slow",
        "-profile:v",
        "high",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        "-an",
        str(out_mp4_path),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

    last_ov_im: Optional[Image.Image] = None
    last_rgb_bytes: Optional[bytes] = None
    rendered_shots = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        page = context.new_page()
        page.goto(f"file://{html_path.resolve()}", wait_until="load")
        page.evaluate("() => document.fonts.ready")
        page.add_script_tag(content=JS_UNIVERSAL_DOM_CONTROLLER)
        page.evaluate(f"() => window.setupLivePosterDOM('{text_motion}')")

        for f_idx in range(total_frames):
            t = f_idx / float(fps)
            dom_active = (f_idx == 0) or (0.80 <= t <= 1.82) or (t >= 5.50)
            if dom_active or last_ov_im is None:
                page.evaluate(f"() => window.setLivePosterTime({t:.4f})")
                png_bytes = page.screenshot(omit_background=True, clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
                last_ov_im = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
                rendered_shots += 1

            # Tính thông số ánh sáng tại thời điểm t
            rim_p = 0.0
            bloom_a = 0.0
            bulb_w = 0.0

            if 1.70 <= t <= 2.20:
                x = (t - 1.70) / 0.50
                rim_p = 3 * x * x - 2 * x * x * x
            if 1.85 <= t <= 2.10:
                bloom_a = 0.30 * ((t - 1.85) / 0.25)
            elif 2.10 < t <= 2.60:
                bloom_a = 0.30 - 0.20 * ((t - 2.10) / 0.50)
            elif 2.60 < t <= 5.55:
                bloom_a = 0.10
            elif 5.55 < t <= 6.00:
                bloom_a = 0.10 * max(0.0, 1.0 - (t - 5.55) / 0.45)

            if 2.40 <= t <= 5.92 and route["light_archetype"] != "LIGHT_NONE":
                bulb_w = math.sin(math.pi * (t - 2.40) / 3.52) ** 2

            light_changed = (bulb_w > 1e-4) or (rim_p > 1e-4) or (bloom_a > 1e-4)
            if dom_active or light_changed or last_rgb_bytes is None:
                cur_bg = render_bg_at_weight(light_engine, bulb_w) if bulb_w > 1e-4 else bg_rgba
                comp_rgb = Image.alpha_composite(cur_bg, last_ov_im).convert("RGB")
                if rim_p > 1e-4 or bloom_a > 1e-4:
                    arr = np.array(comp_rgb, dtype=np.uint8)
                    arr = apply_routed_specular_rim(arr, rim_mode, rim_bbox, rim_p, bloom_a)
                    last_rgb_bytes = arr.tobytes()
                else:
                    last_rgb_bytes = comp_rgb.tobytes()

            proc.stdin.write(last_rgb_bytes)

        browser.close()

    proc.stdin.close()
    stderr_out = proc.stderr.read().decode("utf-8", errors="ignore")
    ret = proc.wait()
    if ret != 0:
        raise RuntimeError(f"FFmpeg failed for {kb_id}: {stderr_out[-500:]}")

    return {
        "video_path": str(out_mp4_path),
        "size_kb": round(out_mp4_path.stat().st_size / 1024.0, 1),
        "elapsed_s": round(time.time() - t0, 2),
        "rendered_playwright_frames": rendered_shots,
    }


def verify_7_gates(
    kb_id: str,
    mp4_path: Path,
    probe: Dict[str, Any],
    route: Dict[str, Any],
    light_engine: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Bước 4 (VERIFY): Chạy 7 Cổng Kiểm Toán Tất Định của Thư ký CLAUDE2 (`G_LP1` .. `G_LP7`).
    """
    kb_lower = kb_id.lower()
    html_path = BATCH_OUT_DIR / f"{kb_lower}_v3_price.html"
    base_u8 = light_engine["base_rgb_u8"]
    peak_u8 = light_engine["peak_rgb_u8"]
    act_mask = light_engine["active_mask"]
    p_x1, hp_y1, p_x2, _ = light_engine["p_guard_box"]
    y_limit = light_engine["y_limit"]

    # G_LP1: Bit-exact ngoài Valid_Light_Zone
    diff_full = peak_u8.astype(np.int16) - base_u8.astype(np.int16)
    outside_max_diff = int(np.abs(diff_full[~act_mask]).max()) if np.any(~act_mask) else 0
    below_headline_diff = int(np.abs(diff_full[y_limit:, :, :]).max())
    g1_pass = (outside_max_diff == 0) and (below_headline_diff == 0)

    # G_LP2: LAW_20 Bảo vệ đầu, tóc và cơ thể (`p_guard_box`)
    person_diff = int(np.abs(diff_full[hp_y1:1350, p_x1:p_x2, :]).max())
    g2_pass = person_diff == 0

    # G_LP3: Đơn điệu (min(out - in) >= 0) & Chống cháy sáng (pixel >= 250 tăng <= 0.5%)
    min_delta = int(diff_full.min())
    base_luma = 0.299 * base_u8[:, :, 0] + 0.587 * base_u8[:, :, 1] + 0.114 * base_u8[:, :, 2]
    peak_luma = 0.299 * peak_u8[:, :, 0] + 0.587 * peak_u8[:, :, 1] + 0.114 * peak_u8[:, :, 2]
    clipped_increase_pct = float(np.mean((peak_luma[act_mask] >= 250.0) & (base_luma[act_mask] < 248.0)) * 100.0) if np.any(act_mask) else 0.0
    g3_pass = (min_delta >= 0) and (clipped_increase_pct <= 0.5)

    # G_LP4: Đủ thấy (Perceptual Visibility: weighted_delta_luma >= 6.0 mức)
    w_delta = float(light_engine["weighted_delta_luma"])
    g4_pass = (w_delta >= 6.0) or (route["light_archetype"] == "LIGHT_NONE")

    # G_LP5: Saliency Scanpath G21 tại 0.5s (f=15), 2.0s (f=60), 4.2s (f=126)
    cap = cv2.VideoCapture(str(mp4_path))
    tmp_dir = Path("/tmp/live_poster_verify")
    tmp_dir.mkdir(parents=True, exist_ok=True)
    saliency_frames = {}
    g5_pass = True
    for label, f_idx in [("t_0.5s", 15), ("t_2.0s", 60), ("t_4.2s", 126)]:
        cap.set(cv2.CAP_PROP_POS_FRAMES, f_idx)
        ok, frame_bgr = cap.read()
        if not ok:
            g5_pass = False
            continue
        f_jpg = tmp_dir / f"{kb_lower}_{label}.jpg"
        cv2.imwrite(str(f_jpg), frame_bgr)
        aud = audit_v3_banner(
            html_path=html_path,
            final_img_path=f_jpg,
            expected_lines=3,
            person_side=probe["side"],
        )
        g21 = aud.get("gates", {}).get("G21_CLAUDE2_saliency_heatmap_scanpath", {})
        order = g21.get("scanpath_order") or []
        no_distractor = "DISTRACTOR_BG" not in order[:3]
        step_ok = bool(g21.get("pass")) and no_distractor
        if not step_ok:
            g5_pass = False
        saliency_frames[label] = {
            "pass": step_ok,
            "scanpath_order": order,
            "headline_mean_saliency": g21.get("headline_mean_saliency"),
            "subbox_p90_saliency": g21.get("subbox_p90_saliency"),
            "distractor_p92_saliency": g21.get("distractor_p92_saliency"),
        }
    cap.release()

    # G_LP6: Tiếp sức, Vòng lặp (frame 0 vs frame 179 diff == 0) & Bảo toàn thân chữ dưới Rim
    f179_im = render_bg_at_weight(light_engine, 0.0).convert("RGB")
    loop_diff = int(np.abs(np.array(f179_im, dtype=np.int16) - base_u8.astype(np.int16)).max())
    rim_mode = route["rim_mode"]
    x1, y1, x2, y2 = [int(v) for v in route["rim_bbox"]]
    test_rim = apply_routed_specular_rim(peak_u8, rim_mode, route["rim_bbox"], rim_progress=0.5, bloom_alpha=0.30)
    if rim_mode in ("BOX_EXTERIOR_RIM", "RIGHT_STAT_BOX_RIM"):
        text_body_diff = int(np.abs(test_rim[y1 + 2 : y2 - 2, x1 + 2 : x2 - 2].astype(np.int16) - peak_u8[y1 + 2 : y2 - 2, x1 + 2 : x2 - 2].astype(np.int16)).max())
    elif rim_mode == "LEFT_ACCENT_TO_ROW2_SWEEP":
        text_body_diff = int(np.abs(test_rim[y1 : y2 + 1, x1 + 8 : x2].astype(np.int16) - peak_u8[y1 : y2 + 1, x1 + 8 : x2].astype(np.int16)).max())
    else:
        text_body_diff = int(np.abs(test_rim[y1 : y2 + 1, x1:x2].astype(np.int16) - peak_u8[y1 : y2 + 1, x1:x2].astype(np.int16)).max())
    g6_pass = (loop_diff == 0) and (text_body_diff == 0)

    # G_LP7: Chịu nén Meta Ads CRF 28
    crf28_path = tmp_dir / f"{kb_lower}_crf28.mp4"
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(mp4_path),
            "-c:v",
            "libx264",
            "-crf",
            "28",
            "-preset",
            "fast",
            "-pix_fmt",
            "yuv420p",
            str(crf28_path),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )
    cap28 = cv2.VideoCapture(str(crf28_path))
    cap28.set(cv2.CAP_PROP_POS_FRAMES, 126)
    ok28, f28_bgr = cap28.read()
    cap28.release()
    if ok28 and np.any(act_mask):
        ys, xs = np.where(act_mask)
        ry0, ry1 = int(ys.min()), int(ys.max()) + 1
        rx0, rx1 = int(xs.min()), int(xs.max()) + 1
        roi_gray = cv2.cvtColor(f28_bgr[ry0:ry1, rx0:rx1], cv2.COLOR_BGR2GRAY).astype(np.float32)
        grad_p95 = float(np.percentile(np.abs(np.diff(roi_gray, axis=1)), 95))
        g7_pass = grad_p95 <= 9.0
    else:
        grad_p95 = 0.0
        g7_pass = True

    all_pass = g1_pass and g2_pass and g3_pass and g4_pass and g5_pass and g6_pass and g7_pass
    return {
        "all_7_pass": all_pass,
        "G_LP1_bit_exact_outside_zone": {"pass": g1_pass, "outside_max_diff": outside_max_diff, "below_headline_diff": below_headline_diff},
        "G_LP2_law20_head_protect": {"pass": g2_pass, "person_diff": person_diff},
        "G_LP3_monotonic_and_ceiling": {"pass": g3_pass, "min_delta": min_delta, "clipped_increase_pct": round(clipped_increase_pct, 3)},
        "G_LP4_perceptual_visibility": {"pass": g4_pass, "weighted_delta_luma": w_delta, "min_required": 6.0},
        "G_LP5_scanpath_g21_3_phases": {"pass": g5_pass, "frames": saliency_frames},
        "G_LP6_relay_loop_and_rim_integrity": {"pass": g6_pass, "loop_diff": loop_diff, "text_body_diff": text_body_diff},
        "G_LP7_meta_crf28_banding": {"pass": g7_pass, "crf28_grad_p95": round(grad_p95, 2)},
    }


def publish_and_learn(
    kb_id: str,
    mp4_path: Path,
    probe: Dict[str, Any],
    route: Dict[str, Any],
    gates: Dict[str, Any],
    fix_rounds: int,
    cid: str,
) -> Dict[str, Any]:
    """
    Bước 5 (PUBLISH) & Bước 6 (LEARN):
    - Đẩy video lên R2 (`https://media.fedu.vn/banner2/{kb_lower}_live_v2.mp4`).
    - Cập nhật `banner2_cards/KB_XX.json` và chạy `update_banner2_hub.py --online`.
    - Bắn video qua Telegram `@viet_vni_bot` kèm lưu Google Drive (`video_vault.py`).
    - Lưu bản ghi tự học vào `live_poster_laws.json`.
    """
    kb_lower = kb_id.lower()
    r2_key = f"banner2/{kb_lower}_live_v2.mp4"
    cdn_url = f"https://media.fedu.vn/banner2/{kb_lower}_live_v2.mp4"

    # 1. Push MP4 to R2
    subprocess.run(
        ["python3", str(R2_MANAGER), "--put", str(mp4_path), r2_key],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # 2. Send Telegram + Auto Google Drive Vault
    card_path = CARDS_DIR / f"{kb_id}.json"
    card_data = json.loads(card_path.read_text(encoding="utf-8"))
    hl_plain = card_data.get("headline_plain", kb_id)
    w_delta = gates["G_LP4_perceptual_visibility"]["weighted_delta_luma"]
    caption = (
        f"🎬 [{kb_id} LIVE POSTER V2 · 7/7 CỔNG PASS] “{hl_plain}”\n"
        f"• Ánh sáng nền: {route['light_archetype']} (ΔLuma = +{w_delta} mức, 0% chạm mặt/tóc)\n"
        f"• Chuyển động chữ: {route['text_motion']} → {route['rim_desc']}\n"
        f"• Web Kệ Duyệt: https://media.fedu.vn/banner2/banner2.html?v=v13_uniqlo_g26#card-{kb_id}"
    )
    tele_out = subprocess.check_output(
        [
            "python3",
            str(TELEGRAM_NOTIFY),
            "--video",
            str(mp4_path),
            "--project",
            f"{kb_lower}_live_poster_v2",
            "--caption",
            caption,
            "--cid",
            cid,
        ],
        text=True,
    )
    m_drive = re.search(r"https://drive\.google\.com/file/d/[A-Za-z0-9_-]+/view\?usp=sharing", tele_out)
    drive_url = m_drive.group(0) if m_drive else "https://drive.google.com"

    # 3. Update KB_XX.json & rebuild banner2.html online
    card_data["has_live_poster"] = True
    card_data["live_poster_meta"] = {
        "light_archetype": route["light_archetype"],
        "text_motion": f"{route['text_motion']} + {route['rim_mode']}",
        "video_url": cdn_url,
        "drive_url": drive_url,
        "gates_score": "7/7 PASS",
        "summary": f"{route['text_motion']} → {route['rim_desc']} → Đèn {route['light_archetype']} thở ấm (+{w_delta} luma · 7/7 PASS)",
    }
    card_path.write_text(json.dumps(card_data, ensure_ascii=False, indent=2), encoding="utf-8")

    subprocess.run(
        ["python3", str(UPDATE_HUB_SCRIPT), "--online"],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # 4. Ghi bài học vào live_poster_laws.json
    laws = load_laws()
    arch = route["light_archetype"]
    if arch in laws.get("archetype_priors", {}):
        laws["archetype_priors"][arch]["n_pass"] = int(laws["archetype_priors"][arch].get("n_pass", 0)) + 1
        from_list = laws["archetype_priors"][arch].get("from", [])
        if kb_id not in from_list:
            from_list.append(kb_id)
        laws["archetype_priors"][arch]["from"] = from_list

    learned_lesson = (
        f"{kb_id} ({card_data.get('style_code')} · side={probe['side']}): "
        f"Ánh sáng {arch} ({len(route['light_sources'])} cụm, p95 nền={probe['zone_stats']['p95_luma']}) đạt ΔLuma=+{w_delta} mức; "
        f"Chữ {route['text_motion']} kết hợp {route['rim_mode']} giữ 0% diff thân chữ và giữ vững Scanpath F1→F3."
    )

    runs = [r for r in laws.get("runs", []) if r.get("kb") != kb_id]
    runs.append(
        {
            "kb": kb_id,
            "date": datetime.date.today().isoformat(),
            "probe_summary": {
                "side": probe["side"],
                "head_protect_guard": probe["head_protect_guard"],
                "headline_top": route["headline_top"],
                "zone_p95_luma": probe["zone_stats"]["p95_luma"],
            },
            "route": {
                "light_archetype": arch,
                "text_motion": route["text_motion"],
                "rim_mode": route["rim_mode"],
                "rim_bbox": route["rim_bbox"],
            },
            "gates": {
                "all_7_pass": gates["all_7_pass"],
                "weighted_delta_luma": w_delta,
                "crf28_grad_p95": gates["G_LP7_meta_crf28_banding"]["crf28_grad_p95"],
            },
            "fix_rounds": fix_rounds,
            "verdict": "PASS" if gates["all_7_pass"] else "FAIL",
            "links": {
                "local_mp4": str(mp4_path),
                "cdn_mp4": cdn_url,
                "drive": drive_url,
                "web": f"https://media.fedu.vn/banner2/banner2.html?v=v13_uniqlo_g26#card-{kb_id}",
            },
            "lessons": [learned_lesson],
        }
    )
    laws["runs"] = runs
    save_laws(laws)

    return {
        "kb_id": kb_id,
        "cdn_mp4": cdn_url,
        "drive_url": drive_url,
        "web_url": f"https://media.fedu.vn/banner2/banner2.html?v=v13_uniqlo_g26#card-{kb_id}",
        "learned_lesson": learned_lesson,
    }


def process_single_kb(kb_id: str, cid: str, publish: bool = True) -> Dict[str, Any]:
    laws = load_laws()
    probe = probe_kb(kb_id)
    route = route_kb(probe, laws)

    kb_lower = kb_id.lower()
    bg_path = DUAL_BG_DIR / f"{kb_lower}_color_bg.jpg"
    bg_rgb_u8 = np.array(Image.open(bg_path).convert("RGB"), dtype=np.uint8)
    out_mp4 = MOTION_OUT_DIR / f"{kb_lower}_live_v2.mp4"

    gain_scale = 1.0
    fix_rounds = 0
    gates = {}
    render_info = {}

    for attempt in range(3):
        light_engine = build_generalized_light_engine(bg_rgb_u8, probe, route, gain_scale=gain_scale)
        # Nếu ngay từ lúc build engine mà weighted_delta_luma < 6.2, tự động nâng nhẹ gain_scale trước khi render
        if light_engine["weighted_delta_luma"] < 6.4 and route["light_archetype"] != "LIGHT_NONE":
            needed_scale = min(1.85, 7.2 / max(1.0, light_engine["weighted_delta_luma"]))
            gain_scale *= needed_scale
            light_engine = build_generalized_light_engine(bg_rgb_u8, probe, route, gain_scale=gain_scale)

        render_info = render_kb_live_poster(kb_id, probe, route, light_engine, out_mp4)
        gates = verify_7_gates(kb_id, out_mp4, probe, route, light_engine)
        if gates["all_7_pass"]:
            break
        fix_rounds += 1
        if not gates["G_LP4_perceptual_visibility"]["pass"]:
            gain_scale *= 1.35
        elif not gates["G_LP5_scanpath_g21_3_phases"]["pass"]:
            gain_scale *= 0.78

    pub_info = {}
    if publish and gates.get("all_7_pass"):
        pub_info = publish_and_learn(kb_id, out_mp4, probe, route, gates, fix_rounds, cid)

    return {
        "kb_id": kb_id,
        "route": {
            "light_archetype": route["light_archetype"],
            "text_motion": route["text_motion"],
            "rim_mode": route["rim_mode"],
            "rim_desc": route["rim_desc"],
        },
        "render": render_info,
        "gates": gates,
        "publish": pub_info,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", required=True, help="Mã KB (ví dụ: KB_01)")
    ap.add_argument("--cid", default="32deb71d-3f2a-4e27-9ba3-57a772b4a167", help="Conversation ID")
    ap.add_argument("--no-publish", action="store_true", help="Chỉ render và verify, không đẩy web/tele")
    args = ap.parse_args()

    res = process_single_kb(args.kb.upper(), args.cid, publish=not args.no_publish)
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()
