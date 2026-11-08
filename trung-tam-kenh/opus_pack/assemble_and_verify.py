#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
assemble_and_verify.py
======================
Lắp ghép bản viết mới của Claude Opus Native (`opus_draft_body.html`) với các fragment giữ nguyên/ẩn đi,
xuất ra:
  - /Users/vietmac/Documents/CODE/k/trung-tam-kenh/logic-tong-hop.html
  - /Users/vietmac/Documents/CODE/k/logic-xay-kenh-tong-hop.html
và chạy 6 Cổng Kiểm Định Tất Định (bao gồm verify_voice.py trên phần văn bản mới của Opus).
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

    # Inject reusable fragments
    replacements = {
        "<!-- INJECT_BASE_STYLES -->": load_frag("base_page1_styles.html"),
        "<!-- INJECT_HIDDEN_3TANG -->": load_frag("frag_hidden_3tang.html"),
        "<!-- INJECT_FAQ_BOTTOM -->": load_frag("frag_faq_bottom.html"),
        "<!-- INJECT_FOOTER -->": load_frag("frag_footer.html"),
    }

    missing_required = []
    for ph in ("<!-- INJECT_HIDDEN_3TANG -->", "<!-- INJECT_FAQ_BOTTOM -->"):
        if ph not in html:
            missing_required.append(ph)

    if missing_required:
        print(f"❌ Gate 1 FAIL: Thiếu placeholder bắt buộc trong opus_draft_body.html: {missing_required}", file=sys.stderr)
        sys.exit(1)

    for ph, val in replacements.items():
        if ph in html:
            html = html.replace(ph, val)

    # Ensure standard FAQ & Flow interactive scripts exist if Opus didn't write custom ones
    if "toggleFlowCheck" not in html or ".faq-question" not in html:
        fallback_js = """
<script>
function toggleFlowCheck(el) {
  el.classList.toggle('is-checked');
  updateFlowStatus();
}
function updateFlowStatus() {
  const checked = document.querySelectorAll('.flow-item.is-checked').length;
  const total = document.querySelectorAll('.flow-item').length;
  const textEl = document.getElementById('flowStatusText');
  const resetBtn = document.getElementById('flowResetBtn');
  if (resetBtn) resetBtn.style.display = checked > 0 ? 'inline-block' : 'none';
  if (!textEl) return;
  if (checked === 0) {
    textEl.textContent = 'Chạm vào từng tiêu chí để kiểm tra tiêu chuẩn video';
  } else if (checked === total) {
    textEl.innerHTML = '🎉 <b style="color: #16a34a;">ĐẠT ĐỦ ' + total + '/' + total + ' TIÊU CHÍ:</b> Video trọn vẹn Thị Giác & Trí Tuệ, sẵn sàng tích lũy 7 giờ niềm tin!';
  } else {
    textEl.innerHTML = 'Đã kiểm tra: <b>' + checked + '/' + total + ' tiêu chuẩn</b> (' + (checked < 3 ? 'Cần bổ sung thêm' : 'Đang rất tốt, tiếp tục hoàn thiện!') + ')';
  }
}
function resetFlowChecks() {
  document.querySelectorAll('.flow-item.is-checked').forEach(el => el.classList.remove('is-checked'));
  updateFlowStatus();
}
function toggleBranch(branch) {
  const items = document.querySelectorAll('.flow-item[data-branch="' + branch + '"]');
  const allChecked = Array.from(items).every(el => el.classList.contains('is-checked'));
  items.forEach(el => allChecked ? el.classList.remove('is-checked') : el.classList.add('is-checked'));
  updateFlowStatus();
}
function highlightAllFlow() {
  const items = document.querySelectorAll('.flow-item');
  const allChecked = Array.from(items).every(el => el.classList.contains('is-checked'));
  items.forEach(el => allChecked ? el.classList.remove('is-checked') : el.classList.add('is-checked'));
  updateFlowStatus();
}
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.faq-item.active').forEach(function(item) {
    var wrapper = item.querySelector('.faq-answer-wrapper');
    if (wrapper) wrapper.style.maxHeight = wrapper.scrollHeight + 'px';
  });
  document.querySelectorAll('.faq-question').forEach(function(question) {
    question.addEventListener('click', function() {
      var item = question.closest('.faq-item');
      if (item) {
        var wrapper = item.querySelector('.faq-answer-wrapper');
        document.querySelectorAll('.faq-item').forEach(function(other) {
          if (other !== item) {
            other.classList.remove('active');
            var ow = other.querySelector('.faq-answer-wrapper');
            if (ow) ow.style.maxHeight = null;
          }
        });
        if (item.classList.contains('active')) {
          item.classList.remove('active');
          if (wrapper) wrapper.style.maxHeight = null;
        } else {
          item.classList.add('active');
          if (wrapper) wrapper.style.maxHeight = wrapper.scrollHeight + 'px';
        }
      } else {
        var next = question.nextElementSibling;
        var icon = question.querySelector('.faq-icon');
        if (next) {
          var hidden = (next.style.display === 'none' || next.style.display === '');
          next.style.display = hidden ? 'block' : 'none';
          if (icon) icon.textContent = hidden ? '−' : '+';
        }
      }
    });
  });
});
</script>
"""
        if "</body>" in html:
            html = html.replace("</body>", fallback_js + "\n</body>")
        else:
            html += fallback_js

    os.makedirs(os.path.dirname(OUT_KENH), exist_ok=True)
    with open(OUT_KENH, "w", encoding="utf-8") as f:
        f.write(html)
    with open(OUT_K, "w", encoding="utf-8") as f:
        f.write(html)

    # Run Gates
    errors = []
    soup = BeautifulSoup(html, "html.parser")

    # Gate 1: No leftover INJECT_ placeholders
    if "<!-- INJECT_" in html:
        errors.append("Gate 1: Còn sót comment placeholder <!-- INJECT_... --> chưa ghép.")

    # Gate 2: Hidden 3-tang exists & visible new prose has 0 mentions of 3-tang / 4-tang
    hidden_div = soup.find(id="legacy-3tang-hidden")
    if not hidden_div or "display:none" not in (hidden_div.get("style") or "").replace(" ", ""):
        errors.append("Gate 2: Khối #legacy-3tang-hidden thiếu hoặc chưa gắn style display:none.")

    # Extract visible new prose (exclude #legacy-3tang-hidden, #sec-faq, footer, scripts, styles)
    visible_clone = BeautifulSoup(html, "html.parser")
    for sel in ["#legacy-3tang-hidden", "#sec-faq", "footer", "script", "style", "svg"]:
        for node in visible_clone.select(sel):
            node.decompose()
    new_prose = visible_clone.get_text("\n", strip=True)
    low_prose = new_prose.lower()

    banned_tier_terms = ["3 tầng", "4 tầng", "ba tầng", "bốn tầng", "tầng 2.5", "tầng 1", "tầng 2", "tầng 3", "công cụ 4 tầng"]
    hit_tiers = [t for t in banned_tier_terms if t in low_prose]
    if hit_tiers:
        errors.append(f"Gate 2: Phần hiển thị mới vẫn còn nhắc đến mô hình tầng cũ: {hit_tiers}")

    # Gate 3: No fake/removed student cases
    banned_cases = ["hằng bđs", "hangbds", "kiên phân bón", "kienpb", "quỳnh anh", "le kitchen", "đặng hường", "tâng xinh", "baohiem", "tattoo"]
    hit_cases = [c for c in banned_cases if c in low_prose]
    if hit_cases:
        errors.append(f"Gate 3: Phần hiển thị mới chứa case học viên đã bị loại bỏ: {hit_cases}")

    # Gate 4: Flow graph & 39 FAQ items intact
    flow_items = soup.select(".flow-item")
    faq_items = soup.select("#sec-faq .faq-item")
    if len(flow_items) < 6:
        errors.append(f"Gate 4: Đồ thị tương tác thiếu .flow-item (chỉ thấy {len(flow_items)}, cần >= 6).")
    if len(faq_items) < 39:
        errors.append(f"Gate 4: Phần câu hỏi dưới cùng #sec-faq bị thiếu câu hỏi (thấy {len(faq_items)}/39).")

    # Gate 5: Length & core synthesis check
    word_count = len(new_prose.split())
    if word_count < 1800:
        errors.append(f"Gate 5: Phần nội dung tổng hợp mới hơi ngắn ({word_count} từ, cần >= 1.800 từ để bao phủ trọn vẹn toàn bộ logic).")
    for kw_group, kws in [
        ("Món quà (Rick Rubin)", ["món quà", "nhận quà"]),
        ("Đầu ra / Bằng chứng (Hormozi & Daniel)", ["đầu ra", "bằng chứng"]),
        ("90-9-1 & Im lặng", ["90", "im lặng", "thầm lặng"]),
        ("7 giờ / 7-11-4", ["7 giờ", "7 tiếng", "11"]),
    ]:
        if not any(k in low_prose for k in kws):
            errors.append(f"Gate 5: Thiếu trục cốt lõi '{kw_group}' trong bài viết mới.")

    # Gate 6: Voice Gate (verify_voice.py)
    prose_md_path = "/tmp/opus_merged_new_prose.md"
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
        errors.append("Gate 6: Trượt cổng giọng văn verify_voice.py (xem chi tiết lỗi bên trên để sửa câu chữ).")

    print(f"=== STATS: New prose = {word_count:,} words | Total HTML = {len(html):,} bytes | Flow items = {len(flow_items)} | FAQ items = {len(faq_items)} ===")
    if errors:
        print("❌ VERIFICATION FAILED:")
        for e in errors:
            print("  -", e)
        sys.exit(2)

    print("✅ ALL 6 GATES PASSED! Files written to:")
    print("  1.", OUT_KENH)
    print("  2.", OUT_K)


if __name__ == "__main__":
    main()
