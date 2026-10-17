import sys

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'r', encoding='utf-8') as f:
    content = f.read()

toc_insert = """<li><a class="ink-toc-link" href="#p14_q71">Q71. Đóng băng vi mô (Micro-freezing)</a></li>
<li><a class="ink-toc-link" href="#p14_q72">Q72. Cỗ máy phát điện lệch pha</a></li>
<li><a class="ink-toc-link" href="#p14_q73">Q73. Bánh xe cong vành</a></li>
<li><a class="ink-toc-link" href="#p14_q74">Q74. Băng thông 40 bits vs 11 triệu</a></li>
<li><a class="ink-toc-link" href="#p14_q75">Q75. Mạch điện đoản mạch</a></li>
<li><a class="ink-toc-link" href="#p14_q76">Q76. B2: Gài bẫy tự thân</a></li>
<li><a class="ink-toc-link" href="#p14_q77">Q77. B3: Mute Tracking</a></li>
<li><a class="ink-toc-link" href="#p14_q78">Q78. B4: Hack Zero Friction</a></li>
<li><a class="ink-toc-link" href="#p14_q79">Q79. Định lý Conant-Ashby</a></li>"""

body_insert = """
<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q71" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 71 [Thước đo Trương lực cơ - Phản xạ Đóng băng vi mô (Micro-freezing)]: Tại sao kẻ học thuộc kịch bản lại mất đi sự uyển chuyển tự nhiên của con người?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Phản xạ đóng băng ẩn nấp. Cỗ máy duy trì trương lực cơ giao cảm cao độ: Mắt ngừng chớp, bả vai gồng cứng để tập trung 100% RAM render dữ liệu giả.</p>
<blockquote>
<p><em>Cơ gồng phản xạ co <strong>ro</strong>,</em><br/>
<em>Đóng băng cơ bắp tàn <strong>tro</strong> vở tuồng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q72" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 72 [Cỗ máy phát điện lệch pha (Lốc máy xóc nảy)]: Cái cớ thanh cao Tầng 1, Tầng 2 giống cỗ máy hỏng hóc ở điểm nào?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Trục xoay lệch tâm. Vỏ ngoài sơn bóng, nhưng bên trong lốc máy ma sát, nảy bần bật. Khán giả chạm vào thấy rung rát, lập tức lùi lại sợ nổ.</p>
<blockquote>
<p><em>Máy kia lệch trục sai <strong>đường</strong>,</em><br/>
<em>Bề ngoài bóng lộn thảm <strong>thương</strong> rã rời.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q73" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 73 [Chiếc bánh xe cong vành (Sự thật tĩnh vs Lời nói dối móp méo)]: Viết content chữ thì êm ru, tại sao mở miệng lên video lại lộn ruột?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Do lực ly tâm cơ học. Bánh xe cong vành (lời nói dối), dắt bộ thì không sao. Nhưng đạp tốc độ cao (nói trước ống kính), nó xóc nảy nghiền nát uy tín.</p>
<blockquote>
<p><em>Vành cong móp méo tơi <strong>bời</strong>,</em><br/>
<em>Đạp nhanh xóc nảy rụng <strong>rời</strong> cốt xương.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q74" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 74 [Bức tường Giấy ăn 40 bits vs Bom hạt nhân 11 Triệu bits]: Tại sao ngụy biện "Em diễn chưa tự nhiên" là sự ngu dốt tận cùng về Vật lý?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Chênh lệch băng thông tàn khốc. Ý thức rặn nụ cười chỉ xử lý 40 bits/s, trong khi hệ thần kinh thực vật xả rác 11 triệu bits/s. Không thể giấu!</p>
<blockquote>
<p><em>Bốn mươi bit mỏng che <strong>mành</strong>,</em><br/>
<em>Triệu luồng xả rác tanh <strong>bành</strong> dối gian.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q75" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 75 [Mạch điện bị đoản mạch (Short circuit) qua ngàn điện trở]: Biểu hiện vấp váp, sượng trân khi nói dối bắt nguồn từ nguyên lý điện học nào?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Sự đoản mạch. Dòng điện sự thật bị ép đi vòng vèo qua hàng chục điện trở kiểm duyệt của vỏ não, dẫn đến quá tải sập nguồn hệ thống tức thì.</p>
<blockquote>
<p><em>Mạch phùng điện trở lan <strong>man</strong>,</em><br/>
<em>Quá tải sập nguồn vỡ <strong>tan</strong> nụ cười.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q76" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 76 [BƯỚC 2 - Gài bẫy tự thân (Tắt chế độ tản nhiệt)]: Cách tàn độc nhất để ép kẻ đạo lý vấp đĩa, chết đứng trước ống kính là gì?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Ép họ vào khuôn vật lý: Cấm chớp mắt, buông thõng vai, thở phình bụng. Khi bị cắt đứt cơ chế "gồng tản nhiệt", hệ thống dối trá lập tức sập nguồn.</p>
<blockquote>
<p><em>Cấm gồng thở bụng oái <strong>oăm</strong>,</em><br/>
<em>Sập nguồn vấp đĩa tối <strong>tăm</strong> mặt mày.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q77" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 77 [BƯỚC 3 - Bằng chứng đối chiếu thép (Mute Tracking)]: Làm sao khóa mõm kẻ lùa gà bằng thông số động học không thể chối cãi?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Tắt sạch âm thanh, tua chậm 0.5x. Màng lọc ngôn ngữ tâm lý bị tiêu diệt, chỉ còn trơ trọi sự "lag" mili-giây đứt gãy giữa cơ miệng và tay vung.</p>
<blockquote>
<p><em>Tắt âm tua chậm phơi <strong>bày</strong>,</em><br/>
<em>Thân gồng tay trễ mặt <strong>mày</strong> sượng trân.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q78" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 78 [BƯỚC 4 - Vũ khí chốt hạ Tầng 2.5 (Trạng thái Zero Friction)]: Xé toạc sự nhục nhã Tầng 2.5 mang lại quyền lực tối thượng nào?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Hack băng thông vô cực. Không ma sát, không rò rỉ nhiệt. Bức xạ phát ra vô khuẩn, màng nhĩ khách hàng quét trúng tín hiệu an toàn tự động tháo giáp.</p>
<blockquote>
<p><em>Chân thành ma sát bằng <strong>không</strong>,</em><br/>
<em>Băng thông vô cực mênh <strong>mông</strong> dội trào.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q79" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 79 [Định lý Conant-Ashby & Ngôi vương chốt sale]: Vì sao khi tôi bóc trần khe hở hèn nhát, khách hàng lại tự nguyện nộp mạng?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Định luật điều khiển hệ thống. Ai gọi tên được chính xác lỗi của cỗ máy, não bộ người xem mặc định kẻ đó nắm giữ phương thuốc giải độc cuối cùng.</p>
<blockquote>
<p><em>Gọi tên khe hở đớn <strong>đau</strong>,</em><br/>
<em>Ngai vàng thuốc giải chốt <strong>mau</strong> thế thời.</em></p>
</blockquote>
</div>
</div>
"""

q70_marker = '<li><a class="ink-toc-link" href="#p14_q70">Q70. Động học chuyển động (Lag)</a></li>'
content = content.replace(q70_marker, q70_marker + '\n' + toc_insert)

split_token = '<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>'
parts = content.split(split_token)
if len(parts) >= 2:
    new_content = parts[0] + body_insert + '\n' + split_token + parts[1]
    with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: logic24.html updated with Q71-Q79.")
else:
    print("FAILED: split_token not found.")
