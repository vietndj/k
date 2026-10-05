import re

with open('logic19.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace TOC
toc_match = re.search(r'<ul class="ink-toc-list">.*?</ul>', content, re.DOTALL)
if toc_match:
    new_toc = '''<ul class="ink-toc-list">
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">THƯƠNG HIỆU CÁ NHÂN & ỐNG KÍNH</li>
<li><a class="ink-toc-link" href="#q1">Q1. Tín hiệu đắt giá</a></li>
<li><a class="ink-toc-link" href="#q2">Q2. Ánh mắt & Giọng ngực</a></li>
<li><a class="ink-toc-link" href="#q3">Q3. Triết lý One Lamp</a></li>
<li><a class="ink-toc-link" href="#q4">Q4. Tỷ lệ B-roll 82.6%</a></li>
<li><a class="ink-toc-link" href="#q5">Q5. Gọt dưa leo</a></li>
<li><a class="ink-toc-link" href="#q6">Q6. Case study thực chiến</a></li>
</ul>'''
    content = content[:toc_match.start()] + new_toc + content[toc_match.end():]

# Replace main content
main_match = re.search(r'(<article class="ink-content ink-mode-dialogue">)(.*?)(</article>)', content, re.DOTALL)
if main_match:
    new_main = '''<article class="ink-content ink-mode-dialogue">
<h2 style="font-family: var(--font-display-short); font-size: 24px;">PHẦN 1: HỆ THỐNG HÓA VÀ TÓM TẮT ĐỀ BÀI TỪ BẠN</h2>
<p>Hệ thống đã tiếp nhận và ghi nhận tuyệt đối các chỉ thị khắt khe từ bạn. Dưới đây là bản giải phẫu lại toàn bộ yêu cầu, đảm bảo không một tiêu chuẩn nào bị bỏ sót trước khi tiến hành thực thi:</p>
<ol>
<li><strong>Vị trí và Cấu trúc:</strong> Phải đặt phần tóm tắt yêu cầu này lên đầu tiên. Toàn bộ nội dung nghiên cứu (Talking Head, thương hiệu cá nhân, thần kinh học, góc quay dựng, case study) phải được tái cấu trúc hoàn toàn thành định dạng Hỏi - Đáp (Q&A).</li>
<li><strong>Về tính chất câu hỏi:</strong> Bắt buộc là các câu hỏi mở, cực kỳ sắc bén, mang tính gây shock nhằm đập tan mọi lầm tưởng, ảo tưởng của người mới xây kênh.</li>
<li><strong>Về tính chất câu trả lời:</strong> Đanh thép, ngắn gọn, trực diện. Giải phẫu cặn kẽ dựa trên nền tảng Tâm lý học tiến hóa và Khoa học thần kinh nhận thức (MNS, Autonomic Leakage, Somatic Markers).</li>
<li><strong>Về thi luật chốt hạ:</strong> MỖI câu trả lời bắt buộc kết thúc bằng đúng 2 câu thơ Lục Bát (luật 6-8). Tuân thủ nghiêm ngặt luật Bằng - Trắc và kỹ thuật gieo vần ngầm (chữ thứ 6 câu Lục vần với chữ thứ 6 câu Bát).</li>
<li><strong>Về văn phong:</strong> Lạnh lùng, sắc lẹm, khách quan. Loại bỏ hoàn toàn các danh xưng cá nhân và tuyệt đối không sử dụng văn mẫu sáo rỗng. Cơ cấu lại tư duy thành quy trình phản xạ thực chiến (Cognitive Re-engineering).</li>
<li><strong>Về quản trị hệ thống:</strong> Báo cáo nếu thiếu token để tiếp tục duy trì mạch văn.</li>
</ol>

<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<h2 style="font-family: var(--font-display-short); font-size: 24px;">PHẦN 2: ĐẠI PHẪU TỐI THƯỢNG - MA TRẬN HỎI ĐÁP BẺ GÃY NHẬN THỨC</h2>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q1" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 1: Có phải bạn đang ảo tưởng rằng chỉ cần bật máy quay, đọc trôi chảy một kịch bản mượt mà là đủ để xây dựng một "thương hiệu cá nhân" quyền lực? Tại sao bộ não khán giả lại khinh bỉ và phát lệnh đào thải bạn chỉ sau chưa tới 100 mili-giây?</h2>
<div class="dialogue-response">
<p><strong>⚡ ĐÁP ÁN SẮC BÉN:</strong><br/>
Thương hiệu cá nhân không phải là lượt view ảo hay sự nổi tiếng phù phiếm. Dưới lăng kính tiến hóa, đó là "Tín hiệu đắt giá" (Costly Signaling) – hành vi đem thân xác, khuôn mặt và danh dự vật lý ra thế chấp để bảo chứng cho sự thật. Talking Head là một trận cận chiến mặt-đối-mặt khốc liệt ở cự ly sinh tồn 60cm. Mọi nỗ lực diễn xuất hay đọc vẹt đều tạo ra sự "lệch pha sinh lý" (Autonomic Leakage). Hệ Nơ-ron gương (MNS) và Trục Não-Ruột của người xem sẽ quét ra sự giả tạo này dưới 100 mili-giây, dội một cảm giác bài xích xuống dạ dày. Họ vuốt bỏ (swipe) vì bản năng sinh tồn báo động: Kẻ này đang nói dối.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Thân mang thế chấp khung <strong>hình</strong>,</em><br/>
<em>Máy quay soi rõ tâm <strong>tình</strong> cạn sâu.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q2" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 2: Tại sao nỗ lực mở to mắt nhìn trừng trừng vào ống kính và cất lên chất giọng the thé chốt sale lại là nhát dao tự sát, kết liễu toàn bộ sự tôn trọng từ người xem? Đâu là vũ khí sinh học thực sự để thao túng dòng chảy thời gian của video?</h2>
<div class="dialogue-response">
<p><strong>⚡ ĐÁP ÁN SẮC BÉN:</strong><br/>
Dán mắt vào máy nhắc chữ tạo ra "độ trễ nhận thức" (Cognitive Lag), tước đoạt sinh khí cơ mặt và biến bạn thành xác sống. Hãy đập bỏ Teleprompter. Kích hoạt "Ánh mắt truy hồi ký ức" (Episodic Memory Retrieval): liếc nhẹ nhãn cầu để lục lọi dữ liệu thật trong vỏ não, rồi phóng tia nhìn khóa mục tiêu (Lock-eye) xuyên thủng thấu kính. Đồng thời, giọng the thé nén ở cổ họng là tín hiệu của kẻ yếu thế. Phản xạ sống còn là bơm khí xuống cơ hoành, dùng giọng ngực (Chest Voice) trầm ấm và tung nhát chém thời gian: ngắt câu lạnh lùng theo nhịp 5-7 từ. Kẻ kiểm soát nhịp thở chính là kẻ thao túng không gian.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Mắt sâu lục lọi ngôn <strong>từ</strong>,</em><br/>
<em>Giọng trầm nén khí uy <strong>dư</strong> muôn phần.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q3" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 3: Vung hàng chục triệu mua dàn đèn đánh sáng rực rỡ phẳng lì, cùng phông nền ảo diệu, bạn có biết chính sự "hoàn hảo sạch sẽ" đó đang lột sạch quyền uy của một chuyên gia?</h2>
<div class="dialogue-response">
<p><strong>⚡ ĐÁP ÁN SẮC BÉN:</strong><br/>
Ánh sáng phẳng (Flat lighting) san bằng mọi hình khối, tiêu diệt chiều sâu tâm lý và biến khuôn mặt thành một tờ giấy vô tri. Hãy ứng dụng triết lý "One Lamp Beats Five" (Một đèn chấp năm): dùng ánh sáng định hướng Chiaroscuro, tàn nhẫn giữ lại bóng tối trên nửa khuôn mặt để tạc nên sự góc cạnh, bí ẩn và quyền lực áp đảo. Đập bỏ tư duy khúm núm của kẻ đi van nài sự chú ý, cấy vào não tâm thế "người chủ nhà" điềm tĩnh. Đặt góc máy Eye-Level tước bỏ phòng vệ, vi chỉnh Low-Angle để ép vị thế. Bối cảnh thực chứng (Environmental Staging) bừa bộn phía sau chính là bản CV vật lý đanh thép nhất.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Một đèn tạc nửa hình <strong>hài</strong>,</em><br/>
<em>Nửa chìm bóng tối xưng <strong>tài</strong> nghệ nhân.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q4" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 4: Cứ phơi nguyên cái mặt ra thao thao bất tuyệt suốt cả video, bạn có nhận ra mình đang bức tử thùy trán khán giả bằng cơn tê liệt thị giác? Công thức nào để tiêm Dopamine liên tục, ép bộ não họ phải quy hàng tuyệt đối?</h2>
<div class="dialogue-response">
<p><strong>⚡ ĐÁP ÁN SẮC BÉN:</strong><br/>
Bộ não linh trưởng khát khao tính vật lý và cực kỳ mau chán. Khuôn mặt bạn chỉ được chiếm tối đa 17.4% thời lượng làm mỏ neo dẫn dắt (A-roll), 82.6% còn lại phải đập B-roll trám hình liên tục đè lên tiếng nói để ném bằng chứng vào nhận thức. Phải xé rào ảo ảnh bằng các đạo cụ xúc giác: tiếng gõ mic (ASMR), vật thể cầm nắm được. Cứ 3-5 giây, hãy tát vào thị giác khán giả bằng cú bẻ gãy nhịp điệu (Pattern Interrupts): tung chớp đen tối giản (Blackout) hay phóng to đột ngột từ khóa chốt hạ (Punchline Keywords). Tuyệt đối không cho não họ một tích tắc nào để xao nhãng.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Ảo hư giăng mắc mịt <strong>mờ</strong>,</em><br/>
<em>Trám hình đập nhịp phá <strong>bờ</strong> vô minh.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q5" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 5: Cứ nói vấp là vươn tay tắt máy quay, rồi mang lên bàn dựng lóng ngóng che đậy vết cắt. Đây là quy trình làm nội dung hay là hành vi khâu vá một tấm giẻ rách? Sự thật đẫm máu trên bàn dựng là gì?</h2>
<div class="dialogue-response">
<p><strong>⚡ ĐÁP ÁN SẮC BÉN:</strong><br/>
Với tay tắt máy giữa chừng là tự tay bẻ gãy luồng khí lực và trạng thái sinh lý (Somatic state) quyền uy vừa dày công thiết lập. Kỷ luật thép: Bấm máy chạy liên tục (Continuous Take). Vấp? Im lặng 3 giây, thở sâu rồi nhả chữ lại. Đưa lên bàn dựng, lôi công cụ tách xóa (Ripple Delete) ra thao tác "Gọt dưa leo" – trảm sạch không thương tiếc mọi khoảng chết (Dead Air) và tiếng lấy hơi. Che giấu vết cắt bằng cú giật Snap Zoom 1.15x. Đỉnh cao nhất là đòn "The Face Return": Ở câu chốt hạ cuối cùng, lột bỏ toàn bộ hình trám, giật khung hình về 100% khuôn mặt tĩnh lặng để đóng đinh chân lý.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Dưa leo gọt sạch hai <strong>đầu</strong>,</em><br/>
<em>Khung hình ép sát găm <strong>câu</strong> trọn đời.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q6" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 6: Ma trận lý thuyết tàn khốc này có phải chỉ là mớ ngôn từ tâm lý học suông trên giấy, hay đã được chứng thực bằng kết quả của những con quái vật đang thống trị thuật toán?</h2>
<div class="dialogue-response">
<p><strong>⚡ ĐÁP ÁN SẮC BÉN:</strong><br/>
Đây là những lưỡi dao đã tạo nên các kiến trúc sư thao túng nhận thức lõi đời. Hãy nhìn Shogentle tạc khối khuôn mặt với 1 đèn Chiaroscuro và lạng bỏ Dead Air vô hình. Nhìn Sắc Ánh thi triển tàn bạo tỷ lệ vàng 82.6% B-roll và chớp đen ngắt nhịp. Alex Boisset kích hoạt móc câu xúc giác "Walk-in Entry" và Mic-Tap. Aayush Swamy neo đậu kiến thức vào bảng trắng vật lý. Jacoub Anwar thao túng tâm lý qua 5 góc máy điện ảnh, hay Mridupawan bẻ cong không gian bằng J-Cut, L-Cut kết hợp ổ cứng thật trên tay. Họ không làm video giải trí, họ thiết kế cơ chế sinh học để hệ thần kinh người xem phải đầu hàng.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Thực tài chói lọi càn <strong>khôn</strong>,</em><br/>
<em>Hiểu sâu bản chất nuốt <strong>hồn</strong> thế gian.</em></p>
</blockquote>
</div>
</div>

</article>'''
    content = content[:main_match.start(1)] + new_main + content[main_match.start(3):]

# Update page title
title_match = re.search(r'<title>.*?</title>', content)
if title_match:
    content = content[:title_match.start()] + '<title>Talking Head & Thương Hiệu</title>' + content[title_match.end():]

with open('logic20.html', 'w', encoding='utf-8') as f:
    f.write(content)

