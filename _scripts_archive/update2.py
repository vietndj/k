import re

with open('logic08.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Thêm TOC
toc_insertion = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">MÃ HÓA CẢM XÚC NGẦM</li>
<li><a class="ink-toc-link" href="#q18">Q1. Cú lừa sự vô cảm</a></li>
<li><a class="ink-toc-link" href="#q19">Q2. Nọc độc tội lỗi</a></li>
<li><a class="ink-toc-link" href="#q20">Q3. Bảo toàn nỗi đau</a></li>
<li><a class="ink-toc-link" href="#q21">Q4. Sinh lý phản bội</a></li>
<li><a class="ink-toc-link" href="#q22">Q5. Đòn chí mạng</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 2. Thêm Nội dung
qa_content = """
<hr style="margin: 4rem 0; border: none; border-top: 4px solid var(--ink-text);"/>
<h1 class="is-short">MÃ HÓA CẢM XÚC NGẦM: BÓC TRẦN TÂM LÝ CHUYỆN KỂ</h1>
<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q18" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 1: CÚ LỪA CỦA SỰ VÔ CẢM<br>Kẻ ráo hoảnh, trơ mắt nhìn người thân nằm xuống là loài quỷ dữ máu lạnh, hay thực chất là nạn nhân đáng thương nhất của một cú lừa mang tên "tiêu chuẩn xã hội"?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong> Họ là nạn nhân của cơ chế sinh tồn! Xã hội nhồi sọ ta "đau thương là phải khóc ngay", nhưng não bộ lại báo động: <em>"Sụp đổ lúc này là chết!"</em>. Hạch hạnh nhân lập tức ngắt cầu dao cảm xúc, đóng băng tâm trí để bạn duy trì lý trí lo liệu thực tại. Sự trống rỗng không phải là vô tâm, mà là chiếc khiên sinh học từ chối gục ngã trước lưỡi hái tử thần.</p>
<blockquote>
<p><em>Trách người ráo hoảnh vô tình,<br/>Đâu hay não bộ giấu mình chở che.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q19" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 2: NỌC ĐỘC CỦA SỰ TỘI LỖI<br>Người ta tưởng kẻ "trơ như đá" ở đám tang là kẻ ngạo nghễ đạp lên dư luận. Sự thật lộn ngược nào ẩn sau vỏ bọc ấy lại biến họ thành thỏi nam châm vắt kiệt sự đồng cảm của khán giả?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong> Sự thật là họ bị ám ảnh tột độ bởi dư luận! Xung đột đắt giá nhất sinh ra khi: ý thức biết rõ "đám tang là phải khóc", nhưng cơ thể lại thẳng thừng đình công. Khán giả sẽ không thương xót một kẻ khóc lóc dễ đoán, họ bị bóp nghẹt tim gan trước nỗ lực vô vọng của một con người đang giằng xé, tự ghê tởm bản thân vì không thể nặn ra cảm xúc cho giống người bình thường.</p>
<blockquote>
<p><em>Khóc than lộ hết thì nông,<br/>Gồng mình nén chặt bão giông trong lòng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q20" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 3: ĐỊNH LUẬT BẢO TOÀN NỖI ĐAU<br>Nỗi đau không bốc hơi qua tuyến lệ thì sẽ đục khoét cơ thể bằng hình thù quái gở nào? Việc điên cuồng cọ bồn cầu rướm máu hay đấm gãy mũi người lạ chen hàng có phải là một sự điên rồ?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong> Đó là định luật bảo toàn cảm xúc! Bị đè nén, nỗi đau sẽ rò rỉ thành những hành vi chệch hướng lố bịch. Đứng trước sự bất lực tuyệt đối của cái chết, tâm trí hoảng loạn ép con người bám víu vào những tiểu tiết có thể kiểm soát. Cơn thịnh nộ vô cớ hay sự bận rộn ám ảnh chính là tiếng thét câm lặng, là van xả áp suất xót xa nhất của một cõi lòng đang vỡ vụn.</p>
<blockquote>
<p><em>Tay chà từng mép gạch men,<br/>Giấu đi bão tố bon chen cõi lòng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q21" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 4: SỰ PHẢN BỘI CỦA SINH LÝ<br>Đứng bên quan tài uy nghiêm, tại sao bạn đột nhiên bật cười ngặt nghẽo chỉ vì một con ruồi đậu trên di ảnh? Phản ứng báng bổ, lệch chuẩn này che đậy sự thật tâm lý khốc liệt nào?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong> Đó là khoảnh khắc hệ thần kinh chập mạch do dung lượng bị ép vượt ngưỡng cực hạn. Bầu không khí ngột ngạt ngầm của bi kịch va chạm với một chi tiết đời thường ngớ ngẩn đã xuyên thủng mọi màng lọc lý trí. Tiếng cười đó tuyệt nhiên không chứa niềm vui, nó là sự phản bội tàn nhẫn của sinh lý đối với mọi chuẩn mực đạo đức, phơi bày sự bi hài nghẹt thở của con người.</p>
<blockquote>
<p><em>Đứng cheo leo miệng vực sầu,<br/>Cười buông một tiếng nát nhàu tâm can.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q22" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 5: ĐÒN CHÍ MẠNG TRÌ HOÃN<br>Tại sao tiếng nấc nghẹn ngào nhất không rơi xuống nấm mồ lạnh lẽo, mà lại vỡ vụn tức tưởi trước một chiếc bàn chải đánh răng cũ kỹ? Điểm kích hoạt trễ nhịp này tàn nhẫn băm vằm tâm trí ra sao?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong> Khóc ở đám tang chỉ là trả bài cho kịch bản đám đông, nơi lớp khiên phòng vệ vẫn bật tối đa. Bi kịch thực sự luôn kích nổ từ những tiểu tiết vô hại – thứ não bộ lơi lỏng không thèm đề phòng. Chiếc bàn chải là bản án trần trụi chốt hạ sự vắng mặt vĩnh viễn. Nỗi đau ập đến sai bối cảnh lột tả sự cô độc tột cùng: cả thế giới vẫn thản nhiên quay, chỉ có vũ trụ của kẻ ở lại vừa chính thức tan tành.</p>
<blockquote>
<p><em>Nghĩa trang nín lặng không lời,<br/>Vô tình chạm vật đất trời vỡ đôi.</em></p>
</blockquote>
</div>
</div>
"""
content = content.replace('<p><em>(Hệ thống đã mã hóa 11 rãnh', qa_content + '\n<p><em>(Hệ thống đã mã hóa 11 rãnh')

with open('logic08.html', 'w', encoding='utf-8') as f:
    f.write(content)

