import re

file_path = '/Users/vietmac/Documents/CODE/k/logic10.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_toc_items = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">GIÁ CẢ & CỘNG ĐỒNG</li>
<li><a class="ink-toc-link" href="#q77">1. Sự vô ơn của giá rẻ</a></li>
<li><a class="ink-toc-link" href="#q78">2. Liều thuốc đắng giá cao</a></li>
<li><a class="ink-toc-link" href="#q79">3. Ông chủ Hộp đêm</a></li>
<li><a class="ink-toc-link" href="#q80">4. Tước đoạt môi trường sống</a></li>
<li><a class="ink-toc-link" href="#q81">5. Nhát dao trì hoãn</a></li>
"""

toc_marker = "</ul>\n</aside>"
if toc_marker in content:
    content = content.replace(toc_marker, new_toc_items + "\n" + toc_marker)

new_content = """
<hr style="margin: 4rem 0; border: none; border-top: 1px solid var(--ink-border);"/>
<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase;">PHẦN 8: HỆ THỐNG TRỤC CÂU HỎI & ĐẬP TAN ẢO TƯỞNG VỀ GIÁ CẢ VÀ CỘNG ĐỒNG</h2>
<p>Dưới đây là màn tái cấu trúc toàn bộ luồng tư duy của chúng ta, được thiết kế như một <strong>"Liều thuốc sốc phản vệ"</strong> dội thẳng vào tiềm thức để đập tan mọi lầm tưởng, sự bao biện và nỗi sợ hãi của bạn.</p>
<p><em>(Trước khi cầm dao phẫu thuật, đây là bức tranh toàn cảnh về những giằng xé nội tâm mà bạn đã đặt ra)</em></p>
<ul>
    <li><strong>Về lầm tưởng "Định Giá":</strong>
        <ul>
            <li>Cơ chế (What, Why, How), logic và phân loại thực sự đằng sau việc định giá sản phẩm là gì?</li>
            <li>Tại sao bán giá rẻ lại luôn thu hút nhóm khách hàng lười biếng, hay phàn nàn, đổ lỗi và đám "Hater"? Điều này có phải là minh chứng cho nguyên lý tương đồng năng lượng không?</li>
            <li>Tại sao việc tăng giá cao lại hoạt động cực kỳ hiệu quả? Hãy phân tích sâu sắc từ góc nhìn năng lượng, tiến hóa, sinh học (ti thể) và lý thuyết trò chơi.</li>
            <li>Tôi vẫn sợ hãi chưa dám thay đổi suy nghĩ, hãy đưa ra 3 lý luận và ẩn dụ sắc bén nhất để đập tan nỗi sợ "bán ế" này.</li>
        </ul>
    </li>
    <li><strong>Về lầm tưởng "Hệ sinh thái & Cộng đồng":</strong>
        <ul>
            <li>Cộng đồng rốt cuộc sinh ra để làm gì? Có phải chỉ để lấy học viên làm minh họa cho video quảng cáo thôi không?</li>
            <li>Có phải tôi đang trốn tránh việc lập nhóm vì mắc kẹt trong nỗi sợ "phải chường mặt ra", sợ tốn thời gian hầu hạ?</li>
            <li>Tại sao việc "bán xong rồi thả học viên tự bơi" lại nguy hiểm? Hãy dùng lăng kính Tâm lý học tiến hóa, Sinh học (Ti thể), Kính thực tại ảo (VR) và Vật lý lượng tử để giải phẫu nó.</li>
        </ul>
    </li>
    <li><strong>Về lầm tưởng "Lý thuyết suông":</strong>
        <ul>
            <li>Chỉ nói logic thôi thì não tôi không chịu thay đổi đâu. Đâu là bước hành động tàn nhẫn và nhỏ nhất (Micro-step) để áp dụng ngay cho lớp offline, ép não tôi phải trực tiếp thẩm nghiệm và tin tưởng vào hệ thống này?</li>
        </ul>
    </li>
</ul>

<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase; margin-top: 4rem;">CHUỖI HỎI ĐÁP SỐC NHẬN THỨC - ĐẬP TAN ẢO TƯỞNG</h2>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q77" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 1: SỰ VÔ ƠN CỦA GIÁ RẺ<br>Bạn được lợi lộc gì khi nhân danh "lòng tốt" để bán giá rẻ, rồi tự biến bản thân thành "thùng rác cảm xúc" hứng chịu sự vô ơn của những kẻ thất bại?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bạn chẳng được gì ngoài sự kiệt quệ linh hồn. Giá rẻ đã triệt tiêu hoàn toàn "chi phí chìm", khách hàng mua không xót tiền nên não bộ lập trình sự ỷ lại. Khi lười biếng sinh ra thất bại, bản ngã (Ego) của họ kiên quyết từ chối nhận lỗi. Họ bắt buộc phải biến bạn thành "vật tế thần" để chửi rủa, ném đá. Sợ ế mà hạ giá, bạn đang phát ra tần số năng lượng "thiếu thốn", tự động biến thành nam châm hút trọn tệp khách hàng mang tư duy nạn nhân. Bán rẻ không phải là cứu người, đó là sự dung túng cho cái ác của sự yếu hèn.</p>
<blockquote>
<p><em>Bán buôn giá rẻ chuốc phiền, <br/>Rước bầy lười biếng, đảo điên tháng ngày. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q78" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 2: LIỀU THUỐC ĐẮNG GIÁ CAO<br>Nếu biết rằng việc "tước đoạt" 50 triệu của khách hàng là cách duy nhất để cứu rỗi sự trì trệ của họ, bạn có dám trở thành một "bác sĩ phẫu thuật" máu lạnh nhưng đạo đức không?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Phải dám! Mất một số tiền khổng lồ là đòn bẩy bạo lực nhất để can thiệp vào sinh học. Hạch hạnh nhân (Amygdala) réo còi báo động sinh tồn, ép cơ thể bơm Adrenaline và vắt kiệt Ti thể sản sinh năng lượng. Khách hàng bị cưỡng chế vào trạng thái "Mario đánh trùm" - tập trung điên cuồng, kỷ luật tuyệt đối để đòi lại vốn (Skin in the game). Cá mập có tiền luôn dùng "Giá cả" làm màng lọc "Chất lượng". Ép họ trả giá cắt cổ chính là liều thuốc đắng duy nhất ép ra kết quả.</p>
<blockquote>
<p><em>Giá cao thức tỉnh tế bào, <br/>Tiền to xót ruột, dâng trào tiến lên. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q79" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 3: ÔNG CHỦ HỘP ĐÊM<br>Ai đã tiêm nhiễm vào đầu bạn ảo tưởng ấu trĩ rằng xây dựng cộng đồng là phải làm "cô bảo mẫu" đi dọn rác, tốn thời gian hầu hạ từng học viên?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đó là sự bao biện của tư duy làm thuê. Kiến trúc sư sinh thái định vị mình là "Ông chủ Hộp Đêm". Việc của bạn là thiết lập một không gian tuyệt đẹp, ban hành luật thép, bật nhạc và... lên lầu VIP ngồi. Khách hàng bước vào sẽ tự nhảy múa, tự ganh đua và tự dạy nhau. Lợi ích tối thượng của cộng đồng là tóm gọn Giá trị vòng đời (LTV). Khi đám đông đang hưng phấn vì nhau, bạn nhàn nhã tung ra các sản phẩm giá cao (Upsell), họ sẽ tự chốt đơn mà bạn tốn đúng 0 đồng chi phí Marketing.</p>
<blockquote>
<p><em>Sân chơi thiết lập luật đây, <br/>Tự thân vận động, dựng xây cơ đồ. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q80" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 4: QUYỀN LỰC HỆ SINH THÁI<br>Bạn có nhận thức được việc "bán khóa học xong rồi thả khách tự bơi" là hành vi tước đoạt môi trường sống, vô tình đẩy họ vào cái chết của sự cô độc?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Sinh vật khi bị tách bầy sẽ lập tức hoảng sợ (não tiết Cortisol gây bỏ cuộc). Việc nhốt khách vào hệ sinh thái là hành động "đổ keo dán chặt chiếc kính VR" lên mắt họ, cách ly mọi cám dỗ từ đối thủ. Về mặt Lượng tử, bạn không cần hò hét lùa bò. Năng lượng của 5 cá nhân xuất sắc nhất trong nhóm sẽ tự động tạo "Hiệu ứng cộng hưởng", sinh ra áp lực bầy đàn (FOMO) cưỡng ép 45 kẻ lười nhác phải đồng bộ tần số. Đám đông tự truyền Dopamine cho nhau, ti thể sục sôi liên tục, còn bạn vĩnh viễn rảnh tay.</p>
<blockquote>
<p><em>Thả bơi khách sẽ bơ vơ, <br/>Giam vào sinh thái, tôn thờ chẳng buông. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q81" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 5: NHÁT DAO TRÌ HOÃN (Micro-step)<br>Vứt bỏ mọi mớ lý thuyết rườm rà đi, nhát dao "tàn nhẫn" nào bạn dám cắm xuống ngay ngày mai ở lớp Offline để ép não bộ nếm mùi Dopamine của sự nhàn hạ?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Sử dụng vũ khí "Trì hoãn can thiệp". Hãy lập ngay một nhóm kín và ghim luật: <em>"Ai giúp đồng đội giải quyết bài tập, thưởng ngay 15 phút Coaching riêng"</em>.<br>Khoảnh khắc quyết định: Ngày mai, khi có người kêu cứu trong nhóm, <strong>MỆNH LỆNH TỐI THƯỢNG CHO BẠN LÀ TẮT MÁY VÀ TUYỆT ĐỐI IM LẶNG 4 TIẾNG</strong>.<br>Lúc mở máy ra, bạn sẽ sốc nặng khi thấy học viên giỏi đã tự vào kèm cặp học viên yếu. Ngay lúc đó, não bạn tận mắt chứng kiến cỗ máy tự chạy. Sự thảnh thơi đó sẽ đập nát vĩnh viễn định kiến "sợ chường mặt" của bạn!</p>
<blockquote>
<p><em>Lùi chân im lặng mà xem, <br/>Học viên tự quản, anh em kết đoàn. </em></p>
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
