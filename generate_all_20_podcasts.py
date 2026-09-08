#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_all_20_podcasts.py
Chuyển đổi toàn bộ 20 bài podcast Raj Shamani sang chuẩn thiết kế 
Swiss Minimalist Reading Flow (Light Theme, FD Aeonik + FD Acta Medium, 
khối code tối giản trắng viền 1px, 1-click copy).
"""

import os
import re
import html
from bs4 import BeautifulSoup

COURSE_DIR = "/Users/vietmac/Documents/CODE/course"
TEMPLATE_FILE = os.path.join(COURSE_DIR, "sauvik-banerjjee-cto-growth-mindset-podcast.html")

ORDERED_PODCASTS = [
    {
        "slug": "sauvik-banerjjee-cto-growth-mindset-podcast.html",
        "speaker": "Sauvik Banerjjee",
        "role": "Cựu CTO Tata Digital / CEO Rezolve AI",
        "tagline": "NGHỆ THUẬT NÂNG TẦM QUYẾT ĐỊNH"
    },
    {
        "slug": "vaibhav-sisinty-ai-second-brain-podcast.html",
        "speaker": "Vaibhav Sisinty",
        "role": "Founder GrowthSchool / AI & Systems Architect",
        "tagline": "HỆ THỐNG SECOND BRAIN & ĐÒN BẨY AI"
    },
    {
        "slug": "andrew-huberman-daily-habits-neuroscience-podcast.html",
        "speaker": "Andrew Huberman",
        "role": "Giáo sư Thần kinh học Stanford",
        "tagline": "KHOA HỌC THÓI QUEN & THẦN KINH THỰC THI"
    },
    {
        "slug": "gaurav-mehta-luxury-watchmaking-business-podcast.html",
        "speaker": "Gaurav Mehta",
        "role": "Founder Jaipur Watch Company",
        "tagline": "NGHỆ THUẬT CHẾ TÁC & KINH DOANH XA XỈ"
    },
    {
        "slug": "sanjiv-goenka-wealth-turnaround-conglomerate-podcast.html",
        "speaker": "Dr. Sanjiv Goenka",
        "role": "Chủ tịch RP-Sanjiv Goenka Group",
        "tagline": "QUẢN TRỊ TẬP ĐOÀN & TƯ DUY TỶ PHÚ"
    },
    {
        "slug": "deepak-sahni-health-gut-liver-longevity-podcast.html",
        "speaker": "Deepak Sahni",
        "role": "Founder Healthians / Chuyên gia Y tế Dự phòng",
        "tagline": "Y HỌC DỰ PHÒNG & GIẢI MÃ SỨC KHỎE ĐỘC LẬP"
    },
    {
        "slug": "frank-walliser-bentley-luxury-automotive-podcast.html",
        "speaker": "Dr. Frank-Steffen Walliser",
        "role": "CEO Bentley Motors / Cựu Lãnh đạo Porsche",
        "tagline": "CẠNH TRANH CẢM XÚC TRÊN ĐỈNH CAO XA XỈ"
    },
    {
        "slug": "mark-bowden-body-language-trust-podcast.html",
        "speaker": "Mark Bowden",
        "role": "Chuyên gia Ngôn ngữ Cơ thể Hàng đầu Thế giới",
        "tagline": "MÃ HÓA NIỀM TIN & 4 CHIẾC HỘP TÂM LÝ"
    },
    {
        "slug": "anahat-singh-squash-champion-mindset-podcast.html",
        "speaker": "Anahat Singh",
        "role": "Nhà vô địch Squash Thế giới Trẻ (18 tuổi)",
        "tagline": "TÂM THÁI VÔ ĐỊCH & KỶ LUẬT THÉP"
    },
    {
        "slug": "puneet-nanda-walmart-retail-brand-scale-podcast.html",
        "speaker": "Puneet Nanda",
        "role": "Founder GuruNanda / Chuyên gia Bán lẻ Toàn cầu",
        "tagline": "CHIẾN LƯỢC BÁN LẺ & QUY MÔ TRIỆU ĐÔ WALMART"
    },
    {
        "slug": "sunil-bajpai-fraud-scams-psychology-podcast.html",
        "speaker": "Sunil Bajpai",
        "role": "Chuyên gia Điều tra Tội phạm Công nghệ & An ninh mạng",
        "tagline": "TÂM LÝ HỌC THAO TÚNG & PHÒNG CHỐNG LỪA ĐẢO"
    },
    {
        "slug": "dr-k-relationship-psychology-trauma-podcast.html",
        "speaker": "Dr. Alok Kanojia (Dr. K)",
        "role": "Bác sĩ Tâm thần Harvard / HealthyGamerGG",
        "tagline": "GIẢI MÃ TÂM LÝ PHẢN BỘI & VẾT THƯƠNG QUÁ KHỨ"
    },
    {
        "slug": "alok-sama-money-trap-softbank-wealth-podcast.html",
        "speaker": "Alok Sama",
        "role": "Cựu Chủ tịch SoftBank Vision Fund",
        "tagline": "BẪY TIỀN BẠC & NGHỆ THUẬT ĐẦU TƯ TỶ ĐÔ"
    },
    {
        "slug": "satinder-sartaaj-sufi-music-culture-fame-podcast.html",
        "speaker": "Dr. Satinder Sartaaj",
        "role": "Nghệ sĩ Sufi / Học giả Văn hóa & Âm nhạc",
        "tagline": "TRIẾT LÝ SUFI & ĐỈNH CAO NGHỆ THUẬT NỘI TÂM"
    },
    {
        "slug": "kiran-mazumdar-shaw-biotech-founder-india-podcast.html",
        "speaker": "Kiran Mazumdar-Shaw",
        "role": "Nhà sáng lập Biocon / Nữ tỷ phú Công nghệ Sinh học",
        "tagline": "XÂY DỰNG KỲ LÂN CÔNG NGHỆ SINH HỌC TOÀN CẦU"
    },
    {
        "slug": "shubhanshu-shukla-astronaut-space-zero-gravity-podcast.html",
        "speaker": "Shubhanshu Shukla",
        "role": "Phi hành gia ISRO / Trạm Vũ trụ Quốc tế ISS",
        "tagline": "TƯ DUY KHÔNG TRỌNG LỰC & GIỚI HẠN CON NGƯỜI"
    },
    {
        "slug": "saurabh-mukherjea-middle-class-loan-trap-investing-podcast.html",
        "speaker": "Saurabh Mukherjea",
        "role": "Founder Marcellus Investment Managers",
        "tagline": "BẪY NỢ TRUNG LƯU & CHIẾN LƯỢC TÀI CHÍNH BỀN VỮNG"
    },
    {
        "slug": "dr-v-mohan-diabetes-sugar-genetics-health-podcast.html",
        "speaker": "Dr. V. Mohan",
        "role": "Chủ tịch MDRF / Chuyên gia Đái tháo đường Hàng đầu",
        "tagline": "NGUYÊN LÝ TIỂU ĐƯỜNG & DINH DƯỠNG TRAO ĐỔI CHẤT"
    },
    {
        "slug": "srini-sriniwasan-ultra-rich-private-equity-wealth-podcast.html",
        "speaker": "Srini Sriniwasan",
        "role": "Managing Director Kotak Alternate Assets",
        "tagline": "BÍ MẬT GIỚI SIÊU GIÀU & CÔNG THỨC ĐẦU TƯ TỶ ĐÔ"
    },
    {
        "slug": "hasan-minhaj-standup-comedy-fame-struggle-podcast.html",
        "speaker": "Hasan Minhaj",
        "role": "Nghệ sĩ Hài / Diễn viên Đoạt giải Peabody",
        "tagline": "NGHỆ THUẬT KỂ CHUYỆN & BẢN LĨNH SÁNG TẠO"
    },
    {
        "slug": "richard-teng-binance-crypto-future-of-money-podcast.html",
        "speaker": "Richard Teng",
        "role": "CEO Binance / Cựu Lãnh đạo MAS Singapore",
        "tagline": "TƯƠNG LAI TIỀN TỆ & BẢN ĐỒ TÀI CHÍNH PHI TẬP TRUNG"
    }
]

# Trích xuất CSS & Scripts chuẩn từ template Sauvik Banerjjee
with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
    template_content = f.read()

style_match = re.search(r'(<style>.*?</style>)', template_content, re.DOTALL)
STANDARDIZED_STYLE = style_match.group(1) if style_match else ""

script_match = re.search(r'(<script>.*?</script>)', template_content, re.DOTALL)
STANDARDIZED_SCRIPT = script_match.group(1) if script_match else ""

def clean_txt(t):
    if not t:
        return ""
    return t.strip().replace('"', '&quot;').replace("'", "&#x27;")

def parse_podcast_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    badge_el = soup.find('div', class_='cl-badge')
    badge_txt = badge_el.text.strip() if badge_el else "CHUYÊN ĐỀ // FO"
    if '//' in badge_txt:
        cat_part, ep_code = [p.strip() for p in badge_txt.split('//', 1)]
    else:
        cat_part, ep_code = badge_txt, "FO"
    cat_part = re.sub(r'^\d+\s*/\s*', '', cat_part).strip()

    h1_el = soup.find('h1')
    speaker_raw = h1_el.text.strip() if h1_el else "DIỄN GIẢ"

    h2_el = soup.find('h2', class_='title-long') or soup.find('h2')
    title_raw = h2_el.text.strip() if h2_el else "Bài Phân Tích Podcast"

    hook_el = soup.find('p', class_='editorial-hook')
    hook_raw = hook_el.text.strip().strip('"“”') if hook_el else "Lắng nghe thực tế để điều chỉnh thuật toán hành vi."

    body_el = soup.find('p', class_='cl-body')
    overview_raw = body_el.text.strip() if body_el else ""

    yt_el = soup.find('a', href=lambda h: h and 'youtube.com' in h)
    yt_url = yt_el['href'] if yt_el else "https://www.youtube.com"

    # Delusion cards
    delusion_sec = soup.find('section', id='sec-delusion')
    delusions = []
    if delusion_sec:
        for card in delusion_sec.find_all('div', class_='apple-card'):
            p = card.find('p')
            if p:
                delusions.append(p.text.strip())

    # 8 Insights
    ins1 = soup.find('section', id='sec-insights-1')
    ins2 = soup.find('section', id='sec-insights-2')
    raw_cards = []
    if ins1:
        raw_cards.extend(ins1.find_all('div', class_='apple-card'))
    if ins2:
        raw_cards.extend(ins2.find_all('div', class_='apple-card'))

    insights = []
    for idx, c in enumerate(raw_cards):
        num_el = c.find('div', class_='apple-card__num')
        num_txt = num_el.text.strip() if num_el else f"INSIGHT #{idx+1:02d}"
        
        t_el = c.find('h3', class_='apple-card__title')
        t_txt = t_el.text.strip() if t_el else f"Insight {idx+1}"

        q_el = c.find('div', class_='apple-card__quote')
        q_txt = q_el.text.strip() if q_el else ""
        q_txt = re.sub(r'^🎙️\s*(Dữ kiện:)?\s*', '', q_txt).strip()

        paras = c.find_all('p')
        surface = ""
        essence = ""
        leverage = ""
        for p in paras:
            pt = p.text.strip()
            if 'Bề mặt:' in pt:
                surface = re.sub(r'^.*?Bề mặt:\s*', '', pt).strip()
            elif 'Bản chất:' in pt:
                essence = re.sub(r'^.*?Bản chất:\s*', '', pt).strip()
            elif 'Đòn bẩy:' in pt:
                leverage = re.sub(r'^.*?Đòn bẩy:\s*', '', pt).strip()

        m_el = c.find('div', string=lambda t: t and '📜' in t)
        m_txt = m_el.text.strip() if m_el else ""
        m_txt = re.sub(r'^📜\s*', '', m_txt).strip().strip('"“”')

        insights.append({
            "num": f"INSIGHT {idx+1:02d}",
            "title": t_txt,
            "quote": q_txt,
            "surface": surface,
            "essence": essence,
            "leverage": leverage,
            "mantra": m_txt
        })

    # Environment
    env_sec = soup.find('section', id='sec-environment')
    env_items = []
    if env_sec:
        for it in env_sec.find_all('div', class_='apple-list-item'):
            c_div = it.find('div', class_='apple-list-item__content')
            if c_div:
                env_items.append(c_div.text.strip())

    # Emotions
    emo_sec = soup.find('section', id='sec-emotions')
    emo_items = []
    if emo_sec:
        for it in emo_sec.find_all('div', class_='apple-list-item'):
            c_div = it.find('div', class_='apple-list-item__content')
            if c_div:
                emo_items.append(c_div.text.strip())

    return {
        "category": cat_part,
        "ep_code": ep_code,
        "speaker": speaker_raw,
        "title": title_raw,
        "hook": hook_raw,
        "overview": overview_raw,
        "yt_url": yt_url,
        "delusions": delusions,
        "insights": insights,
        "env_items": env_items,
        "emo_items": emo_items
    }

def render_podcast_html(meta, data, prev_meta, next_meta):
    speaker = meta['speaker']
    role = meta['role']
    tagline = meta['tagline']
    slug = meta['slug']
    title = data['title']
    category = data['category']
    ep_code = data['ep_code']
    hook = data['hook']
    overview = data['overview']
    yt_url = data['yt_url']
    delusions = data['delusions']
    insights = data['insights']
    env_items = data['env_items']
    emo_items = data['emo_items']

    # Overview lead bullets
    lead_p1 = f"<strong>• Trọng tâm nội dung:</strong> {overview}" if overview else f"<strong>• Trọng tâm nội dung:</strong> Bóc tách toàn bộ nguyên lý và đòn bẩy thực chiến từ {speaker}."
    lead_p2 = f"<strong>• Giá trị cốt lõi:</strong> {insights[0]['title'] if len(insights)>0 else title}. Đóng gói theo chuẩn cấu trúc Thụy Sĩ đơn sắc và phương pháp phân tích 3 tầng nhận thức."

    # Strategic Framework 5 Items
    framework_items = []
    target_indices = [0, 1, 2, 4, 7] if len(insights) >= 8 else range(min(5, len(insights)))
    for rank, idx in enumerate(target_indices):
        if idx < len(insights):
            ins = insights[idx]
            framework_items.append(f"""
          <div class="cb-item">
            <div class="cb-label">{rank+1}. {html.escape(ins['title'])}</div>
            <div class="cb-text">
              • <strong>Bản chất:</strong> {html.escape(ins['essence'])}<br>
              • <strong>Đòn bẩy:</strong> {html.escape(ins['leverage'])}
            </div>
          </div>""")
    framework_items_html = "\n".join(framework_items)

    # Delusion items
    delusion_1 = delusions[0] if len(delusions) > 0 else "Nỗ lực cơ bắp không đi kèm chiến lược sẽ chỉ tạo ra sự kiệt quệ."
    delusion_2 = delusions[1] if len(delusions) > 1 else "Đám đông mải miết chạy theo công cụ bề mặt mà bỏ quên nguyên lý cốt lõi."

    # Insight blocks for Section 3 (1-4)
    ins_html_p1 = []
    for ins in insights[:4]:
        ins_html_p1.append(f"""
      <div class="code-box">
        <button class="copy-btn" onclick="copySnippet(this, 'code-{ins['num'].lower().replace(' ', '-')}')">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>
          <span>Sao chép</span>
        </button>
        <div class="cb-inner" id="code-{ins['num'].lower().replace(' ', '-')}">
          <div class="cb-meta">{ins['num']} // NGUYÊN LÝ HỆ THỐNG</div>
          <div class="cb-title">{html.escape(ins['title'])}</div>

          <div class="cb-item">
            <div class="cb-label">Dữ kiện thực địa</div>
            <div class="cb-text">
              {html.escape(ins['quote'])}
            </div>
          </div>

          <div class="cb-item">
            <div class="cb-label">Bóc tách 3 tầng thấu suốt</div>
            <div class="cb-text">
              • <strong>Bề mặt:</strong> {html.escape(ins['surface'])}<br>
              • <strong>Bản chất:</strong> {html.escape(ins['essence'])}<br>
              • <strong>Đòn bẩy:</strong> {html.escape(ins['leverage'])}
            </div>
          </div>

          <div class="cb-mantra">
            "{html.escape(ins['mantra'])}"
          </div>
        </div>
      </div>""")
    ins_part1_html = "\n".join(ins_html_p1)

    # Insight blocks for Section 4 (5-8)
    ins_html_p2 = []
    for ins in insights[4:8]:
        ins_html_p2.append(f"""
      <div class="code-box">
        <button class="copy-btn" onclick="copySnippet(this, 'code-{ins['num'].lower().replace(' ', '-')}')">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>
          <span>Sao chép</span>
        </button>
        <div class="cb-inner" id="code-{ins['num'].lower().replace(' ', '-')}">
          <div class="cb-meta">{ins['num']} // NGUYÊN LÝ THỰC THI</div>
          <div class="cb-title">{html.escape(ins['title'])}</div>

          <div class="cb-item">
            <div class="cb-label">Dữ kiện thực địa</div>
            <div class="cb-text">
              {html.escape(ins['quote'])}
            </div>
          </div>

          <div class="cb-item">
            <div class="cb-label">Bóc tách 3 tầng thấu suốt</div>
            <div class="cb-text">
              • <strong>Bề mặt:</strong> {html.escape(ins['surface'])}<br>
              • <strong>Bản chất:</strong> {html.escape(ins['essence'])}<br>
              • <strong>Đòn bẩy:</strong> {html.escape(ins['leverage'])}
            </div>
          </div>

          <div class="cb-mantra">
            "{html.escape(ins['mantra'])}"
          </div>
        </div>
      </div>""")
    ins_part2_html = "\n".join(ins_html_p2)

    # Checklist items for Section 5
    action_items = []
    for it in env_items[:2]:
        action_items.append(f"""
        <div class="action-item">
          <div class="action-item__icon">✓</div>
          <div class="action-item__content">
            <strong>Thiết kế không gian:</strong> {html.escape(it)}
          </div>
        </div>""")
    for it in emo_items[:2]:
        action_items.append(f"""
        <div class="action-item">
          <div class="action-item__icon">★</div>
          <div class="action-item__content">
            <strong>Bảo toàn tâm thái:</strong> {html.escape(it)}
          </div>
        </div>""")
    action_items_html = "\n".join(action_items)

    page_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{html.escape(speaker)}: {html.escape(title)} | Chuẩn Đọc & Bố Cục FEDU</title>
  
  <!-- Font Definitions & System Fallbacks -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  {STANDARDIZED_STYLE}
</head>
<body>

  <!-- Reading Progress Bar -->
  <div class="reading-progress-bar" id="readingProgressBar"></div>

  <!-- Top Sticky Navigation -->
  <header class="top-nav">
    <div class="top-nav__inner">
      <a href="21-podcast-raj-shamani-khong-chinh-tri.html" class="top-nav__back">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        <span>Danh mục 21 Podcast</span>
      </a>
      <div class="top-nav__meta">
        <span class="nav-badge">30NGAYVIRAL // BỐ CỤC ĐỌC CHUẨN</span>
        <span style="font-size: 12.5px; color: var(--cl-text-muted);" id="readingPercent">0% ĐÃ ĐỌC</span>
      </div>
      <a href="{html.escape(yt_url)}" target="_blank" class="top-nav__btn">
        <span>Xem YouTube</span>
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/></svg>
      </a>
    </div>
  </header>

  <!-- ═══════════════════════════════════════════════════════
       KHỐI 01: HERO & BẢN ĐỒ TƯ DUY TỔNG QUAN (LIGHT)
       ═══════════════════════════════════════════════════════ -->
  <section class="read-section read-section--light" id="sec-hero">
    <div class="read-container">
      
      <!-- Nhịp 1: Micro-Badge -->
      <div class="cl-badge">{html.escape(category)} // TẬP {html.escape(ep_code)}</div>
      
      <!-- Nhịp 2: Tiêu đề đanh thép ngắt 2 dòng cân xứng -->
      <h1 class="title-hero">{html.escape(speaker.upper())}<br>{html.escape(tagline)}</h1>
      <h2 class="title-sub">{html.escape(title)}</h2>
      
      <!-- Nhịp 3: Trích dẫn thơ FD Acta -->
      <div class="editorial-hook">
        "{html.escape(hook)}"
      </div>

      <!-- Bóc tách ý dẫn nhập theo cấu trúc phân đoạn rõ ràng -->
      <div class="lead-box">
        <p>{lead_p1}</p>
        <p>{lead_p2}</p>
      </div>

      <!-- Metadata Box -->
      <div class="podcast-meta-grid">
        <div class="meta-item">
          <span class="meta-item__label">Khách mời</span>
          <span class="meta-item__val">{html.escape(speaker)}</span>
        </div>
        <div class="meta-item">
          <span class="meta-item__label">Vai trò</span>
          <span class="meta-item__val">{html.escape(role)}</span>
        </div>
        <div class="meta-item">
          <span class="meta-item__label">Thời lượng gốc</span>
          <span class="meta-item__val">1 - 2 giờ</span>
        </div>
        <div class="meta-item">
          <span class="meta-item__label">Thời lượng đọc</span>
          <span class="meta-item__val">~8 phút chắt lọc</span>
        </div>
      </div>

      <!-- Khối Code 01: Bản đồ tư duy tổng quan -->
      <div class="code-box">
        <button class="copy-btn" onclick="copySnippet(this, 'code-hero-summary')">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>
          <span>Sao chép</span>
        </button>
        <div class="cb-inner" id="code-hero-summary">
          <div class="cb-meta">BẢN ĐỒ TƯ DUY // STRATEGIC FRAMEWORK</div>
          <div class="cb-title">5 nguyên lý cốt lõi chắt lọc từ {html.escape(speaker)}</div>
          {framework_items_html}
          <div class="cb-mantra">
            "{html.escape(hook)}"
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════════
       KHỐI 02: BÓC TRẦN LẦM TƯỞNG ĐÁM ĐÔNG (TINT)
       ═══════════════════════════════════════════════════════ -->
  <section class="read-section read-section--tint" id="sec-delusion">
    <div class="read-container">
      
      <div class="cl-badge">02 / BÓC TRẦN ẢO TƯỞNG</div>
      <h2 class="title-sec">ẢO TƯỞNG ĐÁM ĐÔNG & SỰ THẬT BẢN CHẤT</h2>
      
      <p class="body-p">
        Đa số người ngoài cuộc đều tiếp cận vấn đề qua lăng kính bề mặt. Dưới đây là 2 sự thật tương phản trực diện đập tan những ngộ nhận phổ biến nhất:
      </p>

      <!-- Nhịp 3: Thẻ so sánh cân xứng -->
      <div class="compare-grid">
        <div class="compare-card">
          <span class="compare-card__badge">ẢO TƯỞNG ĐÁM ĐÔNG</span>
          <h3 class="compare-card__title">Ngộ nhận bề mặt</h3>
          <p class="compare-card__text">
            {html.escape(delusion_1)}
          </p>
        </div>

        <div class="compare-card">
          <span class="compare-card__badge">SỰ THẬT CỐT LÕI</span>
          <h3 class="compare-card__title">Bản chất hệ thống</h3>
          <p class="compare-card__text">
            {html.escape(delusion_2)}
          </p>
        </div>
      </div>

      <!-- Khối Code 02: Ma trận phân loại -->
      <div class="code-box">
        <button class="copy-btn" onclick="copySnippet(this, 'code-delusion-matrix')">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>
          <span>Sao chép</span>
        </button>
        <div class="cb-inner" id="code-delusion-matrix">
          <div class="cb-meta">MA TRẬN ĐỐI CHIẾU // MATRIX</div>
          <div class="cb-title">Phân biệt 2 tầng nhận thức trong {html.escape(category)}</div>

          <div class="cb-item">
            <div class="cb-label">Nhóm 1: Nhận thức bề mặt (Lối mòn đám đông)</div>
            <div class="cb-text">
              • <strong>Hành vi:</strong> {html.escape(delusion_1)}<br>
              • <strong>Hạn chế:</strong> Dễ rơi vào bẫy quá tải, cạn kiệt năng lượng và dẫm chân tại chỗ khi gặp biến động.
            </div>
          </div>

          <div class="cb-item">
            <div class="cb-label">Nhóm 2: Nhận thức hệ thống (Kiến trúc sư đòn bẩy)</div>
            <div class="cb-text">
              • <strong>Hành vi:</strong> {html.escape(delusion_2)}<br>
              • <strong>Kết quả:</strong> Tạo ra kết quả đột phá phi tuyến tính nhờ vào việc căn chỉnh đúng quy trình và hạ tầng gốc rễ.
            </div>
          </div>

          <div class="cb-mantra">
            "{html.escape(hook)}"
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════════
       KHỐI 03: 4 BÀI HỌC CỐT LÕI ĐẦU TIÊN (LIGHT)
       ═══════════════════════════════════════════════════════ -->
  <section class="read-section read-section--light" id="sec-insights-part1">
    <div class="read-container">
      
      <div class="cl-badge">03 / BÓC TÁCH NGUYÊN LÝ // PHẦN 1</div>
      <h2 class="title-sec">4 BÀI HỌC CỐT LÕI VỀ ĐÒN BẨY & NGUYÊN LÝ GỐC</h2>
      
      <p class="body-p">
        Mỗi bài học được tổ chức chặt chẽ: <strong>Tiêu đề FD Aeonik</strong> → <strong>Dữ kiện thực tế</strong> → <strong>Bóc tách 3 tầng nhận thức</strong> → <strong>Mantra hành động</strong>:
      </p>

      {ins_part1_html}

    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════════
       KHỐI 04: 4 BÀI HỌC ĐỘT PHÁ TIẾP THEO (TINT)
       ═══════════════════════════════════════════════════════ -->
  <section class="read-section read-section--tint" id="sec-insights-part2">
    <div class="read-container">
      
      <div class="cl-badge">04 / BÓC TÁCH NGUYÊN LÝ // PHẦN 2</div>
      <h2 class="title-sec">4 BÀI HỌC VỀ VẬN HÀNH, TÂM THÁI & DI SẢN</h2>
      
      <p class="body-p">
        Từ tư duy đòn bẩy mở rộng quy mô đến việc quản trị năng lượng sinh học và bản lĩnh đối diện với những nghịch cảnh lớn:
      </p>

      {ins_part2_html}

    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════════
       KHỐI 05: KHUNG THIẾT KẾ MÔI TRƯỜNG & TÂM THÁI (LIGHT)
       ═══════════════════════════════════════════════════════ -->
  <section class="read-section read-section--light" id="sec-execution">
    <div class="read-container">
      
      <div class="cl-badge">05 / BỐ CỤC THỰC THI // CHECKLIST</div>
      <h2 class="title-sec">THIẾT KẾ KHÔNG GIAN & BẢO TOÀN TÂM THÁI</h2>
      
      <p class="body-p">
        Mọi chiến lược vĩ đại đều vô nghĩa nếu không có một môi trường vật lý giảm thiểu ma sát và một tâm thái vững vàng để thực thi:
      </p>

      <!-- Checklist 4 nhịp hiển thị trực diện -->
      <div class="action-list">
        {action_items_html}
      </div>

      <!-- Khối Code: Checklist vận hành hàng ngày -->
      <div class="code-box">
        <button class="copy-btn" onclick="copySnippet(this, 'code-checklist-action')">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>
          <span>Sao chép</span>
        </button>
        <div class="cb-inner" id="code-checklist-action">
          <div class="cb-meta">CHECKLIST THỰC CHIẾN // ROUTINE</div>
          <div class="cb-title">Quy trình thực thi hàng ngày cho người hành động</div>

          <div class="cb-item">
            <div class="cb-label">Buổi sáng — Thiết lập đòn bẩy</div>
            <div class="cb-text">
              • <strong>Dọn sạch ma sát:</strong> {html.escape(env_items[0] if len(env_items)>0 else "Chuẩn bị không gian làm việc tĩnh lặng, không màn hình gây xao nhãng.")}<br>
              • <strong>Ưu tiên cao nhất:</strong> Tập trung giải quyết 1 quyết định đinh mang lại 80% kết quả ngày hôm nay.
            </div>
          </div>

          <div class="cb-item">
            <div class="cb-label">Trong ngày — Vận hành &amp; bảo toàn năng lượng</div>
            <div class="cb-text">
              • <strong>Bảo vệ nhịp tim &amp; cảm xúc:</strong> {html.escape(emo_items[0] if len(emo_items)>0 else "Không phản hồi nóng vội khi cảm xúc đang dao động mạnh.")}<br>
              • <strong>Tuân thủ quy trình:</strong> Luôn bám sát hệ thống thay vì phó mặc cho cảm hứng nhất thời.
            </div>
          </div>

          <div class="cb-item">
            <div class="cb-label">Buổi chiều — Rà soát &amp; đóng gói</div>
            <div class="cb-text">
              • <strong>Trích xuất dữ liệu:</strong> {html.escape(emo_items[1] if len(emo_items)>1 else "Xem mọi sai sót là bài học kinh nghiệm để liên tục cải tiến hệ thống.")}
            </div>
          </div>

          <div class="cb-mantra">
            "{html.escape(hook)}"
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════════
       KHỐI 06: ĐIỀU HƯỚNG & KẾT NỐI (TINT)
       ═══════════════════════════════════════════════════════ -->
  <section class="read-section read-section--tint" id="sec-footer">
    <div class="read-container">
      
      <div class="cl-badge">06 / ĐIỀU HƯỚNG HỆ THỐNG</div>
      <h2 class="title-sec">TIẾP TỤC HÀNH TRÌNH TRI THỨC</h2>
      
      <p class="body-p">
        Bài phân tích này thuộc chuỗi 21 podcast tinh hoa của Raj Shamani (đã lọc sạch hoàn toàn yếu tố chính trị/chiến tranh), được tái cấu trúc thị giác theo chuẩn hệ thống thiết kế 30ngayviral.fedu.vn.
      </p>

      <div class="cta-row">
        <a href="{html.escape(yt_url)}" target="_blank" class="cl-btn">
          <span>Xem Podcast Gốc Trên YouTube ↗</span>
        </a>
        <a href="21-podcast-raj-shamani-khong-chinh-tri.html" class="cl-btn cl-btn--secondary">
          <span>← Quay Về Danh Mục 21 Podcast</span>
        </a>
        <a href="{html.escape(next_meta['slug'])}" class="cl-btn cl-btn--secondary">
          <span>Tập Kế Tiếp: {html.escape(next_meta['speaker'])} →</span>
        </a>
      </div>

      <div style="margin-top: 48px; padding-top: 24px; border-top: 1px solid var(--cl-line); font-size: 13.5px; color: var(--cl-text-muted); display: flex; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
        <span>Phát triển bởi FEDU System • Chuẩn đọc &amp; bố cục 30ngayviral</span>
        <span>Cập nhật mới nhất: 2026</span>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════════
       SCRIPTS: SCROLL PROGRESS & 1-CLICK COPY
       ═══════════════════════════════════════════════════════ -->
  {STANDARDIZED_SCRIPT}
</body>
</html>
"""
    return page_html

def main():
    print("🚀 Bắt đầu quá trình chuẩn hóa 20 bài podcast sang chuẩn Swiss Minimalist Reading Flow...")
    n = len(ORDERED_PODCASTS)
    success_count = 0

    for i in range(1, n):
        meta = ORDERED_PODCASTS[i]
        prev_meta = ORDERED_PODCASTS[(i - 1) % n]
        next_meta = ORDERED_PODCASTS[(i + 1) % n]

        src_path = os.path.join(COURSE_DIR, meta['slug'])
        if not os.path.exists(src_path):
            print(f"❌ Không tìm thấy: {src_path}")
            continue

        data = parse_podcast_data(src_path)
        rendered_html = render_podcast_html(meta, data, prev_meta, next_meta)

        with open(src_path, 'w', encoding='utf-8') as f:
            f.write(rendered_html)

        fsize = os.path.getsize(src_path) / 1024
        print(f"[{i:02d}/20] ✅ Đã chuẩn hóa: {meta['slug']} ({fsize:.1f} KB)")
        success_count += 1

    print(f"\n🎉 HOÀN TẤT: Đã nâng cấp thành công {success_count}/20 bài podcast sang chuẩn Swiss Monochrome Reading Flow!")

if __name__ == '__main__':
    main()
