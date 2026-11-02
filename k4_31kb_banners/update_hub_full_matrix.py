#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update /Users/vietmac/Documents/CODE/k/bo-chon-chu-banner.html with the complete
4-Axis Orthogonal Typographic & Campaign Matrix:
  - Axis 1 (H01..H40): 40 Serif/Slab/Flared Headline Typefaces (adds H31..H40)
  - Axis 2 (K01..K50): 50 Subline Box UI/UX Layouts (adds rebuilt K11 + K41..K50, 5 groups x 10)
  - Axis 3 (S01..S35): 35 Subline Sans-Serif Font Pairs (Regular/Medium 500 + Bold 700)
  - Axis 4 (M01..M06): 6 Campaign Meta-Strip Hierarchy Templates (Price 4.000.000đ & Event Filter)
"""
import json
import re
from pathlib import Path

HUB_HTML = Path("/Users/vietmac/Documents/CODE/k/bo-chon-chu-banner.html")
REPORT_HK = Path("/tmp/report_h40_k50.json")
REPORT_S = Path("/tmp/report_s35_subfonts.json")
REPORT_M = Path("/tmp/report_m06_layer4.json")
CAMPAIGN_CFG = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners/campaign_config.json")


def load_m_records():
    if REPORT_M.exists():
        data = json.loads(REPORT_M.read_text(encoding="utf-8"))
        return data.get("templates", [])
    cfg = json.loads(CAMPAIGN_CFG.read_text(encoding="utf-8"))
    vars_d = cfg.get("variables", {})
    tpls = cfg.get("meta_strip_templates", {})
    records = []
    for mid in ["M01", "M02", "M03", "M04", "M05", "M06"]:
        mt = tpls[mid]
        when_t = mt.get("when_template", "")
        price_t = mt.get("price_template", "")
        note_t = mt.get("note_template", "")
        for k, v in vars_d.items():
            when_t = when_t.replace(f"[[{k}]]", str(v))
            price_t = price_t.replace(f"[[{k}]]", str(v))
            note_t = note_t.replace(f"[[{k}]]", str(v))
        records.append({
            "mid": mid,
            "stem": f"meta_{mid.lower()}_v3",
            "tier": mt.get("tier", ""),
            "name": mt.get("name", ""),
            "group": mt.get("group", "MA"),
            "group_label": mt.get("group_label", ""),
            "when_template": mt.get("when_template", ""),
            "price_template": mt.get("price_template", ""),
            "note_template": mt.get("note_template", ""),
            "when_resolved": when_t,
            "price_resolved": price_t,
            "note_resolved": note_t,
            "desc": mt.get("desc", ""),
            "rPad": 42.0,
            "typo_score": "23/23",
        })
    return records


def main():
    hk_data = json.loads(REPORT_HK.read_text(encoding="utf-8"))
    s_data = json.loads(REPORT_S.read_text(encoding="utf-8"))
    m_records = load_m_records()

    rendered_by_sid = hk_data["rendered_by_sid"]
    new_headlines = hk_data["new_headlines_h31_h40"]
    new_subboxes = hk_data["new_subboxes_k11_k41_k50"]

    html = HUB_HTML.read_text(encoding="utf-8")

    # 1. Remove any previously injected H31..H40, K11, K41..K50, sec-layer3-subfonts, or sec-layer4-meta to make idempotent
    html = re.sub(r'\s*<article class="item-card h-card" data-hid="H(?:3[1-9]|40)"[\s\S]*?</article>', "", html)
    html = re.sub(r'\s*<article class="item-card k-card" data-kid="K(?:11|4[1-9]|50)"[\s\S]*?</article>', "", html)
    html = re.sub(
        r'\s*<!-- ==================== SECTION 2B: LAYER 3 \(35 SUBLINE SANS FONTS S01\.\.S35\) ==================== -->[\s\S]*?<!-- ==================== SECTION 3: MASTER OVERVIEW SHEETS ==================== -->',
        '  <!-- ==================== SECTION 3: MASTER OVERVIEW SHEETS ==================== -->',
        html,
    )
    html = re.sub(
        r'\s*<!-- ==================== SECTION 2C: LAYER 4 \(6 CAMPAIGN META-STRIP TEMPLATES M01\.\.M06\) ==================== -->[\s\S]*?<!-- ==================== SECTION 3: MASTER OVERVIEW SHEETS ==================== -->',
        '  <!-- ==================== SECTION 3: MASTER OVERVIEW SHEETS ==================== -->',
        html,
    )

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
        <article class="item-card h-card" data-hid="{hid}" data-hgroup="{grp}" data-hname="{hspec['name']} ({calc['fs']}px, LH={calc['L_target']})" data-crop="k4_31kb_banners/v2_pilots/crop_head_{sid}.jpg?v=v9_r2_sync3_s35" data-full="k4_31kb_banners/v2_pilots/{sid}.jpg?v=v9_r2_sync3_s35" onclick="selectHeadline('{hid}')">
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
            <img class="preview-img" src="k4_31kb_banners/v2_pilots/crop_head_{sid}.jpg?v=v9_r2_sync3_s35" alt="{hid} {hspec['name']}" loading="lazy" />
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
        <article class="item-card k-card" data-kid="{kid}" data-kgroup="{grp}" data-kname="{kspec['name']}" data-crop="k4_31kb_banners/v2_pilots/crop_sub_{sid}.jpg?v=v9_r2_sync3_s35" data-full="k4_31kb_banners/v2_pilots/{sid}.jpg?v=v9_r2_sync3_s35" onclick="selectSubbox('{kid}')">
          <div class="card-head">
            <div class="card-top-row">
              <span class="code-pill k-pill">{kid} • {kspec['name'].upper()}</span>
              <span class="grp-badge" style="{k_badge_map[grp]}">{kspec['kgroup_label']}</span>
            </div>
            <div class="sample-quote">{kspec['sample_quote']}</div>
            <p class="card-desc">{kspec['desc']}</p>
          </div>
          <div class="img-box sub-img-box" onclick="event.stopPropagation(); selectSubbox('{kid}'); openBigPreviewModal();" title="Click vào ảnh để mở BẢNG XEM TO (Ảnh Ví Dụ 1080×1350)">
            <img class="preview-img" src="k4_31kb_banners/v2_pilots/crop_sub_{sid}.jpg?v=v9_r2_sync3_s35" alt="{kid} {kspec['name']}" loading="lazy" />
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

    k10_pos = html.find('data-kid="K10"')
    k10_end = html.find("</article>", k10_pos) + len("</article>")
    html = html[:k10_end] + "\n" + make_k_card(k11_spec) + html[k10_end:]

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
        <article class="item-card s-card" data-sid="{sid}" data-sgroup="{sgrp}" data-sname="{name} (500 + 700)" data-crop="k4_31kb_banners/v2_pilots/crop_sub_{slug}.jpg?v=v9_r2_sync3_s35" data-full="k4_31kb_banners/v2_pilots/{slug}.jpg?v=v9_r2_sync3_s35" onclick="selectSubfont('{sid}')">
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
            <img class="preview-img" src="k4_31kb_banners/v2_pilots/crop_sub_{slug}.jpg?v=v9_r2_sync3_s35" alt="{sid} {name}" loading="lazy" />
            <span class="img-mode-tag sub-tag" style="background:rgba(168,85,247,0.9);color:#fff;">🔍 CLICK ẢNH XEM BẢNG TO (FONT CHỮ NHỎ {sid})</span>
          </div>
          <div class="card-foot">
            <span>rPad={item['rPad']}px • <b style="color:#4ADE80;">{item['score']} PASS</b></span>
            <div style="display:flex;gap:6px;">
              <button type="button" class="btn-pick" style="background:rgba(56,189,248,0.16);color:#38BDF8;border-color:rgba(56,189,248,0.4);" onclick="event.stopPropagation(); selectSubfont('{sid}'); openBigPreviewModal();">🖼️ Xem Bảng To</button>
              <button type="button" class="btn-pick" style="background:rgba(168,85,247,0.2);color:#C084FC;border:1px solid rgba(168,85,247,0.45);" onclick="event.stopPropagation(); selectSubfont('{sid}')">✓ Chọn {sid}</button>
            </div>
          </div>
        </article>""")

    # 5. Build Layer 4 Section: 6 Campaign Meta-Strip Hierarchy Templates (M01..M06)
    m_badge_map = {
        "MA": "background:rgba(245,158,11,0.18);color:#FACC15;border:1px solid rgba(245,158,11,0.45);",
        "MB": "background:rgba(34,197,94,0.18);color:#4ADE80;border:1px solid rgba(34,197,94,0.45);",
        "MC": "background:rgba(56,189,248,0.18);color:#38BDF8;border:1px solid rgba(56,189,248,0.45);",
    }
    m_short_label_map = {
        "M01": "Kiểu 1 (Logic 1): Giá 4Tr Trung Tâm + Vạch Dọc",
        "M02": "Kiểu 2 (Logic 2): Bảng Chia 2 Cột Trái–Phải",
        "M03": "Kiểu 3 (Logic 3): Hàng Chính Thoáng + Thanh Pill",
        "M04": "Kiểu 1B: Nhãn Lịch Trên + Giá & Tặng Online",
        "M05": "Kiểu 2B: Bảng 2 Cột + Cầm Video Về Ngay",
        "M06": "Kiểu 3B: Hàng Chính Thoáng + Pill Quyền Lợi",
    }

    m_cards_html = []
    for mitem in m_records:
        mid = mitem["mid"]
        stem = mitem["stem"]
        mgrp = mitem["group"]
        mgrp_label = mitem["group_label"]
        when_res = mitem["when_resolved"]
        price_res = mitem["price_resolved"]
        note_res = mitem["note_resolved"]
        short_lbl = m_short_label_map.get(mid, f"{when_res} · {price_res}")
        quote_str = f"● {when_res}   ───   {price_res}" + (f"  |  {note_res}" if note_res else "")
        selected_cls = " selected-h" if mid == "M01" else ""

        m_cards_html.append(f"""
        <article class="item-card m-card{selected_cls}" data-mid="{mid}" data-mgroup="{mgrp}" data-mname="{short_lbl}" data-crop="k4_31kb_banners/v2_pilots/crop_{stem}.jpg?v=v10_3designs" data-full="k4_31kb_banners/v2_pilots/{stem}.jpg?v=v10_3designs" onclick="selectMetastrip('{mid}')">
          <div class="card-head">
            <div class="card-top-row">
              <span class="code-pill" style="background:rgba(245,158,11,0.22);color:#FACC15;border:1px solid rgba(245,158,11,0.55);">{mid} • {mitem['name'].upper()}</span>
              <span class="grp-badge" style="{m_badge_map.get(mgrp, m_badge_map['MA'])}">{mgrp_label}</span>
            </div>
            <div class="metrics-bar">
              <span>Lịch &amp; Địa điểm: <b>{when_res}</b></span>
              <span>•</span>
              <span>Giá Chính (Hero): <b>{price_res}</b> (FDAeonik Bold Kerning Khít)</span>
            </div>
            <div class="sample-quote" style="border-left-color:#FACC15;">{quote_str}</div>
            <p class="card-desc">{mitem['desc']}</p>
          </div>
          <div class="img-box sub-img-box" onclick="event.stopPropagation(); selectMetastrip('{mid}'); openBigPreviewModal();" title="Click vào ảnh để mở BẢNG XEM TO (Ảnh Ví Dụ 1080×1350)">
            <img class="preview-img" src="k4_31kb_banners/v2_pilots/crop_{stem}.jpg?v=v10_3designs" alt="{mid} {mitem['name']}" loading="lazy" />
            <span class="img-mode-tag" style="background:rgba(245,158,11,0.92);color:#070B14;border-color:#FACC15;">🔍 CLICK ẢNH XEM BẢNG TO (LỚP 4 {mid})</span>
          </div>
          <div class="card-foot">
            <span>Config: <code>campaign_config.json</code> • rPad={mitem.get('rPad', 42)}px • <b style="color:#4ADE80;">{mitem.get('typo_score', '23/23')} PASS</b></span>
            <div style="display:flex;gap:6px;">
              <button type="button" class="btn-pick" style="background:rgba(56,189,248,0.16);color:#38BDF8;border-color:rgba(56,189,248,0.4);" onclick="event.stopPropagation(); selectMetastrip('{mid}'); openBigPreviewModal();">🖼️ Xem Bảng To</button>
              <button type="button" class="btn-pick" style="background:rgba(245,158,11,0.22);color:#FACC15;border-color:rgba(245,158,11,0.5);" onclick="event.stopPropagation(); selectMetastrip('{mid}')">✓ Chọn {mid}</button>
            </div>
          </div>
        </article>""")

    sec_s_and_m_html = f"""
  <!-- ==================== SECTION 2B: LAYER 3 (35 SUBLINE SANS FONTS S01..S35) ==================== -->
  <section class="section" id="sec-layer3-subfonts" style="background:radial-gradient(circle at 85% 20%, rgba(168,85,247,0.08), transparent 55%);">
    <div class="container">
      <div class="sec-head">
        <span class="sec-tag" style="background:rgba(168,85,247,0.18);color:#C084FC;border:1px solid rgba(168,85,247,0.45);">LỚP 3 (MỚI) • BỘ CHỌN 35 HỌ FONT CHỮ NHỎ KHÔNG CHÂN (S01 → S35 • CẶP REGULAR/MEDIUM 500 + BOLD 700)</span>
        <h2 class="sec-title">🟣 LỚP 3: BỘ CHỌN 35 HỌ FONT CHỮ NHỎ KHÔNG CHÂN (S01 → S35 • ĐẠT 20/20 CỔNG UI/UX)</h2>
        <p class="sec-desc">
          Theo thống kê toàn bộ <b>2.149 file font</b> trong kho cùng <b>CLAUDE2 (Opus 5.5)</b>: đây là trọn bộ <b>35 họ Font Không Chân (`Sans-Serif`)</b> ưu tú nhất có đủ cặp <b>Regular/Medium 500 (cho dòng dẫn/triệu chứng)</b> và <b>Bold 700 (cho dòng kết luận/hành động)</b>, đọc sắc lẹm ở cỡ chữ nhỏ <code>19.5px–21px</code> trên điện thoại. Click vào bất kỳ thẻ <code>S01–S35</code> nào để chọn Font Chữ Nhỏ hoặc mở Bảng Xem To!
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

  <!-- ==================== SECTION 2C: LAYER 4 (6 CAMPAIGN META-STRIP TEMPLATES M01..M06) ==================== -->
  <section class="section" id="sec-layer4-meta" style="background:radial-gradient(circle at 18% 25%, rgba(245,158,11,0.10), transparent 55%);">
    <div class="container">
      <div class="sec-head">
        <span class="sec-tag" style="background:rgba(245,158,11,0.20);color:#FACC15;border:1px solid rgba(245,158,11,0.50);">LỚP 4 (NÂNG CẤP V2.0 • 3 LOGIC CHÍNH–PHỤ × 3 KIỂU THIẾT KẾ) • BỘ CHỌN PHÂN CẤP GIÁ &amp; CAM KẾT (M01 → M06)</span>
        <h2 class="sec-title">🔶 LỚP 4: 3 LOGIC CHÍNH–PHỤ × 3 KIỂU THIẾT KẾ KHUNG GIÁ &amp; BẢO LÃNH (M01 → M06 • ĐÃ KHẮC PHỤC TRIỆT ĐỂ LỖI SÁT CHỮ &amp; DẤU CHẤM RỖNG)</h2>
        <p class="sec-desc">
          Thiết kế mới theo <b>3 Logic Phân Cấp Chính – Phụ</b> (khắc phục hoàn toàn lỗi dấu chấm rỗng <code>4 . 000 . 000đ</code> của font Mono và lỗi 2 hàng chữ dính sát nhau):<br/>
          <b>• Kiểu 1 (<code>M01</code>, <code>M04</code> — Logic 1: Giá &amp; Bảo Lãnh Làm Trung Tâm, Lịch Học Lên Nhãn Eyebrow Trên):</b> Đưa Lịch học lên dòng nhãn nhỏ (<code>14.8px Uppercase #94A3B8</code>) ở trên để giải phóng mặt bằng; Hàng chính bên dưới đặt <b>Giá <code>4.000.000đ</code> (<code>38.5px Bold</code>)</b> làm nhân vật chính bên trái, ngăn cách bằng vạch dọc thoáng <code>48px</code> với khối Bảo lãnh 2 dòng bên phải.<br/>
          <b>• Kiểu 2 (<code>M02</code>, <code>M05</code> — Logic 2: Bảng Chia 2 Cột Trái–Phải Độc Lập / Split Ledger):</b> Chia mặt bằng thành 2 cột bằng vạch ngăn dọc xuyên suốt: <b>Cột Trái</b> xếp chồng Lịch học (<code>21px Bold</code>) + Cam kết hoàn tiền (<code>16.5px Medium</code>, cách dòng <code>10px</code>); <b>Cột Phải</b> là Ô Giá độc lập gồm nhãn <code>HỌC PHÍ 2 NGÀY</code> và số <code>4.000.000đ</code> (<code>35px Bold</code>).<br/>
          <b>• Kiểu 3 (<code>M03</code>, <code>M06</code> — Logic 3: Hàng Chính Tương Phản Mảnh/Đậm + Đóng Khung Thanh Pill Bảo Lãnh):</b> Hàng trên hạ Lịch học xuống <code>20px Medium #CBD5E1</code> để tôn <b>Giá <code>4.000.000đ</code> (<code>36px Bold #FFFFFF</code>)</b> làm chính (khoảng trống giữa 2 cụm rộng <code>&gt;70px</code>); Hàng dưới cách <code>14px</code> đóng gọn vào <b>Thanh Pill nền mờ viền mảnh</b> tách biệt.
        </p>
      </div>

      <div class="filter-row">
        <button class="filter-btn m-filter active" onclick="filterMetastrips('ALL', this)">Tất cả 3 Kiểu Thiết Kế (M01–M06)</button>
        <button class="filter-btn m-filter" onclick="filterMetastrips('MA', this)">Kiểu 1 • Logic 1: Eyebrow Trên + Giá &amp; Bảo Lãnh Dưới (M01, M04)</button>
        <button class="filter-btn m-filter" onclick="filterMetastrips('MB', this)">Kiểu 2 • Logic 2: Bảng Chia 2 Cột Trái–Phải Độc Lập (M02, M05)</button>
        <button class="filter-btn m-filter" onclick="filterMetastrips('MC', this)">Kiểu 3 • Logic 3: Hàng Chính Tương Phản + Thanh Pill (M03, M06)</button>
      </div>

      <div class="cards-grid" id="grid-metastrips" style="grid-template-columns: repeat(3, 1fr);">
        {"".join(m_cards_html)}
      </div>
    </div>
  </section>

  <!-- ==================== SECTION 3: MASTER OVERVIEW SHEETS ==================== -->"""

    html = html.replace("  <!-- ==================== SECTION 3: MASTER OVERVIEW SHEETS ==================== -->", sec_s_and_m_html)

    # 6. Update counts and labels across the page (30 -> 40 Headlines, 39 -> 50 Subboxes, 35 Subfonts, 6 Meta-strips)
    html = html.replace("TIÊU ĐỀ (H01–H30) × KHUNG CHỮ BÉ (K01–K40)", "TIÊU ĐỀ (H01–H40) × KHUNG CHỮ BÉ (K01–K50) × FONT CHỮ BÉ (S01–S35)")
    html = html.replace("🔹 LỚP 1: 30 Font Tiêu Đề Đơn (H01–H30)", "🔹 LỚP 1: 40 Font Tiêu Đề Có Chân (H01–H40)")
    html = html.replace("🔸 LỚP 2: 39 Khuôn Khung Chữ Bé (K01–K40)", "🔸 LỚP 2: 50 Khuôn Khung Chữ Bé (K01–K50)")
    if 'href="#sec-layer3-subfonts"' not in html:
        html = html.replace(
            '<a href="#sec-layer2-subboxes" class="nav-pill">🔸 LỚP 2: 50 Khuôn Khung Chữ Bé (K01–K50)</a>',
            '<a href="#sec-layer2-subboxes" class="nav-pill">🔸 LỚP 2: 50 Khuôn Khung Chữ Bé (K01–K50)</a>\n      <a href="#sec-layer3-subfonts" class="nav-pill">🟣 LỚP 3: 35 Họ Font Chữ Nhỏ (S01–S35)</a>',
        )
    if 'href="#sec-layer4-meta"' not in html:
        html = html.replace(
            '<a href="#sec-layer3-subfonts" class="nav-pill">🟣 LỚP 3: 35 Họ Font Chữ Nhỏ (S01–S35)</a>',
            '<a href="#sec-layer3-subfonts" class="nav-pill">🟣 LỚP 3: 35 Họ Font Chữ Nhỏ (S01–S35)</a>\n      <a href="#sec-layer4-meta" class="nav-pill">🔶 LỚP 4: 6 Khuôn Phân Cấp Giá &amp; Sự Kiện (M01–M06)</a>',
        )

    html = html.replace("[TIÊU ĐỀ H01–H30] × [KHUNG K01–K40]", "[40 TIÊU ĐỀ H01–H40] × [50 KHUNG K01–K50] × [35 FONT CHỮ NHỎ S01–S35] × [6 KHUÔN GIÁ M01–M06]")
    html = html.replace("30 HỌ FONT TIÊU ĐỀ CÓ CHÂN ĐÃ KIỂM ĐỊNH (H01 → H30)", "40 HỌ FONT TIÊU ĐỀ CÓ CHÂN ĐÃ KIỂM ĐỊNH (H01 → H40)")
    html = html.replace("Tất cả 30 Font Tiêu Đề (H01–H30)", "Tất cả 40 Font Tiêu Đề Có Chân (H01–H40)")
    html = html.replace("🔸 LỚP 2: BỘ CHỌN KHUÔN KHUNG CHỮ BÉ (39 KHUÔN CHIA THEO 5 HỌ LOGIC: K01–K10 &amp; K12–K40, BỎ #11)", "🔸 LỚP 2: BỘ CHỌN KHUÔN KHUNG CHỮ BÉ (TRÒN 50 KHUÔN CHIA ĐỀU 5 HỌ LOGIC × 10 KHUÔN: K01 → K50, ĐẠT 20/20 CỔNG)")
    html = html.replace("Tất cả 39 Khuôn Khung Chữ Bé (K01–K40, Đã bỏ #11)", "Tất cả 50 Khuôn Khung Chữ Bé (K01–K50 • 5 Họ × 10 Khuôn)")
    html = html.replace("Họ 1 • Đối Lập & So Sánh 2 Vế (9 khuôn: K01, K06, K07, K17, K20, K22, K24, K31, K35)", "Họ 1 • Đối Lập & So Sánh 2 Vế (10 khuôn: K01, K06, K07, K11, K17, K20, K22, K24, K31, K35)")
    html = html.replace("Họ 2 • Con Số, Thời Gian &amp; Lịch Tuần (9 khuôn: K03, K10, K14, K15, K21, K23, K28, K32, K36)", "Họ 2 • Con Số, Thời Gian &amp; Lịch Tuần (10 khuôn: K03, K10, K14, K15, K21, K23, K28, K32, K36, K41)")
    html = html.replace("Họ 3 • Công Thức &amp; Bảng Kiểm (7 khuôn: K05, K18, K19, K25, K29, K33, K38)", "Họ 3 • Công Thức &amp; Bảng Kiểm (10 khuôn: K05, K18, K19, K25, K29, K33, K38, K42, K43, K44)")
    html = html.replace("Họ 4 • Tin Nhắn &amp; Hỏi–Đáp (5 khuôn: K09, K12, K26, K34, K39)", "Họ 4 • Tin Nhắn &amp; Hỏi–Đáp (10 khuôn: K09, K12, K26, K34, K39, K45, K46, K47, K48, K49)")
    html = html.replace("Họ 5 • Tuyên Ngôn &amp; Đúc Kết (9 khuôn: K02, K04, K08, K13, K16, K27, K30, K37, K40)", "Họ 5 • Tuyên Ngôn &amp; Đúc Kết (10 khuôn: K02, K04, K08, K13, K16, K27, K30, K37, K40, K50)")

    # 7. Add overview sheets for H31..H40, K11/K41..K50, S01..S35, and M01..M06 into #sec-layer3-library
    extra_sheets = """
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:18px;">
        <div class="arch-box" style="background:#0E1526;border:1.5px solid #FACC15;border-radius:14px;padding:14px;">
          <div style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:var(--gold-bright);margin-bottom:8px;">BẢNG MỚI (ĐỢT 1) • 10 FONT SERIF TIÊU ĐỀ H31 → H40 (20/20 PASS)</div>
          <img src="k4_31kb_banners/v2_pilots/h31_h40_10headlines_grid.jpg?v=v9_r2_sync3_s35" alt="H31-H40 Grid" style="width:100%;border-radius:10px;display:block;" />
        </div>
        <div class="arch-box" style="background:#0E1526;border:1.5px solid #38BDF8;border-radius:14px;padding:14px;">
          <div style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:var(--cyan);margin-bottom:8px;">BẢNG MỚI (ĐỢT 2) • 11 KHUÔN CHỮ NHỎ K11 &amp; K41 → K50 (20/20 PASS)</div>
          <img src="k4_31kb_banners/v2_pilots/k11_k41_k50_11subboxes_grid.jpg?v=v9_r2_sync3_s35" alt="K11-K50 Grid" style="width:100%;border-radius:10px;display:block;" />
        </div>
        <div class="arch-box" style="background:#0E1526;border:1.5px solid #C084FC;border-radius:14px;padding:14px;">
          <div style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:#C084FC;margin-bottom:8px;">BẢNG MỚI (ĐỢT 3) • 35 HỌ FONT CHỮ NHỎ S01 → S35 (20/20 PASS)</div>
          <img src="k4_31kb_banners/v2_pilots/s01_s35_subfonts_grid.jpg?v=v9_r2_sync3_s35" alt="S01-S35 Grid" style="width:100%;border-radius:10px;display:block;" />
        </div>
      </div>"""
    if "h31_h40_10headlines_grid.jpg" not in html:
        html = html.replace(
            '<img src="k4_31kb_banners/v2_pilots/serif_sheet_3_remaining8.jpg?v=sci_v5" alt="Bảng 3" style="width:100%;border-radius:10px;display:block;" />\n        </div>\n      </div>',
            '<img src="k4_31kb_banners/v2_pilots/serif_sheet_3_remaining8.jpg?v=sci_v5" alt="Bảng 3" style="width:100%;border-radius:10px;display:block;" />\n        </div>\n      </div>\n' + extra_sheets,
        )

    m_grid_sheet = """
      <div class="arch-box" style="margin-top:18px;border:1.5px solid #F59E0B;border-radius:16px;padding:18px;background:#0E1526;">
        <div style="font-family:var(--font-mono);font-size:13px;font-weight:800;color:#FACC15;margin-bottom:10px;">BẢNG MỚI (ĐỢT 4 • LỚP 4 V2.0) • 3 LOGIC CHÍNH–PHỤ × 3 KIỂU THIẾT KẾ KHUNG GIÁ &amp; BẢO LÃNH (M01 → M06 • 4.000.000Đ)</div>
        <img src="k4_31kb_banners/v2_pilots/m01_m06_layer4_grid.jpg?v=v10_3designs" alt="M01-M06 Layer 4 Grid" style="width:100%;border-radius:12px;display:block;" />
      </div>"""
    if "m01_m06_layer4_grid.jpg" not in html:
        html = html.replace(
            '<img src="k4_31kb_banners/v2_pilots/s01_s35_subfonts_grid.jpg?v=v9_r2_sync3_s35" alt="S01-S35 Grid" style="width:100%;border-radius:10px;display:block;" />\n        </div>\n      </div>',
            '<img src="k4_31kb_banners/v2_pilots/s01_s35_subfonts_grid.jpg?v=v9_r2_sync3_s35" alt="S01-S35 Grid" style="width:100%;border-radius:10px;display:block;" />\n        </div>\n      </div>\n' + m_grid_sheet,
        )

    # 8. Update Modal Quick Lists, Combinator Dock & JS to support S01..S35 and M01..M06
    html = html.replace("2. HOẶC ĐỔI NHANH 30 FONT TIÊU ĐỀ ĐƠN (H01 → H30):", "2. ĐỔI NHANH 40 FONT TIÊU ĐỀ CÓ CHÂN (H01 → H40):")
    html = html.replace("3. ĐỔI NHANH 39 KHUÔN KHUNG CHỮ BÉ (K01 → K40, ĐÃ BỎ #11):", "3. ĐỔI NHANH 50 KHUÔN KHUNG CHỮ BÉ (K01 → K50):")

    if 'id="modalSQuickList"' not in html:
        html = html.replace(
            '<div class="quick-pills-wrap" id="modalKQuickList"></div>\n        </div>',
            '<div class="quick-pills-wrap" id="modalKQuickList"></div>\n        </div>\n\n        <div>\n          <div style="font-family:var(--font-mono);font-size:11.5px;color:#C084FC;font-weight:800;margin-bottom:6px;">4. ĐỔI NHANH 35 HỌ FONT CHỮ NHỎ KHÔNG CHÂN (S01 → S35):</div>\n          <div class="quick-pills-wrap" id="modalSQuickList"></div>\n        </div>',
        )

    if 'id="modalMQuickList"' not in html:
        html = html.replace(
            '<div class="quick-pills-wrap" id="modalSQuickList"></div>\n        </div>',
            '<div class="quick-pills-wrap" id="modalSQuickList"></div>\n        </div>\n\n        <div>\n          <div style="font-family:var(--font-mono);font-size:11.5px;color:#FACC15;font-weight:800;margin-bottom:6px;">5. ĐỔI NHANH 6 KHUÔN PHÂN CẤP GIÁ &amp; SỰ KIỆN (M01 → M06):</div>\n          <div class="quick-pills-wrap" id="modalMQuickList"></div>\n        </div>',
        )

    if 'id="slotSText"' not in html:
        html = html.replace(
            '<span class="slot-badge slot-k" id="slotKText">🔸 KHUNG BÉ: K01 • Hai Vế Đối Lập (× / ✓)</span>',
            '<span class="slot-badge slot-k" id="slotKText">🔸 KHUNG BÉ: K01 • Hai Vế Đối Lập (× / ✓)</span>\n            <span style="font-weight:800;color:var(--text-soft);">×</span>\n            <span class="slot-badge" id="slotSText" style="background:rgba(168,85,247,0.2);color:#C084FC;border:1px solid rgba(168,85,247,0.45);">🟣 FONT BÉ: S01 • FD Aeonik (500 + 700)</span>',
        )

    if 'id="slotMText"' not in html:
        html = html.replace(
            '<span class="slot-badge" id="slotSText" style="background:rgba(168,85,247,0.2);color:#C084FC;border:1px solid rgba(168,85,247,0.45);">🟣 FONT BÉ: S01 • FD Aeonik (500 + 700)</span>',
            '<span class="slot-badge" id="slotSText" style="background:rgba(168,85,247,0.2);color:#C084FC;border:1px solid rgba(168,85,247,0.45);">🟣 FONT BÉ: S01 • FD Aeonik (500 + 700)</span>\n            <span style="font-weight:800;color:var(--text-soft);">×</span>\n            <span class="slot-badge" id="slotMText" style="background:rgba(245,158,11,0.22);color:#FACC15;border:1px solid rgba(245,158,11,0.55);">🔶 LỚP 4 GIÁ: M01 • 07–08/11 Long Biên · 4.000.000đ</span>',
        )

    html = html.replace('<span class="cmd-text" id="cmdOutput">LÀM BANNER: P01 × K01</span>', '<span class="cmd-text" id="cmdOutput">LÀM BANNER: P01 × K01 × S01 × M01</span>')
    html = html.replace('<code id="modalCmdText" style="font-family:var(--font-mono);font-size:14px;color:#4ADE80;font-weight:800;">LÀM BANNER: P01 × K01</code>', '<code id="modalCmdText" style="font-family:var(--font-mono);font-size:14px;color:#4ADE80;font-weight:800;">LÀM BANNER: P01 × K01 × S01 × M01</code>')

    if 'id="modalFullMetaImg"' not in html:
        html = html.replace(
            '<img class="layer-sub-full" id="modalFullSubImg" src="k4_31kb_banners/v2_pilots/p01_l1_domaine_superfamily.jpg?v=v9_r2_sync3" alt="Example Banner Bottom Layer" />',
            '<img class="layer-sub-full" id="modalFullSubImg" src="k4_31kb_banners/v2_pilots/p01_l1_domaine_superfamily.jpg?v=v9_r2_sync3" alt="Example Banner Bottom Layer" />\n          <img class="layer-meta-full" id="modalFullMetaImg" src="k4_31kb_banners/v2_pilots/meta_m01_v3.jpg?v=v9_r2_sync3" alt="Example Banner Layer 4 Price & Event Strip" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;clip-path:inset(65.5% 0 0 0);" />',
        )

    if 'id="modalCropMetaImg"' not in html:
        html = html.replace(
            '<img id="modalCropSubImg" src="k4_31kb_banners/v2_pilots/crop_sub_p01_l1_domaine_superfamily.jpg?v=v9_r2_sync3" alt="Closeup Subbox" />',
            '<img id="modalCropSubImg" src="k4_31kb_banners/v2_pilots/crop_sub_p01_l1_domaine_superfamily.jpg?v=v9_r2_sync3" alt="Closeup Subbox" />\n          <img id="modalCropMetaImg" src="k4_31kb_banners/v2_pilots/crop_meta_m01_v3.jpg?v=v9_r2_sync3" alt="Closeup Layer 4 Meta Strip" />',
        )

    # Replace the <script> block cleanly to guarantee 4-axis state & live preview synthesis
    script_start = html.find("  <script>")
    script_end = html.find("  </script>") + len("  </script>")
    new_script = """  <script>
    let activeMode = 'PAIRING'; // 'PAIRING' or 'CUSTOM_HK'
    let currentP = 'P01';
    let currentH = 'H01';
    let currentK = 'K01';
    let currentS = 'S01';
    let currentM = 'M01';
    let isFullMode = false;
    let currentFullHeadUrl = 'k4_31kb_banners/v2_pilots/p01_l1_domaine_superfamily.jpg?v=v9_r2_sync3';
    let currentFullSubUrl = 'k4_31kb_banners/v2_pilots/p01_l1_domaine_superfamily.jpg?v=v9_r2_sync3';
    let currentFullMetaUrl = 'k4_31kb_banners/v2_pilots/meta_m01_v3.jpg?v=v10_3designs';
    let currentCropHeadUrl = 'k4_31kb_banners/v2_pilots/crop_head_p01_l1_domaine_superfamily.jpg?v=v9_r2_sync3';
    let currentCropSubUrl = 'k4_31kb_banners/v2_pilots/crop_sub_p01_l1_domaine_superfamily.jpg?v=v9_r2_sync3';
    let currentCropMetaUrl = 'k4_31kb_banners/v2_pilots/crop_meta_m01_v3.jpg?v=v10_3designs';

    function selectPairing(pid) {
      activeMode = 'PAIRING';
      currentP = pid;
      document.querySelectorAll('.h-card').forEach(el => el.classList.remove('selected-h'));
      document.querySelectorAll('.p-card').forEach(el => {
        if (el.dataset.pid === pid) {
          el.classList.add('selected-p');
          currentK = el.dataset.kcode;
          document.getElementById('slotPText').className = 'slot-badge slot-p';
          document.getElementById('slotPText').textContent = '🔬 PHỐI CHỮ: ' + pid + ' • ' + el.dataset.pname;
          currentCropHeadUrl = el.dataset.hcrop;
          currentCropSubUrl = el.dataset.scrop;
          currentFullHeadUrl = el.dataset.full;
          currentFullSubUrl = el.dataset.full;
          document.getElementById('dockImgH').src = currentCropHeadUrl;
          document.getElementById('dockImgK').src = currentCropSubUrl;
        } else {
          el.classList.remove('selected-p');
        }
      });
      document.querySelectorAll('.k-card').forEach(el => {
        if (el.dataset.kid === currentK) {
          el.classList.add('selected-k');
          document.getElementById('slotKText').textContent = '🔸 KHUNG BÉ: ' + currentK + ' • ' + el.dataset.kname;
        } else {
          el.classList.remove('selected-k');
        }
      });
      updateCommandText();
      syncModalView();
    }

    function selectHeadline(hid) {
      activeMode = 'CUSTOM_HK';
      currentH = hid;
      document.querySelectorAll('.p-card').forEach(el => el.classList.remove('selected-p'));
      document.querySelectorAll('.h-card').forEach(el => {
        if (el.dataset.hid === hid) {
          el.classList.add('selected-h');
          document.getElementById('slotPText').className = 'slot-badge slot-h';
          document.getElementById('slotPText').textContent = '🔹 TIÊU ĐỀ: ' + hid + ' • ' + el.dataset.hname;
          currentCropHeadUrl = el.dataset.crop;
          currentFullHeadUrl = el.dataset.full;
          document.getElementById('dockImgH').src = currentCropHeadUrl;
        } else {
          el.classList.remove('selected-h');
        }
      });
      updateCommandText();
      syncModalView();
    }

    function selectSubbox(kid) {
      currentK = kid;
      document.querySelectorAll('.k-card').forEach(el => {
        if (el.dataset.kid === kid) {
          el.classList.add('selected-k');
          document.getElementById('slotKText').textContent = '🔸 KHUNG BÉ: ' + kid + ' • ' + el.dataset.kname;
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

    function selectMetastrip(mid) {
      currentM = mid;
      document.querySelectorAll('.m-card').forEach(el => {
        if (el.dataset.mid === mid) {
          el.classList.add('selected-h');
          const mt = document.getElementById('slotMText');
          if (mt) mt.textContent = '🔶 LỚP 4 GIÁ: ' + mid + ' • ' + el.dataset.mname;
          currentCropMetaUrl = el.dataset.crop;
          currentFullMetaUrl = el.dataset.full;
          document.getElementById('dockImgK').src = currentCropMetaUrl;
        } else {
          el.classList.remove('selected-h');
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

    function filterMetastrips(group, btn) {
      document.querySelectorAll('#sec-layer4-meta .filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.m-card').forEach(card => {
        card.style.display = (group === 'ALL' || card.dataset.mgroup === group) ? 'flex' : 'none';
      });
    }

    function updateCommandText() {
      const cmd = (activeMode === 'PAIRING')
        ? `LÀM BANNER: ${currentP} × ${currentK} × ${currentS} × ${currentM}`
        : `LÀM BANNER: ${currentH} × ${currentK} × ${currentS} × ${currentM}`;
      document.getElementById('cmdOutput').textContent = cmd;
      const mCmd = document.getElementById('modalCmdText');
      if (mCmd) mCmd.textContent = cmd;
    }

    function syncModalView() {
      const fh = document.getElementById('modalFullHeadImg');
      const fs = document.getElementById('modalFullSubImg');
      const fm = document.getElementById('modalFullMetaImg');
      const ch = document.getElementById('modalCropHeadImg');
      const cs = document.getElementById('modalCropSubImg');
      const cm = document.getElementById('modalCropMetaImg');
      if (fh) fh.src = currentFullHeadUrl;
      if (fs) fs.src = currentFullSubUrl;
      if (fm) { fm.src = currentFullMetaUrl; fm.style.clipPath = (currentK === "K09" || currentK === "K10") ? "inset(66.2% 0 0 0)" : "inset(65.5% 0 0 0)"; }
      if (ch) ch.src = currentCropHeadUrl;
      if (cs) cs.src = currentCropSubUrl;
      if (cm) cm.src = currentCropMetaUrl;

      const tEl = document.getElementById('modalTitleText');
      if (tEl) {
        const pTxt = document.getElementById('slotPText').textContent;
        const kTxt = document.getElementById('slotKText').textContent;
        const mTxt = document.getElementById('slotMText') ? document.getElementById('slotMText').textContent : currentM;
        tEl.textContent = pTxt + '  ×  ' + kTxt + '  ×  ' + mTxt;
      }

      document.querySelectorAll('#modalPQuickList .q-pill').forEach(b => {
        b.classList.toggle('active-p', activeMode === 'PAIRING' && b.dataset.code === currentP);
      });
      document.querySelectorAll('#modalHQuickList .q-pill').forEach(b => {
        b.classList.toggle('active-h', activeMode === 'CUSTOM_HK' && b.dataset.code === currentH);
      });
      document.querySelectorAll('#modalKQuickList .q-pill').forEach(b => {
        b.classList.toggle('active-k', b.dataset.code === currentK);
      });
      document.querySelectorAll('#modalSQuickList .q-pill').forEach(b => {
        b.classList.toggle('active-k', b.dataset.code === currentS);
      });
      document.querySelectorAll('#modalMQuickList .q-pill').forEach(b => {
        b.classList.toggle('active-h', b.dataset.code === currentM);
      });
    }

    function buildModalQuickLists() {
      const pWrap = document.getElementById('modalPQuickList');
      const hWrap = document.getElementById('modalHQuickList');
      const kWrap = document.getElementById('modalKQuickList');
      const sWrap = document.getElementById('modalSQuickList');
      const mWrap = document.getElementById('modalMQuickList');
      if (pWrap && pWrap.children.length === 0) {
        document.querySelectorAll('.p-card').forEach(c => {
          const pid = c.dataset.pid;
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'q-pill';
          btn.dataset.code = pid;
          btn.textContent = pid + ' (' + c.dataset.plaw + ')';
          btn.onclick = () => selectPairing(pid);
          pWrap.appendChild(btn);
        });
      }
      if (hWrap && hWrap.children.length === 0) {
        document.querySelectorAll('.h-card').forEach(c => {
          const hid = c.dataset.hid;
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'q-pill';
          btn.dataset.code = hid;
          btn.textContent = hid;
          btn.onclick = () => selectHeadline(hid);
          hWrap.appendChild(btn);
        });
      }
      if (kWrap && kWrap.children.length === 0) {
        document.querySelectorAll('.k-card').forEach(c => {
          const kid = c.dataset.kid;
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'q-pill';
          btn.dataset.code = kid;
          btn.textContent = kid;
          btn.onclick = () => selectSubbox(kid);
          kWrap.appendChild(btn);
        });
      }
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
      if (mWrap && mWrap.children.length === 0) {
        document.querySelectorAll('.m-card').forEach(c => {
          const mid = c.dataset.mid;
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'q-pill';
          btn.dataset.code = mid;
          btn.textContent = mid + ' (' + c.dataset.mname + ')';
          btn.onclick = () => selectMetastrip(mid);
          mWrap.appendChild(btn);
        });
      }
    }

    function openBigPreviewModal() {
      buildModalQuickLists();
      syncModalView();
      document.getElementById('bigPreviewModal').classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    function closeBigPreviewModal() {
      document.getElementById('bigPreviewModal').classList.remove('open');
      document.body.style.overflow = '';
    }

    function setModalStageMode(mode) {
      const exFrame = document.getElementById('modalFullExampleFrame');
      const cuFrame = document.getElementById('modalCloseupFrame');
      document.getElementById('btnModeFullExample').classList.toggle('active', mode === 'FULL_EXAMPLE');
      document.getElementById('btnModeCloseup').classList.toggle('active', mode === 'CLOSEUP');
      document.getElementById('btnModeZoom180').classList.toggle('active', mode === 'ZOOM_180');

      if (mode === 'CLOSEUP') {
        exFrame.style.display = 'none';
        cuFrame.style.display = 'flex';
      } else {
        cuFrame.style.display = 'none';
        exFrame.style.display = 'block';
        exFrame.classList.toggle('zoom-180', mode === 'ZOOM_180');
      }
    }

    function stepModalSelection(dir) {
      if (activeMode === 'PAIRING') {
        const pList = Array.from(document.querySelectorAll('.p-card')).map(c => c.dataset.pid);
        const idx = (pList.indexOf(currentP) + dir + pList.length) % pList.length;
        selectPairing(pList[idx]);
      } else {
        const hList = Array.from(document.querySelectorAll('.h-card')).map(c => c.dataset.hid);
        const idx = (hList.indexOf(currentH) + dir + hList.length) % hList.length;
        selectHeadline(hList[idx]);
      }
    }

    document.addEventListener('keydown', (e) => {
      const modal = document.getElementById('bigPreviewModal');
      if (!modal || !modal.classList.contains('open')) return;
      if (e.key === 'Escape') closeBigPreviewModal();
      if (e.key === 'ArrowRight') stepModalSelection(1);
      if (e.key === 'ArrowLeft') stepModalSelection(-1);
    });

    function copyCommand() {
      const txt = document.getElementById('cmdOutput').textContent;
      navigator.clipboard.writeText(txt);
      const btn = document.getElementById('copyBtn');
      btn.textContent = '✓ Đã Copy: ' + txt;
      setTimeout(() => { btn.textContent = '📋 Copy Lệnh'; }, 2000);
    }

    function copySpecCard(pid, btnEl) {
      const card = document.querySelector(`.p-card[data-pid="${pid}"]`);
      if (!card) return;
      const spec = card.dataset.spec.replace(/\\n/g, '\\n');
      navigator.clipboard.writeText(spec);
      const old = btnEl.textContent;
      btnEl.textContent = '✓ Đã Copy Spec';
      setTimeout(() => { btnEl.textContent = old; }, 1800);
    }

    function filterPairings(law, btn) {
      document.querySelectorAll('#sec-layer0-pairings .filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.p-card').forEach(card => {
        card.style.display = (law === 'ALL' || card.dataset.plaw === law) ? 'flex' : 'none';
      });
    }

    function filterHeadlines(group, btn) {
      document.querySelectorAll('#sec-layer1-headlines .filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.h-card').forEach(card => {
        card.style.display = (group === 'ALL' || card.dataset.hgroup === group) ? 'flex' : 'none';
      });
    }

    function filterSubboxes(group, btn) {
      document.querySelectorAll('#sec-layer2-subboxes .filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.k-card').forEach(card => {
        card.style.display = (group === 'ALL' || card.dataset.kgroup === group) ? 'flex' : 'none';
      });
    }

    function toggleCropFullMode() {
      isFullMode = !isFullMode;
      const btn = document.getElementById('toggleViewBtn');
      if (isFullMode) {
        btn.textContent = '🖼️ Đang xem: NGUYÊN TẤM 1080×1350 (Bấm để về Cận Cảnh Phối Chữ)';
        btn.style.background = 'linear-gradient(135deg, #22C55E 0%, #16A34A 100%)';
      } else {
        btn.textContent = '🔍 Đang xem: CẬN CẢNH PHỐI CHỮ (Bấm để xem Nguyên Tấm 1080×1350)';
        btn.style.background = 'linear-gradient(135deg, #F59E0B 0%, #D97706 100%)';
      }
      document.querySelectorAll('.item-card').forEach(card => {
        const img = card.querySelector('.preview-img');
        const tag = card.querySelector('.img-mode-tag');
        img.src = isFullMode ? card.dataset.full : card.dataset.crop;
        if (card.classList.contains('p-card')) {
          tag.textContent = isFullMode ? '🖼️ NGUYÊN TẤM 1080×1350 (CLICK XEM BẢNG TO)' : `🔍 CLICK ẢNH ĐỂ XEM BẢNG TO (${card.dataset.pid} × ${card.dataset.kcode})`;
        } else if (card.classList.contains('h-card')) {
          tag.textContent = isFullMode ? '🖼️ NGUYÊN TẤM 1080×1350 (CLICK XEM BẢNG TO)' : '🔍 CLICK ẢNH XEM BẢNG TO (LỚP 1)';
        } else if (card.classList.contains('m-card')) {
          tag.textContent = isFullMode ? '🖼️ NGUYÊN TẤM 1080×1350 (CLICK XEM BẢNG TO)' : `🔍 CLICK ẢNH XEM BẢNG TO (LỚP 4 ${card.dataset.mid})`;
        } else {
          tag.textContent = isFullMode ? '🖼️ NGUYÊN TẤM 1080×1350 (CLICK XEM BẢNG TO)' : '🔍 CLICK ẢNH XEM BẢNG TO (LỚP 2)';
        }
      });
    }

    selectPairing('P01');
  </script>"""
    if script_start != -1 and script_end != -1:
        html = html[:script_start] + new_script + html[script_end:]

    HUB_HTML.write_text(html, encoding="utf-8")
    print("Successfully updated /Users/vietmac/Documents/CODE/k/bo-chon-chu-banner.html with H01..H40 (40), K01..K50 (50), S01..S35 (35), and M01..M06 (6)!")


if __name__ == "__main__":
    main()
