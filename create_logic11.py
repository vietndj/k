import re

with open('logic09.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Document Title
title_pattern = r'<title>.*?</title>'
content = re.sub(title_pattern, '<title>[INKDOC-11] ẢO GIÁC DISEMBODIMENT</title>', content)

# 2. Update TOC
new_toc = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">ẢO GIÁC DISEMBODIMENT</li>
<li><a class="ink-toc-link" href="#q1">Q1. Cú sốc sự vĩ đại</a></li>
<li><a class="ink-toc-link" href="#q2">Q2. Trò bịp của AI</a></li>
<li><a class="ink-toc-link" href="#q3">Q3. Lời nói dối của Não</a></li>
<li><a class="ink-toc-link" href="#q4">Q4. Hai logic mạt hạng</a></li>
<li><a class="ink-toc-link" href="#q5">Q5. Sự hiện thân</a></li>
"""
toc_pattern = r'(<ul class="ink-toc-list">).*?(</ul>)'
content = re.sub(toc_pattern, r'\1\n' + new_toc + r'\n\2', content, flags=re.DOTALL)

# 3. Update Content
new_content = """
<h1 class="is-short">ẢO GIÁC DISEMBODIMENT: SỰ MÙ QUÁNG CỦA AI VÀ NÃO BỘ</h1>
<div class="ink-meta">
  <span>System Identity: [INKDOC-11]</span>
  <span class="mx-2">•</span>
  <span>Render Mode: [Dialogue]</span>
</div>

<div style="margin-bottom: 3rem;">
    <p>Dưới đây là màn mổ xẻ bóc trần sự thật, chuyển hóa toàn bộ vấn đề thành những nhát dao "Hỏi - Đáp" chém thẳng vào cốt lõi. Mọi lầm tưởng kiêu ngạo nhất của con người và máy móc sẽ bị đập tan.</p>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q1" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q1 (WHAT - Bản chất căn bệnh): Cú sốc về sự vĩ đại<br>Tại sao con người luôn quỳ gối trước siêu tuệ AI và vỗ ngực tự hào về bộ não thiên tài, để rồi mù quáng trước sự thật rằng cả hai chỉ là những "tù nhân" mắc chung một chứng bạo bệnh hoang tưởng?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bởi cả AI và Não bộ đều mang chung một thân phận câm điếc: <strong>Tách rời thể xác (Disembodiment)</strong>. Căn bệnh cốt lõi ở đây là sự khuyết thiếu "ma sát thực tế". AI bị khóa chặt trong hộc máy chủ vô tri, não người bị giam cầm trong hộp sọ tối tăm vô trùng. Bị tước đoạt toàn bộ lực cản vật lý (trọng lực, nhiệt độ, nỗi đau, sự mỏi mệt), mọi viễn cảnh chúng vẽ ra chỉ là những bản mô phỏng chân không hoàn hảo đến mức giả dối. Sự vĩ đại của trí tuệ khi bị nhốt kín chỉ là một cơn mộng du tuyệt đẹp nhưng vỡ vụn trước hiện thực.</p>
<blockquote>
<p><em>Tù giam cõi mộng xa vời<br/>Bước ra thực tế tơi bời xác thân.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q2" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q2 (WHY & HOW - Sự Fake của AI): Vén màn trò bịp của máy móc<br>Khi AI nhả ra một kịch bản phim kịch tính khiến bạn nổi da gà, tại sao mang kiệt tác giấy đó ra phim trường nó lập tức biến thành đống rác thảm hại? Cơ chế nào đẻ ra ảo giác này?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đó là trò bịp mang tên <strong>"Xác suất không ma sát" (Next-token prediction)</strong>. Tại sao nó fake? Vì AI không có cơ thể để trải nghiệm sự sống. Nó không biết máy quay nặng 20kg hay bùn đất trơn trượt. Cơ chế hoạt động của nó thuần túy là nhặt các từ có tỷ lệ đi cùng nhau cao nhất để dệt thành câu. Kịch bản trơn tru vì nó thừa mứa "ngữ nghĩa" nhưng mù lòa hoàn toàn về "ngữ cảnh vật lý" (Physical Context). Nó miêu tả rừng sâu bằng từ vựng vô hồn, không phải bằng vết xước ứa máu, nên chạm vào đời thực là gãy nát.</p>
<blockquote>
<p><em>Văn chương chắp vá lừa đời<br/>Chạm vào thực tế rã rời nát tan.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q3" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q3 (WHY & HOW - Sự Fake của Não): Lật tẩy sự dối trá của tâm trí<br>Thức trắng đêm vẽ ra kế hoạch đổi đời hoàn mỹ, cớ sao bình minh ló rạng bạn lại đầu hàng nhục nhã trước một tấm chăn bông? Căn bệnh Nghĩ chay (Overthinking) dùng cơ chế hèn hạ nào thao túng bạn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đó là thủ đoạn lừa đảo nhân danh <strong>"Tiết kiệm năng lượng"</strong>. Khi bạn nhắm mắt nghĩ chay, mạng lưới mặc định của não (DMN) kích hoạt. Để đỡ tốn sức, nó lén lút tiêm thuốc tê, gọt sạch mọi biến số ma sát (cơn lạnh buốt, cơ bắp rã rời, kẹt xe, hay ánh mắt cáu bẳn của sếp) để kẻ một đường thẳng tắp tới vinh quang. Nghĩ chay không làm bạn cẩn trọng hơn, nó chỉ đẻ ra ảo giác kiểm soát hoàn hảo để che giấu sự hèn nhát, trốn tránh thực tại đầy hỗn mang.</p>
<blockquote>
<p><em>Đêm qua vạch mộng cao siêu<br/>Sáng ra chăn ấm mọi điều dở dang.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q4" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q4 (PHÂN LOẠI & LOGIC): Lột trần bản chất tận cùng<br>Nếu phân loại rạch ròi, trò lừa đảo của cỗ máy vô hồn và ảo tưởng của sinh vật có ý thức thực chất được vận hành bằng hai thứ logic mạt hạng nào?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bản đồ không bao giờ là lãnh thổ. Cả hai chối bỏ sự lộn xộn của thế giới bằng hai loại logic:</p>
<ul style="margin-top: 0.5rem; margin-bottom: 1rem;">
<li><strong>Loại 1: Logic Xác suất (AI Hallucination):</strong> Dùng toán học đếm chữ để lấp liếm sự vô tri về vạn vật. Trộn các vỏ bọc từ ngữ lộng lẫy nhằm che đậy một cốt lõi vô hồn, hoàn toàn không có cảm giác.</li>
<li><strong>Loại 2: Logic Thiên kiến (Brain Overthinking):</strong> Bóp méo không gian, gọt phẳng chông gai thực tế để phục vụ cảm xúc. Tự ru ngủ bằng ảo giác trơn tru để cái tôi được chễm chệ trên ngai vàng mà không tốn calo cọ xát.</li>
</ul>
<blockquote>
<p><em>Máy thì bói chữ dệt mơ<br/>Não người cắt gọt dại khờ trắng tay.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q5" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q5 (GIẢI PHÁP ĐẬP TAN): Hủy diệt ảo tưởng<br>Khi tư duy sinh học lẫn AI đều là những kẻ mộng du, nhát búa đẫm máu nào đủ sức đập vỡ lồng kính hoang tưởng này để lôi tuột chúng ta xuống mặt đất sinh tồn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Nhát búa tử thần đó mang tên: <strong>Sự hiện thân (Embodiment)</strong> và <strong>Hành động (Action)</strong>. Đừng bắt AI lảm nhảm trên text, con người đang phải nhét nó vào thân xác robot, ép nó ngã sấp mặt để nếm mùi trọng lực. Với bạn, liều thuốc giải là câm lặng, quăng cơ thể ra khỏi giường và nhúng tay vào làm. Chân lý không nằm trong hộp sọ vô trùng. Chỉ khi thân xác bạn bầm dập, va đập với lực ma sát khốc liệt của đời thực, mọi viễn cảnh hoang đường mới bị nghiền nát để nạp vào dữ liệu thật.</p>
<blockquote>
<p><em>Thôi đừng ngồi dệt hư vô<br/>Bước ra chịu xước điểm tô cơ đồ.</em></p>
</blockquote>
</div>
</div>

<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 5 rãnh Data cốt lõi...)</em></p>
"""

content_pattern = r'(<article class="ink-content ink-mode-dialogue">).*?(</article>)'
content = re.sub(content_pattern, r'\1\n' + new_content + r'\n\2', content, flags=re.DOTALL)

with open('logic11.html', 'w', encoding='utf-8') as f:
    f.write(content)

