import sys

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'r', encoding='utf-8') as f:
    content = f.read()

toc_insert = """<li><a class="ink-toc-link" href="#p16_q85">Q85. Sợi dây thun căng</a></li>
<li><a class="ink-toc-link" href="#p16_q86">Q86. Smartphone Restart</a></li>
<li><a class="ink-toc-link" href="#p16_q87">Q87. Buông tay xách đồ</a></li>
<li><a class="ink-toc-link" href="#p16_q88">Q88. Về số Mo động cơ</a></li>
<li><a class="ink-toc-link" href="#p16_q89">Q89. Nước mắt sinh hóa</a></li>"""

body_insert = """
<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p16_q85" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 85 [Sợi dây thun bị kéo căng lâu ngày]: Dây thun căng miết thả ra nảy giật, cớ sao cơ bắp ép nhả lại êm ru?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Cơ bắp bị kéo giãn nhiều tháng, khi buông đột ngột tất yếu nảy giật để tìm về số không.</p>
<blockquote>
<p><em>Dây thun gồng gánh bao <strong>ngày</strong>,</em><br/>
<em>Buông tay nảy giật mỏi <strong>thay</strong> xác phàm.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p16_q86" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 86 [Chiếc điện thoại thông minh - Chế độ Sleep vs Restart]: Tắt màn hình tưởng máy nghỉ, sao rác chạy ngầm vẫn vắt kiệt RAM thần kinh?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Nằm ngủ chỉ là tắt màn hình mị dân. Thiền là "Restart", ép hệ thống giật khựng lại để dọn sạch rác.</p>
<blockquote>
<p><em>Màn hình dẫu tắt im <strong>lìm</strong>,</em><br/>
<em>Rác ngầm vẫn cứ đắm <strong>chìm</strong> bên trong.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p16_q87" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 87 [Xách hai túi đồ nặng rã rời - Đổi tay vs Buông thõng]: Đổi tay xách đồ để lừa mình, sao buông phịch xuống đất tay lại giật tung?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Đổi tay cơ bắp vẫn phải gồng. Buông thõng ép cơ sâu nhả nén cực độ, sinh ra run rẩy vật lý.</p>
<blockquote>
<p><em>Gồng tay xách nặng đã <strong>lâu</strong>,</em><br/>
<em>Buông rơi dứt khoát bỗng <strong>đâu</strong> giật rùng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p16_q88" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 88 [Động cơ xe - Rà phanh rỉ rả vs Về số Mo]: Rà phanh miết máy vẫn gầm, chừng nào mới dám cắt số về không xả khói?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Nghỉ ngơi nông chỉ là rà phanh kìm hãm. Thiền là về số 0, để cỗ máy rùng mình văng sạch cặn bã.</p>
<blockquote>
<p><em>Rà phanh xe chạy âm <strong>thầm</strong>,</em><br/>
<em>Về mo máy giật cái <strong>rầm</strong> cặn văng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p16_q89" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 89 [Cơ chế nước mắt thanh tẩy sinh hóa - Catharsis]: Khóc thiền đâu phải sầu bi ướt át, hóa ra chỉ là vòi xả rác sinh hóa?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Chính xác. Nước mắt thiền vắng bóng nỗi buồn, nó thuần túy là ống cống bài tiết hóa chất stress của não bộ.</p>
<blockquote>
<p><em>Lệ rơi đâu bởi xót <strong>thương</strong>,</em><br/>
<em>Mà đem độc tố nhiễu <strong>nhương</strong> tống ngoài.</em></p>
</blockquote>
</div>
</div>
"""

q84_marker = '<li><a class="ink-toc-link" href="#p16_q84">Q84. Đứa trẻ sà vào lòng mẹ</a></li>'
content = content.replace(q84_marker, q84_marker + '\n' + toc_insert)

split_token = '<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>'
parts = content.split(split_token)
if len(parts) >= 2:
    new_content = parts[0] + body_insert + '\n' + split_token + parts[1]
    with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: logic24.html updated with Q85-Q89.")
else:
    print("FAILED: split_token not found.")
