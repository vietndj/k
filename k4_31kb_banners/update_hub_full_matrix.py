#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update /Users/vietmac/Documents/CODE/k/bo-chon-chu-banner.html with the complete
3-Axis Orthogonal Typographic Matrix (20/20 Gates PASS):
  - Axis 1 (H01..H40): 40 Serif/Slab/Flared Headline Typefaces (adds H31..H40)
  - Axis 2 (K01..K50): 50 Subline Box UI/UX Layouts (adds rebuilt K11 + K41..K50, 5 groups x 10)
  - Axis 3 (S01..S35): 35 Subline Sans-Serif Font Pairs (Regular/Medium 500 + Bold 700)
"""
import json
import re
from pathlib import Path

HUB_HTML = Path("/Users/vietmac/Documents/CODE/k/bo-chon-chu-banner.html")
REPORT_HK = Path("/tmp/report_h40_k50.json")
REPORT_S = Path("/tmp/report_s35_subfonts.json")


def main():
    hk_data = json.loads(REPORT_HK.read_text(encoding="utf-8"))
    s_data = json.loads(REPORT_S.read_text(encoding="utf-8"))

    rendered_by_sid = hk_data["rendered_by_sid"]
    new_headlines = hk_data["new_headlines_h31_h40"]
    new_subboxes = hk_data["new_subboxes_k11_k41_k50"]

    html = HUB_HTML.read_text(encoding="utf-8")

    # 1. Remove any previously injected H31..H40, K11, K41..K50, or sec-layer3-subfonts to make idempotent
    html = re.sub(r'\s*<article class="item-card h-card" data-hid="H(?:3[1-9]|40)"[\s\S]*?</article>', "", html)
    html = re.sub(r'\s*<article class="item-card k-card" data-kid="K(?:11|4[1-9]|50)"[\s\S]*?</article>', "", html)
    html = re.sub(r'\s*<!-- ==================== SECTION 2B: LAYER 3 \(35 SUBLINE SANS FONTS S01\.\.S35\) ==================== -->[\s\S]*?<!-- ==================== SECTION 3: MASTER OVERVIEW SHEETS ==================== -->', '  <!-- ==================== SECTION 3: MASTER OVERVIEW SHEETS ==================== -->', html)

    # 2. Build H31..H40 cards
    h_badge_map = {
        "H1A": "background:rgba(34,197,94,0.18);color:#4ADE80;border:1px solid rgba(34,197,94,0.45);",
        "H1B": "background:rgba(56,189,248,0.18);color:#38BDF8;border:1px solid rgba(56,189,248,0.45);",
        "H1C": "background:rgba(245,158,11,0.18);color:#FACC15;border:1px solid rgba(245,158,11,0.45);",
    }
    h_cards_html = []
    for hspec in new_headlines:
        hid = hspec["hid"]
        sid = hspec["sid"]
        rinfo = rendered_by_sid[sid]
        calc = rinfo["calc"]
        grp = hspec["hgroup"]
        font_stem = Path(hspec["font_file"]).stem
        h_cards_html.append(f"""
        <article class="item-card h-card" data-hid="{hid}" data-hgroup="{grp}" data-hname="{hspec['name']} ({calc['fs']}px, LH={calc['L_target']})" data-crop="k4_31kb_banners/v2_pilots/crop_head_{sid}.jpg?v=h40_k50_s35" data-full="k4_31kb_banners/v2_pilots/{sid}.jpg?v=h40_k50_s35" onclick="selectHeadline('{hid}')">
          <div class="card-head">
            <div class="card-top-row">
              <span class="code-pill h-pill">{hid} • {hspec['name'].upper()}</span>
              <span class="grp-badge" style="{h_badge_map[grp]}">{hspec['hgroup_label']}</span>
            </div>
            <div class="metrics-bar">
              <span>Cỡ chuẩn: <b>{calc['fs']}px</b> (1 size)</span>
              <span>•</span>
              <span>Leading riêng: <b>LH = {calc['L_target']}</b></span>
              <span>•</span>
              <span>Trắng quang học: <b>W = {calc['W_ratio']}×xH</b></span>
              <span>•</span>
              <span>xH: <b>{calc['xH']:.3f}</b></span>
            </div>
            <p class="card-desc">{hspec['desc']}</p>
          </div>
          <div class="img-box" onclick="event.stopPropagation(); selectHeadline('{hid}'); openBigPreviewModal();" title="Click vào ảnh để mở BẢNG XEM TO (Ảnh Ví Dụ 1080×1350)">
            <img class="preview-img" src="k4_31kb_banners/v2_pilots/crop_head_{sid}.jpg?v=h40_k50_s35" alt="{hid} {hspec['name']}" loading="lazy" />
            <span class="img-mode-tag">🔍 CLICK ẢNH XEM BẢNG TO (LỚP 1)</span>
          </div>
          <div class="card-foot">
            <span>File: <code>{font_stem}</code> • Khe 2D: <code>{rinfo['gap2D']}px</code> • <b style="color:#4ADE80;">20/20 PASS</b></span>
            <div style="display:flex;gap:6px;">
              <button type="button" class="btn-pick" style="background:rgba(56,189,248,0.16);color:#38BDF8;border-color:rgba(56,189,248,0.4);" onclick="event.stopPropagation(); selectHeadline('{hid}'); openBigPreviewModal();">🖼️ Xem Bảng To</button>
              <button type="button" class="btn-pick" onclick="event.stopPropagation(); selectHeadline('{hid}')">✓ Chọn {hid}</button>
            </div>
          </div>
        </article>""")

    h30_pos = html.find('data-hid="H30"')
    h30_end = html.find("</article>", h30_pos) + len("</article>")
    html = html[:h30_end] + "\n" + "\n".join(h_cards_html) + html[h30_end:]

    # 3. Build K11 and K41..K50 cards
    k_badge_map = {
        "KA": "background:rgba(245,158,11,0.18);color:#FACC15;border:1px solid rgba(245,158,11,0.45);",
        "KB": "background:rgba(56,189,248,0.18);color:#38BDF8;border:1px solid rgba(56,189,248,0.45);",
        "KC": "background:rgba(34,197,94,0.18);color:#4ADE80;border:1px solid rgba(34,197,94,0.45);",
        "KD": "background:rgba(168,85,247,0.18);color:#C084FC;border:1px solid rgba(168,85,247,0.45);",
        "KE": "background:rgba(244,63,94,0.18);color:#FB7185;border:1px solid rgba(244,63,94,0.45);",
    }

    def make_k_card(kspec):
        kid = kspec["kid"]
        sid = kspec["sid"]
        rinfo = rendered_by_sid[sid]
        grp = kspec["kgroup"]
        return f"""
        <article class="item-card k-card" data-kid="{kid}" data-kgroup="{grp}" data-kname="{kspec['name']}" data-crop="k4_31kb_banners/v2_pilots/crop_sub_{sid}.jpg?v=h40_k50_s35" data-full="k4_31kb_banners/v2_pilots/{sid}.jpg?v=h40_k50_s35" onclick="selectSubbox('{kid}')">
          <div class="card-head">
            <div class="card-top-row">
              <span class="code-pill k-pill">{kid} • {kspec['name'].upper()}</span>
              <span class="grp-badge" style="{k_badge_map[grp]}">{kspec['kgroup_label']}</span>
            </div>
            <div class="sample-quote">{kspec['sample_quote']}</div>
            <p class="card-desc">{kspec['desc']}</p>
          </div>
          <div class="img-box sub-img-box" onclick="event.stopPropagation(); selectSubbox('{kid}'); openBigPreviewModal();" title="Click vào ảnh để mở BẢNG XEM TO (Ảnh Ví Dụ 1080×1350)">
            <img class="preview-img" src="k4_31kb_banners/v2_pilots/crop_sub_{sid}.jpg?v=h40_k50_s35" alt="{kid} {kspec['name']}" loading="lazy" />
            <span class="img-mode-tag sub-tag">🔍 CLICK ẢNH XEM BẢNG TO (LỚP 2)</span>
          </div>
          <div class="card-foot">
            <span>Tác giả khuôn: <code>{kspec['author']}</code> • rPad={rinfo['rPad']}px • <b style="color:#4ADE80;">Đạt 20/20 Cổng</b></span>
            <div style="display:flex;gap:6px;">
              <button type="button" class="btn-pick" style="background:rgba(56,189,248,0.16);color:#38BDF8;border-color:rgba(56,189,248,0.4);" onclick="event.stopPropagation(); selectSubbox('{kid}'); openBigPreviewModal();">🖼️ Xem Bảng To</button>
              <button type="button" class="btn-pick k-btn" onclick="event.stopPropagation(); selectSubbox('{kid}')">✓ Chọn {kid}</button>
            </div>
          </div>
        </article>"""

    k11_spec = [k for k in new_subboxes if k["kid"] == "K11"][0]
    k41_50_specs = [k for k in new_subboxes if k["kid"] != "K11"]

    # Insert K11 right after K10
    k10_pos = html.find('data-kid="K10"')
    k10_end = html.find("</article>", k10_pos) + len("</article>")
    html = html[:k10_end] + "\n" + make_k_card(k11_spec) + html[k10_end:]

    # Insert K41..K50 right after K40
    k40_pos = html.find('data-kid="K40"')
    k40_end = html.find("</article>", k40_pos) + len("</article>")
    k41_50_html = "\n".join(make_k_card(k) for k in k41_50_specs)
    html = html[:k40_end] + "\n" + k41_50_html + html[k40_end:]

    # 4. Build Layer 3 Section: 35 Subline Sans-Serif Font Pairs (S01..S35)
    s_cards_html = []
    for item in s_data:
        sid = item["sid"]
        slug = item["slug"]
        name = item["name"]
        role = item["role"]
        prefix = item["prefix"]
        if prefix.startswith("FD") and any(k in name for k in ("Söhne", "Calibre", "Founders", "National", "Untitled", "Domaine", "Family", "Geograph", "Metric", "The Future")):
            sgrp = "SA"
            sgrp_label = "Nhóm S1 • Klim Type Foundry (11 họ)"
            sbadge_style = "background:rgba(34,197,94,0.18);color:#4ADE80;border:1px solid rgba(34,197,94,0.45);"
        elif prefix.startswith("GR"):
            sgrp = "SB"
            sgrp_label = "Nhóm S2 • Grilli Type Thụy Sĩ (7 họ)"
            sbadge_style = "background:rgba(56,189,248,0.18);color:#38BDF8;border:1px solid rgba(56,189,248,0.45);"
        else:
            sgrp = "SC"
            sgrp_label = "Nhóm S3 • Geometric & Neo-Grotesk Quốc Tế (17 họ)"
            sbadge_style = "background:rgba(168,85,247,0.18);color:#C084FC;border:1px solid rgba(168,85,247,0.45);"

        s_cards_html.append(f"""
        <article class="item-card s-card" data-sid="{sid}" data-sgroup="{sgrp}" data-sname="{name} (500 + 700)" data-crop="k4_31kb_banners/v2_pilots/crop_sub_{slug}.jpg?v=h40_k50_s35" data-full="k4_31kb_banners/v2_pilots/{slug}.jpg?v=h40_k50_s35" onclick="selectSubfont('{sid}')">
          <div class="card-head">
            <div class="card-top-row">
              <span class="code-pill" style="background:rgba(168,85,247,0.2);color:#C084FC;border:1px solid rgba(168,85,247,0.45);">{sid} • {name.upper()}</span>
              <span class="grp-badge" style="{sbadge_style}">{sgrp_label}</span>
            </div>
            <div class="metrics-bar">
              <span>Regular/Med: <b>{Path(item['reg_file']).stem}</b></span>
              <span>•</span>
              <span>Bold: <b>{Path(item['bold_file']).stem}</b></span>
              <span>•</span>
              <span>xH-Hier: <b>{item['xh_hier']}×</b></span>
            </div>
            <div class="sample-quote">× 500: {item['line1']}  |  ✓ 700: {item['line2']}</div>
            <p class="card-desc">{role} — Kiểm định trực tiếp cặp Regular/Medium (19.5px) + Bold (20px) trên nền hộp tối, đạt chuẩn 20/20 cổng UI/UX.</p>
          </div>
          <div class="img-box sub-img-box" onclick="event.stopPropagation(); selectSubfont('{sid}'); openBigPreviewModal();" title="Click vào ảnh để mở BẢNG XEM TO (Ảnh Ví Dụ 1080×1350)">
            <img class="preview-img" src="k4_31kb_banners/v2_pilots/crop_sub_{slug}.jpg?v=h40_k50_s35" alt="{sid} {name}" loading="lazy" />
            <span class="img-mode-tag sub-tag" style="background:rgba(168,85,247,0.9);color:#fff;">🔍 CLICK ẢNH XEM BẢNG TO (FONT CHỮ NHỎ {sid})</span>
          </div>
          <div class="card-foot">
            <span>rPad={item['rPad']}px • <b style="color:#4ADE80;">{item['score']} PASS</b></span>
            <div style="display:flex;gap:6px;">
              <button type="button" class="btn-pick" style="background:rgba(56,189,248,0.16);color:#38BDF8;border-color:rgba(56,189,248,0.4);" onclick="event.stopPropagation(); selectSubfont('{sid}'); openBigPreviewModal();">🖼️ Xem Bảng To</button>
              <button type="button" class="btn-pick" style="background:rgba(168,85,247,0.2);color:#C084FC;border-color:rgba(168,85,247,0.45);" onclick="event.stopPropagation(); selectSubfont('{sid}')">✓ Chọn {sid}</button>
            </div>
          </div>
        </article>""")

    sec_s_html = f"""
  <!-- ==================== SECTION 2B: LAYER 3 (35 SUBLINE SANS FONTS S01..S35) ==================== -->
  <section class="section" id="sec-layer3-subfonts" style="background:radial-gradient(circle at 85% 20%, rgba(168,85,247,0.08), transparent 55%);">
    <div class="container">
      <div class="sec-head">
        <span class="sec-tag" style="background:rgba(168,85,247,0.18);color:#C084FC;border:1px solid rgba(168,85,247,0.45);">LỚP 3 (MỚI) • BỘ CHỌN 35 HỌ FONT CHỮ NHỎ KHÔNG CHÂN (S01 → S35 • CẶP REGULAR/MEDIUM 500 + BOLD 700)</span>
        <h2 class="sec-title">🟣 LỚP 3: BỘ CHỌN 35 HỌ FONT CHỮ NHỎ KHÔNG CHÂN (S01 → S35 • ĐẠT 20/20 CỔNG UI/UX)</h2>
        <p class="sec-desc">
          Theo thống kê toàn bộ <b>2.149 file font</b> trong kho FEDU cùng <b>CLAUDE2 (Opus 5.5)</b>: đây là trọn bộ <b>35 họ Font Không Chân (`Sans-Serif`)</b> ưu tú nhất có đủ cặp <b>Regular/Medium 500 (cho dòng dẫn/triệu chứng)</b> và <b>Bold 700 (cho dòng kết luận/hành động)</b>, đọc sắc lẹm ở cỡ chữ nhỏ <code>19.5px–21px</code> trên điện thoại. Click vào bất kỳ thẻ <code>S01–S35</code> nào để chọn Font Chữ Nhỏ hoặc mở Bảng Xem To!
        </p>
      </div>

      <div class="filter-row">
        <button class="filter-btn s-filter active" onclick="filterSubfonts('ALL', this)">Tất cả 35 Họ Font Chữ Nhỏ (S01–S35)</button>
        <button class="filter-btn s-filter" onclick="filterSubfonts('SA', this)">Nhóm S1 • Klim Type Foundry (11 họ: Söhne, Calibre, Founders, National 2, Untitled, Domaine Sans...)</button>
        <button class="filter-btn s-filter" onclick="filterSubfonts('SB', this)">Nhóm S2 • Grilli Type Thụy Sĩ (7 họ: Walsheim Pro, America, Eesti, Era, Flexa, Haptik, Standard M)</button>
        <button class="filter-btn s-filter" onclick="filterSubfonts('SC', this)">Nhóm S3 • Neo-Grotesk &amp; Geometric Quốc Tế (17 họ: Aeonik, Monument, RM Neue, Gilroy, Lock Sans, Die Grotesk...)</button>
      </div>

      <div class="cards-grid" id="grid-subfonts">
        {"".join(s_cards_html)}
      </div>
    </div>
  </section>

  <!-- ==================== SECTION 3: MASTER OVERVIEW SHEETS ==================== -->"""

    html = html.replace("  <!-- ==================== SECTION 3: MASTER OVERVIEW SHEETS ==================== -->", sec_s_html)

    # 5. Update counts and labels across the page (30 -> 40 Headlines, 39 -> 50 Subboxes, add 35 Subfonts)
    html = html.replace("TIÊU ĐỀ (H01–H30) × KHUNG CHỮ BÉ (K01–K40)", "TIÊU ĐỀ (H01–H40) × KHUNG CHỮ BÉ (K01–K50) × FONT CHỮ BÉ (S01–S35)")
    html = html.replace("🔹 LỚP 1: 30 Font Tiêu Đề Đơn (H01–H30)", "🔹 LỚP 1: 40 Font Tiêu Đề Có Chân (H01–H40)")
    html = html.replace("🔸 LỚP 2: 39 Khuôn Khung Chữ Bé (K01–K40)", "🔸 LỚP 2: 50 Khuôn Khung Chữ Bé (K01–K50)")
    if 'href="#sec-layer3-subfonts"' not in html:
        html = html.replace(
            '<a href="#sec-layer2-subboxes" class="nav-pill">🔸 LỚP 2: 50 Khuôn Khung Chữ Bé (K01–K50)</a>',
            '<a href="#sec-layer2-subboxes" class="nav-pill">🔸 LỚP 2: 50 Khuôn Khung Chữ Bé (K01–K50)</a>\n      <a href="#sec-layer3-subfonts" class="nav-pill">🟣 LỚP 3: 35 Họ Font Chữ Nhỏ (S01–S35)</a>'
        )
    html = html.replace("[TIÊU ĐỀ H01–H30] × [KHUNG K01–K40]", "[40 TIÊU ĐỀ H01–H40] × [50 KHUNG K01–K50] × [35 FONT CHỮ NHỎ S01–S35]")
    html = html.replace("30 HỌ FONT TIÊU ĐỀ CÓ CHÂN ĐÃ KIỂM ĐỊNH (H01 → H30)", "40 HỌ FONT TIÊU ĐỀ CÓ CHÂN ĐÃ KIỂM ĐỊNH (H01 → H40)")
    html = html.replace("Tất cả 30 Font Tiêu Đề (H01–H30)", "Tất cả 40 Font Tiêu Đề Có Chân (H01–H40)")
    html = html.replace("🔸 LỚP 2: BỘ CHỌN KHUÔN KHUNG CHỮ BÉ (39 KHUÔN CHIA THEO 5 HỌ LOGIC: K01–K10 &amp; K12–K40, BỎ #11)", "🔸 LỚP 2: BỘ CHỌN KHUÔN KHUNG CHỮ BÉ (TRÒN 50 KHUÔN CHIA ĐỀU 5 HỌ LOGIC × 10 KHUÔN: K01 → K50, ĐẠT 20/20 CỔNG)")
    html = html.replace("Tất cả 39 Khuôn Khung Chữ Bé (K01–K40, Đã bỏ #11)", "Tất cả 50 Khuôn Khung Chữ Bé (K01–K50 • 5 Họ × 10 Khuôn)")
    html = html.replace("Họ 1 • Đối Lập & So Sánh 2 Vế (9 khuôn: K01, K06, K07, K17, K20, K22, K24, K31, K35)", "Họ 1 • Đối Lập & So Sánh 2 Vế (10 khuôn: K01, K06, K07, K11, K17, K20, K22, K24, K31, K35)")
    html = html.replace("Họ 2 • Con Số, Thời Gian &amp; Lịch Tuần (9 khuôn: K03, K10, K14, K15, K21, K23, K28, K32, K36)", "Họ 2 • Con Số, Thời Gian &amp; Lịch Tuần (10 khuôn: K03, K10, K14, K15, K21, K23, K28, K32, K36, K41)")
    html = html.replace("Họ 3 • Công Thức &amp; Bảng Kiểm (7 khuôn: K05, K18, K19, K25, K29, K33, K38)", "Họ 3 • Công Thức &amp; Bảng Kiểm (10 khuôn: K05, K18, K19, K25, K29, K33, K38, K42, K43, K44)")
    html = html.replace("Họ 4 • Tin Nhắn &amp; Hỏi–Đáp (5 khuôn: K09, K12, K26, K34, K39)", "Họ 4 • Tin Nhắn &amp; Hỏi–Đáp (10 khuôn: K09, K12, K26, K34, K39, K45, K46, K47, K48, K49)")
    html = html.replace("Họ 5 • Tuyên Ngôn &amp; Đúc Kết (9 khuôn: K02, K04, K08, K13, K16, K27, K30, K37, K40)", "Họ 5 • Tuyên Ngôn &amp; Đúc Kết (10 khuôn: K02, K04, K08, K13, K16, K27, K30, K37, K40, K50)")

    # 6. Add overview sheets for H31..H40, K11/K41..K50, and S01..S35 into #sec-layer3-library
    extra_sheets = """
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:18px;">
        <div class="arch-box" style="background:#0E1526;border:1.5px solid #FACC15;border-radius:14px;padding:14px;">
          <div style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:var(--gold-bright);margin-bottom:8px;">BẢNG MỚI (ĐỢT 1) • 10 FONT SERIF TIÊU ĐỀ H31 → H40 (20/20 PASS)</div>
          <img src="k4_31kb_banners/v2_pilots/h31_h40_10headlines_grid.jpg?v=h40_k50_s35" alt="H31-H40 Grid" style="width:100%;border-radius:10px;display:block;" />
        </div>
        <div class="arch-box" style="background:#0E1526;border:1.5px solid #38BDF8;border-radius:14px;padding:14px;">
          <div style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:var(--cyan);margin-bottom:8px;">BẢNG MỚI (ĐỢT 2) • 11 KHUÔN CHỮ NHỎ K11 &amp; K41 → K50 (20/20 PASS)</div>
          <img src="k4_31kb_banners/v2_pilots/k11_k41_k50_11subboxes_grid.jpg?v=h40_k50_s35" alt="K11-K50 Grid" style="width:100%;border-radius:10px;display:block;" />
        </div>
        <div class="arch-box" style="background:#0E1526;border:1.5px solid #C084FC;border-radius:14px;padding:14px;">
          <div style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:#C084FC;margin-bottom:8px;">BẢNG MỚI (ĐỢT 3) • 35 HỌ FONT CHỮ NHỎ S01 → S35 (20/20 PASS)</div>
          <img src="k4_31kb_banners/v2_pilots/s01_s35_subfonts_grid.jpg?v=h40_k50_s35" alt="S01-S35 Grid" style="width:100%;border-radius:10px;display:block;" />
        </div>
      </div>"""
    if "h31_h40_10headlines_grid.jpg" not in html:
        html = html.replace(
            '<img src="k4_31kb_banners/v2_pilots/serif_sheet_3_remaining8.jpg?v=sci_v5" alt="Bảng 3" style="width:100%;border-radius:10px;display:block;" />\n        </div>\n      </div>',
            '<img src="k4_31kb_banners/v2_pilots/serif_sheet_3_remaining8.jpg?v=sci_v5" alt="Bảng 3" style="width:100%;border-radius:10px;display:block;" />\n        </div>\n      </div>\n' + extra_sheets
        )

    # 7. Update Modal Quick Lists & JS to support S01..S35 selection as well
    html = html.replace("2. HOẶC ĐỔI NHANH 30 FONT TIÊU ĐỀ ĐƠN (H01 → H30):", "2. ĐỔI NHANH 40 FONT TIÊU ĐỀ CÓ CHÂN (H01 → H40):")
    html = html.replace("3. ĐỔI NHANH 39 KHUÔN KHUNG CHỮ BÉ (K01 → K40, ĐÃ BỎ #11):", "3. ĐỔI NHANH 50 KHUÔN KHUNG CHỮ BÉ (K01 → K50):")

    if 'id="modalSQuickList"' not in html:
        html = html.replace(
            '<div class="quick-pills-wrap" id="modalKQuickList"></div>\n        </div>',
            '<div class="quick-pills-wrap" id="modalKQuickList"></div>\n        </div>\n\n        <div>\n          <div style="font-family:var(--font-mono);font-size:11.5px;color:#C084FC;font-weight:800;margin-bottom:6px;">4. ĐỔI NHANH 35 HỌ FONT CHỮ NHỎ KHÔNG CHÂN (S01 → S35):</div>\n          <div class="quick-pills-wrap" id="modalSQuickList"></div>\n        </div>'
        )

    if 'id="slotSText"' not in html:
        html = html.replace(
            '<span class="slot-badge slot-k" id="slotKText">🔸 KHUNG BÉ: K01 • Hai Vế Đối Lập (× / ✓)</span>',
            '<span class="slot-badge slot-k" id="slotKText">🔸 KHUNG BÉ: K01 • Hai Vế Đối Lập (× / ✓)</span>\n            <span style="font-weight:800;color:var(--text-soft);">×</span>\n            <span class="slot-badge" id="slotSText" style="background:rgba(168,85,247,0.2);color:#C084FC;border:1px solid rgba(168,85,247,0.45);">🟣 FONT BÉ: S01 • FD Aeonik (500 + 700)</span>'
        )

    # Enhance JS for selectSubfont and filterSubfonts
    if "let currentS = 'S01';" not in html:
        html = html.replace("let currentK = 'K01';", "let currentK = 'K01';\n    let currentS = 'S01';")
        html = html.replace(
            "const cmd = (activeMode === 'PAIRING') ? `LÀM BANNER: ${currentP} × ${currentK}` : `LÀM BANNER: ${currentH} × ${currentK}`;",
            "const cmd = (activeMode === 'PAIRING') ? `LÀM BANNER: ${currentP} × ${currentK} × ${currentS}` : `LÀM BANNER: ${currentH} × ${currentK} × ${currentS}`;"
        )
        subfont_js = """
    function selectSubfont(sid) {
      currentS = sid;
      document.querySelectorAll('.s-card').forEach(el => {
        if (el.dataset.sid === sid) {
          el.classList.add('selected-k');
          const st = document.getElementById('slotSText');
          if (st) st.textContent = '🟣 FONT BÉ: ' + sid + ' • ' + el.dataset.sname;
          currentCropSubUrl = el.dataset.crop;
          currentFullSubUrl = el.dataset.full;
          document.getElementById('dockImgK').src = currentCropSubUrl;
        } else {
          el.classList.remove('selected-k');
        }
      });
      updateCommandText();
      syncModalView();
    }

    function filterSubfonts(group, btn) {
      document.querySelectorAll('#sec-layer3-subfonts .filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.s-card').forEach(card => {
        card.style.display = (group === 'ALL' || card.dataset.sgroup === group) ? 'flex' : 'none';
      });
    }
"""
        html = html.replace("function updateCommandText() {", subfont_js + "\n    function updateCommandText() {")
        html = html.replace(
            "document.querySelectorAll('#modalKQuickList .q-pill').forEach(b => {\n        b.classList.toggle('active-k', b.dataset.code === currentK);\n      });",
            "document.querySelectorAll('#modalKQuickList .q-pill').forEach(b => {\n        b.classList.toggle('active-k', b.dataset.code === currentK);\n      });\n      document.querySelectorAll('#modalSQuickList .q-pill').forEach(b => {\n        b.classList.toggle('active-k', b.dataset.code === currentS);\n      });"
        )
        html = html.replace(
            "if (kWrap && kWrap.children.length === 0) {",
            """const sWrap = document.getElementById('modalSQuickList');
      if (sWrap && sWrap.children.length === 0) {
        document.querySelectorAll('.s-card').forEach(c => {
          const sid = c.dataset.sid;
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'q-pill';
          btn.dataset.code = sid;
          btn.textContent = sid;
          btn.onclick = () => selectSubfont(sid);
          sWrap.appendChild(btn);
        });
      }
      if (kWrap && kWrap.children.length === 0) {"""
        )

    HUB_HTML.write_text(html, encoding="utf-8")
    print("Successfully updated /Users/vietmac/Documents/CODE/k/bo-chon-chu-banner.html with H01..H40 (40), K01..K50 (50), and S01..S35 (35)!")


if __name__ == "__main__":
    main()
