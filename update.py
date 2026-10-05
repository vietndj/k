import re

with open('logic08.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Thêm TOC
toc_insertion = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">BẢN CHẤT SỰ KIỆT QUỆ</li>
<li><a class="ink-toc-link" href="#q12">Q1. Cạn kiệt tài nguyên</a></li>
<li><a class="ink-toc-link" href="#q13">Q2. Đàn áp bản năng</a></li>
<li><a class="ink-toc-link" href="#q14">Q3. Tế bào thần kinh gương</a></li>
<li><a class="ink-toc-link" href="#q15">Q4. Boong-ke vật lý</a></li>
<li><a class="ink-toc-link" href="#q16">Q5. Kỹ thuật bám rễ</a></li>
<li><a class="ink-toc-link" href="#q17">Q6. Chấp nhận tuyệt đối</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 2. Thêm Nội dung
qa_content = """
<hr style="margin: 4rem 0; border: none; border-top: 4px solid var(--ink-text);"/>
<h1 class="is-short">BẢN CHẤT SỰ KIỆT QUỆ VÀ SỰ TẬP TRUNG</h1>
<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q12" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 1: Bạn vẫn huyễn hoặc rằng "năng lượng" cạn kiệt ngoài đường là do ma quỷ bủa vây hay tâm linh yếu đuối? Sự thật tàn khốc nào đang diễn ra ngay trong hộp sọ của bạn mỗi khi bạn bước ra phố?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong> Kẻ bòn rút sinh lực thực sự chính là bộ não của bạn! Dù chỉ chiếm 2% trọng lượng, nó thiêu rụi tới 20% năng lượng toàn thân. Sự mệt lả bạn trải qua là hiện tượng "Cạn kiệt tài nguyên nhận thức". Giữa phố xá, não bộ bị ép rà soát, xử lý và phân tích hàng vạn dữ liệu hình ảnh, âm thanh ngoài ý muốn. Bạn không hề kiệt quệ vì tâm linh, bạn đang bị vắt kiệt về mặt sinh lý học!</p>
<blockquote>
<p><em>Tưởng đâu ma quỷ vô hình,<br/>Hóa ra não bộ gồng mình sớm trưa.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q13" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 2: Bằng cách nào việc bạn cắn răng gồng mình, kiên quyết "không thèm liếc nhìn" những bóng hồng quyến rũ trên phố lại chính là nhát dao chí mạng tự kết liễu sinh lực của bạn nhanh nhất?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong> Bởi bạn đang tự nguyện châm ngòi một cuộc nội chiến đắt đỏ! Bị thu hút bởi cái đẹp hay sự lạ là bản năng sinh tồn. Khi bạn dùng ý chí ép "chức năng điều hành" của vỏ não phải kéo phanh khẩn cấp để đàn áp bản năng, hệ thần kinh tiêu tốn một lượng năng lượng khổng lồ. Sự kìm nén khiên cưỡng và kiệt quệ này mới là thứ bòn rút sinh lực tàn bạo nhất, chứ không phải một cái nhìn lướt qua.</p>
<blockquote>
<p><em>Càng ngăn ánh mắt đong đưa,<br/>Tâm can càng cạn như mưa giữa trời.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q14" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 3: Thứ ma lực hắc ám nào thao túng cơ thể bạn, khiến bạn lập tức mệt lả và bực bội lây chỉ vì vô tình chạm phải khuôn mặt cau có của một kẻ xa lạ chẳng hề quen biết?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong> Chẳng có ma lực nào cả, đó là sự phản bội của "Tế bào thần kinh gương". Bản năng ép não bạn tự động sao chép, mô phỏng lại trạng thái tiêu cực của đối phương để đánh giá rủi ro. Bạn bất đắc dĩ bị ép uống một liều thuốc độc cảm xúc ngoại lai. Sau đó, não lại phải trầy trật vắt kiệt sức lực để tự dọn dẹp đống rác tâm lý ấy nhằm lấy lại thăng bằng.</p>
<blockquote>
<p><em>Tế bào sao chép niềm đau,<br/>Rước luôn bực dọc nát nhàu tâm can.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q15" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 4: Việc bạn hùng hục dùng "sức mạnh ý chí" để đối đầu với tiếng ồn và ánh mắt bủa vây xuẩn ngốc tới mức nào, trong khi bạn hoàn toàn có thể "bẻ khóa" hệ thần kinh chỉ bằng công cụ vật lý?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong> Ý chí là tài nguyên cực kỳ đắt đỏ và dễ cạn! Thay vì vắt kiệt bộ não để chịu đựng, hãy dùng "boong-ke vật lý". Kính râm lập tức tắt áp lực giao tiếp ánh mắt. Tai nghe phong tỏa gọn gàng tạp âm. Cộng thêm hơi thở sâu để giật phanh khẩn cấp hạ nhịp tim. Ngắt kết nối đầu vào thụ động luôn thực dụng và sắc bén hơn vạn lần mọi nỗ lực gồng gánh tâm lý!</p>
<blockquote>
<p><em>Kính râm che khuất ánh nhìn,<br/>Tai nghe chặn tiếng giữ mình bình yên.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q16" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 5: Khi não bộ đang bốc cháy vì rò rỉ năng lượng, việc bạn ngồi lải nhải tự nhủ "phải dừng tiến trình xao nhãng này lại" sẽ đẩy bạn xuống vũng lầy nào, và đâu là "cú tát vật lý" để tỉnh giấc?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong> Tự nhắc nhở bản thân chỉ là đổ thêm dầu vào lửa (hiệu ứng gấu trắng). Càng cấm, não càng ám ảnh và khao khát quét tìm! Cú tát tỉnh thức là kỹ thuật "Bám rễ". Hãy ném cho não một mục tiêu vô tri: đếm 5 thứ mắt thấy, 4 thứ da chạm, hoặc dồn toàn tâm trí vào gót chân chạm đất. Thao tác đếm cơ học này tước đoạt tức thì quyền kiểm soát của trung tâm sợ hãi, giật bạn về thực tại an toàn.</p>
<blockquote>
<p><em>Đếm từng sự vật quanh mình,<br/>Bước chân chạm đất bóng hình lùi xa.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q17" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 6: Thói quen tự sỉ vả bản thân là "nhạy cảm, kém cỏi" mỗi khi lỡ xao nhãng ngoại cảnh đang bức tử hệ thần kinh của bạn ra sao, và đâu là cảnh giới tối thượng để khóa chặt van rò rỉ năng lượng?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong> Tự trách móc là đòn trừng phạt tàn nhẫn nhất giáng vào hệ thần kinh vốn đã kiệt quệ! Sự xao nhãng, quét tìm tín hiệu lạ là di sản cảnh báo được lập trình để sinh tồn hàng triệu năm, tuyệt đối không phải lỗi của bạn. Khi lỡ chú ý, hãy ngừng kiểm duyệt. Chỉ cần nhún vai: <em>"À, não mình vừa bật chế độ quét tự động"</em>, rồi thong dong bước tiếp. Chấp nhận tuyệt đối, không phán xét chính là chiếc khiên kim cương bất hoại!</p>
<blockquote>
<p><em>Bản năng tạo hóa muôn đời,<br/>Mỉm cười ghi nhận thảnh thơi cõi lòng.</em></p>
</blockquote>
</div>
</div>
"""
content = content.replace('<p><em>(Hệ thống đã mã hóa 11 rãnh', qa_content + '\n<p><em>(Hệ thống đã mã hóa 11 rãnh')

with open('logic08.html', 'w', encoding='utf-8') as f:
    f.write(content)

