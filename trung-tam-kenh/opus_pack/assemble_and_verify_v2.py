#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
assemble_and_verify_v2.py
=========================
Lắp ghép bản viết mới Việt hóa của Claude Opus Native (`opus_draft_body.html`),
kiểm tra:
- Không còn sót các tên nước ngoài bị cấm: Alex, Hormozi, Daniel, Rubin, Diane, Mumbai, Manhattan, Iowa, Buffett, MrBeast, Christensen, Woodsmall, RadiumOne, Nielsen.
- Không còn 3 kênh mẫu cũ: Hoàng Nga, Từ An, Nhà 3 Hờ.
- Chứa học viên thật: Tâng Xinh.
- Phần câu hỏi FAQ có đúng 10 câu hỏi đắt giá mới.
- Vượt qua cổng giọng văn verify_voice.py.
- Đồng bộ ra:
  + /Users/vietmac/Documents/CODE/k/trung-tam-kenh/logic-tong-hop.html
  + /Users/vietmac/Documents/CODE/k/logic-xay-kenh-tong-hop.html
"""

import os
import re
import subprocess
import sys
from bs4 import BeautifulSoup

PACK_DIR = "/Users/vietmac/Documents/CODE/kenh.fedu.vn/opus_pack"
DRAFT_PATH = os.path.join(PACK_DIR, "opus_draft_body.html")
OUT_KENH = "/Users/vietmac/Documents/CODE/k/trung-tam-kenh/logic-tong-hop.html"
OUT_K = "/Users/vietmac/Documents/CODE/k/logic-xay-kenh-tong-hop.html"


def load_frag(name: str) -> str:
    p = os.path.join(PACK_DIR, name)
    return open(p, "r", encoding="utf-8").read() if os.path.exists(p) else ""


def main():
    if not os.path.exists(DRAFT_PATH):
        print(f"❌ FAIL: Chưa tìm thấy file bản thảo {DRAFT_PATH}", file=sys.stderr)
        sys.exit(1)

    html = open(DRAFT_PATH, "r", encoding="utf-8").read()

    # Inject reusable fragments if placeholders present
    replacements = {
        "<!-- INJECT_BASE_STYLES -->": load_frag("base_page1_styles.html"),
        "<!-- INJECT_HIDDEN_3TANG -->": load_frag("frag_hidden_3tang.html"),
        "<!-- INJECT_FOOTER -->": load_frag("frag_footer.html"),
    }

    for ph, val in replacements.items():
        if ph in html:
            html = html.replace(ph, val)

    os.makedirs(os.path.dirname(OUT_KENH), exist_ok=True)
    with open(OUT_KENH, "w", encoding="utf-8") as f:
        f.write(html)
    with open(OUT_K, "w", encoding="utf-8") as f:
        f.write(html)

    # Verification Gates
    errors = []
    soup = BeautifulSoup(html, "html.parser")

    # Gate 1: Check forbidden foreign names & old sample channels
    visible_clone = BeautifulSoup(html, "html.parser")
    for sel in ["#legacy-3tang-hidden", "script", "style", "svg"]:
        for node in visible_clone.select(sel):
            node.decompose()
    new_prose = visible_clone.get_text("\n", strip=True)
    low_prose = new_prose.lower()

    banned_foreign = [
        "alex", "hormozi", "diane", "daniel", "rubin", "mumbai", "manhattan",
        "iowa", "buffett", "mrbeast", "lamborghini", "radiumone", "nielsen",
        "christensen", "woodsmall", "phút 55", "steven bartlett"
    ]
    hit_foreign = [w for w in banned_foreign if w in low_prose]
    if hit_foreign:
        errors.append(f"Gate 1 FAIL: Vẫn còn chứa tên/nguồn nước ngoài: {hit_foreign}")

    banned_old_channels = ["hoàng nga", "momi trendii", "từ an", "men mộc an", "nhà 3 hờ"]
    hit_channels = [c for c in banned_old_channels if c in low_prose]
    if hit_channels:
        errors.append(f"Gate 1 FAIL: Vẫn còn chứa kênh mẫu cũ (không phải học viên): {hit_channels}")

    # Gate 2: Check student Tang Xinh presence
    if "tâng xinh" not in low_prose:
        errors.append("Gate 2 FAIL: Chưa có dẫn chứng học viên thật (chị Tâng Xinh).")

    # Gate 3: Check 10 FAQ questions
    faq_items = soup.select("#sec-faq .faq-item")
    if len(faq_items) != 10:
        errors.append(f"Gate 3 FAIL: Số lượng câu hỏi FAQ trong #sec-faq là {len(faq_items)}, yêu cầu đúng 10 câu.")

    # Gate 4: Check flow items
    flow_items = soup.select(".flow-item")
    if len(flow_items) < 6:
        errors.append(f"Gate 4 FAIL: Đồ thị tương tác thiếu flow-item ({len(flow_items)}/6).")

    # Gate 5: Length check
    words = len(new_prose.split())
    if words < 2500:
        errors.append(f"Gate 5 FAIL: Bài viết mới hơi ngắn ({words} từ, cần >= 2500 từ).")

    # Gate 6: Voice verifier
    prose_md_path = "/tmp/opus_vietnamese_prose.md"
    with open(prose_md_path, "w", encoding="utf-8") as f:
        f.write(new_prose)
    voice_cmd = [
        "python3",
        "/Users/vietmac/.gemini/config/skills/nguyen-viet-voice/scripts/verify_voice.py",
        "--mode", "giaima",
        "--file", prose_md_path,
    ]
    res = subprocess.run(voice_cmd, capture_output=True, text=True)
    print("=== VOICE VERIFIER OUTPUT ===")
    print((res.stdout or "") + (res.stderr or ""))
    if res.returncode != 0:
        errors.append("Gate 6 FAIL: Trượt cổng giọng văn verify_voice.py.")

    print(f"=== STATS: Words = {words:,} | HTML = {len(html):,} bytes | FAQ items = {len(faq_items)} | Flow items = {len(flow_items)} ===")
    if errors:
        print("❌ VERIFICATION FAILED:")
        for e in errors:
            print("  -", e)
        sys.exit(2)

    print("✅ ALL GATES PASSED! Files successfully updated.")


if __name__ == "__main__":
    main()
