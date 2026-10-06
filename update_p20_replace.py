import sys

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace TOC
toc_start_token = '<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 20: BẺ KHÓA HÀNH VI</li>'
if toc_start_token not in content:
    print("TOC start token not found")
    sys.exit(1)

parts_toc = content.split(toc_start_token)
before_toc = parts_toc[0]
after_toc_part = parts_toc[1].split('</ul>\n</aside>', 1)
after_toc = after_toc_part[1]

new_toc = """<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 20: BẺ KHÓA HÀNH VI</li>
<li><a class="ink-toc-link" href="#p20_q100">Q100. Bản chất sự ngụy biện</a></li>
<li><a class="ink-toc-link" href="#p20_q101">Q101. Lỗi logic bác sĩ ung thư</a></li>
<li><a class="ink-toc-link" href="#p20_q102">Q102. Bẫy kịch bản AI Fake</a></li>
<li><a class="ink-toc-link" href="#p20_q103">Q103. Vũ khí lắng nghe độ lệch</a></li>
<li><a class="ink-toc-link" href="#p20_q104">Q104. Tử huyệt dồn ép chốt sale</a></li>
<li><a class="ink-toc-link" href="#p20_q105">Q105. Ma thuật Lối thoát danh dự</a></li>
<li><a class="ink-toc-link" href="#p20_q106">Q106. Mua hàng bằng thể diện</a></li>
<li><a class="ink-toc-link" href="#p20_q107">Q107. Sinh tử Metacognition</a></li>
"""
content_with_new_toc = before_toc + new_toc + '</ul>\n</aside>' + after_toc

# Replace Body
body_start_token = '<!-- PHẦN 20 -->'
if body_start_token not in content_with_new_toc:
    print("Body start token not found")
    sys.exit(1)

parts_body = content_with_new_toc.split(body_start_token)
before_body = parts_body[0]
after_body_part = parts_body[1].split('</article>', 1)
footer = '\n</article>' + after_body_part[1]

new_body = """<!-- PHẦN 20 -->
<h1 class="is-short">PHẦN 20: TRẬN ĐỊA HỎI MỞ GÂY SHOCK & BẺ KHÓA HÀNH VI</h1>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q100" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 100 [BẢN CHẤT CỦA SỰ NGỤY BIỆN (TẦNG 2.5)]: Tại sao những bộ óc ưu tú nhất, những chuyên gia uy quyền nhất lại sẵn sàng viện dẫn các triết lý vĩ mô kinh thiên động địa... chỉ để lẩn tránh một thao tác vật lý nhỏ bé là bấm nút quay video? Phải chăng chuyên môn của họ là đồ bỏ đi?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Họ không thanh cao, họ đang đối diện với cái chết sinh học! Việc rớt đài từ "chuyên gia" xuống làm "kẻ lóng ngóng" trước ống kính bị não bộ đánh giá là sự sụp đổ vị thế bầy đàn. Để che giấu sự run rẩy cơ bắp, não tự động chế tạo ra chiếc khiên đạo lý Tầng 2.5 (<em>"Tôi bận làm việc lớn", "Hữu xạ tự nhiên hương"</em>). Lý lẽ thốt ra càng vĩ mô, nỗi sợ giấu bên dưới càng trẻ con.</p>
<blockquote>
<p><em>Ngôn từ chót lưỡi thanh <strong>cao</strong>,</em><br/>
<em>Bên trong run rẩy biết <strong>bao</strong> nhiêu <strong>lần</strong>.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q101" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 101 [LỖI LOGIC BÁC SĨ VÀ SỰ THẬT VỀ TRẢI NGHIỆM]: Bác sĩ ung thư không cần mắc bệnh vẫn cầm dao mổ được. Vậy cớ sao bóc tách tâm lý khách hàng lại BẮT BUỘC người làm nội dung phải tự phơi bày quá khứ nhục nhã của mình? Liệu có đang thần thánh hóa "trải nghiệm tự thân"?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Khối u ung thư là vật chất, máy chụp X-quang soi thấu được. Nhưng "Sự sĩ diện" là trò lừa đảo tàng hình của bản ngã! Nếu bạn chưa từng bị sức nặng của danh xưng đè bẹp, chưa từng ngụy biện hèn nhát, thì lời bạn nói ra chỉ là sự phán xét trịch thượng sặc mùi lý thuyết. Khách hàng ngửi thấy mùi "dạy đời", não họ lập tức đóng sập.</p>
<blockquote>
<p><em>Bệnh kia máy móc soi <strong>hình</strong>,</em><br/>
<em>Nỗi đau sĩ diện tự <strong>mình</strong> nếm <strong>qua</strong>.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q102" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 102 [CÁI BẪY CHẾT NGƯỜI CỦA KỊCH BẢN "FAKE"]: Trong thời đại AI tạo kịch bản 3 giây, tôi hoàn toàn có thể "fake" những câu chữ thấu cảm tột độ. Tại sao mang thứ kịch bản giả lập hoàn hảo đó lên Video lại bị coi là hành vi tự sát đẫm máu cho nhân hiệu?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Vì ống kính là cỗ máy dò nói dối sinh lý tàn nhẫn nhất! Văn bản có thể đánh lừa, nhưng cơ thể thì không. Kẻ giả mạo không bao giờ có các chi tiết cơ học vụn vặt. Sự gồng cứng của cơ mặt, ánh mắt tính toán và sự biến mất của nụ cười tự trào sẽ lột mặt nạ của bạn. Khách hàng mang trong mình radar sinh tồn hàng triệu năm, họ vạch trần kẻ thao túng chỉ trong chớp mắt.</p>
<blockquote>
<p><em>Văn hay chữ tốt mượn <strong>lời</strong>,</em><br/>
<em>Lên hình giả tạo rụng <strong>rời</strong> chân <strong>tay</strong>.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q103" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 103 [VŨ KHÍ CƠ HỌC LỘT TRẦN SỰ LỪA DỐI]: Hãy vứt bỏ mớ trực giác tâm lý học đi! Đâu là công thức vật lý, cơ học tuyệt đối lạnh lùng giúp tôi lột trần bộ mặt thật (Tầng 2) của bất kỳ kẻ ngụy biện nào chỉ trong đúng 3 giây giao tiếp?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Hãy vung dao mổ: Lắng nghe độ lệch. Đặt [Lời đạo lý vĩ mô] TRỪ ĐI [Thao tác cơ bắp đang bị kẹt]. Khách chê nước hồ bơi bẩn (ngôn từ), nhưng đôi chân lại khựng run ở mép nước (cơ bắp). Khoảng trống khập khiễng đó vạch trần sự thật: Họ không biết bơi và sợ sặc nước! Chân lý không nằm ở vỏ bọc ngôn từ, chân lý nằm ở khối cơ bắp đang tê liệt.</p>
<blockquote>
<p><em>Ngôn từ vỏ bọc phô <strong>trương</strong>,</em><br/>
<em>Chân tay luống cuống chỉ <strong>đường</strong> tim <strong>đen</strong>.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q104" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 104 [BẢN NĂNG SINH TỒN VÀ TỬ HUYỆT CHỐT SALE]: Khi tôi đã nắm thóp được sự ngu dốt và sợ hãi của khách, tại sao việc đập nát cái cớ đó để dồn họ vào góc tường nhận sai lại là nhát dao tự kết liễu mọi nỗ lực chuyển đổi hành vi?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Vì ép họ nhận dốt đồng nghĩa với tuyên án "Tử hình xã hội". Khi thể diện bị đe dọa, Hạch hạnh nhân (Amygdala) bơm máu, kích hoạt chế độ cắn trả. Họ thà hất đổ bàn cờ, thà chịu phá sản chứ tuyệt đối không để bạn chà đạp lòng tự trọng. Bóc mẽ để thắng một cuộc cãi vã logic, bạn vuốt ve được cái tôi của mình, nhưng vĩnh viễn mất đi dòng tiền!</p>
<blockquote>
<p><em>Dồn người góc tối đường <strong>cùng</strong>,</em><br/>
<em>Não kia đóng sập, lửa <strong>bùng</strong> oán <strong>than</strong>.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q105" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 105 [MA THUẬT QUỶ QUYỆT CỦA LỐI THOÁT DANH DỰ]: Nếu bóc trần tim đen mà không chừa đường lui là tự sát, vậy "Lối thoát danh dự" chứa chất gây nghiện gì mà khiến con người chịu ngoan ngoãn "quay xe" trong vòng một nốt nhạc?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Nó là nghệ thuật "Viết lại lý do". Khách rất khát khao mua giải pháp nhưng bị kẹt bởi sĩ diện lỡ thốt ra hôm qua, nếu tự đổi ý họ sẽ biến thành kẻ nuốt lời. Lối thoát danh dự ban cho họ một chiếc thang bọc nhung đàng hoàng hơn (VD: "Hôm qua nóng tính chắc do mệt"). Hợp pháp hóa sự yếu kém của họ, họ sẽ vớ lấy cái cớ đó như người đuối nước vớ phao, đổi thái độ ngay tắp lự mà vẫn ngẩng cao đầu.</p>
<blockquote>
<p><em>Lỡ buông lời ngạo hôm <strong>nào</strong>,</em><br/>
<em>Trao thang danh dự bước <strong>vào</strong> cho <strong>êm</strong>.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q106" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 106 [CHUYỂN ĐỔI TRẠNG THÁI MUA HÀNG BẰNG THỂ DIỆN]: Bằng cơ chế vặn xoắn tâm lý nào mà việc cấp "Lối thoát danh dự" lại biến những vị sếp bảo thủ nhất thành những kẻ quẹt thẻ mua hàng điên cuồng với niềm kiêu hãnh tột độ?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Hành vi mua hàng gián tiếp thú nhận: "Tôi bất lực". Giới tinh hoa sợ mất mặt hơn mất tiền! Nếu bạn định hình giao dịch là "vá lỗi dốt nát", họ sẽ tẩy chay. Nhưng nếu bạn nâng tầm nó lên: Bán tiếng Anh biến thành "Dạy đàm phán chiến lược"; bán phần mềm biến thành "Thuê đứa chạy việc vặt để sếp đi ngoại giao". Rút ví lúc này là nghi thức khẳng định đẳng cấp, và họ tự hào dâng tiền cho bạn.</p>
<blockquote>
<p><em>Bán buôn chớ dập lòng <strong>kiêu</strong>,</em><br/>
<em>Nâng tầm danh dự, khách <strong>tiêu</strong> bạc <strong>vàng</strong>.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q107" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 107 [BÀI TẬP SINH TỬ METACOGNITION]: Nếu nghệ thuật Storytelling thao túng hành vi nằm ở việc lột trần sự thật, thì đâu là bài tập thực chiến sinh tử, đẫm máu nhất mà tôi BẮT BUỘC phải vượt qua mỗi ngày?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Đó là năng lực "Tự bắt quả tang chính mình" (Metacognition)! Khoảnh khắc ngón tay bạn khựng lại trước một email khó, và não nôn ra cái cớ: <em>"Để mai chuẩn bị thêm cho chỉn chu"</em>. Hãy tát mình một cái và thừa nhận: <em>"Không, tao đang hèn, tao đang sợ phán xét!"</em>. Kẻ nào chưa từng nhẫn tâm lột sạch lớp vỏ đạo đức giả của chính mình, kẻ đó vĩnh viễn không đủ tư cách mổ xẻ tâm can của thiên hạ.</p>
<blockquote>
<p><em>Chưa từng lột lớp vỏ <strong>mình</strong>,</em><br/>
<em>Làm sao thấu suốt nhân <strong>tình</strong> thế <strong>gian</strong>.</em></p>
</blockquote>
</div>
</div>
"""

new_content = before_body + new_body + footer

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("SUCCESS: Part 20 updated with refined titles and poems.")
