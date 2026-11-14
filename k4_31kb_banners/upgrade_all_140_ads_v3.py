#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UPGRADE ALL 140 ADS V3 — CLAUDE2 CONVERSION & EVERGREEN ARCHITECTURE
====================================================================
Nâng cấp toàn bộ thông tin quảng cáo của 140 KB (`KB_01` → `KB_140`) trong:
- `/Users/vietmac/Documents/CODE/k/k4_31kb_banners/banner2_cards/KB_01.json` .. `KB_140.json`
- `/Users/vietmac/Documents/CODE/k/k4_31kb_banners/kb_31_master_specs.json`

Thực thi 3 Quy tắc cốt lõi của Giáo sư CLAUDE2:
1. Khử sạch 100% lỗi chuyển đổi trong thân bài (`ad_copy_1` & `ad_copy_2`):
   - Xóa bỏ mọi URL trần (`https://offline.fedu.vn/`, `http://...`, `offline.fedu.vn`, `fedu.vn`) và từ `FEDU` / `fedu` khỏi `primary_text`.
   - Khử sạch các chi tiết ngoại quốc/chưa kiểm chứng (`Sauvik Banerjjee` ở `KB_34`, `90% đơn giá cao` ở `KB_59`, `quay 30 video` ở `KB_39`).
2. Chèn Phân Cấp Thông Tin Khóa Học, Học Phí `4.000.000đ` & Khử Rủi Ro vào `ad_copy_1` và `ad_copy_2` từ `campaign_config.json`, cập nhật `fb_headline` và `cta_line`.
3. Tạo mới `ad_copy_3` (Khuôn V4 Price-First & Evergreen Template) đặt học phí `4.000.000đ` và lịch học lên Dòng 1 (trong 125 ký tự đầu tiên) kèm `ad_copy_3_template` sử dụng biến `[[...]]`.
"""

import json
import re
from pathlib import Path
from typing import Dict, Any

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
CAMPAIGN_CFG_PATH = BASE_DIR / "campaign_config.json"
CARDS_DIR = BASE_DIR / "banner2_cards"
MASTER_SPEC_PATH = BASE_DIR / "kb_31_master_specs.json"

FB_HEADLINE_V3 = "Lớp Offline 2 Ngày 07–08/11 Tại Hà Nội · Học Phí 4.000.000đ (Hoàn 100% Sau Ngày 1)"
CTA_LINE_V3 = "Bấm nút Đăng ký bên dưới để giữ chỗ (UTM tự động: utm_content={{ad.name}})"

AD12_FOOTER_BLOCK = """───
📍 Lớp Thực Chiến Offline 2 Ngày (Thứ Bảy & Chủ Nhật, 07–08/11 tại Green Hub Long Biên, Hà Nội)
• Học phí: 4.000.000đ (giá gốc 5.000.000đ). Đi 2 người: người thứ 2 chỉ 3.500.000đ.
• Tặng kèm khóa Online quay sẵn từng bước + 30 ngày gửi bài qua Zalo để được sửa trực tiếp.
• Chưa thấy hợp sau Ngày 1: hoàn 100% học phí, không hỏi lý do.

Bấm nút "Đăng ký" ngay dưới bài để để lại tên và số điện thoại (chưa cần chuyển khoản, mình sẽ gọi hỏi ngành của bạn trước, hợp mới giữ chỗ)."""


def clean_voice_text(s: str) -> str:
    """Làm sạch các từ sổ đen trong văn bản và ghi chú meta để đạt chuẩn verify_voice.py."""
    if not isinstance(s, str):
        return s
    s = s.replace(
        "Tối ưu điểm dừng thị giác 3 giây đầu trên Facebook Feed.",
        "Giữ ngón tay người xem trong 3 giây đầu trên bảng tin Facebook.",
    )
    s = s.replace("đặt lại thước đo của chính mình", "đặt lại cách đếm của chính mình")
    s = s.replace("thước đo nên là", "cách đo nên là")
    s = s.replace("đứng làm thước đo cho", "đứng làm chuẩn so sánh cho")
    s = s.replace("Chuyên Gia Trắng Đen", "Chân Dung Trắng Đen")
    s = s.replace("khẩu hiệu chiến lược", "khẩu hiệu chung chung")
    s = s.replace("Chạm nỗi đau 3s", "Gọi trúng chỗ xót 3s")
    s = s.replace("đòn bẩy", "điểm tựa")
    s = s.replace("studio đèn đóm", "studio nhiều đèn")
    s = re.sub(r"\bNỗi đau\b", "Điểm nghẽn", s)
    s = re.sub(r"\bnỗi đau\b", "điểm nghẽn", s)
    return s


def clean_primary_body(raw_text: str, kb_id: str) -> str:
    """
    Làm sạch phần thân bài quảng cáo theo Quy tắc 1 & Quy tắc 2:
    - Idempotent: Cắt bỏ khối footer `───` hoặc khung `ad_copy_3` nếu đã chạy trước đó.
    - Khử chi tiết ngoại quốc / số liệu chưa kiểm chứng (KB_34, KB_59, KB_39).
    - Cắt bỏ dòng lịch học & URL trần rời rạc ở cuối bài.
    - Chuẩn hóa câu chuyển tiếp cuối bài để thân bài Evergreen 100%.
    """
    pt = (raw_text or "").strip()

    # Idempotency: nếu đã gắn khối ─── trước đó thì tách lấy phần thân phía trên
    if "\n───" in pt:
        pt = pt.split("\n───")[0].strip()

    # Quy tắc 1a: KB_34 — Khử tên ngoại quốc Sauvik Banerjjee, cựu CTO Tata Digital
    pt = pt.replace(
        "Sauvik Banerjjee, cựu CTO Tata Digital, gọi tên cơ chế này: làm 14 tiếng mỗi ngày vẫn chạm trần, vì đang lấy sức người bù cho chỗ thiếu 3 Điểm giúp giữ chân.",
        "Nhiều chủ xưởng, chủ tiệm làm 14 tiếng mỗi ngày vẫn chạm trần doanh thu, vì đang lấy sức người bù cho chỗ thiếu hệ thống video giữ chân khách.",
    )

    # Quy tắc 1b: KB_59 (và toàn bộ KB) — Khử "90% đơn giá cao" / "90% đơn" / "90% khách"
    pt = pt.replace("và 90% đơn giá cao", "và phần lớn các đơn hàng giá trị lớn")
    pt = pt.replace("90% đơn giá cao", "Phần lớn các đơn hàng giá trị lớn")
    pt = re.sub(r"90%\s+đơn\b", "phần lớn các đơn hàng", pt, flags=re.IGNORECASE)
    pt = re.sub(r"90%\s+khách\b", "phần lớn khách hàng", pt, flags=re.IGNORECASE)

    # Quy tắc 1c: KB_39 — Thay "quay 30 video" / "quay thành 30 video" / câu chọn 30 câu hỏi ở lớp
    if kb_id == "KB_39":
        pt = pt.replace(
            "chọn 30 câu hỏi nghề khách hay hỏi nhất, viết thành kịch bản video ngắn có mặt chủ, quay ngay tại lớp",
            "lọc ra 30 câu hỏi nghề đắt nhất và cầm tay quay hoàn chỉnh bộ video mẫu ngay tại lớp",
        )
        pt = pt.replace(
            "bạn ra về với danh sách 30 đề tài giải mã nghề của riêng tiệm mình, kịch bản viết sẵn và 3–5 video quay ngay tại lớp",
            "bạn lọc ra 30 câu hỏi nghề đắt nhất và cầm tay quay hoàn chỉnh bộ video mẫu ngay tại lớp",
        )
    pt = re.sub(
        r"quay\s+(?:thành\s+)?30\s+video",
        "lọc ra 30 câu hỏi nghề đắt nhất và cầm tay quay hoàn chỉnh bộ video mẫu ngay tại lớp",
        pt,
        flags=re.IGNORECASE,
    )

    # Quy tắc 2: Bỏ đoạn đuôi cũ rời rạc ở cuối primary_text (chứa URL trần & lịch học lặp)
    pt = re.sub(
        r"\n*Thứ Bảy\s*&\s*Chủ Nhật,\s*07[–-]08/11\s*tại\s*Hà Nội\.?\s*\n*Đăng ký:\s*https?://[^\s]+",
        "",
        pt,
        flags=re.IGNORECASE,
    ).strip()

    # Xóa câu cuối chứa URL https://offline.fedu.vn/ hoặc domain fedu.vn
    pt = re.sub(
        r"\s*(?:[^\.\!\?\n]*https?://[^\s]+|\s*[^\.\!\?\n]*\bfedu\.vn[^\n]*)$",
        "",
        pt,
        flags=re.IGNORECASE,
    ).strip()

    # Xóa mọi URL trần hoặc từ fedu nếu còn sót bất kỳ đâu
    pt = re.sub(r"https?://\S+", "", pt, flags=re.IGNORECASE)
    pt = re.sub(r"\boffline\.fedu\.vn/?\b", "", pt, flags=re.IGNORECASE)
    pt = re.sub(r"\bfedu\.vn/?\b", "", pt, flags=re.IGNORECASE)
    pt = re.sub(r"\bfedu\b", "", pt, flags=re.IGNORECASE)

    # Chuẩn hóa câu chuyển tiếp cuối bài để không lặp ngày tĩnh với khối chốt chặn phía dưới
    pt = re.sub(r"\s*Lịch(?:\s+học)?\s+07[–-]08/11\s+(?:tại|ở)\s+Hà Nội\.?", "", pt)
    pt = re.sub(r":\s*07[–-]08/11\s+(?:tại|ở)\s+Hà Nội\.?", ".", pt)
    pt = re.sub(r",\s*(?:ngày\s+)?07[–-]08/11\s+(?:tại|ở)\s+Hà Nội\.", ".", pt)
    pt = re.sub(r",\s*(?:ngày\s+)?07[–-]08/11\s+(?:tại|ở)\s+Hà Nội,", ",", pt)
    pt = re.sub(r"\s*\(?07[–-]08/11\s+(?:tại|ở)\s+Hà Nội\)?,?", "", pt)
    pt = re.sub(r"Ngày\s+07[–-]08/11\s+(?:tại|ở)\s+Hà Nội,\s*", "", pt)
    pt = re.sub(r"07[–-]08/11\s+(?:tại|ở)\s+Hà Nội,\s*", "", pt)
    pt = re.sub(r"\s*,\s*còn\s*\d+\s*ngày\.", ".", pt)
    pt = re.sub(r"\s+sẽ\s+cùng\s+bạn", " cùng bạn", pt)

    lines = [ln.rstrip() for ln in pt.splitlines()]
    while lines and not lines[-1].strip():
        lines.pop()
    if lines:
        last = lines[-1].strip()
        if last and last[0].islower():
            lines[-1] = last[0].upper() + last[1:]
        pt = "\n".join(lines)

    return clean_voice_text(pt.strip())


def build_ad_copy_3_body(hook_line: str, clean_body_1: str) -> str:
    """Ghép câu Hook sắc nhất và phần thân giải phẫu cơ chế nghề + ẩn dụ của KB cho ad_copy_3."""
    hk = clean_voice_text((hook_line or "").strip())
    if not hk:
        return clean_body_1

    # Kiểm tra nếu câu mở đầu của clean_body_1 đã chứa hook_line thì không lặp lại
    norm_hk = re.sub(r"\W+", "", hk.lower())[:25]
    norm_b1 = re.sub(r"\W+", "", clean_body_1.lower())[:35]
    if norm_hk and norm_hk in norm_b1:
        return clean_body_1

    if hk[-1] not in (".", "!", "?", "…", "”", '"', "'"):
        hk = hk + "."
    return f"{hk}\n\n{clean_body_1}"


def render_template(tpl: str, cfg_vars: Dict[str, str]) -> str:
    """Điền toàn bộ biến [[...]] từ campaign_config.json vào template."""
    out = tpl
    for k, v in cfg_vars.items():
        out = out.replace(f"[[{k}]]", str(v))
    return out


def upgrade_card_dict(card: Dict[str, Any], cfg_vars: Dict[str, str]) -> Dict[str, Any]:
    kb_id = card.get("kb_id", "UNKNOWN")

    # Làm sạch các trường meta (rationale, why_it_works, claude2_audit, banner_style_name)
    if "banner_style_name" in card:
        card["banner_style_name"] = clean_voice_text(card["banner_style_name"])
    if isinstance(card.get("claude2_audit"), dict):
        for k, v in card["claude2_audit"].items():
            if isinstance(v, str):
                card["claude2_audit"][k] = clean_voice_text(v)
    for hk_key in ("hook_1", "hook_2"):
        if isinstance(card.get(hk_key), dict):
            for k, v in card[hk_key].items():
                if isinstance(v, str) and k not in ("headline_plain", "hl_kw", "sub_old", "sub_new", "sub_text"):
                    card[hk_key][k] = clean_voice_text(v)

    # Nâng cấp ad_copy_1 và ad_copy_2
    clean_bodies = {}
    for ad_key in ("ad_copy_1", "ad_copy_2"):
        ad_obj = card.get(ad_key, {})
        if not isinstance(ad_obj, dict):
            ad_obj = {}
        raw_pt = ad_obj.get("primary_text", "")
        cb = clean_primary_body(raw_pt, kb_id)
        clean_bodies[ad_key] = cb

        ad_obj["hook_line"] = clean_voice_text(ad_obj.get("hook_line", ""))
        ad_obj["fb_headline"] = FB_HEADLINE_V3
        ad_obj["cta_line"] = CTA_LINE_V3
        ad_obj["primary_text"] = f"{cb}\n\n{AD12_FOOTER_BLOCK}"
        card[ad_key] = ad_obj

    # Quy tắc 3: Tạo mới ad_copy_3 (Khuôn V4 Price-First & Evergreen Template)
    hook_1_line = card.get("ad_copy_1", {}).get("hook_line", "")
    v4_body = build_ad_copy_3_body(hook_1_line, clean_bodies["ad_copy_1"])

    ad_copy_3_tpl = (
        "Học phí [[HOC_PHI]] · Lớp Offline 2 ngày ([[NGAY_HOC]]) tại [[DIA_DIEM]].\n\n"
        f"{v4_body}\n\n"
        "• [[CAM_KET_HOAN_TIEN]].\n"
        "• [[QUA_TANG]].\n"
        "• Đi 2 người: người thứ 2 chỉ [[HOC_PHI_NHOM]].\n\n"
        "[[CTA_BUTTON_INSTRUCTION]]"
    )
    ad_copy_3_rendered = render_template(ad_copy_3_tpl, cfg_vars)

    card["ad_copy_3"] = {
        "version": "V4_PRICE_FIRST_EVERGREEN",
        "hook_line": f"Học phí {cfg_vars.get('HOC_PHI', '4.000.000đ')} · Lớp Offline 2 ngày ({cfg_vars.get('NGAY_HOC', '07–08/11')}) tại {cfg_vars.get('DIA_DIEM', 'Green Hub Long Biên, Hà Nội')}.",
        "fb_headline": FB_HEADLINE_V3,
        "cta_line": CTA_LINE_V3,
        "primary_text": ad_copy_3_rendered,
        "primary_text_template": ad_copy_3_tpl,
    }
    card["ad_copy_3_template"] = ad_copy_3_tpl

    return card


def main():
    cfg = json.loads(CAMPAIGN_CFG_PATH.read_text(encoding="utf-8"))
    cfg_vars = cfg.get("variables", {})

    files = sorted(CARDS_DIR.glob("KB_*.json"), key=lambda p: int(p.stem.split("_")[1]))
    master_data = json.loads(MASTER_SPEC_PATH.read_text(encoding="utf-8")) if MASTER_SPEC_PATH.exists() else None
    master_kbs = master_data.get("kbs", {}) if isinstance(master_data, dict) else {}

    upgraded_count = 0
    master_synced_count = 0

    for f in files:
        card = json.loads(f.read_text(encoding="utf-8"))
        kb_id = card.get("kb_id", f.stem)
        card = upgrade_card_dict(card, cfg_vars)
        f.write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        upgraded_count += 1

        if kb_id in master_kbs and isinstance(master_kbs[kb_id], dict):
            mkb = master_kbs[kb_id]
            mkb["ad_copy_1"] = card["ad_copy_1"]
            mkb["ad_copy_2"] = card["ad_copy_2"]
            mkb["ad_copy_3"] = card["ad_copy_3"]
            mkb["ad_copy_3_template"] = card["ad_copy_3_template"]
            if "claude2_audit" in mkb and isinstance(card.get("claude2_audit"), dict):
                mkb["claude2_audit"] = card["claude2_audit"]
            master_synced_count += 1

    if master_data is not None:
        MASTER_SPEC_PATH.write_text(json.dumps(master_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "status": "DONE",
                "upgraded_cards": upgraded_count,
                "master_synced": master_synced_count,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
