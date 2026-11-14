#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kb3k4_cli.py — Trình quản trị Tập trung Bộ Kịch Bản Quảng Cáo K4 (Single Source of Truth)
Quản lý đồng bộ 100% giữa:
  1. Kho dữ liệu gốc: /Users/vietmac/Documents/CODE/course/kb3k4_data.json
  2. 4 File HTML đích (Mục lục TOC + Bảng Ma Trận + Thẻ Prompter + Bộ đếm + Auto-Batching JS):
     - /Users/vietmac/Documents/CODE/course/kb3k4.html
     - /Users/vietmac/Documents/CODE/course/kichban-quangcao-k4.html
     - /Users/vietmac/Documents/CODE/k/kb3k4.html
     - /Users/vietmac/Documents/CODE/k/kichban-quangcao-k4.html

Cách dùng nhanh:
  • Liệt kê / Tìm kiếm:
      python3 /Users/vietmac/Documents/CODE/course/kb3k4_cli.py list
      python3 /Users/vietmac/Documents/CODE/course/kb3k4_cli.py list --q "nội thất"
  • Xem chi tiết 1 bài (kèm 14 câu thoại sạch):
      python3 /Users/vietmac/Documents/CODE/course/kb3k4_cli.py show 142
  • Sửa tiêu đề / phụ đề / logic / câu thoại 1 bài (Tự động cập nhật cả TOC + Ma Trận + Thẻ Kịch bản ở 4 file):
      python3 /Users/vietmac/Documents/CODE/course/kb3k4_cli.py update 142 --title "TIÊU ĐỀ MỚI"
      python3 /Users/vietmac/Documents/CODE/course/kb3k4_cli.py update 142 --bai-file /path/to/142.md
  • Thêm 1 bài mới:
      python3 /Users/vietmac/Documents/CODE/course/kb3k4_cli.py add --id 181 --title "..." --bai-file /path/to/181.md
  • Xóa 1 hoặc nhiều bài:
      python3 /Users/vietmac/Documents/CODE/course/kb3k4_cli.py delete 181
  • Biên dịch lại 4 file HTML & Đẩy Online (git push cả 2 repo course & k):
      python3 /Users/vietmac/Documents/CODE/course/kb3k4_cli.py build --push
"""

import argparse
import html as html_lib
import json
import os
import re
import subprocess
import sys
from typing import Dict, List, Optional, Tuple

COURSE_DIR = "/Users/vietmac/Documents/CODE/course"
REPO_K_DIR = "/Users/vietmac/Documents/CODE/k"
DATA_JSON_PATH = os.path.join(COURSE_DIR, "kb3k4_data.json")
DATA_JSON_COPY = os.path.join(REPO_K_DIR, "kb3k4_data.json")

TARGET_HTML_FILES = [
    os.path.join(COURSE_DIR, "kb3k4.html"),
    os.path.join(COURSE_DIR, "kichban-quangcao-k4.html"),
    os.path.join(REPO_K_DIR, "kb3k4.html"),
    os.path.join(REPO_K_DIR, "kichban-quangcao-k4.html"),
]

VERIFY_VOICE_SCRIPT = "/Users/vietmac/.gemini/config/skills/nguyen-viet-voice/scripts/verify_voice.py"

TOC_START = "<!-- KB_TOC_START -->"
TOC_END = "<!-- KB_TOC_END -->"
MAT_START = "<!-- KB_MATRIX_START -->"
MAT_END = "<!-- KB_MATRIX_END -->"
SEC_START = "<!-- KB_SECTIONS_START -->"
SEC_END = "<!-- KB_SECTIONS_END -->"


def add_breathing_slashes(sent: str) -> Tuple[str, str]:
    """Tự động tính thời lượng đọc (2.8 từ/giây) và chèn dấu ngắt hơi '/'."""
    words = sent.split()
    sec = round(len(words) / 2.8, 1)
    sec_str = str(sec).replace(".", ",") + "s"
    if " / " in sent:
        return sent, sec_str
    parts = sent.split(", ")
    if len(parts) > 1:
        slashed = ", / ".join(parts)
    elif len(words) > 14:
        mid = len(words) // 2
        slashed = " ".join(words[:mid]) + " / " + " ".join(words[mid:])
    else:
        slashed = sent
    return slashed, sec_str


def strip_slashes_and_time(raw_line_html: str) -> str:
    """Bóc câu văn thuần từ thẻ <span>... <code...>(4,3s)</code></span>."""
    txt = re.sub(r"<code[^>]*>.*?</code>", "", raw_line_html, flags=re.S)
    txt = re.sub(r"<[^>]+>", "", txt)
    txt = html_lib.unescape(txt)
    txt = re.sub(r"\s*/\s*", " ", txt)
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt


def render_link_badge(label: str, url: str, kind: str = "kho") -> str:
    if kind == "stu" or "stu.fedu.vn" in url:
        style = "display:inline-flex; align-items:center; gap:4px; padding:4px 10px; border-radius:6px; font-family:var(--font-heading); font-size:0.78rem; font-weight:600; text-decoration:none; background:#fef3c7; border:1px solid #fde68a; color:#92400e;"
    elif kind == "repok" or "fedu.vn/k/" in url:
        style = "display:inline-flex; align-items:center; gap:4px; padding:4px 10px; border-radius:6px; font-family:var(--font-heading); font-size:0.78rem; font-weight:600; text-decoration:none; background:#f8fafc; border:1px solid #cbd5e1; color:#0f172a;"
    else:
        style = "display:inline-flex; align-items:center; gap:4px; padding:4px 10px; border-radius:6px; font-family:var(--font-heading); font-size:0.78rem; font-weight:600; text-decoration:none; background:#eff6ff; border:1px solid #bfdbfe; color:#1d4ed8;"
    return f'<a href="{url}" target="_blank" rel="noopener" style="{style}">{label}</a>'


def extract_from_html_to_json() -> Dict:
    """Trích xuất toàn bộ 177 kịch bản hiện có từ kb3k4.html sang cấu trúc JSON chuẩn."""
    src_path = TARGET_HTML_FILES[0]
    with open(src_path, "r", encoding="utf-8") as f:
        html = f.read()

    toc_matches = list(re.finditer(r'[ \t]*<li><a href="#prompter-kb(\d+)"[^>]*>.*?</a></li>', html))
    mat_matches = list(re.finditer(r'[ \t]*<tr>\s*<td><strong><a href="#prompter-kb(\d+)">.*?</tr>', html, flags=re.S))
    sec_matches = list(re.finditer(r'[ \t]*(?:<!--[^\n]*-->\s*)*<section id="prompter-kb(\d+)".*?</section>', html, flags=re.S))

    toc_map = {int(m.group(1)): m.group(0) for m in toc_matches}
    mat_map = {int(m.group(1)): m.group(0) for m in mat_matches}
    sec_map = {int(m.group(1)): m.group(0) for m in sec_matches}

    all_ids = sorted(sec_map.keys())
    items = {}

    for kb_id in all_ids:
        sec_html = sec_map[kb_id]
        toc_html = toc_map.get(kb_id, "")
        mat_html = mat_map.get(kb_id, "")

        # Extract title from section header: 🎙️ KB XX: "..."
        m_title = re.search(r'🎙️\s*KB\s*0?\d+\s*:\s*"([^"]+)"', sec_html)
        if not m_title:
            m_title = re.search(r'KB\s*0?\d+\s*:\s*([^<(]+)', toc_html)
        title = html_lib.unescape(m_title.group(1).strip()) if m_title else f"KỊCH BẢN {kb_id}"

        # Extract badge
        m_badge = re.search(r'<span class="s-badge[^"]*"[^>]*>(.*?)</span>', sec_html, flags=re.S)
        badge = html_lib.unescape(m_badge.group(1).strip()) if m_badge else f"🔥 KỊCH BẢN {kb_id}"

        # Extract subtitle
        m_sub = re.search(r'<div style="font-size:\s*0\.82rem;\s*color:\s*var\(--ink-muted\);">(.*?)</div>', sec_html, flags=re.S)
        subtitle = m_sub.group(1).strip() if m_sub else ""

        # Extract links in kb-ref-box
        links = []
        m_ref = re.search(r'<div class="kb-ref-box".*?</div>\s*</div>', sec_html, flags=re.S)
        if m_ref:
            for m_a in re.finditer(r'<a href="([^"]+)"[^>]*>(.*?)</a>', m_ref.group(0), flags=re.S):
                u, lbl = m_a.group(1).strip(), m_a.group(2).strip()
                kind = "stu" if "stu.fedu.vn" in u else ("repok" if "fedu.vn/k/" in u else "kho")
                links.append({"label": lbl, "url": u, "kind": kind})

        # Extract logic
        m_logic = re.search(r'💡 Logic &amp; Cách tiếp cận:</strong>\s*(.*?)</div>', sec_html, flags=re.S)
        logic = m_logic.group(1).strip() if m_logic else ""

        # Extract clean sentences
        clean_lines = []
        for m_line in re.finditer(
            r'<div class="clean-line"[^>]*data-kb\d+="([^"]+)"[^>]*><span class="clean-num">([^<]+)</span><span>(.*?)</span></div>',
            sec_html,
            flags=re.S,
        ):
            code_key, num_label, span_inner = m_line.group(1), m_line.group(2), m_line.group(3)
            clean_lines.append({
                "key": code_key,
                "num": num_label,
                "text": strip_slashes_and_time(span_inner),
            })

        items[str(kb_id)] = {
            "id": kb_id,
            "title": title,
            "badge": badge,
            "subtitle": subtitle,
            "links": links,
            "logic": logic,
            "sentences": [x["text"] for x in clean_lines],
            "sentence_meta": [{"key": x["key"], "num": x["num"]} for x in clean_lines],
            "toc_html": toc_html,
            "mat_html": mat_html,
            "sec_html": sec_html,
        }

    data = {
        "version": "2.0-ssot",
        "total_scripts": len(all_ids),
        "min_id": min(all_ids),
        "max_id": max(all_ids),
        "items": items,
    }
    with open(DATA_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(DATA_JSON_COPY, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return data


def inject_markers_and_auto_batch_js(html: str) -> str:
    """Gắn 3 cặp Markers (TOC, MATRIX, SECTIONS) và nâng cấp JS sang Auto-Batching động."""
    if TOC_START not in html:
        toc_m = list(re.finditer(r'[ \t]*<li><a href="#prompter-kb(\d+)"[^>]*>.*?</a></li>', html))
        html = html[:toc_m[0].start()] + f"            {TOC_START}\n" + html[toc_m[0].start():toc_m[-1].end()] + f"\n            {TOC_END}" + html[toc_m[-1].end():]

    if MAT_START not in html:
        mat_m = list(re.finditer(r'[ \t]*<tr>\s*<td><strong><a href="#prompter-kb(\d+)">.*?</tr>', html, flags=re.S))
        html = html[:mat_m[0].start()] + f"          {MAT_START}\n" + html[mat_m[0].start():mat_m[-1].end()] + f"\n          {MAT_END}" + html[mat_m[-1].end():]

    if SEC_START not in html:
        sec_m = list(re.finditer(r'[ \t]*(?:<!--[^\n]*-->\s*)*<section id="prompter-kb(\d+)".*?</section>', html, flags=re.S))
        html = html[:sec_m[0].start()] + f"      {SEC_START}\n" + html[sec_m[0].start():sec_m[-1].end()] + f"\n      {SEC_END}" + html[sec_m[-1].end():]

    # Upgrade hardcoded batchDefs and batches in JS to dynamic 20-script chunking for KB >= 121
    old_toc_batch_block = re.search(
        r"const batchDefs = \[.*?\];",
        html,
        flags=re.S,
    )
    new_toc_batch_block = """const batchDefs = [];
        for (let start = Math.floor((maxNum - 121) / 20) * 20 + 121; start >= 121; start -= 20) {
          const end = Math.min(start + 19, maxNum);
          const isLatest = (end === maxNum);
          const lotIdx = Math.floor((start - 121) / 20) + 1;
          batchDefs.push({
            label: (isLatest ? '🚀 Lô Mới Nhất' : '🔥 Lô Thực Chiến Ngành ' + lotIdx) + ': KB ' + start + ' – KB ' + end,
            min: start,
            max: isLatest ? 9999 : end,
            open: isLatest
          });
        }
        batchDefs.push(
          { label: '🔥 Lô Podcast Vĩ Mô 4: KB 110 – KB 120', min: 110, max: 120, open: false },
          { label: '🔥 Lô Podcast Vĩ Mô 3: KB 90 – KB 109', min: 90, max: 109, open: false },
          { label: '⚡ Lô Podcast Vĩ Mô 2: KB 80 – KB 89', min: 80, max: 89, open: false },
          { label: '🎙️ Lô Podcast Vĩ Mô: KB 60 – KB 79', min: 60, max: 79, open: false },
          { label: '⚡ Lô Thực Chiến 2: KB 40 – KB 59', min: 40, max: 59, open: false },
          { label: '📦 Lô Thực Chiến 1: KB 20 – KB 39', min: 20, max: 39, open: false },
          { label: '🌱 Lô Nền Tảng: KB 04 – KB 19', min: 4, max: 19, open: false }
        );"""
    if old_toc_batch_block:
        html = html.replace(old_toc_batch_block.group(0), new_toc_batch_block, 1)

    old_top_batches = re.search(
        r"// Build dynamic batches\s*const batches = \[\];.*?batches\.push\(\{ id: 'all'",
        html,
        flags=re.S,
    )
    new_top_batches = """// Build dynamic batches automatically (no manual edits needed when adding/removing KBs)
      const batches = [];
      for (let start = Math.floor((maxNum - 121) / 20) * 20 + 121; start >= 121; start -= 20) {
        const end = Math.min(start + 19, maxNum);
        const count = kbItems.filter(x => x.num >= start && x.num <= end).length;
        if (count > 0) {
          const isLatest = (end === maxNum);
          batches.push({
            id: 'b' + start,
            label: (isLatest ? '🚀 Mới nhất: KB ' : '🔥 Lô KB ') + start + '–' + end + ' (' + count + ')',
            min: start,
            max: end
          });
        }
      }
      batches.push({ id: 'b110', label: '🔥 Lô KB 110–120 (11)', min: 110, max: 120 });
      batches.push({ id: 'b90', label: '🔥 Lô KB 90–109 (20)', min: 90, max: 109 });
      batches.push({ id: 'b80', label: '⚡ Lô KB 80–89 (10)', min: 80, max: 89 });
      batches.push({ id: 'b60', label: '🎙️ Lô KB 60–79 (20)', min: 60, max: 79 });
      batches.push({ id: 'b40', label: '⚡ Lô KB 40–59 (20)', min: 40, max: 59 });
      batches.push({ id: 'b20', label: '📦 Lô KB 20–39 (20)', min: 20, max: 39 });
      batches.push({ id: 'b04', label: '🌱 Lô KB 04–19 (13)', min: 4, max: 19 });
      batches.push({ id: 'all'"""
    if old_top_batches:
        html = html.replace(old_top_batches.group(0), new_top_batches, 1)

    return html


def load_data() -> Dict:
    if not os.path.exists(DATA_JSON_PATH):
        return extract_from_html_to_json()
    with open(DATA_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data: Dict) -> None:
    all_ids = sorted(int(k) for k in data["items"].keys())
    data["total_scripts"] = len(all_ids)
    data["min_id"] = min(all_ids) if all_ids else 4
    data["max_id"] = max(all_ids) if all_ids else 4
    with open(DATA_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(DATA_JSON_COPY, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def rebuild_item_html(item: Dict) -> None:
    """Cập nhật lại toc_html, mat_html, sec_html của 1 item khi sửa title, logic, links hoặc 14 câu."""
    kb_id = int(item["id"])
    pad = f"{kb_id:02d}" if kb_id < 10 else str(kb_id)
    title = item["title"]
    subtitle = item.get("subtitle", "Chạm từng câu để gạch dấu khi quay")
    badge = item.get("badge", f"🔥 KỊCH BẢN {kb_id} (CLAUDE2 OPUS 5.5 • 2 HOOK • BODY 6 CÂU • 2 CTA)")
    links = item.get("links", [])
    sents = item.get("sentences", [])
    logic = item.get("logic", "")

    # 1. TOC HTML
    item["toc_html"] = (
        f'            <li><a href="#prompter-kb{kb_id}" class="ink-toc-link is-active">'
        f'↳ 🔥 KB {pad}: {title} (2 Hook + Body + 2 CTA)</a></li>'
    )

    # 2. If item already has sec_html/mat_html and sentences count matches, update in-place or build fresh
    slashed_sents = [add_breathing_slashes(s) for s in sents]

    if len(sents) == 14 and (not item.get("sec_html") or item.get("_rebuild_full")):
        badges_html = "\n                ".join(
            render_link_badge(x["label"], x["url"], x.get("kind", "kho")) for x in links
        )
        matrix_links_html = " • ".join(
            f'<a href="{x["url"]}" target="_blank" rel="noopener" style="display:inline-block; font-size:0.76rem; font-weight:600; margin-right:6px; text-decoration:underline;">{x["label"]}</a>'
            for x in links
        )
        matrix_pain = item.get("matrix_pain") or f"{sents[0]}<br/>Vướng: {sents[1]}"
        matrix_base = item.get("matrix_base") or sents[9]
        matrix_high = item.get("matrix_high") or f"Lớp Offline 2 ngày tại Hà Nội: {sents[10]} {sents[12]}"
        if not logic:
            logic = f"{sents[4]} — {sents[5]}"
            item["logic"] = logic

        item["mat_html"] = f"""          <tr>
            <td><strong><a href="#prompter-kb{kb_id}">🔥 KB {pad}</a></strong><br><em>"{title}"</em><br><code>2 Hook · 6 Body · 2 CTA</code></td>
            <td>{matrix_pain}<div style="margin-top:6px; padding-top:6px; border-top:1px dashed #cbd5e1; font-size:0.78rem; line-height:1.45;"><strong>🔗 Nguồn &amp; Logic:</strong> {matrix_links_html}<br><span style="color:#475569;">{logic}</span></div></td>
            <td>{matrix_base}</td>
            <td>{matrix_high}</td>
          </tr>"""

        item["sec_html"] = f"""      <!-- KỊCH BẢN {kb_id} -->
      <section id="prompter-kb{kb_id}" class="clean-prompter" style="border: 3px solid #0f172a; background: #ffffff; box-shadow: 0 12px 28px rgba(15, 23, 42, 0.1);">
        <div class="clean-prompter-header">
          <div>
            <span class="s-badge s-dark" style="margin-bottom: 0.35rem; display: inline-block;">{badge}</span>
            <div style="font-size: 1.08rem; font-weight: 700;">🎙️ KB {pad}: "{title}"</div>
            <div style="font-size: 0.82rem; color: var(--ink-muted);">{subtitle}</div>
            <div class="kb-ref-box" style="margin-top: 0.55rem; padding: 0.55rem 0.75rem; background: #f8fafc; border-left: 3px solid #0f172a; border-radius: 6px; font-size: 0.82rem; line-height: 1.5; color: #334155;">
              <div style="display:flex; flex-wrap:wrap; align-items:center; gap:0.45rem; margin-bottom:0.3rem;">
                <strong style="color:#0f172a;">🔗 Tài liệu gốc &amp; Hồ sơ đối chiếu (Bấm mở trực tiếp):</strong>
                {badges_html}
              </div>
              <div><strong>💡 Logic &amp; Cách tiếp cận:</strong> {logic}</div>
            </div>
          </div>
          <button class="s-btn" onclick="resetPrompter('kb{kb_id}')">🔄 Xóa dấu gạch</button>
        </div>

        <div class="clean-phase-divider" style="background: #eff6ff; color: #1e40af;">PHẦN 1A • 🎯 HOOK A · HIỆN TRƯỜNG &amp; ĐẠO CỤ THẬT TẠI TIỆM</div>
        <div class="clean-line" data-kb{kb_id}="a1" onclick="this.classList.toggle('is-done')"><span class="clean-num">A1</span><span>{slashed_sents[0][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[0][1]})</code></span></div>
        <div class="clean-line" data-kb{kb_id}="a2" onclick="this.classList.toggle('is-done')"><span class="clean-num">A2</span><span>{slashed_sents[1][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[1][1]})</code></span></div>

        <div class="clean-phase-divider" style="background: #fef3c7; color: #92400e;">PHẦN 1B • 🔄 HOOK B · ĐIỂM GÃY KHIẾN KHÁCH XEM XONG RỒI IM LẶNG</div>
        <div class="clean-line" data-kb{kb_id}="b1" onclick="this.classList.toggle('is-done')"><span class="clean-num">B1</span><span>{slashed_sents[2][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[2][1]})</code></span></div>
        <div class="clean-line" data-kb{kb_id}="b2" onclick="this.classList.toggle('is-done')"><span class="clean-num">B2</span><span>{slashed_sents[3][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[3][1]})</code></span></div>

        <div class="clean-phase-divider">PHẦN 2 (BODY 6 CÂU) • 💬 PHẦN THÂN · CƠ CHẾ TÂM LÝ, THAO TÁC VẬT LÝ &amp; ẨN DỤ SÁT NGÀNH</div>
        <div class="clean-line" data-kb{kb_id}="1" onclick="this.classList.toggle('is-done')"><span class="clean-num">01</span><span>{slashed_sents[4][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[4][1]})</code></span></div>
        <div class="clean-line" data-kb{kb_id}="2" onclick="this.classList.toggle('is-done')"><span class="clean-num">02</span><span>{slashed_sents[5][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[5][1]})</code></span></div>
        <div class="clean-line" data-kb{kb_id}="3" onclick="this.classList.toggle('is-done')"><span class="clean-num">03</span><span>{slashed_sents[6][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[6][1]})</code></span></div>
        <div class="clean-line" data-kb{kb_id}="4" onclick="this.classList.toggle('is-done')"><span class="clean-num">04</span><span>{slashed_sents[7][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[7][1]})</code></span></div>
        <div class="clean-line" data-kb{kb_id}="5" onclick="this.classList.toggle('is-done')"><span class="clean-num">05</span><span>{slashed_sents[8][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[8][1]})</code></span></div>
        <div class="clean-line" data-kb{kb_id}="6" onclick="this.classList.toggle('is-done')"><span class="clean-num">06</span><span>{slashed_sents[9][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[9][1]})</code></span></div>

        <div class="clean-phase-divider" style="background: #f1f5f9;">PHẦN 3A • 📩 CTA 1 · BẮT BỆNH HỘP THƯ &amp; GÓC QUAY TẠI LỚP HAI NGÀY HÀ NỘI</div>
        <div class="clean-line" data-kb{kb_id}="c1_1" onclick="this.classList.toggle('is-done')"><span class="clean-num">C1.1</span><span>{slashed_sents[10][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[10][1]})</code></span></div>
        <div class="clean-line" data-kb{kb_id}="c1_2" onclick="this.classList.toggle('is-done')"><span class="clean-num">C1.2</span><span>{slashed_sents[11][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[11][1]})</code></span></div>

        <div class="clean-phase-divider" style="background: #f1f5f9;">PHẦN 3B • 🎯 CTA 2 · ĐẢO NGƯỢC RỦI RO &amp; CẦM BÀI MẪU VỀ TIỆM DÙNG NGAY</div>
        <div class="clean-line" data-kb{kb_id}="c2_1" onclick="this.classList.toggle('is-done')"><span class="clean-num">C2.1</span><span>{slashed_sents[12][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[12][1]})</code></span></div>
        <div class="clean-line" data-kb{kb_id}="c2_2" onclick="this.classList.toggle('is-done')"><span class="clean-num">C2.2</span><span>{slashed_sents[13][0]} <code style="font-size:0.7em; color:var(--ink-muted);">({slashed_sents[13][1]})</code></span></div>
      </section>"""
        item.pop("_rebuild_full", None)
    else:
        # Update title and sentences in existing mat_html and sec_html
        item["mat_html"] = re.sub(
            r'(<td><strong><a href="#prompter-kb\d+">[^<]+</a></strong><br><em>)"[^"]*"(</em>)',
            rf'\1"{title}"\2',
            item.get("mat_html", ""),
        )
        item["sec_html"] = re.sub(
            r'(🎙️\s*KB\s*0?\d+\s*:\s*)"[^"]*"',
            rf'\1"{title}"',
            item.get("sec_html", ""),
        )
        # Replace clean-line contents if sentence count matches
        meta_list = item.get("sentence_meta", [])
        if len(slashed_sents) == len(meta_list):
            sec_s = item["sec_html"]
            for (slashed_txt, sec_str), meta_obj in zip(slashed_sents, meta_list):
                k = re.escape(meta_obj["key"])
                n_lbl = re.escape(meta_obj["num"])
                pattern = rf'(<div class="clean-line"[^>]*data-kb{kb_id}="{k}"[^>]*><span class="clean-num">{n_lbl}</span><span>).*?(</span></div>)'
                replacement = rf'\g<1>{slashed_txt} <code style="font-size:0.7em; color:var(--ink-muted);">({sec_str})</code>\g<2>'
                sec_s = re.sub(pattern, replacement, sec_s, count=1, flags=re.S)
            item["sec_html"] = sec_s


def build_all_html(data: Dict, push: bool = False) -> None:
    """Biên dịch toàn bộ 4 file HTML từ kb3k4_data.json thông qua Markers."""
    sorted_ids = sorted(int(k) for k in data["items"].keys())
    total_count = len(sorted_ids)
    max_id = max(sorted_ids) if sorted_ids else 4

    toc_block = "\n".join(data["items"][str(i)]["toc_html"] for i in sorted_ids)
    mat_block = "\n".join(data["items"][str(i)]["mat_html"] for i in sorted_ids)
    sec_block = "\n\n".join(data["items"][str(i)]["sec_html"] for i in sorted_ids)

    with open(TARGET_HTML_FILES[0], "r", encoding="utf-8") as f:
        html = f.read()

    html = inject_markers_and_auto_batch_js(html)

    # Replace between markers
    html = re.sub(
        rf"{re.escape(TOC_START)}.*?{re.escape(TOC_END)}",
        f"{TOC_START}\n{toc_block}\n            {TOC_END}",
        html,
        flags=re.S,
    )
    html = re.sub(
        rf"{re.escape(MAT_START)}.*?{re.escape(MAT_END)}",
        f"{MAT_START}\n{mat_block}\n          {MAT_END}",
        html,
        flags=re.S,
    )
    html = re.sub(
        rf"{re.escape(SEC_START)}.*?{re.escape(SEC_END)}",
        f"{SEC_START}\n{sec_block}\n      {SEC_END}",
        html,
        flags=re.S,
    )

    # Update total counts dynamically
    html = re.sub(
        r"Bộ \d+ Kịch bản Phổ rộng chạy cùng \"Món Quà\" \(KB 04 – KB \d+\)",
        f'Bộ {total_count} Kịch bản Phổ rộng chạy cùng "Món Quà" (KB 04 – KB {max_id})',
        html,
    )
    html = re.sub(
        r"Bộ \d+ Kịch bản Quảng cáo Phổ rộng chạy song song cùng kịch bản \"Món Quà\" \(KB 04 – KB \d+\)",
        f'Bộ {total_count} Kịch bản Quảng cáo Phổ rộng chạy song song cùng kịch bản "Món Quà" (KB 04 – KB {max_id})',
        html,
    )
    html = re.sub(
        r"<strong>\d+ kịch bản phổ rộng dưới đây",
        f"<strong>{total_count} kịch bản phổ rộng dưới đây",
        html,
    )

    for path in TARGET_HTML_FILES:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ Đã đồng bộ: {path} ({len(html):,} bytes | {total_count} kịch bản, KB 04 – KB {max_id})")

    if push:
        for repo_dir in [COURSE_DIR, REPO_K_DIR]:
            subprocess.run(
                ["git", "add", "kb3k4.html", "kichban-quangcao-k4.html", "kb3k4_data.json"],
                cwd=repo_dir,
                check=False,
            )
            subprocess.run(
                ["git", "commit", "-m", f"chore(kb3k4): sync {total_count} scripts (KB 04 - KB {max_id}) via kb3k4_cli.py"],
                cwd=repo_dir,
                check=False,
            )
            subprocess.run(["git", "push"], cwd=repo_dir, check=True)
            print(f"🚀 Đã git push thành công repo: {repo_dir}")


def cmd_list(args: argparse.Namespace) -> None:
    data = load_data()
    q = (args.q or "").lower().strip()
    count = 0
    for kb_id in sorted(int(k) for k in data["items"].keys()):
        item = data["items"][str(kb_id)]
        haystack = f"kb {kb_id} {item['title']} {item.get('subtitle', '')} {' '.join(item.get('sentences', []))}".lower()
        if q and q not in haystack:
            continue
        count += 1
        print(f"  • KB {kb_id:03d} ({len(item.get('sentences', []))} câu): {item['title']}")
    print(f"\n📊 Tổng cộng: {count} / {data['total_scripts']} kịch bản (KB {data['min_id']:02d} – KB {data['max_id']}).")


def cmd_show(args: argparse.Namespace) -> None:
    data = load_data()
    key = str(args.id)
    if key not in data["items"]:
        sys.exit(f"❌ Không tìm thấy KB {key} trong kho.")
    item = data["items"][key]
    print(f"=== 🎙️ KB {item['id']}: \"{item['title']}\" ===")
    print(f"📌 Badge:    {item.get('badge', '')}")
    print(f"📌 Subtitle: {item.get('subtitle', '')}")
    print(f"💡 Logic:    {item.get('logic', '')}")
    print("🔗 Links:")
    for lk in item.get("links", []):
        print(f"   - [{lk.get('kind')}] {lk.get('label')} -> {lk.get('url')}")
    print(f"\n📝 Nội dung ({len(item.get('sentences', []))} câu):")
    for idx, (s, m_info) in enumerate(zip(item.get("sentences", []), item.get("sentence_meta", [])), 1):
        print(f"  {idx:02d} [{m_info.get('num', idx)}]: {s}")


def cmd_update(args: argparse.Namespace) -> None:
    data = load_data()
    key = str(args.id)
    if key not in data["items"]:
        sys.exit(f"❌ Không tìm thấy KB {key} trong kho. Dùng lệnh `add` nếu muốn thêm bài mới.")
    item = data["items"][key]

    if args.title:
        item["title"] = args.title.strip().upper()
    if args.subtitle:
        item["subtitle"] = args.subtitle.strip()
    if args.logic:
        item["logic"] = args.logic.strip()
    if args.line:
        line_idx, new_text = int(args.line[0]), args.line[1].strip()
        sents = item.get("sentences", [])
        if not (1 <= line_idx <= len(sents)):
            sys.exit(f"❌ Số dòng phải từ 1 đến {len(sents)} (nhận được: {line_idx}).")
        sents[line_idx - 1] = new_text
        item["sentences"] = sents
    if args.bai_file:
        with open(args.bai_file, "r", encoding="utf-8") as f:
            lines = [re.sub(r"^\d+\.\s*", "", ln.strip()) for ln in f.read().strip().splitlines() if ln.strip() and not ln.strip().startswith("#")]
        if not args.skip_verify and os.path.exists(VERIFY_VOICE_SCRIPT):
            res = subprocess.run(
                ["python3", VERIFY_VOICE_SCRIPT, args.bai_file, "--mode", "thoai"],
                capture_output=True,
                text=True,
            )
            if res.returncode != 0:
                sys.exit(f"❌ File {args.bai_file} trượt cổng verify_voice.py:\n{res.stdout}\n{res.stderr}")
        item["sentences"] = lines
        if len(lines) == 14:
            item["sentence_meta"] = [
                {"key": "a1", "num": "A1"}, {"key": "a2", "num": "A2"},
                {"key": "b1", "num": "B1"}, {"key": "b2", "num": "B2"},
                {"key": "1", "num": "01"}, {"key": "2", "num": "02"},
                {"key": "3", "num": "03"}, {"key": "4", "num": "04"},
                {"key": "5", "num": "05"}, {"key": "6", "num": "06"},
                {"key": "c1_1", "num": "C1.1"}, {"key": "c1_2", "num": "C1.2"},
                {"key": "c2_1", "num": "C2.1"}, {"key": "c2_2", "num": "C2.2"},
            ]

    rebuild_item_html(item)
    save_data(data)
    build_all_html(data, push=args.push)
    print(f"✅ Đã cập nhật thành công KB {key}: \"{item['title']}\"")


def cmd_add(args: argparse.Namespace) -> None:
    data = load_data()
    key = str(args.id)
    with open(args.bai_file, "r", encoding="utf-8") as f:
        lines = [re.sub(r"^\d+\.\s*", "", ln.strip()) for ln in f.read().strip().splitlines() if ln.strip() and not ln.strip().startswith("#")]
    assert len(lines) == 14, f"File {args.bai_file} phải có đúng 14 câu (hiện có {len(lines)} câu)"

    if not args.skip_verify and os.path.exists(VERIFY_VOICE_SCRIPT):
        res = subprocess.run(
            ["python3", VERIFY_VOICE_SCRIPT, args.bai_file, "--mode", "thoai"],
            capture_output=True,
            text=True,
        )
        if res.returncode != 0:
            sys.exit(f"❌ File {args.bai_file} trượt cổng verify_voice.py:\n{res.stdout}\n{res.stderr}")

    links = []
    if args.links_json:
        links = json.loads(args.links_json)
    else:
        links = [
            {"label": "📚 Kho AI: Hệ thống kiến thức xây kênh thực chiến ↗", "url": "https://kho.fedu.vn", "kind": "kho"},
            {"label": "📊 Hồ sơ STU: Kho báo cáo khám kênh học viên ↗", "url": "https://stu.fedu.vn", "kind": "stu"},
        ]

    item = {
        "id": int(args.id),
        "title": args.title.strip().upper(),
        "badge": f"🔥 KỊCH BẢN {args.id} (CLAUDE2 OPUS 5.5 • {args.pillar.upper()} • 2 HOOK • BODY 6 CÂU • 2 CTA)",
        "subtitle": args.subtitle or "Ngành thực chiến • Chạm từng câu để gạch dấu khi quay",
        "links": links,
        "logic": args.logic or f"{lines[4]} — {lines[5]}",
        "sentences": lines,
        "sentence_meta": [
            {"key": "a1", "num": "A1"}, {"key": "a2", "num": "A2"},
            {"key": "b1", "num": "B1"}, {"key": "b2", "num": "B2"},
            {"key": "1", "num": "01"}, {"key": "2", "num": "02"},
            {"key": "3", "num": "03"}, {"key": "4", "num": "04"},
            {"key": "5", "num": "05"}, {"key": "6", "num": "06"},
            {"key": "c1_1", "num": "C1.1"}, {"key": "c1_2", "num": "C1.2"},
            {"key": "c2_1", "num": "C2.1"}, {"key": "c2_2", "num": "C2.2"},
        ],
        "_rebuild_full": True,
    }
    rebuild_item_html(item)
    data["items"][key] = item
    save_data(data)
    build_all_html(data, push=args.push)
    print(f"✅ Đã thêm mới thành công KB {key}: \"{item['title']}\"")


def cmd_delete(args: argparse.Namespace) -> None:
    data = load_data()
    removed = []
    for raw_id in args.ids:
        k = str(raw_id)
        if k in data["items"]:
            removed.append((k, data["items"][k]["title"]))
            del data["items"][k]
        else:
            print(f"⚠️ Bỏ qua KB {k} (không tồn tại).")
    if not removed:
        sys.exit("❌ Không có kịch bản nào bị xóa.")
    save_data(data)
    build_all_html(data, push=args.push)
    for k, t in removed:
        print(f"🗑️ Đã xóa sạch KB {k} (\"{t}\") khỏi TOC + Bảng Ma Trận + Prompter trên cả 4 file HTML.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Trình quản trị tập trung Bộ Kịch Bản K4 (Thêm / Sửa / Xóa / Build / Push)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Trích xuất kb3k4_data.json từ HTML hiện tại và gắn Markers + Auto-Batching JS")
    p_init.add_argument("--push", action="store_true", help="Tự động git push sau khi khởi tạo")

    p_list = sub.add_parser("list", help="Liệt kê hoặc tìm kiếm nhanh kịch bản")
    p_list.add_argument("--q", help="Từ khóa tìm kiếm theo tiêu đề hoặc nội dung")

    p_show = sub.add_parser("show", help="Xem chi tiết 1 kịch bản")
    p_show.add_argument("id", type=int, help="Mã số kịch bản (ví dụ: 142)")

    p_exp = sub.add_parser("export-md", help="Xuất 14 câu sạch của 1 kịch bản ra file .md để sửa nhanh")
    p_exp.add_argument("id", type=int, help="Mã số kịch bản (ví dụ: 142)")
    p_exp.add_argument("--out", help="Đường dẫn file .md xuất ra (mặc định in ra màn hình)")

    p_upd = sub.add_parser("update", help="Sửa tiêu đề, phụ đề, logic hoặc 14 câu thoại của 1 kịch bản")
    p_upd.add_argument("id", type=int, help="Mã số kịch bản cần sửa")
    p_upd.add_argument("--title", help="Tiêu đề mới")
    p_upd.add_argument("--subtitle", help="Phụ đề đạo cụ mới")
    p_upd.add_argument("--logic", help="Giải thích logic mới")
    p_upd.add_argument("--line", nargs=2, metavar=("LINE_NUM", "NEW_TEXT"), help="Sửa nhanh 1 dòng cụ thể (1..14), ví dụ: --line 9 'Câu ẩn dụ mới'")
    p_upd.add_argument("--bai-file", help="Đường dẫn file .md chứa 14 câu mới")
    p_upd.add_argument("--skip-verify", action="store_true", help="Bỏ qua kiểm tra verify_voice.py")
    p_upd.add_argument("--push", action="store_true", help="Tự động git push cả 2 repo sau khi sửa")

    p_add = sub.add_parser("add", help="Thêm 1 kịch bản mới vào kho")
    p_add.add_argument("--id", type=int, required=True, help="Mã số kịch bản mới (ví dụ: 181)")
    p_add.add_argument("--title", required=True, help="Tiêu đề kịch bản")
    p_add.add_argument("--bai-file", required=True, help="Đường dẫn file .md chứa 14 câu")
    p_add.add_argument("--subtitle", help="Phụ đề ngành & đạo cụ")
    p_add.add_argument("--pillar", default="TRỤ CỘT B: BẮT LỖI KHUNG HÌNH THEO NGÀNH", help="Nhãn trụ cột")
    p_add.add_argument("--logic", help="Đoạn giải thích logic")
    p_add.add_argument("--links-json", help="Chuỗi JSON mảng links")
    p_add.add_argument("--skip-verify", action="store_true", help="Bỏ qua kiểm tra verify_voice.py")
    p_add.add_argument("--push", action="store_true", help="Tự động git push sau khi thêm")

    p_del = sub.add_parser("delete", help="Xóa 1 hoặc nhiều kịch bản khỏi cả 3 khối HTML trên 4 file")
    p_del.add_argument("ids", type=int, nargs="+", help="Danh sách mã KB cần xóa (ví dụ: 181 182)")
    p_del.add_argument("--push", action="store_true", help="Tự động git push sau khi xóa")

    p_build = sub.add_parser("build", help="Biên dịch lại cả 4 file HTML từ kb3k4_data.json")
    p_build.add_argument("--push", action="store_true", help="Tự động git push cả 2 repo course & k")

    args = parser.parse_args()
    if args.cmd == "init":
        data = extract_from_html_to_json()
        build_all_html(data, push=args.push)
    elif args.cmd == "list":
        cmd_list(args)
    elif args.cmd == "show":
        cmd_show(args)
    elif args.cmd == "export-md":
        data = load_data()
        key = str(args.id)
        if key not in data["items"]:
            sys.exit(f"❌ Không tìm thấy KB {key}.")
        txt = "\n".join(data["items"][key].get("sentences", [])) + "\n"
        if args.out:
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(txt)
            print(f"✅ Đã xuất {len(data['items'][key].get('sentences', []))} câu của KB {key} ra: {args.out}")
        else:
            print(txt, end="")
    elif args.cmd == "update":
        cmd_update(args)
    elif args.cmd == "add":
        cmd_add(args)
    elif args.cmd == "delete":
        cmd_delete(args)
    elif args.cmd == "build":
        data = load_data()
        build_all_html(data, push=args.push)


if __name__ == "__main__":
    main()
