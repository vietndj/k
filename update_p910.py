import sys

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'r', encoding='utf-8') as f:
    content = f.read()

toc_insert = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 9: KIẾN TẠO HỆ ĐIỀU HÀNH XÂY KÊNH</li>
<li><a class="ink-toc-link" href="#p9_1">1. Triết lý Lõi</a></li>
<li><a class="ink-toc-link" href="#p9_2">2. Nghịch cảnh Kẹt ở giữa</a></li>
<li><a class="ink-toc-link" href="#p9_3">3. Chiến thuật Mượn lực</a></li>
<li><a class="ink-toc-link" href="#p9_4">4. Quyền lực Vi mô</a></li>
<li><a class="ink-toc-link" href="#p9_5">5. Thực chiến Đối chiếu</a></li>
<li><a class="ink-toc-link" href="#p9_6">6. Ngành Rủi ro cao</a></li>
<li><a class="ink-toc-link" href="#p9_7">7. Nghịch lý 7 Giờ</a></li>

<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 10: ĐẬP TAN LẦM TƯỞNG THỰC CHIẾN</li>
<li><a class="ink-toc-link" href="#p10_q37">Q37. Ốp lưng vs Tài sản</a></li>
<li><a class="ink-toc-link" href="#p10_q38">Q38. Mặt nạ Tầng 2.5</a></li>
<li><a class="ink-toc-link" href="#p10_q39">Q39. Trốn tránh quán cafe</a></li>
<li><a class="ink-toc-link" href="#p10_q40">Q40. Định luật Woodsmall</a></li>
<li><a class="ink-toc-link" href="#p10_q41">Q41. Vàng bọc nilon</a></li>
<li><a class="ink-toc-link" href="#p10_q42">Q42. Ngựa gỗ thành Troy</a></li>
<li><a class="ink-toc-link" href="#p10_q43">Q43. F-Boy vs Sát thủ</a></li>
<li><a class="ink-toc-link" href="#p10_q44">Q44. Đèn pin rọi rừng tối</a></li>
<li><a class="ink-toc-link" href="#p10_q45">Q45. BĐS ôm đất ngộp</a></li>
<li><a class="ink-toc-link" href="#p10_q46">Q46. Dân công sở giấu dốt</a></li>
<li><a class="ink-toc-link" href="#p10_q47">Q47. Mẹ bỉm kẹt khóa váy</a></li>
<li><a class="ink-toc-link" href="#p10_q48">Q48. Mầm non soi cam</a></li>
<li><a class="ink-toc-link" href="#p10_q49">Q49. Spa che mặt nám</a></li>
<li><a class="ink-toc-link" href="#p10_q50">Q50. Salon tóc rụng kẹt tay</a></li>
<li><a class="ink-toc-link" href="#p10_q51">Q51. Lạm phát ăn trộm</a></li>
<li><a class="ink-toc-link" href="#p10_q52">Q52. Viên thuốc bọc đường</a></li>
<li><a class="ink-toc-link" href="#p10_q53">Q53. Đài Radio tâm lý</a></li>
<li><a class="ink-toc-link" href="#p10_q54">Q54. Dopamine khai sáng</a></li>
"""

body_insert = """
<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 9 -->
<h1 class="is-short">PHẦN 9: KIẾN TẠO HỆ ĐIỀU HÀNH XÂY KÊNH (HỆ THỐNG HÓA)</h1>
<p><em>(Toàn bộ cuộc đại phẫu tư duy của bạn không phải là những câu hỏi rời rạc, mà là 7 chốt chặn cốt lõi để kiến tạo một hệ điều hành xây kênh độc quyền:)</em></p>

<ul>
    <li id="p9_1"><strong>1. Triết lý Lõi:</strong> Làm sao hệ thống hóa tư duy "Bán đồ rẻ cần view, Bán giá cao cần niềm tin" và "Thuyết bóc tách Tầng 2.5 (ngụy biện)" thành kim chỉ nam tối thượng?</li>
    <li id="p9_2"><strong>2. Nghịch cảnh Kẹt ở giữa:</strong> Người làm nghề offline lâu năm, không tiền chạy Ads, không giỏi công nghệ, sĩ diện cao không dám làm rạp xiếc thì luật chơi sinh tồn là gì?</li>
    <li id="p9_3"><strong>3. Chiến thuật Mượn lực:</strong> Cấm tấu hài nhảy múa thì "Trend định dạng" bản chất là gì? Xin 10 khung kịch bản sát thủ để cướp traffic đại chúng mà vẫn giữ áo vest uy quyền.</li>
    <li id="p9_4"><strong>4. Quyền lực của sự Vi mô:</strong> Dựa trên ẩn dụ "tán gái", giải thích cơ chế tâm lý: Tại sao miêu tả chi tiết lén lút lại đập tan rào cản phòng thủ, biến "hỗn độn" thành "rõ ràng" và ép khách phục tùng?</li>
    <li id="p9_5"><strong>5. Thực chiến Đối chiếu:</strong> Xin 3 ví dụ phân định ranh giới giữa Tay mơ (dùng tính từ sáo rỗng) và Sát thủ (dùng hành động vật lý) trong ngành BĐS, Tiếng Anh, Thời trang.</li>
    <li id="p9_6"><strong>6. Bóc tách Ngành Rủi ro cao:</strong> Áp dụng công thức lột mặt nạ Tầng 2.5 cho 3 dịch vụ Offline đòi hỏi niềm tin sinh tử: Mầm non xót con, Spa sợ hỏng mặt, Salon sợ cháy tóc.</li>
    <li id="p9_7"><strong>7. Nghịch lý 7 Giờ & Giải trí:</strong> Khước từ view rác (Drama, Gợi cảm), làm sao giữ chân khách VIP đủ 7 tiếng? Tại sao chiến thuật lồng Voiceover kiến thức vào vỏ bọc Template Video lại biến sự khô khan thành "giải trí nhận thức"?</li>
</ul>

<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 10 -->
<h1 class="is-short">PHẦN 10: HỎI ĐÁP ĐẬP TAN LẦM TƯỞNG - THỰC CHIẾN XÂY KÊNH</h1>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q37" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 37 [Bán ốp lưng 30k vs Tài sản giá cao]: Tại sao đâm đầu uốn éo đu triệu view lại là nhát dao tự sát thương hiệu?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> View rác hút kẻ bốc đồng. Khách VIP mua bằng sự tĩnh lặng và niềm tin vững chãi, không mua rạp xiếc.</p>
<blockquote>
<p><em>Múa may câu khách qua <strong>đường</strong>,</em><br/>
<em>Khách sang họ bỏ lẽ <strong>thường</strong> xưa nay.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q38" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 38 [Chiếc mặt nạ Tầng 2.5]: Vì sao đâm thẳng bế tắc thì khách chửi, khều nhẹ ngụy biện khách lại quỳ?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Lòng tự tôn của người lớn rất lớn. Lột mặt nạ không phán xét giúp bảo vệ sĩ diện, ép họ tự bỏ khiên.</p>
<blockquote>
<p><em>Đâm thẳng khách chửi quay <strong>xe</strong>,</em><br/>
<em>Gọi tên ngụy biện khách <strong>nghe</strong> rập đầu.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q39" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 39 [Mang máy tính ra quán cafe chạy deadline]: Ra quán đổi gió là tìm cảm hứng hay lớp vỏ bọc hoàn hảo của sự bế tắc?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Đổi gió là văn mẫu. Sự thật trần trụi là trốn tránh hiện thực, ngồi nhìn đá tan không gõ nổi một dòng.</p>
<blockquote>
<p><em>Lấy cớ ra quán đổi <strong>thay</strong>,</em><br/>
<em>Nhìn ly đá chảy lắt <strong>lay</strong> ưu phiền.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q40" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 40 [Định luật Woodsmall / Thợ sửa xe]: Khoe bằng cấp bị khinh, cớ sao đọc trúng bệnh vi mô lại hóa thần y?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Khi bạn gọi đúng triệu chứng rành rọt hơn cả bệnh nhân, họ mặc định bạn đang giấu sẵn thuốc giải.</p>
<blockquote>
<p><em>Bằng cấp khoe khoang ai <strong>nhìn</strong>,</em><br/>
<em>Bắt trúng bệnh ẩn khách <strong>xin</strong> nộp tiền.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q41" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 41 [Nhẫn vàng bọc túi nilon vs Hộp nhung]: Kiến thức uyên bác đến mấy vì sao vẫn bị lướt qua trong ba giây ngắn ngủi?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Não bộ lười biếng. Vàng bọc nilon (video ồn, mờ) tạo ma sát, cần hộp nhung hậu kỳ bôi trơn nhận thức.</p>
<blockquote>
<p><em>Nhẫn vàng bọc túi ni <strong>lông</strong>,</em><br/>
<em>Cũng đành vứt bỏ vì <strong>không</strong> mượt mà.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q42" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 42 [Con ngựa gỗ thành Troy / Trend Định dạng]: Cấm làm lố lăng, chuyên gia dùng thủ đoạn gì để cướp traffic thuật toán?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Mượn định dạng quen thuộc làm ngựa gỗ vô hại, giấu lưỡi dao chuyên môn vào bụng để đánh úp tâm lý.</p>
<blockquote>
<p><em>Múa may tấu hài vứt <strong>đi</strong>,</em><br/>
<em>Mượn khung định dạng quản <strong>gì</strong> đám đông.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q43" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 43 [Gã F-Boy lùa gà vs Sát thủ tán gái]: Nói "Tôi hiểu nỗi đau của bạn" sao lại rẻ mạt hơn tả chi tiết "cái cắn môi"?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Tính từ ai cũng copy được. Chi tiết vật lý lén lút là bằng chứng thép của kẻ từng nếm mật nằm gai.</p>
<blockquote>
<p><em>Văn mẫu sáo rỗng trên <strong>môi</strong>,</em><br/>
<em>Chi tiết lén lút cuốn <strong>trôi</strong> nghi ngờ.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q44" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 44 [Kẻ đi lạc & Người cầm đèn pin rọi rừng tối]: Khách đang hoảng loạn, sức mạnh thao túng của việc bóc tách hỗn độn là gì?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Khách lạc trong rừng mù mịt. Ai rọi đèn pin gọi tên vũng lầy, kẻ đó mặc nhiên trở thành minh chủ.</p>
<blockquote>
<p><em>Rừng đêm mù mịt hoang <strong>mang</strong>,</em><br/>
<em>Bật đèn chỉ lối khách <strong>sang</strong> gửi vàng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q45" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 45 [BĐS - Tắt điện thoại thở dài vs Gáy chờ x3]: Điểm yếu chí mạng của kẻ ôm đất ngộp sợ bị chuyên gia lột trần nhất là gì?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Nửa đêm lén check sổ đỏ thở dài, sáng ra quán cafe vắt chân vỗ đùi chém gió chờ nhân ba.</p>
<blockquote>
<p><em>Nửa đêm khóc lén thở <strong>dài</strong>,</em><br/>
<em>Sáng ra quán nước khoe <strong>tài</strong> chờ tăng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q46" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 46 [Tiếng Anh - Ướt chuột mạng lag vs Bận dự án]: Đâu là nhát dao xé toạc sự hèn nhát của dân công sở giấu dốt ngoại ngữ?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Khoảnh khắc toát mồ hôi gõ "mạng lag" khi sếp gọi, nhưng vênh váo chê ngữ pháp lặt vặt vì bận dự án.</p>
<blockquote>
<p><em>Chuột trơn ướt sũng mồ <strong>hôi</strong>,</em><br/>
<em>Mượn cớ bận việc để <strong>trôi</strong> lỗi lầm.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q47" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 47 [Thời trang - Hóp bụng kẹt khóa vs Chuộng Freesize năng động]: Lời dối trá chua xót nhất của mẹ bỉm bị lột trần bằng hành động nào?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Nhói lồng ngực kéo khóa không lên, đành tròng váy thụng rồi dối lòng mặc vậy cho dễ bế con.</p>
<blockquote>
<p><em>Bụng mỡ kéo khóa kẹt <strong>nửa</strong>,</em><br/>
<em>Dối lòng cho khỏe để <strong>chừa</strong> thị phi.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q48" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 48 [Mầm non - 5 phút zoom cam vs Cho đi sớm cho dạn]: Làm sao đâm trúng cảm giác tội lỗi của bà mẹ ném con cho người lạ?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Sáng dứt tay con khóc lóc, trưa lén soi cam liên tục, nhưng mạnh miệng bảo cho đi sớm để tự lập.</p>
<blockquote>
<p><em>Quay đi dứt bỏ tay <strong>con</strong>,</em><br/>
<em>Miệng hô tự lập lòng <strong>còn</strong> xót xa.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q49" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 49 [Spa - Chảy vệt vàng khẩu trang vs Thích đẹp thuận tự nhiên]: Lời ngụy biện "thích đẹp tự nhiên" giấu nhẹm nỗi nhục nhã nào chốn buồng the?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Là cảnh trát ba lớp kem che nám đến mốc mặt, mồ hôi vàng khè khẩu trang, chụp ảnh bóp mặt nát app.</p>
<blockquote>
<p><em>Mặt trát ba lớp kem <strong>dày</strong>,</em><br/>
<em>Miệng bảo tự nhiên đắp <strong>bày</strong> dối gian.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q50" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 50 [Salon Tóc - Vuốt rụng kẹt tay vs Kẹp càng cua cá tính]: Cuộn cục tóc hỏng giấu kẹp càng cua, chị em đang chôn vùi điều gì?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Chôn vùi nỗi xót xa vì ham rẻ gội tiệm cỏ tóc mủn rễ tre, phải dối lòng kẹp lên cho gọn gàng cá tính.</p>
<blockquote>
<p><em>Tóc rụng đứt mủn xót <strong>xa</strong>,</em><br/>
<em>Kẹp cua dối gạt gọi <strong>là</strong> thanh cao.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q51" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 51 [Lạm phát là thằng ăn trộm rút bát phở]: Cấm tấu hài lố lăng, chuyên gia làm thế nào để kiến thức khô khan hóa giải trí?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Biến học thuật thành ẩn dụ bình dân. Sự giải trí chính là cảm giác não được "ăn sẵn" mà vẫn khôn ra.</p>
<blockquote>
<p><em>Từ ngữ học thuật rối <strong>bời</strong>,</em><br/>
<em>Ví von bình dị sáng <strong>ngời</strong> tâm can.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q52" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 52 [Viên thuốc bọc đường / Template chill + Voiceover]: Bí thuật nào lừa khách hàng nuốt trọn chén đắng chuyên môn mà vẫn đê mê?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Lấy template video chill làm vỏ bọc xoa dịu đôi mắt, lồng voiceover bóc tách làm lõi để đánh úp tư duy.</p>
<blockquote>
<p><em>Mắt nhìn cảnh đẹp êm <strong>đề</strong>,</em><br/>
<em>Tai nghe lý lẽ vụt <strong>về</strong> nhận ra.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q53" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 53 [Đài Radio Tâm Lý / Binge-watching tự nguyện]: Khách VIP bận trăm công nghìn việc, bùa ngải nào trói họ lại đủ bảy giờ?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Biến kênh thành trạm phát thanh thụ động. Khách vừa lái xe vừa nghe rửa bát, cộng dồn vô thức tới lúc chốt đơn.</p>
<blockquote>
<p><em>Nửa đêm bật sóng thầm <strong>thì</strong>,</em><br/>
<em>Bảy giờ tích lũy chuyển <strong>đi</strong> bạc vàng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p10_q54" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 54 [Dopamine Khai sáng vs Dopamine Rẻ tiền]: Cười hô hố rồi quên sạch so với tiếng "À há" vỗ đùi, thứ nào ra tiền?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Cười cợt chỉ xả rác vào não. "À há" vì được gỡ rối vĩ mô mới tiết ra sự kính trọng và khao khát nộp tiền.</p>
<blockquote>
<p><em>Cười cợt não rỗng trôi <strong>mau</strong>,</em><br/>
<em>À há khai sáng khách <strong>cầu</strong> chuyên gia.</em></p>
</blockquote>
</div>
</div>
"""

content = content.replace('</ul>\n</aside>', toc_insert + '\n</ul>\n</aside>')

split_token = '<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>'
parts = content.split(split_token)

if len(parts) >= 2:
    new_content = parts[0] + body_insert + '\n' + split_token + parts[1]
    with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: logic24.html updated with Phần 9 & Phần 10.")
else:
    print("FAILED: split_token not found.")

