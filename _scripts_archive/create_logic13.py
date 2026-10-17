import re

with open('logic12.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Document Title
title_pattern = r'<title>.*?</title>'
content = re.sub(title_pattern, '<title>[INKDOC-13] VIDEO STORYTELLING</title>', content)

# 2. Update TOC
new_toc = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">VIDEO STORYTELLING</li>
<li><a class="ink-toc-link" href="#q1">Q1. Cú lừa căn phòng tối</a></li>
<li><a class="ink-toc-link" href="#q2">Q2. Cò súng tâm trí</a></li>
<li><a class="ink-toc-link" href="#q3">Q3. Bản chất cảnh trám</a></li>
<li><a class="ink-toc-link" href="#q4">Q4. Kẻ chưa mất tiền</a></li>
<li><a class="ink-toc-link" href="#q5">Q5. Đòn thực chiến</a></li>
"""
toc_pattern = r'(<ul class="ink-toc-list">).*?(</ul>)'
content = re.sub(toc_pattern, r'\1\n' + new_toc + r'\n\2', content, flags=re.DOTALL)

# 3. Update Content
new_content = """
<h1 class="is-short">VIDEO STORYTELLING: NGHỆ THUẬT THAO TÚNG TÂM TRÍ</h1>
<div class="ink-meta">
  <span>System Identity: [INKDOC-13]</span>
  <span class="mx-2">•</span>
  <span>Render Mode: [Dialogue]</span>
</div>

<div style="margin-bottom: 3rem;">
    <p>Dưới đây là toàn bộ tinh hoa của nghệ thuật "Thao túng tâm trí qua Video Storytelling", được nén lại thành định dạng <strong>Hỏi - Đáp (Q&A) cực gắt</strong>.</p>
    <p>Các câu hỏi được thiết kế sắc bén như dao mổ để đập tan sự kiêu ngạo của lý trí, câu trả lời bóc trần bản chất tâm lý học hành vi một cách tàn nhẫn nhất. Ở cuối mỗi câu, tôi đã khóa lại bằng đúng 2 câu thơ lục bát chuẩn luật Bằng - Trắc và gieo vần chính xác ở chữ thứ 6.</p>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q1" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q1: CÚ LỪA CỦA CĂN PHÒNG TỐI<br>Chúng ta luôn kiêu hãnh cho rằng mình đủ thông minh để phân biệt đời thực và những video "chém gió" trên mạng. Sự thật phũ phàng nào chứng minh bộ não vĩ đại của bạn thực chất chỉ là một kẻ ngốc dễ dàng bị dắt mũi bởi vài câu miêu tả?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Lầm tưởng cốt tử là bạn nghĩ khách hàng xem video bằng "lý trí". Sự thật: Bộ não là một khối thịt mù lòa bị nhốt trong hộp sọ tối om, chỉ đọc thế giới qua xung điện thần kinh. Việc bạn "tự tay làm" hay "nghe kể siêu nét" đều tạo ra chung một mã lệnh. Để tiết kiệm calo, não lười biếng dùng luôn một bản mạch (tế bào gương) để tự động render viễn cảnh ảo thành trải nghiệm thật, bắt khách hàng "dùng thử" ngay trong vô thức mà không thể kháng cự.</p>
<blockquote>
<p><em>Não người nhốt giữa màn đêm,<br/>Lời nghe sắc nét như nêm vào đầu.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q2" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q2: TỬ HUYỆT CỦA CÒ SÚNG TÂM TRÍ<br>Hô hào rát họng bằng những siêu từ vựng như "tối ưu, đột phá, tự động hóa" nhưng mắt khách hàng vẫn trơ ra như đá. Cỗ máy chiếu trong đầu họ đã bị hỏng, hay chính bạn đang dùng sai chiếc chìa khóa sinh tử để bóp cò?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Cỗ máy không hỏng, do bạn nhập sai mã lệnh! Não bộ bị "mù màu" trước các từ vĩ mô trừu tượng, nó báo lỗi 404 vì không có tệp đồ họa cho từ "tối ưu". Công tắc bạo chúa duy nhất ép não chạy phim là ghép: <strong>Động từ vật lý mạnh</strong> (gõ, vuốt, xé rách) với <strong>Danh từ đồ vật cụ thể</strong> (nút Enter, giẻ lau). Đừng bắt não tốn calo suy luận, hãy ném thẳng vật thể vào đầu và ép nó xem phim!</p>
<blockquote>
<p><em>Vĩ mô sáo rỗng mây bay,<br/>Động từ vật lý chạm ngay tim người.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q3" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q3: BẢN CHẤT CỦA B-ROLL (CẢNH TRÁM)<br>Nếu lời nói đã đủ vẽ ra phim ảo, thì việc đổ tiền và công sức quay cảnh cận (B-roll) chèn vào video rốt cuộc là sự lãng phí phù phiếm hay là một "mã ăn gian" tàn bạo tước đoạt mọi ý thức?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đó là "mã ăn gian" tàn bạo nhất! Khách hàng lướt mạng với một bộ não cạn kiệt năng lượng và vô cùng lười biếng. Khi bạn vừa nói "gõ phím", mắt họ thấy ngay ngón tay gõ lạch cạch trên màn hình. Bạn đang đút tận miệng hình ảnh vào võng mạc họ. Âm - Hình khớp lệnh 100%, não lập tức tắt hệ thống phòng ngự và tin sái cổ vì không phải tốn lấy 1 calo nào để tự tưởng tượng.</p>
<blockquote>
<p><em>Tai nghe mắt thấy rõ ràng,<br/>Não lười suy nghĩ khách hàng chốt luôn.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q4" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q4: NGHỊCH LÝ ĐAU ĐỚN CỦA KẺ CHƯA MẤT TIỀN<br>Hoang đường đến mức điên rồ: Tiền vẫn nằm im trong ví, hàng chưa chạm tới tay, mọi thứ đứng ở vạch số 0. Tại sao khi tắt video từ chối mua, khách hàng lại bứt rứt, cay cú và đau đớn như thể vừa bị ăn cướp?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì lý trí tính bằng tiền, còn tiềm thức đo bằng cảm xúc! Khi "dùng thử" ảo giác sung sướng, tiềm thức đã nhận vơ kết quả đó là của mình, dời mốc thực tại từ 0 bay thẳng lên +10. Không mua hàng, hiện thực giật họ từ +10 rơi tóm xuống 0. Não bộ không dịch cú rơi này là "hòa vốn", nó gào lên: "BỊ CƯỚP MẤT 10 ĐIỂM!". Vùng não xử lý nỗi đau thể xác (Insula) phát sáng, họ cuống cuồng chốt đơn chỉ để mua liều thuốc giảm đau.</p>
<blockquote>
<p><em>Chưa mua đã tưởng của mình,<br/>Đến khi mộng vỡ bóng hình vụt tan.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q5" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q5: ĐÒN THỰC CHIẾN (HIỆU ỨNG RÚT QUẠT)<br>Vứt mớ lý thuyết hàn lâm qua một bên! Tóm lại, làm sao để một tay mơ làm nội dung có thể áp dụng đòn tâm lý tàn nhẫn này vào ngay kịch bản ngày mai để vắt kiệt cảm xúc khách hàng?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Hãy thi triển ngay đòn "Rút phích cắm quạt máy lạnh" với 3 nhịp sắc lẹm:</p>
<ol>
<li><strong>Bật quạt (Vẽ mộng):</strong> Mở đầu bằng <em>"Hãy tưởng tượng..."</em>, tả cực nét ảo giác thảnh thơi, sung sướng khi giải quyết xong bế tắc.</li>
<li><strong>Rút phích (Tát tỉnh mộng):</strong> Đảo chiều bằng <em>"Nhưng thực tế là..."</em>. Lột trần sự tăm tối, lộn xộn hiện tại, kích hoạt nỗi uất ức vì bị tước đoạt viễn cảnh đẹp đẽ.</li>
<li><strong>Quăng phao (Chốt sale):</strong> Đưa lời kêu gọi mua hàng làm chiếc phao cứu sinh duy nhất để họ tự bỏ tiền chuộc lại giấc mơ ban nãy!</li>
</ol>
<blockquote>
<p><em>Cho người mộng đẹp đắm say,<br/>Giật phăng thực tại chốt ngay tức thì.</em></p>
</blockquote>
</div>
</div>

<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 5 rãnh Data cốt lõi...)</em></p>
"""

content_pattern = r'(<article class="ink-content ink-mode-dialogue">).*?(</article>)'
content = re.sub(content_pattern, r'\1\n' + new_content + r'\n\2', content, flags=re.DOTALL)

with open('logic13.html', 'w', encoding='utf-8') as f:
    f.write(content)

