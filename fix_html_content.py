import re

content = """<div class="article-content">
  <p class="lead">Hữu Việt — chủ chuỗi salon tóc, đồng thời là nhà phân phối mỹ phẩm sỉ và phát triển App AI quản lý salon. Vấn đề lớn nhất: <b>anh ta giỏi nghề nhưng chưa ai biết đến ngoài khách quen.</b> Kênh cá nhân cần xây từ đầu để chuyển từ "thợ tóc uy tín tại địa phương" sang "chuyên gia quản trị salon có tiếng trên mạng xã hội."</p>

  <blockquote>
    <b>Mục tiêu cuối cùng:</b> Hữu Việt không bán dịch vụ cắt tóc trên mạng. Anh ta bán <b>năng lực quản trị hệ thống salon</b> — gồm SOP vận hành, App AI tính lương/định lượng thuốc, và kênh phân phối mỹ phẩm sỉ. Đối tượng khán giả là <b>các chủ salon khác</b>, không phải khách hàng đi cắt tóc.
  </blockquote>

  <h2>01 / Tại sao Hữu Việt cần kênh</h2>
  <p>Hữu Việt có 3 nguồn thu: chuỗi salon, phân phối mỹ phẩm sỉ, và App AI quản lý. Cả 3 đều bán cho <b>chủ salon</b> — một đối tượng B2B. Nhưng hiện tại anh ta chỉ tiếp cận được khách qua giới thiệu truyền miệng. Kênh mạng xã hội là đòn bẩy duy nhất để mở rộng quy mô mà không cần gặp từng người.</p>
  <ul>
    <li><b>Không có kênh = phụ thuộc giới thiệu.</b> Mỗi tháng chỉ thêm được 2-3 đối tác mới qua quen biết. Muốn mở rộng chuỗi cung ứng mỹ phẩm hay bán App cần hàng trăm chủ salon biết đến.</li>
    <li><b>Có chuyên môn nhưng không chứng minh được.</b> Hữu Việt biết cách tối ưu chi phí thuốc nhuộm, xây SOP, tính lương tự động — nhưng chưa có nội dung nào trên mạng để người lạ xác nhận điều đó.</li>
    <li><b>Đối thủ đang chiếm sóng bằng nội dung rác.</b> Các kênh salon khác đăng video "khoe tay nghề uốn nhuộm" — hướng B2C. Hữu Việt cần chiếm vị trí hoàn toàn khác: người dạy chủ salon cách vận hành.</li>
  </ul>

  <h2>02 / Định vị kênh: Nói về cái gì, nói cho ai</h2>
  <p>Kênh của Hữu Việt không phải kênh làm tóc. Đây là <b>kênh quản trị kinh doanh salon</b> — nhắm vào chủ tiệm đang vật lộn với nhân sự, chi phí và vận hành.</p>
  
  <div class="columns">
    <div class="col col-wrong">
      <h3>❌ Không làm những nội dung này</h3>
      <ul>
        <li>Video khoe kỹ thuật uốn nhuộm đẹp</li>
        <li>Before/After kiểu "mái tóc bồng bềnh"</li>
        <li>Review mỹ phẩm cho người tiêu dùng</li>
        <li>Clip selfie cảm xúc "tâm huyết nghề"</li>
        <li>Nội dung hướng đến khách đi cắt tóc</li>
      </ul>
    </div>
    <div class="col col-right">
      <h3>✅ Chỉ làm những nội dung này</h3>
      <ul>
        <li>Bóc tách chi phí vận hành salon thật</li>
        <li>Cách kiểm soát hao hụt thuốc nhuộm bằng App</li>
        <li>SOP quy trình để salon tự chạy khi chủ vắng</li>
        <li>Mẹo quản lý nhân sự thợ tóc thực tế</li>
        <li>So sánh giá sỉ mỹ phẩm salon minh bạch</li>
      </ul>
    </div>
  </div>

  <blockquote>
    <b>Nguyên tắc sống còn:</b> Mỗi video phải khiến một chủ salon khác xem xong nghĩ: <i>"Ông này hiểu bài toán kinh doanh của mình."</i> — Không phải nghĩ: <i>"Ông này cắt tóc đẹp thật."</i>
  </blockquote>

  <h2>03 / Phong cách nội dung: Quay như phóng viên điều tra</h2>
  <p>Không quay kiểu beauty, không gimbal mượt mà. Hữu Việt quay bằng tay, mic cài áo, xộc thẳng vào hiện trường làm việc. Phong cách giống <b>phóng viên điều tra xộc vào bếp nhà hàng</b> — thô, thật, có bằng chứng cụ thể.</p>
  <ul>
    <li><b>70% B-Roll hiện trường:</b> Cảnh thực tế trong salon: kiểm tra kho thuốc, bắt quả tang thợ pha dư nguyên liệu, mở App AI trên điện thoại cho thấy số liệu thật. Quay cận tay — bát thuốc nhuộm còn dư, vỏ hộp mỹ phẩm trong thùng rác, màn hình bảng lương tự động.</li>
    <li><b>30% Walk & Talk giải thích:</b> Vừa đi dọc salon vừa nói thẳng vào vấn đề. Không ngồi trước camera đọc kịch bản. Giọng điệu như đang nói chuyện riêng với một chủ salon bạn bè — mộc, đanh, có số liệu cụ thể kèm theo.</li>
  </ul>
  
  <blockquote>
    <b>Ví dụ hook mở đầu video:</b><br>
    <i>"Hôm nay tôi ghé một salon đang kêu lỗ. Nhìn bát thuốc nhuộm thợ vừa pha — dư 30 gram. Một ngày 20 khách, bay nửa tuýp thuốc xịn chui xuống cống. SOP không có, định lượng không đo bằng app thì cắt tóc giỏi mấy cuối tháng cũng ăn cám."</i>
  </blockquote>

  <h2>04 / Lộ trình thực thi: 4 bước xây kênh</h2>
  <p>Lộ trình từ con số 0 đến kênh có uy tín trong ngành salon. Mỗi giai đoạn có mục tiêu rõ, không nhảy bước.</p>
  <ol>
    <li><b>Tháng 1-2: Tích lũy bằng chứng (B-Roll không thoại)</b><br>Đăng 3-4 clip ngắn/tuần, mỗi clip 15-30 giây. Chỉ có hình ảnh thực tế trong salon + text overlay ngắn. Cảnh nhập kho mỹ phẩm sỉ, màn hình App AI tính lương, cảnh sửa quy trình cho thợ. Không cần lộ mặt, không cần nói. Mục tiêu: để thuật toán học và khán giả bắt đầu tò mò "ông này làm gì".</li>
    <li><b>Tháng 3-4: Lộ mặt + Walk & Talk ngắn</b><br>Bắt đầu nói trước camera. Video 60-90 giây. Mỗi video giải quyết đúng 1 vấn đề cụ thể mà chủ salon đang gặp: hao hụt thuốc, thợ nghỉ không báo trước, lương thưởng không minh bạch. Hook đầu video đánh thẳng vào túi tiền: <i>"Mỗi tháng anh đang mất 3-5 triệu vì cái này mà không biết."</i></li>
    <li><b>Tháng 5-6: Case study thực tế</b><br>Quay video dài hơn (3-5 phút). Vào thẳng một salon đối tác, bóc tách vấn đề trước camera, đưa ra giải pháp cụ thể bằng App và SOP. Format "bắt quả tang": xộc vào kiểm tra, chỉ ra lỗi, đưa hệ thống vào sửa ngay tại chỗ. Đây là nội dung tạo uy tín mạnh nhất.</li>
    <li><b>Tháng 7+: Chuyển đổi — bán App & dịch vụ tư vấn</b><br>Khi đã có 50-100 video và lượng người theo dõi đủ lớn trong ngành, bắt đầu đặt CTA rõ ràng: dùng thử App AI quản lý salon, đăng ký tư vấn setup SOP, mua mỹ phẩm sỉ từ kênh phân phối. Không bán sớm — bán khi đã có đủ bằng chứng uy tín.</li>
  </ol>

  <h2>05 / Xây niềm tin: Hành động tạo uy tín</h2>
  <p>Nói hay không bằng làm mất lợi ích ngắn hạn để chứng minh uy tín. Đây là những hành động "chịu thiệt" mà Hữu Việt cần ghi lại trên kênh — vì chính chúng tạo niềm tin mạnh hơn mọi lời nói.</p>
  <ul>
    <li><b>Từ chối bán App cho salon không đủ chuẩn:</b> Tuyên bố thẳng trên camera: <i>"Salon không chịu nhập liệu kỷ luật thì mua App về cũng vứt. Tôi không lấy tiền của anh để mang tiếng."</i> — Hành động từ chối tiền chứng minh App có giá trị thật, không phải bán cho ai cũng được.</li>
    <li><b>Cắt đứt đại lý phá giá thị trường:</b> Quay lại cảnh thực tế hủy hợp tác với đại lý mỹ phẩm sỉ bán phá giá. Chấp nhận mất doanh thu ngắn hạn để bảo vệ giá thị trường cho toàn bộ đối tác trong chuỗi. Các chủ salon khác xem clip này sẽ biết: hợp tác với Hữu Việt thì được bảo vệ quyền lợi.</li>
    <li><b>Công khai số liệu thật trên camera:</b> Mở App lên, cho xem bảng chi phí thật, lương thợ thật, tỷ lệ hao hụt thuốc thật. Không giấu, không làm đẹp số liệu. Khi chủ salon khác thấy con số thật, họ tin rằng người này nói thật mọi thứ khác.</li>
  </ul>

  <h2>06 / Sản phẩm: Bán gì qua kênh</h2>
  <p>Kênh không tồn tại để "nổi tiếng". Mỗi video là một bước trong phễu dẫn khách hàng đến 3 sản phẩm cụ thể:</p>
  <ul>
    <li><b>App AI Quản Lý Salon:</b> Tự động tính lương thợ, định lượng thuốc nhuộm theo gram, kiểm soát chi phí vận hành. Video nào cũng nên có ít nhất 1 cảnh mở App lên — tạo thói quen nhận diện sản phẩm.</li>
    <li><b>Phân Phối Mỹ Phẩm Sỉ:</b> Cung cấp thuốc nhuộm, dưỡng, phục hồi cho salon với giá sỉ minh bạch. Nội dung quay cảnh nhập kho, so sánh giá, đánh giá chất lượng sản phẩm — để chủ salon thấy kênh cung ứng đáng tin.</li>
    <li><b>Tư Vấn Setup SOP Salon:</b> Dịch vụ cao cấp nhất: Hữu Việt đến tận nơi, đánh giá salon, xây quy trình vận hành chuẩn để chủ tiệm không cần có mặt mà salon vẫn chạy. Video case study chính là demo miễn phí cho dịch vụ này.</li>
  </ul>

  <hr>
  
  <h2>Tóm tắt: Ghi nhớ 5 điểm</h2>
  <ol>
    <li><b>Đối tượng:</b> Chủ salon, không phải khách cắt tóc. Mọi nội dung phải viết cho người điều hành kinh doanh.</li>
    <li><b>Định vị:</b> Chuyên gia quản trị salon — không phải thợ tóc giỏi. Bán hệ thống, không bán tay nghề.</li>
    <li><b>Phong cách:</b> Phóng viên điều tra — quay tay, thô, thật, có bằng chứng. Không gimbal, không beauty filter.</li>
    <li><b>Lộ trình:</b> B-Roll câm → Walk & Talk ngắn → Case study dài → Chuyển đổi bán hàng. Không nhảy bước.</li>
    <li><b>Uy tín:</b> Xây bằng hành động chịu thiệt — từ chối khách không đủ chuẩn, cắt đứt đối tác phá giá, công khai số liệu thật.</li>
  </ol>
</div>"""

files = ['logickenh-huuviet-pa1.html', 'logickenh-huuviet-pa2.html', 'logickenh-huuviet-pa3.html']

for f in files:
    with open(f, 'r') as file:
        data = file.read()
    
    new_data = re.sub(r'<div class="article-content">.*?</div>\s*</div>\s*</body>', content + '\n\n  </div>\n</body>', data, flags=re.DOTALL)
    
    with open(f, 'w') as file:
        file.write(new_data)
        
print("Updated successfully")
