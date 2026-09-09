# -*- coding: utf-8 -*-
"""
generate_hub.py
Tạo trang Master Hub omarchannel.html theo chuẩn Swiss Minimalist & Zebra Striping của rajchannel.html
"""
import os
import html
from episodes_batch1 import BATCH_1
from episodes_batch2 import BATCH_2
from episodes_batch3 import BATCH_3
from episodes_batch4 import BATCH_4

ALL_EPISODES = BATCH_1 + BATCH_2 + BATCH_3 + BATCH_4
ep_by_code = {ep['ep_code']: ep for ep in ALL_EPISODES}

sec_high_ticket_codes = ["OE01", "OE02", "OE03", "OE07", "OE09", "OE10", "OE15", "OE37", "OE38"]
sec_personal_brand_codes = ["OE05", "OE06", "OE16", "OE18", "OE19", "OE23", "OE24", "OE39"]
sec_youtube_strategy_codes = ["OE12", "OE13", "OE14", "OE20", "OE29", "OE30", "OE31", "OE32", "OE33", "OE40"]
sec_ai_leverage_codes = ["OE08", "OE11", "OE25", "OE26"]
sec_sales_mindset_codes = ["OE04", "OE17", "OE21", "OE22", "OE27", "OE28", "OE34", "OE35", "OE36"]

def render_card(ep, delay_ms=0):
    cat_short = ep['cat_badge'].split('/')[-1].strip()
    p1 = ep['lead_points'][0] if len(ep['lead_points']) > 0 else ""
    p2 = ep['lead_points'][1] if len(ep['lead_points']) > 1 else ""
    
    return f"""        <!-- Video {ep['ep_code']} -->
        <div class="apple-card" style="--card-delay: {delay_ms}ms;">
          <div>
            <div class="apple-card__ep">{ep['ep_code']} // {html.escape(cat_short)} • {ep['publish_date']}</div>
            <h3 class="apple-card__title">{html.escape(ep['tagline'])}</h3>
            <div class="apple-card__speaker">👤 {html.escape(ep['speaker'])}</div>
            <div class="apple-card__summary">
              <p>• {html.escape(p1)}</p>
              <p>• {html.escape(p2)}</p>
            </div>
          </div>
          <div class="apple-card__actions">
            <a class="apple-card__btn apple-card__btn--primary" href="./{ep['slug']}">ĐỌC BÀI PHÂN TÍCH →</a>
            <a class="apple-card__btn apple-card__btn--secondary" href="{ep['youtube_url']}" target="_blank">YOUTUBE ↗</a>
          </div>
        </div>"""

def render_table_rows():
    rows = []
    for idx, ep in enumerate(ALL_EPISODES, 1):
        speaker_name = ep['speaker'].split('&')[0].strip()
        rows.append(f"""          <tr>
            <td>{idx:02d}</td>
            <td style="font-family: var(--font-mono); font-weight:700; color: var(--cl-accent);">{ep['ep_code']}</td>
            <td style="font-family: var(--font-mono); font-size: 12.5px; white-space: nowrap; color: var(--cl-text-muted);">{ep['publish_date']}</td>
            <td><strong>{html.escape(speaker_name)}</strong></td>
            <td>{html.escape(ep['tagline'])}</td>
            <td><a href="./{ep['slug']}" style="color:var(--cl-accent); font-weight:600; text-decoration: none;">Đọc Bài →</a></td>
          </tr>""")
    return "\n".join(rows)

cards_high_ticket = "\n".join([render_card(ep_by_code[c], i*50) for i, c in enumerate(sec_high_ticket_codes)])
cards_personal_brand = "\n".join([render_card(ep_by_code[c], i*50) for i, c in enumerate(sec_personal_brand_codes)])
cards_youtube_strategy = "\n".join([render_card(ep_by_code[c], i*50) for i, c in enumerate(sec_youtube_strategy_codes)])
cards_ai_leverage = "\n".join([render_card(ep_by_code[c], i*50) for i, c in enumerate(sec_ai_leverage_codes)])
cards_sales_mindset = "\n".join([render_card(ep_by_code[c], i*50) for i, c in enumerate(sec_sales_mindset_codes)])
table_rows_html = render_table_rows()

hub_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0, viewport-fit=cover" name="viewport"/>
  <title>40 Video Podcast Omar Eltakrori Tuyển Chọn | Bản Đồ Tri Thức YouTube &amp; Đóng Gói Tri Thức</title>
  
  <!-- Font Definitions & System Fallbacks -->
  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@500;700&amp;family=Playfair+Display:ital,wght@1,400;1,600&amp;family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
  
  <style>
    /* ═══ 1. FONT DECLARATIONS (Local Repo & Fallbacks) ═══ */
    @font-face {{
      font-family: 'FD Aeonik Extended';
      src: url('./fonts/FDAeonikExtended-Bold.woff2') format('woff2'),
           url('./fonts/FDAeonikExtended-Bold.ttf') format('truetype');
      font-weight: 700;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'FD Aeonik Extended';
      src: url('./fonts/FDAeonikExtended-SemiBold.woff2') format('woff2'),
           url('./fonts/FDAeonikExtended-SemiBold.ttf') format('truetype');
      font-weight: 600;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'SVN-Poppins';
      src: url('./fonts/SVN-Poppins-Regular.ttf') format('truetype'),
           url('./assets/fonts/SVN-Poppins-Regular.ttf') format('truetype'),
           local('SVN-Poppins-Regular');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'SVN-Poppins';
      src: url('./fonts/SVN-Poppins-SemiBold.ttf') format('truetype'),
           url('./assets/fonts/SVN-Poppins-SemiBold.ttf') format('truetype'),
           local('SVN-Poppins-SemiBold');
      font-weight: 600;
      font-style: normal;
      font-display: swap;
    }}

    /* ═══ 2. DESIGN TOKENS (30ngayviral.fedu.vn Light Theme) ═══ */
    :root {{
      --cl-bg:          #ffffff;
      --cl-tint:        #f8fafc;
      --cl-card:        #ffffff;
      --cl-card-muted:  #f1f5f9;
      --cl-accent:      #1a73e8;
      --cl-accent-tint: rgba(26, 115, 232, 0.08);
      --cl-accent-text: #ffffff;
      --cl-line:        rgba(0, 0, 0, 0.06);
      --cl-line-strong: rgba(0, 0, 0, 0.12);
      --cl-text-base:   #090d16; /* Deepest Ink Slate 950 (18.8:1 AAA) */
      --cl-text-body:   #0f172a; /* Rich Ink Slate 900 (16.5:1 AAA) */
      --cl-text-muted:  #475569; /* Slate 600 (7.0:1 AAA) */
      --cl-danger:      #dc2626;
      --cl-success:     #16a34a;

      /* Radii */
      --cl-radius-lg:   24px;
      --cl-radius-md:   16px;
      --cl-radius-sm:   10px;
      --cl-radius-full: 9999px;

      /* Typography Stacks */
      --font-display-short: 'FD Aeonik Extended', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-display-long:  'SVN-Poppins', 'Poppins', 'Inter', -apple-system, sans-serif;
      --font-body:          'SVN-Poppins', 'Poppins', 'Inter', -apple-system, sans-serif;
      --font-editorial:     'FD Acta', 'Playfair Display', 'SVN-Acta', 'Noe Display', Georgia, serif;
      --font-mono:          'JetBrains Mono', 'SVN-Sonoma', monospace;

      /* Apple Motion Physics Curves */
      --apple-spring: cubic-bezier(0.25, 1, 0.35, 1.05);
      --apple-ease:   cubic-bezier(0.16, 1, 0.3, 1);
      --apple-hover:  cubic-bezier(0.2, 0.9, 0.3, 1.08);
    }}

    /* ═══ 3. RESET & BASE ═══ */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    html {{
      scroll-behavior: smooth;
      background-color: var(--cl-bg);
      color: var(--cl-text-base);
      font-family: var(--font-body);
    }}

    body {{
      overflow-x: clip;
      min-height: 100vh;
      line-height: 1.7;
    }}

    /* ═══ 4. VIEWPORT-FRAMED ZEBRA SECTIONS ═══ */
    .cl-zebra-section {{
      width: 100%;
      min-height: 100dvh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      position: relative;
      padding: 90px 24px;
      box-sizing: border-box;
      transition: background-color 0.3s ease;
    }}

    .cl-zebra--light {{
      background-color: var(--cl-bg);
    }}

    .cl-zebra--tint {{
      background-color: var(--cl-tint);
      border-top: 1px solid var(--cl-line);
      border-bottom: 1px solid var(--cl-line);
    }}

    .cl-sec-container {{
      width: 100%;
      max-width: 1120px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
      z-index: 2;
    }}

    .cl-sec-container--wide {{
      max-width: 1280px;
    }}

    /* ═══ 5. TYPOGRAPHY SYSTEM ═══ */
    .cl-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 16px;
      background: var(--cl-card);
      border: 1px solid var(--cl-line-strong);
      border-radius: var(--cl-radius-full);
      font-family: var(--font-mono);
      font-size: 11.5px;
      font-weight: 700;
      color: var(--cl-accent);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 20px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }}

    .title-short {{
      font-family: var(--font-display-short);
      font-weight: 700;
      font-size: clamp(28px, 4.5vw, 44px);
      line-height: 1.15;
      letter-spacing: -0.015em;
      text-transform: uppercase;
      color: var(--cl-text-base);
      margin-bottom: 16px;
      text-wrap: balance;
    }}

    .editorial-hook {{
      font-family: var(--font-editorial);
      font-style: italic;
      font-size: clamp(18px, 2.2vw, 22px);
      color: var(--cl-text-muted);
      max-width: 780px;
      margin: 0 auto 28px;
      line-height: 1.5;
      text-wrap: balance;
    }}

    .cl-body {{
      font-family: var(--font-body);
      font-size: 16px;
      color: var(--cl-text-body);
      max-width: 720px;
      margin: 0 auto 36px;
      line-height: 1.8;
      text-align: center;
      text-wrap: pretty;
    }}

    /* ═══ 6. BUTTONS ═══ */
    .cl-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 14px 32px;
      border-radius: var(--cl-radius-full);
      font-family: var(--font-display-long);
      font-weight: 600;
      font-size: 14px;
      text-decoration: none;
      transition: all 0.3s var(--apple-spring);
      cursor: pointer;
      background: var(--cl-text-base);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(9, 13, 22, 0.12);
    }}

    .cl-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(9, 13, 22, 0.2);
    }}

    /* ═══ 7. APPLE CARDS GRID ═══ */
    .apple-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 24px;
      width: 100%;
      margin-top: 36px;
      text-align: left;
    }}

    .apple-card {{
      background: var(--cl-card);
      border: 1px solid var(--cl-line-strong);
      border-radius: var(--cl-radius-lg);
      padding: 28px 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.4s var(--apple-ease);
      box-shadow: 0 4px 12px rgba(0,0,0,0.02);
      position: relative;
    }}

    .apple-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 16px 36px rgba(0,0,0,0.06);
      border-color: rgba(26, 115, 232, 0.3);
    }}

    .apple-card__ep {{
      font-family: var(--font-mono);
      font-size: 11.5px;
      font-weight: 700;
      color: var(--cl-accent);
      letter-spacing: 0.04em;
      margin-bottom: 12px;
    }}

    .apple-card__title {{
      font-family: var(--font-display-long);
      font-weight: 700;
      font-size: 18px;
      line-height: 1.35;
      color: var(--cl-text-base);
      margin-bottom: 12px;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .apple-card__speaker {{
      font-size: 13.5px;
      font-weight: 600;
      color: var(--cl-text-muted);
      margin-bottom: 16px;
      padding-bottom: 14px;
      border-bottom: 1px dashed var(--cl-line-strong);
    }}

    .apple-card__summary {{
      font-size: 14px;
      color: var(--cl-text-body);
      line-height: 1.65;
      margin-bottom: 24px;
    }}

    .apple-card__summary p {{
      margin-bottom: 8px;
    }}

    .apple-card__summary p:last-child {{
      margin-bottom: 0;
    }}

    .apple-card__actions {{
      display: flex;
      gap: 10px;
      margin-top: auto;
    }}

    .apple-card__btn {{
      padding: 10px 18px;
      border-radius: var(--cl-radius-full);
      font-size: 12.5px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}

    .apple-card__btn--primary {{
      background: var(--cl-accent-tint);
      color: var(--cl-accent);
      border: 1px solid rgba(26, 115, 232, 0.2);
      flex: 1;
    }}

    .apple-card__btn--primary:hover {{
      background: var(--cl-accent);
      color: #ffffff;
    }}

    .apple-card__btn--secondary {{
      background: transparent;
      color: var(--cl-text-muted);
      border: 1px solid var(--cl-line-strong);
    }}

    .apple-card__btn--secondary:hover {{
      background: var(--cl-card-muted);
      color: var(--cl-text-base);
    }}

    /* ═══ 8. SUMMARY TABLE ═══ */
    .cl-table-container {{
      width: 100%;
      overflow-x: auto;
      background: var(--cl-card);
      border: 1px solid var(--cl-line-strong);
      border-radius: var(--cl-radius-lg);
      box-shadow: 0 4px 16px rgba(0,0,0,0.02);
      margin-top: 32px;
      margin-bottom: 36px;
    }}

    .cl-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 14px;
      min-width: 900px;
    }}

    .cl-table th {{
      background: var(--cl-tint);
      padding: 16px 20px;
      font-family: var(--font-mono);
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: var(--cl-text-muted);
      border-bottom: 1px solid var(--cl-line-strong);
    }}

    .cl-table td {{
      padding: 16px 20px;
      border-bottom: 1px solid var(--cl-line);
      color: var(--cl-text-body);
      line-height: 1.6;
      vertical-align: top;
    }}

    .cl-table tr:hover td {{
      background: rgba(26, 115, 232, 0.02);
    }}

    .cl-scroll-hint {{
      position: absolute;
      bottom: 24px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      font-size: 11px;
      font-family: var(--font-mono);
      color: var(--cl-text-muted);
      opacity: 0.7;
      animation: pulse 2s infinite ease-in-out;
    }}

    @keyframes pulse {{
      0%, 100% {{ transform: translateY(0); opacity: 0.6; }}
      50% {{ transform: translateY(6px); opacity: 1; }}
    }}

    /* ═══ 9. HARDWARE-ACCELERATED REVEAL ═══ */
    .apple-reveal {{
      opacity: 0;
      transform: translateY(24px);
      transition: opacity 0.8s var(--apple-ease), transform 0.8s var(--apple-ease);
    }}

    .apple-reveal.is-visible {{
      opacity: 1;
      transform: translateY(0);
    }}

    /* ═══ 10. MOBILE OPTIMIZATIONS ═══ */
    @media (max-width: 768px) {{
      .cl-zebra-section {{
        min-height: 100dvh;
        padding: 64px 20px;
      }}
      .apple-cards-grid {{
        grid-template-columns: 1fr;
        gap: 16px;
      }}
      .cl-btn {{
        width: 100%;
        max-width: 100%;
        padding: 16px 24px;
      }}
    }}
  </style>
</head>
<body>

  <!-- ═══ KHỐI 1: HERO SECTION (LIGHT) ═══ -->
  <section class="cl-zebra-section cl-zebra--light" id="sec-hero">
    <div class="cl-sec-container apple-reveal">
      <div class="cl-badge">01 / BỘ TUYỂN CHỌN ĐẶC BIỆT</div>
      <h1 class="title-short">40 PODCAST OMAR ELTAKRORI</h1>
      <p class="editorial-hook">"Bản đồ kiến trúc xây dựng Kênh YouTube Chuyên gia, Thương hiệu Cá nhân Triệu đô &amp; Đóng gói Tri thức High-Ticket."</p>
      <p class="cl-body">
        Tuyển tập 40 video podcast phân tích chuyên sâu từ kênh của Omar Eltakrori (@OmarEltakrori) — cựu Giám đốc Chiến lược Think Media, người đồng hành cùng hàng nghìn chuyên gia, CEO và nhà sáng tạo nội dung hàng đầu thế giới. Mỗi video được bóc tách theo cấu trúc Swiss Minimalist: 8 Insight thực chiến, 3 tầng nhận thức (Bề mặt - Bản chất - Đòn bẩy), ma trận ảo tưởng thị trường và thơ lục bát đúc kết.
      </p>
      <a class="cl-btn" href="#sec-high-ticket">KHÁM PHÁ DANH SÁCH 40 TẬP ↓</a>
    </div>
    <div class="cl-scroll-hint">
      <span>Cuộn để xem</span>
      <svg fill="none" height="14" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" viewbox="0 0 24 24" width="14"><path d="M7 13l5 5 5-5M7 6l5 5 5-5"></path></svg>
    </div>
  </section>

  <!-- ═══ KHỐI 2: ĐÓNG GÓI TRI THỨC & ĐỊNH GIÁ CAO CẤP (TINT) ═══ -->
  <section class="cl-zebra-section cl-zebra--tint" id="sec-high-ticket">
    <div class="cl-sec-container cl-sec-container--wide apple-reveal">
      <div class="cl-badge">02 / ĐÓNG GÓI TRI THỨC &amp; ĐỊNH GIÁ CAO CẤP</div>
      <h2 class="title-short">ĐÓNG GÓI TRI THỨC &amp; ĐỊNH GIÁ HIGH-TICKET</h2>
      <p class="editorial-hook">"Bán thời gian là lao động khổ sai — Đóng gói giá trị giải pháp là con đường tự do tài chính."</p>
      
      <div class="apple-cards-grid">
{cards_high_ticket}
      </div>
    </div>
  </section>

  <!-- ═══ KHỐI 3: THƯƠNG HIỆU CÁ NHÂN & VỊ THẾ CHUYÊN GIA (LIGHT) ═══ -->
  <section class="cl-zebra-section cl-zebra--light" id="sec-personal-brand">
    <div class="cl-sec-container cl-sec-container--wide apple-reveal">
      <div class="cl-badge">03 / THƯƠNG HIỆU CÁ NHÂN &amp; VỊ THẾ CHUYÊN GIA</div>
      <h2 class="title-short">XÂY DỰNG THƯƠNG HIỆU CÁ NHÂN TRIỆU ĐÔ</h2>
      <p class="editorial-hook">"Thương hiệu cá nhân là chiếc khiên bảo hiểm tài sản vững chắc nhất trong mọi cơn biến động kinh tế."</p>
      
      <div class="apple-cards-grid">
{cards_personal_brand}
      </div>
    </div>
  </section>

  <!-- ═══ KHỐI 4: CHIẾN LƯỢC YOUTUBE & VIDEO TRIỆU VIEW (TINT) ═══ -->
  <section class="cl-zebra-section cl-zebra--tint" id="sec-youtube-strategy">
    <div class="cl-sec-container cl-sec-container--wide apple-reveal">
      <div class="cl-badge">04 / CHIẾN LƯỢC YOUTUBE &amp; NỘI DUNG DÀI</div>
      <h2 class="title-short">CHIẾN LƯỢC YOUTUBE CHO DOANH NHÂN</h2>
      <p class="editorial-hook">"YouTube không phải sân chơi câu view giải trí — Đó là cỗ máy nhân bản sự tin cậy và khách hàng cao cấp 24/7."</p>
      
      <div class="apple-cards-grid">
{cards_youtube_strategy}
      </div>
    </div>
  </section>

  <!-- ═══ KHỐI 5: TRÍ TUỆ NHÂN TẠO & ĐỘT PHÁ NĂNG SUẤT (LIGHT) ═══ -->
  <section class="cl-zebra-section cl-zebra--light" id="sec-ai-leverage">
    <div class="cl-sec-container cl-sec-container--wide apple-reveal">
      <div class="cl-badge">05 / TRÍ TUỆ NHÂN TẠO &amp; TỰ ĐỘNG HÓA</div>
      <h2 class="title-short">ĐÒN BẨY TRÍ TUỆ NHÂN TẠO (AI) THỰC CHIẾN</h2>
      <p class="editorial-hook">"AI làm thay phần việc lặp lại vô nghĩa để bạn giải phóng 100% tâm trí cho chiến lược và kết nối con người."</p>
      
      <div class="apple-cards-grid">
{cards_ai_leverage}
      </div>
    </div>
  </section>

  <!-- ═══ KHỐI 6: TÂM LÝ BÁN HÀNG & QUẢN TRỊ TINH THẦN (TINT) ═══ -->
  <section class="cl-zebra-section cl-zebra--tint" id="sec-sales-mindset">
    <div class="cl-sec-container cl-sec-container--wide apple-reveal">
      <div class="cl-badge">06 / TÂM LÝ BÁN HÀNG &amp; QUẢN TRỊ NỘI TÂM</div>
      <h2 class="title-short">TÂM LÝ ĐÀM PHÁN &amp; NỀN TẢNG BỀN VỮNG</h2>
      <p class="editorial-hook">"Bán hàng bằng tinh thần phụng sự thấu cảm; giữ cái đầu lạnh và trái tim ấm trước mọi sóng gió thương trường."</p>
      
      <div class="apple-cards-grid">
{cards_sales_mindset}
      </div>
    </div>
  </section>

  <!-- ═══ KHỐI 7: SUMMARY TABLE (LIGHT) ═══ -->
  <section class="cl-zebra-section cl-zebra--light" id="sec-summary">
    <div class="cl-sec-container cl-sec-container--wide apple-reveal">
      <div class="cl-badge">07 / DANH SÁCH TRA CỨU TOÀN DIỆN</div>
      <h2 class="title-short">BẢNG TỔNG HỢP 40 VIDEO &amp; LIÊN KẾT</h2>
      <p class="editorial-hook">"Hệ thống hóa toàn bộ 40 bài giảng để tra cứu tức thì bất cứ lúc nào."</p>
      
      <div class="cl-table-container">
        <table class="cl-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Tập</th>
              <th>Ngày Publish</th>
              <th>Diễn Giả</th>
              <th>Chủ Đề Cốt Lõi</th>
              <th>Hành Động</th>
            </tr>
          </thead>
          <tbody>
{table_rows_html}
          </tbody>
        </table>
      </div>
      
      <a class="cl-btn" href="#sec-hero">
        QUAY LẠI ĐẦU TRANG ↑
      </a>
    </div>
  </section>

  <!-- ═══ HARDWARE-ACCELERATED ZERO-JANK OBSERVER SCRIPT ═══ -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const observerOptions = {{
        root: null,
        rootMargin: '0px 0px -40px 0px',
        threshold: 0.1
      }};

      const observer = new IntersectionObserver((entries, obs) => {{
        entries.forEach(entry => {{
          if (entry.isIntersecting) {{
            entry.target.classList.add('is-visible');
            obs.unobserve(entry.target);
          }}
        }});
      }}, observerOptions);

      const animatedElements = document.querySelectorAll('.apple-reveal, .apple-card');
      animatedElements.forEach(el => observer.observe(el));
    }});
  </script>
</body>
</html>
"""

path_k = "/Users/vietmac/Documents/CODE/k/omarchannel.html"
with open(path_k, "w", encoding="utf-8") as f:
    f.write(hub_html)

path_course = "/Users/vietmac/Documents/CODE/course/omarchannel.html"
with open(path_course, "w", encoding="utf-8") as f:
    f.write(hub_html)

print(f"🎉 Đã tạo thành công Master Hub omarchannel.html tại cả k/ và course/! Kích thước: {len(hub_html):,} bytes")
