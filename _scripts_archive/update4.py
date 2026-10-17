import re

with open('logic08.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Thêm TOC
toc_insertion = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">NGHỊCH LÝ GIẤU BÀI</li>
<li><a class="ink-toc-link" href="#q_meta">1. Bài toán cốt lõi</a></li>
<li><a class="ink-toc-link" href="#q27">Q1. Ảo giác Kính VR</a></li>
<li><a class="ink-toc-link" href="#q28">Q2. Góc nhìn Thuật toán</a></li>
<li><a class="ink-toc-link" href="#q29">Q3. Góc nhìn Năng lượng</a></li>
<li><a class="ink-toc-link" href="#q30">Q4. Góc nhìn Game</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 2. Thêm Nội dung
qa_content = """
<hr style="margin: 4rem 0; border: none; border-top: 4px solid var(--ink-text);"/>
<h1 class="is-short" id="q_meta">GIẢI MÃ NGHỊCH LÝ "GIẤU BÀI" TRONG ĐÀO TẠO</h1>
<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>

<div style="margin-bottom: 3rem;">
    <h3 style="font-family: var(--font-display-short); font-weight: 600; font-size: 1.25rem;">CÂU LỆNH TỔNG HỢP (META-PROMPT)</h3>
    <blockquote style="font-size: 1.1rem; line-height: 1.7; background: #f8fafc; border-radius: 8px; padding: 1.5rem; margin: 1.5rem 0;">
    <p style="margin-bottom: 0;"><em>"Hãy đóng vai một chuyên gia phân tích chiến lược nội dung thực chiến. Nhiệm vụ của bạn gồm 2 phần:<br>
    1. Hệ thống hóa lại câu hỏi gốc đang lộn xộn của người dùng thành một 'Bài toán cốt lõi' thật rõ ràng, mạch lạc, nêu bật được sự mâu thuẫn giữa tư duy cũ và góc nhìn mới.<br>
    2. Phân tích và trả lời bài toán đó bằng định dạng 'Hỏi Xoáy - Đáp Sắc', đập tan lầm tưởng về việc 'giấu bài' trong kinh doanh thông tin. Phân tích chi tiết qua 4 góc độ: Phân loại What-Why-How, Nghịch lý Thuật toán, Góc nhìn Năng lượng, và Góc nhìn Game (Lý thuyết trò chơi). Mỗi câu trả lời phải sắc bén, đi thẳng vào bản chất và bắt buộc kết thúc bằng 2 câu thơ Lục Bát được kiểm tra ngầm chuẩn xác về niêm luật (Bằng - Trắc và Gieo vần)."</em></p>
    </blockquote>
    
    <h3 style="font-family: var(--font-display-short); font-weight: 600; font-size: 1.25rem; margin-top: 2rem;">1. HỆ THỐNG LẠI BÀI TOÁN GỐC CỦA BẠN</h3>
    <p><strong>Bối cảnh mâu thuẫn:</strong><br>
    Giới đào tạo truyền tai nhau tư duy cũ: <em>"Chỉ cho tư tưởng (What/Why), giấu đi bí quyết thực hành (How)"</em>. Lý do là sợ khách hàng bị "Kính VR" (quá tải thông tin) – xem xong cách làm chi tiết sẽ sinh ra ảo giác no nê, không thèm mua khóa học chuyên sâu.</p>
    
    <p><strong>Góc nhìn phản biện của bạn (Ngành dạy xây kênh/làm video):</strong><br>
    Bạn thấy tư duy trên hoàn toàn sai lệch và vô tác dụng trong hiện tại. Lập luận của bạn là:</p>
    <ul style="margin-bottom: 1.5rem;">
    <li>Thuật toán AI hiện nay đã tự hiểu nội dung để phân bổ đúng tệp.</li>
    <li>Để AI phân phối được, bắt buộc phải làm nội dung chất lượng, hướng dẫn cực kỳ đầy đủ, chi tiết nhưng thật ngắn gọn.</li>
    <li>Bản thân định dạng video ngắn đã là một màng lọc vật lý (không thể nói hết mọi thứ vĩ mô), nên không cần cố tình "phân loại, giấu diếm hay kiêng kỵ không được nói cái này cái kia". Chính cái sự "dạy hết mình" đó mới là phễu dẫn khách hàng đến các lớp học Offline.</li>
    </ul>
    
    <p><strong>Yêu cầu cốt lõi:</strong><br>
    Xác nhận xem trực giác của bạn đúng hay sai? Giải mã cặn kẽ cơ chế của câu nói cũ (What - Why - How) và dùng <strong>Góc nhìn Năng lượng</strong> cùng <strong>Góc nhìn Game</strong> để chứng minh sự ưu việt trong tư duy thực chiến hiện tại của bạn.</p>

    <h3 style="font-family: var(--font-display-short); font-weight: 600; font-size: 1.25rem; margin-top: 2.5rem;">2. GIẢI PHẪU LẦM TƯỞNG & ĐẬP TAN TƯ DUY CŨ (HỎI XOÁY - ĐÁP SẮC)</h3>
    <p>Trực giác của bạn hoàn toàn chính xác. Tư duy "giấu bài" là tàn dư thiu thối của kỷ nguyên bán khóa học đời đầu. Cách bạn đang vận hành nội dung mới chính là nhịp thở thực chiến của một Master.<br>
    Dưới đây là màn giải phẫu chi tiết:</p>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q27" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 1: Nghịch lý What/Why/How & Ảo giác "Kính VR"<br>Phải chăng cứ khơi gợi nỗi đau (Why), vẽ ra chân trời (What) rồi giấu nhẹm công cụ (How) sau bức tường thu phí thì khách hàng sẽ khao khát điên cuồng? Hay đó chỉ là cái bẫy của những kẻ dạy lý thuyết suông, lo sợ phô ra sẽ lộ bản chất nông cạn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP SẮC:</strong><br>
Khán giả ngày nay cực kỳ thực dụng, đạo lý suông không làm họ mở ví. Bản chất của một video 60 giây dẫu có dốc hết ruột gan cũng chỉ chứa nổi một <strong>"Micro-How"</strong> (kỹ năng siêu nhỏ: ví dụ set một cây đèn góc 45 độ, hay cắt một nhịp thở thừa). Khán giả không bao giờ "no nê" với một mảnh ghép!<br>
Khi bạn trao đi một "How-to" bén ngót, họ áp dụng và thấy kênh tăng view ngay (Quick-wins). Chính cái chiến thắng thật đó đập tan "Kính VR", biến họ thành kẻ nghiện kỹ năng của bạn. Phân loại rạch ròi What/Why/How để giấu bài là tự sát, dâng khách hàng cho bên đối thủ chịu chia sẻ.</p>
<blockquote>
<p><em>Giấu nghề cứ ngỡ là hay,<br/>Ngờ đâu khách vuốt qua tay kẻ ngoài.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q28" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 2: Góc nhìn Thuật toán - Đấu với AI bằng tay không?<br>Nếu cất hết bí quyết thực chiến ở nhà, bạn định dùng thứ nội dung úp mở lấp lửng nào để "hối lộ" thuật toán AI, ép nó nhận diện bạn là chuyên gia và bơm traffic đúng tệp?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP SẮC:</strong><br>
AI không có cảm xúc, thức ăn của nó là <strong>Tỷ lệ giữ chân (Retention)</strong> và <strong>Lượt lưu/chia sẻ (Save/Share)</strong>. Chẳng ai rảnh bấm "Lưu" một video chỉ nói vòng vo. Họ chỉ lưu những hướng dẫn đầy đủ, ngắn gọn, súc tích để dành thực hành. Hướng dẫn chi tiết chính là mồi nhử AI mạnh nhất. Bạn dốc lòng hướng dẫn, AI lập tức phân bổ video của bạn đến tận tay những người đang khao khát học làm video. Cố tình giấu đi = Không ai Lưu = Kênh tắt thở!</p>
<blockquote>
<p><em>Thuật AI chẳng thích mập mờ,<br/>Trao đi thực chiến, bến bờ vinh quang.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q29" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 3: Góc nhìn Năng lượng - Sát khí của sự toan tính<br>Tại sao những video rào trước đón sau, thả thính mồi chài lại toát ra thứ "tà khí" khiến người xem xù lông phòng thủ? Trong khi kẻ dốc cạn ruột gan cho đi miễn phí lại tạo ra một trường năng lượng hút khách hàng tự nguyện mang tiền đến nộp?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP SẮC:</strong><br>
Giao tiếp mạng xã hội là sự va chạm về tần số! Giấu bài phát ra năng lượng của sự sợ hãi, vụ lợi và khan hiếm. Khán giả ngửi thấy mùi "lùa gà" ngay lập tức và đóng sập tâm trí.<br>
Ngược lại, bạn hướng dẫn tận tình, ngắn gọn toát ra uy quyền của một Master dư dả kiến thức. Khi họ dùng mẹo của bạn và có kết quả, não họ sinh ra một khoản <strong>"Nợ ân tình" (Karmic Debt)</strong>. Bình chứa năng lượng biết ơn càng đầy, nó càng thôi thúc họ phải tìm đến bạn để trả nợ. Bạn càng vô tư cho đi, tiền càng đuổi theo bạn.</p>
<blockquote>
<p><em>Tính toan mang dáng bần cùng,<br/>Cho đi trù phú, muôn trùng người theo.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q30" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 4: Góc nhìn Game (Lý thuyết trò chơi)<br>Nếu mọi ngón nghề cắt dựng, kịch bản đều bị bạn bóc trần trên video ngắn, vậy hàng chục con người xì tiền đến các workshop Offline 2 ngày của bạn là để mua cái gì? Mua lại dăm ba cú click chuột miễn phí chăng?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP SẮC:</strong><br>
Thứ miễn phí trên mạng chỉ là chiếc rìu gỗ phát cho "Tân thủ" ở khu vực hướng dẫn (Tutorial). Họ chém vài con quái nhỏ, thấy sướng, và nhận ra bạn là Game Master xịn nhất.<br>
Nhưng khi kẹt map, cạn ý tưởng, họ buộc phải nâng cấp. Họ đến lớp Offline không phải học click chuột. Họ đến mua <strong>"Cheat Code"</strong> (Hệ thống vĩ mô như 3 Tầng Sự Thật, 4 Tầng Nhận Thức), mua <strong>"Bang hội"</strong> (Môi trường ép kỷ luật), và đắt giá nhất: Mua <strong>Đặc quyền Feedback 1-1</strong>. Họ cần Game Master tận tay soi kênh, bẻ gãy tư duy cũ và kê đơn riêng cho họ. Nội dung ngắn là mồi nhử, lớp Offline là sự lột xác toàn diện.</p>
<blockquote>
<p><em>Mạng ngoài dắt dẫn tân binh,<br/>Vào trong thực chiến, sửa mình vươn xa.</em></p>
</blockquote>
</div>
</div>
"""

content = content.replace('<p><em>(Hệ thống đã mã hóa 11 rãnh', qa_content + '\n<p><em>(Hệ thống đã mã hóa 11 rãnh')

with open('logic08.html', 'w', encoding='utf-8') as f:
    f.write(content)

