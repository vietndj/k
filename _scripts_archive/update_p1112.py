import sys

with open('/Users/vietmac/Documents/CODE/k/logic24.html', 'r', encoding='utf-8') as f:
    content = f.read()

toc_insert = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 11: KIẾN TRÚC VẬT LÝ CHÂN THẬT</li>
<li><a class="ink-toc-link" href="#p11_1">1. Gốc rễ hoài nghi</a></li>
<li><a class="ink-toc-link" href="#p11_2">2. Vật lý tự thân</a></li>
<li><a class="ink-toc-link" href="#p11_3">3. Lộ trình thuyết phục</a></li>

<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">PHẦN 12: THẨM VẤN VẬT LÝ</li>
<li><a class="ink-toc-link" href="#p12_q55">Q55. Cỗ máy nhiệt động lực học</a></li>
<li><a class="ink-toc-link" href="#p12_q56">Q56. 5 phản xạ vật lý mili-giây</a></li>
<li><a class="ink-toc-link" href="#p12_q57">Q57. Test Tải trọng Nhận thức</a></li>
<li><a class="ink-toc-link" href="#p12_q58">Q58. Tử huyệt Micro-latency</a></li>
<li><a class="ink-toc-link" href="#p12_q59">Q59. Máy phát điện lệch trục</a></li>
<li><a class="ink-toc-link" href="#p12_q60">Q60. Băng thông 40 bits vs 11 triệu</a></li>
<li><a class="ink-toc-link" href="#p12_q61">Q61. Thuật toán Mute Tracking</a></li>
<li><a class="ink-toc-link" href="#p12_q62">Q62. Hack năng lượng chốt sale</a></li>
"""

body_insert = """
<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 11 -->
<h1 class="is-short">PHẦN 11: KIẾN TRÚC VẬT LÝ CỦA SỰ CHÂN THẬT (HỆ THỐNG HÓA)</h1>
<p><em>(Trước khi bước vào phòng thẩm vấn, tôi xin hệ thống lại đầy đủ bức tranh toàn cảnh về những góc khuất và yêu cầu khắt khe mà anh đã đặt lên bàn mổ:)</em></p>

<ul>
    <li id="p11_1"><strong>1. Gốc rễ vấn đề & Sự hoài nghi cốt lõi:</strong> Anh Việt đang phân tích uy lực của "Tầng 2.5" (sự thật ngượng miệng, sợ hèn, tiếc tiền ở dưới đáy) so với Tầng 1 và Tầng 2 (đạo lý, cái cớ). Anh <strong>BÀI TRỪ</strong> mọi lý thuyết tâm lý học hàn lâm như "nơ-ron gương", "trực giác". Anh đặt câu hỏi cốt lõi: <em>"Bản chất thực sự của khả năng phát hiện nói dối là gì nếu gỡ bỏ lăng kính tâm lý?"</em></li>
    <li id="p11_2" style="margin-top: 12px;"><strong>2. Nhóm câu hỏi 1 - Tự thuyết phục chính mình (Bằng chứng Vật lý tự thân):</strong>
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li><strong>Góc nhìn Năng lượng:</strong> Tại sao nói thật là "Năng lượng cực tiểu" (Ground State), còn diễn kịch là "Cưỡng bức ép xung"? Ma sát nhận thức tản nhiệt ra sao?</li>
            <li><strong>Góc nhìn Cơ học:</strong> 5 phản xạ vật lý mất kiểm soát tốc độ mili-giây tố cáo cơ thể rò rỉ tín hiệu dối trá là gì?</li>
            <li><strong>Thực nghiệm tại bàn:</strong> Bài test vật lý cực đoan nào giúp tôi tự bắt quả tang chính mình sập nguồn vì bốc phét?</li>
            <li><strong>Góc nhìn thứ ba:</strong> Ống kính máy quay dùng các "thước đo thuần vật lý" nào (tần số âm, độ trễ lag động học, trương lực cơ) để loại bỏ kẻ giả tạo?</li>
        </ul>
    </li>
    <li id="p11_3" style="margin-top: 12px;"><strong>3. Nhóm câu hỏi 2 - Lộ trình đập tan lầm tưởng (Thuyết phục người khác):</strong>
        <ul style="margin-top: 8px; margin-bottom: 0;">
            <li><strong>Ẩn dụ cơ khí</strong> nào sắc lạnh đến mức một đứa trẻ 10 tuổi cũng hiểu sự dối trá rách nát đến đâu (máy phát điện, bánh xe, mạch điện)?</li>
            <li><strong>Lộ trình 4 bước đanh thép</strong> (Phá ngụy biện -> Gài bẫy tự thân -> Đối chiếu Mute Tracking -> Chốt hạ vũ khí Tầng 2.5 bằng Định lý Conant-Ashby) thực thi ra sao?</li>
        </ul>
    </li>
</ul>

<hr style="margin: 3rem 0; border: none; border-top: 4px solid var(--ink-text);"/>

<!-- PHẦN 12 -->
<h1 class="is-short">PHẦN 12: CUỘC THẨM VẤN VẬT LÝ - LỘT MẶT NẠ SỰ CHÂN THẬT</h1>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p12_q55" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 55: Đập tan lầm tưởng về "trực giác" và "nơ-ron gương". Nếu loại bỏ mớ lý thuyết tâm lý học sáo rỗng, cỗ máy sinh học của con người thực chất dùng radar cơ học nào để "đánh hơi" mùi giả tạo?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Con người là cỗ máy đo lường nhiệt động lực học! Sự thật Tầng 2.5 là "Năng lượng cực tiểu" (Ground State) - ổ cứng chỉ truy xuất, ma sát bằng 0. Khi diễn kịch đạo lý, vỏ não phải "ép xung" (Overclock) để dựng bối cảnh 3D. Ma sát nhận thức sinh ra nhiệt lượng dư thừa bắt buộc xả ra ngoài. Khán giả không hề "thấu cảm" bạn, ADN sinh tồn của họ chỉ đang lùi lại vì ngửi thấy mùi khét từ cỗ máy đang chập cháy của bạn!</p>
<blockquote>
<p><em>Chân ngôn tĩnh lặng an <strong>nhàn</strong>,</em><br/>
<em>Ép xung dối trá, nhiệt <strong>tràn</strong> nóng ran.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p12_q56" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 56: Đừng tự mãn về kỹ năng kiểm soát biểu cảm! Bằng chứng cơ học nào khẳng định cơ thể vật lý sẽ phản bội và tát thẳng vào mặt bạn chỉ trong vài mili-giây khi rặn ra một kịch bản bịa đặt?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Ý thức không bao giờ thao túng được Hệ thần kinh tự chủ! Khi bốc phét, 5 lỗi cơ học xả rác tức thì: (1) Cơ hoành co thắt ngắt bơm trợ lực; (2) Phổi thở nông gây vi ngắt quãng rớt chữ cuối câu; (3) Adrenaline căng cơ cổ, triệt tiêu dải âm trầm (bass); (4) Mao mạch gáy ửng đỏ tản nhiệt cho CPU não; (5) Hai bán cầu não giằng xé băng thông gây giật mép, chớp mắt loạn. Cơ thể bạn đang gào thét báo động giả!</p>
<blockquote>
<p><em>Hụt hơi thanh quản khô <strong>khan</strong>,</em><br/>
<em>Máu dồn ửng đỏ, vỡ <strong>tan</strong> nụ cười.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p12_q57" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 57: Hãy dẹp bỏ các bài test tâm lý rác rưởi! Có thực nghiệm vật lý cực đoan nào ngay tại bàn làm việc để tôi tận mắt thấy bộ não "sập nguồn" khi mở miệng bốc phét không?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Bài test "Tải trọng Nhận thức": Hãy đứng co một chân, tay bưng ly nước đầy ngang mặt. Lập tức thuyết trình to, trôi chảy về một thương vụ ngàn tỷ hoàn toàn bịa đặt. Bạn sẽ lảo đảo, ly nước văng tung tóe! Bộ não không đủ năng lượng (ATP) để gánh đa nhiệm: Vừa render kịch bản ảo, vừa duy trì trương lực cơ tĩnh. Nó buộc phải "cúp cầu dao" tay chân dồn điện lên miệng.</p>
<blockquote>
<p><em>Co chân tay giữ chén <strong>sành</strong>,</em><br/>
<em>Nói điêu bốc phét, tan <strong>tành</strong> đổ ngay.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p12_q58" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 58: Ống kính vô cảm và màng nhĩ khán giả không biết "đọc tâm trí". Vậy chúng dùng thước đo cơ học tàn nhẫn nào để lột mặt nạ kẻ học vẹt kịch bản trong phần ngàn giây?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Đòn tử huyệt là Động học chuyển động (Micro-latency). Sự thật Tầng 2.5: Não xử lý SONG SONG, miệng nhả chữ và tay đập bàn CÙNG MỘT MILI-GIÂY (Độ trễ = 0). Diễn kịch: Não xử lý NỐI TIẾP, vỏ não nặn chữ -> miệng nói -> sực nhớ kịch bản body language -> tay vung lên. Khán giả bắt được độ trễ "lag" 0.5 giây này, radar sinh tồn lập tức cảnh báo "tín hiệu méo", nổi da gà (cringe) và bật khiên cự tuyệt!</p>
<blockquote>
<p><em>Miệng vừa dứt chữ tay <strong>vung</strong>,</em><br/>
<em>Lệch pha nửa nhịp, nổ <strong>tung</strong> bệ đài.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p12_q59" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 59: Dùng ẩn dụ cơ khí tàn bạo nào chọc thủng cái tôi của những kẻ ảo tưởng "kịch bản đạo lý của em mượt mà không tì vết", khiến trẻ con 10 tuổi cũng thấy nhảm nhí?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Kịch bản giả dối là cỗ "máy phát điện lệch trục". Trên giấy (dắt bộ) thì êm ru, sơn bóng lộn. Nhưng bật máy há mồm (đạp 40km/h), trục lệch nện lốc máy xóc nảy, sinh nhiệt rung bần bật. Khán giả chạm tay qua màn hình, thấy độ rung rát bất thường sẽ tự lùi lại vì bản năng sợ nổ. Sự thật là "vành xe tròn tĩnh", kịch bản là "vành xe móp méo", càng gồng diễn, ma sát càng nghiền nát uy tín!</p>
<blockquote>
<p><em>Máy kia lệch trục rã <strong>rời</strong>,</em><br/>
<em>Vành cong đạp vội, tơi <strong>bời</strong> cốt xương.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p12_q60" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 60: Con số toán học sắc lạnh nào đủ sức chôn vùi vĩnh viễn lời biện minh yếu đuối: "Em nói thật mà, chỉ là lên video em chưa quen mặt ống kính nên hơi sượng"?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Nghiền nát bằng Băng thông dữ liệu! Khối ý thức cố nặn nụ cười giả tạo chỉ xử lý tối đa <strong>40 bits/giây</strong>. Nhưng Hệ thần kinh tự chủ đang hoảng loạn xả rác tín hiệu (vi áp lực máu, nhịp thở đứt, cơ gồng đóng băng) ra ngoài ở mức <strong>11 TRIỆU bits/giây</strong>. Dùng tờ giấy ăn 40 bits hòng bọc quả bom hạt nhân 11 triệu bits trước cỗ máy thu thập quang học tàn nhẫn như camera? Đó là sự ngu dốt tận cùng về vật lý!</p>
<blockquote>
<p><em>Bốn mươi bit mỏng che <strong>mành</strong>,</em><br/>
<em>Triệu luồng xả rác, tanh <strong>bành</strong> vỏ thưa.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p12_q61" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 61: Nghi thức "điều tra cơ học" nào ép kẻ lùa gà phải cúi đầu nhận tội giả tạo mà không có lấy một khe hở để há miệng phản kháng?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Thuật toán Mute Tracking (Tắt âm bám vết)! Đặt video họ diễn đạo lý cạnh video bộc phát chửi thề. TẮT SẠCH ÂM THANH để vô hiệu hóa màng lọc ngôn ngữ lừa đảo, tua chậm 0.5x. Đập thước vào màn hình: Đoạn chửi thề (Tầng 2.5), cơ thể lỏng lẻo lướt như chất lỏng, khớp lệnh tuyệt đối. Đoạn diễn kịch, bả vai đóng băng vi mô (micro-freezing), mắt đơ, mồm đi trước tay lag theo sau. Động lượng cơ khí không biết bẻ cong sự thật!</p>
<blockquote>
<p><em>Tắt âm tua chậm mà <strong>xem</strong>,</em><br/>
<em>Thân gồng tay trễ, lấm <strong>lem</strong> vở tuồng.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="p12_q62" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Câu hỏi 62: Cú lật bàn sinh học tối thượng: Tại sao dũng cảm thọc tay vào sự nhục nhã Tầng 2.5 không phải là màn xưng tội ướt át, mà là vũ khí thao túng chốt sale tàn bạo nhất?</h2>
<div class="dialogue-response">
<p><strong>Trả lời:</strong> Chân thật bóc trần Tầng 2.5 KHÔNG PHẢI ĐẠO ĐỨC, nó là Chiến lược Hack Năng Lượng Sinh Học. Khi xé toạc đáy Tầng 2.5, não triệt tiêu ma sát, rớt về Ground State. 100% băng thông tống vào lồng ngực tạo dải bass uy lực, bức xạ phát ra vô khuẩn. Màng nhĩ khách hàng quét trúng tín hiệu an toàn, tự tháo giáp. Theo Định lý Conant-Ashby: Kẻ nào gọi tên chính xác khe hở rách nát của hệ thống, não người xem mặc định phong người đó làm Kẻ Nắm Thuốc Giải. Họ tự chốt sale trước khi bạn kịp bán!</p>
<blockquote>
<p><em>Chân thành năng lượng đỉnh <strong>cao</strong>,</em><br/>
<em>Người xem tháo giáp, đón <strong>chào</strong> ngai vương.</em></p>
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
    print("SUCCESS: logic24.html updated with Phần 11 & Phần 12.")
else:
    print("FAILED: split_token not found.")

