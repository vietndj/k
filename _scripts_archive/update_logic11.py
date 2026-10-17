import re

with open('logic11.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update TOC
toc_insertion = """<li><a class="ink-toc-link" href="#q6">Q6. Thảm họa kép</a></li>
<li><a class="ink-toc-link" href="#q7">Q7. Thuật khắc chế AI</a></li>
<li><a class="ink-toc-link" href="#q8">Q8. Nguồn gốc sinh học</a></li>
<li><a class="ink-toc-link" href="#q9">Q9. Đòn ân huệ</a></li>
<li><a class="ink-toc-link" href="#q10">Q10. Ngôi đền của ma sát</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 2. Update Content
qa_content = """
<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q6" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q6 (THẢM HỌA KÉP): Cú bắt tay tử thần<br>Chuyện kinh dị gì sẽ xảy ra khi một kẻ mắc bệnh "nghĩ chay" (con người) dùng cỗ máy "bơm ảo giác" (AI) làm vũ khí tối thượng để đối phó với cuộc đời?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đó là thảm họa <strong>"Mù lòa vĩnh viễn" (Double Blindness)</strong>. Bộ não sinh học thèm khát sự trơn tru, AI lập tức mớm cho nó một kịch bản không tì vết. Hai thực thể bị nhốt kín này cộng sinh đẻ ra một buồng vang ảo giác (Echo Chamber). Đọc một câu trả lời hoàn mỹ từ AI, não bạn lập tức tiết dopamine cuồn cuộn vì ngỡ mình vừa kiến tạo vĩ nghiệp, dù thực tế chưa có một hòn đá nào bị xê dịch. Khối u ác tính này sinh ra một thế hệ khổng lồ về lý thuyết nhưng bại liệt hoàn toàn về tứ chi.</p>
<blockquote>
<p><em>Tưởng mình tính toán siêu phàm<br/>Ngờ đâu rệu rã chỉ làm phế nhân.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q7" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q7 (THUẬT KHẮC CHẾ AI): Xiềng xích bạo chúa<br>Nếu AI chỉ là kẻ lừa đảo lươn lẹo bằng xác suất, ta phải dùng đòn tra tấn tàn bạo nào để ép cỗ máy vô hồn này nôn ra giá trị thực chiến, biến nó từ kẻ mộng du thành vũ khí sắc bén?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Hãy quăng lựu đạn <strong>"Ma sát"</strong> vào bánh xe thuật toán của nó. Đừng bao giờ quỳ gối nài xin một "kế hoạch hoàn mỹ" vô trùng. Thay vào đó, hãy đóng đinh nó bằng những giới hạn khắc nghiệt nhất: <em>"Viết kịch bản này, nhưng nhớ máy quay nặng 20kg chỉ còn 5% pin, trời đang mưa lầy lội, diễn viên thì đau dạ dày"</em>. Cưỡng ép AI ngạt thở trong sự lộn xộn, nghèo nàn và khiếm khuyết của đời thực (Forced Constraints) là cách duy nhất ép nó bơm "ngữ cảnh vật lý" vào đống từ vựng vô tri.</p>
<blockquote>
<p><em>Giam vào giới hạn chông gai<br/>Ép cho cỗ máy trổ tài thực thi.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q8" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q8 (NGUỒN GỐC SINH HỌC): Nghịch lý của sự sống<br>Nếu "Overthinking" chỉ đẻ ra thứ rác rưởi tạo ảo mộng phế vật, cớ sao hàng triệu năm sinh tồn khắc nghiệt không đào thải nó, mà lại khắc sâu vào ADN của con người như một bản năng tối thượng?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bởi vì sự "hoang tưởng" sinh ra không phải để tìm chân lý, mà để <strong>trốn chạy cái chết!</strong> Ở thời tiền sử, ngồi yên trong hang tối và phóng đại tiếng lá rơi thành con hổ rình rập giúp tổ tiên bạn giữ mạng và tiết kiệm năng lượng. Bản năng chối bỏ sự cọ xát đó từng là tấm khiên sinh tồn vĩ đại. Nhưng ác thay, mang tấm khiên rỉ sét đó vào kỷ nguyên văn minh an toàn, nó trở thành chiếc lồng sắt giam cầm bạn trong nỗi khiếp nhược trước những "con ma" rủi ro không bao giờ có thật.</p>
<blockquote>
<p><em>Xưa kia giữ mạng cho người<br/>Ngày nay hoang tưởng nụ cười héo hon.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q9" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q9 (CÚ TÁT THỨC TỈNH CON NGƯỜI): Đòn ân huệ<br>Gạt phăng mớ triết lý bùi tai, lời tuyên án tàn khốc nào đủ sức đâm toạc màng nhĩ những kẻ đang nằm ườn trên sofa, tự huyễn hoặc về một "kế hoạch không tì vết" sắp thay đổi thế giới?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Sự chuẩn bị kỹ lưỡng trong đầu thường chỉ là lớp son phấn rẻ tiền che đậy cho thân xác hèn nhát. Chân lý không nằm trong một sa bàn tuyệt mỹ hay dòng code kỳ vĩ, nó nằm ở vết chai sần, ở giọt mồ hôi ứa ra nơi võ đài ngập bùn lầy. Tắt máy, quăng mình ra đường, làm hỏng việc, khóc lóc, rồi tự tay khâu lại vết thương. Bất cứ triết lý nào chưa được cọ xát đến bầm dập bởi đời thực, thảy đều là tiếng rên rỉ vô dụng của những cái bóng ma!</p>
<blockquote>
<p><em>Vứt đi mộng ảo viển vông<br/>Lao vào thực tế bão giông mà rèn.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q10" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q10 (NGÔI ĐỀN CỦA MA SÁT): Trọng tài tối thượng<br>Cuối cùng, giữa dải ngân hà dữ liệu AI và vũ trụ vô tận của trí tưởng tượng, thế giới vật lý tàn nhẫn này phán xét giá trị của một sinh mệnh dựa trên thước đo máu lạnh nào?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vũ trụ câm điếc trước mọi vĩ cuồng của ý nghĩ và mù lòa trước mọi ngôn từ hoa mỹ. Nó chỉ quỳ gối trước <strong>Khối lượng ma sát mà bạn dám đưa lưng ra gánh chịu</strong>. Lực cản không khí dạy chim cách bay, trọng lực giữ cơ bắp không teo rã. Sự lộn xộn, đói rét, rủi ro chính là chiếc lò nung man rợ nhất để thiêu rụi ảo giác, luyện "thông tin chết" thành "trí tuệ sống". Bạn ôm bao nhiêu dữ liệu không quan trọng. Bạn mang bao nhiêu vết sẹo, đó mới là minh chứng bạn đang tồn tại!</p>
<blockquote>
<p><em>Mộng mơ dẫu đẹp bằng không<br/>Dấu chân in vệt bụi hồng mới hay.</em></p>
</blockquote>
</div>
</div>
"""

content = content.replace('<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 5 rãnh', qa_content + '\n<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 5 rãnh')
content = content.replace('5 rãnh Data cốt lõi', '10 rãnh Data cốt lõi')

with open('logic11.html', 'w', encoding='utf-8') as f:
    f.write(content)

