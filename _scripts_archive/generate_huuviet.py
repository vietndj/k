import re

with open('logickenh-tattoo.html', 'r') as f:
    tattoo_html = f.read()

# We will extract the CSS and header/footer from tattoo
head_match = re.search(r'(<head>.*?</head>)', tattoo_html, re.DOTALL)
head = head_match.group(1) if head_match else ""

# Replace title in head
head = head.replace("CASE ĐÀO TRUNG NGHĨA TATTOO: TỪ LỚP HỌC VẼ MÁY ĐẾN BẢO VỆ LÀN DA KHÁCH HÀNG THẬT", "CASE HỮU VIỆT: TỪ KHỔ CHỦ SALON ĐẾN TỔNG TƯ LỆNH QUẢN TRỊ HỆ THỐNG")

footer_match = re.search(r'(<footer.*</footer>)', tattoo_html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

body_content = """
<body>
  <!-- Top Nav -->
  <div class="top-nav">
    <div class="top-nav__breadcrumbs">
      <a href="index.html">Trang chủ</a>
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>
      <span>Case Study</span>
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>
      <span style="color: var(--cl-text-base); font-weight: 600;">Hữu Việt Salon</span>
    </div>
  </div>

  <!-- MÀN 1 -->
  <section class="cl-zebra-section cl-zebra--light">
    <div class="cl-sec-container">
      <div class="cl-badge cl-badge--blue">01 / TỔNG KHO TRÍ TUỆ • NGUYỄN ĐỨC VIỆT</div>
      <h1 class="title-short">CASE HỮU VIỆT: GIẢI PHÓNG "KHỔ CHỦ" BẰNG ĐÒN BẨY QUẢN TRỊ & APP AI</h1>
      <p class="cl-body">
        Nghịch lý của thợ tóc giỏi: Càng đông khách càng không có thời gian ăn tối cùng gia đình. Khách chỉ nằng nặc đòi đích thân ông chủ cắt. Từ bỏ ghế cắt để đứng lên quản trị là bước ngoặt đẫm máu.
      </p>
      
      <div class="luc-bat-card">
        <div class="luc-bat-tag">TRÍ TUỆ LỤC BÁT</div>
        <div class="luc-bat-poem">
          <p>Múa kéo điệu nghệ làm gì<br>Khách đông chật tiệm, tối mịt mới ăn<br>Bước ra khỏi ghế khó khăn<br>Đứng lên quản trị, trăm năm vững bền.</p>
        </div>
        <p class="luc-bat-sub"><b>Ý nghĩa:</b> Kỹ năng chốt sale cao nhất không phải là khoe tay nghề cắt tóc, mà là chứng minh năng lực <b>xây dựng quy trình (SOP)</b> để tiệm tự vận hành kể cả khi không có mặt ông chủ.</p>
      </div>
    </div>
  </section>

  <!-- MÀN 2 -->
  <section class="cl-zebra-section cl-zebra--tint">
    <div class="cl-sec-container">
      <div class="cl-badge">02 / AUDIT VĂN PHONG THỰC CHIẾN</div>
      <h2 class="title-short">LỌC BỎ TỪ NGỮ B2C TỰ LUYẾN & CHUẨN HÓA B2B THỰC CHIẾN</h2>
      <p class="cl-body">Tuyệt đối không dùng những từ ngữ thợ tóc hoa mỹ. Hãy dùng ngôn từ của người làm kinh doanh.</p>
      
      <div class="audit-table-wrap">
        <div class="script-columns">
          <div class="script-col col-wrong">
            <div class="script-col__tag">❌ B2C TỰ LUYẾN (BỎ NGAY)</div>
            <p>• "Mái tóc bồng bềnh, uốn lơi quyến rũ..."<br>
               • "Tâm huyết múa kéo 12 năm của em..."<br>
               • "Phục hồi collagen siêu mượt..."</p>
          </div>
          <div class="script-col col-right">
            <div class="script-col__tag">✅ B2B THỰC CHIẾN (DÙNG NGAY)</div>
            <p>• "Tối ưu chi phí cốt, chống hao hụt thuốc nhuộm..."<br>
               • "Quy chuẩn SOP vận hành tự động..."<br>
               • "Giải phóng khổ chủ salon..."</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- MÀN 3 -->
  <section class="cl-zebra-section cl-zebra--light">
    <div class="cl-sec-container">
      <div class="cl-badge">03 / GIẢI PHẪU HIỆN TRƯỜNG</div>
      <h2 class="title-short">TỶ LỆ 70/30 & PHONG CÁCH "PHÓNG VIÊN ĐIỀU TRA"</h2>
      <p class="cl-body">Chất liệu của Hữu Việt khổng lồ như Tuấn Tự Do (F&B). Áp dụng ngay format:</p>
      
      <div class="apple-card">
        <h3 class="apple-card__title">70% B-Roll Hiện Trường Làm Việc</h3>
        <p class="cl-body">Quay 100% bằng tay, không gimbal, dùng mic cài áo thu rõ giọng. Xộc vào salon kiểm tra đột xuất: mắng thợ pha dư thuốc nhuộm, lật thùng rác kiểm tra vỏ hộp, bắt quả tang thợ bỏ bước sấy phục hồi.</p>
      </div>
      <div class="apple-card" style="margin-top: 16px;">
        <h3 class="apple-card__title">30% Walk & Talk Chuyên Môn</h3>
        <p class="cl-body">Vừa đi dọc hành lang salon vừa bóc tách điểm mù của các chủ tiệm khác. Áp dụng định luật Woodsmall về 15% hao hụt nguyên liệu để đánh vào túi tiền người nghe.</p>
      </div>
    </div>
  </section>

  <!-- MÀN 4 -->
  <section class="cl-zebra-section cl-zebra--tint">
    <div class="cl-sec-container">
      <div class="cl-badge">04 / BƯỚC CHUYỂN TOÀN DIỆN</div>
      <h2 class="title-short">LỘ TRÌNH 3 GIAI ĐOẠN ĐỘT PHÁ</h2>
      
      <div class="apple-card">
        <div class="apple-card__badge" style="color: #0369a1; background: #e0f2fe;">GIAI ĐOẠN 1: TÍCH LŨY 7 GIỜ NIỀM TIN</div>
        <p class="cl-body">Tập trung đẩy mạnh B-Roll không thoại. Quay cảnh nhập kho mỹ phẩm sỉ, cảnh màn hình App AI tự động tính lương thợ, cảnh sửa quy trình. Để khách hàng ngầm hiểu quy mô hệ thống.</p>
      </div>
      <div class="apple-card" style="margin-top: 16px;">
        <div class="apple-card__badge" style="color: #0f766e; background: #ccfbf1;">GIAI ĐOẠN 2: LỘ MẶT CHỈ ĐIỂM</div>
        <p class="cl-body">Sử dụng kịch bản 1 dòng hook đanh thép: <i>"Hôm nay tôi ghé 1 salon đang kêu lỗ, xem bếp nhà anh ta bốc mùi ở chỗ nào..."</i></p>
      </div>
    </div>
  </section>

  <!-- MÀN 5 -->
  <section class="cl-zebra-section cl-zebra--light">
    <div class="cl-sec-container">
      <div class="cl-badge">05 / KỊCH BẢN THỰC ĐỊA</div>
      <h2 class="title-short">KỊCH BẢN WALK & TALK BẮT QUẢ TANG</h2>
      
      <div class="script-columns">
        <div class="script-col script-col--visual">
          <div class="script-col__tag">HÌNH ẢNH (B-ROLL)</div>
          <p>Hữu Việt xộc vào phòng kho pha thuốc của tiệm. Cầm bát thuốc nhuộm còn dư 1/3 lên, chỉ thẳng vào ống kính.</p>
          <p>Mở màn hình App AI trên điện thoại, trỏ vào bảng tính định lượng gram.</p>
        </div>
        <div class="script-col script-col--audio">
          <div class="script-col__tag">ÂM THANH (VOICE/THOẠI)</div>
          <p><b>[Thoại]:</b> "Anh em chủ tiệm lúc nào cũng kêu doanh thu cao mà đút túi chẳng được bao nhiêu. Nhìn cái bát thuốc này đi. Mỗi đầu khách thợ pha dư 30 gram. Một ngày 20 khách là bay mẹ nó nửa tuýp thuốc xịn chui xuống cống."</p>
          <p><b>[Thoại]:</b> "SOP không có, định lượng không đo bằng app, thì cắt tóc giỏi đến mấy cuối tháng cũng ăn cám."</p>
        </div>
      </div>
    </div>
  </section>

  <!-- MÀN 6-8 -->
  <section class="cl-zebra-section cl-zebra--tint">
    <div class="cl-sec-container">
      <div class="cl-badge">06-08 / TƯ DUY HỆ THỐNG</div>
      <h2 class="title-short">COSTLY SIGNALING: HÀNH ĐỘNG CHỊU THIỆT VÌ HỆ THỐNG</h2>
      
      <div class="apple-card" style="border-left: 4px solid var(--cl-accent);">
        <div class="apple-card__title" style="color: var(--cl-accent);">Tín Hiệu Đắt Giá (Costly Signaling)</div>
        <p class="cl-body">
          • <b>Từ chối bán App:</b> Hữu Việt tuyên bố không bán App quản lý cho những salon rác rưởi, không chịu tuân thủ kỷ luật nhập liệu. <i>"Anh mua app của em về mà thợ không xài thì cũng vứt. Em không lấy tiền của anh để mang tiếng."</i><br><br>
          • <b>Cắt cầu sỉ phá giá:</b> Sẵn sàng hủy hợp tác với đại lý mỹ phẩm sỉ phá giá thị trường để bảo vệ uy tín chung của chuỗi. Hành động đập vỡ lợi ích ngắn hạn này khiến não bộ đối tác tiết ra dopamine của sự an toàn tuyệt đối.
        </p>
      </div>
    </div>
  </section>

  {footer}
</body>
</html>
"""

full_html = f"<!DOCTYPE html>\n<html lang=\"vi\">\n{head}\n{body_content}"
with open('logickenh-huuviet.html', 'w') as f:
    f.write(full_html)
