#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANNER STUDIO ENGINE & FACE/PHASH GATE (Tầng 0 - 0 Token)
=========================================================
Quản lý cơ sở dữ liệu `banner_db.json`, biên dịch `/Users/vietmac/Documents/CODE/k/banner.html`,
kiểm tra ảnh trùng bằng Perceptual Hash (dHash 64-bit), tạo lưới Contact Sheet 1 tấm
để duyệt nhanh Face DNA >99%, và tự động đẩy R2 `media.fedu.vn/banner/`.

Cách dùng:
  1. Trích xuất DB từ banner.html hiện có:
     python3 /Users/vietmac/Documents/CODE/k/build_banner.py --extract
  2. Biên dịch & Kiểm định bất biến (Monotonic Guard):
     python3 /Users/vietmac/Documents/CODE/k/build_banner.py --build
  3. Tạo Contact Sheet + Kiểm tra trùng ảnh (pHash Gate) trước khi duyệt:
     python3 /Users/vietmac/Documents/CODE/k/build_banner.py --contact-sheet img1.jpg img2.jpg --output /tmp/banner_sheet.jpg
  4. Thêm bộ Banner mới (tự upload R2 + cập nhật JSON + build HTML):
     python3 /Users/vietmac/Documents/CODE/k/build_banner.py --add-card \
       --id "style21-custom" --title "Kiểu 21 - ..." --desc "..." \
       --ref-img "/path/ref.png|GỐC" \
       --gen-imgs "/path/gen1.jpg|AI FACE DNA • OUTFIT 1" "/path/gen2.jpg|AI FACE DNA • OUTFIT 2" \
       --upload-r2
"""

import os
import re
import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Tuple
from bs4 import BeautifulSoup, Tag

REPO_K_DIR = Path("/Users/vietmac/Documents/CODE/k")
BANNER_HTML_PATH = REPO_K_DIR / "banner.html"
BANNER_DB_PATH = REPO_K_DIR / "banner_db.json"
R2_MANAGER_PATH = Path("/Users/vietmac/Documents/CODE/Quản gia/r2_manager.py")


def compute_dhash(image_path: Path, hash_size: int = 8) -> int:
    """Tính 64-bit difference hash (dHash) bằng PIL để phát hiện ảnh trùng không cần thư viện ngoài."""
    from PIL import Image
    with Image.open(image_path) as img:
        img = img.convert("L").resize((hash_size + 1, hash_size), Image.Resampling.LANCZOS)
        pixels = list(img.getdata())
    diff = 0
    for row in range(hash_size):
        for col in range(hash_size):
            left = pixels[row * (hash_size + 1) + col]
            right = pixels[row * (hash_size + 1) + col + 1]
            diff = (diff << 1) | (1 if left > right else 0)
    return diff


def hamming_distance(h1: int, h2: int) -> int:
    return bin(h1 ^ h2).count("1")


def generate_contact_sheet(
    image_paths: List[str],
    output_path: str,
    cols: int = 2,
    dup_threshold: int = 6,
) -> Dict[str, Any]:
    """Ghép nhiều ảnh thành 1 tấm lưới Contact Sheet có nhãn số thứ tự, kích thước và cảnh báo trùng pHash."""
    from PIL import Image, ImageDraw, ImageFont

    valid_imgs = []
    hashes = []
    report_items = []
    duplicates = []

    for idx, p_str in enumerate(image_paths, start=1):
        p = Path(p_str)
        if not p.exists():
            report_items.append({"index": idx, "path": p_str, "status": "MISSING"})
            continue
        h = compute_dhash(p)
        min_dist = 64
        dup_of = None
        for prev_idx, prev_h in hashes:
            dist = hamming_distance(h, prev_h)
            if dist < min_dist:
                min_dist = dist
            if dist <= dup_threshold and dup_of is None:
                dup_of = prev_idx
        hashes.append((idx, h))

        with Image.open(p) as im:
            w, h_px = im.size
            rgb = im.convert("RGB")
            valid_imgs.append((idx, p.name, rgb, min_dist, dup_of))

        status = f"DUP_OF_#{dup_of}" if dup_of else "OK"
        if dup_of:
            duplicates.append({"index": idx, "name": p.name, "duplicate_of": dup_of, "hamming": min_dist})
        report_items.append({
            "index": idx,
            "name": p.name,
            "size": f"{w}x{h_px}",
            "dhash_hex": f"{h:016x}",
            "min_hamming": min_dist if len(hashes) > 1 else None,
            "status": status,
        })

    if not valid_imgs:
        raise RuntimeError("Không có ảnh hợp lệ để tạo Contact Sheet.")

    cell_w, cell_h = 540, 720
    rows = (len(valid_imgs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), (15, 23, 42))
    draw = ImageDraw.Draw(sheet)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 22)
    except Exception:
        font = ImageFont.load_default()

    for i, (idx, name, im, min_dist, dup_of) in enumerate(valid_imgs):
        r = i // cols
        c = i % cols
        x0, y0 = c * cell_w, r * cell_h
        im_resized = im.resize((cell_w - 16, cell_h - 64), Image.Resampling.LANCZOS)
        sheet.paste(im_resized, (x0 + 8, y0 + 8))

        badge_color = (220, 38, 38) if dup_of else (15, 98, 254)
        draw.rectangle([x0 + 8, y0 + cell_h - 52, x0 + cell_w - 8, y0 + cell_h - 8], fill=badge_color)
        label = f"#{idx} | {name[:28]} | {'TRÙNG #' + str(dup_of) if dup_of else 'OK (d=' + str(min_dist) + ')'}"
        draw.text((x0 + 18, y0 + cell_h - 42), label, fill=(255, 255, 255), font=font)

    out_p = Path(output_path)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_p, quality=90)
    return {
        "verdict": "FAIL_DUPLICATE" if duplicates else "PASS",
        "contact_sheet": str(out_p),
        "total_images": len(valid_imgs),
        "duplicates": duplicates,
        "items": report_items,
    }


def extract_db_from_html(html_path: Path = BANNER_HTML_PATH, db_path: Path = BANNER_DB_PATH) -> Dict[str, Any]:
    """Trích xuất toàn bộ cấu trúc banner.html ra banner_db.json bảo toàn 100% thẻ và thuộc tính."""
    raw = html_path.read_text(encoding="utf-8")
    first_card_pos = raw.find('<div class="batch-card"')
    bottom_actions_pos = raw.rfind('<div class="bottom-actions">')
    if first_card_pos == -1 or bottom_actions_pos == -1:
        raise RuntimeError("Không tìm thấy vùng batch-card hoặc bottom-actions trong banner.html")

    # Tìm thẻ </div> đóng của .editorial-body ngay trước <div class="bottom-actions">
    close_editorial_pos = raw.rfind("</div>", 0, bottom_actions_pos)
    header_html = raw[:first_card_pos]
    cards_region = raw[first_card_pos:close_editorial_pos]
    footer_html = raw[close_editorial_pos:]

    soup = BeautifulSoup(cards_region, "html.parser")
    cards_data = []
    for card in soup.find_all("div", class_="batch-card", recursive=False):
        card_id = card.get("id", "")
        header_div = card.find("div", class_="batch-header")
        h3_el = header_div.find("h3") if header_div else None
        p_el = header_div.find("p") if header_div else None
        title_html = h3_el.decode_contents() if h3_el else ""
        desc_html = p_el.decode_contents() if p_el else ""

        items_data = []
        grid_div = card.find("div", class_="masonry-grid")
        if grid_div:
            for item in grid_div.find_all("div", class_="masonry-item", recursive=False):
                classes = item.get("class", [])
                is_ref = "ref-item" in classes
                img_el = item.find("img")
                ov_el = item.find("div", class_="overlay")
                items_data.append({
                    "is_ref": is_ref,
                    "src": img_el.get("src", "") if img_el else "",
                    "alt": img_el.get("alt") if img_el and img_el.has_attr("alt") else None,
                    "loading": img_el.get("loading") if img_el and img_el.has_attr("loading") else None,
                    "img_style": img_el.get("style") if img_el and img_el.has_attr("style") else None,
                    "overlay_html": ov_el.decode_contents() if ov_el else "",
                    "overlay_style": ov_el.get("style") if ov_el and ov_el.has_attr("style") else None,
                })

        cards_data.append({
            "id": card_id,
            "title_html": title_html,
            "desc_html": desc_html,
            "items": items_data,
        })

    # Trích xuất từ điển các kiểu bố cục từ header_html
    header_soup = BeautifulSoup(header_html, "html.parser")
    styles_dict = []
    for li in header_soup.find_all("li"):
        txt = li.get_text(" ", strip=True)
        if txt.startswith("Kiểu "):
            styles_dict.append(txt)

    db_obj = {
        "schema_version": "1.0",
        "total_cards": len(cards_data),
        "total_items": sum(len(c["items"]) for c in cards_data),
        "styles_dictionary": styles_dict,
        "header_html": header_html,
        "footer_html": footer_html,
        "cards": cards_data,
    }
    db_path.write_text(json.dumps(db_obj, ensure_ascii=False, indent=2), encoding="utf-8")
    return db_obj


def render_card_html(card: Dict[str, Any]) -> str:
    id_attr = f' id="{card["id"]}"' if card.get("id") else ""
    lines = [
        f'<div class="batch-card"{id_attr}>',
        '  <div class="batch-header">',
        f'    <h3>{card.get("title_html", "")}</h3>',
        f'    <p>{card.get("desc_html", "")}</p>',
        '  </div>',
        '  <div class="masonry-grid">',
    ]
    for it in card.get("items", []):
        cls = "masonry-item ref-item" if it.get("is_ref") else "masonry-item"
        img_attrs = [f'src="{it.get("src", "")}"']
        if it.get("loading"):
            img_attrs.append(f'loading="{it["loading"]}"')
        if it.get("alt") is not None:
            img_attrs.append(f'alt="{it["alt"]}"')
        if it.get("img_style"):
            img_attrs.append(f'style="{it["img_style"]}"')
        img_tag = f'<img {" ".join(img_attrs)}>'
        ov_style = f' style="{it["overlay_style"]}"' if it.get("overlay_style") else ""
        ov_tag = f'<div class="overlay"{ov_style}>{it.get("overlay_html", "")}</div>'
        lines.append(f'    <div class="{cls}">')
        lines.append(f'      {img_tag}')
        lines.append(f'      {ov_tag}')
        lines.append('    </div>')
    lines.append('  </div>')
    lines.append('</div>')
    return "\n".join(lines)


def build_html_from_db(db_path: Path = BANNER_DB_PATH, html_path: Path = BANNER_HTML_PATH) -> Dict[str, Any]:
    """Biên dịch banner.html từ banner_db.json kèm Monotonic Guard chống mất thẻ."""
    db_obj = json.loads(db_path.read_text(encoding="utf-8"))
    cards = db_obj.get("cards", [])
    total_items = sum(len(c.get("items", [])) for c in cards)

    if len(cards) < 45 or total_items < 229:
        raise RuntimeError(
            f"[MONOTONIC GUARD] Từ chối ghi đè: số card ({len(cards)} < 45) hoặc số ảnh ({total_items} < 229) bị tụt!"
        )

    cards_html = "\n\n".join(render_card_html(c) for c in cards)
    full_html = db_obj["header_html"] + cards_html + "\n            " + db_obj["footer_html"]
    html_path.write_text(full_html, encoding="utf-8")

    # Verify bằng BeautifulSoup
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    v_cards = len(soup.find_all("div", class_="batch-card"))
    v_items = len(soup.find_all("div", class_="masonry-item"))
    if v_cards != len(cards) or v_items != total_items:
        raise RuntimeError(f"Verify HTML thất bại: cards={v_cards}/{len(cards)}, items={v_items}/{total_items}")

    return {"status": "PASS", "cards": v_cards, "items": v_items, "html_path": str(html_path)}


def upload_to_r2(local_path: str) -> str:
    p = Path(local_path)
    if not p.exists():
        raise FileNotFoundError(f"Không tìm thấy ảnh: {local_path}")
    r2_key = f"banner/{p.name}"
    subprocess.run(
        [sys.executable, str(R2_MANAGER_PATH), "--put", str(p), r2_key],
        check=True,
    )
    return f"https://media.fedu.vn/{r2_key}?v=2"


def main() -> None:
    parser = argparse.ArgumentParser(description="Banner Studio Engine & Face/pHash Gate")
    parser.add_argument("--extract", action="store_true", help="Trích xuất banner.html sang banner_db.json")
    parser.add_argument("--build", action="store_true", help="Biên dịch banner.html từ banner_db.json")
    parser.add_argument("--list-styles", action="store_true", help="In danh sách các kiểu bố cục chuẩn")
    parser.add_argument("--contact-sheet", nargs="+", help="Danh sách ảnh cần kiểm tra pHash và ghép Contact Sheet")
    parser.add_argument("--output", default="/tmp/banner_contact_sheet.jpg", help="Đường dẫn ảnh Contact Sheet đầu ra")
    parser.add_argument("--add-card", action="store_true", help="Thêm 1 batch-card mới vào banner_db.json và build")
    parser.add_argument("--id", default="", help="ID của batch-card mới")
    parser.add_argument("--title", default="", help="Tiêu đề h3 của batch-card")
    parser.add_argument("--desc", default="", help="Mô tả p của batch-card")
    parser.add_argument("--ref-img", default="", help="Đường dẫn hoặc URL ảnh gốc kèm nhãn: path_or_url|LABEL")
    parser.add_argument("--gen-imgs", nargs="*", default=[], help="Danh sách ảnh AI: path_or_url|LABEL")
    parser.add_argument("--upload-r2", action="store_true", help="Tự động đẩy các file local lên R2 banner/")
    args = parser.parse_args()

    if args.extract:
        db = extract_db_from_html()
        print(json.dumps({"status": "EXTRACTED", "cards": db["total_cards"], "items": db["total_items"]}, ensure_ascii=False))
        return

    if args.list_styles:
        if not BANNER_DB_PATH.exists():
            extract_db_from_html()
        db = json.loads(BANNER_DB_PATH.read_text(encoding="utf-8"))
        for s in db.get("styles_dictionary", []):
            print(s)
        return

    if args.contact_sheet:
        rep = generate_contact_sheet(args.contact_sheet, args.output)
        print(json.dumps(rep, ensure_ascii=False, indent=2))
        sys.exit(0 if rep["verdict"] == "PASS" else 2)

    if args.add_card:
        if not BANNER_DB_PATH.exists():
            extract_db_from_html()
        db = json.loads(BANNER_DB_PATH.read_text(encoding="utf-8"))
        items = []
        if args.ref_img:
            parts = args.ref_img.split("|", 1)
            src = parts[0].strip()
            lbl = parts[1].strip() if len(parts) > 1 else "GỐC"
            if args.upload_r2 and not src.startswith("http"):
                src = upload_to_r2(src)
            items.append({"is_ref": True, "src": src, "alt": "Reference", "loading": None, "img_style": None, "overlay_html": lbl, "overlay_style": None})
        for g in args.gen_imgs:
            parts = g.split("|", 1)
            src = parts[0].strip()
            lbl = parts[1].strip() if len(parts) > 1 else "AI FACE DNA"
            if args.upload_r2 and not src.startswith("http"):
                src = upload_to_r2(src)
            items.append({"is_ref": False, "src": src, "alt": lbl, "loading": "lazy", "img_style": None, "overlay_html": lbl, "overlay_style": None})

        new_card = {"id": args.id, "title_html": args.title, "desc_html": args.desc, "items": items}
        db["cards"].append(new_card)
        db["total_cards"] = len(db["cards"])
        db["total_items"] = sum(len(c["items"]) for c in db["cards"])
        BANNER_DB_PATH.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")
        res = build_html_from_db()
        print(json.dumps(res, ensure_ascii=False))
        return

    if args.build:
        res = build_html_from_db()
        print(json.dumps(res, ensure_ascii=False))
        return

    parser.print_help()


if __name__ == "__main__":
    main()
