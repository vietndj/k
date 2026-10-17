import sys

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'r', encoding='utf-8') as f:
    content = f.read()

toc_insert = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 17: CƠ CHẾ TUỆ GIÁC</li>
<li><a class="ink-toc-link" href="#p17_1">1. Sự bất lực của Logic</a></li>
<li><a class="ink-toc-link" href="#p17_2">2. Cơ chế của Tia Laser</a></li>
<li><a class="ink-toc-link" href="#p17_3">3. Cách tiếp cận</a></li>
<li><a class="ink-toc-link" href="#p17_4">4. Bẫy của kỳ vọng</a></li>

<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 18: VƯỢT THOÁT LOGIC</li>
<li><a class="ink-toc-link" href="#p18_q90">Q90. Quả chanh vs Công thức</a></li>
<li><a class="ink-toc-link" href="#p18_q91">Q91. Bóng đèn và Tia Laser</a></li>
<li><a class="ink-toc-link" href="#p18_q92">Q92. Đầu gối và Pixel năng lượng</a></li>
<li><a class="ink-toc-link" href="#p18_q93">Q93. Tấm bản đồ và Cơn đói</a></li>
<li><a class="ink-toc-link" href="#p18_q94">Q94. Kính hiển vi và Vi khuẩn</a></li>
<li><a class="ink-toc-link" href="#p18_q95">Q95. Bản vẽ cấu tạo quả bom</a></li>
<li><a class="ink-toc-link" href="#p18_q96">Q96. Lập trình VR và Game kinh dị</a></li>
<li><a class="ink-toc-link" href="#p18_q97">Q97. Vỏ não và Hạch hạnh nhân</a></li>
<li><a class="ink-toc-link" href="#p18_q98">Q98. Tranh ảo ảnh 3D</a></li>
<li><a class="ink-toc-link" href="#p18_q99">Q99. Ép bản thân ngủ</a></li>
"""

body_insert = """
<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 17 -->
<h1 class="is-short">PHẦN 17: SỰ BẤT LỰC CỦA LOGIC VÀ CƠ CHẾ TUỆ GIÁC (HỆ THỐNG HÓA)</h1>
<p><em>(Bạn đã đặt ra 4 nút thắt lớn nhất của một bộ não thiên về logic khi đứng trước cánh cửa thiền định:)</em></p>

<ul>
    <li id="p17_1"><strong>1. Sự bất lực của Logic:</strong> Tại sao tôi hiểu tường tận (bản chất lượng tử/trống rỗng/sự kết xuất của não bộ) nhưng vẫn bị cuốn vào thực tại? Tuệ Giác là cái quái gì nếu nó nằm ngoài logic?</li>
    <li id="p17_2"><strong>2. Cơ chế của Tia Laser:</strong> Làm sao mô tả "Tia Laser" quét vào cơ thể? Nó hoạt động thế nào để phá vỡ ảo giác thực tại?</li>
    <li id="p17_3"><strong>3. Cách tiếp cận:</strong> Có cách nào dùng logic để tiến vào không, hay bắt buộc phải chờ đợi?</li>
    <li id="p17_4"><strong>4. Bẫy của kỳ vọng:</strong> Nếu bắt buộc phải chờ đợi, thì tôi đang chờ cái gì?</li>
</ul>

<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 18 -->
<h1 class="is-short">PHẦN 18: HỎI ĐÁP ĐẬP TAN LẦM TƯỞNG - VƯỢT THOÁT LOGIC</h1>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p18_q90" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 90 [Quả chanh thật và Công thức Hóa học]: Nhai thuộc lòng công thức hóa học, miệng bạn có ứa nước bọt không?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Không. Logic chỉ cung cấp công thức, hệ thần kinh chỉ thực sự phản ứng khi tự mình cắn vào thực tại.</p>
<blockquote>
<p><em>Đọc ngàn công thức rõ <strong>rành</strong>,</em><br/>
<em>Chưa nhai chanh thật, sao <strong>thành</strong> vị chua?</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p18_q91" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 91 [Bóng đèn sợi đốt và Tia Laser]: Đem bóng đèn lờ mờ đi cắt kim loại, bao giờ mới đứt?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Vô vọng. Ánh sáng loe loe là tâm phân tán. Gom cạn tài nguyên chú ý thành tia laser mới xuyên thủng huyễn ảnh.</p>
<blockquote>
<p><em>Đèn mờ chiếu tỏ loanh <strong>quanh</strong>,</em><br/>
<em>Phải gom tụ lại mới <strong>nhanh</strong> chẻ hình.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p18_q92" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 92 [Cái đầu gối rắn chắc và Hạt Pixel năng lượng]: Cơn đau gối là khối đá ngàn cân hay cú lừa của thần kinh?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Là cú lừa đồ họa. Dưới tia laser tập trung, nó lập tức vỡ vụn thành các pixel nhấp nháy sinh diệt.</p>
<blockquote>
<p><em>Ngỡ đau là một khối <strong>bền</strong>,</em><br/>
<em>Soi vào mới thấy nổi <strong>lên</strong> bọt bèo.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p18_q93" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 93 [Tấm bản đồ và Cơn đói]: Nắm trong tay tấm bản đồ chi tiết, bạn đã no bụng chưa?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Bản đồ chỉ đường đi, không thể nhai nuốt. Logic đưa bạn đến trước cửa, nhưng bắt buộc bạn phải tự ghé mắt nhìn.</p>
<blockquote>
<p><em>Bản đồ chỉ lối đường <strong>xa</strong>,</em><br/>
<em>Gặm giấy sao no dạ <strong>ta</strong> hỡi người.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p18_q94" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 94 [Kính hiển vi và Con vi khuẩn]: Soi kính hiển vi rồi ngồi chắp tay đợi vi khuẩn diễn kịch?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Thật lố bịch. Không mong cầu, không kịch bản, cứ lạnh lùng quan sát sự thật thô ráp đang phơi bày.</p>
<blockquote>
<p><em>Soi kính đừng đợi trò <strong>vui</strong>,</em><br/>
<em>Chỉ nhìn sự thật đang <strong>chui</strong> ra ngoài.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p18_q95" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 95 [Bản vẽ cấu tạo quả bom]: Hiểu tường tận bản vẽ cấu trúc bom, bạn có thoát cảnh tan xác?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Vô ích. Khi thực tại dội tới, logic chết đứng; chỉ có sự tỉnh giác mới đỡ được đòn đau.</p>
<blockquote>
<p><em>Thuộc lòng bản vẽ trên <strong>tay</strong>,</em><br/>
<em>Bom nổ xác vẫn bay <strong>ngay</strong> lên trời.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p18_q96" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 96 [Lập trình viên VR, game kinh dị và Tốc độ khung hình]: Biết game kinh dị là mã code giả, sao tim đập, chân vẫn run?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Vì não bạn "render" quá mượt. Cần tia laser ép tụt khung hình để tự mắt bắt quả tang mã nguồn ảo ảnh.</p>
<blockquote>
<p><em>Kính ảo chớp mắt lừa <strong>người</strong>,</em><br/>
<em>Ép cho rớt nhịp, bật <strong>cười</strong> vì không.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p18_q97" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 97 [Vỏ não (Tổng giám đốc) và Hạch hạnh nhân (Chó canh cửa)]: Mang báo cáo lượng tử đi khuyên một con chó dại ngừng cắn?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Điên rồ. Chó chỉ hiểu cảm giác sinh lý. Giữ yên lặng, không phán xét, hệ thống báo động sẽ tự động tắt điện.</p>
<blockquote>
<p><em>Chó điên sủa gắt ngoài <strong>sân</strong>,</em><br/>
<em>Giảng đạo lý, nó cắn <strong>chân</strong> máu trào.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p18_q98" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 98 [Bức tranh ảo ảnh 3D (Magic Eye)]: Căng não phân tích từng vệt màu có khiến con khủng long lồi lên?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Hoàn toàn bất lực. Buông lỏng tiêu cự, giữ yên ánh nhìn, đồ họa 3D sẽ tự động nổ tung thẳng vào nhận thức.</p>
<blockquote>
<p><em>Căng mắt phân tích màu <strong>pha</strong>,</em><br/>
<em>Nhìn xuyên ảo ảnh, hiện <strong>ra</strong> thú liền.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p18_q99" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 99 [Nằm trằn trọc ép bản thân đi vào giấc ngủ]: Căng não tính toán thời gian chờ ngủ, đến kiếp nào mới thiếp đi?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Càng chờ đợi, càng tỉnh như sáo. Chờ đợi chĩa camera về tương lai, trong khi thực tại chỉ render ở hiện tại.</p>
<blockquote>
<p><em>Trằn trọc ngóng đợi mộng <strong>vàng</strong>,</em><br/>
<em>Càng ép càng tỉnh, võng <strong>màng</strong> thêm đau.</em></p>
</blockquote>
</div>
</div>
"""

q89_marker = '<li><a class="ink-toc-link" href="#p16_q89">Q89. Nước mắt sinh hóa</a></li>'
content = content.replace(q89_marker, q89_marker + '\n' + toc_insert)

split_token = '<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>'
parts = content.split(split_token)
if len(parts) >= 2:
    new_content = parts[0] + body_insert + '\n' + split_token + parts[1]
    with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: logic24.html updated with Q90-Q99.")
else:
    print("FAILED: split_token not found.")
