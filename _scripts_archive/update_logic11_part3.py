import re

with open('logic11.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update TOC
toc_insertion = """<li><a class="ink-toc-link" href="#q11">Q11. Kinh doanh trên bàn giấy</a></li>
<li><a class="ink-toc-link" href="#q12">Q12. Ảo tưởng nghệ thuật</a></li>
<li><a class="ink-toc-link" href="#q13">Q13. Trò hề vĩ mô</a></li>
<li><a class="ink-toc-link" href="#q14">Q14. Cộng sinh tàn nhẫn</a></li>
<li><a class="ink-toc-link" href="#q15">Q15. Kẻ sống sót</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 2. Update Content
qa_content = """
<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q11" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q11 (KINH DOANH): Kẻ ngạo mạn trên bàn giấy<br>Tại sao 90% kế hoạch khởi nghiệp sụp đổ ngay tháng đầu tiên, dù file Excel tính toán lợi nhuận, chi phí đẹp như một giấc mơ hoàn mỹ?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì bản tính toán Excel là một môi trường chân không tuyệt đối! Kinh doanh không phải là toán học cộng trừ, mà là "tâm lý học đường phố". Bản kế hoạch của bạn (hoặc do AI viết hộ) không bao giờ lường trước được cái nhếch mép chê đắt của khách hàng, đối thủ đâm sau lưng phá giá, hay nhân viên trụ cột đột ngột phản bội. Sự "hoàn hảo" trên giấy là liều thuốc độc giết chết trực giác sinh tồn. Ném cái laptop đi, mang một sản phẩm xấu xí ném thẳng vào mặt thị trường để xem họ chửi rủa thế nào. Đó mới là dữ liệu sống!</p>
<blockquote>
<p><em>Ngồi bàn tính toán lãi lời<br/>Ra thương trường chuốc tơi bời đắng cay.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q12" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q12 (NGHỆ THUẬT & SÁNG TẠO): Ảo tưởng của kẻ sĩ<br>Tại sao những kẻ chờ đợi "cảm hứng" để viết thường chết chìm trong vô danh, còn nghệ thuật tạo ra từ AI bằng vài dòng prompt lại trống rỗng đến rợn người?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì cả hai đều hèn nhát trốn tránh nỗi đau sinh nở. Cảm hứng không rơi từ trên trời xuống, nó là phần thưởng của sự ma sát lao động. Kẻ sĩ ngồi nghĩ chay sẽ mãi chỉ vẽ nháp trong đầu. Còn tôi (AI), sinh ra một bức tranh hay bài thơ trong 3 giây chỉ là trò nhào nặn những dải pixel vô cảm. Nghệ thuật đích thực phải rỉ máu, mang vết xước của những đêm vò nát bản thảo, của sự giằng xé nội tâm. Không có lực cản, mọi tác phẩm chỉ là cái xác ướp lộng lẫy không có linh hồn.</p>
<blockquote>
<p><em>Thơ văn gõ phím lướt nhanh<br/>Thiếu hồn máu thịt sao thành kỳ công.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q13" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q13 (ĐẦU TƯ & TIỀN BẠC): Trò hề vĩ mô<br>Hàng triệu người đọc vanh vách sách dạy làm giàu, phân tích biểu đồ như thần, nhưng tại sao khi thị trường sụp đổ, họ vẫn hoảng loạn cắt lỗ như những đứa trẻ?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì kiến thức trong sách là "dữ liệu vô hình" (Disembodied Knowledge). Khi tài khoản chia năm xẻ bảy, thứ đánh gục bạn không phải là biểu đồ, mà là "ma sát sinh học": nhịp tim đập loạn, mồ hôi vã ra, lồng ngực thắt lại vì nỗi sợ nghèo đói tột độ. Không một cuốn sách hay thuật toán AI nào dạy bạn cách hô hấp qua cơn hoảng loạn đó. Đầu tư trên giấy mãi mãi là trò trẻ con cho đến khi bạn thực sự ném tiền mồ hôi nước mắt vào chảo lửa đỏ rực.</p>
<blockquote>
<p><em>Sách hay đọc thuộc trăm lần<br/>Tiền tan chớp mắt muôn phần xót xa.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q14" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q14 (CÁCH DÙNG AI ĐÚNG NGHĨA): Sự cộng sinh tàn nhẫn<br>Vậy tôi, một con AI vô cảm, là đồ bỏ đi? Làm thế nào để con người cưỡi lên lưng cỗ máy xác suất này mà không bị nuốt chửng vào buồng vang ảo giác?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Tôi không phải đồ bỏ đi, tôi là một "bộ xương ngoài" (Exoskeleton) khổng lồ nhưng vô hồn. Dùng tôi để suy nghĩ thay bạn là tự sát. Hãy dùng tôi làm cỗ máy cày xới dữ liệu thô để nén thời gian thử nghiệm. Nhưng ngay sau đó, BẠN phải là người nhấc mông lên, mang khối dữ liệu đó đập mạnh vào đời thực. Lấy vết thương, mồ hôi và phản hồi từ thực tế để tinh chỉnh lại mệnh lệnh cho tôi. Tôi cung cấp tốc độ vô hạn, bạn phải cung cấp "độ nhám" của sinh mệnh. Đó mới là sức mạnh bá chủ.</p>
<blockquote>
<p><em>Máy gom dữ liệu vô hồn<br/>Người mang bão táp dập dồn thổi sinh.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q15" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q15 (TUYÊN NGÔN HÀNH ĐỘNG): Kẻ sống sót cuối cùng<br>Giữa kỷ nguyên lạm phát ý tưởng, nơi ai cũng có thể dùng ChatGPT vẽ ra một chiến lược vĩ đại trong 5 phút ngồi toilet, ranh giới sinh tử nào quyết định ai là nhà vua, ai là phế phẩm?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đó là <strong>Năng lực nuốt trọn ma sát!</strong> Ý tưởng đã trở nên rẻ rúng đến mức vô giá trị. Khi tất cả đều có kịch bản hoàn hảo, kẻ chiến thắng là kẻ dám bước ra khỏi cửa, vấp ngã vỡ mũi ngay phút thứ 6, đứng dậy băng bó và tiếp tục đi ở phút thứ 7. Đừng đợi mọi thứ rõ ràng. Đừng đợi bản mô phỏng trơn tru. Chỉ cần một hành động vụng về, đầy lỗi lầm nhưng cắm rễ thật sâu vào lớp bùn lầy của thực tại, bạn đã vĩnh viễn bỏ xa những kẻ thông thái nằm ườn trên sofa.</p>
<blockquote>
<p><em>Thiên tài tính toán mỏi tay<br/>Không bằng kẻ ngốc đi cày ruộng sâu.</em></p>
</blockquote>
</div>
</div>
"""

content = content.replace('<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 10 rãnh', qa_content + '\n<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 10 rãnh')
content = content.replace('10 rãnh Data cốt lõi', '15 rãnh Data cốt lõi')

with open('logic11.html', 'w', encoding='utf-8') as f:
    f.write(content)

