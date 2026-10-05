import re

file_path = '/Users/vietmac/Documents/CODE/k/logic10.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_toc_items = """
<li><a class="ink-toc-link" href="#q64">5. Bẫy nghiện nội sinh</a></li>
<li><a class="ink-toc-link" href="#q65">6. Ảo tưởng siêu nhiên</a></li>
<li><a class="ink-toc-link" href="#q66">7. Bài toán thực tế</a></li>
"""

toc_marker = "</ul>\n</aside>"
if toc_marker in content:
    content = content.replace(toc_marker, new_toc_items + "\n" + toc_marker)

new_content = """
<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase; margin-top: 4rem;">ĐẬP TAN BẪY TÂM LÝ & ẢO TƯỞNG SIÊU NHIÊN</h2>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q64" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 5: BẪY NGHIỆN NGẬP NỘI SINH<br>Khi đã nếm mùi vị "da đầu nở hoa" và "lơ lửng vô trọng lực", bộ não sinh ra khao khát điên cuồng mỗi lần nhắm mắt. Phải chăng kẻ thực hành thiền đang tự biến mình thành một con nghiện sinh học, dùng sự tĩnh lặng làm liều thuốc phiện để đê mê trốn tránh thực tại? Càng cố đuổi bắt chú bướm ảo giác này, cái bẫy tàn khốc nào đang chờ đợi?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Tuyệt đối chính xác! Sự hỷ lạc bạn trải qua kích hoạt bộ não bơm ra một lượng khổng lồ Dopamine và Endorphin (hormone hạnh phúc). Nếu bạn ngồi xuống chỉ để "chờ đợi" cảm giác đó quay lại, bạn không còn là thiền sinh, mà là một con nghiện đang vã thuốc! Nghịch lý vật lý tàn nhẫn nhất ở đây là: Mong cầu chính là sự kích hoạt tư duy (sóng Beta), nó lập tức làm thùy trán căng thẳng, đánh sập băng thông và "tán xạ" mọi năng lượng. Chú bướm sẽ chết chìm trong chính lòng tham của bạn. Kỷ luật thép của thiền là: Thấy cảnh giới vi diệu nhất cũng phải lạnh lùng lướt qua, tuyệt đối không được phép dừng lại thèm khát!</p>
<blockquote>
<p><em>Niềm vui dẫu tuyệt nhường nào, <br/>Khởi tâm mong đợi rơi vào u mê. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q65" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 6: ẢO TƯỞNG SIÊU NHIÊN<br>Khai mở luân xa, xuất hồn, thần giao cách cảm... Hàng triệu người vịn vào cảm giác rung lắc hay mất trọng lượng cơ thể để huyễn hoặc rằng mình đang kết nối với đấng tối cao hay vũ trụ huyền bí. Có chút sự thật phép màu nào ở đây không, hay đó chỉ là cú lừa vĩ đại của một hệ thần kinh đang tự "hack" chính nó?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Không có thế lực siêu nhiên hay phép thuật kỳ bí nào đang can thiệp cả! Trải nghiệm thần thánh thực chất là một phản ứng cơ học sinh lý: Khi bạn chủ động nhắm mắt, khóa chặt giác quan (cắt đứt dòng dữ liệu ngoại vi), não bộ rơi vào trạng thái "đói thông tin". Bị ép cách ly, nó tự động khuếch đại các xung điện nội bộ, sinh ra ảo giác ánh sáng (hiện tượng phosphenes) và xóa bỏ cảm biến không gian. Gắn mác "thần linh, ma quỷ" cho một cơ chế sinh học thuần túy là sự yếu kém về tư duy logic, biến một công cụ khoa học rèn luyện thần kinh thành mớ mê tín dị đoan rẻ tiền!</p>
<blockquote>
<p><em>Đừng mơ phép lạ cao siêu, <br/>Chỉ là sinh lý xoay chiều mà thôi. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q66" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 7: BÀI TOÁN THỰC TẾ<br>Nếu chỉ để tận hưởng cảm giác êm ái, bất động trong một căn phòng kín vắng lặng, thì thiền định có khác gì một trò chơi vô bổ của những kẻ trốn việc? Đích đến cuối cùng của việc rèn luyện "lõi năng lượng tĩnh lặng" này là gì, khi bạn cởi chân chéo, mở mắt ra và buộc phải đối mặt với một thế giới đầy tiếng ồn, áp lực và sự tàn nhẫn ngoài kia?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Ngồi trong phòng kín tĩnh lặng chỉ là "phòng tập Gym" cho não bộ, cuộc đời ồn ào ngoài kia mới là võ đài thực sự! Đích đến của thiền không phải là biến bạn thành một khúc gỗ vô tri trốn tránh thế sự. Mục đích cốt lõi là rèn luyện cho hệ thần kinh thói quen duy trì "dòng chảy tầng" siêu dẫn bất chấp mọi ngoại cảnh. Để khi đối diện với giông tố ngoài đời thực: thị trường sụp đổ, bị kẻ khác chửi rủa, hay áp lực công việc đè nát... bạn vẫn giữ được nhịp tim bình ổn, không bị "tán xạ" năng lượng bởi cảm xúc sợ hãi hay tức giận. Tĩnh lặng giữa đời thường để tung ra những quyết định sắc lẹm không ma sát – đó mới là uy lực thực dụng tối thượng!</p>
<blockquote>
<p><em>Vào đời đối mặt phong ba, <br/>Tâm không ma sát mới là đỉnh cao. </em></p>
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
