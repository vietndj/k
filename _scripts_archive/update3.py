import re

with open('logic08.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Thêm TOC
toc_insertion = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">CHIẾN LƯỢC BÁN HÀNG</li>
<li><a class="ink-toc-link" href="#q23">Q1. Tử huyệt Video Dài</a></li>
<li><a class="ink-toc-link" href="#q24">Q2. Nghịch lý Facebook</a></li>
<li><a class="ink-toc-link" href="#q25">Q3. Ngụy biện tay trắng</a></li>
<li><a class="ink-toc-link" href="#q26">Q4. Cú lừa nút Like</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 2. Thêm Nội dung
qa_content = """
<hr style="margin: 4rem 0; border: none; border-top: 4px solid var(--ink-text);"/>
<h1 class="is-short">XƯƠNG SỐNG CHIẾN LƯỢC: CỖ MÁY BÁN HÀNG</h1>
<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q23" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 1: TỬ HUYỆT CỦA VIDEO DÀI<br>Ai cũng bảo làm video dài để chốt sale, nhưng 99% khách văng ra ngay phút đầu tiên. Cơ chế thao túng tâm lý nào có thể ép một người lạ dán mắt nghe bạn thuyết giáo suốt 30 phút mà vẫn tự nguyện rút ví?</h2>
<div class="dialogue-response">
<p><strong>🔥 Đập tan lầm tưởng:</strong><br>Não bộ người lạ luôn bật khiên phòng vệ sinh tồn: <em>"Lại lùa gà à?"</em>. Nếu mở đầu bằng việc lê thê dạy dỗ, bạn rớt đài ngay lập tức. Để bẻ khóa, bạn bắt buộc phải dùng phác đồ 3P tuyến tính:</p>
<ol>
<li><strong>Proof (Bằng chứng):</strong> Đập ngay kết quả thật vào 15s đầu để phá nát hoài nghi, "mua" lấy 10 phút tò mò.</li>
<li><strong>Principle (Nguyên lý):</strong> Tranh thủ lúc họ đang nể phục, đúc kết tư duy bẻ gãy sai lầm cũ, cấy quyền uy chuyên gia vào tiềm thức để gom đủ 7 giờ lòng tin.</li>
<li><strong>Process (Quy trình):</strong> Trải sẵn tấm bản đồ thực thi, triệt tiêu sự lười biếng và rủi ro. Tâm lý an toàn, họ tự động quẹt thẻ. Đảo lộn thứ tự này, cỗ máy tự gãy vụn!</li>
</ol>
<blockquote>
<p><em>Dùng bằng chứng phá hoài nghi,<br/>Khai thông nguyên lý, thực thi dọn đường.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q24" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 2: NGHỊCH LÝ NỀN TẢNG FACEBOOK<br>Nếu cỗ máy 3P thần thánh đến vậy, thì mang khối video 30 phút nặng đô đó ném thẳng lên bảng tin (Newsfeed) Facebook là nước cờ đột phá hay một vụ tự sát đẫm máu?</h2>
<div class="dialogue-response">
<p><strong>🔥 Đập tan lầm tưởng:</strong><br>Đó là tự sát thuật toán! DNA của Facebook là nền tảng ngắt quãng. Khách lướt Feed vô thức để săn Dopamine giải trí, không ai có tâm thế tĩnh tại để "đi học". Ép tệp khách lạnh (người lạ) xem video dài, tỷ lệ thoát chọc đáy, AI sẽ bóp nghẹt kênh.<br>Đòn bẩy ở đây là: Dùng video ngắn bọc "bằng chứng giật gân" quăng ra diện rộng để cào traffic. Giấu video dài làm "lưới đáy phễu" (để ở link ghim hoặc Inbox). Kẻ nào chủ động vượt rào cản chui vào xem, đó mới là tệp khách vàng đã sẵn sàng chốt đơn!</p>
<blockquote>
<p><em>Ngắn tung mồi nhử vòng ngoài,<br/>Dài ghim đáy phễu, rụng hoài tiền to.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q25" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 3: LỜI NGỤY BIỆN CỦA KẺ TAY TRẮNG<br>"Bằng chứng" là lưỡi dao đoạt mạng nhất, nhưng lính mới chưa có khách thì lấy gì để khoe? Phải chăng giải pháp khôn ngoan lúc này là lùi về làm video ngắn nhảy múa chờ thời?</h2>
<div class="dialogue-response">
<p><strong>🔥 Đập tan lầm tưởng:</strong><br>Lùi về vùng an toàn là bạn tự tay đào mồ chôn định vị! Khách lướt qua bạn 30 giây sẽ mặc định bạn chỉ là kẻ bán hàng vặt vãnh. Không ai dám giao số tiền vĩ đại (High-ticket) cho bạn.<br>Không có khách? Hãy "hack" bằng chứng! Dùng <strong>Bằng chứng vay mượn</strong> (đem chiến dịch của các thương hiệu lớn ra mổ xẻ) hoặc <strong>Bằng chứng thực chứng</strong> (thao tác trực tiếp sửa lỗi/giải quyết vấn đề, không cắt ghép). Khi bạn đủ trình độ bắt bệnh người khổng lồ, khách hàng sẽ tự khắc rợn ngợp và trao quyền!</p>
<blockquote>
<p><em>Tay không mượn thế khổng lồ,<br/>Phơi bày trí tuệ, cơ đồ nảy sinh.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q26" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 4: SỰ LỪA DỐI VĨ ĐẠI CỦA NÚT "LIKE"<br>Cày cuốc ngày đêm săn ngàn like, triệu view nhưng tài khoản vẫn rỗng tuếch. Cú lừa chí mạng của đám đông ồn ào trên mạng xã hội là gì?</h2>
<div class="dialogue-response">
<p><strong>🔥 Đập tan lầm tưởng:</strong><br>Là ảo tưởng ngây thơ: <em>"Tương tác bề nổi đẻ ra tiền"</em>. Thực tế, 1% đám đông cào phím thích bắt bẻ lại thường rỗng túi. Trái lại, 90% khách VIP mua hàng giá cao luôn ở chế độ "tàng hình". Họ soi xét khắt khe nhưng tuyệt đối im lặng. Ở kỷ nguyên Web Ngữ nghĩa (Semantic Web), thuật toán tự thấu hiểu độ sâu chuyên môn và bê thẳng video của bạn ném vào mặt 3.000 người đang thật sự khát khao giải pháp. Đừng hạ mình diễn trò mua vui, hãy tập trung dọn đường đón khách VIP!</p>
<blockquote>
<p><em>Đừng tham bão mạng ồn ào,<br/>Người mua tĩnh lặng, bước vào chốt đơn.</em></p>
</blockquote>
</div>
</div>
"""

content = content.replace('<p><em>(Hệ thống đã mã hóa 11 rãnh', qa_content + '\n<p><em>(Hệ thống đã mã hóa 11 rãnh')

with open('logic08.html', 'w', encoding='utf-8') as f:
    f.write(content)

