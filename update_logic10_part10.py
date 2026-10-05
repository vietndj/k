import re

file_path = '/Users/vietmac/Documents/CODE/k/logic10.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_toc_items = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">MÃ NGUỒN BẢN NGÃ (EGO)</li>
<li><a class="ink-toc-link" href="#q67">1. Sự tấn công ráo hoảnh</a></li>
<li><a class="ink-toc-link" href="#q68">2. Tuyệt sát Tính từ</a></li>
<li><a class="ink-toc-link" href="#q69">3. Vi biểu cảm dã thú</a></li>
<li><a class="ink-toc-link" href="#q70">4. Quyền năng hạ mình</a></li>
<li><a class="ink-toc-link" href="#q71">5. Rỗng cốc vô ngã</a></li>
"""

toc_marker = "</ul>\n</aside>"
if toc_marker in content:
    content = content.replace(toc_marker, new_toc_items + "\n" + toc_marker)

new_content = """
<hr style="margin: 4rem 0; border: none; border-top: 1px solid var(--ink-border);"/>
<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase;">PHẦN 7: HỆ THỐNG TRỤC CÂU HỎI & GIẢI PHẪU MÃ NGUỒN BẢN NGÃ (EGO)</h2>
<p>Dưới đây là bản giải phẫu toàn bộ mạch tư duy của bạn, được tái cấu trúc thành những lát cắt sắc lẹm nhất. Trước khi dùng búa tạ đập vỡ các lầm tưởng, tôi xin tái cấu trúc lại 5 tầng trăn trở sâu thẳm mà bạn đã đặt ra:</p>
<ul>
    <li><strong>Nghịch lý của sự tấn công:</strong> Tại sao mỉa mai, phán xét lại kích hoạt màng lọc tự ái khiến người ta đóng não; trong khi thái độ bình thản, lạnh tanh như "bản tin thời tiết" lại ép họ phải nuốt trôi sự thật nhục nhã mà không thể phản kháng?</li>
    <li><strong>Kỹ thuật lột trần sự thật:</strong> Làm thế nào để mô tả một sự thảm hại khách quan như "nước sôi ở 100 độ" (giống cách các đại văn hào áp dụng) để đối phương không nhận ra tín hiệu bị tấn công và không thể bỏ chạy?</li>
    <li><strong>Cảnh giới nội tâm:</strong> Để đạt được sự ráo hoảnh đó, bên trong ta có bắt buộc phải rỗng rang, không phán xét và bao dung tuyệt đối như một nhà sư hay không?</li>
    <li><strong>Quyền năng đập tan phòng thủ của danh xưng:</strong> Tại sao việc tự hạ thấp vai vế (xưng "con" gọi "chú", hay xưng "em" gọi người kém tuổi là "anh/chị") lại khiến lớp khiên tự ái của đối phương lập tức vỡ vụn?</li>
    <li><strong>Sự chuyển hóa tâm thức:</strong> Cơ chế nào khiến việc gỡ bỏ danh xưng "bề trên" không hề làm ta thấy hèn kém, mà ngược lại, đánh thức sự cầu thị, triệt tiêu rào cản và tạo ra kết nối sâu sắc với vạn vật?</li>
</ul>

<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase; margin-top: 4rem;">HỎI XOÁY GÂY SHOCK - GIẢI PHẪU MÃ NGUỒN BẢN NGÃ (EGO)</h2>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q67" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 1: SỰ TẤN CÔNG RÁO HOẢNH<br>Bạn lầm tưởng cứ phải chửi thẳng mặt, mỉa mai cay độc thì kẻ u mê mới chịu tỉnh ngộ? Tại sao sự tấn công trực diện lại là cách ngu ngốc nhất để bóc trần sự thật, trong khi một thái độ ráo hoảnh, lạnh tanh lại thừa sức ép đối phương nuốt trọn chén đắng mà không thể hé răng cãi nửa lời?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bởi Tự ái (Ego) là hệ thống radar chỉ quét "sát khí", không quét "sự thật". Lời mỉa mai là quả tên lửa rực nhiệt, vừa phóng ra đã bị vòm sắt phòng thủ của đối phương đánh chặn. Ngược lại, thái độ lạnh tanh là chiếc phi cơ tàng hình bay ở nhiệt độ không. Khi bạn vạch trần sự thật bằng giọng điệu vô cảm, bạn không tạo ra "lực đẩy" của ác ý. Đối phương vĩnh viễn mất đi điểm tựa để bật lại. Không tìm thấy kẻ thù, bản ngã tê liệt, họ buộc phải mở toang não bộ để thông điệp ghim thẳng vào trong.</p>
<blockquote>
<p><em>Chê bai chuốc lấy cực hình, <br/>Lạnh tanh sự thật, giật mình ngộ ra. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q68" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 2: TUYỆT SÁT TÍNH TỪ<br>Tại sao việc lôi toàn bộ từ ngữ đao to búa lớn ra để lên án một cái xấu lại là sự hạ sách yếu ớt nhất? Thứ ma thuật ngôn từ nào của các đại văn hào có thể biến một nỗi nhục nhã ê chề thành một "định luật vật lý", tước đoạt hoàn toàn quyền chối cãi của nạn nhân?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bí quyết tối thượng là: Tuyệt sát "Tính từ", suy tôn "Động từ". Tính từ (ngu dốt, hèn nhát) là lưỡi dao gí vào cổ, mang nồng nặc mùi phán xét chủ quan của bạn. Còn Động từ là chiếc camera an ninh vô tri chỉ ghi lại hiện thực khách quan. Đừng chê: <em>"Hắn là kẻ hèn hạ"</em>. Hãy tả: <em>"Hắn lảng mắt đi, mặc vội áo khoác và lẳng lặng chuồn mất"</em>. Khi bạn gọt sạch cảm xúc, biến sự thảm hại thành hệ quả sinh học vật lý, nạn nhân không thể chửi lại một "hiện tượng tự nhiên" do chính họ thủ vai.</p>
<blockquote>
<p><em>Tính từ gieo rắc thị phi, <br/>Động từ tĩnh lặng, sân si rụng rời. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q69" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 3: VI BIỂU CẢM CỦA DÃ THÚ<br>Phải chăng ta chỉ cần mài giũa tiểu xảo ngôn từ, đắp một chiếc mặt nạ lạnh lùng là đủ sức thao túng tâm lý kẻ khác? Tại sao nếu nội tâm không thực sự tĩnh lặng và vô ngã như một nhà sư, mọi nỗ lực tỏ ra bình thản đều sẽ bị đối phương cắn xé nát bấy?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Bởi con người là dã thú mang bản năng đánh hơi "vi biểu cảm" (micro-expressions) sắc bén như loài sói ngửi thấy máu. Một cái nhếch mép ly ti, một nhịp thở gắt cũng làm rò rỉ sự khinh miệt giấu giếm trong bụng bạn. Để trở thành một "tấm gương phẳng", bạn phải đập nát lăng kính Đạo đức (phán xét đúng/sai) và đeo lên lăng kính Nhân quả - Sinh học. Khi bạn thấu hiểu kẻ yếu kém giống như một cái cây mọc xiên do thiếu nắng, sự khinh bỉ lập tức tắt ngấm, nhường chỗ cho khoảng không quan sát vô ngã.</p>
<blockquote>
<p><em>Ngụy trang giấu giếm âm thầm, <br/>Thấu nhìn nhân quả, lỗi lầm tiêu tan. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q70" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 4: QUYỀN NĂNG CỦA SỰ HẠ MÌNH<br>Đám đông luôn điên cuồng gồng mình xưng "bề trên" (làm anh, làm sếp) để thị uy và bảo vệ cái tôi. Vậy cơ chế ngược ngạo nào khiến một cú quỳ gối hạ mình, xưng "con" gọi "chú" với người kém tuổi lại mang uy lực tàn độc đến mức bẻ vụn toàn bộ kiêu hãnh của đối phương?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Xưng hô bề trên thực chất là ép đối phương bước vào một trận "kéo co địa vị" ngốn sạch sinh lực. Khi bạn chủ động nhún nhường, bạn đã đột ngột thả tay khỏi đầu dây. Lực kháng cự bằng không, đối phương đang gồng mình bỗng hụt chân rơi tự do vào khoảng không bất trọng lượng. Lớp giáp xù lông của họ bỗng hóa thành trò hề lố bịch, bởi trên đời không một ai điên rồ đến mức vung gươm chém một dòng nước đang tự nguyện chảy về vùng trũng. Tự ái bị phế truất ngay lập tức.</p>
<blockquote>
<p><em>Xưng cao chuốc lấy mây mù, <br/>Buông tay hạ nhún, kẻ thù bơ vơ. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q71" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 5: RỖNG CỐC VÔ NGÃ<br>Tự phế bỏ ngai vàng "bề trên" trước những kẻ kém tuổi mình, phải chăng là hành động tự hạ thấp giá trị bản thân? Thứ quyền năng bí ẩn nào đằng sau sự từ bỏ này lại khiến ta không hề thấy hèn kém, mà ngược lại bừng nở khát khao học hỏi và hòa tan vào vạn vật?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Danh xưng "bề trên" thực chất là một chiếc vương miện bằng sắt giam cầm tâm trí. Nó ép bạn phải tỏ ra hoàn hảo, cấm bạn được sai lầm, cấm bạn cúi xuống nhặt viên ngọc từ tay kẻ khác. Khi bạn chủ động gọi "anh/chị/chú" với người kém tuổi, bạn tự tay đập nát vương miện ấy, "làm rỗng chiếc cốc" của chính mình. Ranh giới Bản ngã bị xóa sổ, giao tiếp không còn là sự va đập đẫm máu của hai Cái Tôi (Ego), mà thăng hoa thành sự giao thoa thuần khiết của hai Linh hồn nơi tọa độ vô ngã.</p>
<blockquote>
<p><em>Ngai vàng mũ sắt nặng nề, <br/>Cúi đầu rỗng cốc, đường về thênh thang. </em></p>
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
