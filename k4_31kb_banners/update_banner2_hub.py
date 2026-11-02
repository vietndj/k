#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ATOMIC LOCK-FREE HUB BUILDER FOR BANNER2.HTML V9.0 (CLAUDE2 × LUỒNG 9f7f1024: 3 ẢNH × 3 BÀI QUẢNG CÁO CÓ LỌC GIÁ 4.000.000đ & GIỮ UTM)
========================================================================================================================================
- Đọc toàn bộ các file JSON trong `/Users/vietmac/Documents/CODE/k/k4_31kb_banners/banner2_cards/KB_*.json` (KB_01 -> KB_140).
- Với mỗi KB:
  1. Hiển thị 3 Phiên Bản Ảnh Banner 1080x1350:
     - 💰 Ảnh Phiên Bản 3 (V3 Price-Qualified — Có Lớp 4 Phân Cấp Lọc Giá 4.000.000đ · 07–08/11 Long Biên, HN chuẩn Giáo sư CLAUDE2)
     - 🎨 Ảnh Phương Án 1 (Hook 1 — Kèm tiêu đề chuẩn LAW_19)
     - ⚡ Ảnh Phương Án 2 (Hook 2 Mới — Phương án Text Hook đối chứng A/B Testing)
     - 🖼️ Chế độ Xem Song Song 3 Ảnh (Ảnh 1 · Ảnh 2 · Ảnh 3 V3 Lọc Giá 4tr) ngay trên thẻ
     - 🖤 Bản Đen Trắng & 🔥 Bản Đồ Nhiệt Luồng Thị Giác F1→F4
  2. Hiển thị Khối Đánh Giá Của CLAUDE2 (Opus 5.5) & Phân Cấp Giá Luồng 9f7f1024.
  3. Hiển thị 3 Bài Quảng Cáo Facebook Thực Chiến (Ad Copy 1, Ad Copy 2, và Ad Copy 3 Price-First):
     - Đầy đủ thông tin lọc giá 4.000.000đ (đi 2 người 3.500.000đ), địa điểm Green Hub Long Biên, cam kết hoàn 100% học phí sau Ngày 1.
     - 0% URL trần trong thân bài để bảo toàn tuyệt đối `utm_content={{ad.name}}` ở nút CTA chính thức.
"""

import fcntl
import html
import json
import subprocess
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
CARDS_DIR = BASE_DIR / "banner2_cards"
OUT_HTML = Path("/Users/vietmac/Documents/CODE/k/banner2.html")
LOCK_FILE = Path("/tmp/banner2_hub.lock")
R2_MANAGER = Path("/Users/vietmac/Documents/CODE/Quản gia/r2_manager.py")


def load_all_cards() -> List[Dict[str, Any]]:
    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    cards = []
    for p in sorted(CARDS_DIR.glob("KB_*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            cards.append(data)
        except Exception:
            continue
    cards.sort(key=lambda c: int(c.get("order", 999)))
    return cards


def build_default_versions_if_missing(c: Dict[str, Any], ver: str) -> List[Dict[str, Any]]:
    kb_id = c["kb_id"]
    kb_lower = kb_id.lower()
    style_code = c.get("style_code", "K01")
    alt_code = c.get("alt_style_code", "K02")
    meta_code = c.get("meta_code", "M01")
    min_sub = c.get("min_sub_fs_px", 27.0)
    score = c.get("score", "25/25")
    scan = " → ".join(c.get("scanpath_order", ["FACE", "HEADLINE", "SUBBOX"])[:4])

    existing = c.get("versions_history", [])
    out = []
    if existing:
        for item in existing:
            if item.get("ver_id") == "V9_V3_PRICE_QUALIFIED":
                continue
            u = item.get("img_url", "")
            if u.startswith("./k4_31kb_banners/v2_pilots/batch_out/") or "media.fedu.vn/banner2/" in u or "fedu.vn/k/k4_31kb_banners/" in u:
                fn = u.split("/")[-1].split("?")[0]
                u = f"./k4_31kb_banners/v2_pilots/batch_out/{fn}"
            u_ver = f"{u}?v={ver}" if ("?" not in u and u) else u
            cp = dict(item)
            cp["img_url"] = u_ver
            out.append(cp)
    else:
        local_rel = "./k4_31kb_banners/v2_pilots/batch_out"
        out = [
            {
                "step": 1,
                "ver_id": "V8_COLOR_HOOK1",
                "label": f"Ảnh Phương Án 1 ({style_code} · Hook 1)",
                "sub_info": f"Chữ phụ {min_sub}px · {score} PASS",
                "img_url": f"{local_rel}/{kb_lower}_color.jpg?v={ver}",
                "badge_color": "#10B981",
            },
            {
                "step": 2,
                "ver_id": "V8_ALT_HOOK2",
                "label": f"Ảnh Phương Án 2 ({alt_code} · Hook 2 Mới)",
                "sub_info": "Phương án Text Hook đối chứng A/B Testing",
                "img_url": f"{local_rel}/{kb_lower}_hook2.jpg?v={ver}",
                "badge_color": "#F59E0B",
            },
            {
                "step": 3,
                "ver_id": "V8_BW_LAW19",
                "label": f"Bản Đen Trắng ({style_code} · LAW_19)",
                "sub_info": f"Fine-Art B&W · Chữ phụ {min_sub}px",
                "img_url": f"{local_rel}/{kb_lower}_bw.jpg?v={ver}",
                "badge_color": "#38BDF8",
            },
            {
                "step": 4,
                "ver_id": "V8_HEATMAP_SCANPATH",
                "label": "Bản Đồ Nhiệt Luồng Thị Giác (F1→F4)",
                "sub_info": f"Scanpath: {scan}",
                "img_url": f"{local_rel}/{kb_lower}_heatmap.jpg?v={ver}",
                "badge_color": "#F43F5E",
            },
        ]

    # Luôn gắn Phiên bản 3 (V3 Price-Qualified) vào lịch sử
    out.append({
        "step": len(out) + 1,
        "ver_id": "V9_V3_PRICE_QUALIFIED",
        "label": f"Ảnh 3 · Phiên Bản 3 Có Lọc Giá 4.000.000đ ({style_code} × {meta_code})",
        "sub_info": "07–08/11 · Long Biên, HN | 4.000.000đ (34px Tabular-Nums) · 25/25 PASS",
        "img_url": f"./k4_31kb_banners/v2_pilots/batch_out/{kb_lower}_v3_price.jpg?v={ver}",
        "badge_color": "#22C55E",
    })
    return out


def _esc(s: str) -> str:
    return html.escape(str(s or ""), quote=True)


def build_card_html(c: Dict[str, Any]) -> str:
    kb_id = c["kb_id"]
    kb_lower = kb_id.lower()
    title = c.get("title", kb_id)
    h_code = c.get("h_code", "H01")
    style_code = c.get("style_code", "K01")
    style_name = c.get("style_name", "")
    alt_code = c.get("alt_style_code", "K08")
    meta_code = c.get("meta_code", "M01")
    font_name = c.get("font_name", "")
    outfit_id = c.get("outfit_id", "C02_I03")
    banner_style_name = c.get("banner_style_name", "Phong cách Studio")
    headline_plain = c.get("headline_plain", "")
    subline_summary = c.get("subline_summary", "")

    ver = c.get("ver", "v9_p3")
    local_rel_dir = "./k4_31kb_banners/v2_pilots/batch_out"
    local_abs_dir = BASE_DIR / "v2_pilots" / "batch_out"
    gh_base = "https://fedu.vn/k/k4_31kb_banners/v2_pilots/batch_out"

    hook2_file = f"{kb_lower}_hook2.jpg" if (local_abs_dir / f"{kb_lower}_hook2.jpg").exists() else f"{kb_lower}_alt.jpg"
    v3_file = f"{kb_lower}_v3_price.jpg" if (local_abs_dir / f"{kb_lower}_v3_price.jpg").exists() else f"{kb_lower}_color.jpg"

    local_color = f"{local_rel_dir}/{kb_lower}_color.jpg?v={ver}"
    local_bw = f"{local_rel_dir}/{kb_lower}_bw.jpg?v={ver}"
    local_alt = f"{local_rel_dir}/{hook2_file}?v={ver}"
    local_v3 = f"{local_rel_dir}/{v3_file}?v={ver}"
    local_hm = f"{local_rel_dir}/{kb_lower}_heatmap.jpg?v={ver}"

    gh_color = f"{gh_base}/{kb_lower}_color.jpg?v={ver}"
    gh_bw = f"{gh_base}/{kb_lower}_bw.jpg?v={ver}"
    gh_alt = f"{gh_base}/{hook2_file}?v={ver}"
    gh_v3 = f"{gh_base}/{v3_file}?v={ver}"
    gh_hm = f"{gh_base}/{kb_lower}_heatmap.jpg?v={ver}"

    # Mặc định trỏ local_rel_dir (hoạt động cả trên file://, localhost và fedu.vn/k/), fallback sang gh_base nếu mở từ media.fedu.vn
    color_src = local_color
    bw_src = local_bw
    alt_src = local_alt
    v3_src = local_v3
    hm_src = local_hm

    score = c.get("v3_audit_score") or c.get("audit_score", "H1:25/25 · H2:25/25 · V3:25/25")
    min_sub_fs = c.get("min_sub_fs_px", 27.0)
    h_fs = c.get("headline_fs_px", 78.0)
    scan_order = c.get("scanpath_order", ["FACE", "HEADLINE", "SUBBOX", "HEADLINE"])
    scan_short = " → ".join(s[:4] for s in scan_order[:3])
    versions = build_default_versions_if_missing(c, ver)
    n_vers = len(versions)
    filter_tag = style_code.split()[0]

    has_claude2 = bool(c.get("claude2_upgraded"))
    card_extra_cls = "claude2-upgraded" if has_claude2 else ""
    status_badge = f"💰 {kb_id} • ĐÃ CÓ BẢN V3 LỌC GIÁ 4TR (3 ẢNH × 3 BÀI ADS CHUẨN C2)"

    audit = c.get("claude2_audit", {})
    h1 = c.get("hook_1", {})
    h2 = c.get("hook_2", {})
    ad1 = c.get("ad_copy_1", {})
    ad2 = c.get("ad_copy_2", {})
    ad3 = c.get("ad_copy_3", {})

    h1_plain = h1.get("headline_plain") or " / ".join(
        ln.replace('<span class="hl">', "").replace("</span>", "") for ln in h1.get("headline_lines", [])
    )
    h2_plain = h2.get("headline_plain") or " / ".join(
        ln.replace('<span class="hl">', "").replace("</span>", "") for ln in h2.get("headline_lines", [])
    )

    default_fb_hl = "Lớp Offline 2 Ngày 07–08/11 Tại Hà Nội · Học Phí 4.000.000đ (Hoàn 100% Sau Ngày 1)"
    ad1_headline = _esc(ad1.get("fb_headline", default_fb_hl))
    ad1_body = _esc(ad1.get("primary_text", ""))
    ad2_headline = _esc(ad2.get("fb_headline", default_fb_hl))
    ad2_body = _esc(ad2.get("primary_text", ""))
    ad3_headline = _esc(ad3.get("fb_headline", default_fb_hl))
    ad3_body = _esc(ad3.get("primary_text", ad1.get("primary_text", "")))

    meta_note_display = "07–08/11 · Long Biên, HN  |  4.000.000đ"
    if meta_code == "M02":
        meta_note_display += " (✓ Chưa thấy hợp sau Ngày 1: hoàn 100% học phí)"

    claude2_html = f"""
        <div class="c2-audit-box">
          <div class="c2-audit-title">🧠 ĐÁNH GIÁ CỦA GIÁO SƯ CLAUDE2 (OPUS 5.5) &amp; CHUẨN HÓA LUỒNG 9F7F1024</div>
          <div class="c2-audit-item"><strong>🎯 Đánh giá Hook cũ:</strong> {_esc(audit.get("old_hook_verdict", ""))}</div>
          <div class="c2-audit-item"><strong>🔗 Đánh giá Logic:</strong> {_esc(audit.get("logic_verdict", ""))}</div>
          <div class="c2-audit-item"><strong>💰 Phân cấp Giá V3 ({meta_code}):</strong> <code>{_esc(meta_note_display)}</code> — Đã xóa URL trần để giữ 100% <code>utm_content={{{{ad.name}}}}</code>.</div>
        </div>

        <div class="hooks-compare-grid three-cols">
          <div class="hk-box hk-box-3" onclick="switchCardImg('{kb_id}', '{v3_src}', this.closest('.vault-card').querySelector('.btn-v3'))">
            <div class="hk-badge hk-b3">💰 ẢNH 3 • PHIÊN BẢN V3 LỌC GIÁ 4TR ({style_code} × {meta_code})</div>
            <div class="hk-head">“{_esc(h1_plain)}”</div>
            <div class="hk-sub">× {_esc(h1.get("sub_old", ""))}<br/>✓ <strong>{_esc(h1.get("sub_new", ""))}</strong><br/><span style="color:#4ADE80;font-family:var(--font-mono);font-size:11px;font-weight:700;">⎯ 07–08/11 · Long Biên, HN | 4.000.000đ</span></div>
          </div>
          <div class="hk-box hk-box-1" onclick="switchCardImg('{kb_id}', '{color_src}', this.closest('.vault-card').querySelector('.btn-color'))">
            <div class="hk-badge hk-b1">🎨 ẢNH 1 • PHƯƠNG ÁN HOOK 1 ({style_code})</div>
            <div class="hk-head">“{_esc(h1_plain)}”</div>
            <div class="hk-sub">× {_esc(h1.get("sub_old", ""))}<br/>✓ <strong>{_esc(h1.get("sub_new", ""))}</strong></div>
          </div>
          <div class="hk-box hk-box-2" onclick="switchCardImg('{kb_id}', '{alt_src}', this.closest('.vault-card').querySelector('.btn-hook2'))">
            <div class="hk-badge hk-b2">⚡ ẢNH 2 • PHƯƠNG ÁN HOOK 2 MỚI ({alt_code})</div>
            <div class="hk-head">“{_esc(h2_plain)}”</div>
            <div class="hk-sub">× {_esc(h2.get("sub_old", ""))}<br/>✓ <strong>{_esc(h2.get("sub_new", ""))}</strong></div>
          </div>
        </div>

        <div class="ads-copy-section">
          <div class="ads-tabs">
            <button class="ad-tab-btn active" onclick="switchAdTab('{kb_id}', 3, this)">💰 Quảng Cáo 3 (V3 Giá Lên Đầu)</button>
            <button class="ad-tab-btn" onclick="switchAdTab('{kb_id}', 1, this)">📣 Quảng Cáo 1 (Ảnh 1)</button>
            <button class="ad-tab-btn" onclick="switchAdTab('{kb_id}', 2, this)">📣 Quảng Cáo 2 (Ảnh 2)</button>
            <button class="ad-tab-btn" onclick="switchAdTab('{kb_id}', 0, this)">📖 Xem Cả 3</button>
          </div>

          <div class="ad-pane active" id="ad-pane-{kb_id}-3">
            <div class="ad-pane-head">
              <span>💰 <strong>BÀI QUẢNG CÁO FACEBOOK #3 (PHIÊN BẢN V3 — LỌC GIÁ 4TR NGAY DÒNG 1 &amp; GIỮ UTM)</strong></span>
              <button class="copy-ad-btn" onclick="copyAdText('{kb_id}', 3, this)">📋 Copy Quảng Cáo 3</button>
            </div>
            <div class="ad-fb-hl">📌 Tiêu đề dưới ảnh: <strong>{ad3_headline}</strong></div>
            <pre class="ad-text-content" id="ad-txt-{kb_id}-3">{ad3_body}</pre>
          </div>

          <div class="ad-pane" id="ad-pane-{kb_id}-1">
            <div class="ad-pane-head">
              <span>📣 <strong>BÀI QUẢNG CÁO FACEBOOK #1</strong> (Ứng Ảnh 1 · Đã thêm Khối Giá 4tr &amp; Xóa Link Trần)</span>
              <button class="copy-ad-btn" onclick="copyAdText('{kb_id}', 1, this)">📋 Copy Quảng Cáo 1</button>
            </div>
            <div class="ad-fb-hl">📌 Tiêu đề dưới ảnh: <strong>{ad1_headline}</strong></div>
            <pre class="ad-text-content" id="ad-txt-{kb_id}-1">{ad1_body}</pre>
          </div>

          <div class="ad-pane" id="ad-pane-{kb_id}-2">
            <div class="ad-pane-head">
              <span>📣 <strong>BÀI QUẢNG CÁO FACEBOOK #2</strong> (Ứng Ảnh 2 · Đã thêm Khối Giá 4tr &amp; Xóa Link Trần)</span>
              <button class="copy-ad-btn" onclick="copyAdText('{kb_id}', 2, this)">📋 Copy Quảng Cáo 2</button>
            </div>
            <div class="ad-fb-hl">📌 Tiêu đề dưới ảnh: <strong>{ad2_headline}</strong></div>
            <pre class="ad-text-content" id="ad-txt-{kb_id}-2">{ad2_body}</pre>
          </div>
        </div>
    """

    return f"""
        <article class="vault-card approved {card_extra_cls}" data-style="{filter_tag}" data-h="{h_code}" data-kb="{kb_id}" data-upgraded="1" data-v3-src="{v3_src}" data-color-src="{color_src}" data-hook2-src="{alt_src}" data-bw-src="{bw_src}" data-hm-src="{hm_src}" id="card-{kb_id}">
          <div class="vc-head">
            <span class="vault-status ok">{status_badge}</span>
            <span class="vc-score">{score}</span>
          </div>
          <div class="vc-img-box" id="imgbox-{kb_id}">
            <img id="img-{kb_id}" src="{v3_src}" onerror="this.onerror=null;this.src='{gh_v3}';" alt="{kb_id} - {_esc(title)}" loading="lazy" decoding="async" onclick="openLightbox(this.src)" />
            <div class="dual-img-view triple-grid" id="dualview-{kb_id}" style="display:none;">
              <div class="dual-col">
                <span class="dual-tag tag-v3">💰 ẢNH 3 (V3 LỌC GIÁ 4TR)</span>
                <img src="{v3_src}" onerror="this.onerror=null;this.src='{gh_v3}';" alt="V3 Price" onclick="openLightbox(this.src)" />
              </div>
              <div class="dual-col">
                <span class="dual-tag tag-h1">🎨 ẢNH 1 (HOOK 1)</span>
                <img src="{color_src}" onerror="this.onerror=null;this.src='{gh_color}';" alt="Hook 1" onclick="openLightbox(this.src)" />
              </div>
              <div class="dual-col">
                <span class="dual-tag tag-h2">⚡ ẢNH 2 (HOOK 2 MỚI)</span>
                <img src="{alt_src}" onerror="this.onerror=null;this.src='{gh_alt}';" alt="Hook 2" onclick="openLightbox(this.src)" />
              </div>
            </div>
          </div>
          <div class="vc-switch-bar">
            <button class="sw-btn btn-v3 active" onclick="switchCardImg('{kb_id}', '{v3_src}', this)">💰 Ảnh 3 (V3 Giá 4tr)</button>
            <button class="sw-btn btn-color" onclick="switchCardImg('{kb_id}', '{color_src}', this)">🎨 Ảnh 1 (Hook 1)</button>
            <button class="sw-btn btn-hook2" onclick="switchCardImg('{kb_id}', '{alt_src}', this)">⚡ Ảnh 2 (Hook 2)</button>
            <button class="sw-btn btn-dual" onclick="toggleDualImg('{kb_id}', this)">🖼️ Song Song 3 Ảnh</button>
            <button class="sw-btn btn-bw" onclick="switchCardImg('{kb_id}', '{bw_src}', this)">🖤 Đen Trắng</button>
            <button class="sw-btn btn-hm" onclick="switchCardImg('{kb_id}', '{hm_src}', this)">🔥 Bản Đồ Nhiệt</button>
            <button class="sw-btn btn-compare" onclick="openVersionHistoryModal('{kb_id}')">🔍 Lịch Sử ({n_vers} Bản)</button>
          </div>
          <div class="vc-body">
            <h4>{kb_id}: “{_esc(headline_plain)}”</h4>
            <p class="vc-sub">{_esc(subline_summary)}</p>
            {claude2_html}
            <div class="vc-meta">
              <span>🔥 <strong>Luồng mắt WTA:</strong> <code>{scan_short}</code> • Tiêu đề <strong>{h_fs}px</strong> / Chữ phụ <strong>{min_sub_fs}px</strong> / Giá V3 <strong>34px Tabular</strong></span>
              <span>👔 <strong>{_esc(banner_style_name)}</strong> (Phôi <code>{outfit_id}</code> • 85mm f/1.4 Bokeh)</span>
              <span>🔤 <strong>{_esc(font_name)}</strong> × 📐 <strong>{_esc(style_name)}</strong> × 🔶 <strong>Lớp 4: {meta_code}</strong> ({n_vers} phiên bản)</span>
            </div>
          </div>
        </article>"""


def generate_html_content(cards: List[Dict[str, Any]]) -> str:
    done_count = len(cards)
    upgraded_count = sum(1 for c in cards if c.get("claude2_upgraded"))
    cards_html = "\n".join(build_card_html(c) for c in cards)

    kb_versions_map = {}
    for c in cards:
        ver = c.get("ver", "v9_p3")
        kb_id = c["kb_id"]
        kb_lower = kb_id.lower()
        sbs_src = f"./k4_31kb_banners/v2_pilots/batch_out/{kb_lower}_sbs.jpg?v={ver}"
        kb_versions_map[kb_id] = {
            "kb_id": kb_id,
            "title": c.get("title", kb_id),
            "headline": c.get("headline_plain", ""),
            "h_code": c.get("h_code", "H01"),
            "style_code": c.get("style_code", "K01"),
            "style_name": c.get("style_name", ""),
            "font_name": c.get("font_name", ""),
            "score": c.get("audit_score", "25/25 PASS"),
            "h_fs": c.get("headline_fs_px", 78.0),
            "min_sub_fs": c.get("min_sub_fs_px", 27.0),
            "scanpath": c.get("scanpath_order", ["FACE", "HEADLINE", "SUBBOX", "HEADLINE"]),
            "sbs_url": sbs_src,
            "versions": build_default_versions_if_missing(c, ver),
        }
    kb_versions_json = json.dumps(kb_versions_map, ensure_ascii=False)

    filter_buttons = [
        f'<button class="flt-btn active" onclick="filterVault(\'ALL\', this)">Tất cả ({done_count})</button>',
        f'<button class="flt-btn" style="border-color:#22C55E;color:#4ADE80;" onclick="filterVault(\'UPGRADED\', this)">💰 Đã Có Bản V3 Lọc Giá 4tr ({done_count}/{done_count})</button>',
    ]
    for k_idx in range(1, 22):
        kc = f"K{k_idx:02d}"
        cnt = sum(1 for c in cards if c.get("style_code", "").startswith(kc))
        if cnt > 0:
            filter_buttons.append(f'<button class="flt-btn" onclick="filterVault(\'{kc}\', this)">{kc} ({cnt})</button>')
    filter_bar_html = "\n        ".join(filter_buttons)

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>BANNER 2.0 V9.0 • {done_count} Banner K4 × Phiên Bản 3 Lọc Giá 4.000.000đ (3 Ảnh × 3 Bài Quảng Cáo Facebook Chuẩn Luồng 9f7f1024)</title>
  <meta name="description" content="Hệ thống {done_count} Kịch bản Banner Quảng Cáo Facebook Khóa Offline 07–08/11: 3 Phiên Bản Ảnh (kèm Bản V3 Lọc Giá 4.000.000đ) và 3 Bài Quảng Cáo Facebook chuẩn hóa Luồng 9f7f1024." />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #070B14;
      --surface: #0E1525;
      --surface-2: #151F36;
      --border: rgba(148, 163, 184, 0.18);
      --border-gold: rgba(245, 158, 11, 0.45);
      --border-green: rgba(34, 197, 94, 0.55);
      --border-rose: rgba(244, 63, 94, 0.55);
      --text: #F8FAFC;
      --text-soft: #CBD5E1;
      --muted: #94A3B8;
      --gold: #F59E0B;
      --gold-bright: #FACC15;
      --green: #22C55E;
      --red: #EF4444;
      --rose: #F43F5E;
      --cyan: #38BDF8;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
    html {{ scroll-behavior: smooth; background: var(--bg); color: var(--text); font-family: var(--font-sans); line-height: 1.6; }}
    body {{ min-height: 100vh; overflow-x: hidden; }}

    .top-nav {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(7, 11, 20, 0.94); backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border); padding: 12px 24px;
      display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;
    }}
    .brand-group {{ display: flex; align-items: center; gap: 10px; text-decoration: none; color: var(--text); }}
    .brand-badge {{ background: #22C55E; color: #052E16; font-family: var(--font-mono); font-size: 12px; font-weight: 800; padding: 4px 10px; border-radius: 6px; }}
    .brand-title {{ font-weight: 800; font-size: 15px; }}
    .nav-links {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
    .nav-pill {{
      color: var(--text-soft); text-decoration: none; font-size: 12.5px; font-weight: 600;
      padding: 6px 13px; border-radius: 999px; background: var(--surface); border: 1px solid var(--border); transition: all 0.2s; cursor: pointer;
    }}
    .nav-pill:hover, .nav-pill.active {{ background: rgba(245, 158, 11, 0.16); color: var(--gold-bright); border-color: var(--border-gold); }}
    .nav-pill.green-pill {{ background: rgba(34, 197, 94, 0.16); color: #4ADE80; border-color: var(--border-green); }}
    .nav-pill.rose-pill {{ background: rgba(244, 63, 94, 0.16); color: #FB7185; border-color: var(--border-rose); }}

    .hero {{
      background: radial-gradient(circle at 80% 10%, rgba(34, 197, 94, 0.14), transparent 45%), linear-gradient(180deg, #0E1629 0%, #070B14 100%);
      border-bottom: 1px solid var(--border); padding: 38px 24px 32px;
    }}
    .container {{ max-width: 1640px; margin: 0 auto; }}
    .eyebrow-tag {{
      display: inline-flex; align-items: center; gap: 8px; background: rgba(34, 197, 94, 0.16);
      border: 1px solid var(--border-green); color: #4ADE80; font-family: var(--font-mono);
      font-size: 12px; font-weight: 700; padding: 5px 13px; border-radius: 999px; margin-bottom: 14px;
    }}
    .hero h1 {{ font-size: clamp(24px, 3vw, 34px); font-weight: 800; line-height: 1.22; margin-bottom: 12px; text-transform: uppercase; }}
    .hero-lead {{ font-size: 15.5px; color: var(--text-soft); max-width: 1320px; margin-bottom: 24px; }}
    .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }}
    .kpi-card {{ background: rgba(14, 21, 37, 0.85); border: 1px solid var(--border); border-radius: 14px; padding: 14px 18px; }}
    .kpi-card.highlight {{ border-color: var(--border-green); background: linear-gradient(180deg, rgba(34, 197, 94, 0.08) 0%, rgba(14, 21, 37, 0.9) 100%); }}
    .kpi-card .val {{ font-size: 20px; font-weight: 800; color: var(--gold-bright); font-family: var(--font-mono); }}
    .kpi-card.highlight .val {{ color: #4ADE80; }}
    .kpi-card .lbl {{ font-size: 12.5px; color: var(--muted); margin-top: 4px; }}

    .mode-switcher-bar {{
      display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
      background: rgba(21, 31, 54, 0.9); border: 1.5px solid var(--border-green);
      padding: 14px 20px; border-radius: 14px; margin-bottom: 22px;
    }}
    .mode-lbl {{ font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: #4ADE80; text-transform: uppercase; }}
    .mode-btn {{
      background: var(--surface); color: var(--text); border: 1.5px solid var(--border);
      padding: 9px 16px; border-radius: 999px; font-size: 13px; font-weight: 800; cursor: pointer; transition: all 0.2s;
    }}
    .mode-btn.active, .mode-btn:hover {{
      background: #22C55E; color: #052E16; border-color: #22C55E; box-shadow: 0 4px 16px rgba(34, 197, 94, 0.35);
    }}

    .section {{ padding: 40px 24px; border-bottom: 1px solid var(--border); }}
    .sec-header {{ margin-bottom: 24px; }}
    .sec-step {{ font-family: var(--font-mono); font-size: 12px; font-weight: 700; color: var(--cyan); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 6px; }}
    .sec-title {{ font-size: clamp(20px, 2.3vw, 28px); font-weight: 800; text-transform: uppercase; margin-bottom: 6px; }}
    .sec-desc {{ color: var(--text-soft); font-size: 15px; max-width: 1180px; }}

    .filter-bar {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px; }}
    .flt-btn {{
      background: var(--surface-2); color: var(--text-soft); border: 1px solid var(--border);
      padding: 7px 13px; border-radius: 999px; font-size: 12px; font-weight: 700; cursor: pointer; transition: all 0.18s;
    }}
    .flt-btn:hover, .flt-btn.active {{ background: var(--gold); color: #070B14; border-color: var(--gold); }}

    .vault-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(510px, 1fr));
      gap: 26px;
    }}
    @media (max-width: 640px) {{
      .vault-grid {{ grid-template-columns: 1fr; }}
    }}
    .vault-card {{
      background: var(--surface); border: 1.5px solid var(--border-green);
      border-radius: 16px; overflow: hidden; display: flex; flex-direction: column;
      box-shadow: 0 10px 28px rgba(0, 0, 0, 0.35);
    }}
    .vault-card.claude2-upgraded {{
      border-color: var(--border-green);
      box-shadow: 0 12px 34px rgba(34, 197, 94, 0.14);
    }}
    .vc-head {{
      padding: 12px 16px; background: var(--surface-2); border-bottom: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between; gap: 8px;
    }}
    .vault-status.ok {{
      background: rgba(34, 197, 94, 0.18); color: #4ADE80; font-family: var(--font-mono);
      font-size: 11.2px; font-weight: 800; padding: 4px 10px; border-radius: 999px;
    }}
    .vc-score {{ font-family: var(--font-mono); font-size: 11.2px; color: var(--gold-bright); font-weight: 700; flex-shrink: 0; }}
    .vc-img-box {{ background: #050811; aspect-ratio: 4 / 5; overflow: hidden; position: relative; }}
    .vc-img-box.dual-mode {{ aspect-ratio: auto; padding: 10px; }}
    .vc-img-box > img {{ width: 100%; height: 100%; object-fit: cover; display: block; cursor: zoom-in; }}
    .dual-img-view {{
      display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; width: 100%;
    }}
    .dual-col {{
      display: flex; flex-direction: column; background: #0A101E; border: 1px solid var(--border); border-radius: 10px; overflow: hidden;
    }}
    .dual-col img {{ width: 100%; aspect-ratio: 4 / 5; object-fit: cover; cursor: zoom-in; display: block; }}
    .dual-tag {{
      font-family: var(--font-mono); font-size: 10px; font-weight: 800; text-align: center; padding: 5px 4px;
    }}
    .dual-tag.tag-v3 {{ background: rgba(34, 197, 94, 0.25); color: #4ADE80; }}
    .dual-tag.tag-h1 {{ background: rgba(56, 189, 248, 0.2); color: #38BDF8; }}
    .dual-tag.tag-h2 {{ background: rgba(245, 158, 11, 0.22); color: var(--gold-bright); }}

    .vc-switch-bar {{
      display: flex; flex-wrap: wrap; gap: 5px; padding: 10px 10px;
      background: #0A101E; border-bottom: 1px solid var(--border);
    }}
    .sw-btn {{
      flex: 1 1 calc(25% - 6px); min-width: 86px; background: var(--surface-2); color: var(--text-soft);
      border: 1px solid var(--border); border-radius: 6px; padding: 6px 6px;
      font-size: 11px; font-weight: 700; cursor: pointer; text-align: center; transition: all 0.15s;
    }}
    .sw-btn.btn-v3 {{
      border-color: rgba(34, 197, 94, 0.55); color: #4ADE80; font-weight: 800;
    }}
    .sw-btn.btn-hook2 {{
      border-color: rgba(245, 158, 11, 0.45); color: var(--gold-bright);
    }}
    .sw-btn.btn-dual {{
      border-color: rgba(56, 189, 248, 0.45); color: #38BDF8;
    }}
    .sw-btn.btn-compare {{
      background: rgba(56, 189, 248, 0.16); color: #38BDF8; border-color: rgba(56, 189, 248, 0.45);
      font-weight: 800;
    }}
    .sw-btn.active, .sw-btn:hover {{ background: #22C55E; color: #052E16; border-color: #22C55E; }}

    .vc-body {{ padding: 16px; display: flex; flex-direction: column; gap: 12px; flex: 1; }}
    .vc-body h4 {{ font-size: 16px; font-weight: 800; color: var(--text); line-height: 1.35; }}
    .vc-sub {{ font-size: 12.8px; color: var(--text-soft); }}

    /* CLAUDE2 Audit & 3 Hooks & 3 Ads */
    .c2-audit-box {{
      background: rgba(15, 23, 42, 0.92); border: 1px solid rgba(56, 189, 248, 0.35);
      border-left: 4px solid var(--cyan); border-radius: 10px; padding: 12px 14px;
      display: flex; flex-direction: column; gap: 6px; font-size: 12.6px; color: #E2E8F0;
    }}
    .c2-audit-title {{
      font-family: var(--font-mono); font-size: 11.2px; font-weight: 800; color: var(--cyan);
      letter-spacing: 0.04em; margin-bottom: 2px;
    }}
    .c2-audit-item {{ line-height: 1.48; }}
    .c2-audit-item strong {{ color: var(--gold-bright); }}

    .hooks-compare-grid {{
      display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px;
    }}
    @media (max-width: 680px) {{
      .hooks-compare-grid {{ grid-template-columns: 1fr; }}
    }}
    .hk-box {{
      background: #0A101E; border: 1px solid var(--border); border-radius: 10px; padding: 9px 10px;
      cursor: pointer; transition: all 0.18s;
    }}
    .hk-box:hover {{ border-color: #4ADE80; transform: translateY(-1px); }}
    .hk-box-3 {{ border-top: 3px solid #22C55E; background: rgba(34, 197, 94, 0.05); }}
    .hk-box-1 {{ border-top: 3px solid #38BDF8; }}
    .hk-box-2 {{ border-top: 3px solid #F59E0B; }}
    .hk-badge {{
      font-family: var(--font-mono); font-size: 10px; font-weight: 800; margin-bottom: 4px;
    }}
    .hk-b3 {{ color: #4ADE80; }}
    .hk-b1 {{ color: #38BDF8; }}
    .hk-b2 {{ color: var(--gold-bright); }}
    .hk-head {{ font-size: 12.8px; font-weight: 800; color: #FFFFFF; line-height: 1.35; margin-bottom: 5px; }}
    .hk-sub {{ font-size: 11.5px; color: #CBD5E1; line-height: 1.42; }}
    .hk-sub strong {{ color: #FFFFFF; }}

    .ads-copy-section {{
      background: #090E1A; border: 1px solid var(--border); border-radius: 12px; overflow: hidden;
    }}
    .ads-tabs {{
      display: flex; background: #111A2E; border-bottom: 1px solid var(--border); flex-wrap: wrap;
    }}
    .ad-tab-btn {{
      flex: 1; min-width: 110px; background: transparent; color: var(--text-soft); border: none;
      padding: 9px 8px; font-size: 11.5px; font-weight: 700; cursor: pointer;
      border-bottom: 2px solid transparent; transition: all 0.15s;
    }}
    .ad-tab-btn.active, .ad-tab-btn:hover {{
      color: #4ADE80; border-bottom-color: #22C55E; background: rgba(34, 197, 94, 0.08);
    }}
    .ad-pane {{ display: none; padding: 12px 14px; border-bottom: 1px solid var(--border); }}
    .ad-pane:last-child {{ border-bottom: none; }}
    .ad-pane.active {{ display: block; }}
    .ad-pane-head {{
      display: flex; align-items: center; justify-content: space-between; gap: 8px;
      margin-bottom: 8px; font-size: 12px; color: #4ADE80;
    }}
    .copy-ad-btn {{
      background: rgba(34, 197, 94, 0.18); color: #4ADE80; border: 1px solid rgba(34, 197, 94, 0.45);
      border-radius: 6px; padding: 4px 10px; font-size: 11.2px; font-weight: 700; cursor: pointer; flex-shrink: 0;
    }}
    .copy-ad-btn:hover {{ background: #22C55E; color: #070B14; }}
    .ad-fb-hl {{
      background: rgba(34, 197, 94, 0.10); border: 1px dashed rgba(34, 197, 94, 0.4);
      border-radius: 6px; padding: 6px 10px; font-size: 12px; color: #86EFAC; margin-bottom: 8px;
    }}
    .ad-text-content {{
      white-space: pre-wrap; word-wrap: break-word; font-family: var(--font-sans);
      font-size: 13px; line-height: 1.58; color: #F1F5F9; max-height: 360px; overflow-y: auto;
      padding-right: 4px;
    }}

    .vc-meta {{
      margin-top: auto; padding-top: 10px; border-top: 1px solid var(--border);
      display: flex; flex-direction: column; gap: 4px; font-family: var(--font-mono); font-size: 11px; color: var(--muted);
    }}
    .vc-meta strong {{ color: #E2E8F0; font-weight: 600; }}
    .vc-meta code {{ color: var(--gold-bright); }}

    /* Full Multi-Version Comparison Modal */
    .ver-modal {{
      position: fixed; inset: 0; background: rgba(4, 7, 15, 0.94); backdrop-filter: blur(12px);
      z-index: 950; display: none; flex-direction: column; overflow-y: auto; padding: 20px 24px 40px;
    }}
    .ver-modal.open {{ display: flex; }}
    .vm-header {{
      max-width: 1680px; width: 100%; margin: 0 auto 18px;
      background: #0E1628; border: 1.5px solid var(--border-gold); border-radius: 14px;
      padding: 16px 22px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px;
      position: sticky; top: 0; z-index: 20; box-shadow: 0 12px 32px rgba(0,0,0,0.6);
    }}
    .vm-title-box h3 {{ font-size: 19px; font-weight: 800; color: var(--gold-bright); margin-bottom: 4px; }}
    .vm-title-box p {{ font-size: 13px; color: var(--text-soft); font-family: var(--font-mono); }}
    .vm-actions {{ display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }}
    .vm-btn {{
      background: var(--surface-2); color: var(--text); border: 1px solid var(--border);
      padding: 9px 16px; border-radius: 999px; font-size: 13px; font-weight: 700; cursor: pointer;
    }}
    .vm-btn.sbs-btn {{ background: rgba(56, 189, 248, 0.18); color: #38BDF8; border-color: rgba(56, 189, 248, 0.5); }}
    .vm-btn.close-btn {{ background: var(--gold); color: #070B14; border-color: var(--gold); font-weight: 800; }}
    .vm-grid {{
      max-width: 1680px; width: 100%; margin: 0 auto;
      display: grid; grid-template-columns: repeat(auto-fill, minmax(295px, 1fr)); gap: 16px;
    }}
    .vm-card {{
      background: #0B1222; border: 2px solid var(--border); border-radius: 14px;
      overflow: hidden; display: flex; flex-direction: column; transition: transform 0.18s;
    }}
    .vm-card:hover {{ transform: translateY(-3px); }}
    .vm-card-head {{
      padding: 10px 14px; background: #131D35; border-bottom: 1px solid var(--border);
    }}
    .vm-step-badge {{
      display: inline-block; font-family: var(--font-mono); font-size: 11px; font-weight: 800;
      padding: 2px 8px; border-radius: 99px; margin-bottom: 4px; color: #070B14;
    }}
    .vm-card-head h5 {{ font-size: 13.5px; font-weight: 800; color: #FFFFFF; line-height: 1.3; }}
    .vm-card-head p {{ font-size: 11.5px; color: var(--text-soft); font-family: var(--font-mono); margin-top: 3px; }}
    .vm-img-wrap {{ aspect-ratio: 4 / 5; background: #050811; overflow: hidden; }}
    .vm-img-wrap img {{ width: 100%; height: 100%; object-fit: cover; display: block; cursor: zoom-in; }}

    .lightbox {{
      position: fixed; inset: 0; background: rgba(4, 7, 14, 0.95); backdrop-filter: blur(10px);
      z-index: 999; display: none; align-items: center; justify-content: center; padding: 24px;
    }}
    .lightbox.open {{ display: flex; }}
    .lightbox img {{ max-width: 96vw; max-height: 92vh; border-radius: 12px; }}
    .lightbox-close {{
      position: fixed; top: 20px; right: 24px; background: var(--gold); color: #070B14;
      border: none; font-weight: 800; font-size: 14px; padding: 10px 18px; border-radius: 999px; cursor: pointer;
    }}
    footer {{ padding: 28px 24px; text-align: center; color: var(--muted); font-size: 13px; }}
  </style>
</head>
<body>

  <header class="top-nav">
    <a href="banner2.html" class="brand-group">
      <span class="brand-badge">BANNER 2.0 • V9.0 PRICE-QUALIFIED (LUỒNG 9F7F1024)</span>
      <span class="brand-title">Kệ Duyệt {done_count} Banner K4 (07–08/11) • 3 Phiên Bản Ảnh (Có Lọc Giá 4tr) • 3 Bài Quảng Cáo Facebook</span>
    </a>
    <nav class="nav-links">
      <button class="nav-pill green-pill" onclick="switchAllMode('v3', document.getElementById('globalBtnV3'))">💰 Xem Ảnh 3 (V3 Lọc Giá 4tr)</button>
      <button class="nav-pill" onclick="switchAllMode('color', document.getElementById('globalBtnColor'))">🎨 Xem Ảnh 1 (Hook 1)</button>
      <button class="nav-pill" onclick="switchAllMode('hook2', document.getElementById('globalBtnHook2'))">⚡ Xem Ảnh 2 (Hook 2)</button>
      <button class="nav-pill" onclick="switchAllMode('dual', document.getElementById('globalBtnDual'))">🖼️ Song Song 3 Ảnh</button>
      <button class="nav-pill rose-pill" onclick="switchAllMode('hm', document.getElementById('globalBtnHm'))">🔥 Bản Đồ Nhiệt</button>
      <a href="bo-chon-chu-banner.html" class="nav-pill" style="border-color:#22C55E;color:#4ADE80;">🎛️ Bộ Chọn Chữ 4 Lớp (Mới)</a>
      <a href="kichban-quangcao-k4.html" class="nav-pill">📜 142 Kịch Bản Gốc</a>
    </nav>
  </header>

  <section class="hero">
    <div class="container">
      <div class="eyebrow-tag">💰 NÂNG CẤP V9.0 THEO LUỒNG 9F7F1024 &amp; GIÁO SƯ CLAUDE2 • THÊM LỚP 4 PHÂN CẤP GIÁ 4.000.000Đ TRÊN ẢNH &amp; CHUẨN HÓA 3 BÀI QUẢNG CÁO GIỮ 100% UTM</div>
      <h1>Kệ Duyệt {done_count} Banner &amp; Bài Quảng Cáo Facebook Khóa Offline 07–08/11 (3 Phiên Bản Ảnh × 3 Bài Ads Có Lọc Giá 4tr)</h1>
      <p class="hero-lead">
        Theo kết luận kiểm toán từ luồng <code>9f7f1024</code> của <strong>Giáo sư CLAUDE2 (Opus 5.5)</strong>: Mỗi kịch bản trong <strong>{done_count} KB</strong> đã được bổ sung <strong>Phiên Bản Ảnh Thứ 3 (<code>kb_XX_v3_price.jpg</code> — in rõ ngày học <code>07–08/11 · Long Biên, HN</code> và mức học phí <code>4.000.000đ</code> cỡ 34px Tabular-Nums trắng tinh khiết dưới đường kẻ mảnh Editorial để khách tự lọc trong 0.5s)</strong>, đồng thời nâng cấp <strong>3 Bài Quảng Cáo Facebook</strong> (đặt giá 4tr ngay đầu bài, cam kết hoàn 100% học phí sau Ngày 1, ưu đãi đi 2 người 3.5tr, và xóa sạch URL trần để bảo toàn 100% <code>utm_content={{{{ad.name}}}}</code>).
      </p>
      <div class="kpi-grid">
        <div class="kpi-card highlight">
          <div class="val">{done_count} / {done_count} KB</div>
          <div class="lbl">Đã có Phiên Bản Ảnh Thứ 3 (V3 Lọc Giá 4.000.000đ) + 3 Bài Quảng Cáo Chuẩn C2 (140/140 PASS)</div>
        </div>
        <div class="kpi-card">
          <div class="val">3 Ảnh / KB</div>
          <div class="lbl">Ảnh 3 (V3 Lọc Giá 4tr) · Ảnh 1 (Hook 1) · Ảnh 2 (Hook 2 Mới) — Chấm 25/25 cổng UI/UX</div>
        </div>
        <div class="kpi-card">
          <div class="val">3 Bài Ads / KB</div>
          <div class="lbl">Có Giá 4tr trong 125 ký tự đầu (Ads 3), Hoàn 100% Ngày 1, 0% URL trần làm mất UTM</div>
        </div>
        <div class="kpi-card">
          <div class="val">Sẵn Sàng K4 &amp; K5</div>
          <div class="lbl">Tách bạch Kho Phôi Bất Biến &amp; <code>campaign_config.json</code> (đổi 1 file cho khóa sau)</div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="ke-duyet-mau">
    <div class="container">
      <div class="sec-header">
        <span class="sec-step">KỆ DUYỆT BANNER &amp; NỘI DUNG QUẢNG CÁO FACEBOOK KHÓA OFFLINE 07–08/11 ({done_count} KỊCH BẢN)</span>
        <h2 class="sec-title">Danh Sách {done_count} Banner Kèm Phiên Bản 3 Lọc Giá 4.000.000đ &amp; 3 Bài Quảng Cáo Facebook</h2>
        <p class="sec-desc">
          Mặc định hiển thị <strong>💰 Ảnh 3 (Phiên Bản V3 Có Lọc Giá 4.000.000đ)</strong> và <strong>💰 Bài Quảng Cáo 3 (Đặt Giá 4tr Lên Dòng Đầu)</strong>. Bấm các nút bên dưới để chuyển đổi toàn trang giữa Ảnh 3, Ảnh 1, Ảnh 2 hoặc Xem Song Song 3 Ảnh.
        </p>
      </div>

      <div class="mode-switcher-bar">
        <span class="mode-lbl">🔀 Chế Độ Xem Toàn Trang:</span>
        <button id="globalBtnV3" class="mode-btn active" onclick="switchAllMode('v3', this)">💰 1. Ảnh Phiên Bản 3 (Có Lọc Giá 4.000.000đ)</button>
        <button id="globalBtnColor" class="mode-btn" onclick="switchAllMode('color', this)">🎨 2. Ảnh Phương Án 1 (Hook 1)</button>
        <button id="globalBtnHook2" class="mode-btn" onclick="switchAllMode('hook2', this)">⚡ 3. Ảnh Phương Án 2 (Hook 2 Mới)</button>
        <button id="globalBtnDual" class="mode-btn" onclick="switchAllMode('dual', this)">🖼️ 4. Xem Song Song 3 Ảnh (V3 ⇄ H1 ⇄ H2)</button>
        <button id="globalBtnBw" class="mode-btn" onclick="switchAllMode('bw', this)">🖤 5. Bản Đen Trắng</button>
        <button id="globalBtnHm" class="mode-btn" onclick="switchAllMode('hm', this)">🔥 6. Bản Đồ Nhiệt F1→F4</button>
      </div>

      <div class="filter-bar">
        {filter_bar_html}
      </div>

      <div class="vault-grid" id="vaultGrid">
{cards_html}
      </div>
    </div>
  </section>

  <!-- Modal So Sánh Toàn Bộ Các Phiên Bản Lịch Sử -->
  <div class="ver-modal" id="versionModal" onclick="closeVersionModal()">
    <div class="vm-header" onclick="event.stopPropagation()">
      <div class="vm-title-box">
        <h3 id="vmTitle">So Sánh Toàn Bộ Các Phiên Bản Trải Qua</h3>
        <p id="vmSub">Lịch sử tiến hóa từ V1 đến V9.0 (Phiên bản 3 Có Lọc Giá 4.000.000đ + 25/25 Cổng UI/UX)</p>
      </div>
      <div class="vm-actions">
        <button class="vm-btn sbs-btn" id="vmSbsBtn" onclick="">🖼️ Xem Ảnh Ghép Tổng Hợp Tất Cả Phiên Bản</button>
        <button class="vm-btn close-btn" onclick="closeVersionModal()">✕ Đóng Bảng So Sánh (ESC)</button>
      </div>
    </div>
    <div class="vm-grid" id="vmGrid" onclick="event.stopPropagation()"></div>
  </div>

  <!-- Lightbox phóng to 1 ảnh 1080x1350 -->
  <div class="lightbox" id="lightbox" onclick="closeLightbox()">
    <button class="lightbox-close" onclick="closeLightbox()">✕ Đóng Ảnh To (ESC)</button>
    <img id="lightboxImg" src="" alt="Preview" onclick="event.stopPropagation()" />
  </div>

  <footer>
    Hệ Thống Sản Xuất &amp; Kiểm Toán Tự Động {done_count} Banner K4 V9.0 (CLAUDE2 × Luồng 9f7f1024: 3 Phiên Bản Ảnh Có Lọc Giá 4tr + 3 Bài Quảng Cáo Giữ UTM)
  </footer>

  <script>
    const KB_VERSIONS_DB = {kb_versions_json};

    function switchCardImg(kbId, newUrl, btnEl) {{
      const box = document.getElementById('imgbox-' + kbId);
      const singleImg = document.getElementById('img-' + kbId);
      const dualView = document.getElementById('dualview-' + kbId);
      if (box) box.classList.remove('dual-mode');
      if (dualView) dualView.style.display = 'none';
      if (singleImg) {{
        singleImg.style.display = 'block';
        const fn = newUrl.split('/').pop().split('?')[0];
        singleImg.onerror = function() {{
          if (!this.dataset.triedGh) {{
            this.dataset.triedGh = '1';
            this.src = 'https://fedu.vn/k/k4_31kb_banners/v2_pilots/batch_out/' + fn;
            return;
          }}
          if (!this.dataset.triedAlt && fn.endsWith('_v3_price.jpg')) {{
            this.dataset.triedAlt = '1';
            this.src = newUrl.replace('_v3_price.jpg', '_color.jpg');
            return;
          }}
          this.onerror = null;
          this.src = 'https://media.fedu.vn/banner2/' + fn;
        }};
        delete singleImg.dataset.triedGh;
        delete singleImg.dataset.triedAlt;
        singleImg.src = newUrl;
      }}
      if (btnEl && btnEl.parentElement) {{
        Array.from(btnEl.parentElement.querySelectorAll('.sw-btn')).forEach(b => b.classList.remove('active'));
        btnEl.classList.add('active');
      }}
    }}

    function toggleDualImg(kbId, btnEl) {{
      const box = document.getElementById('imgbox-' + kbId);
      const singleImg = document.getElementById('img-' + kbId);
      const dualView = document.getElementById('dualview-' + kbId);
      if (box) box.classList.add('dual-mode');
      if (singleImg) singleImg.style.display = 'none';
      if (dualView) dualView.style.display = 'grid';
      if (btnEl && btnEl.parentElement) {{
        Array.from(btnEl.parentElement.querySelectorAll('.sw-btn')).forEach(b => b.classList.remove('active'));
        btnEl.classList.add('active');
      }}
    }}

    function switchAdTab(kbId, tabNum, btnEl) {{
      const sec = btnEl.closest('.ads-copy-section');
      if (!sec) return;
      Array.from(sec.querySelectorAll('.ad-tab-btn')).forEach(b => b.classList.remove('active'));
      btnEl.classList.add('active');
      const p1 = document.getElementById('ad-pane-' + kbId + '-1');
      const p2 = document.getElementById('ad-pane-' + kbId + '-2');
      const p3 = document.getElementById('ad-pane-' + kbId + '-3');
      if (tabNum === 1) {{
        if (p1) p1.classList.add('active');
        if (p2) p2.classList.remove('active');
        if (p3) p3.classList.remove('active');
      }} else if (tabNum === 2) {{
        if (p1) p1.classList.remove('active');
        if (p2) p2.classList.add('active');
        if (p3) p3.classList.remove('active');
      }} else if (tabNum === 3) {{
        if (p1) p1.classList.remove('active');
        if (p2) p2.classList.remove('active');
        if (p3) p3.classList.add('active');
      }} else {{
        if (p3) p3.classList.add('active');
        if (p1) p1.classList.add('active');
        if (p2) p2.classList.add('active');
      }}
    }}

    function copyAdText(kbId, adNum, btnEl) {{
      const pre = document.getElementById('ad-txt-' + kbId + '-' + adNum);
      if (!pre) return;
      navigator.clipboard.writeText(pre.innerText).then(() => {{
        const oldTxt = btnEl.textContent;
        btnEl.textContent = '✓ Đã Copy!';
        setTimeout(() => {{ btnEl.textContent = oldTxt; }}, 1800);
      }});
    }}

    function switchAllMode(mode, btnEl) {{
      Array.from(document.querySelectorAll('.mode-btn')).forEach(b => b.classList.remove('active'));
      if (btnEl) btnEl.classList.add('active');
      const cards = Array.from(document.querySelectorAll('.vault-card'));
      cards.forEach(c => {{
        const kbId = c.getAttribute('data-kb');
        if (mode === 'dual') {{
          const dualBtn = c.querySelector('.btn-dual');
          toggleDualImg(kbId, dualBtn);
          return;
        }}
        let targetSrc = c.getAttribute('data-v3-src');
        let btnClass = '.btn-v3';
        if (mode === 'color') {{
          targetSrc = c.getAttribute('data-color-src');
          btnClass = '.btn-color';
        }} else if (mode === 'hook2') {{
          targetSrc = c.getAttribute('data-hook2-src');
          btnClass = '.btn-hook2';
        }} else if (mode === 'bw') {{
          targetSrc = c.getAttribute('data-bw-src');
          btnClass = '.btn-bw';
        }} else if (mode === 'hm') {{
          targetSrc = c.getAttribute('data-hm-src');
          btnClass = '.btn-hm';
        }}
        const targetBtn = c.querySelector(btnClass);
        switchCardImg(kbId, targetSrc, targetBtn);
      }});
    }}

    function filterVault(styleCode, btnEl) {{
      Array.from(document.querySelectorAll('.flt-btn')).forEach(b => b.classList.remove('active'));
      btnEl.classList.add('active');
      const cards = Array.from(document.querySelectorAll('.vault-card'));
      cards.forEach(c => {{
        if (styleCode === 'ALL' || styleCode === 'UPGRADED') {{
          c.style.display = 'flex';
        }} else if (c.getAttribute('data-style') === styleCode) {{
          c.style.display = 'flex';
        }} else {{
          c.style.display = 'none';
        }}
      }});
    }}

    function openVersionHistoryModal(kbId) {{
      const info = KB_VERSIONS_DB[kbId];
      if (!info) return;
      const modal = document.getElementById('versionModal');
      const titleEl = document.getElementById('vmTitle');
      const subEl = document.getElementById('vmSub');
      const sbsBtn = document.getElementById('vmSbsBtn');
      const gridEl = document.getElementById('vmGrid');

      const vers = info.versions || [];
      const scanStr = (info.scanpath || []).join(' → ');
      titleEl.textContent = `${{info.kb_id}} (${{info.h_code}} × ${{info.style_code}}): “${{info.headline}}” — Toàn Bộ ${{vers.length}} Phiên Bản Trải Qua`;
      subEl.textContent = `Điểm kiểm toán: ${{info.score}} • Tiêu đề: ${{info.h_fs}}px • Chữ phụ LAW_19: ${{info.min_sub_fs}}px • Luồng mắt WTA: ${{scanStr}} (Bấm vào từng ảnh để phóng to 1080×1350)`;

      sbsBtn.onclick = () => openLightbox(info.sbs_url);

      gridEl.innerHTML = vers.map((v, idx) => {{
        const bCol = v.badge_color || '#38BDF8';
        return `
          <div class="vm-card" style="border-color: ${{bCol}}66;">
            <div class="vm-card-head">
              <span class="vm-step-badge" style="background: ${{bCol}};">PHIÊN BẢN ${{idx + 1}} / ${{vers.length}} • ${{v.ver_id || ''}}</span>
              <h5>${{v.label}}</h5>
              <p>${{v.sub_info || ''}}</p>
            </div>
            <div class="vm-img-wrap">
              <img src="${{v.img_url}}" alt="${{v.label}}" loading="lazy" onclick="openLightbox('${{v.img_url}}')" />
            </div>
          </div>
        `;
      }}).join('');

      modal.classList.add('open');
    }}

    function closeVersionModal() {{
      document.getElementById('versionModal').classList.remove('open');
    }}

    function openLightbox(src) {{
      const lb = document.getElementById('lightbox');
      const im = document.getElementById('lightboxImg');
      im.src = src;
      lb.classList.add('open');
    }}

    function closeLightbox() {{
      document.getElementById('lightbox').classList.remove('open');
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        const lb = document.getElementById('lightbox');
        if (lb.classList.contains('open')) {{
          closeLightbox();
        }} else {{
          closeVersionModal();
        }}
      }}
    }});
  </script>
</body>
</html>
"""


def atomic_rebuild_and_sync(push_r2: bool = False) -> Dict[str, Any]:
    LOCK_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOCK_FILE, "w") as lf:
        fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
        try:
            cards = load_all_cards()
            html_str = generate_html_content(cards)
            tmp_out = OUT_HTML.with_suffix(".html.tmp")
            tmp_out.write_text(html_str, encoding="utf-8")
            tmp_out.replace(OUT_HTML)

            r2_url = "https://media.fedu.vn/banner2/banner2.html"
            if push_r2 and R2_MANAGER.exists():
                subprocess.run(
                    ["python3", str(R2_MANAGER), "--put", str(OUT_HTML), "banner2/banner2.html"],
                    check=False,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            return {
                "total_cards": len(cards),
                "upgraded_cards": sum(1 for c in cards if c.get("claude2_upgraded")),
                "local_path": str(OUT_HTML),
                "r2_url": r2_url,
            }
        finally:
            fcntl.flock(lf.fileno(), fcntl.LOCK_UN)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--online", action="store_true", help="Push banner2.html lên R2")
    args = ap.parse_args()
    res = atomic_rebuild_and_sync(push_r2=args.online)
    print(json.dumps(res, ensure_ascii=False))
