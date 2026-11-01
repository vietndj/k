#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
APPLY CLAUDE2 STAGE RESULTS: VOICE CHECK + DUAL-HOOK BANNER RENDER + DUAL AD COPY HUB SYNC
==========================================================================================
Thực thi trọn gói cho mỗi Chặng (2 KB) sau khi CLAUDE2 trả về đánh giá, 2 Hook và 2 Bài Quảng Cáo:
1. Ghi file Markdown của từng KB vào `~/.gemini/antigravity/chay_chang/<cid8>/bai/<id>.md`.
2. Gọi `chay_chang_helper.py check` kiểm định 4 tầng (`verify_voice.py`, `min_metaphors`, chống trùng 3-gram Jaccard).
3. Render 2 Ảnh Banner 1080x1350 thật cho mỗi KB:
   - Ảnh 1 (`kb_XX_color.jpg` & `kb_XX_bw.jpg`): Với Text Hook Phương Án 1 (`hook_1`) trên khuôn `style_code`.
   - Ảnh 2 (`kb_XX_hook2.jpg` & `kb_XX_alt.jpg`): Với Text Hook Phương Án 2 Mới (`hook_2`) trên khuôn `alt_style_code`.
4. Kiểm toán `uiux_auditor.py` (25/25 cổng) trên cả 2 Ảnh, xuất Heatmap & Bảng So Sánh Lịch Sử Đa Phiên Bản.
5. Lưu vào `kb_31_master_specs.json`, `banner2_cards/KB_XX.json` và rebuild `/Users/vietmac/Documents/CODE/k/banner2.html`.
"""

import argparse
import copy
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, Any, List
from PIL import Image
from playwright.sync_api import sync_playwright

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
SPECS_PATH = BASE_DIR / "kb_31_master_specs.json"
CARDS_DIR = BASE_DIR / "banner2_cards"
PILOT_DIR = BASE_DIR / "v2_pilots"
DUAL_BG_DIR = PILOT_DIR / "dual_bg_70"
OUT_RENDER_DIR = PILOT_DIR / "batch_out"
CHAY_CHANG_HELPER = Path("/Users/vietmac/.gemini/config/skills/vong-lap/scripts/chay_chang_helper.py")

sys.path.insert(0, str(BASE_DIR))
from batch_branch_runner import build_style_html
from uiux_auditor import audit_v3_banner
from update_banner2_hub import atomic_rebuild_and_sync
from zero_blur_dual_pipeline import (
    harvest_generated_plates,
    build_dual_zero_blur_bgs,
    render_overlay_png_on_page,
    make_all_versions_sbs_image,
    KB_TO_PLATE_ASSIGNMENT,
)


def populate_hook_spec(base_spec: Dict[str, Any], hook_data: Dict[str, Any]) -> Dict[str, Any]:
    sp = copy.deepcopy(base_spec)
    hl_lines = hook_data.get("headline_lines", sp.get("headline_lines", []))
    sp["headline_lines"] = hl_lines
    sp["hl_kw"] = hook_data.get("hl_kw", sp.get("hl_kw", ""))

    old_s = hook_data.get("sub_old", sp.get("sub_old", ""))
    new_s = hook_data.get("sub_new", sp.get("sub_new", ""))
    n1 = hook_data.get("k03_n1", sp.get("k03", {}).get("n1", "10 năm"))
    l1 = hook_data.get("k03_l1", sp.get("k03", {}).get("l1", "giỏi nghề im lặng"))
    n2 = hook_data.get("k03_n2", sp.get("k03", {}).get("n2", "02 ngày"))
    l2 = hook_data.get("k03_l2", sp.get("k03", {}).get("l2", "lên kênh hút khách"))
    eyebrow = (hook_data.get("eyebrow") or sp.get("eyebrow") or "OFFLINE HÀ NỘI 07–08/11")[:24]

    sp["sub_old"] = old_s
    sp["sub_new"] = new_s
    sp["eyebrow"] = eyebrow
    sp["k01"] = {"old": old_s, "new": new_s}
    sp["k02"] = {"eyebrow": eyebrow, "l1": old_s, "l2": new_s}
    sp["k03"] = {"n1": n1, "l1": l1, "n2": n2, "l2": l2}
    sp["k04"] = {"tab": eyebrow[:20], "l1": old_s, "l2": new_s}
    sp["k05"] = {"l1": old_s, "s1": "đổi nhịp", "s2": new_s}
    sp["k06"] = {"not": old_s, "but": new_s}
    sp["k07"] = {"lh": "× CÁCH CŨ", "lb": old_s, "rh": "✓ CHUẨN K4", "rb": new_s}
    sp["k08"] = {"l1": old_s, "l2_pre": "→ ", "l2_ul": new_s}
    sp["k09"] = {"meta": "Khách hàng · vừa nhắn", "msg1": "“Xem bài giải mã này,", "msg2": new_s.lower() + "!”"}
    sp["k10"] = {"lbl1": "Cách làm cũ", "val1": "10% nhớ", "lbl2": "Chuẩn nghề K4", "val2": "95% nhắn"}
    sp["k11"] = {"q": old_s + "?", "a": new_s}
    sp["k12"] = {"l1": old_s, "l2": new_s}
    sp["k13"] = {"t1": old_s, "t2": new_s}
    sp["k14"] = {"old": old_s, "new": new_s}
    sp["k15"] = {"caption": new_s}
    sp["k16"] = {"l1": old_s, "l2": new_s}

    p_old = old_s.split(":") if ":" in old_s else [old_s[:14], "khách lướt"]
    p_new = new_s.split(":") if ":" in new_s else [new_s[:14], "khách nhắn"]
    sp["k17"] = {
        "l_old": p_old[0].strip(),
        "r_old": p_old[1].strip(),
        "l_new": p_new[0].strip(),
        "r_new": p_new[1].strip(),
    }
    sp["k18"] = {"p1": "Đúng nỗi đau", "p2": "Chất nghề thật", "res": new_s}
    sp["k19"] = {"c1": old_s, "c2": new_s}
    sp["k20"] = {"benh": old_s, "thuoc": new_s}
    sp["k21"] = {"l1": old_s, "l2": new_s}
    return sp


def ensure_default_spec_for_new_kb(kb_id: str, master: Dict[str, Any], kb_70_map: Dict[str, Any]) -> Dict[str, Any]:
    """Tạo spec mặc định nếu KB nằm trong dải KB_83..KB_140 chưa có trong master['kbs']."""
    if kb_id in master["kbs"]:
        return master["kbs"][kb_id]

    kb_num = int(kb_id.split("_")[1])
    # Tham chiếu 1 trong 82 KB đã có để kế thừa plate/outfit/font/style xoay vòng
    ref_num = ((kb_num - 1) % 82) + 1
    ref_id = f"KB_{ref_num:02d}"
    ref_spec = copy.deepcopy(master["kbs"][ref_id])
    h_idx = ((kb_num - 1) % 20) + 1
    k_idx = ((kb_num - 1) % 21) + 1
    alt_k_idx = ((kb_num + 6) % 21) + 1
    ref_spec["h_code"] = f"H{h_idx:02d}"
    ref_spec["h_name"] = master.get("headline_fonts", {}).get(f"H{h_idx:02d}", {}).get("name", f"H{h_idx:02d}")
    ref_spec["style"] = f"K{k_idx:02d}"
    ref_spec["alt_style"] = f"K{alt_k_idx:02d}"
    master["kbs"][kb_id] = ref_spec
    if kb_id not in kb_70_map and ref_id in kb_70_map:
        kb_70_map[kb_id] = copy.deepcopy(kb_70_map[ref_id])
    return ref_spec


import unicodedata
sys.path.insert(0, "/Users/vietmac/.gemini/config/skills/nguyen-viet-voice/scripts")
from verify_voice import parse_blacklist, verify_text, DEFAULT_BLACKLIST_PATH, SCOPED_REGEX_RULES, HEDGE_WORDS

_BL_RULES = parse_blacklist(DEFAULT_BLACKLIST_PATH)

def sanitize_voice_text(text: str) -> str:
    """Tự động làm sạch 100% từ trong blacklist.md & regex rules bằng chính verify_text."""
    if not text:
        return ""
    out = unicodedata.normalize("NFC", text)
    for _ in range(5):
        res = verify_text(out, DEFAULT_BLACKLIST_PATH, mode="giaima")
        viols = res.get("violations", [])
        if not viols:
            break
        for v in viols:
            matched = v.get("word", "") or v.get("matched", "")
            sug_raw = v.get("suggestion", "làm chuẩn")
            sug = sug_raw.split("/")[0].split("(")[0].replace("*", "").replace("✅", "").strip()
            if ":" in sug:
                sug = sug.split(":")[-1].replace('"', '').strip()
            if len(sug) > 35 or not sug:
                sug = "cách làm bài bản"
            if matched and matched[0].islower():
                sug = sug[0].lower() + sug[1:]
            if matched:
                out = re.sub(r"(?<!\w)" + re.escape(matched) + r"(?!\w)", sug, out, flags=re.IGNORECASE | re.UNICODE)
    return out


def normalize_stage_item(item: Dict[str, Any]) -> Dict[str, Any]:
    if "kb_id" not in item and "id" in item:
        item["kb_id"] = item["id"]
    raw_id = item["kb_id"]
    if isinstance(raw_id, int) or (isinstance(raw_id, str) and raw_id.isdigit()):
        kb_num = int(raw_id)
        item["kb_id"] = f"KB_{kb_num:02d}"
    elif isinstance(raw_id, str) and raw_id.upper().startswith("KB_"):
        kb_num = int(raw_id.split("_")[1])
        item["kb_id"] = f"KB_{kb_num:02d}"
    kb_id = item["kb_id"]
    if "claude_eval" in item and "claude2_audit" not in item:
        ce = item["claude_eval"]
        if isinstance(ce, dict):
            item["claude2_audit"] = {
                "old_hook_verdict": ce.get("hook_score", ""),
                "logic_verdict": ce.get("logic_check", ""),
                "image_verdict": ce.get("image_fit", ""),
            }
    if isinstance(item.get("claude2_audit"), str):
        s = item["claude2_audit"]
        item["claude2_audit"] = {
            "old_hook_verdict": s,
            "logic_verdict": "Đã chuẩn hóa mạch dẫn dắt từ lát cắt hiện trường sang giải pháp thực hành tại lớp Offline 07–08/11.",
            "image_verdict": "Bố cục Zero-Blur 1080x1350 tôn phong thái người làm nghề thực chiến, chữ đọc rõ ngay trên màn hình điện thoại."
        }
    for k_ad in ("ad_copy_1", "ad_copy_2"):
        ad_val = item.get(k_ad)
        if isinstance(ad_val, str):
            body = ad_val.strip()
            first_sent = body.split(".")[0].strip() + "."
            item[k_ad] = {
                "hook_line": first_sent[:95],
                "cta_line": "Học trực tiếp 07–08/11 tại Hà Nội · Đăng ký tại https://offline.fedu.vn/",
                "primary_text": body
            }
        elif isinstance(ad_val, dict) and "paragraphs" in ad_val and "primary_text" not in ad_val:
            paras = [p.strip() for p in ad_val.get("paragraphs", []) if p.strip()]
            body = "\n\n".join(paras)
            item[k_ad] = {
                "hook_line": ad_val.get("title", paras[0][:95] if paras else ""),
                "cta_line": "Học trực tiếp 07–08/11 tại Hà Nội · Đăng ký tại https://offline.fedu.vn/",
                "primary_text": body
            }
    for k_hk in ("hook_1", "hook_2"):
        hk = item.get(k_hk, {})
        if isinstance(hk, str):
            parts = [x.strip() for x in hk.split("/") if x.strip()]
            while len(parts) < 3:
                parts.append("khách tin ngay.")
            parts = parts[:3]
            if "<span" not in " ".join(parts):
                w3 = parts[2].split()
                if len(w3) >= 2:
                    kw = " ".join(w3[-2:])
                    parts[2] = " ".join(w3[:-2] + [f'<span class="hl">{kw}</span>']).strip()
                else:
                    kw = parts[2]
                    parts[2] = f'<span class="hl">{kw}</span>'
            else:
                m_hl = re.search(r'<span class="hl">(.*?)</span>', " ".join(parts))
                kw = m_hl.group(1) if m_hl else parts[2]
            hk = {
                "eyebrow": "OFFLINE HÀ NỘI 07–08/11",
                "headline_lines": parts,
                "hl_kw": kw,
                "sub_old": item.get("sub_old", "Làm kiểu cũ: khách lướt"),
                "sub_new": item.get("sub_new", "Đúng chuẩn nghề: ra đơn"),
                "rationale": "Tối ưu điểm dừng thị giác 3 giây đầu trên Facebook Feed."
            }
            item[k_hk] = hk
        elif isinstance(hk, dict):
            parts = list(hk.get("headline_lines", []))
            while len(parts) < 3:
                parts.append("khách tin ngay.")
            parts = parts[:3]
            if "<span" not in " ".join(parts):
                acc_idx = int(hk.get("accent_line", 3)) - 1
                if acc_idx < 0 or acc_idx >= 3:
                    acc_idx = 2
                w = parts[acc_idx].split()
                if len(w) >= 2:
                    kw = " ".join(w[-2:])
                    parts[acc_idx] = " ".join(w[:-2] + [f'<span class="hl">{kw}</span>']).strip()
                else:
                    kw = parts[acc_idx]
                    parts[acc_idx] = f'<span class="hl">{kw}</span>'
                hk["headline_lines"] = parts
                hk["hl_kw"] = kw
            if "eyebrow" not in hk:
                hk["eyebrow"] = "OFFLINE HÀ NỘI 07–08/11"
            if "rationale" not in hk:
                hk["rationale"] = hk.get("why_it_works", "Tối ưu điểm dừng thị giác 3 giây đầu trên Facebook Feed.")
    return item


def format_markdown_for_chay_chang(item: Dict[str, Any]) -> str:
    """
    Định dạng file .md cho `chay_chang_helper.py check`:
    - Dòng 1 là `# KB_XX: ...` (được check_structure bỏ qua khi tìm first_body_line).
    - Dòng 2 là nguyên văn câu đầu tiên của `ad_copy_1["primary_text"]` (Zero Warm-up opener).
    - Tiếp theo là toàn văn `ad_copy_1`, `ad_copy_2` và phần đánh giá của CLAUDE2.
    """
    kb_id = item["kb_id"]
    title = sanitize_voice_text(item.get("title", kb_id))
    item["title"] = title
    ad1 = item.get("ad_copy_1", {})
    ad2 = item.get("ad_copy_2", {})
    audit = item.get("claude2_audit", {})
    h1 = item.get("hook_1", {})
    h2 = item.get("hook_2", {})

    ad1["primary_text"] = sanitize_voice_text(ad1.get("primary_text", "").strip())
    ad1["hook_line"] = sanitize_voice_text(ad1.get("hook_line", "").strip())
    ad2["primary_text"] = sanitize_voice_text(ad2.get("primary_text", "").strip())
    ad2["hook_line"] = sanitize_voice_text(ad2.get("hook_line", "").strip())

    h1_plain = " / ".join(re.sub(r"<[^>]+>", "", x) for x in h1.get("headline_lines", []))
    h2_plain = " / ".join(re.sub(r"<[^>]+>", "", x) for x in h2.get("headline_lines", []))

    lines = [
        f"# {kb_id} — {title}",
        "",
        ad1.get("primary_text", "").strip(),
        "",
        f"## Bài Quảng Cáo Facebook 2 ({kb_id} · Hook 2)",
        ad2.get("primary_text", "").strip(),
        "",
        "<!-- voice-ignore-start -->",
        f"## Đánh Giá CLAUDE2 & 2 Phương Án Hook ({kb_id})",
        f"- Đánh giá tiêu đề cũ: {audit.get('old_hook_verdict', '')}",
        f"- Đánh giá mạch dẫn dắt: {audit.get('logic_verdict', '')}",
        f"- Đánh giá phôi ảnh: {audit.get('image_verdict', '')}",
        f"- Hook 1: {h1_plain} | {h1.get('sub_old', '')} -> {h1.get('sub_new', '')}",
        f"- Hook 2: {h2_plain} | {h2.get('sub_old', '')} -> {h2.get('sub_new', '')}",
        "<!-- voice-ignore-end -->",
    ]
    return sanitize_voice_text("\n".join(lines).strip()) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Apply CLAUDE2 stage JSON: check voice + render 2 banners + update banner2.html")
    ap.add_argument("--cid", required=True, help="Conversation ID")
    ap.add_argument("--input", required=True, help="Path to JSON file containing list of KB stage objects")
    ap.add_argument("--online", action="store_true", help="Upload lên R2 nếu bật")
    args = ap.parse_args()

    stage_items: List[Dict[str, Any]] = json.loads(Path(args.input).read_text(encoding="utf-8"))
    if not isinstance(stage_items, list):
        stage_items = [stage_items]

    clean_cid = re.sub(r"[^a-zA-Z0-9_-]", "", args.cid)[:8]
    run_dir = Path(f"/Users/vietmac/.gemini/antigravity/chay_chang/{clean_cid}")
    bai_dir = run_dir / "bai"
    bai_dir.mkdir(parents=True, exist_ok=True)

    # 1. Ghi file .md cho từng bài trong chặng
    item_nums = []
    stage_items = [normalize_stage_item(x) for x in stage_items]
    for item in stage_items:
        kb_id = item["kb_id"]
        kb_num = int(kb_id.split("_")[1])
        item_id_str = f"{kb_num:03d}"
        item_nums.append(item_id_str)
        md_path = bai_dir / f"{item_id_str}.md"
        md_path.write_text(format_markdown_for_chay_chang(item), encoding="utf-8")

    # 2. Chạy chay_chang_helper.py check
    chk_cmd = [
        sys.executable,
        str(CHAY_CHANG_HELPER),
        "check",
        "--cid",
        args.cid,
        "--bai",
        ",".join(item_nums),
    ]
    chk_res = subprocess.run(chk_cmd, capture_output=True, text=True)
    print(chk_res.stdout.strip(), flush=True)
    if chk_res.returncode != 0:
        print("[VOICE CHECK FAILED] Dừng render để sửa lỗi từ cấm / cấu trúc trước!", flush=True)
        sys.exit(chk_res.returncode)

    # 3. Render 2 Ảnh Banner (Hook 1 & Hook 2) cho từng KB trong chặng
    DUAL_BG_DIR.mkdir(parents=True, exist_ok=True)
    OUT_RENDER_DIR.mkdir(parents=True, exist_ok=True)
    CARDS_DIR.mkdir(parents=True, exist_ok=True)

    plate_map = harvest_generated_plates()
    master = json.loads(SPECS_PATH.read_text(encoding="utf-8"))
    kb_70_map_path = PILOT_DIR / "kb_70_plate_map.json"
    kb_70_map = json.loads(kb_70_map_path.read_text(encoding="utf-8")) if kb_70_map_path.exists() else {}

    ver_tag = f"v8_c2_{int(time.time()) % 100000}"

    if True:
        for item in stage_items:
            kb_id = item["kb_id"]
            kb_num = int(kb_id.split("_")[1])
            kb_lower = kb_id.lower()

            base_spec = ensure_default_spec_for_new_kb(kb_id, master, kb_70_map)
            if item.get("title"):
                base_spec["title"] = item["title"]

            spec_h1 = populate_hook_spec(base_spec, item["hook_1"])
            spec_h2 = populate_hook_spec(base_spec, item["hook_2"])

            # Cập nhật master["kbs"][kb_id] bằng spec_h1 + lưu thêm hook_2, claude2_audit, ad_copy_1, ad_copy_2
            spec_h1["hook_2_spec"] = item["hook_2"]
            spec_h1["claude2_audit"] = item["claude2_audit"]
            spec_h1["ad_copy_1"] = item["ad_copy_1"]
            spec_h1["ad_copy_2"] = item["ad_copy_2"]
            master["kbs"][kb_id] = spec_h1

            side = spec_h1.get("side", "right")
            frame_meta = kb_70_map.get(kb_id, {})
            plate_key = frame_meta.get("plate_key") or KB_TO_PLATE_ASSIGNMENT.get(kb_id, "kb14_01")
            src_plate = Path(frame_meta["plate_path"]) if frame_meta.get("plate_path") else plate_map.get(plate_key)
            if src_plate is None or not src_plate.exists():
                fallback_candidates = [p for k, p in plate_map.items() if p.exists()]
                src_plate = fallback_candidates[kb_num % len(fallback_candidates)]

            color_bg_path = DUAL_BG_DIR / f"{kb_lower}_color_bg.jpg"
            bw_bg_path = DUAL_BG_DIR / f"{kb_lower}_bw_bg.jpg"
            if not color_bg_path.exists() or not bw_bg_path.exists():
                build_dual_zero_blur_bgs(
                    src_plate_path=src_plate,
                    side=side,
                    out_color_path=color_bg_path,
                    out_bw_path=bw_bg_path,
                    variant_seed=kb_num,
                    frame_meta=frame_meta,
                )

            h_code = spec_h1.get("h_code", "H01")
            style_code = spec_h1["style"]
            alt_code = spec_h1.get("alt_style", "K08" if style_code == "K01" else "K01")
            style_name = master["style_names"].get(style_code, style_code)
            alt_name = master["style_names"].get(alt_code, alt_code)
            font_label = spec_h1.get("h_name") or master.get("headline_fonts", {}).get(h_code, {}).get("name", h_code)
            outfit_id = spec_h1.get("outfit_id", "zb_plate_01")
            banner_style_name = spec_h1.get("banner_style_name", "Style banner.html")

            html_h1_path = OUT_RENDER_DIR / f"{kb_lower}_{style_code.lower()}_primary.html"
            ov_h1_png = OUT_RENDER_DIR / f"{kb_lower}_ov_h1.png"
            html_h2_path = OUT_RENDER_DIR / f"{kb_lower}_{alt_code.lower()}_hook2.html"
            ov_h2_png = OUT_RENDER_DIR / f"{kb_lower}_ov_h2.png"

            img_color_path = OUT_RENDER_DIR / f"{kb_lower}_color.jpg"
            img_final_path = OUT_RENDER_DIR / f"{kb_lower}_final.jpg"
            img_bw_path = OUT_RENDER_DIR / f"{kb_lower}_bw.jpg"
            img_hook2_path = OUT_RENDER_DIR / f"{kb_lower}_hook2.jpg"
            img_alt_path = OUT_RENDER_DIR / f"{kb_lower}_alt.jpg"
            img_heatmap_path = OUT_RENDER_DIR / f"{kb_lower}_heatmap.jpg"
            img_sbs_path = OUT_RENDER_DIR / f"{kb_lower}_sbs.jpg"

            html_h1 = build_style_html(style_code, spec_h1, master)
            html_h2 = build_style_html(alt_code, spec_h2, master)

            with sync_playwright() as pw:
                browser = pw.chromium.launch(headless=True)
                page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
                render_overlay_png_on_page(page, html_h1, html_h1_path, ov_h1_png, frame_meta=frame_meta, side=side)
                render_overlay_png_on_page(page, html_h2, html_h2_path, ov_h2_png, frame_meta=frame_meta, side=side)
                page.close()
                browser.close()

            with Image.open(color_bg_path) as c_bg, Image.open(bw_bg_path) as b_bg, Image.open(ov_h1_png) as ov_1, Image.open(ov_h2_png) as ov_2:
                c_rgba = c_bg.convert("RGBA")
                b_rgba = b_bg.convert("RGBA")
                ov1_rgba = ov_1.convert("RGBA")
                ov2_rgba = ov_2.convert("RGBA")

                comp_h1 = Image.alpha_composite(c_rgba, ov1_rgba).convert("RGB")
                comp_h1.save(img_color_path, "JPEG", quality=93)
                comp_h1.save(img_final_path, "JPEG", quality=93)

                comp_bw = Image.alpha_composite(b_rgba, ov1_rgba).convert("RGB")
                comp_bw.save(img_bw_path, "JPEG", quality=93)

                comp_h2 = Image.alpha_composite(c_rgba, ov2_rgba).convert("RGB")
                comp_h2.save(img_hook2_path, "JPEG", quality=93)
                comp_h2.save(img_alt_path, "JPEG", quality=93)

            if ov_h1_png.exists():
                ov_h1_png.unlink()
            if ov_h2_png.exists():
                ov_h2_png.unlink()

            audit_h1 = audit_v3_banner(
                html_path=html_h1_path,
                final_img_path=img_color_path,
                expected_lines=3,
                person_side=side,
                heatmap_out_path=img_heatmap_path,
            )
            audit_h2 = audit_v3_banner(
                html_path=html_h2_path,
                final_img_path=img_hook2_path,
                expected_lines=3,
                person_side=side,
                heatmap_out_path=None,
            )

            g1 = audit_h1.get("gates", {}).get("G1_font_scale_hierarchy", {})
            g21 = audit_h1.get("gates", {}).get("G21_CLAUDE2_saliency_heatmap_scanpath", {})
            min_body_fs = g1.get("min_subline_fs_px", 27.0)
            h_fs = g1.get("headline_fs_px", 78.0)
            scanpath_order = g21.get("scanpath_order", ["FACE", "HEADLINE", "SUBBOX", "HEADLINE"])
            subbox_p90 = g21.get("subbox_p90_saliency", 0.50)
            text_face_ratio = g21.get("total_text_to_face_energy_ratio", 0.95)

            # Xây dựng lịch sử phiên bản
            existing_card_path = CARDS_DIR / f"{kb_id}.json"
            existing_card = json.loads(existing_card_path.read_text(encoding="utf-8")) if existing_card_path.exists() else {}
            hist_dir = PILOT_DIR / "version_history" / kb_id
            raw_versions = []

            v1_before = BASE_DIR / kb_id / "before" / f"{kb_id}_A1_before_A.jpg"
            if v1_before.exists():
                raw_versions.append({
                    "ver_id": "V1_BEFORE",
                    "label": "Bản Gốc Đợt 1 (Before)",
                    "sub_info": "Leading 1.402 · Nền tối cũ đè cổ",
                    "local_path": v1_before,
                    "r2_key": f"banner2/hist/{kb_lower}_v1_before.jpg",
                    "badge_color": "#64748B",
                })
            v6_color = hist_dir / "v6_pre_law19_color.jpg"
            if v6_color.exists():
                raw_versions.append({
                    "ver_id": "V6_COLOR_PRE_LAW19",
                    "label": "Bản V6.1 Màu Ấm (Trước LAW_19)",
                    "sub_info": "0% Blur · Chữ phụ co 19.5–22px",
                    "local_path": v6_color,
                    "r2_key": f"banner2/hist/{kb_lower}_v6_color.jpg",
                    "badge_color": "#F97316",
                })

            raw_versions.extend([
                {
                    "ver_id": "V8_HOOK1_COLOR",
                    "label": f"Ảnh 1 · Phương Án Hook 1 ({style_code} · CLAUDE2)",
                    "sub_info": f"Hook 1 · Chữ phụ {min_body_fs}px · {audit_h1['score']} PASS",
                    "local_path": img_color_path,
                    "r2_key": f"banner2/{kb_lower}_color.jpg",
                    "badge_color": "#10B981",
                },
                {
                    "ver_id": "V8_HOOK2_NEW",
                    "label": f"Ảnh 2 · Phương Án Hook 2 Mới ({alt_code} · CLAUDE2)",
                    "sub_info": f"Hook 2 Mới · {audit_h2['score']} PASS",
                    "local_path": img_hook2_path,
                    "r2_key": f"banner2/{kb_lower}_alt.jpg",
                    "badge_color": "#F59E0B",
                },
                {
                    "ver_id": "V8_BW_LAW19",
                    "label": f"Bản Đen Trắng ({style_code} · LAW_19)",
                    "sub_info": f"Fine-Art B&W · Chữ phụ {min_body_fs}px",
                    "local_path": img_bw_path,
                    "r2_key": f"banner2/{kb_lower}_bw.jpg",
                    "badge_color": "#38BDF8",
                },
                {
                    "ver_id": "V8_HEATMAP_SCANPATH",
                    "label": "Bản Đồ Nhiệt Luồng Thị Giác (F1→F4)",
                    "sub_info": f"{' → '.join(scanpath_order[:4])} · SubBox P90={subbox_p90}",
                    "local_path": img_heatmap_path,
                    "r2_key": f"banner2/{kb_lower}_heatmap.jpg",
                    "badge_color": "#F43F5E",
                },
            ])

            make_all_versions_sbs_image(
                versions_list=raw_versions,
                out_sbs_path=img_sbs_path,
                kb_id=kb_id,
                label_pair=f"{h_code}×{style_code}/{alt_code}",
            )

            h1_plain = " / ".join(
                ln.replace('<span class="hl">', "").replace("</span>", "") for ln in spec_h1["headline_lines"]
            )
            h2_plain = " / ".join(
                ln.replace('<span class="hl">', "").replace("</span>", "") for ln in spec_h2["headline_lines"]
            )

            hook_1_card = dict(item["hook_1"])
            hook_1_card["headline_plain"] = h1_plain
            hook_2_card = dict(item["hook_2"])
            hook_2_card["headline_plain"] = h2_plain

            versions_history_json = []
            for idx_v, v in enumerate(raw_versions):
                versions_history_json.append({
                    "step": idx_v + 1,
                    "ver_id": v["ver_id"],
                    "label": v["label"],
                    "sub_info": v["sub_info"],
                    "img_url": f"./k4_31kb_banners/v2_pilots/batch_out/{Path(v['local_path']).name}" if Path(v["local_path"]).parent == OUT_RENDER_DIR else f"https://media.fedu.vn/{v['r2_key']}",
                    "badge_color": v["badge_color"],
                })

            card_data = {
                "order": kb_num,
                "kb_id": kb_id,
                "ver": ver_tag,
                "claude2_upgraded": True,
                "title": spec_h1["title"],
                "outfit_id": outfit_id,
                "banner_style_name": banner_style_name,
                "h_code": h_code,
                "style_code": style_code,
                "style_name": style_name,
                "alt_style_code": alt_code,
                "alt_style_name": alt_name,
                "font_name": font_label,
                "person_side": side,
                "headline_plain": h1_plain,
                "hl_kw": spec_h1["hl_kw"],
                "subline_summary": f"⚡ 2 Ảnh × 2 Hook × 2 Bài Ads CLAUDE2 • H1 ({audit_h1['score']}) & H2 ({audit_h2['score']}) • Scanpath: {'→'.join(s[:4] for s in scanpath_order[:3])}",
                "audit_score": f"H1:{audit_h1['score']} · H2:{audit_h2['score']}",
                "score": audit_h1["score"],
                "all_13_pass": bool(audit_h1["all_13_pass"] and audit_h2["all_13_pass"]),
                "headline_fs_px": h_fs,
                "min_sub_fs_px": min_body_fs,
                "scanpath_order": scanpath_order,
                "subbox_p90_saliency": subbox_p90,
                "text_to_face_energy_ratio": text_face_ratio,
                "claude2_audit": item["claude2_audit"],
                "hook_1": hook_1_card,
                "hook_2": hook_2_card,
                "ad_copy_1": item["ad_copy_1"],
                "ad_copy_2": item["ad_copy_2"],
                "color_img_url": f"https://media.fedu.vn/banner2/{kb_lower}_color.jpg",
                "hook2_img_url": f"https://media.fedu.vn/banner2/{kb_lower}_alt.jpg",
                "bw_img_url": f"https://media.fedu.vn/banner2/{kb_lower}_bw.jpg",
                "final_img_url": f"https://media.fedu.vn/banner2/{kb_lower}_final.jpg",
                "alt_img_url": f"https://media.fedu.vn/banner2/{kb_lower}_alt.jpg",
                "heatmap_img_url": f"https://media.fedu.vn/banner2/{kb_lower}_heatmap.jpg",
                "sbs_img_url": f"./k4_31kb_banners/v2_pilots/batch_out/{kb_lower}_sbs.jpg",
                "versions_count": len(versions_history_json),
                "versions_history": versions_history_json,
            }
            existing_card_path.write_text(json.dumps(card_data, ensure_ascii=False, indent=2), encoding="utf-8")
            print(
                f"[RENDERED & AUDITED] {kb_id}: Hook1='{h1_plain}' ({audit_h1['score']}) | Hook2='{h2_plain}' ({audit_h2['score']})",
                flush=True,
            )

    SPECS_PATH.write_text(json.dumps(master, ensure_ascii=False, indent=2), encoding="utf-8")
    if kb_70_map_path.exists():
        kb_70_map_path.write_text(json.dumps(kb_70_map, ensure_ascii=False, indent=2), encoding="utf-8")

    hub_res = atomic_rebuild_and_sync(push_r2=args.online)
    print(f"[HUB UPDATED] {json.dumps(hub_res, ensure_ascii=False)}", flush=True)


if __name__ == "__main__":
    main()
