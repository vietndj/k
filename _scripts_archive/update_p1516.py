import sys

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'r', encoding='utf-8') as f:
    content = f.read()

toc_insert = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 15: CƠ CHẾ SINH HÓA CỦA THIỀN</li>
<li><a class="ink-toc-link" href="#p15_1">1. Phá chấp huyền học</a></li>
<li><a class="ink-toc-link" href="#p15_2">2. Nguồn gốc nội tại</a></li>
<li><a class="ink-toc-link" href="#p15_3">3. Định lượng thực hành</a></li>
<li><a class="ink-toc-link" href="#p15_4">4. Đẳng cấp "Nghỉ ngơi"</a></li>

<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 16: VẬT LÝ HỌC SỰ BUÔNG XẢ</li>
<li><a class="ink-toc-link" href="#p16_q80">Q80. Con hươu rùng mình</a></li>
<li><a class="ink-toc-link" href="#p16_q81">Q81. Áo giáp cơ bắp kìm nén</a></li>
<li><a class="ink-toc-link" href="#p16_q82">Q82. Trạm kiểm duyệt vỏ não</a></li>
<li><a class="ink-toc-link" href="#p16_q83">Q83. Chiếc nồi áp suất đang sôi</a></li>
<li><a class="ink-toc-link" href="#p16_q84">Q84. Đứa trẻ sà vào lòng mẹ</a></li>
"""

body_insert = """
<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 15 -->
<h1 class="is-short">PHẦN 15: CƠ CHẾ SINH HÓA CỦA THIỀN ĐỊNH (HỆ THỐNG HÓA)</h1>
<p><em>(Dưới lăng kính phản biện sắc bén, toàn bộ mớ bòng bong thắc mắc của bạn thực chất xoay quanh 4 trục vấn đề cốt lõi:)</em></p>

<ul>
    <li id="p15_1"><strong>1. Phá chấp huyền học:</strong> Cơ chế khoa học, sinh hóa và thần kinh học vật lý thực sự đứng sau hiện tượng cơ thể rùng mình, rơi nước mắt khi thiền là gì (tuyệt đối gạt bỏ yếu tố "khí" hay "năng lượng" tâm linh)?</li>
    <li id="p15_2"><strong>2. Nguồn gốc nội tại:</strong> Giai đoạn khóc lóc, rùng mình này do tác nhân vật lý hay tâm lý nào ẩn sâu bên trong sinh ra?</li>
    <li id="p15_3"><strong>3. Định lượng thực hành:</strong> Quá trình xả rác thần kinh này diễn ra bao lâu trong toàn bộ tiến trình tu tập? Mỗi lần tọa thiền nên duy trì nó bao lâu để xả áp tối đa mà không bị quá tải?</li>
    <li id="p15_4"><strong>4. Phân biệt đẳng cấp "Nghỉ ngơi":</strong> Tại sao nghỉ ngơi thông thường (nằm ườn, lướt điện thoại, ngủ) lại bị coi là thô kệch và vô tác dụng? Bằng chứng logic nào chứng minh chỉ có thiền định mới là cú "chuyển số" thực sự?</li>
</ul>

<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 16 -->
<h1 class="is-short">PHẦN 16: HỎI ĐÁP ĐẬP TAN LẦM TƯỞNG - VẬT LÝ HỌC CỦA SỰ BUÔNG XẢ</h1>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p16_q80" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 80 [Con hươu rùng mình thoát khỏi thú dữ]: Hươu rùng mình xả độc sinh tồn, sao người lại gồng chờ nổ tung?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Hươu xả stress bằng bản năng. Người tự đầu độc bằng vỏ bọc sĩ diện. Thiền là giải phóng bản năng.</p>
<blockquote>
<p><em>Nai kia thoát nạn rùng <strong>mình</strong>,</em><br/>
<em>Người phàm nén lệ thần <strong>kinh</strong> rã rời.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p16_q81" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 81 [Lớp áo giáp cơ bắp kìm nén tổn thương]: Áo giáp kiên cường bạn mặc bảo vệ bạn hay giam hãm chính bạn?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Nó là gông cùm ép cơ bắp. Thiền đập nát áo giáp, ép bó cơ phải nhả ra và co giật.</p>
<blockquote>
<p><em>Bao năm khoác giáp oai <strong>hùng</strong>,</em><br/>
<em>Nay ngồi nhắm mắt bỗng <strong>rùng</strong> mình buông.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p16_q82" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 82 [Trạm kiểm duyệt - Vỏ não trước trán]: Đang tĩnh tâm lại khóc nấc, kẻ nào trong não vừa chết lâm sàng?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> "Trạm kiểm duyệt" sĩ diện đã sập nguồn. Vô thức không bị soi xét mới dám vùng lên dọn rác.</p>
<blockquote>
<p><em>Não người canh gác tinh <strong>ranh</strong>,</em><br/>
<em>Thiền xua ý thức lanh <strong>chanh</strong> ra ngoài.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p16_q83" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 83 [Chiếc nồi áp suất đang sôi]: Nồi sôi tắt bếp vẫn chực nổ, nằm ườn lướt web có ích gì?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Nằm nghỉ chỉ là tắt lửa bề mặt. Thiền là mở van đáy, nắp nồi phải rung rít xả áp suất.</p>
<blockquote>
<p><em>Tắt lò áp suất vẫn <strong>căng</strong>,</em><br/>
<em>Mở van xì khói xả <strong>băng</strong> muộn phiền.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p16_q84" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 84 [Đứa trẻ nín khóc sà vào lòng mẹ]: Ngã đau rớm máu không khóc, cớ sao về sà lòng mẹ lại gào?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Thần kinh chỉ xả áp khi thấy bến đỗ an toàn. Thiền chính là lòng mẹ của vô thức.</p>
<blockquote>
<p><em>Gồng mình cắn chặt bờ <strong>môi</strong>,</em><br/>
<em>Vào thiền buông xả cái <strong>tôi</strong> rã rời.</em></p>
</blockquote>
</div>
</div>
"""

q79_marker = '<li><a class="ink-toc-link" href="#p14_q79">Q79. Định lý Conant-Ashby</a></li>'
content = content.replace(q79_marker, q79_marker + '\n' + toc_insert)

split_token = '<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>'
parts = content.split(split_token)
if len(parts) >= 2:
    new_content = parts[0] + body_insert + '\n' + split_token + parts[1]
    with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: logic24.html updated with Phần 15 & Phần 16 (Q80-Q84).")
else:
    print("FAILED: split_token not found.")
