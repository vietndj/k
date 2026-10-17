import re

with open('logic10.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update TOC
toc_insertion = """<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">BẢN ĐÚC KẾT 8 NHÁT DAO</li>
<li><a class="ink-toc-link" href="#q20">1. Ảo tưởng khoe hàng</a></li>
<li><a class="ink-toc-link" href="#q21">2. Bẫy đua giá rẻ</a></li>
<li><a class="ink-toc-link" href="#q22">3. Phản bội bối cảnh</a></li>
<li><a class="ink-toc-link" href="#q23">4. Cơ chế ủy thác</a></li>
<li><a class="ink-toc-link" href="#q24">5. Chê bai thật thà</a></li>
<li><a class="ink-toc-link" href="#q25">6. Lời nguyền ăn mày</a></li>
<li><a class="ink-toc-link" href="#q26">7. Thông tin rỗng tuếch</a></li>
<li><a class="ink-toc-link" href="#q27">8. Kỹ xảo làm màu</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 2. Update Content
qa_content = """
<div style="margin-bottom: 3rem; margin-top: 4rem;">
    <p>Dưới đây là bản đúc kết toàn bộ xương máu của chuỗi tư duy kinh doanh thực chiến vừa qua. Tôi đã lột sạch mọi lớp vỏ lý thuyết rườm rà, thiết kế lại thành <strong>8 nhát dao (Hỏi Sốc - Đáp Thẳng)</strong>.</p>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q20" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 1. ẢO TƯỞNG "BÁN HÀNG LÀ PHẢI KHOE HÀNG"<br>Tại sao bạn chĩa máy quay vào sản phẩm, sùi bọt mép khoe "cấu hình cao, chất liệu xịn" mà khách hàng lại lướt qua như chạy giặc?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì mọi sản phẩm vật lý bản chất là một "cục nợ" tốn tiền, chật nhà. Bắt khách nghe thông số là ép não họ làm toán. Khách chỉ mở ví mua 3 đích đến vô hình: Rảnh rỗi tấm thân, Đẻ ra tiền, và Oai với đời. Khoe sản phẩm là bắt khách yêu trạm thu phí!</p>
<blockquote>
<p><em>Đừng mang thông số rườm rà,<br/>Bán ngay sung sướng, khách đà chốt luôn.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q21" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 2. CÁI BẪY CHẾT NGƯỜI CỦA "ĐUA GIÁ RẺ"<br>Tại sao cắm đầu livestream gào thét "xả kho 9k, phá giá sập sàn" lại là tấm vé nhanh nhất đưa bạn ra gầm cầu?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì đem giá rẻ của cò con đọ với tổng kho tận xưởng là tự sát. Bán rẻ biến bạn thành cái chợ cho thiên hạ cò kè. Hãy khoét đúng "Nỗi đau" để hóa thành Bác sĩ. Khách đã đau, bác sĩ bảo nộp bao nhiêu họ câm nín nộp bấy nhiêu, cấm cãi!</p>
<blockquote>
<p><em>Đua nhau đạp giá bán buôn,<br/>Chữa đau trúng chỗ, tiền tuôn ào ào.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q22" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 3. SỰ PHẢN BỘI TÀN NHẪN CỦA BỐI CẢNH<br>Mồm nói đạo lý kiếm tiền tỷ, mặc vest vuốt tóc bóng lộn, tại sao đối tác VIP liếc qua video lại âm thầm block bạn ngay lập tức?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì áo vest và kịch bản là vỏ bọc bạn CỐ TÌNH ngụy tạo được trong 5 phút. Nhưng mớ cáp sạc rối nùi sau lưng lột tả BẢN CHẤT cẩu thả 24/7 của bạn. Đồ vật vô tri không biết nói dối. Sân sau bừa bộn thì không ai dám giao tiền cho bạn quản lý.</p>
<blockquote>
<p><em>Áo quần bóng bẩy làm màu,<br/>Phía sau bừa bộn, khách nhàu niềm tin.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q23" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 4. CƠ CHẾ ỦY THÁC & GIÁ TRỊ CỦA "CÁI MẶT"<br>Tại sao đứng trước bảng cấu hình siêu thị thì vò đầu bỏ về, nhưng thằng bạn vứt cho cái link thì nhắm mắt quẹt thẻ trong 3 giây?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì đứng trước ma trận hàng hóa, não người bị kiệt sức. Họ muốn tìm người "thạo việc" để copy quyết định cho xong. Đưa mặt thật lên mạng là tự biến mình thành "bia đỡ đạn". Khách thấy kẻ có danh dự để túm lỡ có bề gì, họ sẽ tự động tắt não và nhả tiền.</p>
<blockquote>
<p><em>Hàng nhiều lựa chọn thêm đau,<br/>Tin người thạo việc, chốt mau nhẹ đầu.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q24" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 5. NGHỊCH LÝ CỦA SỰ CHÊ BAI (THẬT THÀ ĐẮT GIÁ)<br>Tại sao thề non hẹn biển khen hàng "tuyệt đỉnh" thì khách lờ đi, nhưng dám mắng khách "áo này dễ nhăn, lười ủi đừng mua" lại nổ đơn ầm ầm?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì quảng cáo giờ sặc mùi lừa đảo, cứ khen hoàn hảo là não khách tự động dựng rào phòng thủ. Khi bạn dũng cảm bóc trần một khuyết điểm thật thà nhất, sự bất ngờ đó đập tan cảnh giác, khiến khách tự động tin sái cổ vào những ưu điểm bạn nói sau đó.</p>
<blockquote>
<p><em>Khen ngon khách lại lặng thinh,<br/>Chê bai khuyết điểm, khách rinh ầm ầm.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q25" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 6. LỜI NGUYỀN "ĂN MÀY" TƯƠNG TÁC (CTA)<br>Tại sao cuối video cứ cúi đầu nài nỉ "Mọi người thấy hay xin hãy follow mình nhé" lại biến bạn thành kẻ ăn mày rẻ tiền nhất mạng xã hội?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì khán giả lướt mạng vô thức, họ không ban phát lòng thương hại nếu không được lợi gì. CTA phải là một mệnh lệnh đổi chác sòng phẳng chọc thẳng vào sự lười biếng: <em>"Lưu ngay video này lại để mai copy cho lẹ!"</em>. Có lợi ích thì ngón tay mới nhúc nhích.</p>
<blockquote>
<p><em>Đừng buông lời sáo van nài,<br/>Trao mồi lợi ích, ngày dài khách theo.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q26" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 7. THÔNG TIN RỖNG TUẾCH XÚC PHẠM NGƯỜI XEM<br>Tại sao bạn cầm món đồ lên khen nó hình tròn, nắp đỏ mà lại bị chửi là xúc phạm trí tuệ người xem?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì khách không mù, họ tự thấy màu sắc hình dáng rồi. Khách không bao giờ đổi tiền lấy vật chất vô tri. Lời nói của bạn phải bù đắp được thứ camera không quay được: Món đồ này giúp họ rảnh thêm bao lâu, đẻ ra bao nhiêu tiền và tăng vị thế thế nào!</p>
<blockquote>
<p><em>Khoe chi bề mặt phô trương,<br/>Dịch ra lợi ích, khách thương chốt liền.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q27" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 8. KỸ XẢO LÀM MÀU VS. GIẢI PHÁP THỰC TẾ<br>Tại sao bạn học đủ khóa quay dựng, chèn hiệu ứng lóa mắt, mà video vẫn không ra nổi một đơn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì bạn đang bán "Kỹ năng múa may" chứ không bán "Giải pháp". Khách không trả tiền cho kỹ xảo của bạn, họ trả tiền cho thông tin giúp họ giải quyết được bế tắc. Một video ngồi nói chay nhưng chọc đúng chỗ ngứa vẫn ăn đứt video kỹ xảo Hollywood mà nội dung rỗng tuếch.</p>
<blockquote>
<p><em>Quay phim hiệu ứng tốn tiền,<br/>Gãi ngay chỗ ngứa, khách liền vung tay.</em></p>
</blockquote>
</div>
</div>
"""

content = content.replace('<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 19 rãnh', qa_content + '\n<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 19 rãnh')
content = content.replace('19 rãnh Data cốt lõi', '27 rãnh Data cốt lõi')

with open('logic10.html', 'w', encoding='utf-8') as f:
    f.write(content)

