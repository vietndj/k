# -*- coding: utf-8 -*-
"""
build_batch1.py
Tạo tập dữ liệu episodes_batch1.py (Tập OE01 đến OE10)
"""

import json

episodes = [
    # 01. Myron Golden (mLKwGV5ij0E)
    {
        "id": "mLKwGV5ij0E",
        "slug": "myron-golden-first-million-charge-premium-podcast.html",
        "ep_code": "OE01",
        "cat_badge": "01 / ĐÓNG GÓI TRI THỨC & ĐỊNH GIÁ CAO CẤP",
        "speaker": "Myron Golden & Omar Eltakrori",
        "speaker_role": "Chuyên gia Bán hàng & Chiến lược Định giá Cao cấp (High-Ticket Sales)",
        "tagline": "CÔNG THỨC KIẾM 1 TRIỆU USD: ĐỊNH GIÁ CAO CẤP & BÁN BẰNG GIÁ TRỊ",
        "orig_title": "How To Make Your First Million Dollars (Charge A Premium!) ft. Myron Golden",
        "youtube_url": "https://www.youtube.com/watch?v=mLKwGV5ij0E",
        "publish_date": "27/08/2026",
        "raw_date": "2026-08-27",
        "duration": "37 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Bán rẻ mỏi gối người chê — Bán đúng giá trị vỗ về tương lai",
        "lead_points": [
            "Đa số người khởi nghiệp thất bại vì định giá sản phẩm dựa trên chi phí thời gian bỏ ra, thay vì đo lường bằng kết quả đột phá mà khách hàng nhận được.",
            "Myron Golden bóc tách 4 tầng giá trị (Lao động chân tay, Quản lý, Giao tiếp, và Trí tưởng tượng) và chỉ ra con đường duy nhất để chạm mốc 1 triệu USD là bán dịch vụ cao cấp (Premium Offer)."
        ],
        "hero_summary": {
            "title": "Bản đồ chuyển đổi từ bẫy bán rẻ sang vị thế định giá cao cấp",
            "items": [
                ("1. Nghịch lý giá rẻ (The Low-Price Trap)", "Bán rẻ thu hút nhóm khách hàng đòi hỏi khắt khe nhất, tốn nhiều năng lượng hỗ trợ nhất và có tỷ lệ hài lòng thấp nhất."),
                ("2. 4 Tầng giá trị của cải", "Tầng 1 (Cơ bắp) -> Tầng 2 (Điều hành) -> Tầng 3 (Giao tiếp & Đàm phán) -> Tầng 4 (Ý tưởng & Trí tưởng tượng). Thu nhập tăng vọt khi bước lên tầng 3 và 4."),
                ("3. Công thức Premium Offer", "Thay vì bán 1.000 món hàng giá $100, hãy phục vụ 10 khách hàng xuất sắc ở mức $10.000 với cam kết chuyển hóa toàn diện.")
            ],
            "mantra": "Định giá đo bởi tầm nhìn — Khách trao gửi bạc gửi nghìn niềm tin"
        },
        "delusion": {
            "title": "ẢO TƯỞNG CẠNH TRANH GIÁ RẺ & SỰ THẬT VỀ TÂM LÝ KHÁCH HÀNG",
            "desc": "Người mới kinh doanh luôn sợ hãi rằng đặt giá cao sẽ không ai mua. Thực tế tâm lý học hành vi chứng minh: Khách hàng chi trả càng nhiều tiền, họ càng nghiêm túc thực thi và đạt kết quả cao nhất.",
            "compare_left": {
                "badge": "ẢO TƯỞNG ĐÁM ĐÔNG",
                "title": "Hạ giá để thu hút số đông thị trường",
                "text": "Tin rằng giá thấp là lợi thế cạnh tranh cốt lõi, chấp nhận làm việc kiệt sức để bán số lượng lớn cho những người luôn tìm kiếm khuyến mãi."
            },
            "compare_right": {
                "badge": "SỰ THẬT TƯ DUY TRIỆU PHÚ",
                "title": "Định giá cao tạo ra cam kết thực thi tối thượng",
                "text": "Khách hàng đầu tư số tiền lớn sẽ có động lực hành động gấp 10 lần. Phí dịch vụ cao cho phép bạn dồn 100% nguồn lực chăm sóc họ đạt thành công."
            },
            "matrix_title": "Ma trận đối chiếu giữa Khách hàng giá rẻ và Khách hàng Premium",
            "matrix_items": [
                ("Nhóm 1: Khách hàng giá rẻ ($50 - $200)", "• Phàn nàn về mọi chi tiết nhỏ, chậm trễ thực hiện bài tập.<br>• Thường đổ lỗi cho công cụ khi thất bại, tiêu hao 80% năng lượng hỗ trợ."),
                ("Nhóm 2: Khách hàng cao cấp ($3.000 - $25.000)", "• Tự chịu trách nhiệm 100% về kết quả, chủ động tìm giải pháp.<br>• Tôn trọng thời gian chuyên gia, sẵn sàng giới thiệu khách hàng chất lượng tương đương.")
            ],
            "mantra": "Bán rẻ nhọc xác hao tâm — Giá cao chuẩn mực vững tầm uy phong"
        },
        "insights": [
            {
                "num": 1,
                "meta": "4 TẦNG GIÁ TRỊ",
                "title": "4 Cấp độ tạo ra của cải trong nền kinh tế",
                "ground_truth": "95% dân số mắc kẹt ở tầng 1 và 2 nơi thời gian bị đánh đổi tuyến tính với tiền bạc.",
                "surface": "Nỗ lực làm việc 14 tiếng mỗi ngày để hy vọng tăng gấp đôi thu nhập.",
                "nature": "Tầng 1 (Cơ bắp) nhận thù lao thấp nhất. Tầng 4 (Ý tưởng & Kiến trúc hệ thống) tạo ra của cải vô hạn không bị giới hạn bởi giờ làm.",
                "leverage": "Chuyển dịch vai trò từ 'người đi làm thuê quy trình' sang 'kiến trúc sư giải pháp' bằng cách sở hữu sản phẩm trí tuệ.",
                "mantra": "Đổi giờ lấy bạc gian nan — Đổi tài trí tuệ muôn vàn thảnh thơi"
            },
            {
                "num": 2,
                "meta": "TÂM LÝ ĐỊNH GIÁ",
                "title": "Nghịch lý niềm tin trong mắt người mua",
                "ground_truth": "Giá cả chính là tín hiệu chất lượng đầu tiên mà não bộ khách hàng dùng để đánh giá năng lực của bạn.",
                "surface": "Sợ khách chê đắt nên vội vàng giảm giá ngay khi khách ngập ngừng.",
                "nature": "Khi bạn giảm giá quá dễ dàng, khách hàng nghi ngờ giá trị thực tế của giải pháp và cảm thấy bất an.",
                "leverage": "Giữ vững mức giá niêm yết, gia tăng thêm quà tặng chuyển hóa (bonuses) thay vì bớt một xu phí dịch vụ.",
                "mantra": "Giữ giá là giữ uy danh — Bán rẻ tự cắt ngọn ngành lòng tin"
            },
            {
                "num": 3,
                "meta": "ĐÓNG GÓI GIẢI PHÁP",
                "title": "Bán kết quả cuối cùng, không bán thời gian tư vấn",
                "ground_truth": "Khách hàng không bao giờ muốn mua 10 buổi học Zoom; họ muốn mua kết quả doanh nghiệp tăng trưởng hoặc cơ thể giảm 5kg.",
                "surface": "Chào bán gói coaching '10 buổi 60 phút' với danh sách bài giảng dài dòng.",
                "nature": "Khách hàng bận rộn xem các buổi học kéo dài là một gánh nặng thời gian chứ không phải lợi ích.",
                "leverage": "Đóng gói lời chào hàng thành 'Hệ thống đưa doanh thu cán mốc 500 triệu trong 90 ngày' với quy trình rút gọn.",
                "mantra": "Người mua đích đến an lành — Ai mua số buổi loanh quanh đợi chờ"
            },
            {
                "num": 4,
                "meta": "TOÁN HỌC 1 TRIỆU ĐÔ",
                "title": "Bài toán tối ưu hóa nguồn lực chạm mốc 7 con số",
                "ground_truth": "Để có 1 triệu USD: Cần 10.000 người mua món hàng $100, hoặc chỉ cần 100 người mua giải pháp $10.000.",
                "surface": "Tập trung chạy ads ồ ạt để kéo hàng vạn lượt mua ebook hay khóa học giá rẻ.",
                "nature": "Chi phí chăm sóc và duy trì hạ tầng cho 10.000 khách hàng sẽ nuốt trọn biên lợi nhuận của doanh nghiệp.",
                "leverage": "Thiết kế phễu chọn lọc sâu: Chỉ nhận 8–10 khách hàng cao cấp mỗi quý và phục vụ họ với tỷ lệ thành công 100%.",
                "mantra": "Trăm người tri kỷ đồng hành — Hơn vạn khách lạ trôi nhanh qua đường"
            },
            {
                "num": 5,
                "meta": "CHUYỂN HÓA VỊ THẾ",
                "title": "Sự tự tin nội tại quyết định số tiền trên hóa đơn",
                "ground_truth": "Bạn không thể bán một món hàng $10.000 nếu chính bạn chưa từng dám chi $10.000 để đầu tư vào bản thân.",
                "surface": "Học thuộc các bài bản chốt sale nhưng giọng nói vẫn run rẩy khi báo giá.",
                "nature": "Khách hàng cảm nhận được sự bất an và nỗi sợ thiếu thốn của người bán thông qua vi biểu cảm và ngữ điệu.",
                "leverage": "Đầu tư vào những chương trình cố vấn đỉnh cao để trải nghiệm tâm lý của người chi trả lớn, từ đó định hình lại thước đo giá trị.",
                "mantra": "Tâm chưa dám mở hầu bao — Miệng sao dám bảo người trao bạc vàng"
            },
            {
                "num": 6,
                "meta": "LỌC KHÁCH HÀNG",
                "title": "Nghệ thuật sa thải khách hàng độc hại",
                "ground_truth": "20% khách hàng tồi tệ nhất sẽ ngốn 80% thời gian phàn nàn và phá hủy hoàn toàn văn hóa cộng đồng của bạn.",
                "surface": "Cố gắng làm hài lòng tất cả mọi người vì sợ nhận đánh giá tiêu cực.",
                "nature": "Những người chi trả ít nhất thường mang tâm lý nạn nhân và kỳ vọng chuyên gia phải làm thay toàn bộ phần việc của họ.",
                "leverage": "Thiết lập form khảo sát đầu vào: Từ chối phục vụ những người có thái độ tiêu cực hoặc thiếu cam kết hành động.",
                "mantra": "Khách sai từ chối thẳng tay — Giữ cho năng lượng tháng ngày an nhiên"
            },
            {
                "num": 7,
                "meta": "QUY TRÌNH CHỐT SALE",
                "title": "Biến cuộc trò chuyện bán hàng thành buổi chẩn đoán",
                "ground_truth": "Chuyên gia thực thụ đóng vai trò như một bác sĩ phẫu thuật: Lắng nghe triệu chứng, chỉ ra căn nguyên và kê đơn.",
                "surface": "Thao thao bất tuyệt thuyết trình về tính năng sản phẩm suốt 45 phút.",
                "nature": "Người nói càng nhiều càng mất vị thế đàm phán; người đặt câu hỏi thông minh là người nắm quyền điều phối.",
                "leverage": "Dành 80% thời lượng cuộc gọi để đặt câu hỏi tìm hiểu nỗi đau sâu kín và chỉ báo giá trong 5 phút cuối.",
                "mantra": "Lắng nghe thấu suốt nỗi đau — Kê đơn đúng bệnh cùng nhau đổi đời"
            },
            {
                "num": 8,
                "meta": "BẢO VỆ GIÁ TRỊ",
                "title": "Cam kết bảo hành dựa trên hành động thực thi",
                "ground_truth": "Chính sách hoàn tiền vô điều kiện thường bị lợi dụng bởi những kẻ lười biếng muốn tiêu thụ kiến thức miễn phí.",
                "surface": "Hứa hẹn 'hoàn tiền 100% không cần lý do' để khách hàng không ngần ngại quẹt thẻ.",
                "nature": "Cam kết dễ dãi tạo ra tâm lý ỷ lại, khiến học viên không nỗ lực vượt qua những khó khăn ban đầu.",
                "leverage": "Áp dụng 'Bảo hành có điều kiện': Chỉ hỗ trợ thêm nếu học viên chứng minh đã nộp đầy đủ bài tập và thực thi đúng checklist.",
                "mantra": "Học hành phải đổ mồ hôi — Cam kết vững bước đứng ngồi tự tin"
            }
        ],
        "environment": {
            "title": "Thiết lập không gian chốt hợp đồng giá trị cao",
            "items": [
                ("1. Bối cảnh khung hình chuyên nghiệp", "Góc quay tĩnh, ánh sáng 3 điểm rõ nét, phông nền tối giản không bừa bộn để toát lên uy quyền của một chuyên gia."),
                ("2. Môi trường âm thanh chuẩn phát thanh", "Micro condenser bắt âm trầm ấm, loại bỏ tuyệt đối tiếng ồn tạp âm môi trường nhằm tối ưu hóa sự tập trung."),
                ("3. Kịch bản câu hỏi in sẵn trước mặt", "Dán sơ đồ câu hỏi chẩn đoán ngang tầm mắt cạnh webcam để giữ giao tiếp ánh mắt liên tục với đối tác.")
            ],
            "mantra": "Góc quay gọn gàng uy nghi — Âm thanh ấm áp khách ghi vào lòng"
        },
        "emotional": {
            "title": "Luyện tâm thế bình thản trước những con số lớn",
            "items": [
                ("1. Giải phóng nỗi sợ bị từ chối", "Hiểu rằng khách từ chối báo giá là từ chối thời điểm chưa phù hợp của họ, không phải phủ nhận giá trị con người bạn."),
                ("2. Tâm thái dư dả (Abundance Mindset)", "Bước vào cuộc đàm phán với tâm thế sẵn sàng đứng dậy bỏ đi nếu khách hàng không đáp ứng tiêu chuẩn đạo đức."),
                ("3. Tách biệt cảm xúc khỏi số dư tài khoản", "Không để doanh số ngày hôm nay quyết định giá trị bản thân; xem việc bán hàng là sứ mệnh giúp đỡ người khác thoát khổ.")
            ],
            "mantra": "Thong dong tự tại bước vào — Thuận duyên gặt hái chẳng nao núng lòng"
        }
    },

    # 02. Purpose to Rich (3NJqx0R-P_Y)
    {
        "id": "3NJqx0R-P_Y",
        "slug": "how-to-get-rich-living-in-your-purpose-podcast.html",
        "ep_code": "OE02",
        "cat_badge": "01 / ĐÓNG GÓI TRI THỨC & ĐỊNH GIÁ CAO CẤP",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "LÀM GIÀU TỪ SỨ MỆNH: BIẾN CHUYÊN MÔN THÀNH DÒNG TIỀN BỀN VỮNG",
        "orig_title": "How To Get RICH Living in Your Purpose (Works For Any Industry!)",
        "youtube_url": "https://www.youtube.com/watch?v=3NJqx0R-P_Y",
        "publish_date": "13/08/2026",
        "raw_date": "2026-08-13",
        "duration": "1 giờ 16 phút",
        "read_time": "~9 phút chắt lọc",
        "hero_quote": "Sống đúng sứ mệnh đời trao — Tiền tài tự khắc tuôn trào bên ta",
        "lead_points": [
            "Làm giàu không bắt đầu từ việc đuổi theo các trào lưu ngắn hạn, mà bắt nguồn từ điểm giao thoa giữa Nỗi đau bạn từng vượt qua, Kỹ năng độc bản và Nhu cầu thanh toán của thị trường.",
            "Omar Eltakrori hướng dẫn lộ trình 5 bước chuyển hóa trải nghiệm cá nhân thành dịch vụ tư vấn sinh lời, giúp bạn duy trì năng lượng bền bỉ suốt hàng chục năm."
        ],
        "hero_summary": {
            "title": "Hệ thống định vị sứ mệnh cá nhân thành cỗ máy kinh doanh",
            "items": [
                ("1. Vùng giao thoa sứ mệnh (Purpose Sweet Spot)", "Nằm ở nơi nỗi đau quá khứ của bạn trở thành ngọn đèn soi đường cho những người đang gặp khó khăn tương tự."),
                ("2. Kỹ năng kiếm tiền cao (High-Income Skill)", "Gắn chuyên môn kỹ thuật với năng lực giao tiếp, bán hàng và sáng tạo nội dung truyền cảm hứng."),
                ("3. Tính bền vững của động lực", "Động lực từ tiền bạc sẽ cạn kiệt sau 6 tháng; động lực từ sứ mệnh phụng sự giúp bạn kiên trì vượt qua mọi thung lũng thất bại.")
            ],
            "mantra": "Tìm về gốc rễ đam mê — Gieo hạt giá trị gặt về ấm no"
        },
        "delusion": {
            "title": "ẢO TƯỞNG ĐUỔI THEO TREND & BẢN CHẤT SỰ NGHIỆP TRƯỜNG TỒN",
            "desc": "Người trẻ thường liên tục nhảy việc và đổi mô hình kinh doanh theo các xu hướng nóng trên mạng. Nhưng những người giàu bền vững nhất luôn là những người đào sâu vào một chuyên môn duy nhất và gắn liền với sứ mệnh sống.",
            "compare_left": {
                "badge": "ẢO TƯỞNG ĐÁM ĐÔNG",
                "title": "Làm bất cứ thứ gì kiếm ra tiền nhanh nhất",
                "text": "Nhảy từ crypto sang dropshipping, affiliate rồi AI mà không tích lũy được bất kỳ uy tín hay chuyên môn sâu nào."
            },
            "compare_right": {
                "badge": "SỰ THẬT TƯ DUY SỨ MỆNH",
                "title": "Giải quyết một bài toán lớn cho nhóm người cụ thể",
                "text": "Kiên trì phụng sự một thị trường mục tiêu suốt nhiều năm cho đến khi tên tuổi của bạn trở thành bảo chứng duy nhất."
            },
            "matrix_title": "Đối chiếu Động lực bề nổi và Động lực sứ mệnh",
            "matrix_items": [
                ("Chạy theo xu hướng bên ngoài", "• Hưng phấn ban đầu, nhanh chóng chán nản khi gặp trở ngại kỹ thuật.<br>• Luôn cảm thấy trống rỗng và bất an dù tài khoản có tăng thêm tiền."),
                ("Vận hành từ sứ mệnh bên trong", "• Bình thản trước biến động thị trường, coi thử thách là bài học tiến hóa.<br>• Khách hàng trung thành trọn đời vì cảm nhận được ngọn lửa tâm huyết chân thật.")
            ],
            "mantra": "Đua trend mệt xác hoang mang — Bền tâm phụng sự vững vàng tương lai"
        },
        "insights": [
            {
                "num": 1,
                "meta": "ĐỊNH VỊ CỐT LÕI",
                "title": "Nỗi đau quá khứ là tài sản kinh doanh đắt giá nhất",
                "ground_truth": "Bạn được trang bị tốt nhất để giúp đỡ chính con người của bạn trong quá khứ 3 đến 5 năm trước.",
                "surface": "Cố gắng bắt chước chuyên gia hàng đầu và che giấu những thất bại vụng về của mình.",
                "nature": "Khán giả không kết nối với sự hoàn hảo giả tạo; họ chỉ tin tưởng người từng trải qua nỗi đau giống họ và tìm ra lối thoát.",
                "leverage": "Viết lại câu chuyện vượt khó của bản thân thành lộ trình từng bước để hướng dẫn lại cho người đi sau.",
                "mantra": "Vết thương xưa hóa ngọn đèn — Soi đường dẫn lối người quen lối về"
            },
            {
                "num": 2,
                "meta": "LUẬT GIÁ TRỊ",
                "title": "Quy mô thu nhập tỷ lệ thuận với số người bạn giúp đỡ",
                "ground_truth": "Tiền bạc không phải mục tiêu; tiền bạc là thước đo phụ phẩm phản ánh lượng giá trị bạn trao đi cho xã hội.",
                "surface": "Mở mắt ra là nghĩ cách moi tiền từ túi khách hàng bằng các chiêu trò tiếp thị.",
                "nature": "Khách hàng có radar nhạy bén nhận diện sự trục lợi; khi họ cảm thấy bị lợi dụng, họ sẽ rút lui ngay lập tức.",
                "leverage": "Tập trung giải quyết triệt để 1 vấn đề bức xúc của 1.000 người, thu nhập sẽ tự động chảy về như dòng thác.",
                "mantra": "Gieo nhân giúp ích cho người — Tiền tài tự khắc nở mười bông hoa"
            },
            {
                "num": 3,
                "meta": "THUẬT TOÁN DUYÊN NỢ",
                "title": "Xây dựng cộng đồng dựa trên hệ giá trị đạo đức",
                "ground_truth": "Thương hiệu mạnh nhất không được xây dựng trên sản phẩm, mà xây trên niềm tin đạo đức và thế giới quan chung.",
                "surface": "Chỉ đăng tải nội dung quảng cáo giảm giá và kêu gọi bấm link mua hàng.",
                "nature": "Khách hàng mua hàng bằng cảm xúc và bảo chứng giá trị; họ muốn thuộc về một bộ lạc có cùng lý tưởng sống.",
                "leverage": "Dũng cảm tuyên bố rõ ràng những gì bạn ủng hộ và những gì bạn kiên quyết bài trừ trong ngành nghề của mình.",
                "mantra": "Đồng thanh tương ứng chung lòng — Uy danh lan tỏa tựa dòng phù sa"
            },
            {
                "num": 4,
                "meta": "BẪY SO SÁNH",
                "title": "Đừng so sánh chương 1 của mình với chương 20 của người khác",
                "ground_truth": "Mỗi người có một đồng hồ sinh học và hành trình tiến hóa riêng biệt.",
                "surface": "Lướt mạng xã hội thấy đồng nghiệp cùng lứa mua xe, mua nhà rồi tự dằn vặt bản thân.",
                "nature": "So sánh xã hội kích hoạt hạch hạnh nhân gây tê liệt khả năng sáng tạo và hủy hoại sự tự tin.",
                "leverage": "Tắt thông báo của đối thủ, chỉ tập trung cải thiện kỹ năng của mình thêm 1% mỗi ngày so với hôm qua.",
                "mantra": "Đường ta ta vững bước đi — So đo tính toán làm chi nhọc lòng"
            },
            {
                "num": 5,
                "meta": "NĂNG LỰC TẬP TRUNG",
                "title": "Nguyên lý nhát búa thứ 100 phá vỡ tảng đá lớn",
                "ground_truth": "Thành công đột phá là kết quả tích lũy của hàng ngàn hành động nhỏ bé vô danh được lặp lại kiên trì.",
                "surface": "Làm video được 2 tuần chưa thấy nhiều view đã vội vã từ bỏ và tuyên bố kênh flop.",
                "nature": "Mọi thuật toán mạng xã hội đều cần thời gian thu thập dữ liệu để hiểu tệp khán giả phù hợp với bạn.",
                "leverage": "Cam kết xuất bản đều đặn 50 video chất lượng cao mà không cần bận tâm đến lượt xem ban đầu.",
                "mantra": "Chăm chỉ gõ nhát búa sâu — Đá kia cũng vỡ lo âu tan dần"
            },
            {
                "num": 6,
                "meta": "TỰ DO TÀI CHÍNH",
                "title": "Tách biệt giữa giá trị con người và tài sản ngân hàng",
                "ground_truth": "Bạn có giá trị vô điều kiện như một con người, bất kể số dư tài khoản hiện tại là bao nhiêu.",
                "surface": "Cảm thấy tự ti, hèn kém khi gặp người giàu có và kiêu ngạo khi gặp người nghèo hơn.",
                "nature": "Đánh đồng tài sản với phẩm giá khiến tâm thức bạn luôn chao đảo theo từng biến động thị trường.",
                "leverage": "Giữ tâm thái khiêm nhường khi thành công và giữ vững tự trọng khi gặp khó khăn tài chính tạm thời.",
                "mantra": "Bạc tiền chỉ vật ngoài thân — Giữ tâm trong sáng muôn phần quý hơn"
            },
            {
                "num": 7,
                "meta": "TRI THỨC THỰC CHIẾN",
                "title": "Chỉ dạy những gì bạn đã thực sự làm và chứng minh",
                "ground_truth": "Thế giới thừa mứa những kẻ chỉ đọc sách rồi đi rao giảng đạo lý sáo rỗng.",
                "surface": "Tự phong mình là chuyên gia khi bản thân chưa từng tạo ra kết quả thực tế nào trong ngành.",
                "nature": "Sự giả tạo không thể che giấu được lâu; thị trường sẽ nhanh chóng đào thải những người nói không đi đôi với làm.",
                "leverage": "Thực hành trước, ghi chép lại hành trình, đúc rút bài học rồi mới đóng gói thành giáo trình.",
                "mantra": "Làm rồi mới nói đàng hoàng — Người nghe nể phục muôn vàn khắc sâu"
            },
            {
                "num": 8,
                "meta": "DI SẢN TRƯỜNG TỒN",
                "title": "Nghĩ về di sản bạn để lại khi rời khỏi thế giới",
                "ground_truth": "Điều duy nhất còn lại sau khi bạn qua đời là cuộc đời của những người đã tốt lên nhờ có bạn.",
                "surface": "Sống cuộc đời ích kỷ, chỉ lo vun vén của cải cho riêng bản thân.",
                "nature": "Tích lũy của cải không đem lại bình an nội tại nếu thiếu đi cảm giác phụng sự cộng đồng.",
                "leverage": "Dành một phần doanh thu và thời gian mỗi tuần để đào tạo miễn phí cho những người có hoàn cảnh khó khăn.",
                "mantra": "Trăm năm bia đá cũng mòn — Nghìn năm bia miệng vẫn còn trơ trơ"
            }
        ],
        "environment": {
            "title": "Thiết kế không gian kết nối sâu với nội tâm",
            "items": [
                ("1. Bàn làm việc không thiết bị số", "Dành một góc riêng chỉ có sổ tay và bút mực để viết nhật ký phản tư mỗi sáng sớm."),
                ("2. Ánh sáng tự nhiên và cây xanh", "Bố trí bàn làm việc cạnh cửa sổ đón ánh nắng tự nhiên giúp ổn định nhịp sinh học và tâm trạng."),
                ("3. Bảng tầm nhìn sứ mệnh (Vision Board)", "Treo hình ảnh mục tiêu cuộc đời và những người bạn muốn giúp đỡ ngay trước mắt để duy trì cảm hứng.")
            ],
            "mantra": "Góc phòng tĩnh lặng an nhiên — Viết trang nhật ký nối liền ước mơ"
        },
        "emotional": {
            "title": "Duy trì ngọn lửa nhiệt huyết không bị tắt",
            "items": [
                ("1. Thực hành lòng biết ơn hàng ngày", "Mỗi sáng viết ra 3 điều bạn trân trọng trong cuộc sống hiện tại để nuôi dưỡng tâm thức đủ đầy."),
                ("2. Chấp nhận những ngày năng lượng thấp", "Hiểu rằng cơ thể có chu kỳ nghỉ ngơi tự nhiên; cho phép bản thân xả hơi mà không cảm thấy tội lỗi."),
                ("3. Kết nối với những người cùng chí hướng", "Tham gia các vòng tròn kết nối của những người khởi nghiệp tử tế để tiếp thêm năng lượng tích cực.")
            ],
            "mantra": "Biết ơn hiện tại tròn đầy — Bình an bước tiếp từng ngày thảnh thơi"
        }
    }
]

with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch1_data.json', 'w', encoding='utf-8') as f:
    json.dump(episodes, f, ensure_ascii=False, indent=2)
print("Saved 2 sample episodes to episodes_batch1_data.json")
