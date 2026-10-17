import re

with open('logic10.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update TOC title
content = content.replace("BẢN ĐÚC KẾT 8 NHÁT DAO", "BẢN ĐÚC KẾT 14 NHÁT DAO")

# 2. Append TOC
toc_insertion = """<li><a class="ink-toc-link" href="#q28">9. Bằng chứng thực tế</a></li>
<li><a class="ink-toc-link" href="#q29">10. Trạm thu phí</a></li>
<li><a class="ink-toc-link" href="#q30">11. Phân khúc giá cao</a></li>
<li><a class="ink-toc-link" href="#q31">12. Tội ác dạy từ A-Z</a></li>
<li><a class="ink-toc-link" href="#q32">13. Tin chuyên gia</a></li>
<li><a class="ink-toc-link" href="#q33">14. Thảnh thơi bình dân</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 3. Update Content title
content = content.replace("8 nhát dao (Hỏi Sốc - Đáp Thẳng)", "14 nhát dao (Hỏi Sốc - Đáp Thẳng)")

# 4. Append Content
qa_content = """
<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q28" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 9. BẰNG CHỨNG THỰC TẾ ĐẬP CHẾT "GIẤY TỜ VÔ TRI"<br>Tại sao siêu thị dán tem VietGAP đỏ chót mà khách vẫn bĩu môi, còn ông chủ vườn bứt quả táo chưa rửa nhai rôm rốp trên video lại nổ đơn tới tấp?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì khách biết thừa giấy tờ thời nay là mớ mực in vô tri mua được bằng tiền. Nhưng khi bạn dám dùng cái dạ dày và sinh mệnh của chính mình để nếm thử, bạn đang thế chấp bằng nhân phẩm. Khách chỉ bị khuất phục bởi hành động thực chứng tàn khốc của đồng loại, chứ không tin giấy A4!</p>
<blockquote>
<p><em>Tem xanh mác đỏ rườm rà,<br/>Chính mình thử nghiệm, mới là niềm tin.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q29" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 10. BẢN CHẤT CỦA GIAO DỊCH (SẢN PHẨM LÀ TRẠM THU PHÍ)<br>Khách hàng bỏ hàng chục triệu rước cái máy giặt to oạch, ồn ào về nhà, có phải họ thực sự yêu thích và khao khát cái khối sắt ấy không?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Không ai thức dậy và thèm ôm một cục nợ! Sản phẩm vật lý chỉ là "trạm thu phí" bắt buộc phải bước qua. Thứ khách thực sự vung tiền mua là 45 phút thảnh thơi nằm sofa. Bán hàng mà cứ ca ngợi tính năng máy là bắt khách yêu trạm thu phí. Hãy bán sự sung sướng ở đích đến!</p>
<blockquote>
<p><em>Cái đồ vật lý vô tri,<br/>Bỏ tiền mua lấy, chỉ vì rảnh tay.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q30" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 11. BÍ MẬT CỦA PHÂN KHÚC GIÁ CAO (HIGH-TICKET)<br>Tại sao cái đồng hồ 300 triệu xem giờ sai số lung tung khách VIP vẫn quẹt thẻ cái rụp, còn cái đồng hồ 500 ngàn xem giờ chuẩn xác từng giây họ lại chê bai?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì ở phân khúc đắt tiền, công năng vật lý bị triệt tiêu về 0. Người giàu không mua đồng hồ để xem giờ, họ mua một "Tín hiệu phát sóng" để dằn mặt xã hội. Bạn bán cho họ sự nể trọng trên bàn đàm phán, một tờ giấy thông hành giúp chốt hợp đồng tiền tỷ dễ dàng hơn.</p>
<blockquote>
<p><em>Công năng vật lý vứt đi,<br/>Mua phần vị thế, phòng khi ra ngoài.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q31" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 12. TỘI ÁC MANG TÊN "DẠY TỪ A ĐẾN Z" (HIỆU ỨNG NETFLIX)<br>Tại sao làm video chia sẻ kinh nghiệm rút ruột gan, dạy tận tình từ A đến Z, khách xem sướng rên nhưng cuối cùng không ai thèm mua hàng hay follow?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì bạn đã dọn mâm cho họ "ăn no ứ hự". Bản năng của não là hễ ăn no sẽ lập tức đóng cửa đi ngủ. Muốn giữ chân khách, phải học đạo diễn Netflix: luôn ngắt phim ở cảnh gay cấn nhất. Giữ lại 10% sự dang dở, tò mò mới là sợi xích ép họ bám theo bạn.</p>
<blockquote>
<p><em>Dốc lòng chia sẻ ngọn ngành,<br/>Khách xem no đủ, bước nhanh không tìm.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q32" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 13. SỰ THẬT TRẦN TRỤI VỀ TÂM LÝ "TIN CHUYÊN GIA"<br>Tại sao con ốm lên mạng tra Google thì hoang mang sợ hãi, nhưng bế ra bác sĩ quen bị ổng mắng cho một câu lại thở phào mang con về? Có phải vì họ thần tượng bác sĩ không?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Không! Vì mớ kiến thức khổng lồ vô hồn trên mạng làm não kiệt sức. Khách không rảnh để tự phân tích đúng sai, họ khao khát tìm một "cái bia đỡ đạn" có uy quyền để uỷ thác quyết định. Họ nhắm mắt làm theo để lỡ có bề gì thì có người mà đổ lỗi, bắt đền cho nhẹ đầu.</p>
<blockquote>
<p><em>Tưởng đâu khách nể bề trên,<br/>Hóa ra lười nghĩ, bắt đền cho nhanh.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q33" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ 14. LỜI HỨA HOANG ĐƯỜNG VS SỰ THẢNH THƠI BÌNH DÂN<br>Tại sao hứa "khóa học giúp x10 doanh thu, mua nhà mua xe" sếp không thèm mua, nhưng bảo "tool này giúp anh gõ sườn kịch bản 5 phút để chiều đi cafe" lại quẹt thẻ luôn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì hứa hẹn quá to tát thì não sẽ tự động bật khiên chống lừa đảo. Đích đến mà con người thực sự thèm khát mỗi ngày cực kỳ trần trụi: Đỡ mỏi lưng, bớt nhức mắt, rảnh tay chân, về sớm với con. Bán sự thảnh thơi bình dân luôn chốt đơn nhanh hơn bán mộng tưởng hoang đường.</p>
<blockquote>
<p><em>Vẽ ra mộng lớn hoang đường,<br/>Trao ngay sự rảnh, khách thương rút tiền.</em></p>
</blockquote>
</div>
</div>

<div style="margin-top: 4rem; padding: 2rem; background: var(--ink-bg-secondary); border-radius: 8px;">
<h3 style="margin-top: 0;">💡 BÍ QUYẾT ĐIỀU PHỐI (Dành riêng cho bạn khi đứng trên sân khấu):</h3>
<p>Trọn bộ 14 nhát dao này là một kịch bản hoàn hảo để bạn thao túng nhịp độ hội trường. Đừng đọc slide như trả bài!</p>
<ol>
<li>Trên màn hình máy chiếu, bạn chỉ chiếu đúng MỘT DÒNG: <strong>Câu hỏi xoáy</strong>.</li>
<li><strong>Dừng hình đúng 3-5 giây</strong> (để hội trường im phăng phắc, ép học viên nhăn trán tự thấy cái sai của mình).</li>
<li>Vả phần <strong>Đáp thẳng</strong> vào mặt họ bằng chất giọng trần trụi, điềm tĩnh.</li>
<li>Đọc nhẩn nha 2 câu <strong>Lục bát</strong>, gằn giọng ở những chữ gieo vần để tạo âm hưởng vang rền như một chân lý không thể cãi lại. Họ sẽ tự động lấy sổ ra chép.</li>
</ol>
<p>Chúc bạn có một bục giảng bùng nổ, "gõ đầu" thức tỉnh mọi bộ não u mê nhất!</p>
</div>
"""

content = content.replace('<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 27 rãnh', qa_content + '\n<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 27 rãnh')
content = content.replace('27 rãnh Data cốt lõi', '33 rãnh Data cốt lõi')

with open('logic10.html', 'w', encoding='utf-8') as f:
    f.write(content)

