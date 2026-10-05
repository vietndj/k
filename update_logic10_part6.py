import re

file_path = '/Users/vietmac/Documents/CODE/k/logic10.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_toc_items = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">GIẢI PHÃU TÂM TRÍ</li>
<li><a class="ink-toc-link" href="#q50">1. Công tắc tự sát</a></li>
<li><a class="ink-toc-link" href="#q51">2. Dopamine rẻ tiền</a></li>
<li><a class="ink-toc-link" href="#q52">3. Hố đen cai nghiện</a></li>
<li><a class="ink-toc-link" href="#q53">4. Bình an đích thực</a></li>
"""

toc_marker = "</ul>\n</aside>"
if toc_marker in content:
    content = content.replace(toc_marker, new_toc_items + "\n" + toc_marker)

new_content = """
<hr style="margin: 4rem 0; border: none; border-top: 1px solid var(--ink-border);"/>
<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase;">PHẦN 4: HỆ THỐNG LẠI TÓM TẮT CÂU HỎI & GIẢI PHÃU TÂM TRÍ</h2>
<p>Trước khi đi vào phần giải đáp sắc bén, đây là toàn bộ mạch tư duy và sự đào sâu liên tục mà bạn đã đặt ra:</p>
<ul>
    <li><strong>Bản chất của sự cạn kiệt:</strong> Cơ chế hoạt động của "Hạch hạnh nhân" và "Vỏ não trước trán" diễn ra thế nào (What/Why/How)? Logic phân loại giữa các kích thích não bộ là gì?</li>
    <li><strong>Hố đen của sự cai nghiện:</strong> Quá trình "Tuyệt thực thông tin" diễn ra thực tế ra sao? Giai đoạn giữa có phải là sự chán nản tột độ không, và tại sao nó lại vật vã đến vậy khi não bộ luôn khát kích thích?</li>
    <li><strong>Cú lừa của truyền thông:</strong> "Niềm vui sâu sắc và bình an" dưới góc độ vật lý sinh học và quan sát vi mô thực chất là gì? Tại sao truyền thông dạy rằng vui là phải cười to, nhưng cơ thể lại vận hành theo một cơ chế hoàn toàn ngược lại?</li>
    <li><strong>Đúc kết:</strong> Yêu cầu chuyển hóa toàn bộ kiến thức thành thơ Lục Bát (đã thực hiện) và nay là định dạng Hỏi - Đáp gây shock, đập tan lầm tưởng, kết thúc bằng thơ gieo vần chuẩn xác.</li>
</ul>

<h2 class="is-short" style="font-family: var(--font-display-short); font-weight: 700; text-transform: uppercase; margin-top: 4rem;">GIẢI PHÃU TÂM TRÍ: HỎI ĐÁP ĐẬP TAN LẦM TƯỞNG</h2>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q50" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 1: CÔNG TẮC TỰ SÁT SINH HỌC<br>Bạn nghĩ mình đang giải trí khi hóng drama, nhưng thực chất bạn đang bật "công tắc tự sát" sinh học của chính mình. Tại sao bộ não hiện đại lại ngu ngốc đến mức tự vắt kiệt sức vì những ảo ảnh trên màn hình?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì bộ não của bạn đang mắc kẹt ở thời tiền sử. Hạch hạnh nhân (chiếc còi báo động sinh tồn) hoàn toàn không có khả năng phân biệt giữa một con thú dữ đang lao tới ngoài đời thực và một vụ đánh ghen, chửi rủa trên mạng. Mỗi lần bạn lướt xem drama, não lập tức bật chế độ "Chiến đấu hay Bỏ chạy", rút sạch máu và lượng điện năng quý giá từ Vỏ não trước trán (trung tâm tư duy) để bơm cho các cơ bắp và tuyến hormone. Bạn sập nguồn vì bắt cơ thể phải liên tục "chiến đấu" với những bóng ma vô hình.</p>
<blockquote>
<p><em>Mạng ảo mà ngỡ cọp rừng, <br/>Điện năng rút cạn, nửa chừng sức hao. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q51" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 2: CÁI BẪY DOPAMINE RẺ TIỀN<br>Tại sao cuộn TikTok 15 giây lại dễ dàng hơn việc đọc một trang sách, và tại sao sự "dễ dàng" đó lại là một cú lừa lột sạch tài sản tâm trí của bạn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Đó là cái bẫy chết người của "Dopamine rẻ tiền". Kích thích nhanh, giật gân tạo ra một cú vọt hưng phấn khổng lồ mà không đòi hỏi Vỏ não trước trán phải nỗ lực tư duy. Nó giống như in tiền vô tội vạ gây lạm phát: các thụ thể não của bạn bị "lờn", đòi hỏi những liều lượng độc hại hơn, giật gân hơn để khỏa lấp sự trống rỗng, từ đó vắt kiệt mọi năng lượng dự trữ. Trái lại, Dopamine chậm từ việc khó (đọc sách, tĩnh tâm) bắt não phải làm việc mệt mỏi ban đầu, nhưng lại sinh lời bằng sự thông thái dài hạn.</p>
<blockquote>
<p><em>Rẻ tiền kích thích lướt mau, <br/>Trí tuệ bào mỏng, nát nhàu tâm can. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q52" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 3: ĐỊA NGỤC CAI NGHIỆN THÔNG TIN<br>"Tuyệt thực thông tin" nghe có vẻ thanh cao, nhưng tại sao giai đoạn đầu của nó lại là một địa ngục trống rỗng, chán nản và vật vã đến mức khiến người ta muốn phát điên?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Vì bản chất của quá trình này là Đưa con nghiện vào trại cai. Khi bị cắt nguồn Dopamine rác quen thuộc, bộ não sẽ gào thét phản kháng. Thụ thể Dopamine của bạn đang hỏng, khiến thế giới thực trở nên xám xịt và chậm chạp. Đáng sợ hơn, khi tiếng ồn mạng xã hội tắt đi, mọi công cụ trốn tránh biến mất. Những nỗi đau, lo âu và vi-căng thẳng nội tâm mà bạn cố chôn giấu sẽ lập tức bị phóng đại và nuốt chửng lấy bạn. Đó là sự sụp đổ bắt buộc trước khi hệ thần kinh tái thiết lập được trạng thái cân bằng nội môi.</p>
<blockquote>
<p><em>Cai nghiện vật vã vô cùng, <br/>Vượt qua giông bão, trập trùng bình yên. </em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q53" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ HỎI 4: LỜI NÓI DỐI CỦA TRUYỀN THÔNG VỀ NIỀM VUI<br>Truyền thông nhồi sọ chúng ta rằng "Vui là phải cười to, phải phấn khích tột độ". Lời nói dối này đã tàn phá chúng ta ra sao, và trạng thái bình an đích thực dưới lăng kính vật lý vi mô trông như thế nào?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>Truyền thông bán cho bạn sự "hưng phấn" (Arousal) và gọi nó là niềm vui. Để cười to và phấn khích, cơ thể phải ép tim đập nhanh, bơm Adrenaline, gồng căng hàng chục cơ mặt — một trạng thái tiêu hao điện năng khổng lồ khiến bạn kiệt quệ ngay sau đó. Bình an thực sự là sự "Lược Bỏ": Dây thần kinh phế vị kích hoạt, nhịp phóng điện của não hạ xuống sóng Alpha tĩnh tại, các bó cơ hàm và cơ mày tự động nhả lỏng tạo ra nụ cười hàm tiếu (1-2mm), tiêu cự mắt giãn nở vô thức. Bình an không tốn một giọt năng lượng nào, nó là sự vắng mặt hoàn toàn của mọi điện trở.</p>
<blockquote>
<p><em>Truyền thông dối gạt bao ngày, <br/>Bình an buông xả, nếp mày giãn ra. </em></p>
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
