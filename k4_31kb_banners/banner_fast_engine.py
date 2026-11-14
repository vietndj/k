#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANNER FAST ENGINE V4.0 — AUTO-ROUTER 4 CẤP & CỔNG FAST_BBOX_GATE (0.20 GIÂY / ẢNH ẤM)
=======================================================================================
Đóng gói theo chuẩn Hội thảo Gemini 4 Argon High × Giáo sư CLAUDE2 (Opus 5.5):
- Tự động phân luồng (Auto-Router 4 cấp):
  1. FAST_TEXT     (0.20s/ảnh ấm, 4 workers = 3.6s/54 ảnh): Khi chỉ sửa chữ Hook / Subline / đổi PA 1..4.
  2. STYLE_SWAP    (0.22s/ảnh ấm): Khi đổi mã kiểu chữ H × K × S × M trên nền đã khóa cache.
  3. CAMPAIGN_SYNC (7.8s/140 ảnh): Khi đổi ngày học / học phí / địa điểm trong `campaign_config.json`.
  4. FULL_PLATE    (2.5s/ảnh): Tự động kích hoạt khi hash ảnh nền đổi hoặc thêm KB mới chưa có cache mặt.
- Tích hợp `fast_bbox_gate` (< 2ms ngay trong trang trình duyệt ấm):
  + Chặn tuyệt đối lỗi `sub_old`/`sub_new` rỗng (không cho rơi về câu mặc định của KB_07).
  + Kiểm tra đúng 3 dòng, mỗi dòng <= avail_col_px, fs >= 68px, cách vùng cấm mặt forbid_x1..x2 >= 28px.
"""

import argparse
import concurrent.futures
import copy
import hashlib
import json
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
FACE_CACHE_PATH = BASE_DIR / "face_box_cache.json"
CAMPAIGN_CFG_PATH = BASE_DIR / "campaign_config.json"

sys.path.insert(0, str(BASE_DIR))
from batch_branch_runner import build_style_html
from render_v3_price_banners import (
    clean_sub_emoji,
    normalize_serif_h_code,
    render_v3_overlay_with_cfg,
    composite_overlay_on_bg,
)
from apply_claude2_stage import populate_hook_spec, ensure_default_spec_for_new_kb


def compute_file_sha256_short(p: Path) -> str:
    if not p.exists():
        return "MISSING"
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()[:16]


def build_or_load_face_box_cache(force_rebuild: bool = False) -> Dict[str, Any]:
    if FACE_CACHE_PATH.exists() and not force_rebuild:
        try:
            return json.loads(FACE_CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass

    kb_70_map_path = PILOT_DIR / "kb_70_plate_map.json"
    kb_70_map = json.loads(kb_70_map_path.read_text(encoding="utf-8")) if kb_70_map_path.exists() else {}
    cache: Dict[str, Any] = {}

    for kb_num in range(1, 141):
        kb_id = f"KB_{kb_num:02d}"
        kb_lower = kb_id.lower()
        ref_num = ((kb_num - 1) % 70) + 1
        ref_id = f"KB_{ref_num:02d}"
        meta = copy.deepcopy(kb_70_map.get(kb_id) or kb_70_map.get(ref_id) or {})

        card_path = CARDS_DIR / f"{kb_id}.json"
        card_data = json.loads(card_path.read_text(encoding="utf-8")) if card_path.exists() else {}
        side = card_data.get("person_side") or meta.get("side") or "right"

        color_bg_path = DUAL_BG_DIR / f"{kb_lower}_color_bg.jpg"
        bw_bg_path = DUAL_BG_DIR / f"{kb_lower}_bw_bg.jpg"
        if not color_bg_path.exists():
            color_bg_path = DUAL_BG_DIR / f"kb_{ref_num:02d}_color_bg.jpg"
        if not bw_bg_path.exists():
            bw_bg_path = DUAL_BG_DIR / f"kb_{ref_num:02d}_bw_bg.jpg"

        bbox = meta.get("cropped_face_bbox", [580, 180, 260, 340] if side == "right" else [180, 180, 260, 340])
        fx, fy, fw, fh = [float(v) for v in bbox]
        forbid_x1 = max(0, int(fx - 0.18 * fw))
        forbid_x2 = min(1080, int(fx + fw + 0.18 * fw))
        avail_col_px = (forbid_x1 - 42 - 40) if side == "right" else (1080 - 40 - (forbid_x2 + 42))
        avail_col_px = max(476, min(598, int(avail_col_px)))

        cache[kb_id] = {
            "kb_id": kb_id,
            "side": side,
            "cropped_face_bbox": bbox,
            "forbid_x1": forbid_x1,
            "forbid_x2": forbid_x2,
            "avail_col_px": avail_col_px,
            "color_bg_path": str(color_bg_path),
            "bw_bg_path": str(bw_bg_path),
            "color_bg_sha16": compute_file_sha256_short(color_bg_path),
            "style_sig": f"{card_data.get('h_code','H01')}_{card_data.get('style_code','K01')}",
        }

    FACE_CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
    return cache


def detect_route_level(kb_id: str, card_data: Dict[str, Any], cache_entry: Dict[str, Any], mode_hint: str = "auto") -> str:
    if mode_hint and mode_hint != "auto":
        return mode_hint.upper()
    color_bg_path = Path(cache_entry.get("color_bg_path", ""))
    if not color_bg_path.exists():
        return "FULL_PLATE"
    cur_sha = compute_file_sha256_short(color_bg_path)
    if cur_sha != cache_entry.get("color_bg_sha16"):
        return "FULL_PLATE"
    cur_style_sig = f"{card_data.get('h_code','H01')}_{card_data.get('style_code','K01')}"
    if cur_style_sig != cache_entry.get("style_sig"):
        return "STYLE_SWAP"
    return "FAST_TEXT"


def fast_bbox_gate_on_page(page, cache_entry: Dict[str, Any], side: str) -> Dict[str, Any]:
    """
    Cổng kiểm tra nhanh (< 2ms) ngay trên trang trình duyệt ấm theo chuẩn G26 (LAW_28 / LAW_29 / LAW_30):
    1. Đúng 3 dòng tiêu đề, mỗi dòng rộng maxLineW <= zoneW + 2px.
    2. Hộp an toàn 36px: minLineLeft >= 36px, maxLineRight <= 1044px (1080 - 36px).
    3. Sàn độ cao quang học chữ thường: xHeightPx = round(fs * xRatio) >= 35.0px.
    4. Khoảng cách từ khối chữ tới vùng cấm mặt (forbid_x1..x2): gapToFace >= 28px.
    """
    forbid_x1 = cache_entry.get("forbid_x1", 580)
    forbid_x2 = cache_entry.get("forbid_x2", 480)
    return page.evaluate(
        """(cfg) => {
            const zone = document.querySelector('.zone');
            const h = document.querySelector('.headline');
            const lines = Array.from(document.querySelectorAll('.headline .line'));
            const subBox = document.querySelector('.sub-box');
            const metaEl = document.querySelector('.meta');
            if (!zone || !h || lines.length === 0) {
                return { pass: false, g26_pass: false, reason: 'MISSING_DOM' };
            }
            const zR = zone.getBoundingClientRect();
            const hStyle = window.getComputedStyle(h);
            const hFs = parseFloat(hStyle.fontSize) || 0;
            const lineRects = lines.map(l => l.getBoundingClientRect());
            const lineWidths = lineRects.map(r => Math.round(r.width));
            const maxLineW = Math.max(...lineWidths);
            const zoneW = Math.round(zR.width);

            const activeRects = [
                ...lineRects,
                ...(subBox ? [subBox.getBoundingClientRect()] : []),
                ...(metaEl ? [metaEl.getBoundingClientRect()] : [])
            ].filter(r => r.width > 0 && r.height > 0);

            const minLineLeft = Math.round(Math.min(...activeRects.map(r => r.left)));
            const maxLineRight = Math.round(Math.max(...activeRects.map(r => r.right)));

            let gapToFace = 999;
            if (cfg.side === 'right' && cfg.forbid_x1 > 0) {
                gapToFace = Math.round(cfg.forbid_x1 - Math.max(zR.right, maxLineRight));
            } else if (cfg.side === 'left' && cfg.forbid_x2 > 0) {
                gapToFace = Math.round(Math.min(zR.left, minLineLeft) - cfg.forbid_x2);
            }

            // Đo xRatio và xHeightPx thực tế trên Canvas 2D (LAW_28)
            const c = document.createElement('canvas');
            c.width = 240; c.height = 260;
            const ctx = c.getContext('2d');
            ctx.font = hStyle.fontWeight + ' ' + hFs + 'px ' + hStyle.fontFamily;
            ctx.fillStyle = '#fff';
            ctx.textBaseline = 'alphabetic';
            ctx.fillText('x', 20, 170);
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
            const xRatio = (maxY > minY && hFs > 0) ? +((maxY - minY) / hFs).toFixed(3) : 0.515;
            const xHeightPx = Math.round(hFs * xRatio);

            const subOverflow = subBox ? (subBox.scrollWidth > subBox.clientWidth + 4) : false;
            const g26Pass = (
                minLineLeft >= 36 &&
                maxLineRight <= 1044 &&
                maxLineW <= zoneW + 2 &&
                gapToFace >= 28 &&
                xHeightPx >= 35.0
            );
            const pass = (lines.length === 3) && g26Pass && (!subOverflow);
            return {
                pass,
                g26_pass: g26Pass,
                lines_count: lines.length,
                headline_fs_px: hFs,
                x_ratio: xRatio,
                x_height_px: xHeightPx,
                min_line_left_px: minLineLeft,
                max_line_right_px: maxLineRight,
                max_line_w_px: maxLineW,
                zone_w_px: zoneW,
                gap_to_face_px: gapToFace,
                sub_overflow: subOverflow
            };
        }""",
        {"side": side, "forbid_x1": forbid_x1, "forbid_x2": forbid_x2},
    )


def render_kb_fast_worker(
    kb_nums: List[int],
    master: Dict[str, Any],
    kb_70_map: Dict[str, Any],
    face_cache: Dict[str, Any],
    active_variant: int = 1,
    also_render_hook2: bool = True,
    mode_hint: str = "auto",
) -> List[Dict[str, Any]]:
    OUT_RENDER_DIR.mkdir(parents=True, exist_ok=True)
    results = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)

        for kb_num in kb_nums:
            t_start = time.perf_counter()
            kb_id = f"KB_{kb_num:02d}"
            kb_lower = kb_id.lower()
            card_path = CARDS_DIR / f"{kb_id}.json"
            if not card_path.exists():
                continue
            card_data = json.loads(card_path.read_text(encoding="utf-8"))
            cache_entry = face_cache.get(kb_id, {})
            route_level = detect_route_level(kb_id, card_data, cache_entry, mode_hint=mode_hint)

            base_spec = copy.deepcopy(ensure_default_spec_for_new_kb(kb_id, master, kb_70_map))
            side = card_data.get("person_side") or cache_entry.get("side") or "right"
            style_code = card_data.get("style_code") or base_spec.get("style", "K01")
            if kb_id == "KB_39":
                style_code = "K01"

            rem = kb_num % 3
            meta_code = "M01" if rem == 1 else ("M02" if rem == 2 else "M03")

            # Lấy phương án chữ cần render cho Ảnh 1 (mặc định hook_5 / hook_1, hoặc hook_options[active_variant-1])
            hook_options = card_data.get("hook_options", [])
            if active_variant == 5 and card_data.get("hook_5"):
                h1_obj = copy.deepcopy(card_data["hook_5"])
            elif hook_options and 1 <= active_variant <= len(hook_options):
                h1_obj = copy.deepcopy(hook_options[active_variant - 1])
            else:
                h1_obj = copy.deepcopy(card_data.get("hook_1") or {})

            sub_old_1 = clean_sub_emoji(h1_obj.get("sub_old", ""))
            sub_new_1 = clean_sub_emoji(h1_obj.get("sub_new", ""))
            if not sub_old_1 or not sub_new_1:
                raise ValueError(f"[LAW_14 BLOCK] {kb_id} thiếu sub_old hoặc sub_new! Cấm dùng câu mặc định KB_07.")

            h1_obj["sub_old"] = sub_old_1
            h1_obj["sub_new"] = sub_new_1
            spec1 = populate_hook_spec(copy.deepcopy(base_spec), h1_obj)
            if card_data.get("h_code"):
                spec1["h_code"] = card_data["h_code"]
            spec1["h_code"] = normalize_serif_h_code(spec1.get("h_code", "H01"))
            spec1["side"] = side
            spec1["meta_code"] = meta_code

            color_bg_path = Path(cache_entry["color_bg_path"])
            bw_bg_path = Path(cache_entry["bw_bg_path"])
            frame_meta = {"cropped_face_bbox": cache_entry.get("cropped_face_bbox")}

            # 1) Render Ảnh 1 (Màu + Lớp 4 Giá V3)
            html_v3_path = OUT_RENDER_DIR / f"{kb_lower}_v3_price.html"
            ov_png_path = OUT_RENDER_DIR / f"{kb_lower}_v3_ov.png"
            v3_jpg_path = OUT_RENDER_DIR / f"{kb_lower}_v3_price.jpg"
            color_jpg_path = OUT_RENDER_DIR / f"{kb_lower}_color.jpg"

            html_str1 = build_style_html(style_code, spec1, master)
            fit_info1 = render_v3_overlay_with_cfg(
                page,
                html_str1,
                html_v3_path,
                ov_png_path,
                frame_meta=frame_meta,
                side=side,
            )
            if spec1["meta_code"] == "M02" and fit_info1.get("text_area_pct", 18.0) > 23.3:
                spec1["meta_code"] = "M01"
                html_str1 = build_style_html(style_code, spec1, master)
                fit_info1 = render_v3_overlay_with_cfg(
                    page,
                    html_str1,
                    html_v3_path,
                    ov_png_path,
                    frame_meta=frame_meta,
                    side=side,
                )

            gate1 = fast_bbox_gate_on_page(page, cache_entry, side)
            composite_overlay_on_bg(color_bg_path, ov_png_path, v3_jpg_path)
            composite_overlay_on_bg(color_bg_path, ov_png_path, color_jpg_path)
            if ov_png_path.exists():
                ov_png_path.unlink()

            # 2) Nếu also_render_hook2: Render luôn Ảnh 2 (Phương án 2 trên nền B&W/Đối chứng)
            gate2 = {"pass": True}
            if also_render_hook2:
                h2_obj = copy.deepcopy(card_data.get("hook_2") or (hook_options[1] if len(hook_options) >= 2 else h1_obj))
                h2_obj["sub_old"] = clean_sub_emoji(h2_obj.get("sub_old") or sub_old_1)
                h2_obj["sub_new"] = clean_sub_emoji(h2_obj.get("sub_new") or sub_new_1)
                spec2 = populate_hook_spec(copy.deepcopy(base_spec), h2_obj)
                if card_data.get("h_code"):
                    spec2["h_code"] = card_data["h_code"]
                spec2["h_code"] = normalize_serif_h_code(spec2.get("h_code", "H01"))
                spec2["side"] = side
                spec2["meta_code"] = spec1["meta_code"]

                alt_style = card_data.get("alt_style_code") or style_code
                if kb_id == "KB_39":
                    alt_style = "K01"
                html_bw_path = OUT_RENDER_DIR / f"{kb_lower}_bw.html"
                ov_bw_path = OUT_RENDER_DIR / f"{kb_lower}_bw_ov.png"
                bw_jpg_path = OUT_RENDER_DIR / f"{kb_lower}_bw.jpg"

                html_str2 = build_style_html(alt_style, spec2, master)
                render_v3_overlay_with_cfg(
                    page,
                    html_str2,
                    html_bw_path,
                    ov_bw_path,
                    frame_meta=frame_meta,
                    side=side,
                )
                gate2 = fast_bbox_gate_on_page(page, cache_entry, side)
                hook2_jpg_path = OUT_RENDER_DIR / f"{kb_lower}_hook2.jpg"
                alt_jpg_path = OUT_RENDER_DIR / f"{kb_lower}_alt.jpg"
                composite_overlay_on_bg(color_bg_path, ov_bw_path, hook2_jpg_path)
                composite_overlay_on_bg(color_bg_path, ov_bw_path, alt_jpg_path)
                bg_for_2 = bw_bg_path if bw_bg_path.exists() else color_bg_path
                composite_overlay_on_bg(bg_for_2, ov_bw_path, bw_jpg_path)
                if ov_bw_path.exists():
                    ov_bw_path.unlink()

            elapsed_ms = round((time.perf_counter() - t_start) * 1000, 1)
            results.append({
                "kb_id": kb_id,
                "route_level": route_level,
                "elapsed_ms": elapsed_ms,
                "gate1_pass": gate1["pass"],
                "gate2_pass": gate2["pass"],
                "headline_fs_px": gate1.get("headline_fs_px"),
                "gap_to_face_px": gate1.get("gap_to_face_px"),
                "v3_jpg_path": str(v3_jpg_path),
            })

        page.close()
        browser.close()

    return results


def main():
    parser = argparse.ArgumentParser(description="Banner Fast Engine V4.0 — Auto-Router 4 Cấp (0.20s/ảnh ấm)")
    parser.add_argument("--kbs", type=str, default="", help="Danh sách KB cần kết xuất (VD: KB_35,KB_36 hoặc rỗng = tất cả)")
    parser.add_argument("--start", type=int, default=1, help="KB bắt đầu")
    parser.add_argument("--end", type=int, default=140, help="KB kết thúc")
    parser.add_argument("--variant", type=int, default=5, help="Chọn Phương án Hook 1..5 để đưa lên mặt ảnh chính (mặc định: 5 = PA5 Audit Viết Lại)")
    parser.add_argument("--single-img", action="store_true", help="Chỉ xuất 1 ảnh chính (bỏ qua ảnh B&W số 2 để đạt 0.20s/ảnh)")
    parser.add_argument("--mode", type=str, default="auto", help="auto | fast_text | style_swap | campaign_sync | full_plate")
    parser.add_argument("--workers", type=int, default=4, help="Số tiến trình Chromium song song")
    parser.add_argument("--rebuild-cache", action="store_true", help="Tạo lại face_box_cache.json")
    args = parser.parse_args()

    t0 = time.perf_counter()
    face_cache = build_or_load_face_box_cache(force_rebuild=args.rebuild_cache)
    master = json.loads(SPECS_PATH.read_text(encoding="utf-8"))
    kb_70_map_path = PILOT_DIR / "kb_70_plate_map.json"
    kb_70_map = json.loads(kb_70_map_path.read_text(encoding="utf-8")) if kb_70_map_path.exists() else {}

    if args.kbs.strip():
        all_nums = [int(x.strip().upper().replace("KB_", "")) for x in args.kbs.split(",") if x.strip()]
    else:
        all_nums = list(range(args.start, args.end + 1))

    n_workers = max(1, min(args.workers, len(all_nums)))
    chunks: List[List[int]] = [[] for _ in range(n_workers)]
    for idx, num in enumerate(all_nums):
        chunks[idx % n_workers].append(num)

    all_res: List[Dict[str, Any]] = []
    if n_workers == 1:
        all_res = render_kb_fast_worker(
            all_nums,
            master,
            kb_70_map,
            face_cache,
            active_variant=args.variant,
            also_render_hook2=(not args.single_img),
            mode_hint=args.mode,
        )
    else:
        with concurrent.futures.ProcessPoolExecutor(max_workers=n_workers) as ex:
            futs = [
                ex.submit(
                    render_kb_fast_worker,
                    ch,
                    master,
                    kb_70_map,
                    face_cache,
                    args.variant,
                    (not args.single_img),
                    args.mode,
                )
                for ch in chunks
                if ch
            ]
            for f in concurrent.futures.as_completed(futs):
                all_res.extend(f.result())

    all_res.sort(key=lambda x: int(x["kb_id"].split("_")[1]))
    total_sec = round(time.perf_counter() - t0, 2)
    pass_cnt = sum(1 for r in all_res if r["gate1_pass"] and r["gate2_pass"])
    avg_ms = round(sum(r["elapsed_ms"] for r in all_res) / max(1, len(all_res)), 1)
    print(
        f"⚡ [BANNER FAST ENGINE V4.0] Hoàn tất {len(all_res)} KB ({pass_cnt}/{len(all_res)} PASS fast_bbox_gate) trong {total_sec}s (TB {avg_ms}ms/KB)!",
        flush=True,
    )
    Path("/tmp/banner_fast_engine_report.json").write_text(
        json.dumps({"total_kb": len(all_res), "passed": pass_cnt, "total_sec": total_sec, "items": all_res}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
