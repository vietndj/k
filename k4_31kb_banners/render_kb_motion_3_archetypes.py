#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RENDER LIVE POSTER ARCHETYPES V1 (A, B, C) & V2 UPGRADE (V2, V2b, V2c) + 6-GATE VERIFIER
========================================================================================
Đóng gói theo chuẩn Hội thảo Gemini 4 Argon High × Thư ký CLAUDE2 (Opus 5.5):
- Tỷ lệ: 4:5 (1080x1350), 30fps, 6.0s (180 frames), H.264 yuv420p, +faststart, không âm thanh.
- Khung 0.0s hoàn chỉnh 100% chữ để làm Thumbnail an toàn.
- V1 Archetypes:
  + A: Lật Vế (Contrast Flip)
  + B: Nét Bút Biên Tập (Editorial Underline)
  + C: Đồng Hồ Lọc Vé (Deadline Strip)
- V2 Live Poster Upgrades (Tiếp Sức Chuyển Động + Specular Rim + Đèn Edison Thở Ấm):
  + V2  (`kb_12_motion_V2_lat_ve_rim_den_tho.mp4`): Lật Vế (0.85-1.65s) -> Specular Rim Sweep + Bloom dọc viền hộp lời giải (1.65-2.25s) -> 4 bóng đèn Edison hậu cảnh thở ấm (2.35-6.00s).
  + V2b (`kb_12_motion_V2b_dong_ho_den_tho.mp4`): Đồng Hồ Lọc Vé "THỨ 7 NÀY · 07–08/11" (1.85-2.30s) -> 4 bóng đèn Edison thở ấm (2.35-6.00s) cho nhóm Retargeting.
  + V2c (`kb_12_motion_V2c_cinemagraph_den_tho.mp4`): Cinemagraph Thuần Ánh Sáng (Chữ giữ tĩnh 100% như bản B2 đang thắng, chỉ có 4 bóng đèn Edison thở ấm nhịp đôi + Specular Rim lướt nhẹ qua viền hộp lời giải ở 1.20-1.75s).
- Kiểm định tự động 6 Cổng Toán Học của Thư ký CLAUDE2 (G_M1..G_M6).
"""

import argparse
import io
import json
import math
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

sys.path.insert(0, str(BASE_DIR))
from uiux_auditor import audit_v3_banner


# Tọa độ 4 bóng đèn Edison ấm trên kb_12_color_bg.jpg (đo bằng OpenCV Connected Components)
KB12_BULB_CENTERS: List[Tuple[float, float]] = [
    (825.8, 346.1),
    (879.0, 329.4),
    (941.9, 308.0),
    (1029.1, 287.9),
]


def build_bulb_breathing_engine(bg_rgb_u8: np.ndarray) -> Dict[str, Any]:
    """
    Khởi tạo mặt nạ quang học cho 4 bóng đèn Edison ở góc trên bên phải (y < 374, x >= 780).
    Đảm bảo:
    - Cổng 1: Mọi pixel có y >= 374 hoặc x < 780 có mask == 0 tuyệt đối (diff = 0).
    - Cổng 2: Giao với bbox khuôn mặt (x < 500) bằng 0 tuyệt đối (LAW_20).
    - Cổng 3: Luma đỉnh tại tâm đèn <= 200 (không cướp F1/F2 của Headline trắng 255).
    - Cổng 6: Tích hợp dither tĩnh (static blue-noise/gaussian σ=0.85) chỉ trong vùng mask > 0
      để triệt tiêu hiện tượng bệt dải màu (banding) khi Meta nén lại ở CRF 28.
    """
    h, w, _ = bg_rgb_u8.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)

    # Rào cứng bảo vệ đỉnh Headline (top = 377px) và bảo vệ bên trái (x < 780px)
    guard_y = np.zeros((h, w), dtype=np.float32)
    guard_y[yy <= 356.0] = 1.0
    trans_y = (yy > 356.0) & (yy < 374.0)
    guard_y[trans_y] = 0.5 * (1.0 + np.cos(np.pi * (yy[trans_y] - 356.0) / (374.0 - 356.0)))

    guard_x = np.zeros((h, w), dtype=np.float32)
    guard_x[xx >= 796.0] = 1.0
    trans_x = (xx >= 780.0) & (xx < 796.0)
    guard_x[trans_x] = 0.5 * (1.0 - np.cos(np.pi * (xx[trans_x] - 780.0) / (796.0 - 780.0)))

    hard_guard = guard_y * guard_x

    core_mask = np.zeros((h, w), dtype=np.float32)
    halo_mask = np.zeros((h, w), dtype=np.float32)

    for (cx, cy) in KB12_BULB_CENTERS:
        dx = xx - float(cx)
        dy = yy - float(cy)
        # Bóng đèn dây tóc có dáng hơi bầu dục dọc
        dist2_core = (dx * dx) / (16.5 * 16.5) + (dy * dy) / (22.0 * 22.0)
        dist2_halo = (dx * dx + dy * dy) / (42.0 * 42.0)
        core_mask += np.exp(-0.5 * dist2_core)
        halo_mask += np.exp(-0.5 * dist2_halo)

    core_mask = np.clip(core_mask, 0.0, 1.0) * hard_guard
    halo_mask = np.clip(halo_mask, 0.0, 1.0) * hard_guard

    # Chỉ giữ vùng thực sự có tác động trong ROI [y: 220..374, x: 780..1080]
    active_mask = (core_mask > 1e-4) | (halo_mask > 1e-4)
    # Khóa cứng 100% ngoài biên y < 374 và x >= 780
    active_mask[374:, :] = False
    active_mask[:, :780] = False
    core_mask[~active_mask] = 0.0
    halo_mask[~active_mask] = 0.0

    # Dither tĩnh cố định theo không gian (giống nhau ở mọi frame -> không tốn bitrate thời gian)
    rng = np.random.default_rng(20261103)
    static_dither = rng.normal(0.0, 0.75, size=(h, w, 1)).astype(np.float32)
    static_dither[~active_mask] = 0.0

    # Chuyển ROI sang không gian tuyến tính sRGB -> Linear
    roi_y0, roi_y1 = 210, 374
    roi_x0, roi_x1 = 780, 1080
    base_roi_u8 = bg_rgb_u8[roi_y0:roi_y1, roi_x0:roi_x1].copy()
    base_roi_norm = base_roi_u8.astype(np.float32) / 255.0
    base_roi_lin = np.power(np.clip(base_roi_norm, 0.0, 1.0), 2.2)

    core_roi = core_mask[roi_y0:roi_y1, roi_x0:roi_x1, None]
    halo_roi = halo_mask[roi_y0:roi_y1, roi_x0:roi_x1, None]
    act_roi = active_mask[roi_y0:roi_y1, roi_x0:roi_x1]
    dither_roi = static_dither[roi_y0:roi_y1, roi_x0:roi_x1]

    # Tint ấm dây tóc Edison (R=1.00, G=0.78, B=0.46)
    warm_tint = np.array([[[1.00, 0.78, 0.46]]], dtype=np.float32)

    return {
        "base_rgb_u8": bg_rgb_u8.copy(),
        "roi_bounds": (roi_y0, roi_y1, roi_x0, roi_x1),
        "base_roi_u8": base_roi_u8,
        "base_roi_lin": base_roi_lin,
        "core_roi": core_roi,
        "halo_roi": halo_roi,
        "act_roi": act_roi,
        "dither_roi": dither_roi,
        "warm_tint": warm_tint,
        "active_mask": active_mask,
    }


def render_bg_with_bulb_weight(engine: Dict[str, Any], weight: float) -> Image.Image:
    """
    Trả về ảnh nền RGBA tại mức thở `weight` in [0.0, 1.0].
    Khi weight <= 1e-4, trả về nguyên bản bit-exact 100%.
    Khi weight > 0:
    - Cộng ánh sáng tuyến tính tại lõi (+17% luma tại đỉnh) và quầng ấm (+5.5%).
    - Áp trần soft-knee để Luma (Y = 0.299R + 0.587G + 0.114B) trong vùng đèn luôn <= 199.0 (Cổng 3).
    - Ngoài vùng active_mask (đặc biệt y >= 374 hoặc x < 780), giữ nguyên bit-exact 100% (Cổng 1 & 2).
    """
    base_u8 = engine["base_rgb_u8"]
    if weight <= 1e-4:
        rgba = np.dstack([base_u8, np.full(base_u8.shape[:2], 255, dtype=np.uint8)])
        return Image.fromarray(rgba)

    w = float(np.clip(weight, 0.0, 1.0))
    y0, y1, x0, x1 = engine["roi_bounds"]
    base_lin = engine["base_roi_lin"]
    core_roi = engine["core_roi"]
    halo_roi = engine["halo_roi"]
    act_roi = engine["act_roi"]
    dither_roi = engine["dither_roi"]
    warm_tint = engine["warm_tint"]

    # Tăng sáng tuyến tính ở lõi bóng đèn + quầng ấm xung quanh tại đỉnh (w=1.0)
    delta_lin = (0.195 * core_roi + 0.058 * halo_roi) * warm_tint
    peak_lin = np.clip(base_lin + delta_lin, 0.0, 1.0)
    peak_srgb = np.power(peak_lin, 1.0 / 2.2) * 255.0 + dither_roi

    # Soft-knee ceiling trên trạng thái đỉnh để Luma (Rec.601 Y) không bao giờ vượt 199.0 (Cổng 3 <= 200)
    luma = 0.299 * peak_srgb[:, :, 0] + 0.587 * peak_srgb[:, :, 1] + 0.114 * peak_srgb[:, :, 2]
    knee_start = 178.0
    knee_max = 198.5
    over = luma > knee_start
    if np.any(over):
        excess = luma[over] - knee_start
        compressed = knee_start + (knee_max - knee_start) * np.tanh(excess / (knee_max - knee_start))
        scale = compressed / np.maximum(luma[over], 1e-5)
        for c in range(3):
            ch = peak_srgb[:, :, c]
            ch[over] = ch[over] * scale

    # Nội suy mượt giữa base_roi_u8 và peak_srgb theo trọng số w -> đảm bảo khi w -> 0 thì diff == 0 tuyệt đối!
    base_f32 = engine["base_roi_u8"].astype(np.float32)
    out_srgb = base_f32 + w * (peak_srgb - base_f32)

    roi_u8 = engine["base_roi_u8"].copy()
    computed_u8 = np.clip(np.round(out_srgb), 0, 255).astype(np.uint8)
    roi_u8[act_roi] = computed_u8[act_roi]

    full_u8 = base_u8.copy()
    full_u8[y0:y1, x0:x1] = roi_u8
    rgba = np.dstack([full_u8, np.full(full_u8.shape[:2], 255, dtype=np.uint8)])
    return Image.fromarray(rgba)


def apply_exterior_specular_rim(
    comp_rgb_u8: np.ndarray,
    vf_bbox: Tuple[int, int, int, int],
    rim_progress: float,
    bloom_alpha: float,
) -> np.ndarray:
    """
    Vẽ Specular Rim Sweep (1.70s -> 2.20s) và Exterior Edge Bloom (1.90s -> 2.60s)
    quanh hộp `.vf-hl` (left, top, right, bottom) sao cho:
    - Cổng 5: 100% pixel bên trong ruột hộp chữ `[x1+2 : x2-2, y1+2 : y2-2]` có mask == 0 tuyệt đối
      (KHÔNG chạm vào bất kỳ pixel nào của thân chữ `.vf-hl`).
    - Tia sáng Specular mảnh (dài 125px) chạy dọc theo đường viền trên & dưới của `.vf-hl`
      từ trái sang phải theo hàm cubic-bezier, kèm quầng bloom ấm rất mịn tỏa ra phía ngoài viền.
    """
    if rim_progress <= 0.0 and bloom_alpha <= 0.0:
        return comp_rgb_u8

    x1, y1, x2, y2 = vf_bbox
    h, w, _ = comp_rgb_u8.shape
    pad = 24
    ry0 = max(0, y1 - pad)
    ry1 = min(h, y2 + pad)
    rx0 = max(0, x1 - pad)
    rx1 = min(w, x2 + pad)

    yy, xx = np.mgrid[ry0:ry1, rx0:rx1].astype(np.float32)

    # Khoảng cách có dấu tới hình chữ nhật bo góc (x1..x2, y1..y2, radius=6px)
    cx = 0.5 * (x1 + x2)
    cy = 0.5 * (y1 + y2)
    hx = 0.5 * (x2 - x1) - 6.0
    hy = 0.5 * (y2 - y1) - 6.0
    qx = np.abs(xx - cx) - hx
    qy = np.abs(yy - cy) - hy
    outside_dist = np.hypot(np.maximum(qx, 0.0), np.maximum(qy, 0.0)) + np.minimum(np.maximum(qx, qy), 0.0) - 6.0

    # Mặt nạ bảo vệ tuyệt đối phần ruột chữ bên trong (outside_dist < -1.2px -> mask = 0)
    interior_protect = outside_dist >= -1.2

    out_roi = comp_rgb_u8[ry0:ry1, rx0:rx1].astype(np.float32)

    # 1. Exterior Edge Bloom (tỏa nhẹ ra ngoài viền từ 0px đến 16px, không vào trong ruột chữ)
    if bloom_alpha > 1e-4:
        ext_only = (outside_dist >= 0.0) & (outside_dist <= 18.0)
        bloom_field = np.zeros_like(outside_dist)
        bloom_field[ext_only] = np.exp(-0.5 * (outside_dist[ext_only] / 6.5) ** 2)
        b_strength = (bloom_alpha * bloom_field)[..., None]
        bloom_color = np.array([[[251.0, 156.0, 68.0]]], dtype=np.float32)
        out_roi = out_roi + b_strength * (bloom_color - out_roi) * 0.55

    # 2. Specular Rim Sweep chạy dọc theo đúng vành viền (|outside_dist| <= 1.25px, nhưng >= -1.2px)
    if 0.0 < rim_progress < 1.0:
        # Vị trí tâm tia sáng quét từ x1 - 40 đến x2 + 40
        sweep_x = (x1 - 40.0) + (x2 - x1 + 80.0) * rim_progress
        # Độ mờ dần ở đầu và cuối hành trình
        env = math.sin(min(1.0, max(0.0, rim_progress)) * math.pi)
        # Bề rộng đoạn sáng 120px (sigma = 42px)
        horiz_profile = np.exp(-0.5 * ((xx - sweep_x) / 42.0) ** 2)

        # Vành viền 1.5px + hào quang sát mép ngoài 4px (hoàn toàn ngoài ruột chữ)
        rim_band = np.exp(-0.5 * (np.maximum(outside_dist, 0.0) / 1.35) ** 2) * interior_protect.astype(np.float32)
        rim_halo = np.exp(-0.5 * (np.maximum(outside_dist, 0.0) / 4.2) ** 2) * (outside_dist >= 0.0).astype(np.float32)

        spec_weight = (env * horiz_profile * (0.92 * rim_band + 0.28 * rim_halo))[..., None]
        spec_color = np.array([[[255.0, 240.0, 205.0]]], dtype=np.float32)
        out_roi = out_roi + spec_weight * (spec_color - out_roi)

    # Khóa cứng 100% phần ruột chữ bên trong hộp .vf-hl [y1+2 : y2-2, x1+2 : x2-2]
    res = comp_rgb_u8.copy()
    res[ry0:ry1, rx0:rx1] = np.clip(np.round(out_roi), 0, 255).astype(np.uint8)
    res[y1 + 2 : y2 - 2, x1 + 2 : x2 - 2] = comp_rgb_u8[y1 + 2 : y2 - 2, x1 + 2 : x2 - 2]
    return res


JS_CONTROLLER = r"""
window.easeOutCubic = function(x) {
    x = Math.max(0, Math.min(1, x));
    return 1 - Math.pow(1 - x, 3);
};
window.easeInOutCubic = function(x) {
    x = Math.max(0, Math.min(1, x));
    return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
};

window.setupArchetype = function(mode) {
    window._motionMode = mode;
    const h = document.querySelector('.headline');
    const hl = document.querySelector('.headline .hl');
    const subBox = document.querySelector('.sub-box');

    if (mode === 'A' || mode === 'V2' || mode === 'V2c') {
        const children = subBox ? Array.from(subBox.children) : [];
        window._subRow1 = children[0] || null;
        window._subRow2 = children[1] || null;
        window._vfHl = subBox ? subBox.querySelector('.vf-hl') : null;

        if (window._subRow1) {
            window._subRow1.style.willChange = 'opacity, transform';
            window._subRow1.style.transition = 'none';
        }
        if (window._subRow2) {
            window._subRow2.style.willChange = 'opacity, transform';
            window._subRow2.style.transition = 'none';
        }
        if (window._vfHl && mode !== 'V2c') {
            window._vfHl.style.background = 'linear-gradient(90deg, rgba(250, 204, 21, 0.26) 0%, rgba(251, 146, 60, 0.28) 100%) no-repeat left center';
            window._vfHl.style.backgroundSize = '0% 100%';
            window._vfHl.style.transition = 'none';
        }
    } else if (mode === 'B') {
        if (hl) {
            hl.style.position = 'relative';
            hl.style.display = 'inline-block';
            const rect = hl.getBoundingClientRect();
            const w = Math.max(80, Math.round(rect.width));
            const svgNS = 'http://www.w3.org/2000/svg';
            const svg = document.createElementNS(svgNS, 'svg');
            svg.setAttribute('width', String(w + 10));
            svg.setAttribute('height', '18');
            svg.setAttribute('viewBox', `0 0 ${w + 10} 18`);
            svg.style.position = 'absolute';
            svg.style.left = '-2px';
            svg.style.bottom = '-10px';
            svg.style.overflow = 'visible';
            svg.style.pointerEvents = 'none';

            const path = document.createElementNS(svgNS, 'path');
            const d = `M 2 11 Q ${Math.round(w * 0.46)} 5.5, ${w + 2} 9`;
            path.setAttribute('d', d);
            path.setAttribute('fill', 'none');
            path.setAttribute('stroke', '#FB923C');
            path.setAttribute('stroke-width', '5.5');
            path.setAttribute('stroke-linecap', 'round');

            svg.appendChild(path);
            hl.appendChild(svg);

            const len = path.getTotalLength ? path.getTotalLength() : (w + 12);
            path.style.strokeDasharray = `${len}`;
            path.style.strokeDashoffset = `${len}`;
            window._underlineSvg = svg;
            window._underlinePath = path;
            window._underlineLen = len;
        }
    } else if (mode === 'C' || mode === 'V2b') {
        const whenEl = document.querySelector('.d3-when, .d2-when, .d1-eyebrow');
        if (whenEl) {
            const dotEl = whenEl.querySelector('.dot');
            const spans = Array.from(whenEl.querySelectorAll('span')).filter(s => !s.classList.contains('dot'));
            const textSpan = spans[0] || whenEl;
            const origText = textSpan.textContent.trim();

            const wrap = document.createElement('span');
            wrap.style.position = 'relative';
            wrap.style.display = 'inline-flex';
            wrap.style.alignItems = 'center';
            wrap.style.height = '28px';
            wrap.style.overflow = 'hidden';
            wrap.style.verticalAlign = 'middle';

            const s1 = document.createElement('span');
            s1.textContent = origText;
            s1.style.display = 'block';
            s1.style.whiteSpace = 'nowrap';
            s1.style.willChange = 'transform, opacity';

            const s2 = document.createElement('span');
            s2.innerHTML = `<strong style="color:#FACC15;font-family:'SubBold',sans-serif;font-weight:700;">THỨ 7 NÀY · 07–08/11</strong> <span style="color:#F8FAFC;">· HN</span>`;
            s2.style.position = 'absolute';
            s2.style.left = '0';
            s2.style.top = '0';
            s2.style.height = '28px';
            s2.style.display = 'flex';
            s2.style.alignItems = 'center';
            s2.style.whiteSpace = 'nowrap';
            s2.style.willChange = 'transform, opacity';
            s2.style.transform = 'translateY(28px)';
            s2.style.opacity = '0';

            wrap.appendChild(s1);
            wrap.appendChild(s2);

            if (textSpan !== whenEl) {
                textSpan.replaceWith(wrap);
            } else {
                whenEl.innerHTML = '';
                if (dotEl) whenEl.appendChild(dotEl);
                whenEl.appendChild(wrap);
            }
            const w1 = s1.getBoundingClientRect().width;
            const w2 = s2.getBoundingClientRect().width;
            wrap.style.width = Math.ceil(Math.max(w1, w2) + 6) + 'px';

            window._slot1 = s1;
            window._slot2 = s2;
            window._dotEl = dotEl;
        }
    }

    const hRect = h ? h.getBoundingClientRect() : null;
    const subRect = subBox ? subBox.getBoundingClientRect() : null;
    const vfEl = document.querySelector('.sub-box .vf-hl');
    const vfRect = vfEl ? vfEl.getBoundingClientRect() : null;
    const gapHeadToSub = (hRect && subRect) ? (subRect.top - hRect.bottom) : 999;
    return {
        mode: mode,
        gap_head_to_sub_px: Math.round(gapHeadToSub * 10) / 10,
        underline_clearance_px: mode === 'B' ? Math.round((gapHeadToSub - 10) * 10) / 10 : Math.round(gapHeadToSub * 10) / 10,
        vf_bbox: vfRect ? [Math.round(vfRect.left), Math.round(vfRect.top), Math.round(vfRect.right), Math.round(vfRect.bottom)] : [575, 764, 992, 809]
    };
};

window.setMotionTime = function(t) {
    const mode = window._motionMode;
    if (mode === 'A' || mode === 'V2') {
        const r1 = window._subRow1;
        const r2 = window._subRow2;
        const hl = window._vfHl;
        const subBox = document.querySelector('.sub-box');

        let p1 = 0, p2 = 0, p3 = 0;
        if (t >= 0.85 && t <= 5.55) {
            p1 = window.easeOutCubic((t - 0.85) / 0.30);
            p2 = window.easeOutCubic((t - 1.05) / 0.50);
            p3 = window.easeOutCubic((t - 1.20) / 0.50);
        } else if (t > 5.55) {
            const pOut = window.easeInOutCubic((t - 5.55) / 0.45);
            const rev = 1 - pOut;
            p1 = rev;
            p2 = rev;
            p3 = rev;
        }

        if (r1) {
            r1.style.opacity = String(1.0 - 0.48 * p1);
        }
        if (r2) {
            const op2 = 0.22 + 0.78 * p2;
            const ty2 = 9 * (1 - p2);
            r2.style.opacity = String(op2);
            r2.style.transform = `translateY(${ty2.toFixed(2)}px)`;
        }
        if (hl) {
            hl.style.backgroundSize = `${(p3 * 100).toFixed(1)}% 100%`;
            hl.style.borderBottomColor = `rgba(251, 146, 60, ${(0.22 + 0.78 * p3).toFixed(3)})`;
        }
        if (subBox) {
            subBox.style.borderColor = `rgba(251, 146, 60, ${(0.55 + 0.45 * p3).toFixed(3)})`;
            subBox.style.boxShadow = `0 18px 40px rgba(0, 0, 0, 0.45), 0 0 ${Math.round(24 * p3)}px rgba(251, 146, 60, ${(0.18 * p3).toFixed(3)})`;
        }
    } else if (mode === 'V2c') {
        // Bản Cinemagraph thuần ánh sáng: chữ đứng tĩnh 100% ngay từ frame 0
    } else if (mode === 'B') {
        const path = window._underlinePath;
        const svg = window._underlineSvg;
        const len = window._underlineLen || 160;
        const hl = document.querySelector('.headline .hl');

        let pDraw = 0;
        let op = 0.92;
        if (t < 0.25) {
            pDraw = 0;
            op = 0;
        } else if (t >= 0.25 && t <= 0.78) {
            pDraw = window.easeOutCubic((t - 0.25) / 0.53);
            op = 0.92;
        } else if (t > 0.78 && t <= 5.60) {
            pDraw = 1;
            op = 0.92;
        } else {
            pDraw = 1;
            const pOut = window.easeInOutCubic((t - 5.60) / 0.40);
            op = 0.92 * (1 - pOut);
        }

        if (path) {
            path.style.strokeDashoffset = String((len * (1 - pDraw)).toFixed(2));
        }
        if (svg) {
            svg.style.opacity = String(op.toFixed(3));
        }
        if (hl) {
            let glow = 0;
            if (t >= 0.25 && t <= 0.95) {
                glow = Math.sin(Math.min(1, (t - 0.25) / 0.70) * Math.PI);
            }
            hl.style.textShadow = `0 12px 30px rgba(0, 0, 0, 0.78), 0 0 ${Math.round(22 * glow)}px rgba(251, 146, 60, ${(0.55 * glow).toFixed(3)})`;
        }
    } else if (mode === 'C' || mode === 'V2b') {
        const s1 = window._slot1;
        const s2 = window._slot2;
        const dot = window._dotEl;

        let p = 0;
        if (t < 1.85) {
            p = 0;
        } else if (t >= 1.85 && t <= 2.30) {
            p = window.easeOutCubic((t - 1.85) / 0.45);
        } else if (t > 2.30 && t <= 5.45) {
            p = 1;
        } else if (t > 5.45 && t <= 5.90) {
            p = 1 - window.easeInOutCubic((t - 5.45) / 0.45);
        } else {
            p = 0;
        }

        if (s1) {
            s1.style.transform = `translateY(${(-28 * p).toFixed(2)}px)`;
            s1.style.opacity = String((1 - p).toFixed(3));
        }
        if (s2) {
            s2.style.transform = `translateY(${(28 * (1 - p)).toFixed(2)}px)`;
            s2.style.opacity = String(p.toFixed(3));
        }
        if (dot) {
            dot.style.background = p > 0.5 ? '#FACC15' : '#FB923C';
            dot.style.boxShadow = `0 0 ${Math.round(12 * p)}px rgba(250, 204, 21, ${(0.85 * p).toFixed(3)})`;
        }
    }
};
"""


def is_active_dom_transition_frame(mode: str, frame_idx: int, fps: int = 30) -> bool:
    if frame_idx == 0:
        return True
    t = frame_idx / float(fps)
    if mode in ("A", "V2"):
        return (0.80 <= t <= 1.82) or (t >= 5.50)
    elif mode == "B":
        return (0.20 <= t <= 1.02) or (t >= 5.55)
    elif mode in ("C", "V2b"):
        return (1.80 <= t <= 2.36) or (5.40 <= t <= 5.95)
    elif mode == "V2c":
        return False
    return True


def compute_v2_lighting_params(mode: str, t: float) -> Tuple[float, float, float]:
    """
    Trả về `(bulb_weight, rim_progress, bloom_alpha)` tại thời điểm `t` (giây):
    - Mode V2 (Chuẩn Thư ký CLAUDE2):
      + 0.00 - 1.70s: Đèn tĩnh (0.0), Rim = 0.0 (tập trung Lật vế 0.85-1.70s).
      + 1.70 - 2.20s: Specular Rim Sweep chạy dọc viền `.vf-hl` (0.0 -> 1.0).
      + 1.90 - 5.50s: Exterior Edge Bloom lên đỉnh 0.30 tại 2.05s rồi dịu về 0.10 giữ đến 5.50s.
      + 2.40 - 6.00s: 4 bóng đèn Edison hậu cảnh thở ấm `sin^2(pi * (t - 2.40) / 3.60)` (đỉnh 1.0 tại 4.20s, về 0.0 tại 6.00s).
    - Mode V2b (Đồng Hồ Lọc Vé + Đèn Thở cho nhóm C Retargeting):
      + 1.85 - 2.30s: Cuộn ngày sang "THỨ 7 NÀY · 07–08/11".
      + 2.40 - 6.00s: 4 bóng đèn Edison hậu cảnh thở ấm `sin^2(pi * (t - 2.40) / 3.60)`.
    - Mode V2c (Cinemagraph Thuần Ánh Sáng - Chữ đứng yên 100%):
      + 0.20 - 6.00s: 4 bóng đèn Edison thở ấm nhịp đôi êm ái `sin^2(2 * pi * (t - 0.20) / 5.80)`.
      + 1.20 - 1.75s: Specular Rim Sweep chạy nhẹ dọc viền `.vf-hl` kèm Bloom dịu.
    """
    bulb_w = 0.0
    rim_p = 0.0
    bloom_a = 0.0

    if mode == "V2":
        if 1.70 <= t <= 2.20:
            x = (t - 1.70) / 0.50
            # Cubic ease-in-out nhẹ
            rim_p = 3 * x * x - 2 * x * x * x
        if 1.85 <= t <= 2.10:
            bloom_a = 0.30 * ((t - 1.85) / 0.25)
        elif 2.10 < t <= 2.60:
            bloom_a = 0.30 - 0.20 * ((t - 2.10) / 0.50)
        elif 2.60 < t <= 5.55:
            bloom_a = 0.10
        elif 5.55 < t <= 6.00:
            bloom_a = 0.10 * max(0.0, 1.0 - (t - 5.55) / 0.45)

        if 2.40 <= t <= 5.92:
            bulb_w = math.sin(math.pi * (t - 2.40) / 3.52) ** 2

    elif mode == "V2b":
        if 2.40 <= t <= 5.92:
            bulb_w = math.sin(math.pi * (t - 2.40) / 3.52) ** 2

    elif mode == "V2c":
        if 0.20 <= t <= 5.92:
            bulb_w = math.sin(2.0 * math.pi * (t - 0.20) / 5.72) ** 2
        if 1.20 <= t <= 1.75:
            x = (t - 1.20) / 0.55
            rim_p = 3 * x * x - 2 * x * x * x
        if 1.30 <= t <= 1.60:
            bloom_a = 0.28 * ((t - 1.30) / 0.30)
        elif 1.60 < t <= 2.20:
            bloom_a = 0.28 * (1.0 - (t - 1.60) / 0.60)

    return bulb_w, rim_p, bloom_a


def render_single_archetype_video(
    page,
    html_path: Path,
    bg_rgba: Image.Image,
    bulb_engine: Dict[str, Any],
    mode: str,
    out_mp4_path: Path,
    fps: int = 30,
    duration_s: float = 6.0,
) -> Dict[str, Any]:
    t0 = time.time()
    total_frames = int(round(fps * duration_s))

    page.goto(f"file://{html_path.resolve()}", wait_until="load")
    page.evaluate("() => document.fonts.ready")
    page.add_script_tag(content=JS_CONTROLLER)
    gate_info = page.evaluate(f"() => window.setupArchetype('{mode}')")
    vf_bbox = tuple(gate_info.get("vf_bbox", [575, 764, 992, 809]))

    out_mp4_path.parent.mkdir(parents=True, exist_ok=True)
    is_v2_family = mode.startswith("V2")
    crf_val = "17" if is_v2_family else "15"
    preset_val = "slow" if is_v2_family else "medium"

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
        crf_val,
        "-preset",
        preset_val,
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

    for f_idx in range(total_frames):
        t = f_idx / float(fps)
        dom_changed = (last_ov_im is None) or is_active_dom_transition_frame(mode, f_idx, fps)
        if dom_changed:
            page.evaluate(f"() => window.setMotionTime({t:.4f})")
            png_bytes = page.screenshot(omit_background=True, clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            last_ov_im = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
            rendered_shots += 1

        bulb_w, rim_p, bloom_a = compute_v2_lighting_params(mode, t)
        light_changed = (bulb_w > 1e-4) or (rim_p > 1e-4) or (bloom_a > 1e-4)

        if dom_changed or light_changed or last_rgb_bytes is None:
            cur_bg = render_bg_with_bulb_weight(bulb_engine, bulb_w) if bulb_w > 1e-4 else bg_rgba
            comp_rgb = Image.alpha_composite(cur_bg, last_ov_im).convert("RGB")
            if rim_p > 1e-4 or bloom_a > 1e-4:
                arr = np.array(comp_rgb, dtype=np.uint8)
                arr = apply_exterior_specular_rim(arr, vf_bbox, rim_p, bloom_a)
                last_rgb_bytes = arr.tobytes()
            else:
                last_rgb_bytes = comp_rgb.tobytes()

        proc.stdin.write(last_rgb_bytes)

    proc.stdin.close()
    stderr_out = proc.stderr.read().decode("utf-8", errors="ignore")
    ret = proc.wait()
    if ret != 0:
        raise RuntimeError(f"FFmpeg failed for mode {mode}: {stderr_out[-500:]}")

    elapsed = round(time.time() - t0, 2)
    size_kb = round(out_mp4_path.stat().st_size / 1024.0, 1)
    return {
        "mode": mode,
        "video_path": str(out_mp4_path),
        "size_kb": size_kb,
        "elapsed_s": elapsed,
        "rendered_playwright_frames": rendered_shots,
        "total_frames": total_frames,
        "gate_info": gate_info,
    }


def run_claude2_6_gates_verifier(
    mp4_path: Path,
    html_path: Path,
    bg_rgb_u8: np.ndarray,
    bulb_engine: Dict[str, Any],
    vf_bbox: Tuple[int, int, int, int],
) -> Dict[str, Any]:
    """
    Chạy 6 Cổng Verifier bắt buộc của Thư ký CLAUDE2 cho Live Poster V2:
    1. G_M1 (Background Bit-Exact Outside Bulb Mask): Mọi pixel có y >= 374 hoặc x < 780 trên lớp nền có diff == 0.
    2. G_M2 (LAW_20 Zero Face Mask Overlap): Giao giữa mask đèn thở và vùng mặt nhân vật bằng 0 tuyệt đối.
    3. G_M3 (Peak Bulb Luma <= 200 & Seamless Loop): Luma đỉnh vùng đèn tại t=4.20s <= 200.0; nền frame 0 và frame 179 lệch <= 1 mức.
    4. G_M4 (G21 Saliency Scanpath @ 0.5s, 2.0s, 4.2s): Đèn không cướp F1/F2 của {FACE, HEADLINE} ở bất kỳ thời điểm nào.
    5. G_M5 (Rim Interior Text Integrity): 0 pixel bên trong thân chữ `.vf-hl` bị đổi giá trị khi Rim quét qua.
    6. G_M6 (Meta CRF-28 Re-encode Banding Check): Nén thử CRF 28 mô phỏng Meta, độ mượt gradient vùng quầng đèn không bị vỡ bậc.
    """
    # Cổng 1: Kiểm tra nền tại đỉnh thở (t = 4.20s, weight = 1.0)
    peak_bg_im = render_bg_with_bulb_weight(bulb_engine, 1.0).convert("RGB")
    peak_bg_u8 = np.array(peak_bg_im, dtype=np.uint8)
    diff_full = np.abs(peak_bg_u8.astype(np.int16) - bg_rgb_u8.astype(np.int16))
    max_diff_below_374 = int(diff_full[374:, :, :].max())
    max_diff_left_780 = int(diff_full[:, :780, :].max())
    g1_pass = (max_diff_below_374 == 0) and (max_diff_left_780 == 0)

    # Cổng 2: Giao giữa active_mask và vùng bảo vệ mặt/người bên trái (x < 520)
    act_mask = bulb_engine["active_mask"]
    face_overlap_pixels = int(act_mask[:, :520].sum())
    g2_pass = face_overlap_pixels == 0

    # Cổng 3: Luma đỉnh tại t=4.20s trong vùng đèn <= 200, và độ lệch frame 0 vs frame 179 <= 1
    roi_peak = peak_bg_u8[210:374, 780:1080].astype(np.float32)
    luma_peak = 0.299 * roi_peak[:, :, 0] + 0.587 * roi_peak[:, :, 1] + 0.114 * roi_peak[:, :, 2]
    max_bulb_luma = float(round(luma_peak[bulb_engine["act_roi"]].max(), 2))
    w_f179, _, _ = compute_v2_lighting_params("V2", 179.0 / 30.0)
    f179_bg_u8 = np.array(render_bg_with_bulb_weight(bulb_engine, w_f179).convert("RGB"), dtype=np.uint8)
    loop_diff_max = int(np.abs(f179_bg_u8.astype(np.int16) - bg_rgb_u8.astype(np.int16)).max())
    g3_pass = (max_bulb_luma <= 200.0) and (loop_diff_max <= 1)

    # Cổng 5: Kiểm tra Rim không chạm ruột chữ .vf-hl
    x1, y1, x2, y2 = vf_bbox
    dummy_after = apply_exterior_specular_rim(peak_bg_u8, vf_bbox, rim_progress=0.5, bloom_alpha=0.30)
    interior_diff = int(
        np.abs(
            dummy_after[y1 + 2 : y2 - 2, x1 + 2 : x2 - 2].astype(np.int16)
            - peak_bg_u8[y1 + 2 : y2 - 2, x1 + 2 : x2 - 2].astype(np.int16)
        ).max()
    )
    g5_pass = interior_diff == 0

    # Trích xuất 3 frame thực tế từ video MP4 tại 0.5s (f=15), 2.0s (f=60), 4.2s (f=126) để chạy G21 Saliency
    cap = cv2.VideoCapture(str(mp4_path))
    saliency_checks = {}
    g4_pass = True
    tmp_dir = Path("/tmp/kb12_v2_gate_frames")
    tmp_dir.mkdir(parents=True, exist_ok=True)
    for label, f_idx in [("t_0.5s", 15), ("t_2.0s", 60), ("t_4.2s", 126)]:
        cap.set(cv2.CAP_PROP_POS_FRAMES, f_idx)
        ok, frame_bgr = cap.read()
        if not ok:
            g4_pass = False
            continue
        f_jpg = tmp_dir / f"{mp4_path.stem}_{label}.jpg"
        cv2.imwrite(str(f_jpg), frame_bgr)
        aud = audit_v3_banner(
            html_path=html_path,
            final_img_path=f_jpg,
            expected_lines=3,
            person_side="right",
        )
        g21 = aud.get("gates", {}).get("G21_CLAUDE2_saliency_heatmap_scanpath", {})
        order = g21.get("scanpath_order") or []
        no_distractor = "DISTRACTOR_BG" not in order[:3]
        step_ok = bool(g21.get("pass")) and no_distractor
        if not step_ok:
            g4_pass = False
        saliency_checks[label] = {
            "pass": step_ok,
            "scanpath_order": order,
            "headline_mean_saliency": g21.get("headline_mean_saliency"),
            "subbox_p90_saliency": g21.get("subbox_p90_saliency"),
            "distractor_p92_saliency": g21.get("distractor_p92_saliency"),
        }
    cap.release()

    # Cổng 6: Nén thử CRF 28 mô phỏng Meta Ads và đo sai số banding ở vùng đèn
    crf28_path = tmp_dir / f"{mp4_path.stem}_meta_crf28.mp4"
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
    ok28, frame28_bgr = cap28.read()
    cap28.release()
    if ok28:
        roi28_gray = cv2.cvtColor(frame28_bgr[220:374, 780:1080], cv2.COLOR_BGR2GRAY).astype(np.float32)
        grad_x = np.abs(np.diff(roi28_gray, axis=1))
        # Tỷ lệ bước nhảy luma phẳng cục bộ hoặc gãy bậc
        p95_step = float(np.percentile(grad_x, 95))
        g6_pass = p95_step <= 8.5
    else:
        p95_step = 99.0
        g6_pass = False

    all_pass = g1_pass and g2_pass and g3_pass and g4_pass and g5_pass and g6_pass
    return {
        "all_6_gates_pass": all_pass,
        "G_M1_bg_outside_mask_zero_diff": {
            "pass": g1_pass,
            "max_diff_y_ge_374": max_diff_below_374,
            "max_diff_x_lt_780": max_diff_left_780,
        },
        "G_M2_law20_zero_face_mask_overlap": {
            "pass": g2_pass,
            "face_overlap_pixels": face_overlap_pixels,
        },
        "G_M3_peak_bulb_luma_and_loop": {
            "pass": g3_pass,
            "max_bulb_luma_at_4_2s": max_bulb_luma,
            "ceiling": 200.0,
            "loop_frame0_vs_179_max_diff": loop_diff_max,
        },
        "G_M4_g21_saliency_scanpath_3_phases": {
            "pass": g4_pass,
            "frames": saliency_checks,
        },
        "G_M5_rim_interior_text_zero_diff": {
            "pass": g5_pass,
            "interior_max_diff": interior_diff,
        },
        "G_M6_meta_crf28_banding_guard": {
            "pass": g6_pass,
            "crf28_grad_p95": round(p95_step, 2),
        },
    }


def verify_video_ffprobe(mp4_path: Path) -> Dict[str, Any]:
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,r_frame_rate,nb_frames,pix_fmt,codec_name",
        "-of",
        "json",
        str(mp4_path),
    ]
    out = subprocess.check_output(cmd).decode("utf-8")
    data = json.loads(out)
    st = (data.get("streams") or [{}])[0]
    ok = (
        int(st.get("width", 0)) == 1080
        and int(st.get("height", 0)) == 1350
        and st.get("r_frame_rate") == "30/1"
        and int(st.get("nb_frames", 0)) == 180
        and st.get("pix_fmt") == "yuv420p"
    )
    return {"pass": ok, "stream": st}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--kb", default="KB_12", help="Mã kịch bản, mặc định KB_12")
    parser.add_argument(
        "--modes",
        default="V2,V2b,V2c",
        help="Danh sách mode cần render (mặc định: V2,V2b,V2c; hoặc A,B,C,V2,V2b,V2c)",
    )
    args = parser.parse_args()

    kb_id = args.kb.upper()
    kb_lower = kb_id.lower()

    html_path = BATCH_OUT_DIR / f"{kb_lower}_v3_price.html"
    bg_path = DUAL_BG_DIR / f"{kb_lower}_color_bg.jpg"

    if not html_path.exists():
        raise FileNotFoundError(f"Missing HTML overlay: {html_path}")
    if not bg_path.exists():
        raise FileNotFoundError(f"Missing BG image: {bg_path}")

    bg_rgba = Image.open(bg_path).convert("RGBA")
    bg_rgb_u8 = np.array(bg_rgba.convert("RGB"), dtype=np.uint8)
    bulb_engine = build_bulb_breathing_engine(bg_rgb_u8)

    mode_to_filename = {
        "A": f"{kb_lower}_motion_A_lat_ve.mp4",
        "B": f"{kb_lower}_motion_B_net_but.mp4",
        "C": f"{kb_lower}_motion_C_dong_ho.mp4",
        "V2": f"{kb_lower}_motion_V2_lat_ve_rim_den_tho.mp4",
        "V2b": f"{kb_lower}_motion_V2b_dong_ho_den_tho.mp4",
        "V2c": f"{kb_lower}_motion_V2c_cinemagraph_den_tho.mp4",
    }

    req_modes = [m.strip() for m in args.modes.split(",") if m.strip() in mode_to_filename]

    rendered_items = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        page = context.new_page()

        for mode in req_modes:
            fname = mode_to_filename[mode]
            out_mp4 = MOTION_OUT_DIR / fname
            res = render_single_archetype_video(page, html_path, bg_rgba, bulb_engine, mode, out_mp4)
            ver = verify_video_ffprobe(out_mp4)
            res["verifier"] = ver
            rendered_items.append((mode, out_mp4, res))

        browser.close()

    for mode, out_mp4, res in rendered_items:
        if mode.startswith("V2"):
            vf_bbox = tuple(res["gate_info"].get("vf_bbox", [575, 764, 992, 809]))
            res["claude2_6_gates"] = run_claude2_6_gates_verifier(
                out_mp4, html_path, bg_rgb_u8, bulb_engine, vf_bbox
            )
        print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()
