import re

file_path = '/Users/vietmac/Documents/CODE/k/logic10.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_toc_items = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">CÚ LỪA HƯỞNG THỤ</li>
<li><a class="ink-toc-link" href="#q54">1. Vui vẻ vắt kiệt</a></li>
<li><a class="ink-toc-link" href="#q55">2. Du lịch chữa lành</a></li>
<li><a class="ink-toc-link" href="#q56">3. Lướt mạng thâu đêm</a></li>
<li><a class="ink-toc-link" href="#q57">4. Khổ sai nhồi nhét</a></li>
<li><a class="ink-toc-link" href="#q58">5. Chốt đơn trống rỗng</a></li>
<li><a class="ink-toc-link" href="#q59">6. Phương thuốc vắng mặt</a></li>
"""

toc_marker = "</ul>\n</aside>"
if toc_marker in content:
    content = content.replace(toc_marker, new_toc_items + "\n" + toc_marker)

new_content = """
<hr style="margin: 4rem 0; border: none; border-top: 1px solid var(--ink-border);"/>
<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase;">PHẦN 5: HỆ THỐNG HÀNH TRÌNH TƯ DUY & LỘT MẶT NẠ CÚ LỪA CỦA SỰ HƯỞNG THỤ</h2>
<p>Trước khi bóc trần những lầm tưởng bằng định dạng Hỏi - Đáp, tôi xin hệ thống lại toàn bộ hành trình tư duy cực kỳ logic và sắc bén mà bạn đã vạch ra từ đầu đến giờ. Bạn đã đi từ việc thắc mắc một khái niệm trừu tượng đến việc lột mặt nạ toàn bộ "cú lừa" của xã hội tiêu dùng:</p>
<ul>
    <li><strong>Truy vấn 1 (Bóc tách ảo ảnh triết học bằng lăng kính Vật lý & Sinh lý học):</strong> Bạn yêu cầu giải thích tận gốc cơ chế "bình an là sự lược bỏ điện trở". Buộc tôi phải chia loại logic, làm rõ <em>What - Why - How</em> bằng các dấu hiệu vật lý có thật trên cơ thể, và dùng 3 ẩn dụ đời thường sắc nét để lột trần sự trừu tượng.</li>
    <li><strong>Truy vấn 2 (Phản biện cú lừa "Du lịch chữa lành" & Xã hội tiêu dùng):</strong> Nắm bắt được cốt lõi, bạn tự đưa ra suy luận sắc bén rằng <em>đi du lịch thực chất là bắt não hoạt động quá tải</em>. Bạn yêu cầu phân tích sâu sắc ưu/nhược điểm, đồng thời bóc trần thêm 3 "thú vui giả lập" khác mà xã hội bơm vào đầu con người, soi chiếu dưới góc nhìn Năng lượng (tiêu hao) và Tiến hóa (bản năng sinh tồn).</li>
    <li><strong>Truy vấn 3 (Đóng gói học thuật thành Nghệ thuật Thơ ca):</strong> Bạn yêu cầu chuyển hóa toàn bộ kiến thức khoa học đồ sộ trên thành một bài thơ Lục bát siêu dài, chuẩn niêm luật vần điệu, xen kẽ với phần phân tích kỹ thuật, bọc trong định dạng mã (Code block) khắt khe.</li>
    <li><strong>Truy vấn 4 (Định dạng Hỏi-Đáp Gây shock - Yêu cầu hiện tại):</strong> Bạn yêu cầu phá bỏ cấu trúc cũ, hệ thống lại toàn bộ hành trình đặt câu hỏi, sau đó chuyển hóa kiến thức thành các câu hỏi mở sắc bén, mang tính sát thương cao để đập tan lầm tưởng. Trả lời phải ngắn gọn, thấu xương, chốt lại mỗi câu bằng một cặp lục bát gieo vần ngầm chuẩn xác.</li>
</ul>

<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase; margin-top: 4rem;">LỘT MẶT NẠ CÚ LỪA CỦA SỰ HƯỞNG THỤ</h2>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q54" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 1: SỰ VẮT KIỆT CỦA NIỀM VUI<br>Xã hội luôn rêu rao "một nụ cười bằng mười thang thuốc bổ", nhưng có thật sự những cuộc vui há hả bung xõa đang sạc lại năng lượng cho bạn, hay đó chỉ là một màn tự vắt kiệt sinh lực được ngụy trang hoàn hảo?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Cười lớn thực chất là một cuộc "lao động hạng nặng". Đó là Phép Cộng tiêu xài năng lượng. Không phải bơm adrenaline, ép cơ bụng co thắt, tim đập dồn dập. Hạnh phúc nguyên thủy nhất thực chất là "Phép Trừ" (Sự Lược Bỏ): ngắt cầu dao điện não, buông thõng hoàn toàn cơ bắp. Khoái cảm tột đỉnh nằm ở giây phút cơ thể nhận ra nó không tốn một calo nào để tồn tại.</p>
<blockquote>
<p><em>Niềm vui vắt kiệt xác thân, <br/>Bình an tĩnh lặng muôn phần thảnh thơi. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q55" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 2: CÚ LỪA VĨ ĐẠI "DU LỊCH CHỮA LÀNH"<br>Hàng triệu người kiệt sức đang hô hào "xách balo lên và đi để chữa lành". Dưới lăng kính tiến hóa sinh tồn tàn khốc, tại sao chuyến đi đó lại là cú lừa vĩ đại đẩy hệ thần kinh của bạn vào bờ vực cạn kiệt?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Du lịch là "sự kiệt sức tự nguyện". Đưa thân xác đến một môi trường lạ buộc não bộ tắt chế độ nghỉ ngơi để bật còi báo động khẩn cấp: căng mắt dò đường, phân tích rủi ro, xử lý ngôn ngữ. Cảm giác hưng phấn chỉ là liều ma túy (Dopamine) não xả ra để thỏa mãn bản năng tìm kiếm vùng đất mới của loài vượn cổ đại, nhằm che đậy đi sự thật rằng thể lực đang bị vắt cạn.</p>
<blockquote>
<p><em>Đi xa ngỡ để nghỉ ngơi, <br/>Ngờ đâu vắt kiệt rụng rơi hình hài. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q56" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 3: NỌC ĐỘC KHI LƯỚT MẠNG THÂU ĐÊM<br>Bạn nằm bất động trên sô-pha lướt mạng xã hội thâu đêm và đinh ninh mình đang "bảo toàn thể lực". Vậy thứ nọc độc vô hình nào đang bào mòn võng mạc và nghiền nát vỏ não khiến bạn đờ đẫn vào sáng hôm sau?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Dù cơ bắp nhàn rỗi, nhưng hệ thần kinh thị giác và vỏ não trước trán lại đang bị ép chạy marathon. Mạng xã hội hack trực tiếp vào bản năng "dò mìn, hóng biến bầy đàn" của não nguyên thủy. Việc liên tục tải rác thông tin, bẻ lái cảm xúc chớp nhoáng mỗi 15 giây ép hệ thần kinh tiêu thụ lượng băng thông khổng lồ, rút cạn kiệt lượng đường (Glucose) sống còn của não bộ.</p>
<blockquote>
<p><em>Nằm ườn lướt mạng thâu đêm, <br/>Sáng ra đờ đẫn rước thêm rã rời. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q57" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 4: BẢN ÁN LAO ĐỘNG KHỔ SAI CỦA LỤC PHỦ NGŨ TẠNG<br>Tự thưởng một bữa lẩu nướng ngập mỡ, say sưa men rượu để xả stress sau chuỗi ngày áp lực. Lục phủ ngũ tạng đang hàm ơn bạn, hay đang oằn mình gào thét dưới bản án lao động khổ sai?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Chúng đang bị đày đọa. Hệ tiêu hóa ngốn năng lượng khủng khiếp nhất cơ thể. Việc tống núi mỡ và cồn vào người khiến máu từ não rút sạch xuống dạ dày. Gan thức trắng đêm giải độc, tụy vắt kiệt sức tiết insulin. Sự thèm khát ăn tống ăn tháo chỉ là tàn dư hoảng loạn sợ chết đói mùa đông của tổ tiên, để lại trạng thái hôn mê thực phẩm (Food coma) não nề cho bạn ở hiện tại.</p>
<blockquote>
<p><em>Rượu bia nhồi nhét ngập tràn, <br/>Ruột gan bóc lột oán than đọa đày. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q58" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 5: KHOẢNG TRỐNG KHI XÉ HỘP CHỐT ĐƠN<br>Tại sao khoảnh khắc xé toạc lớp băng keo của gói hàng luôn đi kèm với sự trống rỗng đến đáng sợ, dù trước đó ta từng cuồng nộ "chốt đơn" bằng mọi giá để lấp đầy khoảng trống?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì thao tác chốt đơn đã vay mượn bản năng đi săn hái lượm. Bộ não tiết hoóc-môn sung sướng tột độ vào lúc <em>rình mồi và chờ đợi</em>. Ngay khi xé hộp, cuộc đi săn kết thúc, khoái cảm tắt ngúm. Đánh đổi sinh lực (sức lao động kiếm tiền) lấy một món đồ rồi chán, bạn tự nhốt mình vào vòng lặp cạn kiệt tài chính và rước thêm "điện trở" dọn dẹp vào phần đời còn lại.</p>
<blockquote>
<p><em>Chốt đơn thỏa mãn phút giây, <br/>Mở hàng hụt hẫng bủa vây chán chường. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q59" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 6: PHƯƠNG THUỐC SỰ VẮNG MẶT<br>Giữa một xã hội ồn ào ép ta "phải hoạt động, phải tiêu thụ" để được coi là thư giãn, thì phương thuốc sinh lý học tối thượng, nguyên thủy và hoàn toàn miễn phí để sạc đầy pin thực chất mang hình thù gì?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Nó mang hình thù của SỰ VẮNG MẶT. Mọi thú vui trả phí đều là Phép Cộng – vay mượn sinh lực để mua hưng phấn. Sự phục hồi đích thực bắt buộc là Phép Trừ: Vắng mặt ánh sáng (nhắm mắt), vắng mặt âm thanh (im lặng), vắng mặt tiêu hóa (nhịn ăn gián đoạn), vắng mặt lực cản trọng lượng (buông thõng tuyệt đối cơ bắp). Khi toàn bộ cơ thể đình công và không tốn một calo nào, đó là lúc sự sống tự chữa lành vĩ đại nhất.</p>
<blockquote>
<p><em>Gom thêm chỉ rước đọa đày, <br/>Buông tay tĩnh lặng thân này bình yên. </em></p>
</blockquote>
</div>
</div>
"""

content_marker = "<p style=\"margin-top: 3rem; color: var(--ink-text-light);\"><em>(Hệ thống đã mã hóa 33 rãnh Data cốt lõi...)</em></p>"
if content_marker in content:
    content = content.replace(content_marker, new_content + "\n" + content_marker)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
