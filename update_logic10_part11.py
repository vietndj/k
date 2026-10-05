import re

file_path = '/Users/vietmac/Documents/CODE/k/logic10.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_toc_items = """
<li><a class="ink-toc-link" href="#q72">6. Bẫy ngã mạn tâm linh</a></li>
<li><a class="ink-toc-link" href="#q73">7. Ái kỷ và thú dữ</a></li>
<li><a class="ink-toc-link" href="#q74">8. Cơn giãy chết tự ái</a></li>
<li><a class="ink-toc-link" href="#q75">9. Chiếc cầu vàng</a></li>
<li><a class="ink-toc-link" href="#q76">10. Tự do tuyệt đối</a></li>
"""

toc_marker = "</ul>\n</aside>"
if toc_marker in content:
    content = content.replace(toc_marker, new_toc_items + "\n" + toc_marker)

new_content = """
<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase; margin-top: 4rem;">BẪY TÂM LÝ & ẢO TƯỞNG CỦA SỰ "TỈNH THỨC"</h2>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q72" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 6: BẪY NGÃ MẠN TÂM LINH (Spiritual Ego)<br>Bạn nghĩ cứ ngoan ngoãn cúi đầu, xưng "em/con" với người nhỏ tuổi là tự động giết chết được Bản ngã? Tại sao sự khiêm nhường thái quá này lại là chiếc lồng ấp sinh ra con quái vật "Ngã mạn tâm linh" độc hại và kiêu ngạo gấp ngàn lần kẻ phàm phu tục tử?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bản ngã là một loài ký sinh trùng biến hình. Nếu bạn hạ danh xưng, tỏ ra nhún nhường nhưng sâu trong bụng lại tự vuốt ve: <em>"Nhìn xem, ta tĩnh lặng thế này, ta giác ngộ và bao dung hơn hẳn lũ phàm nhân kia"</em>, thì chúc mừng, bạn đã sập bẫy. Cái tôi của bạn chưa hề chết, nó chỉ lột bỏ chiếc áo vest thế tục để khoác lên tấm áo cà sa lộng lẫy, tiếp tục làm Vua ở một cảnh giới đạo đức giả. Vô ngã thực sự là sự rỗng không. Bạn gọi người khác là "anh/chị" đơn giản vì chiếc cốc của bạn đã rỗng, danh xưng chỉ là công cụ tùy duyên, hoàn toàn không có cảm giác mình đang phải "cố gắng hạ mình" hay "ban phát sự tôn trọng".</p>
<blockquote>
<p><em>Hạ mình che đậy kiêu căng, <br/>Ngã tâm còn đó, trói giăng cuộc đời. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q73" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 7: ÁI KỶ VÀ THÚ DỮ<br>Tuyệt chiêu "Hạ mình như nước" có uy lực đập tan sự phòng thủ. Nhưng tai họa diệt vong nào sẽ giáng xuống đầu bạn nếu bạn hoang tưởng mang "thế võ" này áp dụng bừa bãi với những kẻ mắc chứng Ái kỷ (Narcissist) hay những con quái thú khát quyền lực chốn thương trường?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bạn sẽ bị chúng nhai nuốt không chừa một mẩu xương. Radar của loài Ái kỷ độc hại không quét "sự nhún nhường", chúng chỉ đánh hơi "con mồi hèn yếu". Khi bạn ném bỏ vương miện và xưng "em/con", khiên tự ái của chúng không hề rã ra, trái lại, chúng hân hoan nhào tới chà đạp bạn để thỏa mãn thú tính bạo chúa. Vô ngã không phải là sự cam chịu làm thảm chùi chân. Nội tâm rỗng lặng, nhưng bề ngoài phải linh hoạt. Gặp thú dữ, bạn buộc phải dựng một ranh giới thép, khoác lên chiếc mặt nạ uy quyền sắc lạnh để bẻ gãy nanh vuốt của chúng, nhưng tuyệt đối không để tâm trí bị cuốn vào thù hận.</p>
<blockquote>
<p><em>Dòng sông tĩnh lặng hiền hòa, <br/>Gặp loài ác thú, xót xa ngậm ngùi. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q74" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 8: CƠN GIẪY CHẾT CỦA BẢN NGÃ (Extinction Burst)<br>Khi bạn buông tay khỏi sợi dây "kéo co địa vị", tại sao có những kẻ không chịu bình tĩnh lại, mà quẫy đạp điên cuồng, nhục mạ bạn tàn độc hơn để ép bạn xù lông? Trong khoảnh khắc "thử lửa" này, đỡ đòn thì hỏng, không đỡ thì nhục, phải làm sao?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Khi bị tước đi điểm tựa "kẻ thù", bản ngã của họ ngạt thở. Để sinh tồn, chúng gào thét, buông lời lăng mạ cốt chỉ để quăng cho bạn một "sợi dây tức giận", cầu xin bạn hãy cầm lấy để chúng vớt vát thể diện. Nhiệm vụ duy nhất của bạn: <strong>Mặc kệ chúng đấm vào khoảng không.</strong> Lửa ném vào mặt hồ tĩnh lặng chỉ kêu xèo xèo vài tiếng rồi tự tắt ngấm vì thiếu oxy. Nếu bạn lỡ miệng đáp trả dù chỉ một câu, vòm sắt tự ái của họ lập tức hồi sinh và lấn lướt. Hãy đứng đó bằng ánh mắt ráo hoảnh, họ sẽ tự sụp đổ vì ngượng ngùng khi nhận ra mình đang hóa điên múa rối một mình.</p>
<blockquote>
<p><em>Lửa thù giãy chết cuồng điên, <br/>Tâm ta tựa nước, an nhiên đứng nhìn. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q75" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 9: CHIẾC CẦU VÀNG (Lối thoát danh dự)<br>Bằng thái độ "bản tin thời tiết", bạn đã lột trần sự thật thành công. Đối phương tê liệt, ngượng ngùng, không thể chối cãi. Nhưng nếu vạch trần xong mà bạn bỏ mặc họ ở đó, tại sao bạn lại biến thành một tên đồ tể tàn nhẫn thay vì một vị y bác sĩ cứu người?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Lột trần sự thật chỉ là bước "Phá". Khi lớp vỏ tự ái vỡ vụn, cái tôi của họ trần truồng và ứa máu. Ngay khoảnh khắc não họ mở toang đó, bạn bắt buộc phải quăng ra một <strong>"Chiếc cầu vàng" (Lối thoát danh dự)</strong>. Hãy đồng hóa sự yếu kém của họ với sinh học loài người: <em>"Lúc hoảng loạn thì ai chả phản xạ sai lầm như vậy, não bộ bị quá tải mà."</em> Lập tức, nút thắt nhục nhã được cởi trói. Họ nhận ra mình không phải là tội đồ bị cô lập, mà chỉ là một con người bình thường. Khối u bị cắt bỏ nhưng vết thương được khâu lại bằng sự thấu cảm, oán hận tan biến, họ mới thực sự quy hàng.</p>
<blockquote>
<p><em>Lột trần bẽ mặt ê chề, <br/>Quăng phao cứu vớt, đường về thênh thang. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q76" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 10: TỰ DO TUYỆT ĐỐI<br>Vạn pháp quy tông. Nếu bạn mài giũa trạng thái vô ngã, luyện tuyệt kỹ hạ danh xưng, xóa sổ tính từ... chỉ để thống trị các cuộc đàm phán, thao túng tâm lý và ép thiên hạ phải phục tùng mình... thì bạn đang tự nhốt mình vào tấn bi kịch nực cười nào?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bạn vừa đào tẩu khỏi nhà giam "Tự ái mỏng manh" để tự nộp mình cho ngục tối của "Ngạo mạn quyền lực". Đích đến tối thượng của hệ tư tưởng này chưa bao giờ là dùng để chiến thắng kẻ khác, mà là <strong>Sát thủ tiêu diệt khao khát muốn giành chiến thắng của chính bạn</strong>. Ngày bạn nhìn một lời chửi rủa vô lý mà nhịp tim không đập nhanh thêm một nhịp, ngày bạn cúi đầu trước một người ăn mày với sự trân trọng tột cùng mà không thấy mình cao thượng... đó là lúc bạn thực sự tự do. Khi bạn chấp nhận mình "Không là gì cả", không vũ khí nào đâm thủng được bạn, nhưng bạn lại chứa đựng được cả vũ trụ.</p>
<blockquote>
<p><em>Mưu đồ thao túng nhân tâm, <br/>Buông tay rỗng lặng, nảy mầm tự do. </em></p>
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
