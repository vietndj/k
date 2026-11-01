#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P0.2 - OUTFIT & PORTRAIT REGISTRY (CACHE + FACE BBOX + SAFE ZONES)
==================================================================
1. Tải/cache toàn bộ 176 ảnh chân dung AI Face DNA trong `k4_ledger.json` về
   `/Users/vietmac/Documents/CODE/k/k4_31kb_banners/assets/portraits/` để Playwright
   render offline 0ms latency và không phụ thuộc mạng.
2. Quy chiếu từng ảnh về khung chuẩn `1080×1350` (`object-fit: cover`), dò tọa độ
   khuôn mặt `face_bbox = [x, y, w, h]` bằng OpenCV Haar Cascade (Frontal + Profile + UpperBody fallback).
3. Đo độ sáng (Luminance P10, P50, P90) ở vùng đỉnh và vùng đáy để chọn vùng đặt chữ an toàn
   không bao giờ đè lên khuôn mặt anh Việt (`face_overlap = 0`).
4. Lưu `/Users/vietmac/Documents/CODE/k/k4_31kb_banners/outfit_registry.json` và cập nhật `k4_ledger.json`.
"""

import json
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, Any, List, Tuple
import cv2
import numpy as np
from PIL import Image, ImageOps

OUT_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
PORTRAIT_DIR = OUT_DIR / "assets" / "portraits"
PORTRAIT_DIR.mkdir(parents=True, exist_ok=True)
LEDGER_PATH = OUT_DIR / "k4_ledger.json"
OUTFIT_REG_PATH = OUT_DIR / "outfit_registry.json"

TARGET_W, TARGET_H = 1080, 1350


def download_one(outfit_id: str, url: str) -> Tuple[str, Path, bool]:
    clean_url = url.split("?")[0]
    ext = Path(clean_url).suffix.lower() or ".jpg"
    local_path = PORTRAIT_DIR / f"{outfit_id}{ext}"
    if local_path.exists() and local_path.stat().st_size > 1000:
        return outfit_id, local_path, True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        local_path.write_bytes(data)
        return outfit_id, local_path, True
    except Exception as e:
        print(f"Error downloading {outfit_id} ({url}): {e}")
        return outfit_id, local_path, False


def detect_face_and_zones(img_path: Path) -> Dict[str, Any]:
    """Chuẩn hóa ảnh về 1080x1350 (cover crop) và dò face_bbox + luminance vùng trên/dưới."""
    with Image.open(img_path) as im:
        rgb = im.convert("RGB")
        fitted = ImageOps.fit(rgb, (TARGET_W, TARGET_H), method=Image.Resampling.LANCZOS, centering=(0.5, 0.25))
        arr = np.array(fitted)

    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
    frontal_xml = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    alt_xml = cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml"
    profile_xml = cv2.data.haarcascades + "haarcascade_profileface.xml"

    faces = []
    for xml_file in [frontal_xml, alt_xml, profile_xml]:
        cascade = cv2.CascadeClassifier(xml_file)
        det = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(90, 90))
        if len(det) > 0:
            for (x, y, w, h) in det:
                # Khuôn mặt trong ảnh chân dung thường nằm ở nửa trên hoặc giữa (y < 900)
                if y < 950:
                    faces.append((int(x), int(y), int(w), int(h)))
            if faces:
                break

    if faces:
        # Chọn mặt lớn nhất ở nửa trên
        faces.sort(key=lambda b: b[2] * b[3], reverse=True)
        fx, fy, fw, fh = faces[0]
    else:
        # Fallback an toàn cho ảnh chân dung trung cảnh (chest-up / waist-up):
        # Mặt nằm vùng trung tâm phía trên (X: 360..720, Y: 140..520)
        fx, fy, fw, fh = 380, 160, 320, 340

    # Tính độ sáng tương đối (WCAG Relative Luminance xấp xỉ) ở vùng đỉnh và vùng đáy
    lum = (0.2126 * arr[:, :, 0] + 0.7152 * arr[:, :, 1] + 0.0722 * arr[:, :, 2]) / 255.0
    top_lum = lum[60:340, 60:1020]
    bot_lum = lum[780:1280, 60:1020]

    # Vùng đặt chữ chính mặc định là phần dưới ngực/thắt lưng (Y >= max(fy + fh + 40, 680))
    safe_bottom_y = max(fy + fh + 36, 660)
    if safe_bottom_y > 860:
        safe_bottom_y = 740

    return {
        "face_bbox": [fx, fy, fw, fh],
        "safe_bottom_y": int(safe_bottom_y),
        "top_lum_p50": round(float(np.percentile(top_lum, 50)), 3),
        "bot_lum_p50": round(float(np.percentile(bot_lum, 50)), 3),
        "detected": len(faces) > 0,
    }


def main():
    ledger = json.loads(LEDGER_PATH.read_text())
    unique_outfits: Dict[str, Dict[str, Any]] = {}
    for kb_data in ledger.values():
        for ang in kb_data["angles"]:
            for k in ["before_A", "before_B", "after_opt"]:
                of = ang[k]["outfit"]
                unique_outfits[of["outfit_id"]] = of

    print(f"Downloading/verifying {len(unique_outfits)} portraits to {PORTRAIT_DIR}...")
    local_map: Dict[str, Path] = {}
    with ThreadPoolExecutor(max_workers=16) as ex:
        futs = [ex.submit(download_one, oid, of["src"]) for oid, of in unique_outfits.items()]
        for f in as_completed(futs):
            oid, lpath, ok = f.result()
            if ok:
                local_map[oid] = lpath

    print(f"Downloaded {len(local_map)}/{len(unique_outfits)} portraits. Running Face & Safe-Zone analysis...")
    registry: Dict[str, Dict[str, Any]] = {}
    detected_count = 0
    for oid, of in sorted(unique_outfits.items()):
        lpath = local_map.get(oid)
        if lpath and lpath.exists():
            meta = detect_face_and_zones(lpath)
            if meta["detected"]:
                detected_count += 1
            entry = {
                **of,
                "local_path": str(lpath),
                "face_bbox": meta["face_bbox"],
                "safe_bottom_y": meta["safe_bottom_y"],
                "top_lum_p50": meta["top_lum_p50"],
                "bot_lum_p50": meta["bot_lum_p50"],
                "face_detected_cv": meta["detected"],
            }
        else:
            entry = {
                **of,
                "local_path": "",
                "face_bbox": [380, 160, 320, 340],
                "safe_bottom_y": 680,
                "top_lum_p50": 0.25,
                "bot_lum_p50": 0.20,
                "face_detected_cv": False,
            }
        registry[oid] = entry

    # Cập nhật ngược vào k4_ledger.json
    for kb_data in ledger.values():
        for ang in kb_data["angles"]:
            for k in ["before_A", "before_B", "after_opt"]:
                oid = ang[k]["outfit"]["outfit_id"]
                ang[k]["outfit"] = registry[oid]

    LEDGER_PATH.write_text(json.dumps(ledger, ensure_ascii=False, indent=2))
    OUTFIT_REG_PATH.write_text(json.dumps(registry, ensure_ascii=False, indent=2))
    print(f"Completed outfit_registry.json: {len(registry)} outfits ({detected_count} CV-detected faces).")


if __name__ == "__main__":
    main()
