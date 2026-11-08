#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_round2_fixes.py
=====================
Cập nhật toàn diện theo chỉ đạo của anh Việt và bản viết của Thư ký (Claude Opus 5.5 Native):
1. Mục ③ Cuốn sổ biên lai mồ hôi: Bỏ ví dụ thợ sửa loa, thay bằng ví dụ ngành Spa (chăm ca da mỏng đỏ, quay ngày 3, 7, 14) + hộp mở rộng "Người mới tìm việc thật ở đâu" cân đối giao diện 3 cột.
2. Bài tập 90 giây: Nhúng trực tiếp trình phát video Walk & Talk của Tina Nguyễn (@tinanguyen2004) + 6 khung hình phân cảnh (nổi bật cảnh 3 nói chuyện với khách thật) + link sống 100%.
3. Ba thẻ học viên thật từ STU: Chị Đặng Hường (Spa Đông Y Đặng Hường K3), Chị Thắm Thỏ (Thắm Thỏ Beauty & Spa K2 Hà Tĩnh), Chị Yến Tâng Xinh (Thực phẩm chăm sóc sức khỏe & dẫn dắt đội nhóm K3 - bỏ sạch chữ Diamond/Trang sức bịa đặt).
4. Bộ 10 câu hỏi mở bốc thăm đầu giờ: Có đầy đủ phần Gợi mở trả lời tại lớp + Cách biến thành video 30-60s của Thư ký, thiết kế giao diện lưới thẻ .lx-raffle-grid / .lx-raffle-card chuẩn mực, sửa triệt để lỗi dính vạch xanh.
"""

with open("opus_pack/opus_draft_body.html", "r", encoding="utf-8") as f:
    body = f.read()

# -------------------------------------------------------------------------
# 0. BỔ SUNG CSS CHUẨN CHO .lx-raffle-grid, .lx-tina-showcase, .lx-newbie-box
# -------------------------------------------------------------------------
css_addition = """
  /* === ROUND 2 UI FIXES: TINA SHOWCASE, NEWBIE BOX, STUDENT CARDS, 10 RAFFLE CARDS === */
  .lx-newbie-box {
    background: #ffffff;
    border: 1px solid var(--cl-line);
    border-left: 5px solid var(--cl-accent);
    border-radius: 16px;
    padding: 22px 24px;
    margin: 16px 0 24px;
    box-shadow: 0 4px 16px rgba(9, 13, 22, 0.03);
  }
  .lx-newbie-box h4 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    font-weight: 800;
    color: var(--cl-text-base);
    margin: 0 0 10px;
  }
  .lx-newbie-box ul {
    margin: 8px 0 0;
    padding-left: 20px;
  }
  .lx-newbie-box li {
    font-size: 15px;
    line-height: 1.7;
    color: #1e293b;
    margin-bottom: 8px;
  }

  .lx-tina-showcase {
    margin-top: 16px;
    padding: 20px;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 14px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
  }
  .lx-tina-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 14px;
  }
  .lx-tina-badge {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #166534;
    background: #dcfce7;
    padding: 3px 10px;
    border-radius: 999px;
    margin-bottom: 6px;
  }
  .lx-tina-title {
    display: block;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.35;
  }
  .lx-tina-sub {
    display: block;
    font-size: 13.5px;
    color: #475569;
    margin-top: 4px;
  }
  .lx-tina-btns {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }
  .lx-tina-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 13.5px;
    font-weight: 700;
    padding: 8px 14px;
    border-radius: 10px;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .lx-tina-btn--primary {
    background: #1a73e8;
    color: #ffffff !important;
    border: 1px solid #1a73e8;
  }
  .lx-tina-btn--primary:hover {
    background: #1557b0;
  }
  .lx-tina-btn--ghost {
    background: #f8fafc;
    color: #0f172a !important;
    border: 1px solid #cbd5e1;
  }
  .lx-tina-btn--ghost:hover {
    background: #e2e8f0;
  }
  .lx-tina-body {
    display: grid;
    grid-template-columns: 240px 1fr;
    gap: 18px;
    align-items: start;
  }
  .lx-tina-video-wrap {
    background: #0b0f19;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #1e293b;
  }
  .lx-tina-video-wrap video {
    display: block;
    width: 100%;
    max-height: 420px;
    object-fit: cover;
  }
  .lx-tina-shots {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
  }
  .lx-tina-shot {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    overflow: hidden;
    font-size: 12px;
  }
  .lx-tina-shot--highlight {
    border: 2px solid #16a34a;
    background: #f0fdf4;
  }
  .lx-tina-shot img {
    display: block;
    width: 100%;
    aspect-ratio: 9 / 12;
    object-fit: cover;
  }
  .lx-tina-shot-cap {
    padding: 6px 8px;
    line-height: 1.35;
    color: #1e293b;
  }
  .lx-tina-shot-cap b {
    display: block;
    font-family: var(--font-mono);
    font-size: 10.5px;
    color: #1a73e8;
    margin-bottom: 2px;
  }
  .lx-tina-shot--highlight .lx-tina-shot-cap b {
    color: #15803d;
  }

  .lx-case {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-decoration: none;
    background: #fff;
    border: 1px solid var(--cl-line);
    border-top: 4px solid var(--lx-green);
    border-radius: 16px;
    padding: 20px;
    transition: all .22s ease;
  }
  .lx-case-meta {
    font-size: 14px;
    color: #334155;
    line-height: 1.6;
    margin: 8px 0 14px;
  }
  .lx-case-meta p {
    margin: 0 0 8px;
  }
  .lx-case-lesson {
    background: #f0fdf4;
    border-left: 3px solid #16a34a;
    padding: 8px 10px;
    border-radius: 6px;
    font-size: 13.5px;
    color: #14532d;
    line-height: 1.5;
    margin-bottom: 12px;
  }
  .lx-case-meta strong {
    font-family: inherit;
    font-size: inherit;
    font-weight: 700;
    color: #0f172a;
  }
  .lx-case-lesson strong {
    font-family: inherit;
    font-size: inherit;
    font-weight: 700;
    color: #14532d;
  }
  .lx-case-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 10px;
    border-top: 1px dashed #e2e8f0;
  }

  .lx-raffle-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
    margin-top: 24px;
  }
  .lx-raffle-card {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-top: 4px solid #1a73e8;
    border-radius: 16px;
    padding: 22px 24px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .lx-raffle-top {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .lx-raffle-num {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 700;
    color: #1a73e8;
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    padding: 3px 10px;
    border-radius: 999px;
  }
  .lx-raffle-tag {
    font-family: var(--font-mono);
    font-size: 11.5px;
    font-weight: 600;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }
  .lx-raffle-q {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 17.5px;
    font-weight: 800;
    line-height: 1.4;
    color: #0f172a;
    margin: 0;
  }
  .lx-raffle-ans {
    background: #f8fafc;
    border-left: 3px solid #1a73e8;
    border-radius: 8px;
    padding: 12px 14px;
    font-size: 14.5px;
    line-height: 1.65;
    color: #1e293b;
  }
  .lx-raffle-ans b {
    color: #0f172a;
  }
  .lx-raffle-vid {
    background: #f0fdf4;
    border-left: 3px solid #16a34a;
    border-radius: 8px;
    padding: 11px 14px;
    font-size: 14px;
    line-height: 1.6;
    color: #14532d;
  }
  .lx-raffle-vid b {
    color: #166534;
  }

  @media (max-width: 860px) {
    .lx-tina-body {
      grid-template-columns: 1fr;
    }
    .lx-tina-video-wrap {
      max-width: 300px;
      margin: 0 auto;
    }
    .lx-raffle-grid {
      grid-template-columns: 1fr;
    }
  }
  @media (max-width: 520px) {
    .lx-tina-shots {
      grid-template-columns: repeat(2, 1fr);
    }
  }
"""

if ".lx-raffle-grid" not in body:
    body = body.replace("</style>\n</head>", css_addition + "\n</style>\n</head>")
    print("Injected Round 2 CSS into opus_draft_body.html")

# -------------------------------------------------------------------------
# 1. CẬP NHẬT MỤC ③ CUỐN SỔ BIÊN LAI MỒ HÔI (VÍ DỤ SPA + HỘP NGƯỜI MỚI)
# -------------------------------------------------------------------------
old_proof_block = """      <div class="lx-proof__card">
        <h4>③ Cuốn sổ biên lai mồ hôi</h4>
        <p>Sự tự tin không đến từ câu tự nhủ trước gương. Mỗi việc làm trọn đến cuối là một tờ biên lai, và cái đầu chỉ tin vào cuốn sổ ấy.</p>
        <p>Nhưng người mới nào cũng hỏi đúng một câu: <em>"Chưa có khách, chưa có việc, thì lấy đâu ra biên lai?"</em></p>
        <p>Tờ biên lai đầu tiên không ai cấp cho bạn. Bạn tự viết.</p>
        <p>Người bán dưa ngoài chợ không đứng rao "dưa tôi ngọt lắm". Bác bổ đôi một quả ngay trên sạp, xắn một miếng đưa khách ăn thử. Quả dưa bổ ra đỏ au mới là bằng chứng, lời rao thì không.</p>
        <p>Thợ sửa loa mới mở tiệm cũng thế. Chưa ai biết anh là ai. Anh xin về một chiếc loa rè mà hai tiệm khác đã trả lại. Tháo vỏ, đặt lên bàn, đo từng con tụ, chỉ đúng con tụ phồng đầu, thay xong bật lên cho tiếng trong trở lại. Cả quá trình ấy quay lại được. Đó là tờ biên lai đầu tiên của anh.</p>
        <p><strong>Người mới tìm việc thật ở đâu:</strong></p>
        <ul>
          <li>Làm thật cho người nhà, bạn bè: cắm bó hoa cho mẹ, sửa dàn loa nhà hàng xóm, chăm da cho em gái. Miễn là việc thật, chỗ hỏng thật.</li>
          <li>Nhận một ca khó mà nơi khác đã bó tay, lấy giá vốn, đổi lại xin phép được quay toàn bộ quá trình xử lý.</li>
          <li>Tự làm lại một lỗi hay gặp ngay trên bàn mình: một bó hoa cắt gốc, một bó không cắt, đặt cạnh nhau sau 2 tiếng.</li>
        </ul>
        <p>Kho video quay việc thật là cuốn sổ biên lai công khai của bạn. Mười tờ đầu bạn tự viết. Về sau, khách sẽ viết hộ.</p>
        <small>Logic 36 · Tự viết biên lai đầu tiên</small>
      </div>
    </div>"""

new_proof_block = """      <div class="lx-proof__card">
        <h4>③ Cuốn sổ biên lai mồ hôi</h4>
        <p>Sự tự tin không đến từ câu tự nhủ trước gương. Mỗi việc làm trọn đến cuối là một tờ biên lai, và cái đầu chỉ tin vào sổ biên lai đó. Chưa có khách đông, biên lai có từ ca làm thật đầu tiên cho người quen.</p>
        <p>Một tiệm spa nhỏ mới mở, chị chủ không đăng ảnh mạng hứa "trắng mịn sau một buổi". Chị nhận chăm một ca da thật của người quen bị mỏng đỏ, nổi mụn li ti vì dùng nhầm kem lột tẩy — không lấy tiền, chỉ xin phép ghi hình. Buổi đầu soi da dưới đèn chỉ rõ chỗ mao mạch giãn; các ngày thứ 3, thứ 7, thứ 14 đều quay cận nền da dịu dần dưới cùng một góc đèn. Ca làm thật đó là tờ biên lai đầu tiên của tiệm.</p>
        <small>Logic 36 · Tự viết tờ biên lai đầu tiên</small>
      </div>
    </div>

    <div class="lx-newbie-box">
      <h4>Người mới chưa có khách thì tìm việc thật ở đâu để quay?</h4>
      <ul>
        <li><strong>Nhận ca thật của người quen, đổi lại xin phép quay:</strong> Với <em>Spa</em> là một ca da kích ứng, mỏng đỏ như trên. Với <em>Hoa tươi</em> là bó hoa sinh nhật cho đồng nghiệp, quay từ lúc cắt gốc, tỉa lá ngập nước đến lúc trao tận tay.</li>
        <li><strong>Nhận cứu đồ người khác làm hỏng:</strong> Với <em>Đồ gỗ</em> là chiếc ghế lung lay nhà hàng xóm đã bị đóng đinh chữa tạm — tháo ra, đục lại mộng, ghép keo, kẹp qua đêm, sáng hôm sau ngồi thử cho người xem thấy chắc. Với <em>Hoa tươi</em> là bó hồng khách mua chỗ khác về đã gục cổ — cắt lại gốc, ngâm nước sâu, hai tiếng sau hoa đứng dậy.</li>
        <li><strong>Quay việc trên hàng của chính mình khi chưa có khách:</strong> <em>Hoa tươi</em> quay sơ chế lô hồng mới nhập; <em>Đồ gỗ</em> quay chà nhám mặt dưới bàn chỗ khách không bao giờ nhìn; <em>Spa</em> quay quy trình khử khuẩn dụng cụ trước mỗi ca. Kho video quay việc thật là cuốn sổ biên lai công khai của bạn.</li>
      </ul>
    </div>"""

assert old_proof_block in body, "old_proof_block not found!"
body = body.replace(old_proof_block, new_proof_block)
print("Updated: Section ③ Cuốn sổ biên lai mồ hôi (Ví dụ Spa)")

# -------------------------------------------------------------------------
# 2. CẬP NHẬT BÀI TẬP 90 GIÂY + NHÚNG VIDEO & 6 PHÂN CẢNH TINA NGUYỄN
# -------------------------------------------------------------------------
old_exercise_block = """    <div class="highlight-rule">
      <strong>Bài tập thực hành: Cắt 90 giây giải câu hỏi khó nhất</strong>
      <ol style="margin: 8px 0 12px 20px; padding: 0; line-height: 1.6;">
        <li>Dựng điện thoại ở góc chéo bàn làm việc, cao ngang vai, chếch chừng 45 độ, thấy được tay bạn và một phần khách.</li>
        <li>Bấm quay từ đầu ca rồi quên nó đi. Cứ làm việc như mọi ngày.</li>
        <li>Cuối ngày tua lại, tìm lúc khách hỏi câu khó nhất. Cắt đúng 90 giây bạn giải thích câu đó.</li>
        <li>Che tên khách; nếu chưa xin phép thì che cả mặt. Xin phép từ trước vẫn là tốt nhất.</li>
      </ol>
      <div style="margin-top: 10px; padding-top: 10px; border-top: 1px dashed rgba(0,0,0,0.15);">
        <span>Xem video mẫu trước khi quay: Tina Nguyễn (@tinanguyen2004) cầm máy đi từ cửa phòng khám vào tới giường tư vấn, nói chuyện với khách thật. Không kịch bản, không đèn, chỉ có việc thật đang diễn ra.</span><br/>
        <a href="https://kenh.fedu.vn/dinh-dang/walkntalk2.0.html" target="_blank" rel="noopener" style="font-weight: 700; color: #1a56db; text-decoration: underline; display: inline-block; margin-top: 6px;">👉 Xem video mẫu Walk & Talk của Tina Nguyễn ↗</a>
      </div>
    </div>"""

new_exercise_block = """    <div class="highlight-rule">
      <strong>Bài tập ngày mai: Cắt 90 giây giải câu hỏi khó nhất của khách</strong>
      <ol style="margin: 8px 0 12px 20px; padding: 0; line-height: 1.65;">
        <li>Dựng điện thoại ở góc chéo bàn làm việc, cao ngang vai, chếch chừng 45 độ, thấy được tay bạn và một phần khách.</li>
        <li>Bấm quay từ đầu ca rồi quên nó đi. Cứ làm việc như mọi ngày.</li>
        <li>Cuối ngày tua lại, tìm lúc khách hỏi câu khó nhất. Cắt đúng 90 giây bạn giải thích câu đó.</li>
        <li>Che tên khách; nếu chưa xin phép thì che cả mặt. Xin phép từ trước vẫn là tốt nhất.</li>
      </ol>

      <div class="lx-tina-showcase" id="mau-tina-nguyen">
        <div class="lx-tina-top">
          <div>
            <span class="lx-tina-badge">VIDEO MẪU THỰC CHỨNG · WALK &amp; TALK</span>
            <strong class="lx-tina-title">Tina Nguyễn (@tinanguyen2004) — Đi từ cửa phòng khám → Dừng cạnh giường nói chuyện với khách thật → Ngồi bàn chốt lịch</strong>
            <span class="lx-tina-sub">43,8 giây · 6 phân cảnh thực tế · Bấm phát xem ngay bên dưới hoặc mở trang giải phẫu chi tiết</span>
          </div>
          <div class="lx-tina-btns">
            <a class="lx-tina-btn lx-tina-btn--primary" href="https://kenh.fedu.vn/dinh-dang/walkntalk2.0.html#tina-nguyen" target="_blank" rel="noopener">👉 Mở bài giải phẫu Walk &amp; Talk 2.0 ↗</a>
            <a class="lx-tina-btn lx-tina-btn--ghost" href="https://www.tiktok.com/@tinanguyen2004/video/7673468312290037012" target="_blank" rel="noopener">Bài gốc TikTok ↗</a>
          </div>
        </div>

        <div class="lx-tina-body">
          <div class="lx-tina-video-wrap">
            <video controls playsinline preload="metadata" src="https://media.fedu.vn/videos/7673468312290037012.mp4" poster="https://media.fedu.vn/images/IG_@tinanguyen2004_7673468312290037012_Double_Day_lu%C3%B4n_l%C3%A0_d%E1%BB%8Bp_%C4%91%E1%BB%83_kh%C3%A1ch_h%C3%A0ng_l%E1%BB%B1a_%C4%91%C6%B0%E1%BB%A3c/shot_03_mid.webp"></video>
          </div>
          <div class="lx-tina-shots">
            <div class="lx-tina-shot">
              <img src="https://media.fedu.vn/images/IG_@tinanguyen2004_7673468312290037012_Double_Day_lu%C3%B4n_l%C3%A0_d%E1%BB%8Bp_%C4%91%E1%BB%83_kh%C3%A1ch_h%C3%A0ng_l%E1%BB%B1a_%C4%91%C6%B0%E1%BB%A3c/shot_01_mid.webp" alt="Cảnh 1 Sải bước từ cửa vào" loading="lazy"/>
              <div class="lx-tina-shot-cap"><b>CẢNH 01 · 0–2.4s</b>Sải bước từ cửa vào phòng khám</div>
            </div>
            <div class="lx-tina-shot">
              <img src="https://media.fedu.vn/images/IG_@tinanguyen2004_7673468312290037012_Double_Day_lu%C3%B4n_l%C3%A0_d%E1%BB%8Bp_%C4%91%E1%BB%83_kh%C3%A1ch_h%C3%A0ng_l%E1%BB%B1a_%C4%91%C6%B0%E1%BB%A3c/shot_02_mid.webp" alt="Cảnh 2 Góc qua vai dẫn vào phòng" loading="lazy"/>
              <div class="lx-tina-shot-cap"><b>CẢNH 02 · 2.4–4.7s</b>Góc qua vai dẫn vào phòng điều trị</div>
            </div>
            <div class="lx-tina-shot lx-tina-shot--highlight">
              <img src="https://media.fedu.vn/images/IG_@tinanguyen2004_7673468312290037012_Double_Day_lu%C3%B4n_l%C3%A0_d%E1%BB%8Bp_%C4%91%E1%BB%83_kh%C3%A1ch_h%C3%A0ng_l%E1%BB%B1a_%C4%91%C6%B0%E1%BB%A3c/shot_03_mid.webp" alt="Cảnh 3 Dừng cạnh giường nói chuyện với khách thật" loading="lazy"/>
              <div class="lx-tina-shot-cap"><b>CẢNH 03 · 4.7–18.9s ⭐</b>Dừng cạnh giường nói chuyện với khách thật</div>
            </div>
            <div class="lx-tina-shot">
              <img src="https://media.fedu.vn/images/IG_@tinanguyen2004_7673468312290037012_Double_Day_lu%C3%B4n_l%C3%A0_d%E1%BB%8Bp_%C4%91%E1%BB%83_kh%C3%A1ch_h%C3%A0ng_l%E1%BB%B1a_%C4%91%C6%B0%E1%BB%A3c/shot_04_mid.webp" alt="Cảnh 4 Cận cảnh nền da trước" loading="lazy"/>
              <div class="lx-tina-shot-cap"><b>CẢNH 04 · 18.9–20.8s</b>Cận cảnh nền da trước khi làm</div>
            </div>
            <div class="lx-tina-shot">
              <img src="https://media.fedu.vn/images/IG_@tinanguyen2004_7673468312290037012_Double_Day_lu%C3%B4n_l%C3%A0_d%E1%BB%8Bp_%C4%91%E1%BB%83_kh%C3%A1ch_h%C3%A0ng_l%E1%BB%B1a_%C4%91%C6%B0%E1%BB%A3c/shot_05_mid.webp" alt="Cảnh 5 Cận cảnh nền da sau" loading="lazy"/>
              <div class="lx-tina-shot-cap"><b>CẢNH 05 · 20.8–23.2s</b>Cận cảnh nền da căng bóng sau làm</div>
            </div>
            <div class="lx-tina-shot">
              <img src="https://media.fedu.vn/images/IG_@tinanguyen2004_7673468312290037012_Double_Day_lu%C3%B4n_l%C3%A0_d%E1%BB%8Bp_%C4%91%E1%BB%83_kh%C3%A1ch_h%C3%A0ng_l%E1%BB%B1a_%C4%91%C6%B0%E1%BB%A3c/shot_06_mid.webp" alt="Cảnh 6 Ngồi bàn tư vấn chốt lịch" loading="lazy"/>
              <div class="lx-tina-shot-cap"><b>CẢNH 06 · 23.2–43.8s</b>Ngồi bàn tư vấn chốt lịch hẹn</div>
            </div>
          </div>
        </div>
      </div>
    </div>"""

assert old_exercise_block in body, "old_exercise_block not found!"
body = body.replace(old_exercise_block, new_exercise_block)
print("Updated: Section Bài tập ngày mai + Video & 6 phân cảnh Tina Nguyễn")

# -------------------------------------------------------------------------
# 3. CẬP NHẬT BA THẺ HỌC VIÊN THẬT TỪ STU (ĐẶNG HƯỜNG, THẮM THỎ, TÂNG XINH)
# -------------------------------------------------------------------------
old_cases_block = """    <h3 class="lx-h3">Dẫn chứng từ ba học viên thật tại các lớp Offline</h3>
    <p class="cl-body">Khi đã đi qua đủ số lượng video cần thiết, kết quả hiện ra rõ ràng ở những học viên kiên trì quay việc thật tại cơ sở của mình:</p>
    <div class="lx-cases">
      <a class="lx-case" href="https://stu.fedu.vn/audits/ang_huong.html" target="_blank" rel="noopener">
        <b>Chị Đặng Hường — Đặng Hường Y Quán</b>
        <span>Học viên Lớp K3 · Đông y & Trị liệu</span>
        <p style="font-size: 13px; color: #475569; margin: 6px 0; line-height: 1.4;">Trước đây ngại ống kính, chưa từng đứng trước máy quay. Bắt đầu bằng việc quay thật các ca nắn chỉnh đau mỏi vai gáy ngay tại quán, vừa làm vừa chỉ rõ chỗ tắc nghẽn.</p>
        <strong style="color: #15803d;">Lịch kín cả tuần</strong>
      </a>
      <a class="lx-case" href="https://stu.fedu.vn/audits/tham_tho_offline2.html" target="_blank" rel="noopener">
        <b>Chị Thắm Thỏ — Thắm Thỏ Spa</b>
        <span>Học viên Lớp K2 · Spa Chăm sóc da</span>
        <p style="font-size: 13px; color: #475569; margin: 6px 0; line-height: 1.4;">Quay cận cảnh quy trình xử lý da mụn thực tế, giải thích cặn kẽ từng hoạt chất đang phản ứng trên da thay vì hứa hẹn da đẹp sau 1 đêm.</p>
        <strong style="color: #15803d;">Khách xa tự tìm đến</strong>
      </a>
      <a class="lx-case" href="https://kenh.fedu.vn/09-case.html" target="_blank" rel="noopener">
        <b>Chị Tâng Xinh — Tâng Xinh Diamond</b>
        <span>Học viên Offline · Hệ thống Trang sức</span>
        <p style="font-size: 13px; color: #475569; margin: 6px 0; line-height: 1.4;">Dựng lại kịch bản cho cả hệ thống dựa trên những video chia sẻ giá trị thật, không câu lượt xem ảo. Đưa kênh về đúng mục tiêu ra được đơn hàng thật.</p>
        <strong style="color: #15803d;">Video ra đơn thật</strong>
      </a>
    </div>"""

new_cases_block = """    <h3 class="lx-h3">Dẫn chứng từ ba học viên thật tại các lớp Offline</h3>
    <p class="cl-body">Ba chị dưới đây là học viên thật của lớp, số liệu lấy trực tiếp từ hồ sơ khám kênh trên hệ thống STU. Ba nghề khác nhau nhưng chung một điểm: kênh chỉ bắt đầu giữ đúng người cần khi chủ kênh thôi diễn cho vui và quay đúng việc mình làm hằng ngày.</p>
    <div class="lx-cases">
      <a class="lx-case" href="https://stu.fedu.vn/audits/ang_huong.html" target="_blank" rel="noopener">
        <div>
          <b>Chị Đặng Hường — Spa Đông Y Đặng Hường</b>
          <span>Lớp K3 · Hà Nội · 9.600 theo dõi · 90 video</span>
          <div class="lx-case-meta">
            <p><strong>Nghề:</strong> Tốt nghiệp Cao đẳng Y tế Hà Nội; tiệm chăm nám chân đinh, nám mảng, gội đầu dưỡng sinh, bấm huyệt cổ vai gáy.</p>
            <p><strong>Trước:</strong> Quay nhiều clip vợ chồng nhép tiếng hài đạt 7.000–18.000 lượt xem, nhưng người xem chỉ xem cho vui, không ra khách quanh tiệm.</p>
            <p><strong>Khi quay việc thật:</strong> Cầm bút chấm từng đốt sống lưng trên người thật, chỉ đúng vị trí, giải thích vì sao vai gáy đau mỏi và gốc của vết nám nằm ở đâu — giữ đúng người cần chữa quanh khu vực và cả khách từ Tây Bắc tìm xuống tận tiệm.</p>
          </div>
        </div>
        <div>
          <div class="lx-case-lesson"><strong>Bài học:</strong> Clip vui mang về người xem, còn tay nghề đặt lên người thật mới mang về khách.</div>
          <div class="lx-case-footer">
            <strong style="font-size: 18px; color: #15803d;">Khách Tây Bắc tìm xuống</strong>
            <span style="margin: 0; color: #1a73e8; font-weight: 700;">Xem hồ sơ STU ↗</span>
          </div>
        </div>
      </a>

      <a class="lx-case" href="https://stu.fedu.vn/audits/tham_tho_offline2.html" target="_blank" rel="noopener">
        <div>
          <b>Chị Thắm Thỏ — Thắm Thỏ Beauty &amp; Spa</b>
          <span>Lớp K2 · TP. Hà Tĩnh &amp; Hương Khê · 14.000 theo dõi</span>
          <div class="lx-case-meta">
            <p><strong>Nghề:</strong> 10 năm phun xăm thẩm mỹ và chăm da nám tại 2 cơ sở ở Hà Tĩnh (80 video).</p>
            <p><strong>Khi quay việc thật:</strong> Chị tự thu tiếng bằng giọng Hà Tĩnh của mình, kể chuyện nghề thật: Chặng đường 10 năm làm nghề (29.000 lượt xem), Lái xe 100 km đi về giữa hai cơ sở (15.000 lượt xem), Vì sao tiệm trong ngõ 131 Lê Duẩn không biển to vẫn đông khách (12.000 lượt xem), Hai ca môi hỏng vì mực hóa học (12.000 lượt xem).</p>
            <p><strong>Kết quả:</strong> Khách tìm đến, và cả học viên khóa sau như chị Oanh K4 cũng chủ động gọi điện hỏi chuyện chị Thắm trước khi đi học.</p>
          </div>
        </div>
        <div>
          <div class="lx-case-lesson"><strong>Bài học:</strong> Giọng quê thật và chuyện nghề thật làm người ta tin trước khi gặp mặt.</div>
          <div class="lx-case-footer">
            <strong style="font-size: 18px; color: #15803d;">12K–29K xem từ giọng thật</strong>
            <span style="margin: 0; color: #1a73e8; font-weight: 700;">Xem hồ sơ STU ↗</span>
          </div>
        </div>
      </a>

      <a class="lx-case" href="https://stu.fedu.vn/audits/tang_xinh_chi_yen.html" target="_blank" rel="noopener">
        <div>
          <b>Chị Yến (Tâng Xinh) — Thực phẩm sức khỏe &amp; Đội nhóm</b>
          <span>Lớp K3 · TikTok 69.9K &amp; Facebook 86K theo dõi</span>
          <div class="lx-case-meta">
            <p><strong>Nghề:</strong> 8 năm giảng viên Đại học Hà Nội, Tiến sĩ ở Nhật. Năm 35 tuổi rẽ sang làm nhân viên bán hàng tại FPT bên Nhật, rồi gây dựng đội kinh doanh thực phẩm bảo vệ sức khỏe và dinh dưỡng.</p>
            <p><strong>Trước:</strong> Các bài nói chuyện hôn nhân trên TikTok đạt 2,0 triệu, 1,3 triệu, 1,1 triệu lượt xem, nhưng người xem không biết chị làm nghề gì.</p>
            <p><strong>Khi quay việc thật:</strong> Kể chuyện đời mình "Tiến sĩ đi bán hàng" (16.000 lượt xem trên Facebook) và quay cảnh pha trà dinh dưỡng giữ sức làm 12 tiếng mỗi ngày theo ba nhịp: Vì sao – Là gì – Làm thế nào.</p>
          </div>
        </div>
        <div>
          <div class="lx-case-lesson"><strong>Bài học:</strong> Lượt xem triệu chưa phải là khách. Khi người xem biết bạn là ai và làm gì mỗi ngày, lượt xem mới có lối dẫn về nghề.</div>
          <div class="lx-case-footer">
            <strong style="font-size: 18px; color: #15803d;">Khớp nối triệu view về nghề</strong>
            <span style="margin: 0; color: #1a73e8; font-weight: 700;">Xem hồ sơ STU ↗</span>
          </div>
        </div>
      </a>
    </div>"""

assert old_cases_block in body, "old_cases_block not found!"
body = body.replace(old_cases_block, new_cases_block)
print("Updated: Section 3 thẻ học viên thật từ STU (Đặng Hường, Thắm Thỏ, Chị Yến Tâng Xinh)")

# -------------------------------------------------------------------------
# 4. CẬP NHẬT 10 CÂU HỎI MỞ BỐC THĂM ĐẦU GIỜ (KÈM LỜI GIẢI CỦA THƯ KÝ & GIAO DIỆN MỚI)
# -------------------------------------------------------------------------
start_boctham = "<!-- 10 CÂU HỎI BỐC THĂM ĐẦU GIỜ CHO LỚP OFFLINE -->"
end_boctham = "<!-- 10 CÂU HỎI ĐẮT GIÁ -->"
idx_b1 = body.find(start_boctham)
idx_b2 = body.find(end_boctham)
assert idx_b1 != -1 and idx_b2 != -1, "Boc tham markers not found!"

new_boctham_section = """<!-- 10 CÂU HỎI BỐC THĂM ĐẦU GIỜ CHO LỚP OFFLINE -->
<section class="cl-zebra-section" id="ch-boc-tham" style="background: #f8fafc; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
  <div class="cl-sec-container cl-sec-container--wide">
    <div class="cl-badge">BỐC THĂM ĐẦU GIỜ · LỚP OFFLINE</div>
    <h2 class="title-short">10 câu hỏi mở bốc thăm đầu giờ<br/>Ai cũng có chuyện thật để kể và quay ngay</h2>
    <p class="cl-body">Bộ câu hỏi mở dành cho buổi gặp mặt đầu tiên tại lớp Offline. Dù bạn là người chưa từng cầm máy quay hay đã có kênh hàng chục nghìn người theo dõi, rút một lá thăm bất kỳ đều có ngay cách trả lời từ việc thật và dựng thành kịch bản 30–60 giây:</p>

    <div class="lx-raffle-grid">
      <!-- CÂU 01 -->
      <div class="lx-raffle-card">
        <div class="lx-raffle-top">
          <span class="lx-raffle-num">CÂU 01</span>
          <span class="lx-raffle-tag">Câu hỏi quen thuộc nhất</span>
        </div>
        <h3 class="lx-raffle-q">Câu nào khách hỏi bạn nhiều đến mức đang ngủ bạn cũng trả lời được?</h3>
        <div class="lx-raffle-ans">
          <b>💡 Gợi mở cách trả lời tại lớp:</b> Người làm lâu mở lại Zalo, Messenger, lướt 20 tin gần nhất và tìm câu lặp lại từ ba lần trở lên. Người mới nhớ lại câu người quen hỏi ngay khi biết mình mở tiệm: <em>"Làm có đau không?", "Hoa để được mấy ngày?", "Gỗ này có bị mối không?"</em>. Câu trả lời trơn tru đến mức ngủ cũng nói được thường là câu mình đang trả lời quá vội, chưa lần nào nói cho tận gốc.
        </div>
        <div class="lx-raffle-vid">
          <b>🎬 Dựng thành video 30–60s:</b> Cảnh đầu là màn hình tin nhắn đã che tên, hiện đúng câu hỏi đó, rồi cắt sang đôi tay đang làm. Câu mở: <em>"Tuần này có năm người hỏi em câu này, em trả lời một lần cho đủ."</em>
        </div>
      </div>

      <!-- CÂU 02 -->
      <div class="lx-raffle-card">
        <div class="lx-raffle-top">
          <span class="lx-raffle-num">CÂU 02</span>
          <span class="lx-raffle-tag">Lần mất khách đáng nhớ</span>
        </div>
        <h3 class="lx-raffle-q">Lần gần nhất bạn mất một người khách, lý do thật sự sâu xa theo bạn là gì?</h3>
        <div class="lx-raffle-ans">
          <b>💡 Gợi mở cách trả lời tại lớp:</b> Đừng dừng ở hai chữ "chê đắt". Hỏi tiếp hai lần "vì sao": đắt so với cái gì, và khách đã không được thấy bước nào khiến họ thấy đắt. Người mới nhớ lại lần có người hỏi giá xong rồi im luôn. Lý do sâu xa thường không nằm ở con số mà ở phần việc khách chưa từng được nhìn thấy.
        </div>
        <div class="lx-raffle-vid">
          <b>🎬 Dựng thành video 30–60s:</b> Cảnh đầu quay cận đúng bước việc mà người khách đó không thấy. Câu mở: <em>"Có chị khách bỏ em đi vì chê đắt. Sau này em mới hiểu chị không chê giá, chị chưa được thấy bước này."</em>
        </div>
      </div>

      <!-- CÂU 03 -->
      <div class="lx-raffle-card">
        <div class="lx-raffle-top">
          <span class="lx-raffle-num">CÂU 03</span>
          <span class="lx-raffle-tag">Video khiến bạn bấm lưu</span>
        </div>
        <h3 class="lx-raffle-q">Video gần nhất của người khác khiến bạn bấm nút lưu lại là video gì? Vì sao bạn lưu?</h3>
        <div class="lx-raffle-ans">
          <b>💡 Gợi mở cách trả lời tại lớp:</b> Mở ngay mục "Đã lưu" trên điện thoại. Người ta lưu vì sau này còn dùng: một cách làm, một danh sách, một lời dặn. Người mới chưa có kênh vẫn trả lời được, vì ai cũng là người xem. Cái làm bạn bấm lưu cũng chính là cái khiến khách của bạn bấm lưu.
        </div>
        <div class="lx-raffle-vid">
          <b>🎬 Dựng thành video 30–60s:</b> Giữ khung của video đó, đặt vào một việc trong nghề mình, ví dụ "3 việc phải làm trong 24 giờ sau khi lấy nhân mụn", mỗi việc giơ một ngón tay. Câu mở: <em>"Chị lưu lại, tối nay sẽ cần đến."</em>
        </div>
      </div>

      <!-- CÂU 04 -->
      <div class="lx-raffle-card">
        <div class="lx-raffle-top">
          <span class="lx-raffle-num">CÂU 04</span>
          <span class="lx-raffle-tag">Nỗi sợ trước ống kính</span>
        </div>
        <h3 class="lx-raffle-q">Nếu bật máy quay ngay bây giờ, bạn sợ nhất điều gì: sợ mặt mình, sợ giọng mình, hay sợ người quen xem?</h3>
        <div class="lx-raffle-ans">
          <b>💡 Gợi mở cách trả lời tại lớp:</b> Nói thật nỗi sợ, vì gần như ai cũng sợ người quen xem hơn sợ người lạ. Người mới gỡ bằng cách quay đôi tay trước, khuôn mặt để sau: quay việc chứ không quay mình. Người đã có kênh thường sợ một thứ khác, là sợ video ít người xem. Hỏi lại mình: mình quay cho đông người xem hay cho đúng người cần.
        </div>
        <div class="lx-raffle-vid">
          <b>🎬 Dựng thành video 30–60s:</b> Cảnh đầu chỉ có đôi tay đang làm, giọng nói ngoài khung. Câu mở: <em>"Em chưa quen đứng trước máy, nên hôm nay để đôi tay em nói trước."</em>
        </div>
      </div>

      <!-- CÂU 05 -->
      <div class="lx-raffle-card">
        <div class="lx-raffle-top">
          <span class="lx-raffle-num">CÂU 05</span>
          <span class="lx-raffle-tag">Bước làm nghề khác biệt</span>
        </div>
        <h3 class="lx-raffle-q">Có bước nào trong nghề bạn làm cẩn thận khác hẳn người khác mà khách bình thường không hề biết?</h3>
        <div class="lx-raffle-ans">
          <b>💡 Gợi mở cách trả lời tại lớp:</b> Liệt kê những bước mà bỏ đi khách cũng không phát hiện ra, vì đó là chỗ giá trị thật của bạn nằm. Spa: hấp và khử khuẩn dụng cụ cho từng khách. Hoa tươi: cắt gốc chéo ngập trong nước. Đồ gỗ: chà nhám cả mặt dưới bàn. Người mới lấy bước thầy dạy kỹ mà mình thấy người ngoài hay bỏ qua.
        </div>
        <div class="lx-raffle-vid">
          <b>🎬 Dựng thành video 30–60s:</b> Quay cận đúng bước đó từ đầu đến cuối. Câu mở: <em>"Bước này em bỏ đi chị cũng không biết. Nhưng em không bỏ, vì…"</em>
        </div>
      </div>

      <!-- CÂU 06 -->
      <div class="lx-raffle-card">
        <div class="lx-raffle-top">
          <span class="lx-raffle-num">CÂU 06</span>
          <span class="lx-raffle-tag">Người khách tử tế nhất</span>
        </div>
        <h3 class="lx-raffle-q">Người khách trả tiền tử tế và dễ chịu nhất của bạn từ trước đến nay đã tìm thấy bạn bằng cách nào?</h3>
        <div class="lx-raffle-ans">
          <b>💡 Gợi mở cách trả lời tại lớp:</b> Lần ngược đường khách đã đi: ai giới thiệu, họ thấy gì trước khi nhắn, câu đầu tiên họ nhắn là gì. Người mới lấy người khách đầu tiên chịu trả đúng giá. Thường bạn sẽ thấy khách tử tế đến vì đã thấy một việc thật, không phải vì một lời mời giảm giá.
        </div>
        <div class="lx-raffle-vid">
          <b>🎬 Dựng thành video 30–60s:</b> Cảnh đầu là tin nhắn đầu tiên của khách đó (xin phép, che tên). Câu mở: <em>"Người khách dễ chịu nhất của em tìm đến chỉ vì một việc em làm hôm ấy."</em>
        </div>
      </div>

      <!-- CÂU 07 -->
      <div class="lx-raffle-card">
        <div class="lx-raffle-top">
          <span class="lx-raffle-num">CÂU 07</span>
          <span class="lx-raffle-tag">Một video duy nhất trong năm</span>
        </div>
        <h3 class="lx-raffle-q">Nếu cả năm chỉ được đăng đúng một video, bạn sẽ chọn quay lại khoảnh khắc nào trong ngày làm việc?</h3>
        <div class="lx-raffle-ans">
          <b>💡 Gợi mở cách trả lời tại lớp:</b> Đừng chọn lúc đẹp nhất. Chọn lúc khó nhất, hoặc lúc nét mặt khách đổi khác: khách soi gương sau ca da, người nhận ôm bó hoa, gia chủ ngồi thử chiếc ghế vừa sửa. Người mới chưa có khoảnh khắc đó thì chọn lúc mình tập lại một bước khó lần thứ mười.
        </div>
        <div class="lx-raffle-vid">
          <b>🎬 Dựng thành video 30–60s:</b> Ba giây đầu là ngay trước khoảnh khắc ấy, để người xem phải chờ xem kết quả. Câu mở: <em>"Nếu chỉ được cho chị xem một phút trong ngày của em, em chọn phút này."</em>
        </div>
      </div>

      <!-- CÂU 08 -->
      <div class="lx-raffle-card">
        <div class="lx-raffle-top">
          <span class="lx-raffle-num">CÂU 08</span>
          <span class="lx-raffle-tag">Sai lầm đắt giá của khách</span>
        </div>
        <h3 class="lx-raffle-q">Khách hay tự làm hỏng điều gì trước khi tìm đến bạn, và sai lầm đó đã làm họ mất bao nhiêu tiền?</h3>
        <div class="lx-raffle-ans">
          <b>💡 Gợi mở cách trả lời tại lớp:</b> Nói cụ thể đến mức có con số: tự mua kem lột tẩy trên mạng rồi tốn mấy tháng phục hồi, cắm hoa vào nước máy để qua đêm, lau bàn gỗ bằng nước tẩy. Người làm lâu cộng cả tiền lẫn thời gian khách đã mất. Người mới hỏi thầy hoặc người quen trong nghề ca sửa hỏng tốn nhất họ từng gặp.
        </div>
        <div class="lx-raffle-vid">
          <b>🎬 Dựng thành video 30–60s:</b> Cảnh đầu đặt món đồ gây hỏng lên bàn, cận nhãn. Câu mở: <em>"Hộp này chỉ vài trăm nghìn, nhưng chị khách tốn gấp nhiều lần để sửa lại."</em>
        </div>
      </div>

      <!-- CÂU 09 -->
      <div class="lx-raffle-card">
        <div class="lx-raffle-top">
          <span class="lx-raffle-num">CÂU 09</span>
          <span class="lx-raffle-tag">Hạ giá vì sợ mất khách</span>
        </div>
        <h3 class="lx-raffle-q">Bạn đã bao giờ hạ giá vì sợ mất khách chưa? Chuyện xảy ra sau đó như thế nào?</h3>
        <div class="lx-raffle-ans">
          <b>💡 Gợi mở cách trả lời tại lớp:</b> Kể thật đoạn sau. Hạ giá thường kéo về người mặc cả, và lần sau phải hạ tiếp. Người mới nhớ lại lần làm rẻ hoặc làm không công cho người quen: họ có quý công mình hơn không, hay coi đó là chuyện đương nhiên.
        </div>
        <div class="lx-raffle-vid">
          <b>🎬 Dựng thành video 30–60s:</b> Cảnh đầu là bảng giá cũ bị gạch, cắt sang việc bạn làm kỹ hơn bây giờ. Câu mở: <em>"Có lần em hạ giá vì sợ mất khách. Đây là chuyện xảy ra sau đó."</em>
        </div>
      </div>

      <!-- CÂU 10 -->
      <div class="lx-raffle-card">
        <div class="lx-raffle-top">
          <span class="lx-raffle-num">CÂU 10</span>
          <span class="lx-raffle-tag">Tin nhắn 1 năm sau</span>
        </div>
        <h3 class="lx-raffle-q">Một năm nữa khi kênh đã vững, bạn muốn một người lạ nhắn cho bạn câu đầu tiên là gì?</h3>
        <div class="lx-raffle-ans">
          <b>💡 Gợi mở cách trả lời tại lớp:</b> Viết đúng nguyên câu ra giấy, ví dụ <em>"Chị ơi da em giống hệt ca chị quay hôm trước"</em> hay <em>"Anh sửa giúp em cái tủ y như cái ghế trong video"</em>. Từ câu đó lần ngược lại: muốn người lạ nói được câu ấy thì tuần này phải quay video nào. Câu trả lời này là bản đồ cho cả năm làm kênh.
        </div>
        <div class="lx-raffle-vid">
          <b>🎬 Dựng thành video 30–60s:</b> Quay đúng loại ca khớp với câu nhắn mong muốn, nói thẳng với người đó. Câu mở: <em>"Nếu da chị đang mỏng đỏ sau khi dùng kem lột, video này dành cho chị."</em>
        </div>
      </div>
    </div>
  </div>
</section>

"""

body = body[:idx_b1] + new_boctham_section + body[idx_b2:]
print("Updated: Section 10 câu hỏi mở bốc thăm đầu giờ (kèm lời giải của Thư ký + lưới 2 cột chuẩn)")

# Thêm nút nhảy nhanh tới #ch-boc-tham trên thanh .lx-jump nếu chưa có
if 'href="#ch-boc-tham"' not in body:
    body = body.replace(
        '<a href="#sec-faq">Câu hỏi thực chiến</a>',
        '<a href="#ch-boc-tham">10 câu bốc thăm</a>\n    <a href="#sec-faq">10 câu hỏi thực chiến</a>'
    )

with open("opus_pack/opus_draft_body.html", "w", encoding="utf-8") as f:
    f.write(body)

print("SUCCESSFULLY WROTE opus_draft_body.html!")
