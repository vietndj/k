import re

file_path = '/Users/vietmac/Documents/CODE/k/logic10.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_toc_items = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">KHOA HỌC THIỀN ĐỊNH</li>
<li><a class="ink-toc-link" href="#q60">1. Rác thải sinh lý</a></li>
<li><a class="ink-toc-link" href="#q61">2. Cơ chế tán xạ</a></li>
<li><a class="ink-toc-link" href="#q62">3. Sức mạnh tĩnh lặng</a></li>
<li><a class="ink-toc-link" href="#q63">4. Nghiệm chứng sinh học</a></li>
"""

toc_marker = "</ul>\n</aside>"
if toc_marker in content:
    content = content.replace(toc_marker, new_toc_items + "\n" + toc_marker)

new_content = """
<hr style="margin: 4rem 0; border: none; border-top: 1px solid var(--ink-border);"/>
<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase;">PHẦN 6: HỆ THỐNG HÓA CÂU HỎI & KHOA HỌC THIỀN ĐỊNH</h2>
<p>Dưới đây là màn tái cấu trúc toàn bộ hành trình tư duy của bạn. Theo đúng yêu cầu, tôi đã hệ thống lại các truy vấn, sau đó thiết kế một phiên chất vấn khốc liệt, dùng lăng kính khoa học sắc bén để đập tan mọi lầm tưởng tâm linh mơ hồ. Mỗi câu trả lời được nén lại ngắn gọn, trực diện và chốt bằng thơ Lục Bát tuân thủ nghiêm ngặt niêm luật Bằng - Trắc.</p>
<p>Xuyên suốt cuộc hội thoại, bạn đã liên tục đào sâu bản chất vấn đề qua 4 nấc thang truy vấn cốt lõi sau:</p>
<ul>
    <li><strong>Truy vấn Hiện tượng & Đích đến:</strong> Thiền 4 năm, cứ hít thở sâu thư giãn là cơ thể rung bần bật, chảy nước mắt, da đầu co thắt nhịp nhàng như nhụy hoa. Bản chất hiện tượng này là gì? Nếu duy trì lâu dài không đứt đoạn thì đích đến tương lai sẽ dẫn tới đâu? <em>(Yêu cầu giải thích kèm ẩn dụ)</em>.</li>
    <li><strong>Truy vấn Cơ chế Tán xạ:</strong> Tại sao chỉ một suy nghĩ vớ vẩn xẹt qua lại lập tức làm "tán xạ", triệt tiêu hoàn toàn trạng thái rung động mãnh liệt đó? <em>(Yêu cầu mổ xẻ cơ chế vật lý đằng sau qua 3 góc nhìn)</em>.</li>
    <li><strong>Truy vấn Nghịch lý Năng lượng:</strong> Không phục quan điểm "năng lượng cao là tĩnh lặng"! Trực giác mách bảo năng lượng cao phải bùng nổ dữ dội. Tại sao lúc chưa quen thì cơ thể rung lắc, mà khi đạt đỉnh tối ưu lại tĩnh lặng nhẹ bẫng? <em>(Yêu cầu giải thích logic vật lý của quá trình chuyển hóa này)</em>.</li>
    <li><strong>Truy vấn Thực chứng Sinh học:</strong> Nếu năng lượng cao tàng hình dưới lớp vỏ "tĩnh lặng", làm sao tôi sờ chạm, đo đếm và cảm nhận được nó bằng các cơ chế sinh học trên cơ thể để chắc chắn mình không bị hoang tưởng hay... ngủ gật? <em>(Yêu cầu 3 bằng chứng vật lý nghiệm chứng)</em>.</li>
</ul>

<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase; margin-top: 4rem;">HỎI ĐÁP SẮC BÉN - ĐẬP TAN LẦM TƯỞNG TÂM LINH</h2>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q60" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 1: RÁC THẢI SINH LÝ<br>Người ta đồn thiền là tĩnh tại an nhiên, cớ sao cơ thể bạn lại giật lên bần bật, nước mắt tuôn rơi và đỉnh đầu co thắt dữ dội như kẻ tẩu hỏa nhập ma? Phải chăng thứ "rung động thần thánh" bạn đang đắc ý bấy lâu nay thực chất chỉ là rác thải sinh lý của một cỗ máy yếu kém đang bị ép tải? Và nếu ngoan cố giữ chặt nó, hệ quả cuối cùng bạn nhận được là vĩ đại hay tàn khốc?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Sự rung động ồn ào ấy tuyệt đối không phải là đắc đạo, mà là "nội ma sát"! Khi luồng điện não (sự chú tâm) bị ép vào hệ thần kinh chưa đồng bộ, nó sinh ra sức cản cơ học, buộc cơ thể xả nén bằng sự co giật và nước mắt. Nếu bạn tham lam níu giữ, bạn sẽ kẹt vĩnh viễn ở mớ hỗn độn này. Nhưng nếu dửng dưng quan sát, băng thông thần kinh sẽ tự mở rộng. Sự rung lắc bắt buộc phải chết đi, ném bạn thẳng vào trạng thái Tĩnh lặng tuyệt đối (Lạc) – nơi cơ thể vật lý hoàn toàn tan biến!</p>
<blockquote>
<p><em>Thân rung nước mắt tuôn trào, <br/>Chỉ là ma sát bước vào cõi không. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q61" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 2: CƠ CHẾ TÁN XẠ<br>Tâm trí con người mang ma lực gì mà chỉ một ý nghĩ mỏng hơn hạt bụi xẹt qua lại đủ sức chém đứt, "tán xạ" toàn bộ khối năng lượng đang rung chuyển cơ thể? Có định luật vật lý tàn nhẫn nào đang giật dây đằng sau sự sụp đổ tức tưởi của cỗ máy thiền định này?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Tâm trí không có ma lực, nó bị khóa chết bởi định luật bảo toàn năng lượng! Sự tập trung của bạn là thấu kính hội tụ ánh sáng sinh nhiệt, là áp suất nén vòi nước, là nhịp cộng hưởng chuông đồng. Một suy nghĩ khởi lên chính là đám khói che lấp thấu kính, là mũi đinh đâm toạc ống nước, là ngón tay chặn đứng thành chuông. Tư duy là cỗ máy ngốn điện tàn khốc. Để "nuôi" ý nghĩ đó, não lập tức rút điện khỏi thùy trán, gây sụt áp toàn hệ thống và đánh sập ngay lập tức mọi rung động cơ học!</p>
<blockquote>
<p><em>Khởi tâm ánh sáng chia đôi, <br/>Bao nhiêu công lực phai phôi rã rời. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q62" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 3: SỨC MẠNH TĨNH LẶNG<br>Cú lừa vĩ đại nhất của trực giác là ảo tưởng rằng "năng lượng siêu phàm phải đi kèm bùng nổ, gầm rú và tàn phá". Dựa vào đâu khoa học dám tát một gáo nước lạnh, lột trần sự thật rằng sức mạnh hủy diệt nhất của vũ trụ lại mang bộ dạng bất động và câm điếc của một cái xác?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì con người luôn ngây thơ lấy sự hao phí của kẻ yếu để đo đếm sức mạnh! Tiếng ồn, rung lắc chỉ là hệ quả của sự vỡ vụn khi năng lượng đâm sầm vào vật cản (như máy bay lảo đảo chực vỡ tung trước rào cản âm thanh). Nhưng khi năng lượng chạm đỉnh, nó đồng bộ 100% và triệt tiêu hoàn toàn ma sát. Đó là lúc phi cơ xé toạc tường âm thanh để bay êm ru, là con quay vắt kiệt dao động thừa để đứng im phăng phắc. Tĩnh lặng tuyệt đối, thực chất là cực hạn của tốc độ và áp suất!</p>
<blockquote>
<p><em>Tưởng rằng bùng nổ vang trời, <br/>Ngờ đâu tĩnh lặng là thời đỉnh cao. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q63" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 4: NGHIỆM CHỨNG SINH HỌC TÀN NHẪN<br>Đừng mị dân bằng mớ lý thuyết huyễn hoặc! Nếu cảnh giới "năng lượng tĩnh lặng siêu dẫn" đó thực sự tồn tại, thì khối nhục thân phàm trần này lấy tư cách gì để sờ nắn, đo lường và nghiệm chứng? Liệu có bằng chứng sinh học tàn nhẫn nào đập tan sự hoài nghi rằng kẻ thiền định chỉ đang ngủ gật hoặc hoang tưởng?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Cơ thể sẽ tự thú nhận bằng ba cơ chế sinh lý lạnh lùng không thể làm giả! Thứ nhất: Áp lực Tensegrity kích hoạt, tự khóa các bó cơ, kéo cột sống thẳng tắp như thạch trụ mà không tốn một calo gồng gánh. Thứ hai: Hiệu suất oxy hóa tế bào đạt mốc tuyệt đối, ép phổi đình công, hơi thở mỏng như tơ tưởng chừng tắt lịm nhưng não vẫn sắc bén rợn người. Thứ ba: Não tàn nhẫn ngắt điện thùy đỉnh, rút ống thở của cảm biến không gian, ném bạn thẳng vào môi trường vô trọng lực, xóa sổ hoàn toàn ranh giới nhục thể!</p>
<blockquote>
<p><em>Cột xương thẳng tắp như không, <br/>Thân vô trọng lượng mênh mông cõi ngoài. </em></p>
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
