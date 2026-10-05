# -*- coding: utf-8 -*-
"""
build_batch2.py: Tạo episodes_batch2.py chứa 10 tập (OE11 - OE20)
"""
import json

with open('/Users/vietmac/.gemini/antigravity/brain/24deb8b1-3156-43d0-91a1-3246f0cc4078/scratch/omar_40_videos.json') as f:
    raw_vids = {v['idx']: v for v in json.load(f)}

batch2 = [
    # 11. AI Changed Marketing (iYqeUD0dkys)
    {
        "id": raw_vids[11]['id'],
        "slug": "ai-changed-marketing-forever-agencies-dead-podcast.html",
        "ep_code": "OE11",
        "cat_badge": "04 / TRÍ TUỆ NHÂN TẠO & ĐỘT PHÁ NĂNG SUẤT",
        "speaker": "Omar Eltakrori & Chuyên gia Tiếp thị AI",
        "speaker_role": "Giám đốc Chiến lược Tự động hóa & Kiến trúc sư Tiếp thị AI",
        "tagline": "AI TÁI CẤU TRÚC TIẾP THỊ: SỰ SUY TÀN CỦA AGENCY TRUYỀN THỐNG",
        "orig_title": raw_vids[11]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[11]['id']}",
        "publish_date": raw_vids[11]['date'],
        "raw_date": f"{raw_vids[11]['raw_date'][:4]}-{raw_vids[11]['raw_date'][4:6]}-{raw_vids[11]['raw_date'][6:]}",
        "duration": "2 giờ 04 phút",
        "read_time": "~9 phút chắt lọc",
        "hero_quote": "Agency cồng kềnh dần tàn lụi — Solo Creator vững vàng bay",
        "lead_points": [
            "Các agency tiếp thị truyền thống tính phí hàng chục ngàn USD mỗi tháng đang đứng trước nguy cơ sụp đổ vì các công cụ AI thế hệ mới cho phép 1 cá nhân làm được khối lượng việc của cả phòng ban 20 người.",
            "Phân tích sự trỗi dậy của mô hình 'Agency 1 Người' (One-Person AI Agency): Tối ưu hóa chi phí vận hành, cung cấp dịch vụ siêu tốc và tạo ra tỷ suất lợi nhuận trên 90%."
        ],
        "hero_summary": {
            "title": "Bản đồ dịch chuyển từ Agency truyền thống sang Hệ thống Tiếp thị AI",
            "items": [
                ("1. Cái chết của phí duy trì hàng tháng vô nghĩa", "Khách hàng không còn chấp nhận trả $5.000/tháng cho những bản báo cáo PDF sáo rỗng và vài bài post Facebook cơ bản."),
                ("2. Vũ khí của Solo Creator", "Kết hợp tư duy thẩm mỹ con người với tốc độ sản sinh nội dung của AI để tạo ra các chiến dịch tiếp thị cá nhân hóa quy mô lớn."),
                ("3. Mô hình thanh toán theo kết quả (Performance-based)", "Dịch chuyển từ tính phí theo giờ làm việc sang chia sẻ phần trăm doanh thu thực tế mang về cho đối tác.")
            ],
            "mantra": "Máy làm việc mọn thảnh thơi — Người cầm bánh lái sáng ngời tương lai"
        },
        "delusion": {
            "title": "ẢO TƯỞNG CẦN ĐỘI NGŨ ĐÔNG ĐÚC & SỰ THẬT VỀ TỐC ĐỘ TINH GỌN",
            "desc": "Các doanh nghiệp thường tự hào khoe công ty có 50 nhân viên. Nhưng trong thời đại AI, một đội ngũ đông đúc cồng kềnh đồng nghĩa với chi phí quản lý khổng lồ và tốc độ thích ứng chậm như rùa.",
            "compare_left": {
                "badge": "MÔ HÌNH CŨ",
                "title": "Thuê agency truyền thống đông người",
                "text": "Mất 2 tuần họp hành chỉ để duyệt 1 kịch bản video; chi phí quản lý đắt đỏ nuốt trọn ngân sách tiếp thị."
            },
            "compare_right": {
                "badge": "MÔ HÌNH MỚI",
                "title": "Hợp tác với Creator ứng dụng AI",
                "text": "Ra mắt chiến dịch quảng cáo hoàn chỉnh chỉ trong 24 giờ với chi phí bằng 1/10 và độ chuyển đổi cao gấp 3 lần."
            },
            "matrix_title": "So sánh Agency truyền thống và Hệ thống Solo Creator AI",
            "matrix_items": [
                ("Agency truyền thống cồng kềnh", "• Bộ máy quan liêu, qua nhiều tầng duyệt bài khiến nội dung mất hết tính chân thực.<br>• Phụ thuộc nặng nề vào các thủ thuật chạy ads tốn kém."),
                ("Hệ thống Solo Creator AI", "• Trực tiếp làm việc với chuyên gia có năng lực ra quyết định tức thì.<br>• Nội dung mang đậm hơi thở thực chiến và cá tính thương hiệu độc bản.")
            ],
            "mantra": "Đông người lắm chuyện rườm rà — Tinh gọn đòn bẩy một nhà ấm êm"
        },
        "insights": [
            {"num": 1, "meta": "SỤP ĐỔ PHÍ DUY TRÌ", "title": "Thời kỳ thu phí duy trì hàng tháng không cam kết đã kết thúc", "ground_truth": "Doanh nghiệp không còn chấp nhận trả retainer fee mà không thấy rõ doanh thu.", "surface": "Cố gắng thuyết phục khách hàng ký hợp đồng 12 tháng với các chỉ số tương tác ảo.", "nature": "Sự phát triển của AI giúp khách hàng tự kiểm tra được hiệu quả thực tế và phát hiện sự lười biếng của agency.", "leverage": "Chuyển sang mô hình trả phí theo kết quả hoặc đặt cọc thấp kèm % doanh số bán hàng.", "mantra": "Chỉ số ảo tưởng tan tành — Tiền tươi thóc thật đồng hành dài lâu"},
            {"num": 2, "meta": "TỰ ĐỘNG HÓA SẢN XUẤT", "title": "Nhân bản nội dung video bằng AI Avatar và Voice Clone", "ground_truth": "Một chuyên gia có thể xuất hiện trong 30 video mỗi ngày mà không cần trực tiếp quay hình.", "surface": "Ngồi quay từng video ngắn một cách thủ công kiệt sức.", "nature": "Các mô hình nhân bản giọng nói và hình ảnh đã đạt đến độ chân thật 95%, người xem không thể phân biệt.", "leverage": "Quay mẫu 1 lần để tạo Voice Clone, sau đó dùng AI sinh ra hàng loạt video ngắn trả lời khách hàng.", "mantra": "Khuôn hình giọng nói nhân đôi — Lan tỏa giá trị muôn nơi sáng ngời"},
            {"num": 3, "meta": "THẨM MỸ CON NGƯỜI", "title": "Gu thẩm mỹ và sự thấu cảm là rào cản độc quyền cuối cùng", "ground_truth": "Khi ai cũng có quyền truy cập vào cùng một công cụ AI, người có gu thẩm mỹ cao sẽ chiến thắng.", "surface": "Nghĩ rằng chỉ cần biết gõ prompt là trở thành chuyên gia tiếp thị.", "nature": "AI không có trải nghiệm sống, không biết đau đớn hay hạnh phúc; nó chỉ sắp xếp lại dữ liệu cũ.", "leverage": "Đầu tư rèn luyện tư duy điện ảnh, nghệ thuật kể chuyện và sự nhạy cảm văn hóa con người.", "mantra": "Công cụ ai cũng như ai — Gu thẩm mỹ đỉnh mới tài mới vinh"},
            {"num": 4, "meta": "CÁ NHÂN HÓA QUY MÔ LỚN", "title": "Gửi video cá nhân hóa tới từng khách hàng tiềm năng", "ground_truth": "Email có chèn tên khách hàng bằng video riêng có tỷ lệ mở và phản hồi cao hơn 300%.", "surface": "Gửi email hàng loạt vô hồn bằng các phần mềm gửi thư tự động kiểu cũ.", "nature": "Khách hàng cảm thấy được tôn trọng tối đa khi thấy chính chuyên gia gọi đúng tên mình trong video.", "leverage": "Ứng dụng công cụ AI cá nhân hóa để tạo 500 video ngắn gọi tên từng đối tác lớn chỉ trong 1 giờ.", "mantra": "Gọi tên trao gửi ân tình — Khách thương mở cửa kết tình tri giao"},
            {"num": 5, "meta": "TỐC ĐỘ THỰC THI", "title": "24 giờ là tiêu chuẩn vàng mới của ngành tiếp thị", "ground_truth": "Trong thời đại thuật toán cập nhật theo ngày, chiến dịch lên kế hoạch 3 tháng là chiến dịch đã chết.", "surface": "Họp hành qua lại 5 lần để sửa 1 câu slogan tiếp thị.", "nature": "Sự chần chừ làm nguội lạnh ngọn lửa hào hứng và khiến bạn bỏ lỡ thời điểm vàng của xu hướng.", "leverage": "Sáng tạo và chạy thử nghiệm ngay trong ngày; sai đâu sửa đó dựa trên dữ liệu thời gian thực.", "mantra": "Ra quân thần tốc trong ngày — Thị trường đón nhận đổi thay từng giờ"},
            {"num": 6, "meta": "DỮ LIỆU ĐỘC QUYỀN", "title": "Xây dựng hào sâu bảo vệ bằng dữ liệu nội bộ riêng biệt", "ground_truth": "Mô hình AI công cộng chỉ biết những gì cả thế giới đã biết.", "surface": "Dùng ChatGPT nguyên bản mà không nạp thêm bất kỳ dữ liệu thực chiến nào của công ty.", "nature": "Lợi thế cạnh tranh thực sự nằm ở kho dữ liệu lịch sử bán hàng, phản hồi khách hàng và case study độc quyền.", "leverage": "Xây dựng cơ sở tri thức riêng (Vector Database) nạp toàn bộ lịch sử tư vấn và kịch bản thành công của bạn.", "mantra": "Kho vàng tri thức riêng tây — AI học hỏi tháng ngày tinh thông"},
            {"num": 7, "meta": "SOLO CREATOR AGENCY", "title": "Mô hình công ty 1 người tạo doanh thu triệu đô", "ground_truth": "Một cá nhân làm chủ AI có thể vận hành hệ thống tiếp thị tạo ra dòng tiền của một công ty vừa.", "surface": "Nghĩ rằng phải tuyển dụng thật nhiều nhân viên mới là doanh nhân thành đạt.", "nature": "Mỗi nhân sự tuyển vào làm tăng cấp số nhân sự phức tạp trong giao tiếp nội bộ và rủi ro quản trị.", "leverage": "Giữ bộ máy siêu tinh gọn: 1 nhà sáng lập + AI + 2 trợ lý ảo chuyên trách thực thi kỹ thuật.", "mantra": "Một người cầm trịch ung dung — Bạc tiền tích lũy ung dung thanh nhàn"},
            {"num": 8, "meta": "ĐẠO ĐỨC TIẾP THỊ", "title": "Minh bạch trong việc ứng dụng công nghệ trí tuệ nhân tạo", "ground_truth": "Người tiêu dùng sẽ quay lưng vĩnh viễn nếu phát hiện họ bị lừa dối bởi những nội dung giả tạo thiếu đạo đức.", "surface": "Dùng AI tạo ra các lời chứng thực giả hoặc hình ảnh lừa đảo để bán hàng.", "nature": "Lòng tin mất 10 năm để xây dựng nhưng có thể sụp đổ hoàn toàn trong 10 giây.", "leverage": "Công khai cam kết đạo đức: Chỉ dùng AI để gia tăng chất lượng dịch vụ, luôn bảo vệ quyền lợi con người.", "mantra": "Giữ gìn chữ tín làm đầu — Công nghệ soi lối dài lâu vững bền"}
        ],
        "environment": {
            "title": "Thiết lập trạm điều hành tiếp thị AI tự động",
            "items": [
                ("1. Hệ thống máy tính hiệu năng cao với GPU mạnh", "Xử lý kết xuất video và chạy các mô hình AI cục bộ không bị giật lag."),
                ("2. Màn hình cong siêu rộng (Ultrawide Monitor)", "Mở song song bảng điều khiển phân tích quảng cáo, kịch bản video và luồng tự động hóa."),
                ("3. Bảng phân quyền dữ liệu bảo mật", "Thiết lập hệ thống lưu trữ đám mây mã hóa để bảo vệ an toàn tuyệt đối dữ liệu khách hàng.")
            ],
            "mantra": "Màn hình mở rộng thênh thang — Hệ thống tự chạy nhẹ nhàng hanh thông"
        },
        "emotional": {
            "title": "Bản lĩnh của nhà lãnh đạo thời kỳ chuyển dịch công nghệ",
            "items": [
                ("1. Không sợ hãi trước làn sóng AI", "Nhận thức rõ AI là người hầu trung thành giúp bạn giải phóng sức lao động, không phải kẻ thù cướp việc."),
                ("2. Giữ vững ngọn lửa học hỏi mỗi ngày", "Dành 30 phút mỗi sáng để thử nghiệm các tính năng mới mà không mang tâm lý phòng thủ bảo thủ."),
                ("3. Tận hưởng niềm vui của sự sáng tạo thuần khiết", "Khi việc tay chân đã có máy lo, hãy thả lỏng tâm trí để bay bổng với những ý tưởng nghệ thuật lớn.")
            ],
            "mantra": "Tâm không sợ hãi đổi thay — Cưỡi đầu ngọn sóng dựng xây cơ đồ"
        }
    },

    # 12. 99% Businesses Replaced (XezZOMx6q2o)
    {
        "id": raw_vids[12]['id'],
        "slug": "99-percent-online-businesses-replaced-content-podcast.html",
        "ep_code": "OE12",
        "cat_badge": "03 / CHIẾN LƯỢC NỘI DUNG YOUTUBE & VIDEO TRIỆU VIEW",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "99% DOANH NGHIỆP ONLINE SẼ BỊ THAY THẾ BỞI MÔ HÌNH SÁNG TẠO NỘI DUNG NÀY",
        "orig_title": raw_vids[12]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[12]['id']}",
        "publish_date": raw_vids[12]['date'],
        "raw_date": f"{raw_vids[12]['raw_date'][:4]}-{raw_vids[12]['raw_date'][4:6]}-{raw_vids[12]['raw_date'][6:]}",
        "duration": "1 giờ 28 phút",
        "read_time": "~9 phút chắt lọc",
        "hero_quote": "Bán hàng vô cảm lụi tàn — Nội dung chân thật ngập tràn lòng tin",
        "lead_points": [
            "Các website thương mại điện tử và trang bán hàng tĩnh (Static Landing Pages) đang mất dần hiệu lực vì người tiêu dùng ngày nay chỉ mua hàng sau khi đã theo dõi hành trình sáng tạo nội dung của người sáng lập.",
            "Phân tích sự dịch chuyển từ 'Doanh nghiệp có làm nội dung' sang 'Nhà sáng tạo sở hữu doanh nghiệp' (Creator-Led Business): Mô hình kinh doanh có lợi thế cạnh tranh bất khả xâm phạm."
        ],
        "hero_summary": {
            "title": "Bản đồ tiến hóa sang mô hình Doanh nghiệp dẫn dắt bởi Nội dung",
            "items": [
                ("1. Khủng hoảng chú ý và sự tê liệt quảng cáo", "Khách hàng đã phát triển cơ chế mù quảng cáo (Ad Blindness); họ lướt qua mọi banner mời chào lộ liễu."),
                ("2. Nội dung giáo dục mang tính giải trí (Edutainment)", "Mang lại giá trị tri thức thực sự nhưng trình bày bằng phong cách cuốn hút, dễ tiếp cận."),
                ("3. Phễu chuyển đổi dựa trên quan hệ bạn bè", "Biến người theo dõi xa lạ thành những người bạn tâm giao tin tưởng bạn trước khi mua bất kỳ thứ gì.")
            ],
            "mantra": "Quảng cáo lộ liễu người chê — Nội dung sâu sắc khách mê trọn đời"
        },
        "delusion": {
            "title": "ẢO TƯỞNG VỀ WEBSITE BÁN HÀNG TĨNH & SỰ THẬT VỀ DÒNG CHẢY MEDIA",
            "desc": "Nhiều người nghĩ chỉ cần dựng một website thật đẹp rồi bơm tiền chạy ads là tiền tự về. Nhưng thế hệ người tiêu dùng mới chỉ mở ví khi họ cảm nhận được sự hiện diện sống động và cập nhật liên tục của thương hiệu.",
            "compare_left": {
                "badge": "MÔ HÌNH LỖI THỜI",
                "title": "Website tĩnh đóng băng thông tin",
                "text": "Trang web chỉ có thông tin sản phẩm khô khan, không có nội dung mới, không có tương tác người thật."
            },
            "compare_right": {
                "badge": "MÔ HÌNH HIỆN ĐẠI",
                "title": "Hệ sinh thái Media sống động",
                "text": "Mỗi tuần ra mắt video phân tích chuyên môn, bài viết giải mã xu hướng và tương tác trực tiếp với cộng đồng."
            },
            "matrix_title": "So sánh Doanh nghiệp truyền thống và Doanh nghiệp Media-First",
            "matrix_items": [
                ("Doanh nghiệp chỉ bán hàng", "• Chi phí quảng cáo tăng liên tục, lợi nhuận ngày càng teo tóp.<br>• Dễ dàng bị đối thủ sao chép sản phẩm và phá giá."),
                ("Doanh nghiệp Media-First", "• Chi phí quảng cáo tiến về 0 nhờ lượng traffic tự nhiên khổng lồ.<br>• Khách hàng trung thành với cá tính người sáng lập, không đối thủ nào sao chép được.")
            ],
            "mantra": "Website đóng băng lụi tàn — Media sống động ngập tràn niềm vui"
        },
        "insights": [
            {"num": 1, "meta": "CHUYỂN DỊCH QUYỀN LỰC", "title": "Sự thống trị của các doanh nghiệp do Creator dẫn dắt", "ground_truth": "Các thương hiệu như Feastables (MrBeast) hay Prime (Logan Paul) đánh bại các tập đoàn trăm năm tuổi chỉ trong 2 năm.", "surface": "Nghĩ rằng nhà sáng tạo nội dung chỉ là những kẻ làm trò mua vui trên mạng.", "nature": "Sở hữu sự chú ý và lòng tin của hàng triệu người là tài sản kinh doanh tối thượng trong thời đại số.", "leverage": "Biến doanh nghiệp của bạn thành một công ty truyền thông sản xuất nội dung đỉnh cao trong ngành.", "mantra": "Ai nắm chú ý trong tay — Người đó làm chủ tháng ngày tương lai"},
            {"num": 2, "meta": "QUY TẮC 80/20 NỘI DUNG", "title": "80% giá trị miễn phí - 20% lời chào hàng", "ground_truth": "Nếu bạn liên tục bán hàng trong mọi bài đăng, khán giả sẽ hủy theo dõi kênh của bạn.", "surface": "Biến kênh YouTube thành một trang mua sắm truyền hình phát đi phát lại các bài quảng cáo.", "nature": "Quy luật tương hỗ (Reciprocity): Con người khao khát đền đáp khi họ nhận được giá trị lớn mà không bị đòi hỏi.", "leverage": "Cho đi những bí quyết tốt nhất của bạn miễn phí; chỉ thu tiền khi họ cần sự đồng hành cá nhân hóa.", "mantra": "Tám phần cho hết thật tâm — Hai phần khẽ ngỏ khách chăm chỉ mua"},
            {"num": 3, "meta": "TÍNH CHÂN THỰC (AUTHENTICITY)", "title": "Sự vụng về chân thật đánh bại sự hoàn hảo giả tạo", "ground_truth": "Khán giả ngày càng dị ứng với những video quảng cáo bóng bẩy quay tại trường quay đắt đỏ.", "surface": "Thuê diễn viên đóng kịch bản hoàn hảo không tì vết.", "nature": "Sự hoàn hảo tạo ra khoảng cách vô hình; những lỗi vụng về nhỏ và cảm xúc thật mới tạo ra sự đồng cảm.", "leverage": "Quay video bằng điện thoại trong phòng làm việc thực tế, giữ lại những khoảnh khắc tự nhiên không cắt gọt.", "mantra": "Mộc mạc chân thật người thương — Trau chuốt giả tạo ai vương vấn lòng"},
            {"num": 4, "meta": "KỂ CHUYỆN THƯƠNG HIỆU", "title": "Biến hành trình phát triển sản phẩm thành một bộ phim tài liệu", "ground_truth": "Khách hàng muốn tham gia vào quá trình kiến tạo sản phẩm trước khi sản phẩm ra mắt.", "surface": "Giấu kín thông tin cho đến ngày mở bán mới công bố.", "nature": "Tâm lý sở hữu (IKEA Effect): Khách hàng càng chứng kiến nhiều khó khăn bạn vượt qua, họ càng yêu quý sản phẩm.", "leverage": "Quay lại hậu trường những lần thất bại, những đêm thức trắng nghiên cứu và hỏi ý kiến khán giả.", "mantra": "Kể chuyện gian nan đầu đời — Sản phẩm ra mắt vạn người chung vui"},
            {"num": 5, "meta": "ĐỊNH VỊ ĐỘC BẢN", "title": "Tạo ra một danh mục thị trường của riêng bạn (Category of One)", "ground_truth": "Đừng cố gắng trở thành người giỏi nhất trong danh mục cũ; hãy tạo ra danh mục mới nơi bạn là duy nhất.", "surface": "Cạnh tranh trực tiếp với các ông lớn bằng việc giảm giá vài phần trăm.", "nature": "Cạnh tranh giá là cuộc đua xuống đáy nơi không ai có lợi nhuận bền vững.", "leverage": "Kết hợp hai chuyên môn độc đáo (ví dụ: 'Nhiếp ảnh' + 'Tâm lý học bán hàng') để tạo ra lối đi riêng.", "mantra": "Rẽ lối đi riêng thênh thang — Không tranh với kẻ ngang hàng bon chen"},
            {"num": 6, "meta": "TỐI ƯU HÓA PHỄU", "title": "Mỗi video là một cửa ngõ đón khách vào hệ sinh thái", "ground_truth": "Một video YouTube xuất bản hôm nay có thể tiếp tục mang về khách hàng đều đặn sau 5 năm.", "surface": "Chỉ dựa vào bài đăng Facebook biến mất khỏi bảng tin sau 24 giờ.", "nature": "YouTube là công cụ tìm kiếm lớn thứ hai hành tinh; video của bạn có giá trị tích lũy dài hạn như bất động sản.", "leverage": "Tối ưu hóa tiêu đề và từ khóa tìm kiếm cho các video giải quyết vấn đề muôn thuở (Evergreen Content).", "mantra": "Video như đất sinh sôi — Năm năm mười tháng vẫn ngồi hái hoa"},
            {"num": 7, "meta": "XÂY DỰNG BỘ LẠC", "title": "Biến người xem thành những người ủng hộ cuồng nhiệt (Superfans)", "ground_truth": "Bạn chỉ cần 1.000 người hâm mộ đích thực (True Fans) để có cuộc sống tự do tài chính trọn đời.", "surface": "Cố gắng làm hài lòng hàng triệu người xa lạ không quan tâm đến bạn.", "nature": "1.000 người sẵn sàng mua mọi thứ bạn tạo ra có giá trị gấp trăm lần 1 triệu người chỉ bấm like dạo.", "leverage": "Dành thời gian trả lời chi tiết từng bình luận của những khán giả trung thành nhất mỗi tuần.", "mantra": "Nghìn fan tri kỷ sắt son — Nuôi ta no ấm cháu con rạng ngời"},
            {"num": 8, "meta": "TIÊU DIỆT SỰ TRÌ HOÃN", "title": "Bắt đầu làm nội dung ngay hôm nay trước khi quá muộn", "ground_truth": "Trong 3 năm tới, những doanh nghiệp không có kênh truyền thông riêng sẽ bị xóa sổ khỏi thị trường.", "surface": "Chờ đợi đến khi mua đủ máy ảnh đắt tiền và học xong các khóa học mới dám bắt đầu.", "nature": "Khoảng cách giữa bạn và người thành công không phải là tài năng, mà là số lượng video họ đã dám bấm máy.", "leverage": "Cầm chiếc điện thoại thông minh lên, bật chế độ quay và đăng video đầu tiên trong vòng 24 giờ tới.", "mantra": "Đừng chờ hoàn hảo mới làm — Làm đi cho tới khi hoàn hảo sau"}
        ],
        "environment": {
            "title": "Thiết lập studio sản xuất nội dung kiểu phim tài liệu",
            "items": [
                ("1. Đèn nền tạo khối màu sắc (Practical Lights)", "Bố trí đèn bàn cổ điển hoặc dải đèn LED ấm phía sau để tạo chiều sâu điện ảnh cho khung hình."),
                ("2. Micro cài áo không dây Rode Wireless Pro", "Tự do di chuyển trong phòng làm việc mà âm thanh thu vào vẫn rõ nét như trong rạp chiếu phim."),
                ("3. Bảng phân cảnh các câu chuyện đời thực", "Ghi chú các sự kiện và trải nghiệm đáng nhớ trong tuần lên bảng để làm chất liệu kể chuyện.")
            ],
            "mantra": "Góc quay điện ảnh nên thơ — Chuyện đời chân thật từng giờ khắc sâu"
        },
        "emotional": {
            "title": "Nuôi dưỡng sự dũng cảm đối diện với ống kính",
            "items": [
                ("1. Xem ống kính máy quay là một người bạn thân", "Nói chuyện với chiếc máy ảnh như thể bạn đang tâm sự với người bạn tri kỷ ngồi đối diện bên ly cà phê."),
                ("2. Vượt qua nỗi sợ bị chê cười", "Hiểu rằng những người phán xét bạn thường là những người chưa bao giờ dám làm bất cứ điều gì có giá trị."),
                ("3. Tận hưởng niềm vui của sự tiến bộ", "Xem lại video đầu tiên để thấy mình đã trưởng thành và bản lĩnh hơn biết bao nhiêu trên hành trình này.")
            ],
            "mantra": "Máy quay là bạn tâm giao — Trút bầu tâm sự dạt dào yêu thương"
        }
    }
]

# Đọc episodes_batch2.py nếu có hoặc tạo mới
with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch2.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
"""
episodes_batch2.py
Batch 2: 10 Episodes (OE11 - OE20)
"""

BATCH_2 = ''' + json.dumps(batch2, ensure_ascii=False, indent=4) + '\n')

print(f"Đã tạo episodes_batch2.py với {len(batch2)} tập ban đầu (OE11 - OE12)!")
