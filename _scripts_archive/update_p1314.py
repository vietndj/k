import sys

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'r', encoding='utf-8') as f:
    content = f.read()

toc_insert = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 13: HỆ THỐNG HÓA VẬT LÝ (LẦN 2)</li>
<li><a class="ink-toc-link" href="#p13_1">1. Từ chối sự sáo rỗng</a></li>
<li><a class="ink-toc-link" href="#p13_2">2. Chứng minh bằng năng lượng</a></li>
<li><a class="ink-toc-link" href="#p13_3">3. Phản xạ tự thân</a></li>
<li><a class="ink-toc-link" href="#p13_4">4. Thực nghiệm tại bàn</a></li>
<li><a class="ink-toc-link" href="#p13_5">5. Thước đo quan sát</a></li>
<li><a class="ink-toc-link" href="#p13_6">6. Ẩn dụ cơ khí</a></li>
<li><a class="ink-toc-link" href="#p13_7">7. Lộ trình thao túng</a></li>

<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 14: PHÂN TÍCH CHUYÊN SÂU CƠ HỌC</li>
<li><a class="ink-toc-link" href="#p14_q63">Q63. Cỗ máy nhiệt động lực học</a></li>
<li><a class="ink-toc-link" href="#p14_q64">Q64. Co thắt cơ hoành (Micro-apnea)</a></li>
<li><a class="ink-toc-link" href="#p14_q65">Q65. Khô cứng thanh quản (Bass loss)</a></li>
<li><a class="ink-toc-link" href="#p14_q66">Q66. Vi áp lực máu vùng gáy</a></li>
<li><a class="ink-toc-link" href="#p14_q67">Q67. Xung đột bán cầu não (Glitch)</a></li>
<li><a class="ink-toc-link" href="#p14_q68">Q68. Test tải trọng nhận thức</a></li>
<li><a class="ink-toc-link" href="#p14_q69">Q69. Tần số âm thanh (Vocal Formants)</a></li>
<li><a class="ink-toc-link" href="#p14_q70">Q70. Động học chuyển động (Lag)</a></li>
"""

body_insert = """
<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 13 -->
<h1 class="is-short">PHẦN 13: HỆ THỐNG HÓA CÂU HỎI GỐC (BÓC TÁCH VI MÔ LẦN 2)</h1>
<p><em>(Để không đi lạc vào mớ bùng nhùng của tâm lý học, đây là toàn bộ vấn đề cốt lõi mà tôi đã ném lên bàn mổ yêu cầu xử lý:)</em></p>

<ul>
    <li id="p13_1"><strong>1. Từ chối sự sáo rỗng:</strong> Loại bỏ các lý thuyết "nơ-ron gương", "trực giác thấu cảm". Cần một lý giải thuần Vật lý, Nhiệt động lực học và Sinh học tiến hóa về năng lực phát hiện nói dối của con người.</li>
    <li id="p13_2"><strong>2. Chứng minh bằng năng lượng:</strong> Tại sao nói sự thật (Tầng 2.5) lại là trạng thái năng lượng cực tiểu (Ground State), còn diễn kịch (Tầng 1, Tầng 2) là trạng thái ép xung gây ma sát và rò rỉ nhiệt lượng?</li>
    <li id="p13_3"><strong>3. Phản xạ tự thân:</strong> 5 biến đổi vật lý mất kiểm soát nào xảy ra ở cấp độ mili-giây tố cáo chính tôi khi tôi nói dối?</li>
    <li id="p13_4"><strong>4. Thực nghiệm tại bàn:</strong> Bài test vật lý cụ thể nào ép cơ thể tôi sập nguồn ngay lập tức khi mồm tôi bốc phét?</li>
    <li id="p13_5"><strong>5. Thước đo quan sát:</strong> Máy quay và màng nhĩ khán giả dùng các thông số cơ học/động học nào để "đọc vị" kẻ lùa gà?</li>
    <li id="p13_6"><strong>6. Ẩn dụ cơ khí:</strong> Cần các ẩn dụ sắc lạnh (máy phát điện, bánh xe, mạch điện) để đập tan ngụy biện của người học vẹt kịch bản, trẻ con cũng hiểu được.</li>
    <li id="p13_7"><strong>7. Lộ trình thao túng:</strong> Lộ trình 4 bước đanh thép (Phá ngụy biện -> Gài bẫy tự thân -> Đối chiếu thép -> Chốt hạ vũ khí Tầng 2.5 bằng định lý Conant-Ashby).</li>
</ul>

<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 14 -->
<h1 class="is-short">PHẦN 14: HỎI ĐÁP ĐẬP TAN LẦM TƯỞNG - PHÂN TÍCH CHUYÊN SÂU CƠ HỌC</h1>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q63" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 63 [Cỗ máy Sinh học Nhiệt động lực học & Sự ép xung CPU]: Bỏ mác tâm lý rẻ tiền, cỗ máy sinh học thực chất ngửi thấy mùi gì từ kẻ dối trá?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Mùi khét của CPU ép xung. Sự thật là ổ cứng chạy không ma sát. Kịch bản giả bắt não phải "ép xung" render 3D, xả rác nhiệt lượng ra ngoài.</p>
<blockquote>
<p><em>Sự thật tĩnh lặng an <strong>nhàn</strong>,</em><br/>
<em>Ép xung dối trá nhiệt <strong>tràn</strong> nóng ran.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q64" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 64 [Sự co thắt cơ hoành & Vi ngắt quãng nhịp thở - Micro-apnea]: Tại sao kẻ bốc phét lại tự nhiên đứt hơi, vỡ vụn từ ngữ ở cuối câu?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Do phản xạ sinh tồn. Bơm cơ hoành bị khóa chặt để bảo vệ nội tạng, phổi phải thở nông bằng ngực trên gây đứt gãy nhịp điệu sinh học.</p>
<blockquote>
<p><em>Cơ hoành co thắt nghẹn <strong>ngào</strong>,</em><br/>
<em>Phổi trên thở gấp hơi <strong>trào</strong> vỡ đôi.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q65" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 65 [Khô cứng dây thanh quản & Mất dải tần trầm - Bass loss]: Vì sao giọng kẻ rao giảng đạo lý giả tạo luôn mất trầm, chua chát và the thé?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Adrenaline kéo căng cơ cổ bảo vệ động mạch. Dây thanh âm bị vặn lố tay, mất hẳn âm vực ngực dày dặn, văng tuột lên khoang mũi.</p>
<blockquote>
<p><em>Thanh âm căng cứng sai <strong>đường</strong>,</em><br/>
<em>Mất trầm chua chát thảm <strong>thương</strong> nhĩ màng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q66" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 66 [Vi áp lực máu vùng gáy/tai - Micro-vasodilation]: Mạch máu vùng gáy và tai tố cáo bí mật gì khi vỏ não cố nặn kịch bản?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Tản nhiệt khẩn cấp. Bộ não chạy kịch bản giả bị quá tải nhiệt, ép hệ tuần hoàn giãn mao mạch lập tức để xả rác năng lượng.</p>
<blockquote>
<p><em>Máu dồn tản nhiệt lan <strong>man</strong>,</em><br/>
<em>Gáy tai ửng đỏ dối <strong>gian</strong> cúi đầu.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q67" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 67 [Xung đột bán cầu não & Giật lag cơ học - Glitch]: Mép giật méo mó, mắt chớp loạn nhịp phản ánh lỗi vật lý nào của bộ não?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Xung đột băng thông cực hạn. Não trái nặn logic giả, não phải bị bỏ đói, gây ra cú "giật lag" chập mạch trên hệ vận động cơ mặt.</p>
<blockquote>
<p><em>Bán cầu giằng xé nông <strong>sâu</strong>,</em><br/>
<em>Mép giật mắt chớp rớt <strong>câu</strong> bẽ bàng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q68" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 68 [BÀI TEST Tải trọng nhận thức - Cốc nước đầy]: Làm sao ép bộ não kẻ bốc phét phải tự ngắt cầu dao ngay tại chỗ?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Bắt nó đa nhiệm: Đứng một chân, bưng ly nước đầy, miệng nói dối. Não thiếu ATP giữ thăng bằng, lập tức sập nguồn tay chân dồn điện lên mồm.</p>
<blockquote>
<p><em>Co chân tay giữ chén <strong>vàng</strong>,</em><br/>
<em>Nói điêu một tiếng bẽ <strong>bàng</strong> đổ ngay.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q69" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 69 [Thước đo Tần số âm thanh - Vocal Formants]: Máy quay và màng nhĩ khán giả quét trúng tần số nào để chốt hạ kẻ giả tạo?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Sóng ngắn khoang mũi. Sự thật tạo sóng dài dội từ ngực. Kịch bản bị nghẽn ở hoành cách mô, ép tạo ra sóng bẹt the thé rác rưởi.</p>
<blockquote>
<p><em>Chân ngôn lồng ngực vút <strong>bay</strong>,</em><br/>
<em>Gian dối kẹt mũi đắng <strong>cay</strong> sóng tàn.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p14_q70" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 70 [Thước đo Động học chuyển động - Độ trễ Lag mili-giây]: Đòn chí mạng nào bóc trần sự lệch pha của kẻ cố tình diễn body language?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Độ trễ mili-giây. Nói thật: Não xử lý song song, miệng và tay đồng bộ. Diễn kịch: Xử lý nối tiếp, mồm nhả chữ xong 0.5 giây tay mới vung.</p>
<blockquote>
<p><em>Miệng vừa dứt chữ vội <strong>vàng</strong>,</em><br/>
<em>Tay vung nửa nhịp bẽ <strong>bàng</strong> lệch pha.</em></p>
</blockquote>
</div>
</div>
"""

content = content.replace('</ul>\n</aside>', toc_insert + '\n</ul>\n</aside>')

split_token = '<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>'
parts = content.split(split_token)

if len(parts) >= 2:
    new_content = parts[0] + body_insert + '\n' + split_token + parts[1]
    with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: logic24.html updated with Phần 13 & Phần 14.")
else:
    print("FAILED: split_token not found.")

