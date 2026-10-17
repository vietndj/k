import re

with open('logic08.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update title from 7 to 12
content = content.replace("7 BẪY ẢO GIÁC", "12 BẪY ẢO GIÁC")

# 2. Thêm TOC
toc_insertion = """<li><a class="ink-toc-link" href="#q38">Q8. Hoang tưởng sáng tạo</a></li>
<li><a class="ink-toc-link" href="#q39">Q9. Cớ "chờ hoàn hảo"</a></li>
<li><a class="ink-toc-link" href="#q40">Q10. Máy báo tử</a></li>
<li><a class="ink-toc-link" href="#q41">Q11. Thị trường đại trà</a></li>
<li><a class="ink-toc-link" href="#q42">Q12. Lái xe bịt mắt</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 3. Thêm Nội dung
qa_content = """
<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q38" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 8: CƠN HOANG TƯỞNG SÁNG TẠO<br>Đăng video mỗi ngày thì phải vắt não nghĩ ra 365 kịch bản mới lạ, độc đáo để khán giả không bị nhàm chán, đúng không?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Đó là sự kiêu ngạo của kẻ tay ngang! Khán giả mạng lướt trong trạng thái vô thức, chả ai rảnh để nhớ hôm qua bạn nói câu gì. Đỉnh cao của các bậc thầy Youtuber không phải là nặn ra hàng trăm ý tưởng rác, mà là: <strong>Tìm ĐÚNG 1 thông điệp cốt lõi (Vốn trí tuệ), và nhai đi nhai lại nó qua 11 lăng kính khác nhau.</strong><br>Ed Sheeran quanh năm chỉ hát bài của anh ấy mà khán giả vẫn gào thét rách họng. Sự lặp lại định hình quyền uy, cố tỏ ra sáng tạo chỉ đẻ ra sự hỗn loạn.</p>
<blockquote>
<p><em>Cứ lo sáng tạo trăm đường,<br/>Chỉ cần một lõi tỏ tường vạn lần.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q39" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 9: BỆNH VIỆN CỚ "CHỜ HOÀN HẢO"<br>Tôi sợ ống kính, nói hay vấp. Nên tôi sẽ chờ set-up xong studio xịn, học khóa diễn thuyết cho phong thái hoàn hảo rồi mới quay để bảo vệ hình ảnh, chuẩn chứ?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Hoàn hảo là vỏ bọc của sự hèn nhát! Sự sợ hãi camera không phải bệnh tâm lý, dưới góc nhìn khoa học, nó chỉ là <strong>"Kích thước mẫu" (Sample Size) bằng 0</strong>. Não bộ không thể tự tin nếu thiếu dữ liệu cọ xát.<br>Cắn răng bật điện thoại lên, mặt đơ cũng được, quay 30 video rác rưởi đầu tiên để phá băng. Vượt mốc 150 clip, khí chất chuyên gia tự toát ra bóp nghẹt khung hình. Bậc thầy hài độc thoại triệu đô trên Netflix đều bắt đầu từ những quán nhậu mạt rệp 40 người xem. Đợi studio xịn thì đối thủ đã cướp sạch khách!</p>
<blockquote>
<p><em>Ngồi chờ hoàn hảo hụt hơi,<br/>Làm liều ba chục đổi đời vinh quang.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q40" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 10: SỰ KIÊU KỲ CỦA KẺ BỎ QUÊN MÁY BÁO TỬ<br>Tôi bận làm sếp, 1 tuần đăng 1 clip xịn là được rồi. Đăng mỗi ngày hóa ra tôi thành thằng làm content dạo à?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Hãy tưởng tượng trên bàn bạn có một "Chiếc điện thoại ma thuật", cứ nhấc lên là nó tự động gọi thẳng cho 100 khách hàng VIP đang khao khát mua đồ, bạn sẽ nhấc mấy lần? Sẽ nhấc điên cuồng!<br>Mỗi lần bạn tải 1 clip lên, Thuật toán Semantic AI chính là chiếc điện thoại đó, nó tự bốc máy gọi thẳng cho hàng trăm khách mục tiêu. Khẳng định của Daniel Priestley: Đăng video chính là gọi điện (Autodial). Kẻ kiếm tiền không quan tâm sĩ diện rởm, họ chỉ quan tâm dòng tiền. Càng lười đăng, bạn càng tự cắt đứt đường dây liên lạc!</p>
<blockquote>
<p><em>Ngồi lười viện cớ để ngưng,<br/>Đăng bài bốc máy tưng bừng hốt đô.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q41" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 11: ẢO MỘNG HỐT TRỌN THỊ TRƯỜNG ĐẠI TRÀ<br>Sản phẩm của tôi (rèm che, phần mềm...) ai cũng xài được. Tôi sẽ làm video hô to: "Ai muốn mua cái này không?" để hốt trọn thị trường đại chúng, tối ưu quá đúng không?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Tối ưu để... đi ăn mày! Giữa đám đông 100 người, chỉ có đúng 2 người "Sẵn sàng tìm giải pháp" (Solution-aware). Hô to tính năng sản phẩm là bạn tự vứt bỏ 98 người còn lại.<br>Vũ khí đoạt mạng là phải <strong>"Bới móc nỗi đau" (Problem-aware)</strong>. Đổi kịch bản thành: <em>"Ai đang phát điên vì rắc rối này phá nát công ty/gia đình?"</em>. Lập tức 80 người sẽ quay ngoắt lại nhìn bạn như đấng cứu thế. Kẻ nghiệp dư đi khoe thuốc, bậc thầy đi xát muối vào vết thương!</p>
<blockquote>
<p><em>Rao hàng bề mặt thờ ơ,<br/>Xoáy sâu nỗi khổ khách chờ nộp tiền.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q42" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 12: LÁI XE BỊT MẮT (TƯ DUY THIẾT KẾ NGƯỢC)<br>Khí thế quá! Mai tôi xách máy ra quay bão táp 11 video ngắn câu view trước, lùa được đông người rồi tôi mới tính làm phễu Video dài và Form trắc nghiệm sau, chuẩn quy trình chưa?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Chuẩn để đâm xuống vực! Đó là cầm cày đi trước con trâu. Bậc thầy luôn dùng cỗ máy <strong>"Thiết Kế Ngược" (Reverse Engineering)</strong>.<br>CẤM TUYỆT ĐỐI bật máy quay nếu chưa vạch lùi từ đích: (1) Định chốt Gói Dịch vụ giá cao nào cuối cùng? (Offer) ➡️ (2) Đặt Bài Trắc nghiệm nào để tóm được bọn có tiền mua nó? (Lead Form) ➡️ (3) Video dài nào đủ sức tẩy não chúng điền Form? ➡️ (4) Cuối cùng mới tính 11 Video ngắn nào lùa chúng vào bẫy. Chưa thấy rõ điểm rơi của tiền mà đã xách máy đi quay là sự nỗ lực mù quáng!</p>
<blockquote>
<p><em>Cắm đầu quay đại cho xong,<br/>Đi lùi thiết kế mới mong hốt tiền.</em></p>
</blockquote>
</div>
</div>
"""

content = content.replace('<p><em>(Hệ thống đã mã hóa 11 rãnh', qa_content + '\n<p><em>(Hệ thống đã mã hóa 11 rãnh')

with open('logic08.html', 'w', encoding='utf-8') as f:
    f.write(content)

