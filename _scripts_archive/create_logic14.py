import re

with open('logic13.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Document Title
title_pattern = r'<title>.*?</title>'
content = re.sub(title_pattern, '<title>[INKDOC-14] BẢN CHẤT SINH HỌC CỦA HOOK</title>', content)

# 2. Update TOC
new_toc = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">SINH HỌC CỦA HOOK</li>
<li><a class="ink-toc-link" href="#q4">4. Tầng 2.5: Ma sát tâm lý</a></li>
<li><a class="ink-toc-link" href="#q5">5. L1 Cache Miss</a></li>
<li><a class="ink-toc-link" href="#q6">6. Mitophagy trong Content</a></li>
"""
toc_pattern = r'(<ul class="ink-toc-list">).*?(</ul>)'
content = re.sub(toc_pattern, r'\1\n' + new_toc + r'\n\2', content, flags=re.DOTALL)

# 3. Update Content
new_content = """
<h1 class="is-short">BẢN CHẤT SINH HỌC CỦA HOOK: MA SÁT VÀ NĂNG LƯỢNG</h1>
<div class="ink-meta">
  <span>System Identity: [INKDOC-14]</span>
  <span class="mx-2">•</span>
  <span>Render Mode: [Dialogue]</span>
</div>

<div style="margin-bottom: 3rem;">
    <p>Tiếp tục đào sâu vào tầng vi sinh học của quá trình sáng tạo nội dung. Dưới đây là những cơ chế tàn khốc quyết định sinh tử của một "Hook" trong 3 giây đầu tiên.</p>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q4" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 4️⃣ Tầng 2.5: Nói điều đúng đắn hay Khoét vào ma sát tâm lý thầm kín?<br>Tại sao cung cấp kiến thức "chuẩn logic" (Tầng 1) lại thường thất bại ê chề, trong khi chỉ cần gọi tên một sự cọ xát nhỏ bé (Tầng 2.5) lại khiến user dính chặt không rời?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Sự thật phũ phàng là: Logic chỉ chạm đến vỏ não – bộ phận tiêu thụ năng lượng chậm rãi và cực kỳ dễ chán. Một hook sát thủ không dạy đời, nó khoan thẳng vào "Tầng 2.5": tầng của những nỗi đau vi tế, sự ngần ngại, và ma sát tâm lý thầm kín mà user thậm chí không dám nói ra. Khi bạn bóc trần sự cọ xát này, não bộ user nhận được "tín hiệu chi phí" (cost-signaling): Bạn đã đổ máu để hiểu tận cùng tâm can họ. Tướng quân Cuống Não lập tức mở cổng thành mà không cần phòng vệ.</p>
<blockquote>
<p><em>Nói đúng, não thấy bình thường,<br/>Chạm ngay ma sát, mở đường hóc môn.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q5" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 5️⃣ L1 Cache Miss: Vuột mất lượt xem hay Vĩnh viễn bị xóa khỏi RAM?<br>Anh em nghĩ để tuột user ở 3 giây đầu chỉ là xui xẻo mất đi một view, hay thực chất anh em đã vĩnh viễn bị đá văng khỏi bộ nhớ RAM của họ?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Lướt qua một hook yếu không phải là sự từ chối nhẹ nhàng. Khi hook không đủ độ sắc, não user lập tức thực hiện lệnh "L1 Cache Miss" – xóa sổ hoàn toàn dữ liệu của bạn khỏi bộ nhớ tạm để nhường RAM cho video khác. Sự đứt gãy này tàn nhẫn đến mức não phải mất 23 phút hồi phục mới có thể nạp lại bối cảnh ban đầu. Hook không "đóng băng" được RAM ngay nhịp đầu, thì nội dung vàng ròng phía sau cũng chỉ là rác rưởi trôi tuột vào hư vô.</p>
<blockquote>
<p><em>Ba giây không giữ được hồn,<br/>RAM não xóa sạch, vùi chôn công trình.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q6" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 6️⃣ Mitophagy trong Content: Nhồi nhét nguy hiểm hay Tàn nhẫn cắt gọt?<br>Cố nhồi nhét hàng tá thông tin giật gân vào Hook để chứng tỏ sự nguy hiểm, hay cắt gọt tàn nhẫn như cơ chế "thực bào ti thể" (Mitophagy) mới là đỉnh cao của sự dính chặt?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Nhồi nhét tạo ra "rác thải nhận thức" (cognitive overload). Khi bị ngợp dữ liệu, não cúp cầu dao điện tức thì để bảo vệ phần cứng. Đỉnh cao của Hook là sự thanh lọc. Giống như Mitophagy tự động nuốt chửng các ti thể già cỗi để dọn sạch đường ống electron, một hook hiệu quả phải bị gọt giũa tàn nhẫn mọi từ ngữ thừa thãi. Chỉ giữ lại đúng MỘT tinh thể tò mò duy nhất. Hook càng "nhẹ", tia chớp đánh vào hệ thần kinh càng sắc, càng sâu.</p>
<blockquote>
<p><em>Gọt bớt cho nhẹ khung hình,<br/>Rác thừa dọn sạch, thình lình não thông.</em></p>
</blockquote>
<p style="margin-top: 2rem;"><em>(Thấy chạm đúng chỗ ngứa thì ới mình nếu cần hỗ trợ thêm nhé, cứ xách máy lên mà farm số giờ bay thôi! 🎬)</em></p>
</div>
</div>

<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 3 rãnh Data cốt lõi...)</em></p>
"""

content_pattern = r'(<article class="ink-content ink-mode-dialogue">).*?(</article>)'
content = re.sub(content_pattern, r'\1\n' + new_content + r'\n\2', content, flags=re.DOTALL)

with open('logic14.html', 'w', encoding='utf-8') as f:
    f.write(content)

