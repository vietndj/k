#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_opus_updates.py — Cập nhật 9 khối nội dung từ Thư ký (Claude Opus Native) vào opus_draft_body.html
"""
import re

with open('opus_pack/opus_draft_body.html', 'r', encoding='utf-8') as f:
    body = f.read()

# -------------------------------------------------------------
# 1. BẢNG SO SÁNH 4 NGÀNH HỌC VIÊN THỰC TẾ
# -------------------------------------------------------------
old_table_section = r'''    <div class="lx-table-wrap">
      <table class="lx-table">
        <thead>
          <tr><th>Tiêu chí</th><th>Mở đầu kiểu gây sốc</th><th>Mở đầu gọi đúng chỗ kẹt</th></tr>
        </thead>
        <tbody>
          <tr><td>Câu mở (ngành sửa nhà)</td><td class="lx-col-bad">"Đừng lướt nếu bạn sắp sửa nhà!"</td><td class="lx-col-good">"Nhận nhà xong, đêm mưa đầu tiên trần nhà vệ sinh rỉ nước xuống đúng chỗ vừa ốp gạch…"</td></tr>
          <tr><td>Người xem nghĩ gì</td><td>Lại một video câu kéo</td><td>Người này hiểu đúng chuyện nhà mình</td></tr>
          <tr><td>Hành vi sau khi xem</td><td>Cười, lướt tiếp, quên người nói</td><td>Lưu lại, gửi Zalo cho vợ hoặc chồng</td></tr>
          <tr><td>Giọng nói</td><td>Cao, gấp, hét</td><td>Thấp, bình tĩnh, chắc chắn</td></tr>
          <tr><td>Ví dụ minh họa</td><td>50.000 view → 0 lưu → 0 khách</td><td>2.000 view → 200 lưu → 50 gửi Zalo → 5 tin nhắn → 2 hợp đồng</td></tr>
        </tbody>
      </table>
    </div>
    <p class="lx-note">Dòng số liệu cuối là ví dụ minh họa để thấy cơ chế, không phải số đo từ một kênh cụ thể. Điều cần nhớ là hướng đi: ít view hơn nhiều lần nhưng đúng người đang có việc cần làm và có tiền trả.</p>
    <p class="cl-body">Người có tiền không tin người hét. Họ tin người nói nhỏ mà đúng, nên câu mở hay luôn bắt đầu bằng một khoảnh khắc nhìn thấy được (nước rỉ xuống, tay lục ví, giấu tờ hóa đơn vào ngăn kéo), không bắt đầu bằng mệnh lệnh "đừng lướt", "phải xem".</p>'''

new_table_section = r'''    <!-- BẢNG ĐỐI SÁNH 4 NGÀNH HỌC VIÊN THỰC TẾ -->
    <p class="cl-body">Cùng một tiệm, cùng một chiếc điện thoại. Chỉ khác nhau ở đúng câu nói mở đầu, và kết quả thực tế nhận về sẽ rẽ sang hai hướng hoàn toàn đối lập:</p>

    <div class="lx-industry-tabs">
      <!-- NGÀNH 1: HOA TƯƠI -->
      <div class="lx-ind-card">
        <div class="lx-ind-header">
          <span class="lx-ind-icon">🌹</span>
          <strong>Ngành Hoa tươi & Cây cảnh</strong>
        </div>
        <div class="lx-table-wrap">
          <table class="lx-table">
            <thead>
              <tr><th>Tiêu chí</th><th>Mở đầu kiểu gây sốc, hò hét</th><th>Mở đầu gọi đúng chỗ kẹt</th></tr>
            </thead>
            <tbody>
              <tr><td>Câu mở đầu</td><td class="lx-col-bad">"SỐC! Hồng chỉ 5 nghìn một bông, rẻ nhất Hà Nội!!!"</td><td class="lx-col-good">"Bó hồng giao tới tay người nhận chưa được 2 tiếng đã gục cổ. Lỗi không nằm ở hoa, mà ở cái gốc chưa được cắt lại trong nước."</td></tr>
              <tr><td>Người xem nghĩ gì</td><td>"Lại xả hàng. Rẻ thế chắc hoa cũ dập nát."</td><td>"Đúng rồi, lần trước mình đặt tặng bạn cũng gục y như thế."</td></tr>
              <tr><td>Hành vi sau khi xem</td><td>Thả tim cho vui rồi lướt qua</td><td>Lưu lại, nhắn hỏi: "Chiều nay giao kịp bó này không chị?"</td></tr>
              <tr><td>Giọng nói</td><td>Gào to, nhạc giật dồn dập</td><td>Giọng bình thường, như nói với khách đang đứng trước quầy</td></tr>
              <tr><td>Việc thật trong video</td><td>Quay đống hoa, chèn chữ giá đỏ chót</td><td>Cắt chéo gốc dưới vòi nước chảy, tuốt lá dưới mực nước, đặt cạnh bó không cắt gốc sau 2 tiếng</td></tr>
              <tr><td>Con số sau 7 ngày</td><td>40.000 lượt xem · 3 tin hỏi giá · 0 đơn</td><td>3.000 lượt xem · 180 lượt lưu · 25 tin nhắn · 9 đơn chốt</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- NGÀNH 2: LOA ĐÀI ÂM THANH -->
      <div class="lx-ind-card">
        <div class="lx-ind-header">
          <span class="lx-ind-icon">🔊</span>
          <strong>Ngành Loa đài & Âm thanh phòng hát</strong>
        </div>
        <div class="lx-table-wrap">
          <table class="lx-table">
            <thead>
              <tr><th>Tiêu chí</th><th>Mở đầu kiểu gây sốc, hò hét</th><th>Mở đầu gọi đúng chỗ kẹt</th></tr>
            </thead>
            <tbody>
              <tr><td>Câu mở đầu</td><td class="lx-col-bad">"Bộ dàn karaoke đỉnh nhất 2026, hát là phê!"</td><td class="lx-col-good">"Cứ cầm micro lên là loa hú rít chói tai? Chưa chắc do micro. Phần nhiều là đặt loa sai góc, hoặc đấu dây lệch trở kháng, để lâu là cháy con tép."</td></tr>
              <tr><td>Người xem nghĩ gì</td><td>"Quảng cáo, quán nào chả khen dàn hay."</td><td>"Dàn ở nhà mình đang bị đúng tình trạng này."</td></tr>
              <tr><td>Hành vi sau khi xem</td><td>Bình luận chữ "giá?" rồi quên bẵng</td><td>Lưu lại, gửi cho bạn bè, nhắn: "Anh qua xem giúp dàn nhà em với."</td></tr>
              <tr><td>Giọng nói</td><td>Hô to như MC hội chợ sự kiện</td><td>Chậm, rõ, vừa nói vừa cầm đồng hồ chỉ vào cọc dây</td></tr>
              <tr><td>Việc thật trong video</td><td>Bật nhạc xập xình, lia đèn led lòe loẹt</td><td>Đo trở kháng bằng đồng hồ, tháo con tép cháy đen ra đặt lên bàn, đấu lại đúng cọc rồi thử tiếng</td></tr>
              <tr><td>Con số sau 7 ngày</td><td>30.000 lượt xem · 5 tin hỏi vu vơ · 0 đơn</td><td>2.500 lượt xem · 150 lượt lưu · 18 tin nhắn · 6 lịch qua tận nhà</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- NGÀNH 3: XƯỞNG ĐỒ GỖ NỘI THẤT -->
      <div class="lx-ind-card">
        <div class="lx-ind-header">
          <span class="lx-ind-icon">🪵</span>
          <strong>Ngành Xưởng gỗ & Đồ nội thất</strong>
        </div>
        <div class="lx-table-wrap">
          <table class="lx-table">
            <thead>
              <tr><th>Tiêu chí</th><th>Mở đầu kiểu gây sốc, hò hét</th><th>Mở đầu gọi đúng chỗ kẹt</th></tr>
            </thead>
            <tbody>
              <tr><td>Câu mở đầu</td><td class="lx-col-bad">"Nội thất gỗ đẹp nhất, giá rẻ không tưởng!"</td><td class="lx-col-good">"Tủ mới đóng chưa qua một mùa hanh khô, mộng đã nứt toác, cánh cong không đóng nổi? Lỗi có từ lúc xẻ gỗ, chứ không phải lúc lắp."</td></tr>
              <tr><td>Người xem nghĩ gì</td><td>"Rẻ thế chắc lại gỗ pha tạp, ép mùn cưa."</td><td>"Cái tủ bếp nhà mình đúng là cong vênh như vậy."</td></tr>
              <tr><td>Hành vi sau khi xem</td><td>Lướt qua không đọng lại gì</td><td>Lưu lại, nhắn tin hỏi: "Xưởng có qua đo đạc trực tiếp tận nhà không?"</td></tr>
              <tr><td>Giọng nói</td><td>Đọc liến thoắng như rao hàng giảm giá</td><td>Giọng thợ mộc mạc, tay vẫn cầm thước đo ván gỗ</td></tr>
              <tr><td>Việc thật trong video</td><td>Lia máy lướt qua cả phòng mẫu bóng bẩy</td><td>Cầm hai tấm ván cùng một cây gỗ: tấm xẻ đúng thớ phẳng lì, tấm xẻ ngang thớ đã vênh, soi vân thớ cho người xem thấy</td></tr>
              <tr><td>Con số sau 7 ngày</td><td>25.000 lượt xem · 2 tin nhắn hỏi giá · 0 hợp đồng</td><td>2.000 lượt xem · 140 lượt lưu · 12 tin hẹn đo · 3 hợp đồng ký thật</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- NGÀNH 4: SPA LÀM ĐẸP -->
      <div class="lx-ind-card">
        <div class="lx-ind-header">
          <span class="lx-ind-icon">💆</span>
          <strong>Ngành Spa, Chăm sóc da & Trị liệu</strong>
        </div>
        <div class="lx-table-wrap">
          <table class="lx-table">
            <thead>
              <tr><th>Tiêu chí</th><th>Mở đầu kiểu gây sốc, hò hét</th><th>Mở đầu gọi đúng chỗ kẹt</th></tr>
            </thead>
            <tbody>
              <tr><td>Câu mở đầu</td><td class="lx-col-bad">"Trắng bật tông sau 1 liệu trình, cam kết 100%!"</td><td class="lx-col-good">"Peel xong, mụn mủ bùng khắp hai má. Chưa chắc là da đang 'đẩy độc'. Có khi da đã mỏng sẵn vì dùng kem trộn, và việc cần làm là dừng peel ngay."</td></tr>
              <tr><td>Người xem nghĩ gì</td><td>"Lại hứa hẹn trên trời. Ai biết thật hay giả."</td><td>"Mặt mình đang y hệt thế này, may mà chưa đi peel tiếp buổi 2."</td></tr>
              <tr><td>Hành vi sau khi xem</td><td>Bình luận chữ "giá?" cho có lệ</td><td>Lưu lại, chụp ảnh da gửi tin nhắn riêng: "Chị ơi da em thế này có cần đi soi không?"</td></tr>
              <tr><td>Giọng nói</td><td>Giọng cao vút, dồn dập, ép khách chốt</td><td>Nhỏ nhẹ, điềm tĩnh, chắc chắn, như đang ngồi tư vấn cạnh giường khách</td></tr>
              <tr><td>Việc thật trong video</td><td>Lấy ảnh trước–sau chỉnh màu láng mịn</td><td>Soi da dưới đèn thật, chỉ từng vùng da mỏng đỏ giãn mao mạch, giải thích vì sao cai kem có corticoid phải đi từng bước có người theo sát</td></tr>
              <tr><td>Con số sau 7 ngày</td><td>60.000 lượt xem · nhiều bình luận 'giá' · 1 khách</td><td>4.000 lượt xem · 220 lượt lưu · 30 tin nhắn gửi ảnh da · 8 lịch soi da đặt trước</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <p class="lx-note">Các con số trên là ví dụ minh họa để thấy rõ độ chênh lệch về chất lượng chuyển đổi, không phải số đo của riêng một học viên cụ thể. Điểm mấu chốt cần nhớ: Video hò hét đếm bằng lượt xem ảo; video gọi đúng chỗ kẹt đếm bằng tin nhắn và lịch hẹn thật.</p>
    <p class="cl-body">Người có tiền không tin người hét. Họ tin người nói nhỏ mà trúng. Câu mở đầu hay luôn bắt đầu bằng một khoảnh khắc nhìn thấy được ngoài đời thực (hoa gục cổ, tiếng loa rít, mộng gỗ nứt toác, da đỏ ửng), chứ không bao giờ bắt đầu bằng khẩu hiệu "đừng lướt" hay "phải xem".</p>'''

assert old_table_section in body, "old_table_section not found!"
body = body.replace(old_table_section, new_table_section)
print("Updated: Section 1 (4 ngành)")

# -------------------------------------------------------------
# 2. CUỐN SỔ BIÊN LAI MỒ HÔI (MỤC ③)
# -------------------------------------------------------------
old_proof = r'''      <div class="lx-proof__card">
        <h4>③ Cuốn sổ biên lai mồ hôi</h4>
        <p>Sự tự tin không đến từ câu tự nhủ trước gương. Mỗi việc làm trọn đến cuối là một tờ biên lai, và cái đầu chỉ tin vào sổ biên lai đó. Bác thợ mộc tự chui xuống gầm bàn đánh giấy ráp nhẵn chỗ không ai nhìn, nên khách lật bàn lên soi bác vẫn bình thản.</p>
        <p>Kho video quay việc thật là cuốn sổ biên lai công khai của bạn.</p>
        <small>Logic 36 · Logic 40</small>
      </div>'''

new_proof = r'''      <div class="lx-proof__card">
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
      </div>'''

assert old_proof in body, "old_proof not found!"
body = body.replace(old_proof, new_proof)
print("Updated: Section 2 (Cuốn sổ biên lai mồ hôi)")

# -------------------------------------------------------------
# 3. BÀI TẬP NGÀY MAI + LINK TINA NGUYỄN
# -------------------------------------------------------------
old_exercise = r'''    <div class="highlight-rule">Bài tập ngày mai: dựng điện thoại ở góc chéo bàn, ghi lại cả ngày làm việc thật, cuối ngày cắt riêng 90 giây lúc bạn trả lời câu hỏi khó nhất của khách, nhớ che tên khách.</div>'''

new_exercise = r'''    <div class="highlight-rule">
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
    </div>'''

assert old_exercise in body, "old_exercise not found!"
body = body.replace(old_exercise, new_exercise)
print("Updated: Section 3 (Bài tập ngày mai + link Tina)")

# -------------------------------------------------------------
# 4. VLOG ĐỜI TƯ VS VIDEO VIỆC THẬT (BỎ NÉN THỜI GIAN)
# -------------------------------------------------------------
old_vlog = r'''    <p class="cl-body">Quay việc thật cũng không phải làm vlog kể sáng nay uống cà phê gì. Vlog đời tư kể chuyện của mình, còn video việc thật trao cho người xem một bài học đã nén sẵn thời gian. Chỗ khác nhau nằm ở câu người xem tự hỏi trong đầu: "Xem cái này tôi được gì?" Hễ câu trả lời là "được bớt cả ngày tự mò", họ ở lại.</p>'''

new_vlog = r'''    <p class="cl-body">Quay việc thật không phải làm vlog.</p>
    <p class="cl-body">Vlog đời tư kể "sáng nay tôi ăn gì, đi đâu, gặp ai". Người xem lướt qua cho vui, mai đã quên.</p>
    <p class="cl-body">Video việc thật gỡ đúng một chỗ người xem đang kẹt. Nó giúp họ khỏi mất cả tuần tự mò, khỏi mất tiền oan thêm một lần.</p>
    <p class="cl-body">Hai loại khác nhau ở đúng một câu người xem tự hỏi trong đầu: <strong>"Xem cái này, việc của tôi có xong được không?"</strong></p>
    <p class="cl-body">Trả lời được "có" thì họ lưu lại, và họ quay lại tìm bạn.</p>'''

assert old_vlog in body, "old_vlog not found!"
body = body.replace(old_vlog, new_vlog)
print("Updated: Section 4 (Vlog vs Việc thật)")

# -------------------------------------------------------------
# 5. LÁT CẮT VI MÔ TÂY SƠN (NGÔI THỨ NHẤT: MÌNH / TÔI)
# -------------------------------------------------------------
old_story = r'''    <p class="cl-body">Anh Việt từng kể một khoảnh khắc như vậy: cuối tháng nhìn báo cáo thấy tiền quảng cáo ngốn 80% doanh thu, trừ hết chi phí chỉ còn 10% về túi, sau 15 năm làm giáo dục mà ngồi nuốt nước bọt khan không nói nên lời. Vì đó là trải nghiệm thật nên kể lại rất sống, và người làm chủ nghe đúng khoảnh khắc ấy thì tự tin rằng người kể có cách gỡ cho mình.</p>'''

new_story = r'''    <p class="cl-body">Khóa học đầu tiên mình mở, nhìn doanh thu thì mừng. Ngồi cộng lại mới thấy tiền chạy quảng cáo đã ngốn mất 80%. Trừ thêm tiền phòng, thiết bị, người hỗ trợ, trong túi còn sót lại chừng 10%.</p>
    <p class="cl-body">Buổi cuối gặp anh chị em học viên, ai cũng quý, ai cũng vui, mình cũng vui. Nhưng bước ra khỏi lớp thì thấy một thứ khó gọi tên, vừa bất lực vừa chua xót. Mồ hôi của mình, tiền học viên dành dụm đóng học, phần lớn đã chảy về nền tảng và người chạy quảng cáo.</p>
    <p class="cl-body">Tối hôm ấy trời mưa lất phất. Mình xách cái túi to đựng chân máy với đèn quay, nặng trĩu một bên vai, đi bộ dọc phố Tây Sơn đang tắc cứng. Còi xe inh ỏi, nước mưa hắt vào túi. Trong đầu vừa nhớ tiếng cười trong lớp, vừa thấy động lực làm tiếp như cạn đáy.</p>
    <p class="cl-body">Đi hết đoạn phố ấy, mình nghĩ thông một chuyện. Mình không thể bám mãi vào câu "tôi là giáo viên, tôi chỉ lo đứng lớp dạy cho hay". Quảng cáo và cách làm nội dung quyết định tám phần chuyện sống còn. Đứng ngoài cuộc chơi đó, mười lăm năm làm giáo dục của mình cũng chỉ là đi làm thuê cho thuật toán.</p>
    <p class="cl-body">Từ hôm đó mình tự cầm máy. Không phải để nổi tiếng, mà để tự nói bằng việc thật của mình, khỏi phải trả 80% cho người khác nói hộ.</p>'''

assert old_story in body, "old_story not found!"
body = body.replace(old_story, new_story)
print("Updated: Section 5 (Chuyện phố Tây Sơn - ngôi mình)")

# -------------------------------------------------------------
# 6. KHUNG 30 GIÂY THỰC HÀNH CHO NGƯỜI MỚI (BỘ KỊCH BẢN TRỰC QUAN)
# -------------------------------------------------------------
old_tools = r'''    <div class="lx-links">
      <a href="https://ytuong.fedu.vn" target="_blank" rel="noopener">Kho định dạng quốc tế ↗</a>
      <a href="https://fedu.vn/course/3congcu.html" target="_blank" rel="noopener">Bộ 3 công cụ AI viết kịch bản ↗</a>
    </div>'''

new_tools = r'''    <!-- KHUNG KỊCH BẢN THỰC HÀNH 30S TRỰC QUAN -->
    <div class="lx-script-box" style="margin: 28px 0; padding: 24px; background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
      <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; color: #1a56db; letter-spacing: 0.05em; margin-bottom: 6px;">KHUNG THỰC HÀNH TẠI LỚP & TẠI TIỆM</div>
      <h4 style="margin: 0 0 12px 0; font-size: 20px; color: #0f172a;">Kịch bản 30 giây cho người mới (Cơ chế 5 nhịp thực chiến)</h4>
      <p class="cl-body" style="margin-bottom: 16px;">Để người mới không bị đơ trước máy quay, quy trình chia làm 2 bước cực kỳ nhẹ nhàng:</p>

      <div style="background: #f8fafc; padding: 16px; border-radius: 8px; margin-bottom: 18px; border-left: 4px solid #1a56db;">
        <strong style="color: #0f172a; display: block; margin-bottom: 6px;">Bước 1: Trả lời 4 câu hỏi sự thật (nói vào voice điện thoại hoặc ghi ra giấy):</strong>
        <ol style="margin: 0 0 0 20px; padding: 0; line-height: 1.6; color: #334155;">
          <li>Tuần này khách hỏi bạn câu gì nhiều nhất?</li>
          <li>Khách hay tự làm hỏng ở đâu trước khi tìm đến bạn?</li>
          <li>Bạn làm khác người khác ở đúng một bước nào, và vì sao?</li>
          <li>Nếu khách chỉ nhớ được một câu của bạn, đó là câu gì?</li>
        </ol>
      </div>

      <div style="margin-bottom: 16px;">
        <strong style="color: #0f172a; display: block; margin-bottom: 8px;">Bước 2: Đổ câu trả lời vào khung 5 nhịp (85–92 tiếng ≈ 29 giây)</strong>
        <div class="lx-table-wrap">
          <table class="lx-table" style="font-size: 14px;">
            <thead>
              <tr><th>Nhịp</th><th>Thời lượng</th><th>Cỡ cảnh hình ảnh</th><th>Lời mẫu thực tế (Ví dụ tiệm hoa)</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Câu 1</strong></td><td>6 giây</td><td>Nhìn thẳng ống kính</td><td>"Hoa hồng giao đến tay người nhận mà gục cổ, chín phần mười là do cái gốc."</td></tr>
              <tr><td><strong>Câu 2</strong></td><td>6 giây</td><td>Mở laptop/sổ đơn, xem số liệu</td><td>"Tháng trước tiệm mình nhận mười hai cuộc gọi phàn nàn, mười một cuộc cùng một lỗi."</td></tr>
              <tr><td><strong>Câu 3</strong></td><td>6 giây</td><td>Quay qua vai, cận tay đang cắt gốc</td><td>"Gốc phải cắt chéo ngay dưới vòi nước chảy, để không khí không lọt vào thân hoa."</td></tr>
              <tr><td><strong>Câu 4</strong></td><td>6 giây</td><td>Nhấp ngụm nước/cà phê, đọc đè lên hình</td><td>"Cắt trên mặt bàn khô thì đầu gốc hút khí, tắc lại, hoa có cắm nước cũng không uống được."</td></tr>
              <tr><td><strong>Câu 5</strong></td><td>5 giây</td><td>Nhìn thẳng ống kính, chốt lời khuyên</td><td>"Hoa về đến nhà, việc đầu tiên là cắt lại gốc trong chậu nước nhé."</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="highlight-rule" style="margin: 12px 0 0 0; background: #eff6ff; border-color: #3b82f6;">
        <strong>Bí quyết giảm áp lực cho người sợ ống kính:</strong> Bạn chỉ cần học thuộc lòng <strong>Câu 1 và Câu 5</strong> (chỉ mất ~12 giây nhìn máy). Toàn bộ <strong>Câu 2, Câu 3, Câu 4</strong> cứ cầm giấy đọc thoải mái như lồng tiếng, vì lúc đó hình ảnh đã được phủ trọn bởi cảnh tay làm, mở laptop hoặc nhấp ngụm cà phê, không ai nhìn thấy mắt bạn.
      </div>
    </div>

    <div class="lx-links">
      <a href="https://ytuong.fedu.vn" target="_blank" rel="noopener">Kho định dạng quốc tế ↗</a>
      <a href="https://fedu.vn/course/3congcu.html" target="_blank" rel="noopener">Bộ công cụ kịch bản 2.0 ↗</a>
    </div>'''

assert old_tools in body, "old_tools not found!"
body = body.replace(old_tools, new_tools)
print("Updated: Section 6 (Khung kịch bản 30s)")

# -------------------------------------------------------------
# 7. BA KHỐI HỌC VIÊN THỰC TẾ (ĐẶNG HƯỜNG, THẮM THỎ, TÂNG XINH)
# -------------------------------------------------------------
old_cases_intro = r'''    <h3 class="lx-h3">Dẫn chứng từ học viên thật tại các lớp Offline</h3>
    <p class="cl-body">Khi đã qua đủ lô, kết quả hiện ra ở những người kiên trì quay việc thật. Chị Tâng Xinh (Tâng Xinh Diamond) — học viên lớp Offline, người kinh doanh hệ thống có tiếng — đã từng trải qua giai đoạn video nhiều người xem nhưng phải đưa về đúng bài toán thực tế: không phải cần thêm view, mà cần đúng người hỏi mua. Các anh chị khác ở lớp K3, K4 — người làm nội thất, spa, xưởng đồ gỗ, cửa hàng hoa, bán loa đài âm thanh — cũng đi qua đúng quá trình này: tháng đầu ít tương tác, vài tháng sau bắt đầu nhận tin nhắn "Em theo dõi anh/chị lâu rồi" từ những người chưa bao giờ bấm like.</p>
    <div class="lx-cases">
      <a class="lx-case" href="https://kenh.fedu.vn/09-case.html">
        <b>Chị Tâng Xinh — Tâng Xinh Diamond</b>
        <span>Kinh doanh hệ thống · Học viên Offline</span>
        <strong>Bài toán thật</strong>
      </a>
      <a class="lx-case" href="https://kenh.fedu.vn/09-case.html">
        <b>Học viên ngành Nội thất & Đồ gỗ</b>
        <span>Lớp K3, K4 · Quay xưởng mỗi ngày</span>
        <strong>Tin nhắn đều</strong>
      </a>
      <a class="lx-case" href="https://kenh.fedu.vn/09-case.html">
        <b>Học viên ngành Spa & Loa đài</b>
        <span>Lớp K4 · Từ 0 tương tác đến khách tự tìm</span>
        <strong>Khách chất lượng</strong>
      </a>
    </div>'''

new_cases_intro = r'''    <h3 class="lx-h3">Dẫn chứng từ ba học viên thật tại các lớp Offline</h3>
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
        <p style="font-size: 13px; color: #475569; margin: 6px 0; line-height: 1.4;">Dựng lại kịch bản cho cả hệ thống dựa trên những video chia sẻ giá trị thật, không câu lượt xem ảo. Đưa kênh về đúng mục tiêu chuyển đổi doanh số.</p>
        <strong style="color: #15803d;">Video ra đơn thật</strong>
      </a>
    </div>'''

assert old_cases_intro in body, "old_cases_intro not found!"
body = body.replace(old_cases_intro, new_cases_intro)
print("Updated: Section 7 (3 học viên thật)")

# -------------------------------------------------------------
# 8. GIÁ CAO, TRẦN VẬT LÝ & TRIẾT LÝ BẢN 4 K4
# -------------------------------------------------------------
old_high_price = r'''    <h3 class="lx-h3">Ngành dịch vụ có trần vật lý: dùng kênh làm bộ lọc, không làm cái loa gọi khách đại trà</h3>
    <p class="cl-body">Một bác sĩ, thợ sửa nhà, chủ spa hay người kèm 1-1 chỉ có chừng ấy giờ làm trực tiếp mỗi ngày. Thu nhập bị chặn trần: khám thêm bao nhiêu người cũng không vượt được 24 giờ. Kênh kéo về nhiều khách hơn mà giờ làm không đổi thì chỉ làm bạn kiệt sức nhanh hơn.</p>
    <p class="cl-body">Nên với ngành dịch vụ cá nhân, kênh làm việc của một bộ lọc. Nội dung càng sát việc thật, khách không hợp càng tự rời đi, khách hiểu giá trị càng tự tìm đến. Một bài tập đơn giản: lấy mức giá bạn đang thu, thêm một số 0 phía sau, rồi liệt kê 5 việc chăm sóc tận tay khiến khách thấy hời ở mức giá mới. Thu 100 triệu để kèm một người, đến tận nơi, đi khảo sát cùng, chỉ cần 5 khách là đủ 500 triệu.</p>
    <p class="cl-body">Giá cao còn có một tác dụng ít ai để ý: nó ép bạn bỏ mẹo vặt để đào sâu vào đúng trăn trở vận hành của người làm chủ, vì treo giá cao mà vẫn đăng mẹo bề nổi thì không bán được đơn nào. Chính nội dung điềm tĩnh, trúng việc thật đó lại lọc đúng người có tiền tự tìm đến, và biên lãi rộng cho bạn thời gian chăm từng người kỹ hơn.</p>'''

new_high_price = r'''    <h3 class="lx-h3">Ngành dịch vụ có trần vật lý: Giá cao không phải hét giá, mà là bộ lọc chọn đúng người</h3>
    <p class="cl-body">Bán giá cao không phải là mánh khóe hét giá cho oai.</p>
    <p class="cl-body">Khi đứng lớp với những anh chị học viên có cơ sở thật, có khách thật, có tiền thật ngoài đời, chính người dạy lại học được nhiều điều giá trị nhất. Mỗi câu hỏi thực tế của họ là một ca việc thật gai góc, không một cuốn sách vở giáo khoa nào chép sẵn.</p>
    <p class="cl-body">Một bác sĩ, người sửa nhà, chủ spa hay chuyên gia tư vấn chỉ có chừng ấy giờ làm trực tiếp mỗi ngày. Thu nhập luôn bị chặn trần vật lý: một ngày không thể có quá 24 tiếng. Nếu kênh cứ kéo về một lượng khách đại trà ham rẻ, bạn sẽ chỉ kiệt sức nhanh hơn mà chất lượng phục vụ ngày càng đi xuống.</p>
    <p class="cl-body">Video việc thật chính là một cái rây tự nhiên. Người chỉ chực chờ săn đồ rẻ xem video thấy "nhiều chữ, kỹ tính quá" rồi sẽ tự bỏ đi. Người còn ở lại xem hết là người biết trân trọng sự tử tế, cần sự an tâm tuyệt đối, và sẵn lòng trả đúng giá cho tay nghề của bạn.</p>
    <p class="cl-body"><strong>Giá cao không bao giờ đuổi khách. Nó làm nhiệm vụ chọn lọc đúng người khách trân quý bạn.</strong></p>'''

assert old_high_price in body, "old_high_price not found!"
body = body.replace(old_high_price, new_high_price)
print("Updated: Section 8 (Giá cao & Triết lý Bản 4)")

# -------------------------------------------------------------
# 9. BỘ 10 CÂU HỎI BỐC THĂM ĐẦU GIỜ CHO LỚP OFFLINE
# -------------------------------------------------------------
boctham_html = r'''
<!-- 10 CÂU HỎI BỐC THĂM ĐẦU GIỜ CHO LỚP OFFLINE -->
<section class="cl-zebra-section" id="ch-boc-tham" style="background: #f1f5f9; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; padding: 48px 0;">
  <div class="cl-sec-container cl-sec-container--wide">
    <div class="cl-badge" style="background: #0f172a; color: #f8fafc;">BỐC THĂM ĐẦU GIỜ · LỚP OFFLINE</div>
    <h2 class="title-short">10 câu hỏi mở bốc thăm đầu giờ<br/>Ai cũng có chuyện thật để kể</h2>
    <p class="cl-body">Bộ câu hỏi mở dành cho buổi gặp mặt đầu tiên tại lớp Offline. Dù bạn là người chưa từng cầm máy quay hay đã có kênh hàng chục nghìn người theo dõi, rút một lá thăm bất kỳ đều sẽ khơi mở ngay một câu chuyện nghề sâu sắc để cả bàn cùng trao đổi:</p>

    <div class="lx-cards" style="margin-top: 24px;">
      <div class="lx-card" style="border-left: 4px solid #1a56db;">
        <span class="lx-card__num" style="color: #1a56db;">01</span>
        <h4 style="font-size: 17px; margin-bottom: 6px;">Câu hỏi quen thuộc nhất</h4>
        <p>Câu nào khách hỏi bạn nhiều đến mức đang ngủ bạn cũng trả lời được?</p>
      </div>

      <div class="lx-card" style="border-left: 4px solid #1a56db;">
        <span class="lx-card__num" style="color: #1a56db;">02</span>
        <h4 style="font-size: 17px; margin-bottom: 6px;">Lần mất khách đáng nhớ</h4>
        <p>Lần gần nhất bạn mất một người khách, lý do thật sự sâu xa theo bạn là gì?</p>
      </div>

      <div class="lx-card" style="border-left: 4px solid #1a56db;">
        <span class="lx-card__num" style="color: #1a56db;">03</span>
        <h4 style="font-size: 17px; margin-bottom: 6px;">Video khiến bạn phải bấm lưu</h4>
        <p>Video gần nhất của người khác khiến bạn bấm nút lưu lại là video gì? Vì sao bạn lưu?</p>
      </div>

      <div class="lx-card" style="border-left: 4px solid #1a56db;">
        <span class="lx-card__num" style="color: #1a56db;">04</span>
        <h4 style="font-size: 17px; margin-bottom: 6px;">Nỗi sợ trước ống kính</h4>
        <p>Nếu bật máy quay ngay bây giờ, bạn sợ nhất điều gì: sợ mặt mình, sợ giọng mình, hay sợ người quen xem?</p>
      </div>

      <div class="lx-card" style="border-left: 4px solid #1a56db;">
        <span class="lx-card__num" style="color: #1a56db;">05</span>
        <h4 style="font-size: 17px; margin-bottom: 6px;">Bước làm nghề khác biệt</h4>
        <p>Có bước nào trong nghề bạn làm cẩn thận khác hẳn người khác mà khách bình thường không hề biết?</p>
      </div>

      <div class="lx-card" style="border-left: 4px solid #1a56db;">
        <span class="lx-card__num" style="color: #1a56db;">06</span>
        <h4 style="font-size: 17px; margin-bottom: 6px;">Người khách tuyệt vời nhất</h4>
        <p>Người khách trả tiền tử tế và dễ chịu nhất của bạn từ trước đến nay đã tìm thấy bạn bằng cách nào?</p>
      </div>

      <div class="lx-card" style="border-left: 4px solid #1a56db;">
        <span class="lx-card__num" style="color: #1a56db;">07</span>
        <h4 style="font-size: 17px; margin-bottom: 6px;">Một video duy nhất trong năm</h4>
        <p>Nếu cả năm chỉ được đăng đúng một video, bạn sẽ chọn quay lại khoảnh khắc nào trong ngày làm việc?</p>
      </div>

      <div class="lx-card" style="border-left: 4px solid #1a56db;">
        <span class="lx-card__num" style="color: #1a56db;">08</span>
        <h4 style="font-size: 17px; margin-bottom: 6px;">Sai lầm đắt giá của khách</h4>
        <p>Khách hay tự làm hỏng điều gì trước khi tìm đến bạn, và sai lầm đó đã làm họ mất bao nhiêu tiền?</p>
      </div>

      <div class="lx-card" style="border-left: 4px solid #1a56db;">
        <span class="lx-card__num" style="color: #1a56db;">09</span>
        <h4 style="font-size: 17px; margin-bottom: 6px;">Hạ giá để giữ khách</h4>
        <p>Bạn đã bao giờ hạ giá vì sợ mất khách chưa? Chuyện xảy ra sau đó như thế nào?</p>
      </div>

      <div class="lx-card" style="border-left: 4px solid #1a56db;">
        <span class="lx-card__num" style="color: #1a56db;">10</span>
        <h4 style="font-size: 17px; margin-bottom: 6px;">Tin nhắn mong đợi 1 năm sau</h4>
        <p>Một năm nữa khi kênh đã vững, bạn muốn một người lạ nhắn cho bạn câu đầu tiên là gì?</p>
      </div>
    </div>
  </div>
</section>
'''

marker_faq = '<!-- 10 CÂU HỎI ĐẮT GIÁ -->'
assert marker_faq in body, "marker_faq not found!"
body = body.replace(marker_faq, boctham_html + '\n' + marker_faq)
print("Updated: Section 9 (10 câu bốc thăm đầu giờ)")

with open('opus_pack/opus_draft_body.html', 'w', encoding='utf-8') as f:
    f.write(body)

print("ALL 9 SECTIONS UPDATED IN opus_draft_body.html SUCCESSFULLY!")
