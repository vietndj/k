#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tạo trang web tương tác toàn diện gmail_brand.html cho 38 tài khoản Gmail của anh Việt.
Tích hợp sẵn JSON dữ liệu, trình mô phỏng Chrome Tab 1:1, bộ lọc 5 nhóm, tìm kiếm tức thì,
toggle hiển thị mật khẩu/ghi chú, và sao chép 1-click SVG / Data URI.
"""

import json

JSON_PATH = '/Users/vietmac/Documents/CODE/k/gmail_assets.json'
OUT_HTML = '/Users/vietmac/Documents/CODE/k/gmail_brand.html'

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    items = json.load(f)

json_data_str = json.dumps(items, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="vi" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>BỘ NHẬN DIỆN LOGO 38 TÀI KHOẢN GMAIL • NGUYỄN VIỆT</title>
  
  <!-- Dynamic Favicon (Mặc định vietndj Master) -->
  <link id="dynamic-favicon" rel="icon" type="image/svg+xml" href="{items[0]['uri_dark']}">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  
  <style>
    @font-face {{
      font-family: 'FD Anguita Sans';
      src: url('https://font.fedu.vn/fonts/FDAnguitaSans-Black.woff2') format('woff2'),
           url('/Users/vietmac/Library/Fonts/FDAnguitaSans-Black.ttf') format('truetype');
      font-weight: 900;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'FD Aeonik Extended'; text-transform: uppercase;
      src: url('https://font.fedu.vn/fonts/FDAeonikExtended-Bold.woff2?v=20260911b') format('woff2'),
           url('./fonts/FDAeonikExtended-Bold.woff2') format('woff2');
      font-weight: 700;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'FD Aeonik';
      src: url('https://font.fedu.vn/fonts/FDAeonikExtended-SemiBold.woff2?v=20260911b') format('woff2'),
           url('./fonts/FDAeonikExtended-SemiBold.woff2') format('woff2');
      font-weight: 600;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'Tiempos Text';
      src: url('/Users/vietmac/Library/Fonts/FDTiemposText-Regular.otf') format('opentype');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }}

    :root {{
      --cl-bg:          #07090e;
      --cl-tint:        #0c101a;
      --cl-card:        #111622;
      --cl-card-muted:  #161d2d;
      --cl-accent:      #38bdf8;
      --cl-accent-tint: rgba(56, 189, 248, 0.12);
      --cl-line:        rgba(255, 255, 255, 0.08);
      --cl-line-strong: rgba(255, 255, 255, 0.18);
      --cl-text-base:   #f8fafc;
      --cl-text-muted:  #94a3b8;
      --cl-text-faint:  #64748b;
      --cl-radius-sm:   10px;
      --cl-radius-md:   16px;
      --cl-radius-lg:   24px;
      --cl-font-head:   'FD Aeonik Extended', -apple-system, BlinkMacSystemFont, sans-serif;
      --cl-font-sub:    'FD Aeonik', -apple-system, BlinkMacSystemFont, sans-serif;
      --cl-font-serif:  'Tiempos Text', Georgia, serif;
      --cl-font-mono:   'JetBrains Mono', monospace;
    }}

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }}
    body {{
      background-color: var(--cl-bg);
      color: var(--cl-text-base);
      font-family: var(--cl-font-sub);
      font-size: 16px;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      padding-bottom: 100px;
    }}

    /* Navigation */
    .site-nav {{
      position: fixed;
      top: 0; left: 0; right: 0;
      height: 64px;
      background: rgba(7, 9, 14, 0.88);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--cl-line);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 clamp(20px, 4vw, 48px);
      z-index: 1000;
    }}
    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: #ffffff;
      font-family: var(--cl-font-head);
      font-weight: 700;
      font-size: 15px;
      letter-spacing: 0.04em;
    }}
    .nav-links {{
      display: flex;
      align-items: center;
      gap: 18px;
      list-style: none;
    }}
    .nav-links a {{
      color: var(--cl-text-muted);
      text-decoration: none;
      font-size: 13px;
      font-weight: 500;
      transition: color 0.15s ease;
    }}
    .nav-links a:hover {{ color: #ffffff; }}

    .cl-block {{
      min-height: 100dvh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: clamp(60px, 8vh, 100px) clamp(20px, 5vw, 64px);
      position: relative;
    }}
    .cl-zebra--dark-0 {{ background-color: var(--cl-bg); }}
    .cl-zebra--dark-1 {{ background-color: var(--cl-tint); border-top: 1px solid var(--cl-line); border-bottom: 1px solid var(--cl-line); }}

    .cl-container {{
      max-width: 1360px;
      margin: 0 auto;
      width: 100%;
    }}

    .cl-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: 9999px;
      background: var(--cl-card-muted);
      border: 1px solid var(--cl-line-strong);
      color: var(--cl-accent);
      font-family: var(--cl-font-mono);
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 16px;
    }}
    .cl-title {{
      font-family: var(--cl-font-head);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      font-size: clamp(26px, 3.8vw, 46px);
      line-height: 1.1;
      color: #ffffff;
      margin-bottom: 14px;
    }}
    .cl-desc {{
      font-family: var(--cl-font-serif);
      font-size: clamp(16px, 1.2vw, 18px);
      color: var(--cl-text-muted);
      max-width: 880px;
      line-height: 1.7;
      margin-bottom: 32px;
    }}

    /* Metrics Grid */
    .metric-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 20px;
      margin-top: 16px;
    }}
    .metric-card {{
      background: var(--cl-card);
      border: 1px solid var(--cl-line);
      border-radius: var(--cl-radius-md);
      padding: 24px;
      transition: all 0.22s ease;
    }}
    .metric-card:hover {{
      border-color: rgba(255, 255, 255, 0.25);
      transform: translateY(-2px);
    }}
    .metric-num {{
      font-family: var(--cl-font-mono);
      font-size: 34px;
      font-weight: 800;
      line-height: 1;
      margin-bottom: 8px;
    }}

    /* Buttons */
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 16px;
      border-radius: 10px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.18s ease;
      border: 1px solid transparent;
      white-space: nowrap;
    }}
    .btn-primary {{ background: #ffffff; color: #07090e; }}
    .btn-primary:hover {{ background: #e2e8f0; transform: translateY(-1px); }}
    .btn-accent {{ background: #38bdf8; color: #07090e; }}
    .btn-accent:hover {{ background: #7dd3fc; transform: translateY(-1px); }}
    .btn-subtle {{
      background: rgba(255, 255, 255, 0.06);
      color: #f8fafc;
      border-color: var(--cl-line);
    }}
    .btn-subtle:hover {{
      background: rgba(255, 255, 255, 0.14);
      border-color: var(--cl-line-strong);
    }}

    /* Tab bar simulator */
    .tab-bar-sim {{
      background: #1e222b;
      border-radius: 14px;
      padding: 10px 14px 0 14px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: flex;
      gap: 6px;
      overflow-x: auto;
      margin-bottom: 28px;
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.5);
    }}
    .chrome-tab {{
      height: 38px;
      padding: 0 14px;
      border-radius: 10px 10px 0 0;
      background: #11141c;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-bottom: none;
      display: flex;
      align-items: center;
      gap: 9px;
      font-size: 12.5px;
      color: #94a3b8;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
      min-width: 140px;
      max-width: 220px;
    }}
    .chrome-tab.active {{
      background: #07090e;
      color: #ffffff;
      font-weight: 600;
      border-color: rgba(255, 255, 255, 0.18);
    }}
    .chrome-tab:hover {{ background: #181d28; color: #f1f5f9; }}
    .chrome-tab img {{
      width: 16px;
      height: 16px;
      border-radius: 4px;
      flex-shrink: 0;
    }}

    /* Category Filter Tabs */
    .filter-tabs {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 12px;
      margin-bottom: 24px;
      -webkit-overflow-scrolling: touch;
    }}
    .filter-btn {{
      padding: 7px 16px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 600;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--cl-line);
      color: var(--cl-text-muted);
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .filter-btn.active, .filter-btn:hover {{
      background: #ffffff;
      color: #07090e;
      border-color: #ffffff;
    }}

    /* Account Grid */
    .acc-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 18px;
    }}
    .acc-card {{
      background: var(--cl-card);
      border: 1px solid var(--cl-line);
      border-radius: var(--cl-radius-md);
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      transition: all 0.22s ease;
      position: relative;
    }}
    .acc-card:hover {{
      border-color: rgba(255, 255, 255, 0.25);
      transform: translateY(-2px);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.55);
    }}
    .acc-card.inactive {{
      opacity: 0.6;
      border-style: dashed;
    }}
    .acc-card.inactive:hover {{
      opacity: 0.9;
    }}

    .acc-head {{
      display: flex;
      gap: 16px;
      align-items: center;
    }}
    .logo-frame {{
      width: 64px;
      height: 64px;
      border-radius: 16px;
      background: #07090e;
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.45);
      overflow: hidden;
    }}
    .logo-frame svg {{
      width: 100%;
      height: 100%;
      display: block;
    }}

    .acc-info {{
      flex: 1;
      overflow: hidden;
    }}
    .acc-name-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }}
    .acc-title {{
      font-family: var(--cl-font-mono);
      font-size: 15px;
      font-weight: 700;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .code-badge {{
      font-family: var(--cl-font-mono);
      font-size: 11px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 6px;
      border: 1px solid;
      flex-shrink: 0;
    }}
    .acc-desc-text {{
      font-size: 12px;
      color: var(--cl-text-muted);
      margin-top: 3px;
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    /* Previews row 16px, 24px, 32px */
    .preview-strip {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      background: rgba(255, 255, 255, 0.03);
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.06);
    }}
    .prev-item {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      color: var(--cl-text-muted);
      font-family: var(--cl-font-mono);
    }}
    .prev-item img {{
      border-radius: 4px;
      display: block;
    }}

    /* Pass & Note box */
    .note-box {{
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 8px 12px;
      font-size: 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .pass-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }}
    .pass-val {{
      font-family: var(--cl-font-mono);
      font-weight: 700;
      color: #38bdf8;
      letter-spacing: 0.05em;
    }}
    .pass-masked {{
      filter: blur(4px);
      user-select: none;
      transition: filter 0.2s ease;
    }}
    .show-passwords .pass-masked {{
      filter: none;
      user-select: auto;
    }}

    /* Card Action buttons */
    .card-btns {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}
    .btn-sm {{
      padding: 6px 10px;
      border-radius: 8px;
      font-size: 11.5px;
      font-weight: 600;
      justify-content: center;
    }}

    /* Toast */
    #toast {{
      position: fixed;
      bottom: 30px;
      right: 30px;
      background: #ffffff;
      color: #07090e;
      padding: 14px 26px;
      border-radius: 12px;
      font-weight: 700;
      font-size: 14px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.7);
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.25s cubic-bezier(0.25, 1, 0.35, 1.05);
      z-index: 99999;
      pointer-events: none;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    #toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}
  </style>
</head>
<body>

  <!-- FIXED NAVIGATION -->
  <nav class="site-nav">
    <a href="#hero" class="nav-brand">
      <svg width="28" height="28" viewBox="0 0 64 64">
        <rect width="64" height="64" rx="16" fill="#07090E"/>
        <text x="30" y="44" text-anchor="middle" font-family="'FD Anguita Sans', system-ui" font-weight="900" font-size="38" fill="#EF4444">VJ</text>
        <circle cx="52.0" cy="13.0" r="4.2" fill="#EF4444"/>
      </svg>
      <span>38 GMAIL PROFILES BRAND</span>
    </a>
    <ul class="nav-links">
      <li><a href="#simulator">Thử Tab 16px</a></li>
      <li><a href="#accounts">Danh Sách 38 Gmail</a></li>
      <li><a href="brand.html" style="color: #38bdf8;">Subdomain Hub ←</a></li>
      <li><a href="logo_567.html" style="color: #fb923c;">Logo 5, 6, 7 ✨</a></li>
    </ul>
    <div style="display: flex; gap: 8px;">
      <button class="btn btn-subtle" onclick="togglePasswords()" id="btnTogglePass">
        👁️ Hiện Mật Khẩu
      </button>
      <button class="btn btn-primary" onclick="copyFullData()">
        📋 Copy JSON Dữ Liệu
      </button>
    </div>
  </nav>

  <!-- BLOCK 1: HERO & TỔNG QUAN HỆ THỐNG GMAIL (Zebra Dark 0) -->
  <section id="hero" class="cl-block cl-zebra--dark-0" style="padding-top: 120px;">
    <div class="cl-container">
      <div class="cl-pill">FD ANGUITA SANS BLACK • SIGNATURE DOT • 38 TÀI KHOẢN GMAIL ECOSYSTEM</div>
      <h1 class="cl-title">BỘ NHẬN DIỆN LOGO 38 GMAIL CHUẨN BRAND.HTML</h1>
      <p class="cl-desc">
        Toàn bộ 38 tài khoản Google / Gmail của anh Việt được số hóa và chuẩn hóa nhận diện thị giác độc quyền: Ký tự Monogram nét <strong>900 Black condensed</strong> trích xuất từ <code>FDAnguitaSans-Black.ttf</code>, bo góc chuẩn <code>rx=16</code> và dấu chấm tròn nhận diện quang học tại <code>(cx=52, cy=13)</code>. Tách bạch hoàn toàn từng Chrome Profile, nhận diện tức thì trong 0.1 giây từ kích thước 16x16 pixel.
      </p>

      <!-- Key Metrics -->
      <div class="metric-grid">
        <div class="metric-card">
          <div class="metric-num" style="color: #ef4444;">34 / 38</div>
          <div style="font-size: 14px; font-weight: 700; color: #ffffff;">Tài Khoản Đang Hoạt Động</div>
          <p style="font-size: 13px; color: var(--cl-text-muted); margin-top: 6px;">34 tài khoản active đầy đủ mật khẩu, 4 tài khoản dự phòng / tạm ẩn được ghi chú riêng biệt.</p>
        </div>
        <div class="metric-card">
          <div class="metric-num" style="color: #38bdf8;">16px • 512px</div>
          <div style="font-size: 14px; font-weight: 700; color: #ffffff;">Tối Ưu Đa Tỉ Lệ Hiển Thị</div>
          <p style="font-size: 13px; color: var(--cl-text-muted); margin-top: 6px;">Hiển thị sắc nét trên thanh tab Chrome 16px, icon thanh dock 32px và ảnh đại diện Google Account 512px.</p>
        </div>
        <div class="metric-card">
          <div class="metric-num" style="color: #10b981;">2 Mode</div>
          <div style="font-size: 14px; font-weight: 700; color: #ffffff;">Dark Y & Solid Adobe</div>
          <p style="font-size: 13px; color: var(--cl-text-muted); margin-top: 6px;">Linh hoạt chuyển đổi giữa Nền Đen + Chữ Neon hoặc Nền Màu Thương Hiệu + Chữ Trắng.</p>
        </div>
        <div class="metric-card">
          <div class="metric-num" style="color: #facc15;">1-Click</div>
          <div style="font-size: 14px; font-weight: 700; color: #ffffff;">Đổi Tab Chrome & Copy SVG</div>
          <p style="font-size: 13px; color: var(--cl-text-muted); margin-top: 6px;">Thử favicon trực tiếp lên tab Chrome thật hoặc sao chép mã SVG / Data URI nhúng nhanh.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- BLOCK 2: PHÒNG THÍ NGHIỆM TAB CHROME 16px (Zebra Dark 1) -->
  <section id="simulator" class="cl-block cl-zebra--dark-1">
    <div class="cl-container">
      <div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 20px; margin-bottom: 24px;">
        <div>
          <div class="cl-pill">TRÌNH MÔ PHỎNG TAB THỰC TẾ • 1:1 REAL CHROME TAB</div>
          <h2 class="cl-title" style="font-size: clamp(24px, 3vw, 38px);">ĐỐI SOÁT TRỰC QUAN TRÊN THANH TAB CHROME</h2>
          <p class="cl-desc" style="margin-bottom: 0;">
            Nhấp bất kỳ tab nào phía dưới để đổi favicon của tab Chrome hiện tại xem độ tương phản thực tế ở đúng tỉ lệ 16x16px:
          </p>
        </div>

        <div style="display: flex; gap: 10px;">
          <button id="btnStyleDark" class="btn btn-accent" onclick="switchStyle('dark')">
            ⚡ Phong Cách 1: Nền Đen + Chữ Neon (Chuẩn Y)
          </button>
          <button id="btnStyleSolid" class="btn btn-subtle" onclick="switchStyle('solid')">
            🎨 Phong Cách 2: Nền Màu + Chữ Trắng (Adobe)
          </button>
        </div>
      </div>

      <!-- Real Tab Bar Simulator -->
      <div class="tab-bar-sim" id="tabBarSim">
        <!-- Rendered via JS -->
      </div>
    </div>
  </section>

  <!-- BLOCK 3: BẢNG LƯỚI 38 TÀI KHOẢN GMAIL (Zebra Dark 0) -->
  <section id="accounts" class="cl-block cl-zebra--dark-0">
    <div class="cl-container">
      <div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 20px; margin-bottom: 24px;">
        <div>
          <div class="cl-pill">HỆ THỐNG 38 TÀI KHOẢN GMAIL • DANH MỤC THỰC CHIẾN</div>
          <h2 class="cl-title" style="font-size: clamp(24px, 3vw, 38px);">DANH SÁCH LOGO MONOGRAM TOÀN HỆ THỐNG</h2>
          <p class="cl-desc" style="margin-bottom: 0;">
            Quản lý tập trung mật khẩu, mã nhận diện Monogram và tệp logo chuẩn hóa cho từng hồ sơ tài khoản:
          </p>
        </div>

        <!-- Search Box -->
        <div style="width: 100%; max-width: 340px;">
          <input type="text" id="accSearch" placeholder="Tìm theo tên (vietnd4, seo, ai, milk...)"
                 oninput="filterAccounts()"
                 style="width: 100%; padding: 12px 18px; border-radius: 12px; background: #131722; border: 1px solid var(--cl-line-strong); color: #ffffff; font-size: 13.5px; outline: none;">
        </div>
      </div>

      <!-- Category Filter Tabs -->
      <div class="filter-tabs" id="categoryTabs">
        <button class="filter-btn active" onclick="setCategory('all')">Tất Cả (38)</button>
        <button class="filter-btn" onclick="setCategory('satellite')">Vệ Tinh Số (20)</button>
        <button class="filter-btn" onclick="setCategory('specialized')">Chuyên Môn & AI (7)</button>
        <button class="filter-btn" onclick="setCategory('personal')">Cá Nhân & Gia Đình (7)</button>
        <button class="filter-btn" onclick="setCategory('core')">Master Điều Hành (2)</button>
        <button class="filter-btn" onclick="setCategory('inactive')">Tài Khoản Tạm Ẩn (4)</button>
      </div>

      <!-- Accounts Grid -->
      <div class="acc-grid" id="accGrid">
        <!-- Rendered via JS -->
      </div>
    </div>
  </section>

  <!-- TOAST NOTIFICATION -->
  <div id="toast">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
    <span id="toastMsg">Đã sao chép!</span>
  </div>

  <!-- SCRIPT DỮ LIỆU & TƯƠNG TÁC -->
  <script>
    const GMAIL_DATA = {json_data_str};
    let currentStyle = 'dark';
    let currentCategory = 'all';
    let showPasswords = false;

    // Toast
    function showToast(msg) {{
      const toast = document.getElementById('toast');
      document.getElementById('toastMsg').innerText = msg;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2400);
    }}

    function copyText(text, msg) {{
      navigator.clipboard.writeText(text).then(() => {{
        showToast(msg || 'Đã sao chép vào clipboard!');
      }}).catch(() => {{
        showToast('Lỗi sao chép clipboard!');
      }});
    }}

    function tryFavicon(uri, name) {{
      const link = document.getElementById('dynamic-favicon');
      if (link) {{
        link.href = uri;
        showToast(`Đã đổi Favicon tab Chrome sang: ${{name}}!`);
      }}
    }}

    function togglePasswords() {{
      showPasswords = !showPasswords;
      const body = document.body;
      const btn = document.getElementById('btnTogglePass');
      if (showPasswords) {{
        body.classList.add('show-passwords');
        btn.innerText = '🔒 Ẩn Mật Khẩu';
        btn.classList.add('btn-primary');
        btn.classList.remove('btn-subtle');
        showToast('Đang hiển thị mật khẩu!');
      }} else {{
        body.classList.remove('show-passwords');
        btn.innerText = '👁️ Hiện Mật Khẩu';
        btn.classList.add('btn-subtle');
        btn.classList.remove('btn-primary');
        showToast('Đã ẩn mật khẩu an toàn!');
      }}
    }}

    function switchStyle(style) {{
      currentStyle = style;
      const btnDark = document.getElementById('btnStyleDark');
      const btnSolid = document.getElementById('btnStyleSolid');
      if (style === 'dark') {{
        btnDark.className = 'btn btn-accent';
        btnSolid.className = 'btn btn-subtle';
      }} else {{
        btnDark.className = 'btn btn-subtle';
        btnSolid.className = 'btn btn-accent';
      }}
      renderTabBar();
      filterAccounts();
      showToast(`Đã chuyển sang phong cách: ${{style === 'dark' ? 'Nền Đen + Neon (Chuẩn Y)' : 'Nền Màu + Trắng (Adobe)'}}`);
    }}

    function setCategory(cat) {{
      currentCategory = cat;
      const buttons = document.querySelectorAll('#categoryTabs .filter-btn');
      buttons.forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      filterAccounts();
    }}

    function renderTabBar() {{
      const sim = document.getElementById('tabBarSim');
      const sampleIds = ['vietndj', 'vietnd4', 'vietnd5', 'vietnd6', 'nddviet', 'aidesginforwork', 'vietndseo01', 'feduvn'];
      
      let html = `
        <div class="chrome-tab" onclick="tryFavicon('https://news.ycombinator.com/favicon.ico', 'HackerNews')" title="Mẫu chuẩn HackerNews">
          <img src="https://news.ycombinator.com/favicon.ico" alt="Y">
          <span>HackerNews (Mẫu Y)</span>
        </div>
      `;

      sampleIds.forEach((id, idx) => {{
        const item = GMAIL_DATA.find(a => a.id === id);
        if (!item) return;
        const uri = currentStyle === 'dark' ? item.uri_dark : item.uri_solid;
        const isActive = idx === 0 ? 'active' : '';
        html += `
          <div class="chrome-tab ${{isActive}}" onclick="tryFavicon('${{uri}}', '${{item.name}}')" title="Nhấp để thử lên Tab Chrome thật">
            <img src="${{uri}}" alt="${{item.code}}">
            <span>${{item.name}}</span>
          </div>
        `;
      }});

      sim.innerHTML = html;
    }}

    function filterAccounts() {{
      const q = document.getElementById('accSearch').value.toLowerCase().trim();
      let list = GMAIL_DATA;

      if (currentCategory !== 'all') {{
        if (currentCategory === 'inactive') {{
          list = list.filter(a => a.status === 'inactive');
        }} else {{
          list = list.filter(a => a.category === currentCategory && a.status === 'active');
        }}
      }}

      if (q) {{
        list = list.filter(a => 
          a.id.toLowerCase().includes(q) ||
          a.name.toLowerCase().includes(q) ||
          a.code.toLowerCase().includes(q) ||
          a.desc.toLowerCase().includes(q) ||
          a.note.toLowerCase().includes(q)
        );
      }}

      renderGrid(list);
    }}

    function renderGrid(list) {{
      const grid = document.getElementById('accGrid');
      grid.innerHTML = '';

      if (!list || list.length === 0) {{
        grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 60px; color: var(--cl-text-muted);">Không tìm thấy tài khoản nào khớp với từ khóa.</div>';
        return;
      }}

      list.forEach(item => {{
        const card = document.createElement('div');
        const isInactive = item.status === 'inactive';
        card.className = `acc-card ${{isInactive ? 'inactive' : ''}}`;

        const svgCode = currentStyle === 'dark' ? item.svg_dark : item.svg_solid;
        const uri = currentStyle === 'dark' ? item.uri_dark : item.uri_solid;
        const passText = item.pass;

        card.innerHTML = `
          <div class="acc-head">
            <div class="logo-frame" title="Logo Monogram ${{item.code}}">
              ${{svgCode}}
            </div>
            <div class="acc-info">
              <div class="acc-name-row">
                <span class="acc-title">${{item.name}}</span>
                <span class="code-badge" style="color: ${{item.color}}; border-color: ${{item.color}}40; background: ${{item.color}}15;">${{item.code}}</span>
              </div>
              <div class="acc-desc-text" title="${{item.desc}}">${{item.desc}}</div>
            </div>
          </div>

          <!-- Preview scale strip -->
          <div class="preview-strip">
            <div class="prev-item" title="Đúng cỡ 16x16px trên tab Chrome">
              <img src="${{uri}}" width="16" height="16" alt="${{item.code}}">
              <span>16px Tab</span>
            </div>
            <div class="prev-item" title="Đúng cỡ 24x24px thanh Taskbar">
              <img src="${{uri}}" width="24" height="24" alt="${{item.code}}">
              <span>24px</span>
            </div>
            <div class="prev-item" title="Đúng cỡ 32x32px Profile Icon">
              <img src="${{uri}}" width="32" height="32" alt="${{item.code}}">
              <span>32px</span>
            </div>
          </div>

          <!-- Password & Note Box -->
          <div class="note-box">
            <div class="pass-row">
              <span style="color: var(--cl-text-muted); font-size: 11px;">Mật khẩu:</span>
              <span class="pass-val pass-masked" onclick="copyText('${{passText}}', 'Đã chép mật khẩu ${{item.name}}')" title="Nhấp để copy mật khẩu">${{passText}}</span>
            </div>
            <div style="font-size: 11px; color: var(--cl-text-faint); margin-top: 2px;">
              📝 ${{item.note}}
            </div>
          </div>

          <!-- Action buttons -->
          <div class="card-btns">
            <button class="btn btn-accent btn-sm" onclick="tryFavicon('${{uri}}', '${{item.name}}')">
              👁️ Đổi Tab Thật
            </button>
            <button class="btn btn-subtle btn-sm" onclick="copyText('${{uri}}', 'Đã copy Data URI Favicon ${{item.name}}')">
              🔗 Copy URI
            </button>
            <button class="btn btn-subtle btn-sm" onclick="copySvgCode('${{item.id}}')">
              📋 Copy SVG
            </button>
            <button class="btn btn-subtle btn-sm" onclick="downloadSvgFile('${{item.id}}')">
              ⬇️ Tải SVG
            </button>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    function copySvgCode(id) {{
      const item = GMAIL_DATA.find(a => a.id === id);
      if (!item) return;
      const code = currentStyle === 'dark' ? item.svg_dark : item.svg_solid;
      copyText(code, `Đã sao chép mã SVG logo ${{item.name}}!`);
    }}

    function downloadSvgFile(id) {{
      const item = GMAIL_DATA.find(a => a.id === id);
      if (!item) return;
      const code = currentStyle === 'dark' ? item.svg_dark : item.svg_solid;
      const blob = new Blob([code], {{ type: 'image/svg+xml' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `logo_${{item.id}}_${{currentStyle}}.svg`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      showToast(`Đã tải về tệp: logo_${{item.id}}_${{currentStyle}}.svg`);
    }}

    function copyFullData() {{
      copyText(JSON.stringify(GMAIL_DATA, null, 2), 'Đã sao chép toàn bộ cơ sở dữ liệu JSON 38 tài khoản!');
    }}

    // Init
    window.addEventListener('DOMContentLoaded', () => {{
      renderTabBar();
      filterAccounts();
    }});
  </script>
</body>
</html>
"""

with open(OUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ Đã tạo thành công cổng giao diện tương tác: {OUT_HTML}")
