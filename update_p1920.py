import sys

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'r', encoding='utf-8') as f:
    content = f.read()

toc_insert = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 19: 11 PHÁT SÚNG TRUY VẤN</li>
<li><a class="ink-toc-link" href="#p19_1">1. Hoài nghi bản chất</a></li>
<li><a class="ink-toc-link" href="#p19_2">2. Truy vấn mục đích</a></li>
<li><a class="ink-toc-link" href="#p19_3">3. Thách thức tính chân thực</a></li>
<li><a class="ink-toc-link" href="#p19_4">4. Đòi hỏi logic cơ học</a></li>
<li><a class="ink-toc-link" href="#p19_5">5. Gỡ rối hệ thống</a></li>
<li><a class="ink-toc-link" href="#p19_6">6. Bẻ gãy ngụy biện</a></li>
<li><a class="ink-toc-link" href="#p19_7">7. Lối thoát danh dự</a></li>
<li><a class="ink-toc-link" href="#p19_8">8. Đòi hỏi trực diện</a></li>
<li><a class="ink-toc-link" href="#p19_9">9. Điểm mù chuyển đổi</a></li>
<li><a class="ink-toc-link" href="#p19_10">10. Kiểm chứng thực chiến</a></li>
<li><a class="ink-toc-link" href="#p19_11">11. Giác ngộ phương pháp</a></li>

<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 20: BẺ KHÓA HÀNH VI</li>
<li><a class="ink-toc-link" href="#p20_q100">Q100. Đạo lý vĩ mô trí thức</a></li>
<li><a class="ink-toc-link" href="#p20_q101">Q101. Bác sĩ ung thư</a></li>
<li><a class="ink-toc-link" href="#p20_q102">Q102. AI viết kịch bản</a></li>
<li><a class="ink-toc-link" href="#p20_q103">Q103. Lắng nghe độ lệch</a></li>
<li><a class="ink-toc-link" href="#p20_q104">Q104. Kẻ say rượu cãi càn</a></li>
<li><a class="ink-toc-link" href="#p20_q105">Q105. Hạch hạnh nhân báo động</a></li>
<li><a class="ink-toc-link" href="#p20_q106">Q106. Nghệ thuật đổi vị thế</a></li>
<li><a class="ink-toc-link" href="#p20_q107">Q107. Năng lực Metacognition</a></li>
"""

body_insert = """
<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 19 -->
<h1 class="is-short">PHẦN 19: HỆ THỐNG HÓA 11 PHÁT SÚNG TRUY VẤN (TỔNG KẾT)</h1>
<p><em>(Dưới tư cách là một Kiến trúc sư Hệ thống & Chuyên gia Tâm lý học Hành vi / Storytelling Thực chiến, tôi đã đưa toàn bộ dữ liệu cuộc trò chuyện của chúng ta vào buồng mổ DEEP THINK để rã đông và tái cấu trúc. Lộ trình anh đi từ hoài nghi bề mặt đến việc chạm tay vào lõi của sự thật:)</em></p>

<ul>
    <li id="p19_1"><strong>1. Hoài nghi bản chất:</strong> Logic thực sự của việc "ngại lên video" là gì? Nằm trong 18 lý do ngụy biện kia hay đây là bản chất sinh học chung của loài người khi gặp cái mới?</li>
    <li id="p19_2"><strong>2. Truy vấn mục đích:</strong> Bóc tách các tầng logic nhận thức này rốt cuộc để làm gì trong thực chiến?</li>
    <li id="p19_3"><strong>3. Thách thức tính chân thực:</strong> Bóc tách sự thật bắt buộc phải đi từ trải nghiệm tự thân sao? Dùng kỹ thuật kịch bản (fake) để nói trúng tim đen thì có bị lộ không?</li>
    <li id="p19_4"><strong>4. Đòi hỏi logic cơ học:</strong> Tôi chưa hiểu vì sao lại bóc tách được! Hãy giải phẫu bằng lăng kính vật lý, cơ học thay vì cảm xúc tâm lý.</li>
    <li id="p19_5"><strong>5. Gỡ rối hệ thống:</strong> Đã hiểu não dùng kiến thức để hợp lý hóa cái cớ. Nhưng phân tích Tầng 2.5 rốt cuộc giúp ích gì, chẳng lẽ chỉ để "nói trúng tim đen" người khác?</li>
    <li id="p19_6"><strong>6. Bẻ gãy ngụy biện:</strong> Bác sĩ ung thư đâu cần bị ung thư mới chữa được! Lấy ví dụ đó để ép "người làm nội dung phải có trải nghiệm" là sai logic!</li>
    <li id="p19_7"><strong>7. Bắt mạch Lối thoát danh dự (Lần 1):</strong> Tại sao mục đích tối thượng chỉ là "Tặng lối thoát danh dự"? Người ta có thực sự khát khao nó không và logic xoa dịu là gì?</li>
    <li id="p19_8"><strong>8. Đòi hỏi sự trực diện (Lần 2):</strong> Ví dụ ông thợ mộc dài dòng quá. Giải thích lại thật ngắn gọn: Tại sao họ CẦN Lối thoát danh dự?</li>
    <li id="p19_9"><strong>9. Điểm mù chuyển đổi:</strong> Tại sao KHÔNG cung cấp Lối thoát danh dự thì KHÔNG BAO GIỜ bán được hàng?</li>
    <li id="p19_10"><strong>10. Kiểm chứng thực chiến:</strong> Hãy chứng minh bằng 3 ví dụ ở các ngành khác nhau (người uống rượu nóng tính, sếp 40 tuổi học tiếng Anh, bán SaaS B2B).</li>
    <li id="p19_11"><strong>11. Giác ngộ phương pháp:</strong> Bản chất Storytelling là bóc tách sự thật? Và gốc rễ là năng lực tự quan sát Metacognition? Xin bài tập thực hành lắng nghe 3 tầng này!</li>
</ul>

<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 20 -->
<h1 class="is-short">PHẦN 20: HỎI XOÁY SỐC TÂM LÝ & BẺ KHÓA HÀNH VI</h1>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q100" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 100: Tại sao những trí thức, chuyên gia uyên bác nhất lại luôn mượn các đạo lý vĩ mô để khước từ một hành động cực kỳ nhỏ bé (như bấm máy quay)? Phải chăng họ quá đẳng cấp?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Hoàn toàn ngược lại! Lý lẽ thốt ra càng vĩ mô, nỗi sợ giấu bên dưới càng trẻ con. Bản ngã con người thà chịu nghèo chứ không bao giờ chịu hèn. Khi chạm vào cái mới, họ đối diện nguy cơ rớt đài từ "chuyên gia" xuống làm "kẻ lóng ngóng". Để sinh tồn, não bộ lập tức sản xuất ra chiếc khiên đạo lý Tầng 2.5 (<em>"tôi bận làm việc lớn", "hữu xạ tự nhiên hương"</em>) nhằm bảo vệ thể diện và che đậy sự run rẩy cơ bắp bên trong.</p>
<blockquote>
<p><em>Miệng hô đạo lý thanh <strong>cao</strong>,</em><br/>
<em>Bên trong run rẩy biết <strong>bao</strong> nhiêu lần.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q101" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 101: Bác sĩ ung thư không cần mắc bệnh mới chữa được. Vậy cớ sao việc bóc tách tâm lý khách hàng lại BẮT BUỘC phải đi từ trải nghiệm tự thân của bạn? Đó chẳng phải ngụy biện sao?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Ung thư là bệnh lý thể chất, khối u có thể nhìn thấy qua phim chụp X-quang. Nhưng Sự Sĩ Diện là trò lừa đảo vô hình của tâm trí! Bạn không thể dùng máy móc để đo lường nỗi sợ mất mặt. Kẻ đứng ngoài hàng rào chưa từng bị sức nặng của danh xưng đè bẹp, thì mọi kịch bản thốt ra chỉ là sự phán xét trịch thượng sặc mùi lý thuyết, khiến khách hàng đóng sập não bộ.</p>
<blockquote>
<p><em>Bệnh kia máy móc soi <strong>hình</strong>,</em><br/>
<em>Nỗi đau sĩ diện tự <strong>mình</strong> nếm qua.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q102" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 102: Thời đại AI sinh kịch bản trong 3 giây, tôi hoàn toàn có thể viết ra kịch bản thấu cảm tột độ. Tại sao mang nó lên video lại là hành vi tự sát đẫm máu cho nhân hiệu?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Vì ống kính máy quay là cỗ máy dò nói dối sinh lý tàn nhẫn nhất! Chữ viết có thể giả mạo, nhưng cơ thể thì không. Sự căng cứng của cơ mặt, ánh mắt tính toán và việc thiếu vắng nụ cười tự trào sẽ bán đứng bạn. Người chưa từng bị lột trần bản ngã, vĩnh viễn không thể sở hữu những vi biểu cảm thả lỏng bao dung để xoa dịu người khác.</p>
<blockquote>
<p><em>Văn hay chữ tốt mượn <strong>lời</strong>,</em><br/>
<em>Lên hình giả tạo rụng <strong>rời</strong> tay chân.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q103" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 103: Bỏ qua mọi trực giác tâm linh mơ hồ, công thức vật lý sắc lạnh nào giúp bạn lột trần bộ mặt thật của bất kỳ vị sếp đạo mạo nào chỉ trong 3 giây giao tiếp?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Đó là công cụ giải phẫu: "Lắng nghe độ lệch". Hãy lấy <strong>[Lời đạo lý vĩ mô] TRỪ ĐI [Thao tác cơ bắp đang bị kẹt]</strong>. Khách chê nước hồ bơi bẩn, nhưng sự thật là đôi chân đang khựng lại ở mép nước. Sự khập khiễng vật lý đó chính là điểm nghẽn của nỗi sợ hãi sặc nước trước đám đông. Chân lý luôn nằm trần trụi ở khối cơ bắp đang tê liệt, không nằm ở vỏ bọc ngôn từ.</p>
<blockquote>
<p><em>Ngôn từ vỏ bọc phô <strong>trương</strong>,</em><br/>
<em>Chân tay luống cuống chỉ <strong>đường</strong> tim đen.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q104" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 104: Tại sao một người say rượu cãi càn, nếu bạn ép họ nhận sai họ sẽ đập bàn bỏ đi, nhưng nếu bạn bảo "hôm qua chắc do mày say/mệt" thì họ lại lập tức làm hòa? Khách hàng có giống vậy không?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Khách hàng y hệt như người say! Họ bế tắc, thèm khát giải pháp nhưng bị giam cầm trong cái bẫy sĩ diện. Tự nhận sai thì thành kẻ nuốt lời, tự tát vào mặt mình. Họ khao khát một lối thoát nhưng không bao giờ há miệng xin. Việc bạn mượn cớ (do rượu, do bận, do tuổi tác) đã hợp pháp hóa sự yếu kém của họ, cho họ một cái bục đàng hoàng để bước xuống mà không bị người đời chê cười.</p>
<blockquote>
<p><em>Lỡ buông đạo lý hôm <strong>nao</strong>,</em><br/>
<em>Bây giờ kẹt cứng làm <strong>sao</strong> mở lời.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q105" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 105: Khi đã bắt đúng tim đen và nỗi đau, tại sao dồn ép khách hàng thừa nhận điểm yếu lại là nhát dao tự kết liễu mọi nỗ lực chốt sale của bạn?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Vì dồn con người vào góc tường bóc mẽ sẽ lập tức kích hoạt Hạch hạnh nhân (Amygdala) báo động đỏ. Họ thà cắn trả, thà hất đổ bàn cờ, thà chịu phá sản chứ tuyệt đối không để kẻ khác chà đạp lòng tự trọng. Ép họ thừa nhận sự dốt nát là bạn đang bóp nghẹt đường sống sinh học của cái tôi. Thắng một cuộc cãi vã logic, bạn mất vĩnh viễn dòng tiền!</p>
<blockquote>
<p><em>Dồn người vào góc đường <strong>cùng</strong>,</em><br/>
<em>Não kia đóng sập lửa <strong>bùng</strong> oán than.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q106" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 106: Bằng ma thuật nào mà một khóa học ngoại ngữ hay một phần mềm quản lý lại khiến những khách hàng bảo thủ nhất sẵn sàng quẹt thẻ mua điên cuồng trong niềm kiêu hãnh tột độ?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Đó là nghệ thuật "Viết lại lý do" - Đổi vị thế! Đừng bán khóa chữa dốt, hãy bán "Khóa đàm phán chiến lược cho sếp 40 tuổi". Đừng chê giám đốc mù công nghệ, hãy bán phần mềm "Làm đứa chạy việc vặt để sếp rảnh tay đi ngoại giao". Rút ví mua hàng phải là một nghi thức tôn vinh thể diện. Khi bạn giữ được lòng kiêu hãnh cho khách, họ sẽ kiêu hãnh dâng tiền cho bạn.</p>
<blockquote>
<p><em>Bán buôn chớ dập lòng <strong>kiêu</strong>,</em><br/>
<em>Nâng tầm danh dự khách <strong>tiêu</strong> tiền liền.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p20_q107" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 107: Sự thức tỉnh tàn khốc nhất mà bạn BẮT BUỘC phải trải qua trước khi muốn đi bóc tách tâm trí, thao túng hành vi hay viết kịch bản Storytelling là gì?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Đó là năng lực Siêu nhận thức (Metacognition) - Khả năng bắt quả tang chính mình! Mỗi khi ngón tay bạn khựng lại trước một việc khó, và não bộ nôn ra cái cớ <em>"để mai chuẩn bị thêm cho chỉn chu"</em>, hãy tự tát mình một cái: <em>"Mày đang hèn!"</em>. Kẻ nào chưa từng lột trần và cười nhạo lớp áo sĩ diện của chính bản thân, vĩnh viễn không đủ tư cách để mổ xẻ thiên hạ.</p>
<blockquote>
<p><em>Chưa từng tự bóc vỏ <strong>mình</strong>,</em><br/>
<em>Làm sao thấu suốt nhân <strong>tình</strong> thế gian.</em></p>
</blockquote>
</div>
</div>
"""

q99_marker = '<li><a class="ink-toc-link" href="#p18_q99">Q99. Ép bản thân ngủ</a></li>'
content = content.replace(q99_marker, q99_marker + '\n' + toc_insert)

split_token = '<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>'
parts = content.split(split_token)

if len(parts) >= 2:
    new_content = parts[0] + body_insert + '\n' + split_token + parts[1]
    with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: logic24.html updated with Q100-Q107.")
else:
    print("FAILED: split_token not found.")

