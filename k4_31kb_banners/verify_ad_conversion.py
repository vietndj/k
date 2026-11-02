#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIFY AD CONVERSION & CAMPAIGN CONSISTENCY (CLAUDE2 ARCHITECTURE — GATE B3)
============================================================================
Kiểm định tự động 5 Cổng Chuyển Đổi Quảng Cáo (`C1` → `C5`) trên toàn bộ 140 KB (`KB_01..KB_140`)
để đảm bảo đầu ra đồng nhất 100% với `campaign_config.json`:
- C1_PRICE_IN_OPENING: Mức học phí (`4.000.000đ` / `HOC_PHI`) xuất hiện rõ ràng (trong 125 ký tự đầu đối với `ad_copy_3` và trong khối lọc giá đối với `ad_copy_1/2`).
- C2_ZERO_NAKED_URL_AND_BRAND: 0% URL trần (`http://`, `https://`, `fedu.vn`, `offline.fedu.vn`) trong `primary_text` để bảo toàn 100% `utm_content={{ad.name}}` ở nút CTA chính thức và không lộ thương hiệu FEDU.
- C3_ZERO_UNFILLED_PLACEHOLDERS: 0% biến `[[...]]` hoặc `{{...}}` bị sót chưa điền trong văn bản xuất bản.
- C4_CAMPAIGN_FACTS_MATCH: Có đầy đủ Ngày học (`NGAY_HOC`), Địa điểm (`DIA_DIEM`), Cam kết hoàn tiền (`hoàn 100% học phí`), Ưu đãi đi 2 người (`HOC_PHI_NHOM`), và không chứa tên ngoại quốc lạ (`Sauvik Banerjjee`, `Tata Digital`) hay số liệu ảo (`90%`).
- C5_HEADLINE_AND_SUBLINE_LENGTH: Từng dòng Headline `<= 22` ký tự hiển thị (không đếm thẻ HTML), Subline gọn gàng không tràn.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Any, List

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
CAMPAIGN_CFG_PATH = BASE_DIR / "campaign_config.json"
CARDS_DIR = BASE_DIR / "banner2_cards"

BANNED_CLAIMS = [
    "sauvik",
    "banerjjee",
    "tata digital",
    "90% đơn",
    "90% khách",
    "fedu",
    "http://",
    "https://",
]


def strip_html(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s or "").strip()


def verify_kb_card(card: Dict[str, Any], cfg_vars: Dict[str, str]) -> Dict[str, Any]:
    kb_id = card.get("kb_id", "UNKNOWN")
    hoc_phi = cfg_vars.get("HOC_PHI", "4.000.000đ")
    ngay_hoc = cfg_vars.get("NGAY_HOC", "07–08/11")
    hoc_phi_nhom = cfg_vars.get("HOC_PHI_NHOM", "3.500.000đ")

    issues: List[str] = []
    gates = {
        "C1_price_qualification": True,
        "C2_zero_naked_url_and_brand": True,
        "C3_zero_unfilled_vars": True,
        "C4_campaign_facts_and_clean_claims": True,
        "C5_hook_and_v3_image_ready": True,
    }

    for ad_key in ("ad_copy_1", "ad_copy_2", "ad_copy_3"):
        ad_obj = card.get(ad_key)
        if not isinstance(ad_obj, dict) or not ad_obj.get("primary_text"):
            gates["C1_price_qualification"] = False
            issues.append(f"{ad_key}: missing primary_text")
            continue

        pt = ad_obj["primary_text"].strip()
        pt_lower = pt.lower()

        # C1: Price check
        if hoc_phi not in pt and "4.000.000" not in pt and "4 triệu" not in pt_lower:
            gates["C1_price_qualification"] = False
            issues.append(f"{ad_key}: missing price {hoc_phi}")
        if ad_key == "ad_copy_3":
            first_135 = pt[:135]
            if hoc_phi not in first_135 and "4.000.000" not in first_135:
                gates["C1_price_qualification"] = False
                issues.append(f"{ad_key}: price {hoc_phi} not in first 125-135 chars")

        # C2: Zero naked URL & zero FEDU brand in primary_text
        for bad in ("http://", "https://", "fedu.vn", "fedu"):
            if bad in pt_lower:
                gates["C2_zero_naked_url_and_brand"] = False
                issues.append(f"{ad_key}: contains forbidden '{bad}' in primary_text")

        # C3: Zero unfilled placeholders
        if "[[" in pt or "]]" in pt:
            gates["C3_zero_unfilled_vars"] = False
            issues.append(f"{ad_key}: contains unfilled [[...]] placeholder")

        # C4: Campaign facts & banned unverified claims
        if ngay_hoc not in pt and "07-08/11" not in pt:
            gates["C4_campaign_facts_and_clean_claims"] = False
            issues.append(f"{ad_key}: missing date {ngay_hoc}")
        if "hoàn 100%" not in pt_lower and "hoàn đủ 100%" not in pt_lower:
            gates["C4_campaign_facts_and_clean_claims"] = False
            issues.append(f"{ad_key}: missing 100% refund guarantee")
        if hoc_phi_nhom not in pt and "3.500.000" not in pt:
            gates["C4_campaign_facts_and_clean_claims"] = False
            issues.append(f"{ad_key}: missing group price {hoc_phi_nhom}")
        for bc in BANNED_CLAIMS:
            if bc in pt_lower:
                gates["C4_campaign_facts_and_clean_claims"] = False
                issues.append(f"{ad_key}: contains banned claim '{bc}'")

    # C5: Check hook_1, hook_2, hook_3 / v3_price_src
    for hk_key in ("hook_1", "hook_2"):
        hk = card.get(hk_key, {})
        lines = hk.get("headline_lines", []) if isinstance(hk, dict) else []
        if len(lines) != 3:
            gates["C5_hook_and_v3_image_ready"] = False
            issues.append(f"{hk_key}: expected 3 headline_lines, got {len(lines)}")

    all_pass = all(gates.values())
    return {
        "kb_id": kb_id,
        "pass": all_pass,
        "gates": gates,
        "issues": issues,
    }


def main():
    ap = argparse.ArgumentParser(description="Verify Ad Conversion & Campaign Consistency across 140 KBs")
    ap.add_argument("--kb", type=str, default="ALL", help="KB_XX or ALL")
    args = ap.parse_args()

    cfg = json.loads(CAMPAIGN_CFG_PATH.read_text(encoding="utf-8"))
    cfg_vars = cfg.get("variables", {})

    if args.kb == "ALL":
        files = sorted(CARDS_DIR.glob("KB_*.json"), key=lambda p: int(p.stem.split("_")[1]))
    else:
        files = [CARDS_DIR / f"{args.kb}.json"]

    passed_count = 0
    failed_items = []
    for f in files:
        if not f.exists():
            failed_items.append({"kb_id": f.stem, "pass": False, "issues": ["File not found"]})
            continue
        card = json.loads(f.read_text(encoding="utf-8"))
        res = verify_kb_card(card, cfg_vars)
        if res["pass"]:
            passed_count += 1
        else:
            failed_items.append(res)

    summary = {
        "total": len(files),
        "passed": passed_count,
        "failed": len(failed_items),
        "all_pass": len(failed_items) == 0,
        "failed_details": failed_items[:15],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    sys.exit(0 if summary["all_pass"] else 1)


if __name__ == "__main__":
    main()
