#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIFIER TẤT ĐỊNH CHO HOOK BANNER K4 + AUDIT VIẾT LẠI (PA5) — VERIFY_HOOK_AUDIT_V5.PY
=====================================================================================
Kiểm tra 6 chốt chặn ngôn ngữ & thị giác (bao gồm LAW_30 & Cognitive Fluency Gate T4):
1. Cấm từ ghép tắt giả tạo / khẩu ngữ AI / ẩn dụ cụt trên Headline & Sub-box.
2. Cấm cụm từ gây ma sát nhận thức (T4 Cognitive Fluency Gate):
   ("tờ rơi", "văn mẫu", "bảng hiệu", "kịch bản giấy", "trải nghiệm", "đời tư",
    "tâm huyết", "năng lượng", "đẳng cấp", "loãng khách", "nhồi bảy gạch đầu",
    "đọc vỏ hộp", "mới đắt", "nói sâu", "sâu sắc").
3. Cấm kiểu cắt chữ điện tín bằng dấu hai chấm `:` hoặc dấu chấm hỏi cụt trong `sub_old` / `sub_new`.
4. Cấm ngắt dòng làm gãy từ ghép tiếng Việt.
5. LAW_30: Mỗi dòng trong 3 dòng của `hook_5["headline_lines"]` (và `hook_1["headline_lines"]`,
   `headline_plain`, sau khi bỏ thẻ `<span class="hl">`) bắt buộc có độ dài `8 <= len(line_plain) <= 16`
   (tối đa 17 ký tự nếu có dấu chấm/phẩy ở cuối và không có chữ rộng `nghiêng, thương`).
6. Bắt buộc có đủ `audit_viet_lai` và `hook_5`.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Any, List

CARDS_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners/banner2_cards")

BANNED_AI_PHRASES = [
    "nghề khô",
    "ngành khô",
    "khô khan",
    "rất khô",
    "bên kia sợ quay",
    "bạn lên sẽ hơn",
    "còn lưỡng",
    "một chợ",
    "một mình một chợ",
    "khách nét",
    "khách kèo",
    "khách sộp",
    "lười đâu",
    "không phải vì",
    "cứng họng",
    "tắt thở",
    "khung rác",
    "bạn đọc số",
    "quay tay thợ",
    "tắt ads",
    "im như chùa",
    "ăn hồng",
    "đai gối",
    "cây đa",
    "tả trúng 3 khó",
    "nhảy trend",
    "view rác",
    "tấu hài",
    "giỏ hàng trống",
    "chữ sách",
    "như mèo",
    "rượu quý",
    "can nhựa",
    "người bán dưa",
]

T4_COGNITIVE_FRICTION_PHRASES = [
    "tờ rơi",
    "văn mẫu",
    "bảng hiệu",
    "kịch bản giấy",
    "trải nghiệm",
    "đời tư",
    "tâm huyết",
    "năng lượng",
    "đẳng cấp",
    "loãng khách",
    "nhồi bảy gạch đầu",
    "đọc vỏ hộp",
    "mới đắt",
    "nói sâu",
    "sâu sắc",
]

BROKEN_SPLIT_PATTERNS = [
    r"vài chục\s*/\s*triệu",
    r"dọn bàn\s*/\s*sạch",
    r"không bằng 1\s*/\s*người",
    r"không bằng một\s*/\s*cái",
    r"cho người chưa\s*/\s*đứng",
    r"chưa dám đăng vì\s*/\s*ngại",
    r"chuẩn bị quá\s*/\s*20 giây",
    r"đừng khoe hàng\s*/\s*mới",
    r"thử máy lau\s*/\s*trên sàn đã",
    r"mười năm làm nghề\s*/\s*hai cơ sở đàng hoàng",
]

WIDE_WORDS = ("nghiêng", "thương")


def strip_html_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s or "").strip()


def check_law_30_line_len(line_plain: str, tag: str, idx: int, issues: List[str]) -> None:
    n = len(line_plain)
    low = line_plain.lower()
    has_trailing_punct = line_plain.endswith(".") or line_plain.endswith(",")
    has_wide_word = any(w in low for w in WIDE_WORDS)
    max_allowed = 17 if (has_trailing_punct and not has_wide_word) else 16
    if n < 8 or n > max_allowed:
        issues.append(f"LAW_30_{tag}_LINE_{idx}_LEN_{n}_OUT_OF_RANGE(8..{max_allowed}):'{line_plain}'")


def verify_single_kb(kb_id: str) -> Dict[str, Any]:
    p = CARDS_DIR / f"{kb_id}.json"
    if not p.exists():
        return {"kb_id": kb_id, "pass": False, "issues": ["MISSING_FILE"]}

    data = json.loads(p.read_text(encoding="utf-8"))
    issues: List[str] = []

    h_plain = data.get("headline_plain", "")
    h1 = data.get("hook_1") or {}
    h5 = data.get("hook_5") or {}
    audit_vl = data.get("audit_viet_lai") or {}

    # 1. Check audit_viet_lai and hook_5 presence
    if not h5 or not h5.get("headline_plain") or not h5.get("headline_lines"):
        issues.append("MISSING_HOOK_5_AUDIT_VIET_LAI")
    if not audit_vl or not audit_vl.get("diagnosis") or not audit_vl.get("core_claim"):
        issues.append("MISSING_AUDIT_VIET_LAI_DIAGNOSIS")

    # 2. Check active headline_plain & hook_5 for banned AI / T4 cognitive friction phrases & LAW_30
    for tag, txt in [("ACTIVE_HEADLINE", h_plain), ("HOOK_5", h5.get("headline_plain", ""))]:
        low = txt.lower()
        for bad in BANNED_AI_PHRASES:
            if bad in low:
                issues.append(f"{tag}_BANNED_PHRASE:{bad}")
        for t4_bad in T4_COGNITIVE_FRICTION_PHRASES:
            if t4_bad in low:
                issues.append(f"{tag}_T4_COGNITIVE_FRICTION:{t4_bad}")
        for pat in BROKEN_SPLIT_PATTERNS:
            if re.search(pat, low):
                issues.append(f"{tag}_BROKEN_WORD_SPLIT:{pat}")

        lines = [x.strip() for x in txt.split("/") if x.strip()]
        if len(lines) != 3:
            issues.append(f"{tag}_NOT_3_LINES:{len(lines)}")
        else:
            for idx, ln in enumerate(lines, 1):
                check_law_30_line_len(ln, tag, idx, issues)

    # 3. Check LAW_30 directly on hook_5["headline_lines"] and hook_1["headline_lines"]
    for h_tag, h_obj in [("HOOK_5_LINES", h5), ("HOOK_1_LINES", h1)]:
        raw_lines = h_obj.get("headline_lines") or []
        if len(raw_lines) != 3:
            issues.append(f"{h_tag}_NOT_3_LINES:{len(raw_lines)}")
        else:
            for idx, raw_ln in enumerate(raw_lines, 1):
                ln_plain = strip_html_tags(raw_ln)
                check_law_30_line_len(ln_plain, h_tag, idx, issues)
                low_ln = ln_plain.lower()
                for t4_bad in T4_COGNITIVE_FRICTION_PHRASES:
                    if t4_bad in low_ln:
                        issues.append(f"{h_tag}_T4_COGNITIVE_FRICTION:{t4_bad}")

    # 4. Check sync between hook_5, hook_1, headline_plain, hook_options[0]
    h5_plain = h5.get("headline_plain", "")
    if h_plain != h5_plain:
        issues.append("UNSYNCED_ACTIVE_HEADLINE_VS_HOOK_5")
    if h1.get("headline_plain", "") != h5_plain:
        issues.append("UNSYNCED_HOOK_1_VS_HOOK_5")
    opts = data.get("hook_options") or []
    if not opts or opts[0].get("headline_plain", "") != h5_plain:
        issues.append("UNSYNCED_HOOK_OPTIONS_0_VS_HOOK_5")

    # 5. Check sub_old & sub_new for robotic colon ':' or question mark '?' and banned phrases
    sub_old = str(h1.get("sub_old", "")).strip()
    sub_new = str(h1.get("sub_new", "")).strip()
    for s_tag, s_val in [("SUB_OLD", sub_old), ("SUB_NEW", sub_new)]:
        if not s_val:
            issues.append(f"{s_tag}_EMPTY")
        if ":" in s_val or "?" in s_val:
            issues.append(f"{s_tag}_ROBOTIC_COLON_OR_QMARK:'{s_val}'")
        low_s = s_val.lower()
        for bad in BANNED_AI_PHRASES:
            if bad in low_s:
                issues.append(f"{s_tag}_BANNED_PHRASE:{bad}")
        for t4_bad in T4_COGNITIVE_FRICTION_PHRASES:
            if t4_bad in low_s:
                issues.append(f"{s_tag}_T4_COGNITIVE_FRICTION:{t4_bad}")
        if len(s_val) > 42 or len(s_val) < 12:
            issues.append(f"{s_tag}_LEN_{len(s_val)}_OUT_OF_RANGE(12..42):'{s_val}'")

    return {
        "kb_id": kb_id,
        "pass": len(issues) == 0,
        "headline_plain": h_plain,
        "line_lengths": [len(strip_html_tags(x)) for x in (h5.get("headline_lines") or [])],
        "sub_old": sub_old,
        "sub_new": sub_new,
        "hook_5": h5_plain,
        "issues": issues,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kbs", type=str, default="", help="Danh sách KB (VD: KB_01,KB_02,KB_03)")
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--end", type=int, default=140)
    args = ap.parse_args()

    if args.kbs.strip():
        kb_list = [x.strip().upper() for x in args.kbs.split(",") if x.strip()]
    else:
        kb_list = [f"KB_{i:02d}" for i in range(args.start, args.end + 1)]

    results = [verify_single_kb(k) for k in kb_list]
    passed = sum(1 for r in results if r["pass"])
    failed = [r for r in results if not r["pass"]]
    print(json.dumps({
        "total": len(results),
        "passed": passed,
        "failed_count": len(failed),
        "all_pass": len(failed) == 0,
        "failed_preview": failed[:10],
    }, ensure_ascii=False, indent=2))
    sys.exit(0 if len(failed) == 0 else 1)


if __name__ == "__main__":
    main()
