import re

# Read logic05.html
with open('/Users/vietmac/Documents/CODE/k/logic05.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header up to ink-toc-list
head_end = html.find('<ul class="ink-toc-list">')
header_part = html[:head_end + len('<ul class="ink-toc-list">\n')]

# Generate new TOC
toc_content = """<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 1: TÓM TẮT HÀNH TRÌNH</li>
<li><a class="ink-toc-link" href="#p1_q1">1. Truy vấn Nghịch lý Quyền lực</a></li>
<li><a class="ink-toc-link" href="#p1_q2">2. Truy vấn Tính Đại chúng</a></li>
<li><a class="ink-toc-link" href="#p1_q3">3. Truy vấn Cơ chế Thấu hiểu ảo</a></li>
<li><a class="ink-toc-link" href="#p1_q4">4. Truy vấn "Cú lừa Vay mượn"</a></li>
<li><a class="ink-toc-link" href="#p1_q5">5. Truy vấn bằng Đời thực</a></li>
<li><a class="ink-toc-link" href="#p1_q6">6. Truy vấn Lột mặt nạ Marketing</a></li>
<li><a class="ink-toc-link" href="#p1_q7">7. Truy vấn Lõi "Rác Tâm Lý"</a></li>
<li><a class="ink-toc-link" href="#p1_q8">8. Truy vấn Vỏ bọc Lấp liếm</a></li>
<li><a class="ink-toc-link" href="#p1_q9">9. Truy vấn Thực chiến Kênh</a></li>
<li><a class="ink-toc-link" href="#p1_q10">10. Truy vấn Tối hậu</a></li>

<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 2: BỘ HỎI ĐÁP SẮC BÉN</li>
<li><a class="ink-toc-link" href="#p2_q1">Q1. Nghịch lý quyền lực thao túng</a></li>
<li><a class="ink-toc-link" href="#p2_q2">Q2. Chi tiết cá nhân vô lý</a></li>
<li><a class="ink-toc-link" href="#p2_q3">Q3. Vụ buôn lậu cảm xúc</a></li>
<li><a class="ink-toc-link" href="#p2_q4">Q4. Tiếng ồn che tiếng rắm</a></li>
<li><a class="ink-toc-link" href="#p2_q5">Q5. Bản chất Storytelling</a></li>
<li><a class="ink-toc-link" href="#p2_q6">Q6. Vung dao 15 giây đầu tiên</a></li>
<li><a class="ink-toc-link" href="#p2_q7">Q7. Bản chất tàn khốc của đám đông</a></li>
"""

# Extract between TOC end and article start
article_start = html.find('<div class="ink-meta">')
middle_part = """</ul>
</aside>

<!-- MAIN CONTENT -->
<main class="ink-main-wrapper">
<article class="ink-content ink-mode-dialogue">
<div class="ink-meta">
<span class="ink-badge">BÁCH KHOA TOÀN THƯ</span>
<span>Nguyễn Việt</span>
<span>•</span>
<span>Thực chiến</span>
</div>
"""

# Generate main content
main_content = """
<!-- PHẦN 1 -->
<h1 class="is-short" id="top">PHẦN 1: HỆ THỐNG HÓA TÓM TẮT HÀNH TRÌNH ĐẶT CÂU HỎI CỦA BẠN</h1>
<p><em>(Trước khi giáng búa đập tan lầm tưởng, đây là bức tranh toàn cảnh về quỹ đạo tư duy sắc bén mà bạn đã truy vấn tôi từ đầu đến giờ):</em></p>
<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<ul style="list-style-type: none; padding-left: 0;">
  <li id="p1_q1" style="margin-bottom: 16px;"><strong>1. Truy vấn Nghịch lý Quyền lực:</strong> Tại sao bêu cái nhục của mình ra một cách lạnh tanh lại không thảm hại, mà sinh ra đỉnh cao quyền lực thao túng? (Phân tích cơ chế What - Why - How).</li>
  <li id="p1_q2" style="margin-bottom: 16px;"><strong>2. Truy vấn Tính Đại chúng:</strong> Từ 2 bài hát của Adele & Taylor Swift, tại sao tiểu tiết vụn vặt, cá nhân đến vô lý lại chạm đến hàng tỷ người? Áp dụng logic đó vào ngách quay dựng thế nào?</li>
  <li id="p1_q3" style="margin-bottom: 16px;"><strong>3. Truy vấn Cơ chế Thấu hiểu ảo:</strong> Tôi không hề gặp mặt hay an ủi khán giả, tại sao việc tôi tự chửi TÔI lại khiến HỌ khóc vì cảm thấy "được thấu hiểu"?</li>
  <li id="p1_q4" style="margin-bottom: 16px;"><strong>4. Truy vấn "Cú lừa Vay mượn":</strong> Thuật ngữ "Vay mượn để thương mình" bản chất là gì? Giải thích qua cơ chế Vật lý cộng hưởng và Công nghệ VPN.</li>
  <li id="p1_q5" style="margin-bottom: 16px;"><strong>5. Truy vấn bằng Đời thực:</strong> Cơ chế não bộ "tráo đổi dữ liệu" nghe quá khoa học viễn tưởng. Hãy chứng minh nó tự động xảy ra bằng các hiện tượng đời thường (Ăn chanh, Hát Karaoke).</li>
  <li id="p1_q6" style="margin-bottom: 16px;"><strong>6. Truy vấn Lột mặt nạ Marketing:</strong> Từ "Storytelling" (Kể chuyện) quá sáo rỗng mỹ miều. Hãy đổi nó thành 5 thuật ngữ dân dã, "vỉa hè", trần trụi nhất.</li>
  <li id="p1_q7" style="margin-bottom: 16px;"><strong>7. Truy vấn Lõi "Rác Tâm Lý":</strong> Rác thần kinh là gì? Tại sao người bình thường không tự dọn rác mà cứ phải mượn Creator làm "bao cát"? "Bất hòa nhận thức" là gì? (Dùng ví dụ tiếng ồn che tiếng rắm để trẻ con cũng hiểu).</li>
  <li id="p1_q8" style="margin-bottom: 16px;"><strong>8. Truy vấn Vỏ bọc Lấp liếm:</strong> Yêu cầu thêm các ví dụ đời thường (Thái hành tây, Hỏi ngu, Bỏ cuộc) để chứng minh con người luôn cần một "chứng cứ ngoại phạm".</li>
  <li id="p1_q9" style="margin-bottom: 16px;"><strong>9. Truy vấn Thực chiến Kênh:</strong> Yêu cầu lấy các tử huyệt (Sợ keo kiệt, Sợ lười, Sợ đố kỵ) lật ngược thành dạng Hỏi - Đáp bóc trần sự lươn lẹo của đám Newbie để viết Hook.</li>
  <li id="p1_q10" style="margin-bottom: 16px;"><strong>10. Truy vấn Tối hậu (Hiện tại):</strong> Tái cấu trúc toàn bộ cuộc hội thoại thành các câu Hỏi - Đáp mở gây shock, đập tan lầm tưởng, kết mỗi câu bằng 2 câu thơ Lục Bát check ngầm kỹ vần điệu.</li>
</ul>

<hr style="margin: 4rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 2 -->
<h1 class="is-short">PHẦN 2: BỘ HỎI ĐÁP SẮC BÉN - ĐẬP TAN MỌI LẦM TƯỞNG TÂM LÝ</h1>
<p>Dưới đây là bản "giải phẫu" toàn bộ hành trình tư duy của bạn, lột xác mọi lý thuyết dài dòng thành những nhát dao sắc lẹm nhất.</p>
<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p2_q1" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 1: Ai cũng nỗ lực xây dựng hình ảnh chuyên gia hoàn hảo để thị uy trên mạng. Nhưng tại sao sự hoàn hảo ấy lại biến bạn thành con mồi yếu ớt, còn việc tự lôi vết nhơ ê chề nhất của bản thân lên bàn mổ lại trao cho bạn quyền lực thao túng tối thượng?</h2>
<div class="dialogue-response">
<p><strong>🔪 ĐÁP BÉN:</strong> Vì sự hoàn hảo kích hoạt "radar phòng thủ" và thói sân si của đám đông. Sự thảm hại chỉ xảy ra khi bạn mếu máo mưu cầu thương hại. Khi bạn lạnh lùng tự phanh phui cái nhục của chính mình, bạn đã tước đoạt toàn bộ vũ khí phán xét của họ. Kẻ không che giấu khuyết điểm là kẻ bất khả xâm phạm.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Giấu dốt hoàn hảo người <strong>khinh</strong>, (khinh)</em><br/>
<em>Phơi trần vết sẹo, uy <strong>linh</strong> ngút ngàn. (linh)</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p2_q2" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 2: Giới chuyên gia luôn khuyên phải nói đạo lý vĩ mô, đại diện cho nhân loại để chạm đến số đông. Vậy tại sao hàng tỷ bộ não lại bị đâm xuyên chỉ vì một chi tiết cá nhân vô lý, tủn mủn như "chiếc khăn choàng cũ" hay "ánh đèn tủ lạnh"?</h2>
<div class="dialogue-response">
<p><strong>🔪 ĐÁP BÉN:</strong> Vì não bộ "mù" trước sự trừu tượng nhưng nhạy bén tột độ với kích thích vật lý. Đạo lý sáo rỗng chỉ trượt trên ý thức. Khi bạn ném ra một tiểu tiết trần trụi cực đoan, nó trở thành chiếc mỏ neo ép vô thức khán giả tự động lục lọi, tráo đổi và đắp đè vết thương của chính họ vào câu chuyện của bạn.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Đạo lý sáo rỗng mây <strong>trôi</strong>, (trôi)</em><br/>
<em>Chỉ bằng tiểu tiết, sục <strong>sôi</strong> cõi lòng. (sôi)</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p2_q3" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 3: Khi khán giả khóc lóc, bình luận "Thương anh quá, anh nói trúng tim đen em", có phải họ thực sự xót xa cho nỗi đau của bạn và hàm ơn vì bạn đã thấu hiểu họ?</h2>
<div class="dialogue-response">
<p><strong>🔪 ĐÁP BÉN:</strong> Hãy tỉnh mộng, khán giả vô cảm tuyệt đối với bạn! Xã hội cấm con người tự thương hại bản thân. Họ lén lút thực hiện một vụ "buôn lậu cảm xúc": Mượn câu chuyện bi đát của bạn làm tấm bình phong, để danh chính ngôn thuận rơi lệ cho sự thảm hại của CHÍNH HỌ mà không bị xã hội dị nghị.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Mượn người khóc lóc bi <strong>thương</strong>, (thương)</em><br/>
<em>Thực ra xả rác, dọn <strong>đường</strong> thân ta. (đường)</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p2_q4" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 4: Nếu ai cũng mang khối "rác" đố kỵ, dốt nát trong bụng, tại sao họ không tự đóng cửa phòng dọn dẹp tâm trí, mà phải chực chờ lướt trúng video bóc phốt bản thân của bạn mới xả được?</h2>
<div class="dialogue-response">
<p><strong>🔪 ĐÁP BÉN:</strong> Vì nỗi sợ "Bất hòa nhận thức". Sĩ diện (Ego) cài đặt niềm tin rằng họ cao thượng, tài giỏi. Tự nhìn vào cái dốt sẽ làm Ego sụp đổ, gây đau đớn tột cùng. Họ bắt buộc phải nín nhịn như đứa trẻ đau bụng, chờ một kẻ dũng cảm (là bạn) tạo ra "tiếng ồn" chịu báng, để họ lấp liếm xả cái "xì hơi" bế tắc của mình ra ngoài mà vỏ bọc đạo đức vẫn an toàn.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Cái Tôi sĩ diện giam <strong>cầm</strong>, (cầm)</em><br/>
<em>Chờ ai chịu nhục, âm <strong>thầm</strong> xả hơi. (thầm)</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p2_q5" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 5: Cụm từ "Kể chuyện chạm cảm xúc" (Storytelling) luôn được giới Marketing tung hô như một bộ môn nghệ thuật văn chương thiêng liêng. Lột bỏ lớp áo tẩy trắng đó, bản chất thực dụng giang hồ của nó là gì?</h2>
<div class="dialogue-response">
<p><strong>🔪 ĐÁP BÉN:</strong> Chẳng có nhà văn mộng mơ nào ở đây cả! Bản chất của nó thuần túy là 4 thủ đoạn thao túng điểm mù: Tự làm "bia đỡ đạn" chịu chửi, tiêm "thuốc mê" khóa mõm chó dữ sĩ diện, cấp "chứng cứ" ngoại phạm để khóc ké, và "chọc thủng bọc mủ" bắt quả tang những tật xấu lén lút. Bạn là kỹ sư tâm lý, không phải thợ viết văn.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Văn chương kể lể xa <strong>xôi</strong>, (xôi)</em><br/>
<em>Thực ra thao túng, đánh <strong>mồi</strong> tâm can. (mồi)</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p2_q6" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 6: Đám Newbie làm kênh đầy rẫy sự xót tiền, lười biếng và ghen ăn tức ở. Nếu khuyên răn bằng lòng tốt "hãy cố lên, đừng đố kỵ" là tự sát, thì phải vung nhát dao nào ở 15 giây đầu tiên (Hook) để ép họ quy phục?</h2>
<div class="dialogue-response">
<p><strong>🔪 ĐÁP BÉN:</strong> Khuyên răn trực diện là chĩa dao vào lòng tự ái, khán giả sẽ đóng sập tâm trí. Hãy tự thú nhận: "Tao từng lười biếng, từng ghen tị hộc máu đi report kênh đối thủ". Khi bạn tự đạp đổ đạo đức của mình, Ego của họ lập tức bị gây mê. Họ sẽ ùa vào thú tội xả rác, và ngoan ngoãn nuốt trọn mọi giải pháp kỹ thuật bạn gài cắm phía sau.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Dạy đời rước lấy oán <strong>than</strong>, (than)</em><br/>
<em>Nhận ngu chịu nhục, muôn <strong>ngàn</strong> người theo. (ngàn)</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p2_q7" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ CÂU HỎI 7: Từ việc mượn mùi củ hành tây để khóc, mượn cớ hùa theo hỏi ngu, hay mượn cái miệng độc địa của đồng nghiệp để chửi hùa... Sự thanh cao của đám đông thực chất che đậy bản chất tàn khốc nào?</h2>
<div class="dialogue-response">
<p><strong>🔪 ĐÁP BÉN:</strong> Sự thanh cao chỉ là màn kịch đạo đức giả! Đám đông luôn thèm khát xả rác nhưng lại nhát cáy sợ phán xét. Họ lươn lẹo, chực chờ một "Vật tế thần" mở đường để hợp thức hóa thói xấu của mình. Không có kẻ dũng cảm đóng vai ác, vai nghèo, vai dốt làm mồi nhử, sự bẩn tính của đám đông sẽ vĩnh viễn thối rữa trong nhà tù sĩ diện.</p>
<blockquote>
<p><strong>📜 Đúc kết Lục bát:</strong><br/>
<em>Miệng thì đạo lý thanh <strong>cao</strong>, (cao)</em><br/>
<em>Mượn người làm cớ, tuôn <strong>trào</strong> rác tâm. (trào)</em></p>
</blockquote>
</div>
</div>
"""

# Footer part
footer_part = """
</article>
</main>
</body>
</html>
"""

# Write to logic12.html
with open('/Users/vietmac/Documents/CODE/k/logic12.html', 'w', encoding='utf-8') as f:
    f.write(header_part + toc_content + middle_part + main_content + footer_part)

print("Done creating logic12.html")
