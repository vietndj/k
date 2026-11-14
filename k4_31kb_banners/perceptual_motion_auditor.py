#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PERCEPTUAL MOTION & LIGHT AUDITOR (Human Vision Reality Check)
==============================================================
Đo lường khách quan vì sao mắt người nhìn vào Live Poster thấy "rõ ràng, thu hút"
hay thấy "lờ mờ, không cảm giác ánh sáng, lấn cấn như ảnh tĩnh".

5 Chỉ Số Thị Giác Thực Tế (Human Perceptual Metrics):
  M1. Thumb-Stop Activity (0.0s -> 0.8s):
      Khi khách lướt Facebook Feed, 0.8s đầu tiên có gì chuyển động đủ để mắt bắt được không?
      - Mục tiêu hiệu quả Ads: >= 0.80% diện tích có chuyển động rõ (>15 mức) trong 0.8s đầu.
  M2. Text & Box Motion Footprint (Biên độ khối thông điệp):
      Diện tích và lực thị giác của pha chuyển động chữ/hộp.
      - Nếu chỉ có 1 dòng chữ nhỏ 22px mờ hiện (< 1.0% diện tích màn hình), mắt thấy "lấn cấn, thiếu dứt khoát".
      - Mục tiêu rõ ràng: >= 2.20% diện tích màn hình tham gia nhịp chuyển (hộp đối chiếu + thanh tiêu điểm + dòng lời giải).
  M3. Peripheral Light Perception (Độ rõ ánh sáng ngoại vi - Weber Velocity):
      Mắt đang đọc chữ ở dưới, vùng ngoại vi chỉ nhận biết được ánh sáng nền khi:
      (a) Diện tích vùng biến đổi rõ (|ΔLuma| >= 18) đạt >= 6.0% diện tích ảnh.
      (b) Độ tương phản tương đối Weber (|ΔI| / I_base) >= 25% trên ít nhất 4.0% diện tích ảnh.
      (c) Tốc độ biến thiên d(Weber)/dt đủ nhanh (>= 12%/giây) hoặc có tia quét không gian (Spatial Sweep / Chiaroscuro).
  M4. Temporal Dead-Zone Ratio (Tỷ lệ thời gian "chết lâm sàng" đứng yên):
      Bao nhiêu % số frames trong 6.0s có tốc độ thay đổi giữa 2 nhịp cách nhau 0.2s (6 frames) gần bằng 0?
      - Nếu > 60% thời lượng video nhìn như đứng đơ -> Người xem tưởng ảnh tĩnh.
      - Mục tiêu: Dead-zone <= 35%.
  M5. Perceptual Clarity Score (Thang 100 điểm cảm nhận mắt người):
      Tổng hợp M1..M4. Yêu cầu đạt >= 75/100 để mắt thường nhìn thấy rõ ràng, có hồn và hiệu quả cho Ads.
"""

import os
import sys
import glob
import json
import cv2
import numpy as np


def audit_video_perceptual(video_path: str) -> dict:
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    frames = []
    while True:
        ret, f = cap.read()
        if not ret:
            break
        frames.append(f)
    cap.release()

    n = len(frames)
    if n < 60:
        return {"error": f"Too few frames: {n}"}

    lumas = [
        (0.114 * f[:, :, 0] + 0.587 * f[:, :, 1] + 0.299 * f[:, :, 2]).astype(np.float32)
        for f in frames
    ]
    f0_bgr = frames[0].astype(np.float32)

    # M1: Thumb-Stop Activity in first 0.8s (frames 0..24)
    first_08s_diffs = [
        np.mean(np.max(np.abs(frames[i].astype(np.float32) - f0_bgr), axis=2) > 15.0) * 100.0
        for i in range(1, min(25, n))
    ]
    m1_max_area_08s = float(max(first_08s_diffs)) if first_08s_diffs else 0.0
    m1_pass = m1_max_area_08s >= 0.80

    # M2: Text & Box Motion Footprint (0.0s .. 2.0s, lower 60% of canvas where text/box lives)
    H, W = lumas[0].shape
    y_text_start = int(H * 0.45)
    f56_bgr = frames[min(56, n - 1)].astype(np.float32)
    text_zone_diff_max = np.zeros((H - y_text_start, W), dtype=np.float32)
    for i in range(0, min(60, n)):
        d = np.max(np.abs(frames[i][y_text_start:, :, :].astype(np.float32) - f56_bgr[y_text_start:, :, :]), axis=2)
        text_zone_diff_max = np.maximum(text_zone_diff_max, d)
    m2_footprint_pct_canvas = float(np.sum(text_zone_diff_max > 18.0) / float(H * W) * 100.0)
    m2_pass = m2_footprint_pct_canvas >= 2.20

    # M3: Peripheral Light Perception (Upper 65% of canvas across entire video)
    y_bg_end = int(H * 0.65)
    bg_stack = np.stack([l[:y_bg_end, :] for l in lumas], axis=0)  # (N, H_bg, W)
    bg_min = np.min(bg_stack, axis=0)
    bg_max = np.max(bg_stack, axis=0)
    bg_range = bg_max - bg_min
    weber_map = bg_range / np.maximum(bg_min, 25.0)

    m3_area_dluma_gt18_pct = float(np.sum(bg_range >= 18.0) / float(H * W) * 100.0)
    m3_area_weber_gt25_pct = float(np.sum(weber_map >= 0.25) / float(H * W) * 100.0)

    # Measure peak velocity over 0.5s window (15 frames) in background
    vel_stack = np.abs(bg_stack[15:] - bg_stack[:-15]) / np.maximum(bg_min[None, :, :], 25.0) * 2.0  # per second
    peak_vel_map = np.max(vel_stack, axis=0)
    m3_area_fast_weber_pct = float(np.sum(peak_vel_map >= 0.15) / float(H * W) * 100.0)
    m3_pass = (m3_area_dluma_gt18_pct >= 6.0) and (m3_area_weber_gt25_pct >= 4.0)

    # M4: Temporal Dead-Zone Ratio (frames where 0.2s window [6 frames] has < 0.25% canvas changing > 8 levels)
    dead_windows = 0
    total_windows = 0
    step = 6  # 0.2s
    for i in range(0, n - step):
        total_windows += 1
        d = np.abs(lumas[i + step] - lumas[i])
        active_pct = float(np.mean(d > 6.0) * 100.0)
        if active_pct < 0.30:
            dead_windows += 1
    m4_dead_time_ratio_pct = round(dead_windows / max(total_windows, 1) * 100.0, 1)
    m4_pass = m4_dead_time_ratio_pct <= 35.0

    # M5: Composite Perceptual Clarity Score (0-100)
    s1 = min(25.0, (m1_max_area_08s / 1.20) * 25.0)
    s2 = min(25.0, (m2_footprint_pct_canvas / 2.50) * 25.0)
    s3 = min(30.0, ((m3_area_dluma_gt18_pct / 8.0) * 15.0 + (m3_area_weber_gt25_pct / 5.0) * 15.0))
    s4 = max(0.0, min(20.0, (1.0 - m4_dead_time_ratio_pct / 80.0) * 20.0))
    m5_score = round(s1 + s2 + s3 + s4, 1)

    verdict = "RÕ RÀNG & THU HÚT" if m5_score >= 75 else ("LẤN CẤN / MỜ NHẠT (GIỐNG ẢNH TĨNH)" if m5_score < 50 else "TRUNG BÌNH (CẦN TĂNG ĐỘ RÕ)")

    return {
        "video": os.path.basename(video_path),
        "M1_thumbstop_08s_area_pct": round(m1_max_area_08s, 2),
        "M1_pass": m1_pass,
        "M2_text_footprint_pct": round(m2_footprint_pct_canvas, 2),
        "M2_pass": m2_pass,
        "M3_light_area_dluma18_pct": round(m3_area_dluma_gt18_pct, 2),
        "M3_light_area_weber25_pct": round(m3_area_weber_gt25_pct, 2),
        "M3_fast_weber_area_pct": round(m3_area_fast_weber_pct, 2),
        "M3_pass": m3_pass,
        "M4_dead_time_ratio_pct": m4_dead_time_ratio_pct,
        "M4_pass": m4_pass,
        "M5_perceptual_score_100": m5_score,
        "verdict": verdict,
    }


def main():
    vids = sorted(glob.glob("/Users/vietmac/Documents/CODE/k/k4_31kb_banners/v2_pilots/motion_out/kb_*_live_v2.mp4"))
    results = [audit_video_perceptual(v) for v in vids]
    out_path = "/Users/vietmac/Documents/CODE/k/k4_31kb_banners/v2_pilots/motion_out/perceptual_audit_report.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
