#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ATOMIC LOCK-FREE HUB BUILDER FOR BANNER2.HTML V8.0 (CLAUDE2 DUAL-HOOK + DUAL-IMAGE + DUAL-FB-AD-COPY + LAW_19 + SCANPATH)
=========================================================================================================================
- Đọc toàn bộ các file JSON trong `/Users/vietmac/Documents/CODE/k/k4_31kb_banners/banner2_cards/KB_*.json` (hỗ trợ từ KB_01 đến KB_140).
- Với mỗi KB:
  1. Hiển thị 2 Phương Án Ảnh Banner 1080x1350:
     - 🎨 Ảnh Phương Án 1 (Hook A — Đã gọt sắc bén cho Ads Offline 07–08/11)
     - ⚡ Ảnh Phương Án 2 (Hook B — Phương án Text Hook đối chứng mới do CLAUDE2 đề xuất)
     - 🖼️ Chế độ Xem Song Song 2 Ảnh (Hook A ⇄ Hook B) ngay trên thẻ
     - 🖤 Bản Đen Trắng & 🔥 Bản Đồ Nhiệt Luồng Thị Giác F1→F4
  2. Hiển thị Khối Đánh Giá Của CLAUDE2 (Opus 5.5):
     - Đánh giá Tiêu đề cũ đã đủ Hook chưa
     - Đánh giá Logic chuyển đổi về lớp Offline 07–08/11
     - Đánh giá Phôi ảnh & Bối cảnh
  3. Hiển thị 2 Bài Quảng Cáo Facebook Thực Chiến (Ad Copy 1 & Ad Copy 2) tương ứng với 2 Ảnh ngay bên dưới,
     văn phong Claude × Nguyễn Việt, kèm nút Copy 1 chạm.
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
    min_sub = c.get("min_sub_fs_px", 27.0)
    score = c.get("score", "25/25")
    scan = " → ".join(c.get("scanpath_order", ["FACE", "HEADLINE", "SUBBOX"])[:4])

    existing = c.get("versions_history", [])
    if existing:
        out = []
        for item in existing:
            u = item.get("img_url", "")
            if u.startswith("./k4_31kb_banners/v2_pilots/batch_out/") or "media.fedu.vn/banner2/" in u:
                fn = u.split("/")[-1].split("?")[0]
                u = f"https://fedu.vn/k/k4_31kb_banners/v2_pilots/batch_out/{fn}"
            u_ver = f"{u}?v={ver}" if ("?" not in u and u) else u
            cp = dict(item)
            cp["img_url"] = u_ver
            out.append(cp)
        return out

    gh_base = "https://fedu.vn/k/k4_31kb_banners/v2_pilots/batch_out"
    color_url = f"{gh_base}/{kb_lower}_color.jpg"
    bw_url = f"{gh_base}/{kb_lower}_bw.jpg"
    alt_url = f"{gh_base}/{kb_lower}_hook2.jpg"
    hm_url = f"{gh_base}/{kb_lower}_heatmap.jpg"
    return [
        {
            "step": 1,
            "ver_id": "V7_COLOR_HOOK1",
            "label": f"Ảnh Phương Án 1 ({style_code} · Hook A)",
            "sub_info": f"Chữ phụ {min_sub}px (#E2E8F0/#FFF) · {score} PASS",
            "img_url": f"{color_url}?v={ver}",
            "badge_color": "#10B981",
        },
        {
            "step": 2,
            "ver_id": "V7_ALT_HOOK2",
            "label": f"Ảnh Phương Án 2 ({alt_code} · Hook B Mới)",
            "sub_info": "Phương án Text Hook đối chứng A/B Testing",
            "img_url": f"{alt_url}?v={ver}",
            "badge_color": "#F59E0B",
        },
        {
            "step": 3,
            "ver_id": "V7_BW_LAW19",
            "label": f"Bản Đen Trắng ({style_code} · LAW_19)",
            "sub_info": f"Fine-Art B&W · Chữ phụ {min_sub}px",
            "img_url": f"{bw_url}?v={ver}",
            "badge_color": "#38BDF8",
        },
        {
            "step": 4,
            "ver_id": "V7_HEATMAP_SCANPATH",
            "label": "Bản Đồ Nhiệt Luồng Thị Giác (F1→F4)",
            "sub_info": f"Scanpath: {scan}",
            "img_url": f"{hm_url}?v={ver}",
            "badge_color": "#F43F5E",
        },
    ]


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
    alt_name = c.get("alt_style_name", "")
    font_name = c.get("font_name", "")
    outfit_id = c.get("outfit_id", "C02_I03")
    banner_style_name = c.get("banner_style_name", "Phong cách Studio")
    headline_plain = c.get("headline_plain", "")
    subline_summary = c.get("subline_summary", "")

    ver = c.get("ver", "v8")
    # Ưu tiên đường dẫn tuyệt đối https://fedu.vn/k/... để hiển thị 100% trên cả media.fedu.vn và fedu.vn/k/
    local_rel_dir = "./k4_31kb_banners/v2_pilots/batch_out"
    local_abs_dir = BASE_DIR / "v2_pilots" / "batch_out"
    gh_base = "https://fedu.vn/k/k4_31kb_banners/v2_pilots/batch_out"

    hook2_file = f"{kb_lower}_hook2.jpg" if (local_abs_dir / f"{kb_lower}_hook2.jpg").exists() else f"{kb_lower}_alt.jpg"
    r2_color = f"{gh_base}/{kb_lower}_color.jpg?v={ver}"
    r2_bw = f"{gh_base}/{kb_lower}_bw.jpg?v={ver}"
    r2_alt = f"{gh_base}/{hook2_file}?v={ver}"
    r2_hm = f"{gh_base}/{kb_lower}_heatmap.jpg?v={ver}"

    local_color = f"{local_rel_dir}/{kb_lower}_color.jpg?v={ver}"
    local_bw = f"{local_rel_dir}/{kb_lower}_bw.jpg?v={ver}"
    local_alt = f"{local_rel_dir}/{hook2_file}?v={ver}"
    local_hm = f"{local_rel_dir}/{kb_lower}_heatmap.jpg?v={ver}"

    color_src = r2_color
    bw_src = r2_bw
    alt_src = r2_alt
    hm_src = r2_hm

    score = c.get("audit_score", "25/25 PASS")
    min_sub_fs = c.get("min_sub_fs_px", 27.0)
    h_fs = c.get("headline_fs_px", 78.0)
    scan_order = c.get("scanpath_order", ["FACE", "HEADLINE", "SUBBOX", "HEADLINE"])
    scan_short = " → ".join(s[:4] for s in scan_order[:3])
    versions = build_default_versions_if_missing(c, ver)
    n_vers = len(versions)
    filter_tag = style_code.split()[0]

    has_claude2 = bool(c.get("claude2_upgraded"))
    card_extra_cls = "claude2-upgraded" if has_claude2 else ""
    status_badge = (
        f"⚡ {kb_id} • ĐÃ NÂNG CẤP CLAUDE2 (2 ẢNH × 2 HOOK × 2 ADS)"
        if has_claude2
        else f"✓ {kb_id} • {h_code} × {style_code} (LAW_19: {min_sub_fs}px)"
    )

    # Khối CLAUDE2 Audit + 2 Hook + 2 Bài Quảng Cáo
    claude2_html = ""
    if has_claude2:
        audit = c.get("claude2_audit", {})
        h1 = c.get("hook_1", {})
        h2 = c.get("hook_2", {})
        ad1 = c.get("ad_copy_1", {})
        ad2 = c.get("ad_copy_2", {})

        h1_plain = h1.get("headline_plain") or " / ".join(
            ln.replace('<span class="hl">', "").replace("</span>", "") for ln in h1.get("headline_lines", [])
        )
        h2_plain = h2.get("headline_plain") or " / ".join(
            ln.replace('<span class="hl">', "").replace("</span>", "") for ln in h2.get("headline_lines", [])
        )

        ad1_headline = _esc(ad1.get("fb_headline", "07 - 08 tháng 11, học trực tiếp 2 ngày tại Hà Nội"))
        ad1_body = _esc(ad1.get("primary_text", ""))
        ad2_headline = _esc(ad2.get("fb_headline", "07 - 08 tháng 11, học trực tiếp 2 ngày tại Hà Nội"))
        ad2_body = _esc(ad2.get("primary_text", ""))

        claude2_html = f"""
            <div class="c2-audit-box">
              <div class="c2-audit-title">🧠 ĐÁNH GIÁ CỦA CỐ VẤN CLAUDE2 (OPUS 5.5) • KHÓA OFFLINE 07–08/11</div>
              <div class="c2-audit-item"><strong>🎯 Đánh giá Hook cũ:</strong> {_esc(audit.get("old_hook_verdict", ""))}</div>
              <div class="c2-audit-item"><strong>🔗 Đánh giá Logic:</strong> {_esc(audit.get("logic_verdict", ""))}</div>
              <div class="c2-audit-item"><strong>📸 Đánh giá Ảnh Ads:</strong> {_esc(audit.get("image_verdict", ""))}</div>
            </div>

            <div class="hooks-compare-grid">
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
                <button class="ad-tab-btn active" onclick="switchAdTab('{kb_id}', 1, this)">📣 Quảng Cáo 1 (Ứng Ảnh 1)</button>
                <button class="ad-tab-btn" onclick="switchAdTab('{kb_id}', 2, this)">📣 Quảng Cáo 2 (Ứng Ảnh 2)</button>
                <button class="ad-tab-btn" onclick="switchAdTab('{kb_id}', 0, this)">📖 Xem Cả 2 Bài</button>
              </div>

              <div class="ad-pane active" id="ad-pane-{kb_id}-1">
                <div class="ad-pane-head">
                  <span>📣 <strong>BÀI QUẢNG CÁO FACEBOOK #1</strong> (Đi kèm Ảnh 1 · Hook 1)</span>
                  <button class="copy-ad-btn" onclick="copyAdText('{kb_id}', 1, this)">📋 Copy Quảng Cáo 1</button>
                </div>
                <div class="ad-fb-hl">📌 Tiêu đề dưới ảnh: <strong>{ad1_headline}</strong></div>
                <pre class="ad-text-content" id="ad-txt-{kb_id}-1">{ad1_body}</pre>
              </div>

              <div class="ad-pane" id="ad-pane-{kb_id}-2">
                <div class="ad-pane-head">
                  <span>📣 <strong>BÀI QUẢNG CÁO FACEBOOK #2</strong> (Đi kèm Ảnh 2 · Hook 2 Mới)</span>
                  <button class="copy-ad-btn" onclick="copyAdText('{kb_id}', 2, this)">📋 Copy Quảng Cáo 2</button>
                </div>
                <div class="ad-fb-hl">📌 Tiêu đề dưới ảnh: <strong>{ad2_headline}</strong></div>
                <pre class="ad-text-content" id="ad-txt-{kb_id}-2">{ad2_body}</pre>
              </div>
            </div>
        """

    return f"""
        <article class="vault-card approved {card_extra_cls}" data-style="{filter_tag}" data-h="{h_code}" data-kb="{kb_id}" data-upgraded="{'1' if has_claude2 else '0'}" data-color-src="{color_src}" data-hook2-src="{alt_src}" data-bw-src="{bw_src}" data-hm-src="{hm_src}" id="card-{kb_id}">
          <div class="vc-head">
            <span class="vault-status ok">{status_badge}</span>
            <span class="vc-score">{score}</span>
          </div>
          <div class="vc-img-box" id="imgbox-{kb_id}">
            <img id="img-{kb_id}" src="{color_src}" onerror="this.onerror=null;this.src='{local_color}';" alt="{kb_id} - {_esc(title)}" loading="lazy" decoding="async" onclick="openLightbox(this.src)" />
            <div class="dual-img-view" id="dualview-{kb_id}" style="display:none;">
              <div class="dual-col">
                <span class="dual-tag tag-h1">🎨 ẢNH 1 (HOOK 1)</span>
                <img src="{color_src}" onerror="this.onerror=null;this.src='{local_color}';" alt="Hook 1" onclick="openLightbox(this.src)" />
              </div>
              <div class="dual-col">
                <span class="dual-tag tag-h2">⚡ ẢNH 2 (HOOK 2 MỚI)</span>
                <img src="{alt_src}" onerror="this.onerror=null;this.src='{local_alt}';" alt="Hook 2" onclick="openLightbox(this.src)" />
              </div>
            </div>
          </div>
          <div class="vc-switch-bar">
            <button class="sw-btn btn-color active" onclick="switchCardImg('{kb_id}', '{color_src}', this)">🎨 Ảnh 1 (Hook 1)</button>
            <button class="sw-btn btn-hook2" onclick="switchCardImg('{kb_id}', '{alt_src}', this)">⚡ Ảnh 2 (Hook 2 Mới)</button>
            <button class="sw-btn btn-dual" onclick="toggleDualImg('{kb_id}', this)">🖼️ Song Song 2 Ảnh</button>
            <button class="sw-btn btn-bw" onclick="switchCardImg('{kb_id}', '{bw_src}', this)">🖤 Đen Trắng</button>
            <button class="sw-btn btn-hm" onclick="switchCardImg('{kb_id}', '{hm_src}', this)">🔥 Bản Đồ Nhiệt</button>
            <button class="sw-btn btn-compare" onclick="openVersionHistoryModal('{kb_id}')">🔍 Lịch Sử ({n_vers} Bản)</button>
          </div>
          <div class="vc-body">
            <h4>{kb_id}: “{_esc(headline_plain)}”</h4>
            <p class="vc-sub">{_esc(subline_summary)}</p>
            {claude2_html}
            <div class="vc-meta">
              <span>🔥 <strong>Luồng mắt WTA:</strong> <code>{scan_short}</code> • Tiêu đề <strong>{h_fs}px</strong> / Chữ phụ <strong>{min_sub_fs}px</strong></span>
              <span>👔 <strong>{_esc(banner_style_name)}</strong> (Phôi <code>{outfit_id}</code> • 85mm f/1.4 Bokeh)</span>
              <span>🔤 <strong>{_esc(font_name)}</strong> × 📐 <strong>{_esc(style_name)}</strong> ({n_vers} phiên bản lịch sử)</span>
            </div>
          </div>
        </article>"""


def generate_html_content(cards: List[Dict[str, Any]]) -> str:
    done_count = len(cards)
    upgraded_count = sum(1 for c in cards if c.get("claude2_upgraded"))
    cards_html = "\n".join(build_card_html(c) for c in cards)

    kb_versions_map = {}
    for c in cards:
        ver = c.get("ver", "v8")
        kb_id = c["kb_id"]
        kb_lower = kb_id.lower()
        sbs_src = f"https://fedu.vn/k/k4_31kb_banners/v2_pilots/batch_out/{kb_lower}_sbs.jpg?v={ver}"
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
        f'<button class="flt-btn" style="border-color:#F59E0B;color:#FACC15;" onclick="filterVault(\'UPGRADED\', this)">⚡ Đã Nâng Cấp CLAUDE2 ({upgraded_count}/{done_count})</button>',
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
  <title>BANNER 2.0 V8.0 • {done_count} Banner K4 × CLAUDE2 Audit (2 Ảnh × 2 Hook × 2 Bài Quảng Cáo Facebook Offline 07–08/11)</title>
  <meta name="description" content="Hệ thống {done_count} Kịch bản Banner Quảng Cáo Facebook Khóa Offline 07–08/11: Đánh giá CLAUDE2, 2 Phương án Ảnh & Text Hook chuẩn LAW_19 (27-28px), và 2 Bài Quảng Cáo Facebook văn phong Claude × Nguyễn Việt." />
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
    .brand-badge {{ background: var(--gold); color: #070B14; font-family: var(--font-mono); font-size: 12px; font-weight: 800; padding: 4px 10px; border-radius: 6px; }}
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
      background: radial-gradient(circle at 80% 10%, rgba(245, 158, 11, 0.14), transparent 45%), linear-gradient(180deg, #0E1629 0%, #070B14 100%);
      border-bottom: 1px solid var(--border); padding: 38px 24px 32px;
    }}
    .container {{ max-width: 1640px; margin: 0 auto; }}
    .eyebrow-tag {{
      display: inline-flex; align-items: center; gap: 8px; background: rgba(34, 197, 94, 0.14);
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
      background: rgba(21, 31, 54, 0.9); border: 1.5px solid var(--border-gold);
      padding: 14px 20px; border-radius: 14px; margin-bottom: 22px;
    }}
    .mode-lbl {{ font-family: var(--font-mono); font-size: 13px; font-weight: 800; color: var(--gold-bright); text-transform: uppercase; }}
    .mode-btn {{
      background: var(--surface); color: var(--text); border: 1.5px solid var(--border);
      padding: 9px 16px; border-radius: 999px; font-size: 13px; font-weight: 800; cursor: pointer; transition: all 0.2s;
    }}
    .mode-btn.active, .mode-btn:hover {{
      background: var(--gold); color: #070B14; border-color: var(--gold); box-shadow: 0 4px 16px rgba(245, 158, 11, 0.35);
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
      grid-template-columns: repeat(auto-fill, minmax(480px, 1fr));
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
      border-color: var(--border-gold);
      box-shadow: 0 12px 34px rgba(245, 158, 11, 0.16);
    }}
    .vc-head {{
      padding: 12px 16px; background: var(--surface-2); border-bottom: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between; gap: 8px;
    }}
    .vault-status.ok {{
      background: rgba(34, 197, 94, 0.18); color: #4ADE80; font-family: var(--font-mono);
      font-size: 11.2px; font-weight: 800; padding: 4px 10px; border-radius: 999px;
    }}
    .vault-card.claude2-upgraded .vault-status.ok {{
      background: rgba(245, 158, 11, 0.22); color: var(--gold-bright);
    }}
    .vc-score {{ font-family: var(--font-mono); font-size: 11.5px; color: var(--gold-bright); font-weight: 700; flex-shrink: 0; }}
    .vc-img-box {{ background: #050811; aspect-ratio: 4 / 5; overflow: hidden; position: relative; }}
    .vc-img-box.dual-mode {{ aspect-ratio: auto; padding: 10px; }}
    .vc-img-box > img {{ width: 100%; height: 100%; object-fit: cover; display: block; cursor: zoom-in; }}
    .dual-img-view {{
      display: grid; grid-template-columns: 1fr 1fr; gap: 10px; width: 100%;
    }}
    .dual-col {{
      display: flex; flex-direction: column; background: #0A101E; border: 1px solid var(--border); border-radius: 10px; overflow: hidden;
    }}
    .dual-col img {{ width: 100%; aspect-ratio: 4 / 5; object-fit: cover; cursor: zoom-in; display: block; }}
    .dual-tag {{
      font-family: var(--font-mono); font-size: 11px; font-weight: 800; text-align: center; padding: 5px 6px;
    }}
    .dual-tag.tag-h1 {{ background: rgba(34, 197, 94, 0.2); color: #4ADE80; }}
    .dual-tag.tag-h2 {{ background: rgba(245, 158, 11, 0.22); color: var(--gold-bright); }}

    .vc-switch-bar {{
      display: flex; flex-wrap: wrap; gap: 5px; padding: 10px 10px;
      background: #0A101E; border-bottom: 1px solid var(--border);
    }}
    .sw-btn {{
      flex: 1 1 calc(33.3% - 6px); min-width: 92px; background: var(--surface-2); color: var(--text-soft);
      border: 1px solid var(--border); border-radius: 6px; padding: 6px 6px;
      font-size: 11px; font-weight: 700; cursor: pointer; text-align: center; transition: all 0.15s;
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
    .sw-btn.active, .sw-btn:hover {{ background: var(--gold); color: #070B14; border-color: var(--gold); }}

    .vc-body {{ padding: 16px; display: flex; flex-direction: column; gap: 12px; flex: 1; }}
    .vc-body h4 {{ font-size: 16px; font-weight: 800; color: var(--text); line-height: 1.35; }}
    .vc-sub {{ font-size: 12.8px; color: var(--text-soft); }}

    /* CLAUDE2 Audit & Dual Hooks & Dual Ads */
    .c2-audit-box {{
      background: rgba(15, 23, 42, 0.92); border: 1px solid rgba(56, 189, 248, 0.35);
      border-left: 4px solid var(--cyan); border-radius: 10px; padding: 12px 14px;
      display: flex; flex-direction: column; gap: 6px; font-size: 12.8px; color: #E2E8F0;
    }}
    .c2-audit-title {{
      font-family: var(--font-mono); font-size: 11.5px; font-weight: 800; color: var(--cyan);
      letter-spacing: 0.04em; margin-bottom: 2px;
    }}
    .c2-audit-item {{ line-height: 1.48; }}
    .c2-audit-item strong {{ color: var(--gold-bright); }}

    .hooks-compare-grid {{
      display: grid; grid-template-columns: 1fr 1fr; gap: 10px;
    }}
    @media (max-width: 560px) {{
      .hooks-compare-grid {{ grid-template-columns: 1fr; }}
    }}
    .hk-box {{
      background: #0A101E; border: 1px solid var(--border); border-radius: 10px; padding: 10px 12px;
      cursor: pointer; transition: all 0.18s;
    }}
    .hk-box:hover {{ border-color: var(--gold); transform: translateY(-1px); }}
    .hk-box-1 {{ border-top: 3px solid #22C55E; }}
    .hk-box-2 {{ border-top: 3px solid #F59E0B; }}
    .hk-badge {{
      font-family: var(--font-mono); font-size: 10.5px; font-weight: 800; margin-bottom: 5px;
    }}
    .hk-b1 {{ color: #4ADE80; }}
    .hk-b2 {{ color: var(--gold-bright); }}
    .hk-head {{ font-size: 13.5px; font-weight: 800; color: #FFFFFF; line-height: 1.35; margin-bottom: 6px; }}
    .hk-sub {{ font-size: 12px; color: #CBD5E1; line-height: 1.42; }}
    .hk-sub strong {{ color: #FFFFFF; }}

    .ads-copy-section {{
      background: #090E1A; border: 1px solid var(--border); border-radius: 12px; overflow: hidden;
    }}
    .ads-tabs {{
      display: flex; background: #111A2E; border-bottom: 1px solid var(--border);
    }}
    .ad-tab-btn {{
      flex: 1; background: transparent; color: var(--text-soft); border: none;
      padding: 9px 10px; font-size: 12px; font-weight: 700; cursor: pointer;
      border-bottom: 2px solid transparent; transition: all 0.15s;
    }}
    .ad-tab-btn.active, .ad-tab-btn:hover {{
      color: var(--gold-bright); border-bottom-color: var(--gold); background: rgba(245, 158, 11, 0.08);
    }}
    .ad-pane {{ display: none; padding: 12px 14px; border-bottom: 1px solid var(--border); }}
    .ad-pane:last-child {{ border-bottom: none; }}
    .ad-pane.active {{ display: block; }}
    .ad-pane-head {{
      display: flex; align-items: center; justify-content: space-between; gap: 8px;
      margin-bottom: 8px; font-size: 12.2px; color: var(--gold-bright);
    }}
    .copy-ad-btn {{
      background: rgba(34, 197, 94, 0.18); color: #4ADE80; border: 1px solid rgba(34, 197, 94, 0.45);
      border-radius: 6px; padding: 4px 10px; font-size: 11.5px; font-weight: 700; cursor: pointer;
    }}
    .copy-ad-btn:hover {{ background: #22C55E; color: #070B14; }}
    .ad-fb-hl {{
      background: rgba(245, 158, 11, 0.12); border: 1px dashed rgba(245, 158, 11, 0.4);
      border-radius: 6px; padding: 6px 10px; font-size: 12.2px; color: #FDE047; margin-bottom: 8px;
    }}
    .ad-text-content {{
      white-space: pre-wrap; word-wrap: break-word; font-family: var(--font-sans);
      font-size: 13.2px; line-height: 1.58; color: #F1F5F9; max-height: 340px; overflow-y: auto;
      padding-right: 4px;
    }}

    .vc-meta {{
      margin-top: auto; padding-top: 10px; border-top: 1px solid var(--border);
      display: flex; flex-direction: column; gap: 4px; font-family: var(--font-mono); font-size: 11.2px; color: var(--muted);
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
      <span class="brand-badge">BANNER 2.0 • V8.0 CLAUDE2 × NGUYỄN VIỆT</span>
      <span class="brand-title">Kệ Duyệt {done_count} Banner K4 (07–08/11) • 2 Phương Án Ảnh &amp; Hook • 2 Bài Quảng Cáo Facebook</span>
    </a>
    <nav class="nav-links">
      <button class="nav-pill green-pill" onclick="switchAllMode('color', document.getElementById('globalBtnColor'))">🎨 Xem Ảnh 1 (Hook 1)</button>
      <button class="nav-pill" onclick="switchAllMode('hook2', document.getElementById('globalBtnHook2'))">⚡ Xem Ảnh 2 (Hook 2 Mới)</button>
      <button class="nav-pill" onclick="switchAllMode('dual', document.getElementById('globalBtnDual'))">🖼️ Xem Song Song 2 Ảnh</button>
      <button class="nav-pill rose-pill" onclick="switchAllMode('hm', document.getElementById('globalBtnHm'))">🔥 Bản Đồ Nhiệt</button>
      <a href="kichban-quangcao-k4.html" class="nav-pill">📜 142 Kịch Bản Gốc (kb3k4)</a>
      <a href="bo-chon-chu-banner.html" class="nav-pill">🎛️ Bộ Chọn Chữ</a>
    </nav>
  </header>

  <section class="hero">
    <div class="container">
      <div class="eyebrow-tag">⚡ NÂNG CẤP V8.0 (CLAUDE2 OPUS 5.5 × NGUYỄN VIỆT) • QUẢNG CÁO FACEBOOK KHÓA OFFLINE HÀ NỘI 07–08/11 • MỖI KB: ĐÁNH GIÁ CLAUDE2 + 2 ẢNH + 2 HOOK + 2 BÀI QUẢNG CÁO</div>
      <h1>Kệ Duyệt Banner &amp; Bài Quảng Cáo Facebook Khóa Offline 07–08/11 ({upgraded_count}/{done_count} KB Đã Nâng Cấp 2 Ảnh × 2 Hook × 2 Bài Ads)</h1>
      <p class="hero-lead">
        Mỗi Kịch bản Banner được <strong>Cố vấn CLAUDE2 (Opus 5.5)</strong> trực tiếp đánh giá độ sắc của Tiêu đề Hook, mạch Logic chuyển đổi về lớp <strong>Offline 2 ngày tại Hà Nội (07–08/11/2026 — offline.fedu.vn)</strong> và mức độ phù hợp của Phôi ảnh; đồng thời xuất <strong>2 Phương Án Ảnh Banner 1080×1350 (Hook 1 &amp; Hook 2 mới chuẩn đọc Mobile LAW_19 27–28px)</strong> kèm <strong>2 Bài Quảng Cáo Facebook hoàn chỉnh ngay bên dưới</strong> theo văn phong <strong>Claude × Nguyễn Việt</strong>.
      </p>
      <div class="kpi-grid">
        <div class="kpi-card highlight">
          <div class="val">{upgraded_count} / {done_count} KB</div>
          <div class="lbl">Đã hoàn tất đánh giá CLAUDE2 + 2 Ảnh Banner + 2 Hook + 2 Bài Quảng Cáo Facebook</div>
        </div>
        <div class="kpi-card">
          <div class="val">2 Ảnh × 2 Hook / KB</div>
          <div class="lbl">Phương án 1 (Hook A) &amp; Phương án 2 (Hook B đối chứng A/B Testing chuẩn LAW_19 27–28px)</div>
        </div>
        <div class="kpi-card">
          <div class="val">2 Bài Ads / KB</div>
          <div class="lbl">Văn phong Claude × Nguyễn Việt sắc bén, bấm 1 chạm Copy dán thẳng vào Facebook Ads Manager</div>
        </div>
        <div class="kpi-card">
          <div class="val">07–08/11 Hà Nội</div>
          <div class="lbl">Ghim chuẩn lịch học Offline 2 ngày tại Hà Nội &amp; trang đích https://offline.fedu.vn/</div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="ke-duyet-mau">
    <div class="container">
      <div class="sec-header">
        <span class="sec-step">KỆ DUYỆT BANNER &amp; NỘI DUNG QUẢNG CÁO FACEBOOK KHÓA OFFLINE 07–08/11 ({done_count} KỊCH BẢN)</span>
        <h2 class="sec-title">Danh Sách {done_count} Banner Kèm Đánh Giá CLAUDE2, 2 Phương Án Ảnh Hook &amp; 2 Bài Quảng Cáo Facebook</h2>
        <p class="sec-desc">
          Bấm nút bên dưới để xem <strong>🎨 Ảnh 1 (Hook 1)</strong>, <strong>⚡ Ảnh 2 (Hook 2 Mới)</strong>, hoặc <strong>🖼️ Xem Song Song 2 Ảnh (Hook 1 ⇄ Hook 2)</strong> trên toàn trang. Ngay bên dưới mỗi ảnh là nhận xét của CLAUDE2 và 2 bài quảng cáo Facebook tương ứng.
        </p>
      </div>

      <div class="mode-switcher-bar">
        <span class="mode-lbl">🔀 Chế Độ Xem Toàn Trang:</span>
        <button id="globalBtnColor" class="mode-btn active" onclick="switchAllMode('color', this)">🎨 1. Ảnh Phương Án 1 (Hook 1)</button>
        <button id="globalBtnHook2" class="mode-btn" onclick="switchAllMode('hook2', this)">⚡ 2. Ảnh Phương Án 2 (Hook 2 Mới)</button>
        <button id="globalBtnDual" class="mode-btn" onclick="switchAllMode('dual', this)">🖼️ 3. Xem Song Song 2 Ảnh (Hook 1 ⇄ Hook 2)</button>
        <button id="globalBtnBw" class="mode-btn" onclick="switchAllMode('bw', this)">🖤 4. Bản Đen Trắng</button>
        <button id="globalBtnHm" class="mode-btn" onclick="switchAllMode('hm', this)">🔥 5. Bản Đồ Nhiệt F1→F4</button>
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
        <p id="vmSub">Lịch sử tiến hóa từ V1 đến V8.0 (CLAUDE2 Dual-Hook + LAW_19 + Scanpath)</p>
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
    Hệ Thống Sản Xuất &amp; Kiểm Toán Tự Động {done_count} Banner K4 V8.0 (CLAUDE2 Dual-Hook + Dual Facebook Ad Copy + LAW_19 Mobile Legibility)
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
          if (!this.dataset.triedAlt && fn.endsWith('_hook2.jpg')) {{
            this.dataset.triedAlt = '1';
            this.src = newUrl.replace('_hook2.jpg', '_alt.jpg');
            return;
          }}
          this.onerror = null;
          if (newUrl.includes('media.fedu.vn')) {{
            this.src = './k4_31kb_banners/v2_pilots/batch_out/' + fn;
          }} else {{
            this.src = 'https://media.fedu.vn/banner2/' + fn;
          }}
        }};
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
      if (tabNum === 1) {{
        if (p1) p1.classList.add('active');
        if (p2) p2.classList.remove('active');
      }} else if (tabNum === 2) {{
        if (p1) p1.classList.remove('active');
        if (p2) p2.classList.add('active');
      }} else {{
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
        let targetSrc = c.getAttribute('data-color-src');
        let btnClass = '.btn-color';
        if (mode === 'hook2') {{
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
        if (styleCode === 'ALL') {{
          c.style.display = 'flex';
        }} else if (styleCode === 'UPGRADED') {{
          c.style.display = (c.getAttribute('data-upgraded') === '1') ? 'flex' : 'none';
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
