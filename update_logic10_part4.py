import re

file_path = '/Users/vietmac/Documents/CODE/k/logic10.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_toc = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">TIẾN HÓA MẠNG XÃ HỘI</li>
<li><a class="ink-toc-link" href="#q40">1. Bức tử kết nối</a></li>
<li><a class="ink-toc-link" href="#q41">2. Thầy bói mù</a></li>
<li><a class="ink-toc-link" href="#q42">3. Sa thải đám đông</a></li>
<li><a class="ink-toc-link" href="#q43">4. Không gian toán học</a></li>
<li><a class="ink-toc-link" href="#q44">5. Án tử kẻ cuồng view</a></li>
"""

toc_marker = "</ul>\n</aside>"
if toc_marker in content:
    content = content.replace(toc_marker, new_toc + "\n" + toc_marker)

new_content = """
<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase; margin-top: 4rem;">PHẦN 3: SỰ TIẾN HÓA CỦA MẠNG XÃ HỘI (SEMANTIC MEDIA)</h2>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q40" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 1: BỨC TỬ ẢO MỘNG "KẾT NỐI BẠN BÈ"<br>Nếu mạng xã hội sinh ra để "kết nối bạn bè", vậy tại sao ngay lúc này, 80% thứ đập vào mắt bạn lại là video của những kẻ xa lạ ở tận đẩu tận đâu? Phải chăng chữ "Xã hội" đã chết và chúng ta đang bị lừa?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Chữ "Xã hội" đã chết ngắc! Giai đoạn 1 (Social Media) từng là một gã bưu tá trung thành giao thư theo danh bạ. Nhưng sự thật phũ phàng: bạn bè của bạn đăng bài quá chán. Nếu cứ giữ cái "tình bạn" đó, bạn sẽ xóa app. Để sống còn, nền tảng buộc phải bức tử mối quan hệ thực tế, tàn nhẫn nhồi nhét nội dung giật gân của người lạ vào mặt bạn để cướp đoạt sự chú ý.</p>
<blockquote>
<p><em>Mạng xưa tìm kiếm bạn thân,<br/>Nay nhồi người lạ, muôn phần đắm say.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q41" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 2: LỘT MẶT NẠ "ÔNG THẦY BÓI MÙ" VÀ ĐÁM ĐÔNG RẺ TIỀN<br>Triệu view, triệu like có phải là thước đo của "chân lý" nội dung hay? Hay bao năm qua, máy móc chỉ là một cỗ máy đần độn, bị thao túng và cổ xúy cho những rác rưởi, drama, khoe thân?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Nó thực sự là một tên đần độn mù lòa! Ở Giai đoạn 2 (Interest Media), thuật toán là "ông thầy bói mù". Nó tung video vào bóng tối và đo độ ồn ào (Lượt Click, Thời gian xem). Mà đám đông thì luôn bị dẫn dắt bởi bản năng tò mò và tăm tối. Thầy bói mù nghe đám đông ồn ào liền lầm tưởng rác là ngọc, vặn van phân phối vạn người. Triệu view ngày đó là đỉnh cao của thao túng tâm lý, không phải chất lượng.</p>
<blockquote>
<p><em>Thầy mù nghe tiếng vỗ tay,<br/>Đẩy bao rác rưởi tung bay ngập trời.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q42" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 3: PHÉP MÀU KHI ĐÁM ĐÔNG BỊ SA THẢI<br>Ai đã tẩy não bạn rằng tải video lên phải cần "đám đông vỗ tay mồi" thì mới có đề xuất? Giải thích sao về một kênh mới toanh, 0 follower, 0 view vẫn cắn xu hướng và chốt đơn ầm ầm giữa đêm? Lấy đâu ra tiếng hò reo để mồi cỗ máy mù lòa kia?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì quyền lực đám đông đã bị sa thải! Ở Giai đoạn 3 (Semantic Media), AI đã mở mắt và thính tai nhờ công nghệ đa phương thức. Video vừa tải lên 0 view, AI lập tức quét hình, bóc băng giọng nói để nội soi ý nghĩa chuyên môn. Nó tự làm giám khảo phán quyết, chà đạp lên rào cản Follower để gắp thẳng nội dung ném vào mặt những kẻ đang khao khát. AI không thèm ngửa tay xin đám đông ban phát tương tác nữa.</p>
<blockquote>
<p><em>Cần chi lượt thích ban đầu,<br/>Máy nay đã hiểu từng câu tỏ tường.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q43" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 4: BẢN CHẤT LẠNH LẼO CỦA KHÔNG GIAN TOÁN HỌC<br>Dừng ngay những từ ẩn dụ sến súa! Một đống mã code vô tri thì "thấu hiểu" ý nghĩa thâm sâu của con người bằng thứ ma thuật nào? Sự thật tàn nhẫn sau cỗ máy thấu cảm này là gì?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Không có cảm xúc hay ma thuật nào cả, chỉ có toán học không gian đa chiều! AI băm nát video của bạn thành một chuỗi tọa độ "Vector nội dung". Thói quen, khao khát của người xem bị đúc thành "Vector nhu cầu". Logic thuật toán chỉ là phép đo khoảng cách hình học giữa 2 tọa độ đó. Gần nhau là khớp lệnh. Cỗ máy ngữ nghĩa vô hồn, máu lạnh nhưng kết nối người mua - người bán với độ chính xác tuyệt đối.</p>
<blockquote>
<p><em>Véc-tơ đo khoảng cách xa,<br/>Khớp xong tọa độ sinh ra bạc tiền.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q44" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 5: BẢN ÁN TỬ CHO KẺ CUỒNG VIEW<br>Nếu nền tảng đã tiến hóa thành "sàn khớp lệnh", vậy tại sao bạn vẫn cắn răng nhảy múa, làm trò lố để câu triệu view rác rồi khóc ròng vì chốt đơn bằng không? Khát khao triệu view có phải là tự đào mồ chôn mình?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Chính xác là tự sát! Thuật toán Ngữ nghĩa sẵn sàng tàn sát video múa may câu view rác — vì tệp đó làm loạn não AI, không chịu chi tiền, khiến nền tảng mất giá trị. Đổi lại, nó lấy video chuyên môn siêu khô khan của bạn, gắp ném chuẩn xác vào tay 500 khách VIP đang cầm tiền tìm giải pháp. Nền tảng vứt bỏ đám đông hão huyền, đổi lấy tỷ lệ chốt sale cực đoan. Kẻ nào tôn thờ view ảo, kẻ đó diệt vong!</p>
<blockquote>
<p><em>Triệu view rác rưởi vứt đi,<br/>Vài trăm khách chuẩn, thực thi chốt lời.</em></p>
</blockquote>
</div>
</div>
"""

content_marker = "<p style=\"margin-top: 3rem; color: var(--ink-text-light);\"><em>(Hệ thống đã mã hóa 33 rãnh Data cốt lõi...)</em></p>"
if content_marker in content:
    content = content.replace(content_marker, new_content + "\n" + content_marker)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
