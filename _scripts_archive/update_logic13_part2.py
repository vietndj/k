import re

with open('logic13.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update TOC
toc_insertion = """<li><a class="ink-toc-link" href="#q6">Q6. Bằng chứng thép fMRI</a></li>
<li><a class="ink-toc-link" href="#q7">Q7. Hiệu ứng thu hồi</a></li>
<li><a class="ink-toc-link" href="#q8">Q8. Tử huyệt danh tính</a></li>
<li><a class="ink-toc-link" href="#q9">Q9. Ẩn dụ chiếc váy</a></li>
<li><a class="ink-toc-link" href="#q10">Q10. Nhiệt động lực học não</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 2. Update Content
qa_content = """
<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q6" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q6: BẰNG CHỨNG THÉP TỪ MÁY QUÉT NÃO (Dopamine & Insula)<br>Nhiều kẻ mỉa mai rằng "chưa mua mà thấy bị cướp" chỉ là ảo giác tâm linh do bọn bán hàng bốc phét bịa ra. Bằng chứng y khoa vật lý nào tát thẳng vào sự kiêu ngạo này, chứng minh từ chối mua hàng là một vết thương rỉ máu thật sự?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Hãy ném tờ kết quả quét não fMRI vào mặt họ! Khi khách "dùng thử ảo", não tiết ngập tràn Dopamine sung sướng. Nhưng khoảnh khắc họ chối từ mua hàng, Dopamine sụp đổ và vùng não <strong>Insula</strong> (trung khu xử lý nỗi đau đứt tay, rỉ máu) lập tức rực sáng. Khách hàng không mua vì lý trí, họ hoảng loạn quẹt thẻ như một phản xạ sinh tồn để mua "liều thuốc giảm đau", dập tắt cơn đau đớn sinh lý do chính sự tước đoạt của bạn tạo ra!</p>
<blockquote>
<p><em>Nói lời từ chối mua hàng,<br/>Não đau như cắt vội vàng chốt ngay.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q7" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q7: HIỆU ỨNG THU HỒI VŨ KHÍ VIP (Góc nhìn Game)<br>Nếu thực tại của khách hàng đang ở mức 0 (bế tắc), khi không mua giải pháp họ chỉ quay về số 0. Nghịch lý toán học nào khiến tiềm thức đánh lừa họ rằng: "Trở về số 0 chính là vừa bị trừ đi 10 điểm"?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì cỗ máy não bộ vận hành y hệt một tựa game nhập vai tàn nhẫn! Khi khách bế tắc, bạn cho họ mượn "Vũ khí VIP Max Level" (viễn cảnh nhàn hạ). Họ đắm chìm và bay thẳng lên mức +10. Ngay khi bạn dọa thu hồi vũ khí, Điểm Neo Thực Tại đã bị dời đi. Cú rơi tự do từ +10 xuống 0 không được dịch là "hòa vốn", não gào thét rằng đó là một <strong>Cú Nerf (Giảm sức mạnh) tước đoạt quyền lực</strong>. Cơn cay cú vì bị hạ cấp ép họ nạp tiền chuộc lại thanh gươm!</p>
<blockquote>
<p><em>Mượn gươm chém quái tung hoành,<br/>Thu hồi một phát tan tành mộng mơ.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q8" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q8: TỬ HUYỆT DANH TÍNH BẦY ĐÀN (Cấp độ sở hữu tàn độc nhất)<br>Tước đi sự mát mẻ hay rảnh rỗi mới chỉ gãi ngứa ngoài da. Đâu mới là chiếc công tắc nguyên thủy, nhẫn tâm nhất trong DNA khiến một người dùng lý trí đến mấy cũng phải điên cuồng vung tiền bằng mọi giá?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đó là khi bạn tước đoạt <strong>Danh tính và Vị thế bầy đàn</strong>! Thay vì vẽ cảnh nhàn hạ, hãy chiếu đoạn phim họ đứng trên bục cao, sếp nể trọng, kẻ thù ghen tị hộc máu. Lúc này, não đã tự động khoác lên chiếc áo hoàng bào quyền lực. Khi bạn rút phích cắm, thứ họ đối mặt không phải là sự vất vả tay chân, mà là <strong>nỗi nhục nhã ê chề</strong> vì bị giáng chức về làm kẻ bần hàn. Bản năng sợ hãi bị bầy đàn đào thải, khinh bỉ sẽ bóp nghẹt mọi lý trí!</p>
<blockquote>
<p><em>Khoác lên chiếc áo kiêu hùng,<br/>Lột ra nhục nhã bần cùng xót xa.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q9" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q9: ẨN DỤ CHIẾC VÁY TRONG PHÒNG THỬ (Bán dịch vụ vô hình)<br>Bán cái quạt vật lý thì dễ hình dung việc "tước đoạt". Nhưng nếu tôi bán khóa học, bán tư duy vô hình thì làm sao áp dụng? Làm thế nào để tước đi một thứ mà bản thân nó còn không có hình hài để cầm nắm?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Lầm tưởng vĩ đại: Khách hàng không bao giờ tranh giành miếng vải, họ giành giật <strong>viễn cảnh tương lai</strong>! Cô gái mất chiếc váy khóc hận vì viễn cảnh "làm lác mắt người yêu cũ" vừa bị cướp trắng. Bán vô hình cũng vậy, bạn phải "vật lý hóa" thành quả. Hãy dùng lời nói mặc cho não họ chiếc áo của sự thông thái, quyền uy. Lời từ chối mua khóa học lúc này chính là hành động tự lột sạch quần áo danh vọng, bắt họ đứng trần truồng giữa đám đông dốt nát!</p>
<blockquote>
<p><em>Bán buôn chữ nghĩa vô hình,<br/>Vẽ ra viễn cảnh giật mình chốt luôn.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q10" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q10: BÀI TOÁN NHIỆT ĐỘNG LỰC HỌC CỦA NÃO (Góc nhìn năng lượng)<br>Không mua hàng rõ ràng là tiết kiệm được tiền. Tại sao não lại coi sự "tiết kiệm" đó là tội ác, rồi phản kháng bằng sự bứt rứt, cáu bẳn y như bị đuổi ra đứng giữa trời nắng 40 độ?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bởi tiền bạc chỉ là khái niệm nhân tạo, <strong>Năng lượng (Calo)</strong> mới là đồng tiền tối cao của sinh tồn! Thực tại hỗn loạn của khách ngốn quá nhiều Calo để chịu đựng. Giải pháp bạn vẽ ra là đường tắt tiết kiệm pin tuyệt đối. Khi khách từ chối mua, não lập tức biểu tình vì nó vừa bị tước đoạt "bộ sạc dự phòng" và bắt buộc phải trở về trạng thái đốt Calo rỉ máu. Cơn bứt rứt chính là tiếng thét đòi sinh tồn, ép họ mua giải pháp chỉ để được... quyền lười biếng!</p>
<blockquote>
<p><em>Não lười chỉ thích thảnh thơi,<br/>Rút đi máy lạnh chơi vơi cõi lòng.</em></p>
</blockquote>
</div>
</div>
"""

content = content.replace('<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 5 rãnh', qa_content + '\n<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 5 rãnh')
content = content.replace('5 rãnh Data cốt lõi', '10 rãnh Data cốt lõi')

with open('logic13.html', 'w', encoding='utf-8') as f:
    f.write(content)

