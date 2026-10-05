import re

file_path = '/Users/vietmac/Documents/CODE/k/logic10.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_toc_items = """
<li><a class="ink-toc-link" href="#q45">6. Nấm mồ phục vụ số đông</a></li>
<li><a class="ink-toc-link" href="#q46">7. Án tử hack thuật toán</a></li>
<li><a class="ink-toc-link" href="#q47">8. Đuối lý hào nhoáng</a></li>
<li><a class="ink-toc-link" href="#q48">9. AI là sếp thật sự</a></li>
<li><a class="ink-toc-link" href="#q49">10. Tang lễ quảng cáo lùa gà</a></li>
"""

toc_marker = "</ul>\n</aside>"
if toc_marker in content:
    content = content.replace(toc_marker, new_toc_items + "\n" + toc_marker)

new_content = """
<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q45" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 6: NẤM MỒ TẬP THỂ CỦA TƯ DUY "PHỤC VỤ SỐ ĐÔNG"<br>Tại sao việc bạn cố gắng làm nội dung "dễ dãi, ai xem cũng hiểu" lại chính là hành động tự đào mồ chôn kênh của mình? Phục vụ tất cả mọi người chẳng phải là sẽ bán được nhiều hàng hơn sao?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đó là tư duy của kẻ nghiệp dư! Phục vụ tất cả đồng nghĩa với việc bạn trở nên vô giá trị. Khi bạn làm nội dung "lẩu thập cẩm", Vector dữ liệu của bạn rối loạn. AI không thể định vị bạn là chuyên gia lĩnh vực nào, liền thẳng tay ném bạn vào bãi rác vô danh. Hãy cực đoan hóa! Chỉ nói về một ngách hẹp, dùng ngôn từ chuyên môn hóc búa nhất. AI căm ghét sự chung chung, nhưng nó sẽ cống hiến hết mình để gắp nội dung chuyên biệt ném thẳng vào mâm của tệp khách VIP.</p>
<blockquote>
<p><em>Đừng tham phục vụ muôn người, <br/>Ngách sâu sắc bén, vàng mười trong tay. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q46" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 7: BẢN ÁN CHO TRÒ MA GIÁO "HACK THUẬT TOÁN"<br>Vẫn miệt mài nhét hàng chục hashtag #xuhuong, giật tít lừa đảo để "hack" đề xuất? Bạn thực sự nghĩ vài dòng code thủ thuật rẻ tiền có thể qua mặt được một cỗ máy đang soi thấu cả khẩu hình miệng của bạn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Sự ngây thơ đến thảm hại! AI cấp 3 không thèm liếc mắt đến hashtag lừa bịp. Nó sử dụng "Thị giác máy tính" quét bối cảnh, "Xử lý ngôn ngữ" bóc băng từng âm tiết bạn thốt ra. Treo đầu dê bán thịt chó chỉ làm gãy vụn Tọa độ Ngữ nghĩa, khiến bạn lập tức bị phong sát vì tội "lừa đảo dữ liệu". Hãy thành thật đến tàn nhẫn, nhả từ khóa chuyên môn bằng chính miệng mình. Lời bạn nói, đồ vật bạn cầm trên tay mới chính là SEO tối thượng!</p>
<blockquote>
<p><em>Mẹo hèn thủ thuật ích chi, <br/>Máy soi từng chữ, giấu gì được đâu. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q47" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 8: SỰ ĐUỐI LÝ CỦA NỘI DUNG "HÀO NHOÁNG, UỐN ÉO"<br>Bỏ chục triệu mua máy quay xịn, thuê mẫu uốn éo mong lọt vào mắt xanh thuật toán. Tại sao một video lộng lẫy như điện ảnh lại bị AI đè bẹp bởi clip quay mờ căm của một gã thợ mộc dính đầy mùn cưa?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì AI mù lòa trước sự hào nhoáng, nhưng thèm khát "Mật độ thông tin" (Information Density)! Bạn uốn éo màu mè nhưng rỗng tuếch, AI lập tức đánh giá đó là "tín hiệu nhiễu" và dìm xuống đáy. Gã thợ mộc quay mờ nhòe nhưng bóc tách đúng điểm yếu chết người của thớ gỗ, lập tức tạo ra tọa độ sắc lẹm, đâm trúng tim đen giới sành chơi. Thẩm mỹ phù phiếm chỉ sinh ra lượt Like dạo, chiều sâu chuyên môn mới tạo ra lệnh chuyển khoản!</p>
<blockquote>
<p><em>Bạc tiền chuốt vẻ bề ngoài, <br/>Bên trong rỗng tuếch, phí hoài công phu. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q48" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 9: CÚ LỘT XÁC SINH TỬ - AI MỚI LÀ SẾP THẬT SỰ?<br>Bạn luôn tự vỗ ngực "tôi làm nội dung để chiều lòng khách hàng". Nhưng sự thật máu lạnh là: Quyền sinh sát video của bạn thuộc về con người hay cỗ máy vô hồn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Khán giả đầu tiên và duy nhất bạn phải quỳ lạy chính là MÁY TÍNH! Đừng ảo tưởng bạn đang giao tiếp trực tiếp với khách hàng. AI là gã gác cổng máu lạnh. Nếu từ khóa bạn nói mờ nhạt, dữ liệu mâu thuẫn, nó sẽ nghiền nát video của bạn trước khi bất kỳ ai kịp thấy. Ngừng làm nội dung cho người xem! Hãy "lập trình dữ liệu" cho AI nuốt, biến cỗ máy thành nhân viên Sale tận tụy, tự động dâng sản phẩm của bạn đến tận tay khách VIP!</p>
<blockquote>
<p><em>Đừng lo nịnh nọt người ta, <br/>Chiều lòng máy móc, hái ra bộn tiền. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q49" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 10: TANG LỄ CỦA QUẢNG CÁO "LÙA GÀ QUANH PHỄU"<br>Tại sao mô hình phễu marketing vạn năng (phủ rộng ➔ hâm nóng ➔ lùa gà ➔ chốt sale) đang mục nát? Vì cớ gì những kẻ vô danh vừa xuất hiện đã chốt đơn giá cao mà chẳng cần mất cả tháng trời rải thính?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì AI đã đập nát chiếc phễu cồng kềnh đó! Mạng xã hội Ngữ nghĩa vận hành như một Sàn khớp lệnh tốc độ cao. Nó bắt sóng chính xác tín hiệu khao khát cấp bách (Micro-intent) của người dùng ở ngay thời điểm hiện tại. Khi Tọa độ chuyên môn của bạn đâm trúng Tọa độ nhu cầu của họ, niềm tin hình thành tức thì dẫu họ mới thấy bạn lần đầu. Vĩnh biệt kỷ nguyên rải phễu lùa gà, bán hàng giờ đây là Khớp lệnh trực tiếp không cần sưởi ấm!</p>
<blockquote>
<p><em>Giăng mưu rải phễu lùa gà, <br/>Khớp ngay tọa độ, tiền ra ầm ầm. </em></p>
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
