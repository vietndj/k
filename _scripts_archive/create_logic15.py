import re

with open('logic14.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Document Title
title_pattern = r'<title>.*?</title>'
content = re.sub(title_pattern, '<title>[INKDOC-15] KỊCH TÍNH THỊ GIÁC VÀ B-ROLL</title>', content)

# 2. Update TOC
new_toc = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">KỊCH TÍNH THỊ GIÁC & B-ROLL</li>
<li><a class="ink-toc-link" href="#summary">Hệ thống hóa vấn đề</a></li>
<li><a class="ink-toc-link" href="#q1">Q1. Nhịp điệu và thời gian</a></li>
<li><a class="ink-toc-link" href="#q2">Q2. Định lượng cảnh trám</a></li>
<li><a class="ink-toc-link" href="#q3">Q3. Nút tử thần "phẳng lì"</a></li>
<li><a class="ink-toc-link" href="#q4">Q4. Kịch tính khoảng "Khựng"</a></li>
<li><a class="ink-toc-link" href="#q5">Q5. Phản xạ vô điều kiện</a></li>
"""
toc_pattern = r'(<ul class="ink-toc-list">).*?(</ul>)'
content = re.sub(toc_pattern, r'\1\n' + new_toc + r'\n\2', content, flags=re.DOTALL)

# 3. Update Content
new_content = """
<h1 class="is-short">KỊCH TÍNH THỊ GIÁC & B-ROLL: NGHỆ THUẬT ĐẠO DIỄN VÀ DIỄN XUẤT</h1>
<div class="ink-meta">
  <span>System Identity: [INKDOC-15]</span>
  <span class="mx-2">•</span>
  <span>Render Mode: [Dialogue]</span>
</div>

<div style="margin-bottom: 3rem;">
    <h2 id="summary" style="margin-top: 0; font-size: 1.5rem; font-weight: 600; color: var(--ink-text); padding-bottom: 0.5rem; border-bottom: 1px solid var(--ink-border);">PHẦN 1: HỆ THỐNG HÓA VÀ TÓM TẮT CÁC CÂU HỎI CỦA BẠN</h2>
    <p>Trước khi đập tan các lầm tưởng, dưới đây là bức tranh toàn cảnh tóm gọn lại toàn bộ những trăn trở, thắc mắc cốt lõi của bạn từ đầu buổi trò chuyện đến giờ:</p>
    <ol style="margin-bottom: 2rem;">
        <li><strong>Vấn đề Thời gian & Căn nhịp:</strong> Đặt nhiều góc máy nhưng chỉ ngồi viết thì đổi góc không hiệu quả, cần hành động. Vậy bao nhiêu giây thì nên có hành động và chuyển góc máy? Làm sao để tự căn thời gian lúc quay mà không phải đếm nhẩm trong đầu (tránh làm mặt bị cứng đơ)?</li>
        <li><strong>Vấn đề Phân loại & Cấu trúc:</strong> Trong quá trình quay, các hành động như gõ bút, chống cằm, thở dài, lật trang... diễn ra lộn xộn. Cần một hệ thống phân loại khoa học (tỷ lệ động/tĩnh, thời lượng cho mỗi loại) để tạo thành một bộ khung logic dễ dàng áp dụng cho mọi bối cảnh.</li>
        <li><strong>Vấn đề Logic & Căn nguyên:</strong> Tại sao mọi cảnh trám lại phải tuân theo tiến trình <em>"Khởi động -> Hăng say -> Suy nghĩ -> Giải quyết -> Thư giãn"</em>? Logic này chưa thuyết phục, cần giải thích sâu sắc dưới góc nhìn vật lý học, năng lượng, tiến hóa, tâm lý học, và chứng minh bằng cảnh vừa làm máy tính vừa chép tay.</li>
        <li><strong>Vấn đề Thực chiến & Ghi nhớ:</strong> Làm sao để nhớ vòng lặp 5 bước này thay vì học vẹt lý thuyết? Ứng dụng chúng vào các bối cảnh đời thường tẻ nhạt (như pha cà phê, đọc sách, làm máy tính, ngồi thiền, tưới cây, setup đồ nghề) như thế nào? Cần những lối tắt nào để cơ thể tự động diễn xuất chuẩn xác một cách vô thức?</li>
    </ol>
</div>

<h2 style="margin-top: 4rem; margin-bottom: 2rem; font-size: 1.5rem; font-weight: 600; color: var(--ink-text); padding-bottom: 0.5rem; border-bottom: 1px solid var(--ink-border);">PHẦN 2: HỎI ĐÁP SẮC BÉN - ĐẬP TAN LẦM TƯỞNG</h2>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q1" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 1: Bằng cách nào mà chiếc đồng hồ đếm nhẩm "1-2-3 giây" trong đầu, thứ bạn tưởng là thước đo nhịp điệu hoàn hảo, lại trở thành liều thuốc độc giết chết toàn bộ thần thái của bạn trước ống kính?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Lầm tưởng lớn nhất của bạn là đánh đồng "thời gian quay" và "thời lượng dựng". Khi bạn bận đếm số, não bộ lập tức chuyển sang cơ chế tính toán khô khan, làm ánh mắt vô hồn và cơ mặt căng cứng. Sự thật là lúc quay, tuyệt đối không được đếm giây hay cắt vụn. Hãy bấm máy và diễn liên tục một mạch dài. Thay vì đếm, hãy mượn nhịp thời gian sinh lý thật bằng cách chép trọn vẹn một đoạn văn, hoặc lẩm nhẩm một câu "độc thoại nội tâm". Thời gian của công việc thật sẽ tự sinh ra nhịp điệu chuẩn xác nhất, còn việc cắt ra 3 giây hay 5 giây là quyền lực của bạn lúc ngồi trên phần mềm dựng phim.</p>
<blockquote>
<p><em>Quay phim chớ đếm từng giây,<br/>Cứ làm việc thật, phim đây có hồn.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q2" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 2: Tại sao việc ghép bừa bãi hàng tá tiểu tiết xoa cằm, lật trang, cắn bút lại tố cáo sự nghiệp dư, trong khi chỉ cần nắm vững 10% các "chuyển động bản lề" là đủ để thao túng hoàn toàn thị giác khán giả?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Ném bừa hành động vào khung hình chỉ tạo ra rác thị giác. Một cảnh trám chuẩn mực phải tuân theo định lượng tàn nhẫn: 40% Vĩ mô (chuyển động lớn giữ nhịp), 30% Tĩnh (tạo chiều sâu nội tâm), và 20% Vi mô (tiểu tiết tạo âm thanh ASMR). Đỉnh cao nghệ thuật giấu ở 10% còn lại: Nhóm hành động Bản lề (vươn vai, chồm người tới trước, vung tay vỗ bàn). Bằng cách đè nhát dao cắt chuyển góc máy vào ngay chính giữa khoảnh khắc lực vật lý đang bung ra, động năng sẽ giấu nhẹm hoàn toàn vết cắt ghép. Khán giả bị lôi cuốn theo chuyển động vật lý mà không hề nhận ra máy quay vừa đổi góc.</p>
<blockquote>
<p><em>Cảnh quay phân lớp rõ ràng,<br/>Cắt ngay chuyển động, ngỡ ngàng người xem.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q3" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 3: Dưới góc nhìn tiến hóa thảm khốc, tại sao một thước phim nhân vật cắm cúi làm việc trơn tru, say mê hoàn hảo từ đầu đến cuối lại chính là đường điện tâm đồ phẳng lì đưa người xem vào giấc ngủ ngàn thu?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì tự nhiên học không bao giờ dung túng sự trơn tuột! Vật lý cần ma sát để sinh công, tế bào cần chạm đáy năng lượng để sạc lại. Đặc biệt, não bộ nguyên thủy của con người được tiến hóa để đánh hơi rủi ro và phớt lờ vùng an toàn. Khán giả chỉ thực sự dán mắt vào video khi thấy bạn vấp phải "biến cố", và bộ não họ chỉ phóng thích Dopamine (hoóc-môn thỏa mãn) khi thấy bạn vượt qua nó. Một thước phim thiếu đi điểm khựng, thiếu sự giằng xé hay nút thắt tâm lý, vĩnh viễn chỉ là một đoạn camera an ninh vô tri. Khán giả khao khát nhìn thấy bạn bế tắc trước khi tỏa sáng.</p>
<blockquote>
<p><em>Phim trơn là nốt tử thần,<br/>Phải sinh bế tắc, muôn phần thăng hoa.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q4" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 4: Đào đâu ra kịch tính sinh tử trong những sinh hoạt tẻ nhạt đến vô tri như pha một ly cà phê hay ngồi tĩnh tâm nhắm mắt? Bí thuật nào lột xác những bối cảnh bình phàm ấy thành những phân cảnh nghẹt thở?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Kịch tính không cần đến súng đạn, nó nằm trọn ở khoảng "KHỰNG". Vạn vật đều có thể ép vào khuôn đúc: <em>Khởi - Hăng - Khựng - Gỡ - Xả</em>.<br>
Với pha cà phê: Bạn đang rót nước cuộn trào (Hăng), đột ngột nín thở nheo mắt bất động nhìn cân điện tử nhảy số (Khựng), rồi giật phắt chiếc ấm ra (Gỡ). Với thiền định: Đang hít thở tĩnh lặng (Hăng), bất ngờ nhíu mày giằng xé nội tâm vì cơn ngứa ở mũi (Khựng), rồi nghiến răng hít hơi sâu nuốt trôi sự bực tức (Gỡ). Chữ Khựng là hố đen hút trọn sự chú ý. Tự tay tạo ra một điểm nghẽn năng lượng tâm lý rồi đập vỡ nó, bạn sẽ có kịch tính đỉnh cao.</p>
<blockquote>
<p><em>Bình thường cảnh nhạt buồn tênh,<br/>Thêm vào khoảng khựng, lênh đênh cõi tình.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q5" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 5: Bằng những lối tắt nào mà bạn có thể thao túng trực tiếp tủy sống, ép cơ bắp bung kỹ năng diễn xuất xuất thần mà không cần bắt não bộ phải nhồi nhét nửa chữ kịch bản hàn lâm?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Hãy cất lý trí đi và mượn phản xạ vô điều kiện qua 2 phím tắt sinh tồn.<br>
Cách 1, "Đồng bộ hô hấp": Khớp hành động khung hình y như đi bơi (Hít đà bắt đầu -> Bơi lướt đi -> Nín thở nghẹn lồng ngực lúc gặp bế tắc -> Vùng vẫy ngoi lên xử lý -> Thở hắt ra xả hơi).<br>
Cách 2, "Sự cố giả lập": Đừng ép cơ mặt diễn, cứ làm thật 100% nhưng tự giao kèo với bản thân phải vấp một lỗi giả (vờ rơi nắp bút, vờ thấy con rệp lúc tưới cây, vờ máy tính bị treo). Phản xạ sinh tồn sẽ ngay lập tức phanh cơ thể bạn lại và vung tay xử lý mượt mà, sống động đến độ chính bạn xem lại cũng phải nổi da gà.</p>
<blockquote>
<p><em>Chớ gồng diễn xuất làm chi,<br/>Mượn ngay nhịp thở, khắc ghi vào hồn.</em></p>
</blockquote>
</div>
</div>

<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 5 rãnh Data cốt lõi...)</em></p>
"""

content_pattern = r'(<article class="ink-content ink-mode-dialogue">).*?(</article>)'
content = re.sub(content_pattern, r'\1\n' + new_content + r'\n\2', content, flags=re.DOTALL)

with open('logic15.html', 'w', encoding='utf-8') as f:
    f.write(content)

