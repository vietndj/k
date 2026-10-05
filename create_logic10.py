import re

with open('logic09.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Document Title
title_pattern = r'<title>.*?</title>'
content = re.sub(title_pattern, '<title>[INKDOC-10] GIAO THỨC CHẤT VẤN LƯỢNG TỬ</title>', content)

# 2. Update TOC
new_toc = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">MA TRẬN LƯỢNG TỬ</li>
<li><a class="ink-toc-link" href="#q1">Q1. Cú lừa nỗ lực</a></li>
<li><a class="ink-toc-link" href="#q2">Q2. Bức tường phòng vệ</a></li>
<li><a class="ink-toc-link" href="#q3">Q3. Đòn bẩy ma sát</a></li>
<li><a class="ink-toc-link" href="#q4">Q4. Lỗ hổng lưu chất</a></li>
<li><a class="ink-toc-link" href="#q5">Q5. Lực quán tính AI</a></li>
<li><a class="ink-toc-link" href="#q6">Q6. Buôn không khí</a></li>
<li><a class="ink-toc-link" href="#q7">Q7. Lỗ đen tài chính</a></li>
<li><a class="ink-toc-link" href="#q8">Q8. Hộp đen IP</a></li>
<li><a class="ink-toc-link" href="#q9">Q9. Ping server thị trường</a></li>
<li><a class="ink-toc-link" href="#q10">Q10. Quy tắc 10/90</a></li>
"""
toc_pattern = r'(<ul class="ink-toc-list">).*?(</ul>)'
content = re.sub(toc_pattern, r'\1\n' + new_toc + r'\n\2', content, flags=re.DOTALL)

# 3. Update Content
new_content = """
<h1 class="is-short">GIAO THỨC CHẤT VẤN LƯỢNG TỬ: BẺ GÃY RÀO CẢN NHẬN THỨC</h1>
<div class="ink-meta">
  <span>System Identity: [INKDOC-10]</span>
  <span class="mx-2">•</span>
  <span>Render Mode: [Dialogue]</span>
</div>

<div style="margin-bottom: 3rem;">
    <p>Tôi đã tháo dỡ toàn bộ các khối kiến trúc từ đầu đến giờ và nén chúng lại thành một bộ Ma trận Hỏi - Đáp (Q&A) mang sát thương cao nhất. Mục tiêu: Bẻ gãy rào cản nhận thức bằng lực va đập vật lý. Mọi tàn dư của tư duy "cố gắng, ý chí" sẽ bị nghiền nát thành bụi.</p>
    <p><em>(Quy tắc Lục Bát: Kiểm duyệt ngầm bằng trắc chữ 2-4-6-8, gieo vần tuyệt đối chính xác tại chữ thứ 6).</em></p>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q1" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 1: Cày cuốc 16 tiếng mỗi ngày nhễ nhại mồ hôi, vắt kiệt sinh lực với niềm tin vũ trụ sẽ ban phát sự giàu có. Tại sao phương trình nỗ lực này lại là cú lừa tàn bạo nhất của hệ sinh thái làm thuê?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì thị trường là một cỗ máy mù lòa, tuyệt đối không có cảm biến để đo lường mồ hôi của bạn. Bán sức lao động là động năng tuyến tính, sinh công xong là tiêu tán 100% năng lượng. Dòng tiền vĩ mô chỉ chảy vào khối "Thế năng tĩnh" (Tài sản số, Sở hữu trí tuệ) có chi phí nhân bản bằng 0, ép máy chủ đi cày thay bạn ngàn năm.</p>
<blockquote>
<p><em>Cày thuê vắt kiệt xác thân<br/>Đúc thành tài sản để phần máy lo.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q2" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 2: Lao ra đường vồ vập khách hàng, ép họ chốt Sale ngay lần đầu chạm mặt để rồi bị chặn số chửi rủa. Đâu là thuật toán vô hiệu hóa bức tường phòng vệ sinh tồn này mà không tốn một lời nài nỉ?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đòi chốt đơn ngay là lực ép vuông góc, kích hoạt hạch hạnh nhân tự vệ của não bò sát. Phải dùng thuật toán 7-11-4 (7 giờ, 11 chạm, 4 nền tảng) để hack nơ-ron gương. Sự hiện diện lặp lại ở đa chiều sẽ tự động đánh sập cầu dao nghi ngờ, ép não họ ra lệnh quẹt thẻ như một phản xạ tủy sống.</p>
<blockquote>
<p><em>Khách hàng không chốt lần đầu<br/>Bảy giờ chạm mặt bắc cầu vung đô.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q3" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 3: Hầu hạ khách hàng tận răng, giảm giá sập sàn, dẹp bỏ mọi rào cản để vơ vét đám đông. Tại sao lòng tham rẻ rúng này lại tự tay cắt đứt quyền lực định giá và biến doanh nghiệp thành bãi rác?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì bạn đã triệt tiêu hoàn toàn "Đòn bẩy Ma sát". Thứ gì trơn tru dễ dãi, não người tự động gán nhãn hạ đẳng. Áp suất định giá siêu ngạch (Oversubscribed) chỉ bùng nổ khi bạn vặn khóa van công suất, nhốt khách vào Danh sách chờ. Rào cản vật lý này kích nổ mã độc FOMO, ép tệp tinh hoa vung tiền giành giật chỗ đứng.</p>
<blockquote>
<p><em>Hàng thừa khách khứa làm ngơ<br/>Khóa van khan hiếm chực chờ tranh mua.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q4" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 4: Ôm 33.000 Follower trên Fanpage, vuốt ve cái tôi bằng những nút Like dạo, để rồi khóc thét khi thuật toán bóp tương tác về 0. Lỗ hổng lưu chất nào đang bóp nghẹt túi tiền của bạn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đám mây Follower đó chỉ là khối khí gas vô giá trị trôi trên vùng đất đi thuê. Khí không đi qua cổ chai thì không bao giờ sinh công. Phải cắm mồi nhử API, ép đám đông nộp Data (Email, Số điện thoại) để chiết xuất khối mây ảo thành tài sản vật lý bị nhốt chặt trong Server tư hữu của bạn.</p>
<blockquote>
<p><em>Xây nhà trên đất người ta<br/>Rút ngay tệp khách mang ra vườn mình.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q5" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 5: Run rẩy sợ AI lấp đầy thị trường vào năm sau, đồng thời khinh bỉ đám thợ lấm bùn lầy nhớt. Tại sao sự ngạo mạn công nghệ này lại là minh chứng của một bộ não mù tịt về lực quán tính?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Lưới điện AI truyền bằng tốc độ ánh sáng, nhưng xã hội hấp thụ bằng lực cản xương thịt. Sự ì ạch của thế hệ Boomer chính là hằng số sinh lời vĩ đại nhất. Chênh lệch giá (Arbitrage) sinh ra từ việc lấy API xịn xò bọc lại thành cái vỏ "1 nút bấm" cực ngu ngốc, cắm vào tiệm sửa xe và lạnh lùng thu lộ phí từ sự mù mờ của đám đông.</p>
<blockquote>
<p><em>Điện kia lan chớp chân mây<br/>Thói quen ì ạch ta đây hái vàng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q6" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 6: Khư khư giấu kín chút bí quyết ngành, ép khách trả tiền lẻ mua lý thuyết suông. Việc "đi buôn không khí" này vi phạm định luật Nhiệt động lực học nào?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Trong kỷ nguyên số, thông tin thô là lưu chất mất ma sát, chi phí biên bằng 0. Cố thu tiền từ không khí là chống lại tự nhiên. Hãy mở mã nguồn 100%, ném sạch lý thuyết làm nam châm cào Traffic. Chỉ lập trạm thu tiền ở "Hạ tầng thi công" (phần mềm, làm hộ A-Z), thứ trực tiếp giúp não bộ khách hàng bảo toàn năng lượng.</p>
<blockquote>
<p><em>Mở kho kiến thức đem cho<br/>Thu tiền ở đoạn đứng lo vận hành.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q7" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 7: Chửi rủa bọn tinh hoa ngồi mát ăn bát vàng, cắn răng làm gấp đôi ở tầng đáy mong ngày thăng cấp. Lỗ hổng Vật lý Thiên văn nào đang nghiền nát giấc mơ thăng tiến tuyến tính này?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Kim tự tháp giá trị không phải cầu thang để trèo, nó là 4 chiều không gian dị biệt. Tầng đáy sinh công cơ bắp, tiêu tán 100%. Tầng đỉnh (Tài sản Tài chính) là một Lỗ Đen. Khi đạt khối lượng tới hạn, nó tự bẻ cong không-thời gian và hút mồ hôi của kẻ khác bằng Trọng trường. Thoát đáy bằng cách viết Quy trình (SOP) và sở hữu nó, tuyệt đối đừng tự tay làm.</p>
<blockquote>
<p><em>Đáy sâu vắt kiệt mồ hôi<br/>Đỉnh cao tài sản vương ngôi gom tiền.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q8" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 8: Tự vỗ ngực mình là chuyên gia xuất sắc nhất, kỹ năng thượng thừa nhưng lại cam chịu bị đám đông mang lên bàn cân ép giá từng đồng. Cơ chế nào đã tước đoạt quyền định giá của bạn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì bạn dán nhãn "Kỹ năng" cho mình, tự ném bản thân vào bể máu có tổng bằng không. Khách hàng sẽ dùng lối tắt logic để so sánh giá của bạn với vạn thợ cày khác. Đập nát mác kỹ năng, đóng gói nó thành một "Hộp đen IP" độc quyền. Việc tước đoạt công cụ tham chiếu sẽ tạo ra sự khan hiếm nhận thức, ép họ mua với giá phi tuyến tính.</p>
<blockquote>
<p><em>Kỹ năng thiên hạ tranh đua<br/>Tạo khung độc bản làm vua một vùng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q9" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 9: Đập sạch vốn liếng, giam mình 6 tháng code một siêu sản phẩm rồi mới tung ra mong chấn động thế giới. Bản án tử hình nào đang chờ đợi lối tư duy ngây thơ này?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Ném toàn bộ máu vào một con Boss ẩn chỉ số là hành vi tự sát! Tuyệt đối không chế tạo sản phẩm khi chưa Ping được Server thị trường. Bơm 200 đô chạy Ads giả lập nút "Pre-order". Dữ liệu trả về bằng 0 thì vứt ngay dự án để bảo toàn động năng. Trò chơi kinh doanh chạy bằng cảm biến Data, không chạy bằng đức tin.</p>
<blockquote>
<p><em>Hai trăm đô thử thị trường<br/>Đừng xây ảo mộng trên giường ngủ mê.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q10" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 10: Thức đến 2h sáng tự tay bọc hàng, rep tin nhắn, vỗ ngực tự hào mình là chiến thần cày cuốc. Đòn bẩy ma sát nào đang tự cưa cụt đôi tay của kẻ làm sếp?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Dành sức làm 90% việc lặt vặt là bạn đang ép cánh tay đòn về sát điểm tựa, triệt tiêu hoàn toàn momen xoay của hệ thống (Quy tắc 10/90). Kẻ kiến trúc sư tước đoạt quyền "được bận rộn" của chính mình, đẩy sạch tác vụ tay chân cho Bot và AI. Bạn chỉ giữ lại 10% mắt xích chiến lược để nhấp chuột và quan sát bảng điều khiển.</p>
<blockquote>
<p><em>Mười phần nắm chốt then cài<br/>Chín mươi phần việc nhường ai vận hành.</em></p>
</blockquote>
</div>
</div>

<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 10 rãnh Data cốt lõi...)</em></p>
"""
content_pattern = r'(<article class="ink-content ink-mode-dialogue">).*?(</article>)'
content = re.sub(content_pattern, r'\1\n' + new_content + r'\n\2', content, flags=re.DOTALL)

with open('logic10.html', 'w', encoding='utf-8') as f:
    f.write(content)

