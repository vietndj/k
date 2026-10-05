import re

with open('logic09.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Thêm TOC
toc_insertion = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">THIẾT KẾ HÀNH VI</li>
<li><a class="ink-toc-link" href="#q5">Q5. Vỏ bọc an toàn</a></li>
<li><a class="ink-toc-link" href="#q6">Q6. Đình chiến tâm lý</a></li>
<li><a class="ink-toc-link" href="#q7">Q7. Đồng bộ khiếm khuyết</a></li>
<li><a class="ink-toc-link" href="#q8">Q8. Điểm xả trung gian</a></li>
<li><a class="ink-toc-link" href="#q9">Q9. Neo trí nhớ vi mô</a></li>
"""
content = content.replace("</ul>\n</aside>", toc_insertion + "</ul>\n</aside>")

# 2. Thêm Nội dung
qa_content = """
<hr style="margin: 4rem 0; border: none; border-top: 4px solid var(--ink-text);"/>
<h1 class="is-short">KHOA HỌC THIẾT KẾ HÀNH VI: BẢN CHẤT CỦA STORYTELLING</h1>
<hr style="margin: 3rem 0; border: none; border-top: 1px solid var(--ink-border);"/>

<div style="margin-bottom: 3rem;">
    <p>Bạn nhận định hoàn toàn chính xác. Lời góp ý của bạn thể hiện tư duy của một người hiểu rất rõ bản chất của giao tiếp và tâm lý học: <strong>Sự thật tự thân nó đã có sức thuyết phục tuyệt đối.</strong></p>
    <p>Thuyết phục đỉnh cao không nằm ở việc dùng ngôn từ đao to búa lớn, tiếng lóng hay cường điệu hóa cảm xúc. Sự cường điệu thực chất là lớp vỏ bọc che đậy sự thiếu tự tin vào cốt lõi vấn đề. Quyền lực thực sự của lời nói nằm ở tính logic, sự trực diện và khả năng "đọc vị" chính xác đến mức người nghe tự nguyện đồng tình.</p>
    <p>Để thay thế cho từ "Storytelling" hào nhoáng, chúng ta sẽ trả nó về đúng bản chất là <strong>Khoa học thiết kế hành vi</strong>. Dưới đây là 5 cơ chế tâm lý cốt lõi, được trình bày dưới dạng Hỏi - Đáp trực diện, điềm tĩnh và chuyên nghiệp.</p>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q5" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q5: Cơ chế "Vỏ Bọc An Toàn" (Cung cấp lý do hợp pháp)<br>Tại sao khán giả hiếm khi tự than vãn về khó khăn của họ trên mạng, nhưng lại dễ dàng bình luận bày tỏ sự bế tắc khi tôi là người chủ động chia sẻ về thất bại của mình trước?</h2>
<div class="dialogue-response">
<p><strong>💡 Trả lời trực diện:</strong><br>Vì cơ chế bảo vệ hình ảnh cá nhân (Ego). Việc tự thừa nhận khó khăn khiến con người cảm thấy yếu thế trước đám đông. Tuy nhiên, khi bạn chủ động bộc lộ sự bế tắc của mình, bạn cung cấp cho khán giả một "vỏ bọc an toàn". Họ mượn sự đồng cảm với câu chuyện của bạn để danh chính ngôn thuận bộc lộ áp lực của chính họ, dưới lớp vỏ bọc là một người biết lắng nghe và thấu cảm.</p>
<p><strong>🔍 Ví dụ thực tế:</strong><br>Một người đang gặp áp lực tài chính rất lớn, muốn rơi nước mắt nhưng không muốn gia đình lo lắng. Khi nấu ăn, người đó thái một củ hành tây để nước mắt chảy tự nhiên. Khi được hỏi, người đó đáp: <em>"Do hành cay quá"</em>. Củ hành là lớp vỏ bọc hoàn hảo để hợp thức hóa việc khóc. Sự thất bại bạn chia sẻ trên video đóng vai trò chính xác như củ hành đó.</p>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q6" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q6: Cơ chế "Đình Chiến Tâm Lý" (Hạ vũ khí phòng thủ)<br>Nếu kiến thức tôi chia sẻ là đúng và hữu ích, tại sao việc đưa ra lời khuyên trực tiếp thường khiến người xem phản kháng, cãi lại hoặc lướt qua?</h2>
<div class="dialogue-response">
<p><strong>💡 Trả lời trực diện:</strong><br>Vì lời khuyên trực tiếp tự động đặt bạn ở vị thế "người biết dạy người chưa biết", điều này vô thức kích hoạt rào cản tự ái của người nghe. Để họ tiếp nhận thông tin, bạn phải dỡ bỏ rào cản này bằng cách tự hạ thấp vị thế. Khi bạn mở đầu bằng việc thừa nhận một sai lầm của bản thân, khán giả cảm thấy an toàn và mất đi sự đề phòng. Chỉ khi hàng rào phòng thủ hạ xuống, kiến thức của bạn mới có thể đi vào nhận thức của họ.</p>
<p><strong>🔍 Ví dụ thực tế:</strong><br>Khi bạn vi phạm giao thông mức độ nhẹ, nếu bạn bước xuống xe và cãi lý, sự căng thẳng sẽ leo thang vì hai bên ở thế đối kháng. Nhưng nếu bạn chủ động nhận lỗi ngay lập tức: <em>"Tôi sơ suất quá, lỗi hoàn toàn do tôi"</em>, thái độ của người xử lý thường sẽ dịu lại. Việc tự nhận khuyết điểm đã triệt tiêu vũ khí phản kháng của cả hai bên.</p>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q7" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q7: Cơ chế "Đồng Bộ Khiếm Khuyết" (Xóa bỏ khoảng cách)<br>Là một người chia sẻ chuyên môn về xây kênh, việc tôi luôn giữ hình ảnh kỷ luật, hoàn hảo có giúp tôi xây dựng uy tín vững chắc hơn không?</h2>
<div class="dialogue-response">
<p><strong>💡 Trả lời trực diện:</strong><br>Không. Sự hoàn hảo chỉ tạo ra sự ngưỡng mộ từ xa. Trong thực tế, những người mới làm nghề luôn có những thói quen chưa chuẩn mực mà họ thường giấu kín (ví dụ: lén dùng điện thoại khác để cày view, đố kỵ ngầm với kênh đối thủ). Khi bạn thú nhận mình cũng từng có những hành vi đó, bạn xóa bỏ khoảng cách chuyên gia. Lòng tin sâu sắc nhất được thiết lập khi hai bên chia sẻ chung một khiếm khuyết, vì nó là minh chứng rõ nhất cho việc bạn thực sự thấu hiểu thực tế của họ.</p>
<p><strong>🔍 Ví dụ thực tế:</strong><br>Trong một buổi họp, nếu người quản lý nói: <em>"Tôi luôn làm việc với 100% kỷ luật"</em>, nhân viên sẽ nghe nhưng giữ khoảng cách. Nếu quản lý nói: <em>"Thú thật, thỉnh thoảng tôi cũng chán nản và trì hoãn công việc đến sát giờ"</em>, nhân viên lập tức cảm thấy sự gần gũi. Sự chân thật và tính "con người" tạo ra niềm tin nhanh hơn sự hoàn hảo.</p>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q8" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q8: Cơ chế "Điểm Xả Trung Gian" (Chuyển hướng áp lực)<br>Tại sao những nội dung phàn nàn về lỗi phần mềm, máy móc hư hỏng hay thuật toán nền tảng lại thường nhận được sự tương tác và đồng tình cao bất thường?</h2>
<div class="dialogue-response">
<p><strong>💡 Trả lời trực diện:</strong><br>Con người thường xuyên tích tụ áp lực trong công việc và cuộc sống nhưng hiếm khi có không gian an toàn để trút bỏ. Khi bạn phàn nàn về một đối tượng vô tri vô giác (như thuật toán hay phần mềm), bạn đang tạo ra một "điểm xả trung gian". Khán giả hùa theo để phàn nàn cùng bạn, nhưng thực chất họ đang mượn đối tượng đó để giải tỏa sự bức xúc cá nhân mà không sợ làm tổn hại đến các mối quan hệ thực tế.</p>
<p><strong>🔍 Ví dụ thực tế:</strong><br>Một nhân viên bị cấp trên khiển trách vô lý nhưng phải nhẫn nhịn. Khi về đến nhà, vô tình vấp vào cạnh bàn, người này tức giận đá mạnh vào chiếc bàn. Chiếc bàn không có lỗi, nó chỉ là điểm tiếp nhận an toàn cho sự bực tức không thể xả ở công ty.</p>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q9" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q9: Cơ chế "Neo Trí Nhớ Vi Mô" (Đọc vị qua chi tiết)<br>Tại sao việc nói về những khó khăn chung chung (như "làm video rất cực") lại kém hiệu quả hơn việc mô tả một thao tác vật lý vô cùng nhỏ nhặt?</h2>
<div class="dialogue-response">
<p><strong>💡 Trả lời trực diện:</strong><br>Não bộ thường lờ đi các khái niệm trừu tượng vì đã nghe quá nhiều, nhưng lại ghi nhớ rất sâu các hành động vật lý cụ thể. Khi bạn miêu tả một thói quen vi mô mà chỉ người trực tiếp làm nghề mới biết, khán giả lập tức có cảm giác "bị đọc vị". Tính chính xác tuyệt đối của một chi tiết nhỏ sẽ tự động xóa bỏ sự hoài nghi và chứng minh năng lực chuyên môn của bạn, thay vì những lời khẳng định dông dài.</p>
<p><strong>🔍 Ví dụ thực tế:</strong><br>Thay vì nói chung chung: <em>"Phòng của bạn bừa bộn quá"</em>, người nghe có thể ngụy biện <em>"Tôi đã dọn rồi"</em>. Nhưng nếu bạn nói: <em>"Dưới gầm giường có 3 vỏ kẹo và góc tủ giấu một chiếc tất chưa giặt"</em>, người nghe buộc phải im lặng chấp nhận. Chi tiết cụ thể loại bỏ hoàn toàn cơ hội ngụy biện.</p>
</div>
</div>

<div style="margin-top: 3rem; background: var(--ink-bg-alt); padding: 2rem; border-left: 4px solid var(--ink-border);">
    <h3 style="font-family: var(--font-display-short); font-weight: 600; font-size: 1.25rem; margin-top: 0;">TỔNG KẾT TƯ DUY (Dành cho việc viết kịch bản):</h3>
    <p>Từ nay, thay vì mơ hồ với khái niệm "Storytelling", khi bạn viết phần mở đầu (Hook) cho video, bạn chỉ cần tư duy theo 1 trong 3 hướng điềm tĩnh và logic sau:</p>
    <ol style="margin-bottom: 0;">
        <li>Mình đang dùng câu chuyện này để làm <strong>Vỏ bọc an toàn</strong> cho họ giải tỏa điều gì?</li>
        <li>Mình đã <strong>Đình chiến tâm lý</strong> (tự hạ rào phòng thủ) trước khi đưa ra kiến thức chưa?</li>
        <li>Mình dùng <strong>Neo trí nhớ vi mô</strong> nào để chứng minh mình hiểu công việc này đến tận cùng?</li>
    </ol>
    <p style="margin-bottom: 0; margin-top: 1rem;">Sự thật, khi được đặt đúng vào các cơ chế tâm lý này, sẽ tự động phát huy sức mạnh thuyết phục của nó một cách điềm tĩnh và chuyên nghiệp nhất.</p>
</div>
"""

content = content.replace('<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 4 rãnh', qa_content + '\n<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 4 rãnh')
content = content.replace('4 rãnh', '9 rãnh')

with open('logic09.html', 'w', encoding='utf-8') as f:
    f.write(content)

