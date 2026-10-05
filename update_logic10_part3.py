import re

file_path = '/Users/vietmac/Documents/CODE/k/logic10.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_toc = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">THUẬT TOÁN & BẢN NGÃ</li>
<li><a class="ink-toc-link" href="#q34">1. Bạo chúa phân phối</a></li>
<li><a class="ink-toc-link" href="#q35">2. Dữ liệu vi mô</a></li>
<li><a class="ink-toc-link" href="#q36">3. Sòng bạc Dopamine</a></li>
<li><a class="ink-toc-link" href="#q37">4. Buồng vang phẫn nộ</a></li>
<li><a class="ink-toc-link" href="#q38">5. Nhu cầu giả tạo</a></li>
<li><a class="ink-toc-link" href="#q39">6. Ảo giác tự do</a></li>
"""

toc_marker = "</ul>\n</aside>"
if toc_marker in content:
    content = content.replace(toc_marker, new_toc + "\n" + toc_marker)


new_content = """
<hr style="margin: 4rem 0; border: none; border-top: 1px solid var(--ink-border);"/>
<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase;">PHẦN 1: HỆ THỐNG HÓA TIẾN TRÌNH CÂU HỎI CỦA BẠN</h2>
<p>Trước khi bóc trần những lầm tưởng sâu sắc nhất, hãy nhìn lại chuỗi tư duy phản biện vô cùng sắc sảo của bạn qua các lượt hỏi. Bạn đã liên tục gạt bỏ những câu trả lời bề mặt để ép tôi đi đến tận cùng của bản chất:</p>
<ul>
    <li><strong>Khởi điểm trực giác (What - Why - How):</strong> Bạn đặt nghi vấn về nhận định: <em>"Thuật toán đề xuất thao túng thế giới mạnh hơn ChatGPT"</em>. Trực giác của bạn rất nhạy bén khi hỏi có phải việc mạng xã hội "hiểu rõ tôi" chính là mấu chốt tạo ra sự thay đổi ở cấp độ vĩ mô (từ bầu cử đến kinh tế).</li>
    <li><strong>Đòi hỏi logic và dữ liệu:</strong> Khi nghe giải thích về "Buồng vang thông tin" và "Nhu cầu giả tạo", bạn lập tức phản biện là chưa thuyết phục. Bạn đòi hỏi phải giải thích lại bằng logic ngầm, bằng dữ liệu phân tích hệ thống (như hồ sơ tâm lý, vi dữ liệu) và bằng 2 lăng kính khách quan, sắc bén hơn.</li>
    <li><strong>Yêu cầu thực chứng:</strong> Khái niệm "Sự chia rẽ xã hội" thực chất hoạt động thế nào? Bạn đã yêu cầu một ví dụ thực tế, sống động dựa trên các báo cáo rò rỉ của MIT và Facebook để hiểu rõ cơ chế kích động đám đông.</li>
    <li><strong>Bác bỏ sự ví von hời hợt:</strong> Khi tôi dùng hình ảnh "ChatGPT là Từ điển, Thuật toán là Đầu bếp", bạn thẳng thừng gạt bỏ. Bạn ép tôi phải có một góc nhìn vĩ mô và gai góc hơn (Sản xuất vs Phân phối, Lực ma sát nhận thức) để chứng minh quyền lực tuyệt đối của Thuật toán.</li>
    <li><strong>Nghệ thuật hóa triết lý:</strong> Bạn yêu cầu mã hóa toàn bộ lượng kiến thức công nghệ khô khan thành một bài thơ Lục Bát siêu chi tiết, có bình giảng, tuân thủ định dạng mã code khắt khe.</li>
    <li><strong>Yêu cầu hiện tại:</strong> Tái cấu trúc toàn bộ cuộc phân tích thành một hệ thống Hỏi - Đáp (Q&A) gây shock, bóc trần ảo tưởng, và kết thúc mỗi câu trả lời bằng 2 câu thơ Lục Bát được gieo vần chuẩn xác.</li>
</ul>

<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase; margin-top: 4rem;">PHẦN 2: HỎI ĐÁP SẮC BÉN - ĐẬP TAN LẦM TƯỞNG</h2>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q34" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 1: Bạn đang run sợ trước sự thông minh của AI (như ChatGPT) và coi nó là mối đe dọa thống trị tương lai. Nhưng làm sao một "kẻ sai vặt" ngoan ngoãn, chỉ lên tiếng khi bạn ra lệnh lại có thể đe dọa nhân loại? Đâu mới là "tên bạo chúa" thực sự đang cai trị tâm trí bạn ngay cả khi bạn không hề yêu cầu?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Sự ngây thơ lớn nhất của con người là hoảng sợ trước khâu "Sản xuất" (ChatGPT) mà quỳ gối quy phục trước khâu "Phân phối" (Thuật toán). ChatGPT là cơ chế thụ động; bạn không gõ phím, nó vô tri. Nhưng Thuật toán đề xuất là một con quái vật chủ động. Nó không chờ bạn hỏi, nó tự dội bom thông tin thẳng vào võng mạc, đi vòng qua mọi màng lọc lý trí. Kẻ tạo ra nội dung vĩnh viễn không có quyền lực bằng kẻ quyết định hàng tỷ người "được phép" nhìn thấy điều gì mỗi ngày. Kẻ kiểm soát kênh phân phối mới là kẻ cai trị thế giới.</p>
<blockquote>
<p><em>Chát AI vốn dĩ lặng im,<br/>Kẻ ngầm giăng lưới đắm chìm nhân sinh.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q35" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 2: Bạn tin rằng quyền riêng tư của mình được bảo mật tuyệt đối vì bạn chẳng bao giờ bấm "Like", "Share" hay bình luận bậy bạ trên mạng? Bạn định giấu đi sự yếu đuối của mình thế nào khi cỗ máy kia có thể đong đếm được nỗi buồn của bạn chỉ qua vận tốc cuộn ngón tay?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Thuật toán coi khinh những cái "Like" đầy ý thức của bạn. Thứ nó khai thác là "Dữ liệu vi mô" (Micro-data): đếm số mili-giây ánh mắt bạn dừng lại, đo gia tốc ngón tay khi bạn cáu gắt, hay nhịp lướt chậm chạp khi bạn cô đơn lúc 2 giờ sáng. Từ hàng tỷ hành vi vật lý vô thức ấy, nó dùng không gian toán học để vẽ ra bản sao tâm lý của bạn. Nó nắm thóp tử huyệt của bạn nhạy bén và tàn nhẫn hơn cả người bạn đời chung chăn gối.</p>
<blockquote>
<p><em>Lượt share dẫu chẳng chạm tay,<br/>Lướt nhanh một nhịp phơi bày tâm can.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q36" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 3: Bạn tự nhận mình là người kỷ luật và có lý trí vững vàng. Vậy tại sao bạn không thể tập trung đọc trọn vẹn một cuốn sách, nhưng lại bất lực để ngón tay cuộn vô thức những video 15 giây đến tận sáng? Phải chăng ý chí của bạn chỉ là một trò đùa trước những dòng mã code?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bộ não của bạn đã bị "hack" hoàn toàn. Thuật toán biến điện thoại thành một sòng bạc kỹ thuật số bằng "Tỷ lệ trả thưởng biến thiên". Bằng cách trộn lẫn các video nhạt nhẽo với video giật gân, nó tước đi khả năng dự đoán của bạn. Hành động vuốt màn hình chính là kéo cần gạt máy đánh bạc. Nó ép não bạn liên tục tiết ra hoóc-môn Dopamine trong sự "kỳ vọng", biến bạn thành con nghiện tự nguyện để nền tảng bào tiền quảng cáo.</p>
<blockquote>
<p><em>Vuốt hoài cứ ngỡ là vui,<br/>Nào hay lý trí chôn vùi đêm thâu.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q37" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 4: Internet từng được kỳ vọng sẽ kết nối nhân loại. Vậy tại sao thế giới ngày càng ngập ngụa trong sự chửi rủa, thù hằn và chia rẽ? Có phải con người ngày càng độc ác hơn, hay đang có một bàn tay âm thầm cấu kết bầy đàn để trục lợi từ sự phẫn nộ của đám đông?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Con người không tệ đi, nhưng hệ sinh thái thông tin đã bị đầu độc. Thuật toán hiểu rằng sự điềm tĩnh không sinh ra tiền, còn "Sự phẫn nộ" (Outrage) mới giữ chân người dùng lâu nhất. Nó nhốt bạn vào "Buồng vang thông tin" (Echo Chamber), cố tình giấu đi góc nhìn toàn cảnh, và liên tục dội bom những tin tức cực đoan để chọc tức bạn. Chúng ta mạt sát nhau vì mỗi người đang bị nhốt trong một thực tại song song đầy thù hận, do chính thuật toán dàn dựng để vắt kiệt tương tác.</p>
<blockquote>
<p><em>Buồng vang nhốt kẻ cuồng si,<br/>Bơm mồi phẫn nộ chia ly cõi người.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q38" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 5: Tủ quần áo đã chật, tài khoản thì cạn kiệt, tại sao bạn vẫn bấm "Chốt đơn" mua một món đồ vô thưởng vô phạt lúc nửa đêm? Bạn thực sự cần nó, hay bạn vừa bị ép mua một "viên thuốc giảm đau" cho tâm lý kiệt quệ của chính mình?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Thuật toán không phục vụ nhu cầu có sẵn, nó KIẾN TẠO nhu cầu giả tạo. Nó canh đúng khoảnh khắc hàng rào lý trí của bạn yếu nhất (mệt mỏi, tự ti, cô đơn) để dội bom các tiêu chuẩn sống ảo. Ngay lúc đó, nút "Mua ngay" xuất hiện triệt tiêu mọi lực ma sát. Cái chốt đơn bốc đồng đó không phải để lấy món đồ, mà là một cú vung tiền nhằm xoa dịu cảm xúc chớp nhoáng. Nó thao túng tâm lý để bắt chuỗi cung ứng toàn cầu chạy theo sự bốc đồng của nhân loại.</p>
<blockquote>
<p><em>Đêm khuya trống rỗng âu lo,<br/>Chốt đơn giả tạo dâng trò mua vui.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q39" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 6: Một kẻ độc tài chĩa súng bắt bạn tuân lệnh, bạn sẽ phẫn nộ và đổ máu phản kháng. Nhưng làm sao để bạn lật đổ một chế độ bạo quyền tước đoạt hoàn toàn Ý CHÍ TỰ DO của bạn, trong khi nó vẫn ân cần ban phát cho bạn ảo giác rằng bạn đang làm chủ cuộc đời mình?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đó là tội ác hoàn hảo nhất của thế kỷ 21. Sự thao túng đáng sợ nhất không nằm ở sự ép buộc bằng bạo lực, mà ở việc định hình bối cảnh. Bằng cách âm thầm chọn lọc thông tin đầu vào trong nhiều năm, thuật toán đã từ từ lập trình lại nhận thức, định kiến và hệ giá trị của hàng tỷ người. Suy nghĩ thay đổi, hành động (từ mua sắm đến bầu cử) sẽ bị bẻ lái theo. Không có khẩu súng nào, chỉ có ảo giác về tự do. Kẻ điều khiển được vô thức của nhân loại, chính là kẻ đang vận hành cả thế giới.</p>
<blockquote>
<p><em>Tự do cứ ngỡ do mình,<br/>Nào hay thuật toán vô hình giật dây.</em></p>
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
