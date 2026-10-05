import re

with open('logic08.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Thêm TOC
toc_insertion = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">7 BẪY ẢO GIÁC</li>
<li><a class="ink-toc-link" href="#q31">Q1. Ảo giác "Hack" thuật toán</a></li>
<li><a class="ink-toc-link" href="#q32">Q2. Bệnh ảo tưởng sản phẩm tốt</a></li>
<li><a class="ink-toc-link" href="#q33">Q3. Căn bệnh núp bóng an toàn</a></li>
<li><a class="ink-toc-link" href="#q34">Q4. Cái chết ép đơn 60 giây</a></li>
<li><a class="ink-toc-link" href="#q35">Q5. Căn phòng tẩy não</a></li>
<li><a class="ink-toc-link" href="#q36">Q6. Lưới rách xin SĐT</a></li>
<li><a class="ink-toc-link" href="#q37">Q7. Tư duy cờ bạc và AI</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 2. Thêm Nội dung
qa_content = """
<hr style="margin: 4rem 0; border: none; border-top: 4px solid var(--ink-text);"/>
<h1 class="is-short">7 BẪY ẢO GIÁC: TƯ DUY DANIEL PRIESTLEY</h1>
<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q31" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 1: ẢO GIÁC "HACK" THUẬT TOÁN<br>Đăng video lên, nhờ hội anh em vào chéo like, thả tim để mồi thuật toán cắn xu hướng. Dễ thế tội gì không làm?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Làm thế là tự sát! Bạn tưởng AI vẫn "mù chữ" và phải đếm like bề mặt như chục năm trước? Thuật toán hiện tại (Semantic AI) tự động bóc băng kịch bản, soi vi biểu cảm và hiểu cặn kẽ nội dung. Nếu video B2B thâm sâu mà toàn tài khoản sinh viên hóng phốt vào thả tim, AI lập tức dán nhãn "dữ liệu bẩn" và bóp chết kênh vĩnh viễn. Máy móc không đếm like, nó quét sự tương thích ngữ nghĩa.</p>
<blockquote>
<p><em>Cày tim chéo nịnh dối gian,<br/>Máy soi sai tệp nát tan cơ đồ.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q32" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 2: BỆNH ẢO TƯỞNG SẢN PHẨM TỐT<br>Sản phẩm của tôi tốt nhất, giá lại rẻ nhất thị trường. Khách hàng chắc chắn sẽ tự ùa tới mua, đúng chứ?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Khách ùa tới để... chém giá! Sản phẩm vô hồn là vốc cát bãi biển, thằng nào cũng bán được. Muốn thao túng cuộc chơi, hãy biến cát thành "Chip Apple" – đó là <strong>Vốn Trí Tuệ (Intellectual Capital)</strong>. Đóng gói kinh nghiệm của bạn thành một "Triết lý độc quyền". Khi khách khao khát cái triết lý đó, bạn tước đoạt hoàn toàn quyền so sánh giá của họ. Độc quyền tư tưởng là độc quyền định giá.</p>
<blockquote>
<p><em>Bán hàng chịu cảnh bọt bèo,<br/>Gói riêng triết lý thoát nghèo vinh quang.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q33" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 3: CĂN BỆNH NÚP BÓNG AN TOÀN<br>Dùng logo công ty chạy quảng cáo cho uy tín và chuyên nghiệp. Tội gì phải vác mặt mình lên mạng cho thiên hạ phán xét?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Núp sau logo là bạn đang tự nguyện đóng <strong>"95% Thuế Sự Chú Ý"</strong>! Sinh lý học não bộ chỉ tin tưởng khuôn mặt đồng loại, không tin một cái ảnh graphic vô hồn. Thò mặt lên hình, bạn bú trọn traffic và cảm xúc. Che giấu thân phận là tự thiến dòng phân phối và dâng mỡ tới miệng đối thủ. Đừng làm anh hùng giấu mặt trong kỷ nguyên cá nhân hóa!</p>
<blockquote>
<p><em>Nấp sau biểu tượng vô hồn,<br/>Dâng bao khách sộp sinh tồn cho ai.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q34" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 4: CÁI CHẾT CỦA ÉP ĐƠN 60 GIÂY<br>Clip 60 giây đang viral triệu view, tôi cắm luôn link gói tư vấn giá cao chốt sale cho lẹ. Dễ ăn quá đúng không?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Dễ ăn chửi! Để quẹt thẻ một đơn hàng giá cao, não người cần tĩnh tâm <strong>2 đến 7 tiếng</strong>, và phải lướt qua bạn <strong>11 lần</strong> để hết cảnh giác. Đòi chốt sale trong 60 giây ồn ào y hệt vỗ vai gái lạ ngoài đường gào lên: "Cưới anh đi!". Khách sẽ dựng khiên phòng thủ, coi bạn là bọn chèo kéo lừa đảo và block thẳng tay. Clip ngắn chỉ là mũi khoan phá băng, cấm ép mua!</p>
<blockquote>
<p><em>Ngắn mồi đòi chốt vội vàng,<br/>Khách sinh phòng thủ phũ phàng quay lưng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q35" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 5: CĂN PHÒNG TẨY NÃO<br>Thời nay ai chả thích lướt clip ngắn, hì hục làm video dài 1 tiếng đồng hồ ai mà thèm xem?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Đám đông rảnh rỗi thích xem ngắn, người cầm ví tiền khao khát xem dài! Video dài (Long Form) là "Căn phòng tẩy não". Khi khách bấm vào, hãy nhốt họ lại và nã liên tục 3 nhát búa: Bằng chứng - Nguyên lý - Quy trình. Rã đông 60 phút đủ lâu, khiên phòng thủ sụp đổ. Họ sẽ nhìn bạn như một Đấng cứu thế vạch ra đường sống, chứ không phải một thằng Sale đi xin việc.</p>
<blockquote>
<p><em>Ngắn mồi nhử khách tò mò,<br/>Phim dài nhốt chặt vào lò bóc sâu.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q36" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 6: CHIẾC LƯỚI RÁCH "XIN SỐ ĐIỆN THOẠI"<br>Dẫn khách qua video dài thuyết phục rồi, tôi để form xin Họ tên và Số điện thoại gọi chốt đơn cho gọn, chuẩn bài chưa?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Chuẩn bài để bị đuổi đi! Chẳng ai muốn giao số cho bọn telesale gọi làm phiền. Nhưng ai cũng thèm khát được "khám bệnh". Hãy vứt form đó đi, bắt họ điền <strong>Bài Trắc nghiệm chẩn đoán</strong>: <em>"Nỗi đau lớn nhất? Đã đốt tiền ngu ở đâu?"</em>. Bắt họ tự khai tử huyệt. Bốc máy lên, bạn là bác sĩ cầm bệnh án, chốt sale không trượt phát nào.</p>
<blockquote>
<p><em>Cò mồi xin số đuổi đi,<br/>Hỏi han chẩn bệnh khách ghi vội vàng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q37" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ BẪY 7: TƯ DUY CỜ BẠC VÀ AI<br>Nhìn vào đống form khách điền, mình cứ vỗ đùi phán bừa giá chốt sale xem hên xui, khách chịu thì ăn, đúng không?</h2>
<div class="dialogue-response">
<p><strong>⚡ Đáp:</strong><br>
Tư duy của kẻ đánh bạc! Bậc thầy dùng AI để vắt kiệt dữ liệu. Ném file hàng trăm câu trả lời đó cho Claude/ChatGPT, ra lệnh cho nó băm nát dữ liệu để tìm ra các nhóm chân dung tàng hình. Nó sẽ chỉ đích danh nhóm này dư sức trả 25.000 đô la, và viết luôn kịch bản telesale gài bẫy cho từng người. Bỏ 20 USD/tháng mua AI mà không biết dùng thì sớm dẹp tiệm.</p>
<blockquote>
<p><em>Nhìn vào dữ liệu lơ ngơ,<br/>Nhờ AI tính toán nước cờ thu đô.</em></p>
</blockquote>
</div>
</div>
"""

content = content.replace('<p><em>(Hệ thống đã mã hóa 11 rãnh', qa_content + '\n<p><em>(Hệ thống đã mã hóa 11 rãnh')

with open('logic08.html', 'w', encoding='utf-8') as f:
    f.write(content)

