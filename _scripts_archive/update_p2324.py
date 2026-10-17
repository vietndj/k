import sys

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'r', encoding='utf-8') as f:
    content = f.read()

toc_insert = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 23: TỬ HUYỆT XAO NHÃNG</li>
<li><a class="ink-toc-link" href="#p23_1">1. Bản chất sự Hội tụ</a></li>
<li><a class="ink-toc-link" href="#p23_2">2. Giải phẫu cơn đói tâm trí</a></li>
<li><a class="ink-toc-link" href="#p23_3">3. Bóc trần logic ngụy biện</a></li>
<li><a class="ink-toc-link" href="#p23_4">4. Vũ khí thực chiến</a></li>
<li><a class="ink-toc-link" href="#p23_5">5. Triết lý tĩnh lặng</a></li>

<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 24: BẺ KHÓA SỰ TẬP TRUNG</li>
<li><a class="ink-toc-link" href="#p24_q115">Q115. Cơn đói tâm trí</a></li>
<li><a class="ink-toc-link" href="#p24_q116">Q116. Màng lọc RAS</a></li>
<li><a class="ink-toc-link" href="#p24_q117">Q117. Thú hoang nỗ lực</a></li>
<li><a class="ink-toc-link" href="#p24_q118">Q118. Tàn dư chú ý</a></li>
<li><a class="ink-toc-link" href="#p24_q119">Q119. Nhiễu tích trữ</a></li>
<li><a class="ink-toc-link" href="#p24_q120">Q120. Nhiễu cảnh giác</a></li>
<li><a class="ink-toc-link" href="#p24_q121">Q121. Nhiễu năng suất giả</a></li>
<li><a class="ink-toc-link" href="#p24_q122">Q122. Phương pháp 1 vạch</a></li>
<li><a class="ink-toc-link" href="#p24_q123">Q123. Mặt hồ bùn & Chiếc thìa</a></li>
<li><a class="ink-toc-link" href="#p24_q124">Q124. Kính lúp & Laser</a></li>
<li><a class="ink-toc-link" href="#p24_q125">Q125. Vua và hề nịnh thần</a></li>
<li><a class="ink-toc-link" href="#p24_q126">Q126. Tượng cẩm thạch</a></li>
<li><a class="ink-toc-link" href="#p24_q127">Q127. Máy dò sóng radio</a></li>
"""

body_insert = """
<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 23 -->
<h1 class="is-short">PHẦN 23: TỬ HUYỆT XAO NHÃNG (HỆ THỐNG HÓA)</h1>
<p><em>(Dưới lăng kính mổ xẻ tâm lý học và thần kinh học, toàn bộ những thắc mắc của bạn trải dài từ hiện tượng bề mặt đến phần rễ sâu nhất của tâm trí, được hệ thống hóa thành 5 tử huyệt sau:)</em></p>

<ul>
    <li id="p23_1"><strong>1. Bản chất của sự Hội tụ:</strong> Tại sao khi khóa tâm trí vào một mục tiêu sống còn (Tín hiệu), các khao khát xao nhãng (mua sắm, tò mò) tự động bị dập tắt? Cơ chế này tạo ra dòng chảy hội tụ năng lượng như thế nào?</li>
    <li id="p23_2"><strong>2. Giải phẫu "Cơn đói Tâm trí":</strong> Nguyên lý rò rỉ sinh lực diễn ra ra sao (What/Why/How)? Tại sao tâm trí luôn lang thang đi lùng sục "dopamine mẩu vụn" rẻ tiền thay vì đối mặt với việc cốt lõi?</li>
    <li id="p23_3"><strong>3. Bóc trần Logic Ngụy biện:</strong> Các loại xao nhãng (Nhiễu tích trữ, Nhiễu cảnh giác, Nhiễu năng suất giả) đang sử dụng những lý lẽ sinh tồn tinh vi thời nguyên thủy nào để đánh lừa nhận thức của bạn?</li>
    <li id="p23_4"><strong>4. Vũ khí Thực chiến:</strong> Làm sao để đập bỏ bộ 4 câu hỏi rườm rà, thay bằng một vũ khí mang tính bạo lực, trực diện và dễ nhớ nhất trên giấy bút để ép bản thân chốt được Tín hiệu ngay lập tức?</li>
    <li id="p23_5"><strong>5. Triết lý Tĩnh lặng & Lối sống:</strong> Có phải giấy bút chỉ là bề nổi? Năng lực thực sự để bắt được Tín hiệu vốn dĩ không nằm ở thủ thuật logic, mà là thành quả của "Sự tĩnh lặng" được tích lũy từ phong cách sống kỷ luật mỗi ngày?</li>
</ul>

<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 24 -->
<h1 class="is-short">PHẦN 24: BẺ KHÓA SỰ TẬP TRUNG</h1>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q115" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 115 [Cơn đói tâm trí & Đồ ăn vặt lề đường]: Bạn lướt web để xả stress, hay tâm trí đang chết đói?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Khi thiếu vắng mục tiêu sinh tử, bộ não bơ vơ đành nhai ngấu nghiến những khoái cảm rác rưởi.</p>
<blockquote>
<p><em>Tâm trí đói khát bơ <strong>vơ</strong>,</em><br/>
<em>Nhai mẩu vụn rác hững <strong>hờ</strong> cho qua.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q116" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 116 [Hệ thống Lưới Hoạt hóa - RAS]: Phải dùng ý chí sắt đá để nhịn mua sắm khi làm việc?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Không hề! Màng lọc sinh học tự động dán nhãn xao nhãng là rác và chặn đứng nó trước ý thức.</p>
<blockquote>
<p><em>Ý chí gồng gánh mệt <strong>nhoài</strong>,</em><br/>
<em>Màng lọc kích hoạt vứt <strong>ngoài</strong> rác dơ.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q117" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 117 [Con thú hoang dã & Nỗ lực tối thiểu]: Trì hoãn vì lười biếng, hay vì con thú trong bạn kinh hãi?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Bản năng sinh tồn nguyên thủy lừa bạn chọn việc dễ để tiết kiệm calo, chối bỏ sự vất vả.</p>
<blockquote>
<p><em>Thú hoang sợ tốn sức <strong>mình</strong>,</em><br/>
<em>Núp vào mạng ảo mặc <strong>tình</strong> rong chơi.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q118" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 118 [Tàn dư chú ý & Bình xăng đục lỗ]: Nghỉ giải lao lướt điện thoại 5 phút có giúp bạn hồi sinh lực?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Đóng mở bối cảnh liên tục sẽ đục thủng bình năng lượng, cướp đoạt trực tiếp sinh lực của bạn.</p>
<blockquote>
<p><em>Chuyển kênh hao tổn tinh <strong>thần</strong>,</em><br/>
<em>Bình xăng thủng lỗ bào <strong>dần</strong> sức trai.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q119" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 119 [Nhiễu Tích trữ & Tập tính Hái lượm]: Sắm thêm đồ nghề để làm việc hiệu quả hay đang lẩn trốn?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Bạn chỉ đang mua "ảo giác kiểm soát" hòng trốn chạy sự bế tắc của công việc hiện tại.</p>
<blockquote>
<p><em>Chốt đơn ngỡ để tiến <strong>lên</strong>,</em><br/>
<em>Hóa ra mượn cớ để <strong>quên</strong> nhọc nhằn.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q120" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 120 [Nhiễu Cảnh giác & Tập tính Bầy đàn]: Hóng drama mạng để khỏi "tối cổ" hay đang tự nốc thuốc độc?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Não bộ lừa bạn tiêu thụ rác rưởi để nạp cảm giác an toàn bầy đàn một cách giả tạo.</p>
<blockquote>
<p><em>Sợ bầy đàn bỏ đằng <strong>sau</strong>,</em><br/>
<em>Hóng tin rác rưởi đâm <strong>nhau</strong> rách hồn.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q121" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 121 [Nhiễu Năng suất giả & Tránh né nỗi đau]: Chăm chỉ dọn bàn làm việc sát deadline là minh chứng kỷ luật?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Đó là sự lẩn trốn tinh vi. Bạn dùng việc cỏn con để trốn chạy tử huyệt đẫm máu.</p>
<blockquote>
<p><em>Cắm đầu dọn dẹp mặt <strong>bàn</strong>,</em><br/>
<em>Chỉ là trốn việc muôn <strong>vàn</strong> hóc xương.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q122" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 122 [Phương pháp 1 vạch kẻ & Vũ khí 3 chữ T]: Dùng 4 câu hỏi logic dài dòng có dập tắt được cơn nghiện?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Không! Cơn nghiện cần một nhát chém bạo lực vạch thẳng lên giấy để lột trần sự ngụy biện.</p>
<blockquote>
<p><em>Một đường chia nửa giấy <strong>nay</strong>,</em><br/>
<em>Vạch trần lẩn trốn ra <strong>tay</strong> chém liền.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q123" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 123 [Mặt hồ bùn & Chiếc thìa]: Càng vắt óc phân tích, tâm trí càng trở nên minh mẫn hơn?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Suy nghĩ logic là chiếc thìa khuấy bùn, càng khuấy càng đục. Sự tĩnh lặng mới làm ngọc hiện hình.</p>
<blockquote>
<p><em>Lấy thìa khuấy nước hồ <strong>sâu</strong>,</em><br/>
<em>Bùn văng vẩn đục biết <strong>đâu</strong> tỏ mờ.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q124" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 124 [Kính lúp & Mũi khoan laser]: Đa nhiệm làm nhiều việc cùng lúc là năng suất hay tự sát?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Năng lượng phân tán vô hại như nắng, hội tụ qua kính lúp mới thành tia laser thiêu rụi trở ngại.</p>
<blockquote>
<p><em>Nắng vương tản mác nhạt <strong>nhòa</strong>,</em><br/>
<em>Gom vào một điểm chói <strong>lòa</strong> hào quang.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q125" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 125 [Vị Vua & Lũ hề nịnh thần]: Phải khổ sở vung gươm ý chí để chống lại bầy xao nhãng?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Vua uy nghi tĩnh tại hướng về đại sự, lũ hề xao nhãng sợ hãi sẽ tự động câm nín lui bước.</p>
<blockquote>
<p><em>Vua say hề múa loạn <strong>nhà</strong>,</em><br/>
<em>Vua ngồi tĩnh tại yêu <strong>ma</strong> cúi đầu.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q126" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 126 [Tượng Cẩm thạch của Michelangelo]: Tín hiệu là thứ xa xôi cần phải vất vả bới móc tìm kiếm?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Tín hiệu đã có sẵn trong tâm. Sự tĩnh lặng là nhát búa gọt đi những lớp đá ồn ào thừa thãi.</p>
<blockquote>
<p><em>Tượng thần nấp giữa đá <strong>thô</strong>,</em><br/>
<em>Gõ đi vụn vặt để <strong>phô</strong> dáng hình.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p24_q127" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 127 [Máy dò sóng Radio & Ắc-quy gỉ sét]: Vài mẹo logic có cứu vớt được một lối sống nát bét không?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Pin cạn, máy hỏng vặn gãy tay cũng chỉ thu được tiếng rè. Sống kỷ luật mới bắt sóng tín hiệu.</p>
<blockquote>
<p><em>Thân tàn máy rỉ tả <strong>tơi</strong>,</em><br/>
<em>Sóng kêu rền rĩ chơi <strong>vơi</strong> mịt mù.</em></p>
</blockquote>
</div>
</div>
"""

q114_marker = '<li><a class="ink-toc-link" href="#p22_q114">Q114. 10 định luật sinh tồn</a></li>'
content = content.replace(q114_marker, q114_marker + '\n' + toc_insert)

parts_body = content.split('</article>', 1)
new_content = parts_body[0] + body_insert + '\n</article>' + parts_body[1]

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SUCCESS: logic24.html updated with Q115-Q127.")
