#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P0.1 - FONT REGISTRY & VIETNAMESE GLYPH METRICS ENGINE
======================================================
Quét toàn bộ kho font `/Users/vietmac/Documents/CODE/fedu-font/fonts/` và các thư mục font hệ thống:
1. Kiểm tra độ phủ 134 ký tự tiếng Việt có dấu (67 thường + 67 HOA) bằng `fontTools` (loại bỏ font thiếu glyph hoặc trỏ về `.notdef`).
2. Đo chính xác bằng đơn vị font (Font Units) và chuẩn hóa theo `UPM`:
   - `upm` (Units Per Em)
   - `x_height` & `x_ratio = x_height / upm` (để tính `font_size_px = target_x_height_px / x_ratio`)
   - `cap_height` & `cap_ratio = cap_height / upm`
   - `stacked_top_max` (đỉnh dấu chồng cao nhất của `Ặ, Ẫ, Ỗ, Ữ, Ấ, Ể, Ổ, Ứ`)
   - `descender_bottom_min` (đáy dấu nặng/móc dưới thấp nhất của `ặ, ỵ, ỹ, ự, ộ, g, p, y`)
   - `min_line_height_ratio = (stacked_top_max + abs(descender_bottom_min)) / upm + 0.02`
3. Xếp mỗi họ font vào 6 nhóm thiết kế: `Grotesk`, `Serif`, `Condensed`, `Extended`, `Mono`, `Display`.
4. Lưu `/Users/vietmac/Documents/CODE/k/k4_31kb_banners/font_registry.json` và đồng bộ đường dẫn tuyệt đối + thông số đo đạc vào `k4_ledger.json`.
"""

import json
import os
import re
import unicodedata
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

VIET_LOWER = "àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
VIET_UPPER = VIET_LOWER.upper()
VIET_134 = list(unicodedata.normalize("NFC", VIET_LOWER + VIET_UPPER))
assert len(VIET_134) == 134, f"Expected 134 Vietnamese chars, got {len(VIET_134)}"

STACKED_UPPER_CHARS = [unicodedata.normalize("NFC", c) for c in ["Ặ", "Ẫ", "Ỗ", "Ữ", "Ấ", "Ể", "Ổ", "Ứ", "Ắ", "Ẳ"]]
DESCENDER_LOWER_CHARS = [unicodedata.normalize("NFC", c) for c in ["ặ", "ỵ", "ỹ", "ự", "ộ", "ệ", "ậ", "g", "p", "q", "y"]]

FONT_SEARCH_DIRS = [
    Path("/Users/vietmac/Documents/CODE/fedu-font/fonts"),
    Path("/Users/vietmac/Documents/CODE/Quản gia/auto-edit-tuquay/fonts"),
    Path("/Users/vietmac/.gemini/config/skills/auto-edit-video/remotion-studio/public/fonts"),
]

OUT_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
REGISTRY_PATH = OUT_DIR / "font_registry.json"
LEDGER_PATH = OUT_DIR / "k4_ledger.json"


def get_glyph_bounds(tt: TTFont, glyph_set, glyph_name: str) -> Optional[Tuple[float, float, float, float]]:
    """Trả về (xMin, yMin, xMax, yMax) của glyph bằng BoundsPen."""
    try:
        pen = BoundsPen(glyph_set)
        glyph_set[glyph_name].draw(pen)
        return pen.bounds
    except Exception:
        return None


def inspect_font_file(font_path: Path) -> Optional[Dict[str, Any]]:
    """Kiểm tra 1 file font có đủ 134 ký tự tiếng Việt và đo thông số UPM, x-height, cap-height, đỉnh/đáy dấu."""
    try:
        tt = TTFont(str(font_path), lazy=True)
        cmap = tt.getBestCmap()
        if not cmap:
            tt.close()
            return None

        glyph_set = tt.getGlyphSet()
        notdef_bounds = get_glyph_bounds(tt, glyph_set, ".notdef")

        missing_chars = []
        for ch in VIET_134:
            cp = ord(ch)
            gname = cmap.get(cp)
            if not gname or gname == ".notdef" or gname not in glyph_set:
                missing_chars.append(ch)
                continue
            b = get_glyph_bounds(tt, glyph_set, gname)
            if b is None:
                missing_chars.append(ch)
                continue
            # Nếu chữ có dấu mà kích thước hộp y hệt chữ không dấu hoặc .notdef (lỗi font giả Việt hóa)
            if notdef_bounds and b == notdef_bounds:
                missing_chars.append(ch)

        if missing_chars:
            tt.close()
            return None

        upm = int(tt["head"].unitsPerEm)

        # Đo x-height thực tế từ glyph 'x'
        x_gname = cmap.get(ord("x"))
        x_bounds = get_glyph_bounds(tt, glyph_set, x_gname) if x_gname else None
        x_height = int(round(x_bounds[3] - x_bounds[1])) if x_bounds else 0
        if x_height <= 0 and "OS/2" in tt and getattr(tt["OS/2"], "sxHeight", 0) > 0:
            x_height = int(tt["OS/2"].sxHeight)
        if x_height <= 0:
            x_height = int(round(upm * 0.52))

        # Đo cap-height thực tế từ glyph 'H'
        h_gname = cmap.get(ord("H"))
        h_bounds = get_glyph_bounds(tt, glyph_set, h_gname) if h_gname else None
        cap_height = int(round(h_bounds[3] - h_bounds[1])) if h_bounds else 0
        if cap_height <= 0 and "OS/2" in tt and getattr(tt["OS/2"], "sCapHeight", 0) > 0:
            cap_height = int(tt["OS/2"].sCapHeight)
        if cap_height <= 0:
            cap_height = int(round(upm * 0.72))

        # Đo đỉnh dấu chồng cao nhất (Ặ, Ẫ, Ỗ, Ữ...)
        stacked_tops = []
        for ch in STACKED_UPPER_CHARS:
            gn = cmap.get(ord(ch))
            if gn:
                b = get_glyph_bounds(tt, glyph_set, gn)
                if b:
                    stacked_tops.append(b[3])
        stacked_top_max = int(round(max(stacked_tops))) if stacked_tops else int(round(cap_height * 1.32))

        # Đo đáy dấu nặng / móc dưới thấp nhất (ặ, ỵ, ỹ, g, p, y...)
        desc_bottoms = []
        for ch in DESCENDER_LOWER_CHARS:
            gn = cmap.get(ord(ch))
            if gn:
                b = get_glyph_bounds(tt, glyph_set, gn)
                if b:
                    desc_bottoms.append(b[1])
        descender_bottom_min = int(round(min(desc_bottoms))) if desc_bottoms else -int(round(upm * 0.25))

        x_ratio = round(x_height / upm, 4)
        cap_ratio = round(cap_height / upm, 4)
        min_line_height_ratio = round((stacked_top_max + abs(descender_bottom_min)) / upm + 0.02, 4)

        tt.close()
        return {
            "file_name": font_path.name,
            "abs_path": str(font_path),
            "ext": font_path.suffix.lower(),
            "upm": upm,
            "x_height": x_height,
            "cap_height": cap_height,
            "x_ratio": x_ratio,
            "cap_ratio": cap_ratio,
            "stacked_top_max": stacked_top_max,
            "descender_bottom_min": descender_bottom_min,
            "min_line_height_ratio": min_line_height_ratio,
            "viet_134_complete": True,
        }
    except Exception:
        return None


def classify_font_group(family_name: str) -> str:
    """Xếp họ font vào 6 nhóm: Condensed, Extended, Mono, Serif, Display, Grotesk."""
    low = family_name.lower()
    if any(k in low for k in ["cond", "schmal", "narrow", "compressed", "compact"]):
        return "Condensed"
    if any(k in low for k in ["wide", "ext", "integral", "expanded"]):
        return "Extended"
    if any(k in low for k in ["mono", "code", "console", "courier"]):
        return "Mono"
    if any(k in low for k in [
        "tiempos", "domaine", "sectra", "financier", "alpina", "noe", "feijoa",
        "acta", "caslon", "jenson", "freight", "serif", "garamond", "minion",
        "baskerville", "bodoni", "didot", "canela", "lyon", "chronicle", "ogg",
        "editorial", "recife", "moret", "boska", "sentient", "zodiak", "newyork"
    ]):
        return "Serif"
    if any(k in low for k in ["clash", "abril", "thunder", "display", "fatface", "stencil", "poster"]):
        return "Display"
    return "Grotesk"


def build_registry() -> Dict[str, Any]:
    all_files: Dict[str, Path] = {}
    for d in FONT_SEARCH_DIRS:
        if not d.exists():
            continue
        for p in sorted(d.rglob("*")):
            if p.is_file() and p.suffix.lower() in (".ttf", ".otf", ".woff2"):
                # Ưu tiên .ttf / .otf nếu trùng tên gốc hoặc giữ theo tên file đầy đủ
                if p.name not in all_files:
                    all_files[p.name] = p

    print(f"Scanning {len(all_files)} font files across {len(FONT_SEARCH_DIRS)} directories...")
    valid_files: Dict[str, Dict[str, Any]] = {}
    for fname, fpath in all_files.items():
        info = inspect_font_file(fpath)
        if info:
            valid_files[fname] = info

    print(f"Found {len(valid_files)} font files with 100% 134 Vietnamese characters!")

    # Gom theo họ font (Family prefix trước dấu '-')
    families: Dict[str, Dict[str, Any]] = {}
    for fname, info in valid_files.items():
        stem = Path(fname).stem
        parts = stem.split("-")
        fam_name = parts[0] if len(parts) == 2 else "-".join(parts[:-1]) if len(parts) > 2 else stem
        if fam_name not in families:
            families[fam_name] = {
                "family_name": fam_name,
                "group": classify_font_group(fam_name),
                "styles": [],
            }
        families[fam_name]["styles"].append(info)

    # Cập nhật và kiểm chứng 20 họ font trong k4_ledger.json
    ledger = json.loads(LEDGER_PATH.read_text())
    curated_20 = {}
    for kb_data in ledger.values():
        for ang in kb_data["angles"]:
            for k in ["before_A", "before_B"]:
                f = ang[k]["font"]
                curated_20[f["id"]] = f

    verified_curated: Dict[str, Dict[str, Any]] = {}
    # Danh sách dự phòng theo từng nhóm nếu có file nào trong curated_20 thiếu dấu tiếng Việt
    group_fallbacks = {
        "Grotesk": ("FDAeonik", "FDAeonik-Bold.ttf", "FDAeonik-Regular.ttf"),
        "Serif": ("FDTiemposHeadline", "FDTiemposHeadline-Bold.woff2", "FDTiemposText-Bold.woff2"),
        "Condensed": ("FDFoundersGroteskCondensed", "FDFoundersGroteskCondensed-Bold.woff2", "FDFoundersGrotesk-Regular.woff2"),
        "Extended": ("FDIntegralCF", "FDIntegralCF-Bold.ttf", "FDIntegralCF-Regular.ttf"),
        "Display": ("FDClashDisplay", "FDClash-DisplaySemibold.ttf", "FDGilroy-Medium.otf"),
        "Mono": ("FDSohneMono", "FDSohneMono-Fett.woff2", "FDSohneMono-Buch.woff2"),
    }

    for fid, f in sorted(curated_20.items()):
        b_name = f["bold"]
        r_name = f["reg"]
        b_info = valid_files.get(b_name)
        r_info = valid_files.get(r_name)

        # Nếu không tìm thấy trong valid_files, thử tìm phiên bản .ttf/.otf/.woff2 cùng stem
        if not b_info:
            b_stem = Path(b_name).stem
            for cand_ext in [".ttf", ".otf", ".woff2"]:
                if b_stem + cand_ext in valid_files:
                    b_info = valid_files[b_stem + cand_ext]
                    b_name = b_stem + cand_ext
                    break
        if not r_info:
            r_stem = Path(r_name).stem
            for cand_ext in [".ttf", ".otf", ".woff2"]:
                if r_stem + cand_ext in valid_files:
                    r_info = valid_files[r_stem + cand_ext]
                    r_name = r_stem + cand_ext
                    break

        if not b_info or not r_info:
            print(f"WARNING: {fid} ({f['name']}) bold={b_name} ({bool(b_info)}) reg={r_name} ({bool(r_info)}) -> finding replacement in group {f['group']}")
            # Tìm họ khác trong valid_files thuộc cùng group
            fb_fam, fb_b, fb_r = group_fallbacks.get(f["group"], group_fallbacks["Grotesk"])
            if not b_info:
                b_info = valid_files[fb_b]
                b_name = fb_b
            if not r_info:
                r_info = valid_files[fb_r]
                r_name = fb_r

        verified_curated[fid] = {
            "id": fid,
            "group": f["group"],
            "name": f["name"],
            "bold": b_name,
            "bold_path": b_info["abs_path"],
            "reg": r_name,
            "reg_path": r_info["abs_path"],
            "metrics": {
                "upm": b_info["upm"],
                "x_height": b_info["x_height"],
                "cap_height": b_info["cap_height"],
                "x_ratio": b_info["x_ratio"],
                "cap_ratio": b_info["cap_ratio"],
                "stacked_top_max": b_info["stacked_top_max"],
                "descender_bottom_min": b_info["descender_bottom_min"],
                "min_line_height_ratio": max(b_info["min_line_height_ratio"], r_info["min_line_height_ratio"]),
                "reg_x_ratio": r_info["x_ratio"],
                "reg_min_line_height_ratio": r_info["min_line_height_ratio"],
            },
        }
        print(
            f"  [VERIFIED {fid}] {f['name']:28s} ({f['group']:9s}) | "
            f"x_ratio={b_info['x_ratio']:.3f} | min_lh={verified_curated[fid]['metrics']['min_line_height_ratio']:.3f} | "
            f"bold={b_name}"
        )

    # Cập nhật thông số metrics và đường dẫn vào k4_ledger.json
    for kb_data in ledger.values():
        for ang in kb_data["angles"]:
            for k in ["before_A", "before_B"]:
                fid = ang[k]["font"]["id"]
                ang[k]["font"] = verified_curated[fid]

    LEDGER_PATH.write_text(json.dumps(ledger, ensure_ascii=False, indent=2))
    print(f"Updated {LEDGER_PATH} with verified font paths and x-height/line-height metrics.")

    registry_data = {
        "total_scanned_files": len(all_files),
        "total_valid_viet_134_files": len(valid_files),
        "total_valid_families": len(families),
        "curated_20_families": verified_curated,
        "all_valid_files": valid_files,
    }
    REGISTRY_PATH.write_text(json.dumps(registry_data, ensure_ascii=False, indent=2))
    print(f"Saved {REGISTRY_PATH} ({REGISTRY_PATH.stat().st_size:,} bytes).")
    return registry_data


if __name__ == "__main__":
    build_registry()
