import re

html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vaibhav Sisinty: Cách AI Nhân Bản Thu Nhập Lên Tiền Tỷ</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    @font-face { font-family: 'FD Aeonik Extended'; src: url('./fonts/FDAeonikExtended-Regular.woff2?v=2') format('woff2'); font-weight: 400; font-style: normal; font-display: swap; }
    @font-face { font-family: 'FD Aeonik Extended'; src: url('./fonts/FDAeonikExtended-Bold.woff2?v=2') format('woff2'); font-weight: 700; font-style: normal; font-display: swap; }
    @font-face { font-family: 'FD Aeonik'; src: url('./fonts/FDAeonikRegular.ttf') format('truetype'); font-weight: 400; font-style: normal; font-display: swap; }
    @font-face { font-family: 'FD Aeonik'; src: url('./fonts/FDAeonikMedium.ttf') format('truetype'); font-weight: 500; font-style: normal; font-display: swap; }
    @font-face { font-family: 'FD Aeonik'; src: url('./fonts/FDAeonikSemiBold.ttf') format('truetype'); font-weight: 600; font-style: normal; font-display: swap; }
    @font-face { font-family: 'FD Aeonik'; src: url('./fonts/FDAeonikBold.ttf') format('truetype'); font-weight: 700; font-style: normal; font-display: swap; }
    @font-face { font-family: 'Tiempos Text Web'; src: url('./fonts/FDTiemposText-Regular.woff2?v=2') format('woff2'); font-weight: 400; font-style: normal; font-display: swap; }
    @font-face { font-family: 'Tiempos Text Web'; src: url('./fonts/FDTiemposText-Bold.woff2?v=2') format('woff2'); font-weight: 700; font-style: normal; font-display: swap; }
    @font-face { font-family: 'Tiempos Text Web'; src: url('./fonts/FDTiemposText-Semibold.woff2?v=2') format('woff2'); font-weight: 600; font-style: normal; font-display: swap; }
    @font-face { font-family: 'Tiempos Text Web'; src: url('./fonts/FDTiemposText-RegularItalic.woff2?v=2') format('woff2'); font-weight: 400; font-style: italic; font-display: swap; }

    :root {
      --cl-bg: #ffffff;
      --cl-tint: #f8fafc;
      --cl-card: #ffffff;
      --cl-accent: #1a73e8;
      --cl-line: rgba(0, 0, 0, 0.06);
      --cl-line-strong: rgba(0, 0, 0, 0.12);
      --cl-border-code: #e2e8f0;
      --cl-text-base: #090d16;
      --cl-text-body: #0f172a;
      --cl-text-muted: #475569;
      --cl-radius-md: 12px;
      --cl-radius-sm: 8px;
      --cl-radius-full: 9999px;
      --font-display-short: 'FD Aeonik Extended', 'FD Aeonik', -apple-system, sans-serif;
      --font-display-long: 'FD Aeonik', -apple-system, sans-serif;
      --font-body: 'FD Aeonik', 'Inter', -apple-system, sans-serif;
      --font-reading: 'Tiempos Text Web', Georgia, serif;
      --font-acta: 'Tiempos Text Web', Georgia, serif;
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }
    html { background-color: var(--cl-bg); color: var(--cl-text-base); font-family: var(--font-body); }
    body { line-height: 1.8; font-size: 16.5px; color: var(--cl-text-body); }
    
    .reading-progress-bar { position: fixed; top: 0; left: 0; height: 3px; width: 0%; background: linear-gradient(90deg, #1a73e8, #38bdf8); z-index: 1000; }
    .top-nav { position: sticky; top: 0; width: 100%; background: rgba(255, 255, 255, 0.96); backdrop-filter: blur(12px); border-bottom: 1px solid var(--cl-line); z-index: 999; padding: 12px 20px; }
    .top-nav__inner { max-width: 800px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; gap: 16px; }
    .top-nav__back { display: inline-flex; align-items: center; gap: 8px; color: var(--cl-text-muted); text-decoration: none; font-size: 14px; font-weight: 500; }
    .top-nav__meta { display: flex; align-items: center; gap: 12px; }
    .top-nav__btn { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600; color: #ffffff; background: var(--cl-text-base); padding: 6px 14px; border-radius: var(--cl-radius-sm); text-decoration: none; }
    
    .read-section { width: 100%; padding: 72px 24px; position: relative; }
    .read-section--light { background-color: var(--cl-bg); }
    .read-section--tint { background-color: var(--cl-tint); border-top: 1px solid var(--cl-line); border-bottom: 1px solid var(--cl-line); }
    .read-container { width: 100%; max-width: 760px; margin: 0 auto; position: relative; }
    
    .cl-badge { display: inline-flex; align-items: center; gap: 8px; font-family: 'FD Aeonik', sans-serif; font-size: 11px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: var(--cl-text-muted); background: #f1f5f9; border: 1px solid var(--cl-border-code); padding: 5px 14px; border-radius: var(--cl-radius-full); margin-bottom: 18px; }
    .title-hero { font-family: var(--font-display-short); font-weight: 700; font-size: clamp(28px, 4vw, 38px); line-height: 1.25; text-transform: uppercase; margin-bottom: 12px; }
    .title-sub { font-family: var(--font-display-long); font-weight: 600; font-size: clamp(20px, 2.8vw, 25px); line-height: 1.38; margin-bottom: 18px; }
    .editorial-hook { font-family: var(--font-acta); font-style: italic; font-weight: 500; font-size: clamp(19px, 2.3vw, 23px); line-height: 1.55; margin: 18px 0 24px; padding-left: 18px; border-left: 3px solid var(--cl-text-base); }
    
    .lead-box { background: var(--cl-card); border: 1px solid var(--cl-line); border-radius: var(--cl-radius-md); padding: 22px 24px; margin-bottom: 28px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02); }
    .lead-box p { font-size: 16px; line-height: 1.8; margin-bottom: 12px; }
    .lead-box p:last-child { margin-bottom: 0; }
    
    .podcast-meta-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 18px 0 28px; padding: 14px 18px; background: var(--cl-tint); border: 1px solid var(--cl-line); border-radius: var(--cl-radius-md); }
    .meta-item { display: flex; flex-direction: column; gap: 2px; }
    .meta-item__label { font-family: 'FD Aeonik', sans-serif; font-size: 10px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: var(--cl-text-muted); }
    .meta-item__val { font-size: 13.5px; font-weight: 600; }
    
    .code-box { position: relative; background: #ffffff; border: 1px solid var(--cl-border-code); border-radius: 12px; margin: 28px 0 36px; padding: 24px 28px 22px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02); }
    .copy-btn { position: absolute; top: 14px; right: 14px; display: inline-flex; align-items: center; gap: 6px; background: #ffffff; color: var(--cl-text-muted); border: 1px solid var(--cl-border-code); border-radius: 6px; padding: 5px 11px; font-family: 'FD Aeonik', sans-serif; font-size: 11.5px; font-weight: 600; cursor: pointer; }
    .copy-btn:hover { background: var(--cl-tint); color: var(--cl-text-base); }
    
    .cb-meta { font-family: 'FD Aeonik', sans-serif; font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--cl-text-muted); margin-bottom: 4px; }
    .cb-title { font-family: 'FD Aeonik', sans-serif; font-size: 18px; font-weight: 700; margin-bottom: 18px; }
    .cb-item { margin-bottom: 16px; }
    .cb-label { font-family: 'FD Aeonik', sans-serif; font-size: 13.5px; font-weight: 600; margin-bottom: 4px; display: block; }
    .cb-text { font-family: var(--font-reading); font-size: 16.5px; line-height: 1.82; }
    .cb-mantra { margin-top: 18px; padding-top: 14px; border-top: 1px solid var(--cl-line); font-family: var(--font-reading); font-style: italic; font-size: 16.5px; font-weight: 500; }
  </style>
</head>
<body>
  <div class="reading-progress-bar" id="readingProgressBar"></div>
  <header class="top-nav">
    <div class="top-nav__inner">
      <a href="#" class="top-nav__back">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        <span>Back</span>
      </a>
      <div class="top-nav__meta">
        <span style="font-size: 11.5px; color: var(--cl-text-muted); font-family: var(--font-mono); margin-right: 12px;">📅 26/05/2026</span>
        <span style="font-size: 12.5px; color: var(--cl-text-muted);" id="readingPercent">0%</span>
      </div>
      <a href="https://www.youtube.com/watch?v=kKNoBH0iE1k" target="_blank" class="top-nav__btn">
        <span>Xem YouTube</span>
      </a>
    </div>
  </header>

  <section class="read-section read-section--light">
    <div class="read-container">
      <div class="cl-badge">TƯ DUY NHÂN BẢN THU NHẬP</div>
      <h1 class="title-hero">VAIBHAV SISINTY<br>NHÂN BẢN THU NHẬP BẰNG AI</h1>
      <h2 class="title-sub">How To Grow Your Salary To ₹1 Crore Using AI</h2>
      
      <div class="editorial-hook">
        "Cắm đầu cày cuốc ngày đêm<br>Ngờ đâu AI gánh êm đềm nhàn tênh."
      </div>

      <div class="lead-box">
        <p><strong>• Cái bẫy của lao động tay chân:</strong> Đa số nhân viên văn phòng nghĩ rằng làm việc chăm chỉ, cày thêm giờ sẽ giúp tăng thu nhập. Họ lầm tưởng thời gian bỏ ra tương đương với giá trị tạo ra.</p>
        <p><strong>• Sự thật trần trụi:</strong> Thu nhập tỷ lệ thuận với khả năng giải quyết vấn đề bằng đòn bẩy. Nếu không biết dùng AI để tự động hóa, bạn đang bán thời gian với giá bèo.</p>
      </div>

      <div class="podcast-meta-grid">
        <div class="meta-item"><span class="meta-item__label">Khách mời</span><span class="meta-item__val">Vaibhav Sisinty</span></div>
        <div class="meta-item"><span class="meta-item__label">Kênh</span><span class="meta-item__val">Raj Shamani</span></div>
        <div class="meta-item"><span class="meta-item__label">Phát hành</span><span class="meta-item__val">26/05/2026</span></div>
        <div class="meta-item"><span class="meta-item__label">Thời lượng</span><span class="meta-item__val">2:31:55</span></div>
        <div class="meta-item"><span class="meta-item__label">Đọc</span><span class="meta-item__val">15 phút</span></div>
      </div>
"""

insights = [
    {
        "title": "Bằng Cấp Vô Nghĩa, Năng Lực Giải Quyết Vấn Đề Lên Ngôi",
        "fact": "Thị trường trả tiền cho kết quả cuối cùng, không phải cho quá trình học tập hay bằng cấp truyền thống.",
        "surface": "Hàng nghìn người thất nghiệp dù có bằng cấp cao, trong khi công ty khát nhân sự biết dùng AI.",
        "core": "AI san bằng lợi thế kiến thức cơ bản. Điều tạo ra sự khác biệt là khả năng kết hợp công cụ để ra thành phẩm.",
        "action": "Ngừng theo đuổi chứng chỉ vô nghĩa. Dành 100 giờ làm chủ 3 công cụ AI cốt lõi và show kết quả thực tế.",
        "poem": "Bằng cấp như giấy vẽ bùa<br>Làm được việc thật mới lùa được vàng."
    },
    {
        "title": "Đừng Làm Việc Chăm Chỉ, Hãy Làm Việc Bằng Hệ Thống",
        "fact": "Một người dùng AI có thể hoàn thành khối lượng công việc của 5 người trong cùng một thời gian.",
        "surface": "Nhiều người tự hào vì làm việc 14 tiếng/ngày nhưng thu nhập không tăng.",
        "core": "Sức lực con người có giới hạn. AI là đòn bẩy vô hạn giúp nhân bản thời gian và công sức.",
        "action": "Tự động hóa 80% công việc lặp đi lặp lại bằng AI. Dùng 20% thời gian còn lại để tư duy chiến lược.",
        "poem": "Cày cuốc bạc tóc mòn hơi<br>Biết dùng máy móc ngồi chơi xơi tiền."
    },
    {
        "title": "Xây Dựng Thương Hiệu Cá Nhân Bằng AI Content",
        "fact": "Content là tài sản số. AI giúp tạo ra content nhanh gấp 10 lần với chất lượng ổn định.",
        "surface": "Rất nhiều người ngại làm nội dung vì tốn thời gian viết kịch bản và chỉnh sửa.",
        "core": "AI phá vỡ rào cản sáng tạo. Bạn chỉ cần đưa ra góc nhìn, AI sẽ lo phần diễn đạt và đóng gói.",
        "action": "Sử dụng ChatGPT để lập dàn ý và viết bài. Dùng AI tạo hình ảnh/video để duy trì tần suất đăng bài mỗi ngày.",
        "poem": "Viết lách vốn chuyện đau đầu<br>Có AI gánh vác làm giàu mấy hồi."
    },
    {
        "title": "Mở Rộng Nguồn Thu Bằng AI Freelancing",
        "fact": "Khách hàng mua giải pháp, không quan tâm bạn làm bằng tay hay bằng AI.",
        "surface": "Freelancer truyền thống kiệt sức vì nhận quá nhiều job, không có thời gian nghỉ.",
        "core": "AI giúp rút ngắn thời gian hoàn thành dự án từ vài ngày xuống vài giờ, biên độ lợi nhuận cực cao.",
        "action": "Cung cấp các dịch vụ như viết copy, thiết kế logo, lập trình web cơ bản bằng các công cụ AI mạnh nhất.",
        "poem": "Bán chất xám, bán thời gian<br>Dùng AI giúp muôn vàn thảnh thơi."
    },
    {
        "title": "Prompt Là Ngôn Ngữ Lập Trình Của Tương Lai",
        "fact": "Người biết cách giao tiếp với AI sẽ thay thế người chỉ biết code truyền thống.",
        "surface": "Nhiều người chê AI dở vì họ chỉ biết gõ những câu lệnh chung chung.",
        "core": "Chất lượng đầu ra của AI phụ thuộc 100% vào ngữ cảnh và sự chính xác của prompt.",
        "action": "Học cách viết prompt theo cấu trúc: Vai trò - Nhiệm vụ - Ngữ cảnh - Ràng buộc - Định dạng đầu ra.",
        "poem": "Hỏi ngốc thì máy cũng ngây<br>Lệnh chuẩn máy đáp như thầy với tao."
    },
    {
        "title": "Tư Duy Hệ Thống Vượt Trội Tư Duy Công Cụ",
        "fact": "Công cụ AI thay đổi mỗi ngày, nhưng tư duy ghép nối hệ thống thì trường tồn.",
        "surface": "Đám đông chạy theo từng tool mới ra mắt rồi nhanh chóng chán nản.",
        "core": "Kẻ mạnh không phải là người biết nhiều tool, mà là người biết liên kết các tool thành cỗ máy in tiền.",
        "action": "Vẽ ra workflow xử lý công việc. Tìm các AI phù hợp để nhúng vào từng bước thay vì dùng một AI cho mọi thứ.",
        "poem": "Chạy theo công cụ mệt nhoài<br>Xây xong hệ thống hái tài trăm năm."
    },
    {
        "title": "Đàm Phán Lương Bằng Dữ Liệu AI",
        "fact": "Công ty trả lương dựa trên giá trị thặng dư bạn mang lại.",
        "surface": "Nhân sự xin tăng lương bằng cách kể lể sự vất vả, thâm niên.",
        "core": "Sếp chỉ nhìn vào con số. Nếu bạn chứng minh được AI giúp bạn tiết kiệm chi phí cho công ty, bạn có quyền đòi chia phần.",
        "action": "Dùng AI thống kê hiệu suất công việc. Trình bày rõ ràng: 'Tôi đã dùng hệ thống X để tiết kiệm Y giờ/tháng, tạo ra Z doanh thu'.",
        "poem": "Than nghèo kể khổ ai thương<br>Chìa ra con số sếp nhường phần ngon."
    },
    {
        "title": "Tái Đầu Tư Thời Gian Rảnh",
        "fact": "AI giải phóng thời gian, nhưng cách bạn dùng thời gian đó quyết định tài sản.",
        "surface": "Nhiều người dùng thời gian rảnh do AI tạo ra để lướt mạng xã hội.",
        "core": "Thời gian được chuộc lại bằng AI là nguồn vốn quý nhất để học hỏi và mở rộng networking.",
        "action": "Khi AI làm thay 4 tiếng mỗi ngày, hãy dùng 4 tiếng đó để nâng cấp bản thân hoặc xây dựng business riêng.",
        "poem": "Rảnh rang chớ có chơi bời<br>Đầu tư trí tuệ đổi đời mai sau."
    }
]

for i, insight in enumerate(insights):
    html_content += f"""
      <div class="code-box">
        <button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.innerText)">Copy</button>
        <div class="cb-inner">
          <div class="cb-meta">INSIGHT {i+1:02d}</div>
          <div class="cb-title">{insight['title']}</div>
          <div class="cb-item"><span class="cb-label">🎙️ Dữ kiện gốc:</span><div class="cb-text">{insight['fact']}</div></div>
          <div class="cb-item"><span class="cb-label">👁️ Hiện tượng bề mặt:</span><div class="cb-text">{insight['surface']}</div></div>
          <div class="cb-item"><span class="cb-label">🔬 Giải mã bản chất:</span><div class="cb-text">{insight['core']}</div></div>
          <div class="cb-item"><span class="cb-label">⚙️ Đòn bẩy thực chiến:</span><div class="cb-text">{insight['action']}</div></div>
          <div class="cb-mantra">"{insight['poem']}"</div>
        </div>
      </div>
"""

html_content += """
    </div>
  </section>
  <script>
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('readingProgressBar').style.width = scrolled + '%';
      document.getElementById('readingPercent').textContent = Math.round(scrolled) + '% ĐÃ ĐỌC';
    });
  </script>
</body>
</html>
"""

with open('/Users/vietmac/Documents/CODE/k/vaibhav-sisinty-ai-salary-podcast.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Done")
