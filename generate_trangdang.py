import re

with open('logickenh-tattoo.html', 'r') as f:
    tattoo_html = f.read()

head_match = re.search(r'(<head>.*?</head>)', tattoo_html, re.DOTALL)
head = head_match.group(1) if head_match else ""
head = head.replace("CASE ĐÀO TRUNG NGHĨA TATTOO: TỪ LỚP HỌC VẼ MÁY ĐẾN BẢO VỆ LÀN DA KHÁCH HÀNG THẬT", "CASE TRANG ĐẶNG: TỪ NGƯỢNG NGÙNG TRƯỚC ỐNG KÍNH ĐẾN CHỐT SALE IM LẶNG")

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
      <span style="color: var(--cl-text-base); font-weight: 600;">Trang Đặng Hair Salon</span>
    </div>
  </div>

  <!-- MÀN 1 -->
  <section class="cl-zebra-section cl-zebra--light">
    <div class="cl-sec-container">
      <div class="cl-badge cl-badge--blue">01 / TỔNG KHO TRÍ TUỆ • NGUYỄN ĐỨC VIỆT</div>
      <h1 class="title-short">CASE TRANG ĐẶNG: BIẾN SỰ NGƯỢNG NGÙNG THÀNH VŨ KHÍ TẠO NIỀM TIN</h1>
      <p class="cl-body">
        Rất giỏi nghề nhưng lại sợ ống kính. Luôn ngượng ngùng khi phải quay video nói chuyện. Nhưng khách hàng không cần một diễn viên lưu loát, họ cần một người thợ chân thật để giao phó mái tóc của mình.
      </p>
      
      <div class="luc-bat-card">
        <div class="luc-bat-tag">TRÍ TUỆ LỤC BÁT</div>
        <div class="luc-bat-poem">
          <p>Cầm kéo muôn vạn ngày đêm<br>Lên hình một phút yếu mềm chân tay<br>Ngượng ngùng ấp úng chẳng hay<br>Nhưng đầy sự thật, khách say chốt liền.</p>
        </div>
        <p class="luc-bat-sub"><b>Ý nghĩa:</b> Sự hoàn hảo giả tạo sinh ra phòng thủ. Chính sự ngượng ngùng, chân chất khi giao tiếp mới là điểm chạm cảm xúc mạnh nhất phá vỡ lớp khiên của tệp khách hàng "Tàu ngầm" (Lurker).</p>
      </div>
    </div>
  </section>

  <!-- MÀN 2 -->
  <section class="cl-zebra-section cl-zebra--tint">
    <div class="cl-sec-container">
      <div class="cl-badge">02 / AUDIT VĂN PHONG THỰC CHIẾN</div>
      <h2 class="title-short">LỌC BỎ LỜI CHÀO MỜI SÁO RỖNG & TẬP TRUNG VÀO SỰ THẬT ĐÃ CHUẨN BỊ TRƯỚC</h2>
      <p class="cl-body">Đừng ép bản thân phải nói "Kính chào quý khách". Hãy cứ mộc mạc như lúc đang tư vấn tại ghế.</p>
      
      <div class="audit-table-wrap">
        <div class="script-columns">
          <div class="script-col col-wrong">
            <div class="script-col__tag">❌ QUẢNG CÁO SÁO RỖNG</div>
            <p>• "Xin chào mọi người, đến với Trang Salon bạn sẽ có mái tóc tuyệt vời..."<br>
               • "Bên em đang có khuyến mãi sốc giảm 50% uốn nhuộm..."<br>
               • "Mái tóc này quá xuất sắc luôn ạ!"</p>
          </div>
          <div class="script-col col-right">
            <div class="script-col__tag">✅ TỰ SỰ MỘC MẠC (ĐỜI THỰC)</div>
            <p>• "Ca này tóc chị khách nát bét rồi, em không dám uốn luôn..."<br>
               • "Hôm nay tiệm đông quá, em vừa cắt vừa thở đây mọi người..."<br>
               • "Tóc yếu thế này thì cứ dưỡng trước đi đã, tháng sau hãy uốn."</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- MÀN 3 -->
  <section class="cl-zebra-section cl-zebra--light">
    <div class="cl-sec-container">
      <div class="cl-badge">03 / GIẢI PHẪU HIỆN TRƯỜNG</div>
      <h2 class="title-short">TÍCH LŨY 7 GIỜ BẰNG QUY TẮC 70/30 CHO NGƯỜI ÍT NÓI</h2>
      <p class="cl-body">Làm thế nào để xây kênh khi bạn không thể nói quá 3 câu trên video?</p>
      
      <div class="apple-card">
        <h3 class="apple-card__title">70% B-Roll Không Lời (Đời Sống Tiệm)</h3>
        <p class="cl-body">Quay cảnh mở cửa, quét dọn, pha thuốc, tiếng máy sấy, tiếng kéo lách cách. Hoàn toàn không cần thoại, chỉ lồng nhạc Lofi nhẹ nhàng. Mục đích: Để khách quen thuộc với không gian và khuôn mặt của Trang.</p>
      </div>
      <div class="apple-card" style="margin-top: 16px;">
        <h3 class="apple-card__title">30% Walk & Talk (Kiểu Tina)</h3>
        <p class="cl-body">Đeo mic cài áo, vừa đi quanh tiệm vừa kiểm tra tóc thợ đang làm. Chỉ nói những câu ngắn gọn chuyên môn với khách, không cần nhìn chằm chằm vào ống kính.</p>
      </div>
    </div>
  </section>

  <!-- MÀN 4 -->
  <section class="cl-zebra-section cl-zebra--tint">
    <div class="cl-sec-container">
      <div class="cl-badge">04 / BƯỚC CHUYỂN TOÀN DIỆN</div>
      <h2 class="title-short">LỘ TRÌNH 3 GIAI ĐOẠN CHO NGƯỜI SỢ CAMERA</h2>
      
      <div class="apple-card">
        <div class="apple-card__badge" style="color: #0369a1; background: #e0f2fe;">GIAI ĐOẠN 1: TẬP BAY BẰNG THỊ GIÁC (TUẦN 1-2)</div>
        <p class="cl-body">Chưa lộ mặt. Cầm điện thoại luyện kỹ thuật quay cận cảnh, trung cảnh (5 Kỹ thuật cơ bản). Lồng nhạc theo nhịp chuyển cảnh (Match cut). Tạo ra những video khoe nếp tóc bồng bềnh mượt mà.</p>
      </div>
      <div class="apple-card" style="margin-top: 16px;">
        <div class="apple-card__badge" style="color: #0f766e; background: #ccfbf1;">GIAI ĐOẠN 2: STORYTELLING 4 TẦNG (TUẦN 3-6)</div>
        <p class="cl-body">Bắt đầu thu voice-over (lồng tiếng) kể chuyện đằng sau bức ảnh. Sau đó tiến tới xuất hiện 3 giây đầu video, vừa làm tóc vừa tâm sự mỏng với khách.</p>
      </div>
    </div>
  </section>

  <!-- MÀN 5 -->
  <section class="cl-zebra-section cl-zebra--light">
    <div class="cl-sec-container">
      <div class="cl-badge">05 / KỊCH BẢN THỰC ĐỊA</div>
      <h2 class="title-short">KỊCH BẢN WALK & TALK TRỊ TÓC NÁT</h2>
      
      <div class="script-columns">
        <div class="script-col script-col--visual">
          <div class="script-col__tag">HÌNH ẢNH (B-ROLL)</div>
          <p>Trang đi từ từ lại phía ghế khách. Cầm lọn tóc của khách lên vuốt nhẹ, đưa sát vào ống kính cho thấy độ khô xơ.</p>
          <p>Lắc đầu nhẹ, sau đó bắt đầu bôi phục hồi.</p>
        </div>
        <div class="script-col script-col--audio">
          <div class="script-col__tag">ÂM THANH (VOICE/THOẠI)</div>
          <p><b>[Thoại]:</b> "Khách qua tiệm em đòi tẩy nhuộm sáng, nhưng nhìn đuôi tóc thế này thì em chịu. Tiền thì em thích thật, nhưng làm xong khách rụng hết tóc thì em thà mất khách còn hơn."</p>
          <p><b>[Thoại]:</b> "Bây giờ em ủ phục hồi cho chị trước, 1 tháng sau tóc khỏe lại rồi em mới uốn cho chị nhé."</p>
        </div>
      </div>
    </div>
  </section>

  <!-- MÀN 6-8 -->
  <section class="cl-zebra-section cl-zebra--tint">
    <div class="cl-sec-container">
      <div class="cl-badge">06-08 / TƯ DUY HỆ THỐNG</div>
      <h2 class="title-short">HÀNH ĐỘNG CHỊU THIỆT ĐỂ CHỐT TỆP LURKER</h2>
      
      <div class="apple-card" style="border-left: 4px solid var(--cl-accent);">
        <div class="apple-card__title" style="color: var(--cl-accent);">Tín Hiệu Đắt Giá (Costly Signaling)</div>
        <p class="cl-body">
          • <b>Từ chối kiếm tiền nhanh:</b> Khước từ yêu cầu uốn/tẩy của khách khi nền tóc không đảm bảo. Sẵn sàng mất doanh thu 2-3 triệu ngay trước mắt để bảo vệ da đầu và sức khỏe tóc của khách. Những người xem im lặng (Lurker) nhìn thấy điều này sẽ tuyệt đối tin tưởng.<br><br>
          • <b>Cam kết đền tiền:</b> <i>"Làm tóc bên em về gội đầu mà mất nếp, em hoàn lại 100% tiền."</i> Sự tự tin này chỉ có ở những người thợ làm ăn thật chất, và nó tiết kiệm hàng tháng trời tư vấn chốt sale.
        </p>
      </div>
    </div>
  </section>

  {footer}
</body>
</html>
"""

full_html = f"<!DOCTYPE html>\n<html lang=\"vi\">\n{head}\n{body_content}"
with open('logickenh-trangdang.html', 'w') as f:
    f.write(full_html)
