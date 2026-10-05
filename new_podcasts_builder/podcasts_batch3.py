# -*- coding: utf-8 -*-
"""
podcasts_batch3.py
Batch 3: 6 Episodes (FO498, FO495, FO494, FO481, FO476, FO475)
"""

BATCH_3 = [
    # 14. Prasad Chalavadi (FO498)
    {
        "id": "3dqWCppVKCU",
        "slug": "prasad-chalavadi-retail-brand-scaling-ai-systems-podcast.html",
        "ep_code": "FO498",
        "cat_badge": "14 / HỆ THỐNG BÁN LẺ & CHUYỂN ĐỔI SỐ AI",
        "speaker": "Prasad Chalavadi",
        "speaker_role": "Nhà sáng lập Kalamandir & SSKL / Đế chế bán lẻ dệt may hàng trăm triệu USD",
        "tagline": "TÁI SINH BÁN LẺ TRUYỀN THỐNG BẰNG HỆ THỐNG & AI",
        "orig_title": "How to Build Saree Brand: Strategy, Systems, AI & Profit",
        "youtube_url": "https://www.youtube.com/watch?v=3dqWCppVKCU",
        "duration": "1 giờ 31 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Khăn tơ dệt áo ngàn đời — Đưa vào máy móc sáng ngời tương lai",
        "lead_points": [
            "Làm thế nào một cửa hàng bán sari truyền thống nhỏ bé có thể mở rộng thành chuỗi hơn 50 đại siêu thị và niêm yết thành công trên sàn chứng khoán?",
            "Prasad Chalavadi chia sẻ công thức số hóa ngành nghề thủ công: Chuẩn hóa quy trình mua sắm, ứng dụng camera AI đo lường hành vi khách hàng và tối ưu hóa biên lợi nhuận bằng chuỗi cung ứng khép kín."
        ],
        "hero_summary": {
            "title": "Bản thiết kế chuyển đổi số ngành bán lẻ thủ công",
            "items": [
                ("1. Chuẩn hóa sản phẩm thủ công (Standardization)", "Chuyển từ mua bán cảm tính sang hệ thống gắn mã vạch thông minh, phân loại hoa văn và kiểm soát nguồn gốc sợi dệt."),
                ("2. Ứng dụng AI phân tích luồng nhiệt di chuyển (Heatmap AI)", "Theo dõi chính xác khách hàng dừng lại ngắm mẫu vải nào lâu nhất trong cửa hàng để tự động tối ưu hóa vị trí trưng bày."),
                ("3. Mô hình tài chính IPO minh bạch", "Tách bạch tài chính gia đình khỏi tài chính doanh nghiệp từ ngày đầu để tạo niềm tin cho các quỹ đầu tư tổ chức.")
            ],
            "mantra": "Thủ công kết hợp phần mềm — Cửa hàng truyền thống nở thêm cơ đồ"
        },
        "delusion": {
            "title": "ẢO TƯỞNG KINH DOANH GIA ĐÌNH THEO CẢM TÍNH & HỆ THỐNG HÓA",
            "desc": "Các chủ tiệm truyền thống thường tin vào 'con mắt nhà nghề' và trí nhớ của bản thân. Nhưng bạn không bao giờ có thể mở rộng vượt quá 3 cửa hàng nếu mọi quyết định nhập hàng và định giá đều nằm trong đầu của một ông chủ duy nhất.",
            "compare_left": {
                "badge": "ẢO TƯỞNG ĐÁM ĐÔNG",
                "title": "Kinh doanh dựa vào linh cảm và ghi chép sổ tay",
                "text": "Nhập hàng theo sở thích cá nhân, hàng tồn kho ứ đọng không rõ số liệu, nhân viên tự do bớt giá cho người quen."
            },
            "compare_right": {
                "badge": "HỆ THỐNG BÁN LẺ CHUẨN",
                "title": "Vận hành hoàn toàn bằng dữ liệu ERP thời gian thực",
                "text": "Mỗi chiếc sari có hồ sơ dữ liệu riêng: Tốc độ bán, biên lợi nhuận, sở thích màu sắc theo từng mùa lễ hội."
            },
            "matrix_title": "So sánh giữa Cửa tiệm gia đình và Chuỗi bán lẻ đại chúng",
            "matrix_items": [
                ("Cửa tiệm gia đình manh mún", "• Phụ thuộc 100% vào sự hiện diện của chủ tiệm.<br>• Giới hạn quy mô, không thể tiếp cận nguồn vốn rẻ của thị trường tài chính."),
                ("Đế chế bán lẻ niêm yết (Listed Retail Giant)", "• Vận hành bằng quy trình SOP chuẩn xác, nhân viên mới đào tạo 7 ngày là bán hàng thành thạo.<br>• Dễ dàng huy động hàng trăm triệu USD từ đợt phát hành cổ phiếu IPO.")
            ],
            "mantra": "Cảm tính trói buộc đôi chân — Hệ thống mở lối muôn phần thênh thang"
        },
        "insights": [
            {
                "num": 1,
                "meta": "CHUẨN HÓA THỦ CÔNG",
                "title": "Muốn nhân bản quy mô, phải biến nghệ thuật thành quy trình",
                "ground_truth": "Kalamandir đã phân loại hơn 50.000 mẫu dệt hoa văn truyền thống thành các mã danh mục số hóa chi tiết.",
                "surface": "Tin rằng các mặt hàng may mặc thủ công truyền thống thì không thể chuẩn hóa như đồ điện tử.",
                "nature": "Bất kỳ sự phức tạp nào cũng có thể phân rã thành các thông số kỹ thuật (mật độ sợi, gam màu, hoa văn viền).",
                "leverage": "Xây dựng bảng tiêu chuẩn kiểm tra chất lượng (QC) 10 bước cho từng lô hàng nhập từ làng nghề.",
                "mantra": "Thủ công dẫu lắm hoa văn — Đưa vào quy chuẩn muôn phần dễ sao"
            },
            {
                "num": 2,
                "meta": "AI TRONG RETAIL",
                "title": "Camera AI phát hiện điểm mù trong trải nghiệm mua sắm",
                "ground_truth": "Hệ thống AI nhận diện khách hàng nữ thường bỏ đi nếu phải chờ đợi nhân viên lấy mẫu quá 4 phút tại quầy.",
                "surface": "Chỉ dựa vào phản hồi của nhân viên bán hàng để đánh giá hiệu quả phục vụ của cửa hàng.",
                "nature": "Dữ liệu thị giác khách quan không biết nói dối; nó vạch trần các nút thắt cổ chai trong quy trình vận hành.",
                "leverage": "Tái cấu trúc quầy kệ theo bản đồ nhiệt AI: Đưa các mẫu bán chạy nhất ra khu vực có lưu lượng bước chân cao nhất.",
                "mantra": "Camera soi tỏ lối đi — Chỗ nào tắc nghẽn gỡ đi kịp thời"
            },
            {
                "num": 3,
                "meta": "QUẢN TRỊ NGUỒN CUNG",
                "title": "Cắt bỏ trung gian: Làm việc trực tiếp với người thợ dệt",
                "ground_truth": "Bằng cách tài trợ khung cửi và bao tiêu sản phẩm cho các hợp tác xã làng nghề, Kalamandir cắt giảm 25% chi phí trung gian.",
                "surface": "Mua hàng qua 3-4 tầng thương lái đầu nậu ở chợ đầu mối.",
                "nature": "Khoảng cách giữa bạn và người sản xuất gốc càng xa thì biên lợi nhuận của bạn càng mỏng và chất lượng càng bấp bênh.",
                "leverage": "Thiết lập các trạm thu mua trực tiếp tại làng nghề và thanh toán tiền mặt ngay trong ngày cho thợ thủ công.",
                "mantra": "Về tận làng dệt tìm nguồn — Cắt khâu trung gian nhẹ gánh đường dài"
            },
            {
                "num": 4,
                "meta": "TRẢI NGHIỆM KHÁCH HÀNG",
                "title": "Bán hàng cho phụ nữ: Không khí cửa hàng quyết định ví tiền",
                "ground_truth": "Thời gian lưu lại cửa hàng trung bình của một gia đình mua đồ cưới là 3-4 tiếng; sự thoải mái quyết định giá trị đơn hàng.",
                "surface": "Chỉ quan tâm đến việc nhồi nhét thật nhiều quần áo lên mắc treo cho kín không gian.",
                "nature": "Mua sắm trang phục cưới là sự kiện cảm xúc gia đình; không gian máy lạnh, nước uống miễn phí và ghế ngồi êm ái kích thích mua thêm.",
                "leverage": "Thiết kế khu vực phòng chờ VIP có trà bánh và đồ chơi cho trẻ em để người mẹ yên tâm lựa chọn đồ.",
                "mantra": "Khách ngồi thoải mái thảnh thơi — Hào phóng chi trả nụ cười rạng tươi"
            },
            {
                "num": 5,
                "meta": "CHIẾN LƯỢC ĐA THƯƠNG HIỆU",
                "title": "Mỗi phân khúc khách hàng cần một thương hiệu độc lập",
                "ground_truth": "Tập đoàn tách thành 4 thương hiệu riêng: Kalamandir cho bình dân, Kancheepuram cho đám cưới cao cấp, Brand Mandir cho giới thượng lưu.",
                "surface": "Bày bán đồ giá rẻ và đồ xa xỉ chung trong một cửa hàng dưới cùng một bảng hiệu.",
                "nature": "Khách hàng giàu có sẽ không mua một bộ trang phục 2.000 USD tại nơi người ta đang mặc cả chiếc áo 10 USD.",
                "leverage": "Định vị rạch ròi từng thương hiệu về không gian, bao bì và mức giá để tránh xung đột hình ảnh.",
                "mantra": "Mỗi thương hiệu một tầm nhìn — Sang hèn tách bạch giữ gìn uy danh"
            },
            {
                "num": 6,
                "meta": "TỐI ƯU TỒN KHO",
                "title": "Quy tắc thanh lý hàng tồn sau 90 ngày",
                "ground_truth": "Một mẫu sari nằm trên kệ quá 90 ngày sẽ được chuyển ngay sang kênh xả hàng chiết khấu để thu hồi dòng tiền mặt.",
                "surface": "Tiếc của, giữ khư khư hàng tồn trên kệ với giá niêm yết cũ suốt 2 năm trời.",
                "nature": "Xu hướng thời trang thay đổi theo mùa; chi phí cơ hội của việc giữ hàng tồn đắt hơn nhiều so với việc cắt lỗ 20%.",
                "leverage": "Tự động kích hoạt chương trình giảm giá thanh lý cho mọi SKU chạm mốc 90 ngày tuổi kho.",
                "mantra": "Hàng tồn giữ chặt làm chi — Bán nhanh thu vốn xoay đi kịp thời"
            },
            {
                "num": 7,
                "meta": "MINH BẠCH TÀI CHÍNH",
                "title": "Bỏ túi riêng: Bí quyết chuẩn bị lên sàn chứng khoán",
                "ground_truth": "Prasad đã thuê công ty kiểm toán Big 4 rà soát sổ sách từ khi công ty mới chỉ có 5 cửa hàng.",
                "surface": "Lấy tiền mặt từ két bán hàng của tiệm để chi tiêu việc riêng gia đình mà không ghi chép sổ sách.",
                "nature": "Các tổ chức tài chính định giá doanh nghiệp dựa trên sự minh bạch của dòng tiền; sổ sách mập mờ sẽ bị chiết khấu giá trị thảm hại.",
                "leverage": "Tách bạch 100% tài khoản cá nhân và doanh nghiệp; trả lương cứng cho chính mình như một CEO làm thuê.",
                "mantra": "Tiền nong rành mạch rõ ràng — Sàn chứng khoán đón đàng hoàng vinh quang"
            },
            {
                "num": 8,
                "meta": "LÒNG BIẾT ƠN DI SẢN",
                "title": "Giữ gìn tinh hoa văn hóa dân tộc trong từng thớ vải",
                "ground_truth": "Mỗi bộ sưu tập của Kalamandir đều kèm theo câu chuyện lịch sử về làng nghề dệt thủ công hàng trăm năm tuổi.",
                "surface": "Xem sản phẩm chỉ là món hàng mua đi bán lại kiếm chênh lệch lợi nhuận thuần túy.",
                "nature": "Khách hàng hiện đại mua câu chuyện bản sắc và sự tự hào văn hóa chứ không chỉ mua một tấm vải.",
                "leverage": "Vinh danh tên tuổi của các nghệ nhân dệt may lên thẻ bài sản phẩm để tôn vinh giá trị lao động sáng tạo.",
                "mantra": "Thớ vải dệt mối tâm tình — Tự hào bản sắc nước mình ngàn năm"
            }
        ],
        "environment": {
            "title": "Thiết lập hệ thống vận hành siêu thị bán lẻ chuẩn hóa",
            "items": [
                ("Hệ thống kiểm kê mã vạch RFID tự động", "Sử dụng đầu đọc RFID cầm tay quét toàn bộ 5.000 sản phẩm trong cửa hàng chỉ trong 30 phút vào mỗi buổi sáng."),
                ("Hệ thống chiếu sáng quang học chuyên dụng", "Sử dụng bóng đèn LED có chỉ số hoàn màu CRI > 95 để tôn vinh màu sắc chân thực nhất của sợi tơ lụa tự nhiên.")
            ],
            "mantra": "Mã vạch quét khắp gian hàng — Ánh đèn tỏa sáng sắc vàng lụa tơ"
        },
        "emotional": {
            "title": "Giữ vững sự điềm tĩnh và khiêm nhường khi doanh nghiệp bùng nổ",
            "items": [
                ("Không để vinh quang IPO làm mờ mắt mục tiêu phục vụ khách hàng", "Thường xuyên ghé thăm cửa hàng vào cuối tuần để trò chuyện trực tiếp với khách hàng như những ngày đầu khởi nghiệp."),
                ("Tôn trọng sự cống hiến của những nhân viên gắn bó từ thời gian khó", "Chia sẻ cổ phần và chính sách phúc lợi xứng đáng cho những cộng sự trung thành.")
            ],
            "mantra": "Lên đỉnh vẫn nhớ gốc xưa — Khách hàng là gốc sớm trưa phụng thờ"
        }
    },

    # 15. Ankur Warikoo (FO495)
    {
        "id": "vFrkf8WyJVc",
        "slug": "ankur-warikoo-fake-life-money-psychology-podcast.html",
        "ep_code": "FO495",
        "cat_badge": "15 / TÂM LÝ HỌC TIỀN BẠC & THỰC TẾ CUỘC ĐỜI",
        "speaker": "Ankur Warikoo",
        "speaker_role": "Doanh nhân Khởi nghiệp, Tác giả Best-seller (Do Epic Shit) & Nhà giáo dục Tài chính",
        "tagline": "BẪY SỐNG ẢO, ÁP LỰC XÃ HỘI & TỰ DO TÀI CHÍNH",
        "orig_title": "Ankur Warikoo on People Living a Fake Life, Societal Pressure & Staying Poor",
        "youtube_url": "https://www.youtube.com/watch?v=vFrkf8WyJVc",
        "duration": "1 giờ 38 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Tiêu tiền mua sự phô trương — Hóa ra tự nhốt vào đường cùng túng",
        "lead_points": [
            "Hàng triệu người trẻ trung lưu đang nghèo đi mỗi ngày vì cố gắng mua những thứ họ không cần, bằng số tiền họ không có, để gây ấn tượng với những người họ không hề thích.",
            "Ankur Warikoo bóc trần những bẫy tâm lý tài chính phổ biến nhất: Ảo tưởng mua nhà trả góp quá sớm, bẫy tín dụng tiêu dùng và công thức xây dựng sự giàu có bền vững thông qua việc sống dưới mức thu nhập."
        ],
        "hero_summary": {
            "title": "Bản đồ giải phóng tài chính và thoát bẫy sống ảo",
            "items": [
                ("1. Phân biệt Tài sản thực (Assets) và Biểu tượng địa vị (Status Symbols)", "Người giàu thực sự mua tài sản sinh dòng tiền; người nghèo giả giàu mua những món đồ tiêu sản hào nhoáng để khoe mẽ."),
                ("2. Sự tàn phá của lãi suất kép ngược (Compound Debt)", "Thẻ tín dụng và các khoản vay mua điện thoại, xe hơi trả góp là chiếc máy xay nghiền nát tự do tương lai của bạn."),
                ("3. Công thức đầu tư đơn giản nhất: Tự động hóa quỹ chỉ số", "Dành 20-30% thu nhập đầu tư đều đặn vào Index Funds mỗi tháng mà không cần dự đoán thị trường chứng khoán.")
            ],
            "mantra": "Bỏ bớt phô trương bề ngoài — Giữ lấy tự do tháng ngày thảnh thơi"
        },
        "delusion": {
            "title": "ẢO TƯỞNG AN CƯ LẬP NGHIỆP BẰNG NỢ & SỰ THẬT TỰ DO",
            "desc": "Xã hội nhồi sọ thanh niên 25 tuổi rằng phải vay nợ ngân hàng 20 năm để mua một căn chung cư mới là người thành đạt và có trách nhiệm. Thực tế khoản nợ khổng lồ đó biến bạn thành một người nô lệ không dám nhảy việc, không dám khởi nghiệp hay mạo hiểm.",
            "compare_left": {
                "badge": "ÁP LỰC XÃ HỘI",
                "title": "Cố gắng mua nhà xe bằng mọi giá trước tuổi 30",
                "text": "Dành 60% lương hàng tháng trả lãi ngân hàng, sống trong căng thẳng lo sợ bị mất việc từng ngày."
            },
            "compare_right": {
                "badge": "TỰ DO TÀI CHÍNH",
                "title": "Thuê nhà linh hoạt và đầu tư toàn bộ vốn vào tài sản sinh lời",
                "text": "Giữ dòng tiền thanh khoản cao, sẵn sàng chuyển nơi ở theo cơ hội nghề nghiệp tốt nhất."
            },
            "matrix_title": "So sánh giữa Người nghèo sống ảo và Người giàu ẩn dật",
            "matrix_items": [
                ("Người nghèo sống ảo (Fake Rich)", "• Đi xe sang trả góp, dùng iPhone đời mới nhất nhưng số dư tài khoản dưới 10 triệu đồng.<br>• Phụ thuộc vào từng kỳ lương, khủng hoảng tột độ nếu công ty chậm trả lương."),
                ("Người giàu ẩn dật (Stealth Wealth)", "• Mặc áo phông giản dị, đi xe phổ thông nhưng sở hữu danh mục đầu tư hàng triệu USD.<br>• Tự do tuyệt đối về thời gian, có thể nghỉ việc bất kỳ lúc nào mà không lo thiếu tiền sống.")
            ],
            "mantra": "Nhà to xe đẹp nợ mang — Bằng sao thanh thản nhẹ nhàng túi sâu"
        },
        "insights": [
            {
                "num": 1,
                "meta": "BẪY CHI TIÊU ĐỊA VỊ",
                "title": "Bạn không nghèo vì lương thấp, bạn nghèo vì muốn trông có vẻ giàu",
                "ground_truth": "Phần lớn số tiền tăng thêm sau mỗi đợt thăng chức đều bị nuốt chửng bởi việc nâng cấp phong cách sống (Lifestyle Inflation).",
                "surface": "Nghĩ rằng khi lương tăng từ 15 triệu lên 30 triệu thì đương nhiên phải đổi điện thoại và ăn nhà hàng sang trọng hơn.",
                "nature": "Ham muốn được công nhận địa vị xã hội là chiếc hố không đáy; nâng cấp tiêu dùng không bao giờ mang lại sự thỏa mãn vĩnh viễn.",
                "leverage": "Đóng băng mức sống: Khi được tăng lương, hãy chuyển ngay 80% số tiền tăng thêm vào tài khoản đầu tư tự động.",
                "mantra": "Lương tăng mức sống giữ nguyên — Khoản dư đầu tư bình yên sau này"
            },
            {
                "num": 2,
                "meta": "BẪY MUA NHÀ SỚM",
                "title": "Mua nhà trả góp 20 năm khi còn trẻ là xiềng xích tài chính",
                "ground_truth": "Lãi suất ngân hàng kép trong 20 năm khiến bạn phải trả số tiền gấp 2.5 lần giá trị thực của căn nhà.",
                "surface": "Nghe lời cha mẹ rằng 'tiền thuê nhà là tiền ném qua cửa sổ, mua nhà mới là tài sản tích lũy'.",
                "nature": "Ở tuổi 25-35, giá trị lớn nhất của bạn là sự linh hoạt địa lý để theo đuổi các cơ hội tăng trưởng thu nhập bứt phá.",
                "leverage": "Thuê nhà gần nơi làm việc để tiết kiệm 2 tiếng di chuyển mỗi ngày, dùng thời gian đó học kỹ năng tăng thu nhập.",
                "mantra": "Nợ nhà hai chục năm ròng — Trói chân buộc gót sao mong vẫy vùng"
            },
            {
                "num": 3,
                "meta": "SỰ NGUY HIỂM CỦA THẺ TÍN DỤNG",
                "title": "Thẻ tín dụng được thiết kế để gây tê liệt nỗi đau trả tiền",
                "ground_truth": "Nghiên cứu hành vi chứng minh quẹt thẻ tín dụng khiến người ta chi tiêu nhiều hơn 30% so với việc đếm tiền mặt trả tay.",
                "surface": "Tận dụng các chương trình hoàn tiền 1% và tích điểm dặm bay để biện minh cho việc quẹt thẻ liên tục.",
                "nature": "Khoảng cách thời gian giữa việc nhận hàng và ngày trả nợ làm mất đi phản xạ cảnh giác tự nhiên của não bộ.",
                "leverage": "Hủy toàn bộ thẻ tín dụng hạn mức cao; chỉ sử dụng thẻ ghi nợ (Debit Card) có số tiền định mức hàng tháng.",
                "mantra": "Quẹt thẻ tay nhẹ tênh tênh — Đến ngày thanh toán giật mình nợ sâu"
            },
            {
                "num": 4,
                "meta": "QUỸ DỰ PHÒNG KHẨN CẤP",
                "title": "6 tháng chi phí sinh hoạt gửi tiết kiệm: Liều thuốc an thần tốt nhất",
                "ground_truth": "Người không có quỹ dự phòng khẩn cấp sẽ buộc phải chấp nhận làm công việc tồi tệ hoặc vay nợ lãi cao khi biến cố xảy ra.",
                "surface": "Đem toàn bộ tiền đi đánh chứng khoán hoặc tiền ảo vì chê lãi suất tiết kiệm ngân hàng quá thấp.",
                "nature": "Quỹ khẩn cấp không phải là công cụ làm giàu; nó là tấm đệm sinh tồn bảo vệ bạn khỏi những quyết định tuyệt vọng.",
                "leverage": "Tích lũy đủ 6 tháng chi phí sinh hoạt tối thiểu trong tài khoản ngân hàng riêng biệt trước khi bắt đầu đầu tư mạo hiểm.",
                "mantra": "Sáu tháng sinh hoạt sẵn sàng — Bão giông ập đến vững vàng vượt qua"
            },
            {
                "num": 5,
                "meta": "LÃI KÉP THỜI GIAN",
                "title": "Bắt đầu đầu tư ở tuổi 20 quan trọng gấp 10 lần số tiền bạn có",
                "ground_truth": "Một người đầu tư 1 triệu mỗi tháng từ năm 20 tuổi sẽ giàu hơn người đầu tư 5 triệu mỗi tháng từ năm 35 tuổi.",
                "surface": "Nghĩ rằng 'bây giờ lương ít quá để dành vài trăm ngàn cũng chẳng bõ, đợi khi nào lương cao rồi mới tiết kiệm'.",
                "nature": "Phương trình lãi kép số mũ phụ thuộc lớn nhất vào biến số thời gian (Time in market), không phải số tiền ban đầu.",
                "leverage": "Bắt đầu trích 500.000 đồng mua chứng chỉ quỹ mở ngay trong tháng này để tạo thói quen đầu tư suốt đời.",
                "mantra": "Cây non gieo sớm lớn nhanh — Thời gian tích lũy kết thành rừng cây"
            },
            {
                "num": 6,
                "meta": "ÁP LỰC ĐÁM ĐÔNG",
                "title": "Hầu hết bạn bè bạn không thực sự quan tâm bạn đi xe gì",
                "ground_truth": "Người ta chỉ nhìn chiếc xe của bạn trong 5 giây và ngay lập tức quay lại nghĩ về những bất an của chính họ.",
                "surface": "Vay mượn mua xe hơi đắt tiền để chứng minh bản thân thành đạt trong buổi họp lớp hàng năm.",
                "nature": "Hiệu ứng tâm lý ánh đèn sân khấu (Spotlight Effect) khiến chúng ta phóng đại mức độ chú ý của xã hội đối với mình.",
                "leverage": "Nhắc nhở bản thân: 'Không ai quan tâm đến đồ đạc của mình nhiều như mình nghĩ đâu'.",
                "mantra": "Đèn sân khấu chiếu hư vô — Người ta bận rộn chẳng mồ ngắm ta"
            },
            {
                "num": 7,
                "meta": "TỰ DO TUYỆT ĐỐI",
                "title": "Định nghĩa giàu có thực sự: Quyền năng kiểm soát thời gian",
                "ground_truth": "Một triệu phú làm việc 80 tiếng mỗi tuần trong căng thẳng không giàu bằng một người có thu nhập vừa đủ nhưng được làm chủ 100% thời gian.",
                "surface": "Đo lường sự giàu có bằng số lượng bất động sản và các món đồ trang sức trên người.",
                "nature": "Mục đích tối thượng của tiền bạc là mua lại thời gian tự do để bạn được thức dậy và làm những gì mình muốn với người mình yêu.",
                "leverage": "Tính toán chỉ số độc lập tài chính (Số tiền chi tiêu hàng năm nhân với 25) để biết rõ cột mốc tự do của bạn.",
                "mantra": "Tiền là phương tiện đổi đời — Tự do làm chủ tháng ngày mới sang"
            },
            {
                "num": 8,
                "meta": "BẢN LĨNH TỪ CHỐI",
                "title": "Dám sống cuộc đời bình thường để có tương lai phi thường",
                "ground_truth": "Những người đạt tự do tài chính ở tuổi 40 đều từng bị bạn bè coi là 'kẻ lập dị và keo kiệt' trong suốt những năm tuổi 20.",
                "surface": "Sợ bị bạn bè xa lánh nếu từ chối các cuộc ăn chơi tốn kém vượt quá khả năng tài chính.",
                "nature": "Bạn không thể vừa có kết quả khác biệt đám đông lại vừa muốn nhận được sự đồng thuận của đám đông.",
                "leverage": "Dũng cảm mỉm cười nói: 'Khoản chi đó không nằm trong kế hoạch tài chính của tôi hiện nay'.",
                "mantra": "Khác người một thuở thanh xuân — Về già ung dung an nhàn tấm thân"
            }
        ],
        "environment": {
            "title": "Thiết lập môi trường thanh lọc cám dỗ chi tiêu bốc đồng",
            "items": [
                ("Gỡ bỏ toàn bộ thẻ ngân hàng đã lưu trên các ứng dụng mua sắm trực tuyến", "Mỗi khi muốn mua hàng, bắt buộc phải nhập lại số thẻ thủ công để tạo ra 2 phút suy nghĩ lại xem món đồ có thực sự cần thiết không."),
                ("Quy tắc 72 giờ trước khi mua bất kỳ món đồ không thiết yếu", "Ghi món đồ muốn mua vào sổ tay; nếu sau 3 ngày bạn vẫn còn cảm thấy cần thiết thì mới quyết định mua.")
            ],
            "mantra": "Ba ngày ngẫm nghĩ suy tư — Món đồ cần thiết mới từ tốn mua"
        },
        "emotional": {
            "title": "Duy trì sự bình an nội tại trước cuộc đua địa vị",
            "items": [
                ("Không tìm kiếm sự công nhận từ những người bạn không tôn trọng", "Nhận thức rõ những lời trầm trồ trên mạng xã hội không giúp bạn trả viện phí hay nuôi dạy con cái sau này."),
                ("Tìm thấy niềm vui trong những trải nghiệm giản dị miễn phí", "Đi bộ cùng người thân, đọc sách hay ngồi ngắm hoàng hôn mang lại dopamine bền vững hơn mọi chuyến mua sắm xa xỉ.")
            ],
            "mantra": "Trầm trồ ảo ảnh qua mau — Bình an thanh thản trước sau vẹn toàn"
        }
    }
]

print(f"Loaded {len(BATCH_3)} episodes in batch 3 (part 1).")

# 16. Suyash Saraf (FO494)
BATCH_3.append({
    "id": "q1hvfs-VL5U",
    "slug": "suyash-saraf-d2c-branding-gen-z-marketing-podcast.html",
    "ep_code": "FO494",
    "cat_badge": "16 / XÂY DỰNG THƯƠNG HIỆU D2C & TIẾP THỊ GEN Z",
    "speaker": "Suyash Saraf",
    "speaker_role": "Đồng sáng lập Dot & Key Skincare / Thương hiệu D2C định giá hàng trăm triệu USD",
    "tagline": "CHIẾN LƯỢC XÂY DỰNG THƯƠNG HIỆU D2C TRIỆU ĐÔ",
    "orig_title": "How to Build a Big Brand: Gen Z, Packaging & Influencer Marketing",
    "youtube_url": "https://www.youtube.com/watch?v=q1hvfs-VL5U",
    "duration": "1 giờ 30 phút",
    "read_time": "~8 phút chắt lọc",
    "hero_quote": "Bao bì bắt mắt chạm tim — Chất lượng giữ khách mới tìm thành công",
    "lead_points": [
        "Làm thế nào một thương hiệu mỹ phẩm khởi nghiệp có thể đánh bại các gã khổng lồ FMCG đa quốc gia trên kệ hàng số để được tập đoàn Nykaa thâu tóm với giá trị khổng lồ?",
        "Suyash Saraf bóc tách công thức D2C hiện đại: Sức mạnh của thiết kế bao bì 'Instagrammable', nghệ thuật làm việc với hàng ngàn Micro-Influencer và công thức tối ưu hóa chỉ số LTV/CAC trong thương mại điện tử."
    ],
    "hero_summary": {
        "title": "Bản thiết kế thương hiệu D2C tốc độ cao thời đại số",
        "items": [
            ("1. Đột phá bao bì giác quan (Sensory Packaging)", "Thiết kế hũ mỹ phẩm không chỉ để đựng kem mà phải tạo cảm giác muốn chạm vào và chụp ảnh khoe lên mạng xã hội ngay khi đập hộp."),
            ("2. Tiếp thị qua mạng lưới Micro-Influencer chân thực", "Thay vì chi triệu USD cho ngôi sao điện ảnh xa vời, phân bổ ngân sách cho hàng ngàn người dùng thật chia sẻ trải nghiệm không màu mè."),
            ("3. Quản trị chỉ số kinh tế đơn vị (Unit Economics)", "Chi phí thu hút khách hàng (CAC) liên tục tăng; chìa khóa sống còn là tỷ lệ khách hàng mua lại lần 2 và lần 3 (Repeat Rate).")
        ],
        "mantra": "Bao bì mở lối trao tay — Khách mua lần nữa đong đầy thành công"
    },
    "delusion": {
        "title": "ẢO TƯỞNG ĐỐT TIỀN QUẢNG CÁO FACEBOOK & BẢN CHẤT SẢN PHẨM CỐT LÕI",
        "desc": "Nhiều người khởi nghiệp thương mại điện tử nghĩ chỉ cần biết chạy ads Facebook giỏi là có thể xây dựng thương hiệu triệu đô. Nhưng quảng cáo chỉ mang lại đơn hàng đầu tiên; nếu chất lượng sản phẩm tồi tệ, bạn sẽ phá sản ngay khi chi phí quảng cáo tăng vọt.",
        "compare_left": {
            "badge": "ẢO TƯỞNG ĐÁM ĐÔNG",
            "title": "Bán hàng theo trào lưu 'Ăn xổi ở thì'",
            "text": "Nhập hàng trôi nổi giá rẻ, chạy quảng cáo giật gân thu tiền một lần rồi bỏ mặc khách hàng chịu hậu quả."
        },
        "compare_right": {
            "badge": "XÂY DỰNG THƯƠNG HIỆU THỰC",
            "title": "Đầu tư nghiêm túc vào công thức R&D độc quyền",
            "text": "Mất hàng tháng thử nghiệm lâm sàng để sản phẩm mang lại hiệu quả thấy rõ trên da trong 14 ngày, tạo nên sự truyền miệng tự nhiên."
        },
        "matrix_title": "So sánh giữa Người chạy Ads bán hàng và Người xây Thương hiệu",
        "matrix_items": [
            ("Người chạy Ads bán hàng (Dropshipper)", "• Tắt quảng cáo là doanh số về con số 0.<br>• Không có tài sản vô hình, khách hàng không nhớ tên thương hiệu."),
            ("Nhà sáng lập thương hiệu D2C (Brand Builder)", "• Khách hàng chủ động gõ tên thương hiệu lên thanh tìm kiếm Google và sàn TMĐT.<br>• Doanh nghiệp được định giá theo cấp số nhân khi bán lại cho các tập đoàn lớn.")
        ],
        "mantra": "Đốt tiền quảng cáo qua mau — Xây dựng thương hiệu trước sau vững bền"
    },
    "insights": [
        {
            "num": 1,
            "meta": "THIẾT KẾ BAO BÌ",
            "title": "Bao bì là nhân viên bán hàng im lặng hiệu quả nhất",
            "ground_truth": "Dot & Key chi gấp 2.5 lần chi phí trung bình ngành cho việc đúc khuôn chai lọ có hình dáng bo tròn và màu pastel độc bản.",
            "surface": "Dùng chai lọ gia công sẵn đại trà trên thị trường để tiết kiệm chi phí ban đầu.",
            "nature": "Khách hàng đưa ra quyết định mua hàng trên mạng xã hội dựa trên 3 giây đầu tiên nhìn thấy hình ảnh thị giác.",
            "leverage": "Đầu tư khuôn bao bì độc quyền không thể nhầm lẫn để biến sản phẩm thành một món đồ trang trí trên bàn trang điểm.",
            "mantra": "Bao bì nét vẽ kiêu sa — Nhìn qua một thoáng nhớ mà khôn nguôi"
        },
        {
            "num": 2,
            "meta": "MICRO-INFLUENCER",
            "title": "100 Micro-Influencer uy tín hơn 1 Ngôi sao lớn",
            "ground_truth": "Tỷ lệ tương tác và chuyển đổi của các nhà sáng tạo nội dung có từ 10.000 đến 50.000 người theo dõi cao gấp 4 lần so với các KOL triệu view.",
            "surface": "Dồn toàn bộ ngân sách tiếp thị mời một diễn viên hạng A đóng TVC quảng cáo truyền hình.",
            "nature": "Khách hàng thế hệ Gen Z không còn tin vào các kịch bản quảng cáo bóng bẩy; họ tin vào lời nhận xét chân thực của những người giống họ.",
            "leverage": "Gửi sản phẩm tặng kèm thư tay cho hàng trăm nhà sáng tạo nhỏ và cho phép họ tự do chia sẻ cảm nhận thật.",
            "mantra": "KOL lớn tiếng xa xôi — Người dùng chân thật muôn lời tin yêu"
        },
        {
            "num": 3,
            "meta": "KINH TẾ HỌC ĐƠN VỊ",
            "title": "Đơn hàng đầu tiên chỉ để hòa vốn chi phí quảng cáo",
            "ground_truth": "Với chi phí quảng cáo số ngày càng đắt đỏ, lợi nhuận ròng của một thương hiệu D2C chỉ thực sự xuất hiện từ lần mua thứ 2 trở đi.",
            "surface": "Kỳ vọng phải có lãi ngay lập tức từ lần đầu tiên khách hàng nhấn vào link mua hàng.",
            "nature": "Mô hình kinh doanh số là trò chơi tối ưu hóa tỷ lệ giữ chân khách hàng (Customer Retention).",
            "leverage": "Thiết lập hệ thống email và tin nhắn chăm sóc tự động sau 14 ngày nhận hàng để hướng dẫn sử dụng và tặng mã mua lại.",
            "mantra": "Lần đầu hòa vốn chớ than — Lần sau khách lại bạc vàng sinh sôi"
        },
        {
            "num": 4,
            "meta": "LẮNG NGHE KHÁCH HÀNG",
            "title": "Phần đánh giá 1 sao là bản thiết kế cho sản phẩm tiếp theo",
            "ground_truth": "Kem chống nắng bán chạy nhất của Dot & Key ra đời từ việc lắng nghe hàng ngàn lời phàn nàn của khách hàng về việc kem chống nắng cũ bị để lại vệt trắng bết dính.",
            "surface": "Xóa bỏ các bình luận chê bai tiêu cực trên website để giữ hình ảnh hoàn hảo giả tạo.",
            "nature": "Sự thất vọng của khách hàng chỉ ra chính xác khoảng trống thị trường mà các đối thủ lớn chưa giải quyết được.",
            "leverage": "Hàng tuần tổ chức cuộc họp mổ xẻ toàn bộ các đánh giá tiêu cực để cải tiến công thức ngay lập tức.",
            "mantra": "Lời chê quý giá ngàn vàng — Sửa sai chuẩn xác mở đàng thành công"
        },
        {
            "num": 5,
            "meta": "TỐC ĐỘ R&D",
            "title": "Chu kỳ ra mắt sản phẩm mới trong 90 ngày",
            "ground_truth": "Trong khi các tập đoàn đa quốc gia mất 2 năm để duyệt một sản phẩm mới, Dot & Key có thể đưa ý tưởng từ phòng lab lên kệ trong 3 tháng.",
            "surface": "Chờ đợi sự hoàn hảo tuyệt đối và quy trình phê duyệt quan liêu qua hàng chục cấp lãnh đạo.",
            "nature": "Tốc độ thử nghiệm và thích ứng với trào lưu thành phần mới (Niacinamide, Cica, Hyaluronic) quyết định kẻ dẫn đầu.",
            "leverage": "Sản xuất thử nghiệm lô nhỏ 5.000 sản phẩm để kiểm tra phản ứng thị trường trước khi sản xuất hàng loạt.",
            "mantra": "Nhanh chân chớp lấy thời cơ — Chậm chân chậm bước đứng trơ ngắm người"
        },
        {
            "num": 6,
            "meta": "ĐA KÊNH OMNICHANNEL",
            "title": "Từ Online bước ra Kệ hàng thực tế (Offline Expansion)",
            "ground_truth": "Dù khởi đầu là thương hiệu thuần D2C, hơn 40% doanh số hiện nay của Dot & Key đến từ các chuỗi cửa hàng bán lẻ và siêu thị vật lý.",
            "surface": "Nghĩ rằng kinh doanh thời đại số thì chỉ cần bán trên website và TikTok Shop là đủ.",
            "nature": "Người tiêu dùng vẫn có nhu cầu nếm, thử, ngửi sản phẩm trực tiếp trước khi gắn bó lâu dài.",
            "leverage": "Sử dụng độ phủ thương hiệu online để đàm phán vị trí quầy kệ đẹp nhất trong các chuỗi cửa hàng mỹ phẩm lớn.",
            "mantra": "Online dựng tiếng vang xa — Bước ra thực tế chan hòa muôn nơi"
        },
        {
            "num": 7,
            "meta": "CHIẾN LƯỢC ĐỊNH GIÁ",
            "title": "Định vị Sang trọng Vừa tầm (Masstige: Mass + Prestige)",
            "ground_truth": "Mức giá sản phẩm được neo ở khoảng 10-15 USD — cao hơn hàng bình dân đại trà nhưng rẻ hơn nhiều so với mỹ phẩm xa xỉ nhập khẩu.",
            "surface": "Chạy đua hạ giá sát đáy để cạnh tranh với các sản phẩm gia công kém chất lượng.",
            "nature": "Phân khúc khách hàng trẻ muốn trải nghiệm cảm giác sang trọng nhưng ngân sách có hạn là đại dương xanh khổng lồ.",
            "leverage": "Mang lại trải nghiệm mở hộp đẳng cấp 5 sao nhưng với mức giá ai cũng có thể tự thưởng cho mình mỗi tháng.",
            "mantra": "Vừa túi mà lại sang trang — Khách hàng thích thú ngập tràn niềm vui"
        },
        {
            "num": 8,
            "meta": "CHIẾN LƯỢC THOÁI VỐN",
            "title": "Xây dựng doanh nghiệp như thể bạn sẽ bán nó vào ngày mai",
            "ground_truth": "Việc giữ sổ sách minh bạch và hệ thống dữ liệu khách hàng sạch sẽ giúp Dot & Key được Nykaa mua lại cổ phần chi phối với giá trị hàng ngàn tỷ đồng.",
            "surface": "Vận hành theo kiểu bạ đâu làm đấy, không lưu trữ số liệu khách hàng và hợp đồng rõ ràng.",
            "nature": "Các tập đoàn lớn không chỉ mua sản phẩm; họ mua một cỗ máy tăng trưởng có thể tích hợp ngay vào hệ sinh thái của họ.",
            "leverage": "Chuẩn hóa toàn bộ hệ thống quản trị dữ liệu và pháp lý để luôn sẵn sàng cho các thương vụ M&A chiến lược.",
            "mantra": "Cỗ máy vững chãi từng phần — Nhà đầu tư lớn muôn phần ngợi khen"
        }
    ],
    "environment": {
        "title": "Thiết lập không gian sáng tạo nội dung thị giác liên tục",
        "items": [
            ("Studio chụp ảnh ánh sáng tự nhiên tại văn phòng", "Luôn có sẵn các góc decor tối giản để đội ngũ nội dung có thể quay chụp và thử nghiệm các concept video ngắn mới mỗi ngày."),
            ("Bảng theo dõi các chỉ số hiệu suất TMĐT theo thời gian thực", "Màn hình hiển thị doanh số, chi phí quảng cáo ROAS và tỷ lệ chuyển đổi trực tiếp để đội ngũ kịp thời điều chỉnh ngân sách.")
        ],
        "mantra": "Studio sáng rực ánh đèn — Video bắt mắt khách khen nức lòng"
    },
    "emotional": {
        "title": "Giữ vững sự bình thản trước sự biến động của thuật toán quảng cáo",
        "items": [
            ("Không hoảng loạn khi chi phí quảng cáo Facebook tăng vọt", "Tập trung cải tiến tỷ lệ giữ chân khách hàng cũ và mở rộng kênh phân phối tự nhiên thay vì phụ thuộc hoàn toàn vào quảng cáo trả phí."),
            ("Tôn vinh sự sáng tạo của thế hệ trẻ Gen Z trong tổ chức", "Trao quyền tự do thử nghiệm nội dung cho các bạn trẻ phụ trách mạng xã hội, chấp nhận những thử nghiệm sai lệch nhỏ.")
        ],
        "mantra": "Thuật toán biến đổi khôn lường — Gốc rễ sản phẩm vẫn đường ta đi"
    }
})

# 17. Dr. Alok Kanojia / Dr. K (FO481)
BATCH_3.append({
    "id": "R878NxqapRA",
    "slug": "dr-k-successful-people-broken-loneliness-ai-podcast.html",
    "ep_code": "FO481",
    "cat_badge": "17 / TÂM THẦN HỌC HARVARD & TÂM LÝ KỶ NGUYÊN AI",
    "speaker": "Dr. Alok Kanojia (Dr. K)",
    "speaker_role": "Bác sĩ Tâm thần Đại học Harvard / Nhà sáng lập Healthy Gamer",
    "tagline": "GÓC TỐI NGƯỜI THÀNH CÔNG, CÔ ĐƠN & BƯỚC NGOẶT AI",
    "orig_title": "Are Successful People Broken? Dark Traits, AI Evolution & Loneliness",
    "youtube_url": "https://www.youtube.com/watch?v=R878NxqapRA",
    "duration": "2 giờ 12 phút",
    "read_time": "~9 phút chắt lọc",
    "hero_quote": "Đỉnh cao danh vọng lạnh lùng — Tâm hồn rách nát ai cùng sẻ chia",
    "lead_points": [
        "Tại sao những cá nhân xuất chúng đạt mọi mục tiêu tài chính và danh vọng lại là những người cô đơn, bất an và dễ sụp đổ tâm lý nhất?",
        "Dr. K mổ xẻ những góc khuất tâm lý của giới tinh hoa: Động lực thành công bắt nguồn từ chấn thương tâm lý thời thơ ấu (Trauma-driven Success), cuộc khủng hoảng ý nghĩa khi trí tuệ nhân tạo thay thế năng lực tư duy con người và con đường tìm lại sự lành lặn nội tâm."
    ],
    "hero_summary": {
        "title": "Bản đồ giải phẫu tâm lý học người thành công và cô đơn hiện đại",
        "items": [
            ("1. Nghịch lý thành công từ vết thương tâm lý", "Nhiều triệu phú làm việc điên cuồng 16 tiếng mỗi ngày không phải vì đam mê, mà vì nỗi sợ hãi tiềm thức rằng nếu dừng lại họ sẽ là kẻ vô giá trị."),
            ("2. Sự phân rã của ý thức trong thời đại AI", "Khi AI làm thơ hay hơn người, viết code nhanh hơn kỹ sư, con người đối mặt với cuộc khủng hoảng hiện sinh tàn khốc về giá trị tồn tại."),
            ("3. Chuyển hóa từ 'Thành tựu' sang 'Sự trọn vẹn'", "Chữa lành đứa trẻ bên trong để tận hưởng cuộc sống hiện tại thay vì mãi đuổi theo những cột mốc phù du trong tương lai.")
        ],
        "mantra": "Hàn gắn vết rách trong tim — An yên tự tại mới tìm thấy mình"
    },
    "delusion": {
        "title": "ẢO TƯỞNG THÀNH CÔNG CHỮA LÀNH TẤT CẢ & SỰ THẬT NỘI TÂM",
        "desc": "Xã hội dạy chúng ta rằng chỉ cần kiếm được 1 triệu USD, mua được xe sang nhà to thì mọi bất an và tự ti sẽ biến mất. Nhưng thực tế thành công bên ngoài chỉ đóng vai trò như một liều thuốc tê tạm thời; khi thuốc tê tan hết, nỗi đau nguyên thủy vẫn còn nguyên vẹn.",
        "compare_left": {
            "badge": "ẢO TƯỞNG ĐÁM ĐÔNG",
            "title": "Đạt mục tiêu tiếp theo sẽ mang lại hạnh phúc vĩnh viễn",
            "text": "Liên tục dời đích ngắm: Kiếm được 1 tỷ thì muốn 10 tỷ, mua được xe C-Class thì thèm S-Class, không bao giờ thấy đủ."
        },
        "compare_right": {
            "badge": "TÂM THẦN HỌC HARVARD",
            "title": "Hạnh phúc là năng lực chấp nhận chính mình ở hiện tại",
            "text": "Nhận diện rằng không có thành tích bên ngoài nào có thể lấp đầy chiếc hố đen của cảm giác thiếu thốn tình thương từ thời thơ ấu."
        },
        "matrix_title": "So sánh giữa Người thành công vì Chấn thương và Người thành công vì Bình an",
        "matrix_items": [
            ("Thành công vì Chấn thương (Trauma-Driven)", "• Động lực là nỗi sợ thất bại và khao khát chứng minh với cha mẹ.<br>• Luôn nghi ngờ người xung quanh, kiệt sức (burnout) và cô độc trên đỉnh danh vọng."),
            ("Thành công vì Sự trọn vẹn (Wholeness-Driven)", "• Động lực là sự tò mò thuần khiết và niềm vui cống hiến giá trị.<br>• Biết điểm dừng, có các mối quan hệ sâu sắc và tâm hồn thanh thản.")
        ],
        "mantra": "Đuổi theo ảo ảnh không cùng — Trở về soi bóng lòng mình mới an"
    },
    "insights": [
        {
            "num": 1,
            "meta": "CHẤN THƯƠNG THỜI THƠ ẤU",
            "title": "Thành tích học tập xuất sắc: Cơ chế sinh tồn của đứa trẻ bất an",
            "ground_truth": "Nhiều học sinh xuất sắc tại Harvard thú nhận họ chỉ cảm thấy được cha mẹ yêu thương khi họ mang về điểm số tuyệt đối.",
            "surface": "Tự hào rằng con cái mình chăm chỉ và có kỷ luật thép từ nhỏ mà không cần ai nhắc nhở.",
            "nature": "Đứa trẻ học cách trở nên hoàn hảo như một chiến lược tự vệ để tránh bị cha mẹ ruồng bỏ hoặc chỉ trích.",
            "leverage": "Tự vấn bản thân: 'Tôi đang làm việc điên cuồng vì tôi thực sự muốn, hay vì đứa trẻ 10 tuổi trong tôi vẫn đang cố chứng minh mình có giá trị?'.",
            "mantra": "Điểm mười đổi lấy lời khen — Đằng sau nụ cười một phen tủi hờn"
        },
        {
            "num": 2,
            "meta": "KHỦNG HOẢNG THỜI AI",
            "title": "Khi năng lực nhận thức bị hàng hóa hóa: Cuộc khủng hoảng ý nghĩa",
            "ground_truth": "Các bác sĩ, luật sư, lập trình viên kỳ cựu đang rơi vào trầm cảm diện rộng khi chứng kiến AI làm công việc của họ trong vài giây.",
            "surface": "Nghĩ rằng chỉ cần học thêm kỹ năng mới là có thể tiếp tục chạy đua với máy móc.",
            "nature": "Nếu bạn định nghĩa giá trị bản thân bằng năng lực xử lý thông tin, bạn sẽ hoàn toàn sụp đổ trước trí tuệ nhân tạo.",
            "leverage": "Tái định vị giá trị con người: Tập trung vào sự đồng cảm, khả năng hiện diện, tình yêu thương và sự kết nối tâm linh.",
            "mantra": "Máy kia tính toán ngàn mây — Tình người sâu đậm trong tay giữ gìn"
        },
        {
            "num": 3,
            "meta": "HỘI CHỨNG KẺ KẺ MẠO DANH",
            "title": "Imposter Syndrome: Nỗi sợ bị vạch trần trên đỉnh cao",
            "ground_truth": "Hơn 70% các nhà sáng lập khởi nghiệp thành công luôn sống trong nỗi sợ rằng một ngày nào đó thiên hạ sẽ nhận ra họ không giỏi như người ta nghĩ.",
            "surface": "Nghĩ rằng chỉ có những kẻ bất tài mới bị hội chứng kẻ mạo danh.",
            "nature": "Càng lên cao, bạn càng nhận ra sự phức tạp của thế giới và sự may mắn đóng vai trò lớn thế nào trong thành công.",
            "leverage": "Bình thường hóa cảm giác nghi ngờ bản thân; chấp nhận rằng không ai biết trước mọi câu trả lời của cuộc đời.",
            "mantra": "Nghi ngờ bản thân chuyện thường — Người khôn biết sợ mới tường sự khôn"
        },
        {
            "num": 4,
            "meta": "SỰ CÔ ĐƠN CỦA ĐỈNH CAO",
            "title": "Càng thành công càng khó tìm được người nói thật",
            "ground_truth": "Các CEO tập đoàn lớn bao quanh mình bởi những người chỉ biết gật đầu đồng ý, dẫn đến sự mù lòa nhận thức và cô lập tột cùng.",
            "surface": "Nghĩ rằng có nhiều người vây quanh xin lời khuyên đồng nghĩa với việc có nhiều bạn bè.",
            "nature": "Quyền lực tạo ra một bức tường vô hình ngăn cản sự giao tiếp chân thực giữa hai tâm hồn bình đẳng.",
            "leverage": "Chủ động tìm kiếm những người bạn hoặc chuyên gia tâm lý độc lập không hưởng lợi gì từ thành công của bạn để lắng nghe sự thật.",
            "mantra": "Người vây quanh nịnh đủ điều — Tìm người nói thật mấy chiều gió lay"
        },
        {
            "num": 5,
            "meta": "CƠ CHẾ NGHIỆN CÔNG VIỆC",
            "title": "Workaholism: Cơn nghiện được xã hội khen ngợi nhiều nhất",
            "ground_truth": "Nghiện công việc kích hoạt các thụ thể thần kinh tương tự như nghiện cờ bạc nhưng lại được xã hội tôn vinh là 'tấm gương cống hiến'.",
            "surface": "Tự hào khoe khoang việc làm việc 80 tiếng một tuần và không có kỳ nghỉ suốt 5 năm.",
            "nature": "Lao vào công việc là cách tinh vi nhất để trốn tránh việc phải đối diện với sự trống rỗng và rạn nứt trong hôn nhân.",
            "leverage": "Đặt ra ranh giới cứng: Tắt toàn bộ máy tính sau 19h và dành trọn vẹn buổi tối cho gia đình và bản thân.",
            "mantra": "Cày sâu cuốc bẫm đêm ngày — Trốn chạy thực tại đắng cay lòng mình"
        },
        {
            "num": 6,
            "meta": "CHỮA LÀNH NỘI TÂM",
            "title": "Đối thoại với đứa trẻ bị tổn thương bên trong (Inner Child)",
            "ground_truth": "Các phản ứng bốc đồng, giận dữ dữ dội của người trưởng thành khi bị phê bình thực chất là phản ứng của đứa trẻ 7 tuổi bị mắng.",
            "surface": "Cố gắng dùng lý trí đè nén cơn giận hoặc xấu hổ mỗi khi bị chỉ trích.",
            "nature": "Phần tổn thương chưa được giải quyết trong quá khứ sẽ tiếp tục điều khiển tay lái cuộc đời bạn dưới dạng tiềm thức.",
            "leverage": "Khi cảm thấy bị kích động, hãy dừng lại 1 phút, ôm lấy lồng ngực và tự nhủ: 'Mọi chuyện đã an toàn rồi, bạn đã lớn và có thể tự bảo vệ mình'.",
            "mantra": "Về ôm đứa trẻ ngày xưa — Vỗ về an ủi sớm trưa ấm lòng"
        },
        {
            "num": 7,
            "meta": "SỨC MẠNH CỦA SỰ THỪA NHẬN",
            "title": "Thừa nhận 'Tôi không ổn' là bước đầu tiên của sự tự do",
            "ground_truth": "Thời khắc các bệnh nhân của Dr. K bắt đầu hồi phục là khi họ bật khóc và thừa nhận họ đang vô cùng kiệt sức và bế tắc.",
            "surface": "Luôn nở nụ cười gượng gạo và nói 'Tôi rất ổn' trước mặt đồng nghiệp và người thân.",
            "nature": "Năng lượng tiêu tốn để duy trì chiếc mặt nạ hoàn hảo là nguyên nhân chính gây suy nhược thần kinh.",
            "leverage": "Dũng cảm chia sẻ với một người đáng tin cậy về những khó khăn thực sự mà bạn đang phải gánh chịu một mình.",
            "mantra": "Nhận mình yếu đuối chẳng sao — Giọt nước mắt xuống mở vào an yên"
        },
        {
            "num": 8,
            "meta": "TRIẾT LÝ PHỤC THIỆN",
            "title": "Chuyển từ 'Chinh phục thế giới' sang 'Nuôi dưỡng tâm hồn'",
            "ground_truth": "Ở nửa sau của cuộc đời, người khôn ngoan nhận ra rằng không có danh hiệu nào sánh bằng việc được ngủ một giấc thật sâu không mộng mị.",
            "surface": "Tiếp tục lao vào những dự án điên cuồng mới khi cơ thể đã phát ra hàng loạt tín hiệu cảnh báo bệnh tật.",
            "nature": "Cuộc đời là một vòng tròn hoàn nguyên; đích đến cuối cùng của người tài giỏi là sự giản dị và hòa hợp với tự nhiên.",
            "leverage": "Dành thời gian chăm sóc cây cối, nấu một bữa ăn ngon và tận hưởng từng hơi thở trong lành mỗi sớm mai.",
            "mantra": "Tranh danh đoạt lợi làm chi — Tâm hồn thanh thản bước đi nhẹ nhàng"
        }
    ],
    "environment": {
        "title": "Thiết lập không gian trị liệu tâm lý và giải phóng ức chế",
        "items": [
            ("Góc ngồi thiền định không có bất kỳ thiết bị điện tử nào", "Bố trí một chiếc đệm êm cạnh cửa sổ nhìn ra cây xanh để thực hành ngồi yên quan sát hơi thở 20 phút mỗi sáng."),
            ("Cuốn sổ nhật ký cảm xúc (Shadow Work Journal)", "Dành riêng một cuốn sổ để viết ra những suy nghĩ tăm tối, nỗi bất an và sự ghen tị mà bạn không dám nói với ai.")
        ],
        "mantra": "Đệm êm cửa sổ ngắm cây — Trút trang nhật ký đong đầy bình an"
    },
    "emotional": {
        "title": "Bảo toàn năng lượng trước những cuộc tấn công của sự tự phán xét",
        "items": [
            ("Đối xử với bản thân như một người bạn thân nhất", "Khi mắc sai lầm, hãy tự hỏi: 'Nếu bạn thân của tôi mắc lỗi này, tôi sẽ an ủi họ hay sỉ nhục họ?' và dành sự dịu dàng đó cho chính mình."),
            ("Chấp nhận sự hữu hạn của kiếp người", "Hiểu rằng bạn không cần phải cứu rỗi toàn bộ thế giới; chỉ cần sống trọn vẹn và tử tế với những người xung quanh là đã đủ một đời ý nghĩa.")
        ],
        "mantra": "Dịu dàng với chính bản thân — Đời người hữu hạn muôn phần thứ tha"
    }
})

# 18. Simon Sinek (FO476)
BATCH_3.append({
    "id": "etgQjtdNEtc",
    "slug": "simon-sinek-trust-crisis-gen-z-burnout-leadership-podcast.html",
    "ep_code": "FO476",
    "cat_badge": "18 / NGHỆ THUẬT LÃNH ĐẠO & VĂN HÓA NIỀM TIN",
    "speaker": "Simon Sinek",
    "speaker_role": "Tác giả Toàn cầu (Start With Why, Leaders Eat Last, The Infinite Game)",
    "tagline": "KHỦNG HOẢNG NIỀM TIN, GEN Z KIỆT SỨC & LÃNH ĐẠO THỜI AI",
    "orig_title": "Simon Sinek on India’s Future, Trust Crisis, Gen Z Burnout, Anxiety & AI Friends",
    "youtube_url": "https://www.youtube.com/watch?v=etgQjtdNEtc",
    "duration": "1 giờ 48 phút",
    "read_time": "~8 phút chắt lọc",
    "hero_quote": "Lãnh đạo chẳng phải ngôi cao — Lãnh đạo là nhận lo âu cho người",
    "lead_points": [
        "Thế hệ trẻ hiện đại đang đối mặt với một cuộc khủng hoảng niềm tin và kiệt sức chưa từng có: Thiếu sự kết nối con người sâu sắc, văn hóa sa thải tàn nhẫn của doanh nghiệp và sự trỗi dậy của tình bạn ảo thời AI.",
        "Simon Sinek giải mã bản chất của thuật lãnh đạo vị nhân sinh: Làm thế nào để tạo ra một 'Vòng tròn An toàn' (Circle of Safety), nơi nhân viên cảm thấy được bảo vệ, dám bộc lộ sai lầm và dốc lòng cống hiến vì một mục đích cao cả."
    ],
    "hero_summary": {
        "title": "Bản thiết kế văn hóa tổ chức và nghệ thuật lãnh đạo vị nhân sinh",
        "items": [
            ("1. Vòng tròn An toàn (Circle of Safety)", "Khi các mối đe dọa bên trong tổ chức (sợ bị sa thải, sợ bị đổ lỗi) được triệt tiêu, toàn bộ năng lượng sẽ được dồn để đối phó với thách thức bên ngoài."),
            ("2. Tư duy Trò chơi Vô cực (The Infinite Game)", "Kinh doanh không có người thắng kẻ thua chung cuộc; mục tiêu là duy trì cuộc chơi và liên tục hoàn thiện sứ mệnh."),
            ("3. Kỹ năng lắng nghe đồng cảm (Active Listening)", "Lắng nghe không phải là chờ đợi đến lượt mình nói; lắng nghe là tạo không gian để đối phương cảm thấy được thấu hiểu trọn vẹn.")
        ],
        "mantra": "Vòng an toàn mở rộng ra — Cùng nhau tiến bước vượt qua phong trần"
    },
    "delusion": {
        "title": "ẢO TƯỞNG QUẢN LÝ BẰNG NỖI SỢ & SỨC MẠNH CỦA SỰ TIN CẬY",
        "desc": "Các nhà quản lý truyền thống tin rằng phải đe dọa sa thải và tạo áp lực liên tục thì nhân viên mới làm việc chăm chỉ. Nhưng nỗi sợ hãi chỉ tạo ra sự phục tùng đối phó ngắn hạn; nó giết chết hoàn toàn sự sáng tạo và lòng trung thành.",
        "compare_left": {
            "badge": "ẢO TƯỞNG QUẢN TRỊ CŨ",
            "title": "Đo lường con người bằng bảng tính Excel",
            "text": "Sẵn sàng sa thải hàng loạt nhân sự để làm đẹp báo cáo tài chính quý, coi con người như chi phí tiêu hao."
        },
        "compare_right": {
            "badge": "LÃNH ĐẠO THỰC SỰ",
            "title": "Coi con người là tài sản quý giá nhất",
            "text": "Bảo vệ nhân viên trước bão tố kinh tế, đào tạo họ vượt qua sai lầm để cùng nhau xây dựng tương lai bền vững."
        },
        "matrix_title": "So sánh giữa Trò chơi Hữu hạn và Trò chơi Vô cực",
        "matrix_items": [
            ("Trò chơi Hữu hạn (Finite Mindset)", "• Mục tiêu là đánh bại đối thủ trong quý này bằng mọi giá.<br>• Phá hủy văn hóa nội bộ, xói mòn niềm tin của khách hàng."),
            ("Trò chơi Vô cực (Infinite Mindset)", "• Mục tiêu là tồn tại và phục vụ lý tưởng cao đẹp (Just Cause).<br>• Thu hút những nhân tài kiệt xuất nhất và trường tồn qua nhiều thập kỷ.")
        ],
        "mantra": "Quản lý bằng sợ hãi qua — Niềm tin dẫn lối mới là thiên thu"
    },
    "insights": [
        {
            "num": 1,
            "meta": "VÒNG TRÒN AN TOÀN",
            "title": "Tổ chức mạnh mẽ khi nhân viên không phải phòng thủ lẫn nhau",
            "ground_truth": "Các đơn vị đặc nhiệm SEAL của quân đội Mỹ thành công nhờ các chiến binh hoàn toàn tin tưởng người bên cạnh sẽ bảo vệ lưng mình.",
            "surface": "Kích động sự cạnh tranh nội bộ khốc liệt giữa các nhân viên để 'tăng năng suất'.",
            "nature": "Nếu phải tiêu tốn năng lượng để đề phòng đồng nghiệp đâm sau lưng, nhân viên sẽ không còn sức lực để sáng tạo phục vụ khách hàng.",
            "leverage": "Xây dựng văn hóa không đổ lỗi: Khi xảy ra sự cố, tập trung truy tìm lỗ hổng quy trình chứ không tìm người để trừng phạt.",
            "mantra": "Lưng kề lưng cánh kề vai — Chẳng lo phản trắc tương lai vững vàng"
        },
        {
            "num": 2,
            "meta": "LÝ DO BẮT ĐẦU",
            "title": "Bắt đầu với câu hỏi TẠI SAO (Start With Why)",
            "ground_truth": "Mọi người không mua cái bạn làm (What); họ mua lý do tại sao bạn làm điều đó (Why).",
            "surface": "Chỉ thao thao bất tuyệt kể về các tính năng kỹ thuật và giá cả của sản phẩm.",
            "nature": "Hệ viền của não bộ chi phối cảm xúc và quyết định mua hàng không có ngôn ngữ; nó phản ứng với lý tưởng và niềm tin.",
            "leverage": "Luôn bắt đầu mọi bài thuyết trình bằng sứ mệnh cốt lõi và giá trị nhân văn mà dự án hướng tới.",
            "mantra": "Khơi nguồn từ chữ 'Tại sao' — Rung động lòng dạ ngút ngàn niềm tin"
        },
        {
            "num": 3,
            "meta": "BẢN CHẤT LÃNH ĐẠO",
            "title": "Lãnh đạo là người ăn sau cùng (Leaders Eat Last)",
            "ground_truth": "Trong lực lượng Thủy quân lục chiến, các sĩ quan chỉ huy luôn là người xếp hàng ăn sau cùng sau khi tất cả binh nhì đã có phần cơm.",
            "surface": "Lãnh đạo giành lấy bổng lộc, tiền thưởng cao nhất trước tiên và đẩy rủi ro xuống cấp dưới.",
            "nature": "Sự kính trọng và lòng trung thành không thể mua được bằng tiền; nó là phản ứng sinh học trước sự hy sinh của người đi đầu.",
            "leverage": "Khi công ty gặp khó khăn, lãnh đạo hãy chủ động giảm lương trước khi tính đến việc cắt giảm nhân sự.",
            "mantra": "Cơm nhường lính trước chỉ huy — Đồng cam cộng khổ quản gì gian nan"
        },
        {
            "num": 4,
            "meta": "NGHỆ THUẬT LẮNG NGHE",
            "title": "Hãy là người cuối cùng phát biểu trong phòng họp",
            "ground_truth": "Nelson Mandela luôn để tất cả mọi người trong bộ tộc phát biểu ý kiến trước khi ông đưa ra nhận xét tổng kết cuối cùng.",
            "surface": "Sếp bước vào phòng họp và đưa ra ngay ý kiến kết luận, sau đó hỏi 'Mọi người có đồng ý không?'.",
            "nature": "Khi người đứng đầu đã lên tiếng, toàn bộ cấp dưới sẽ tự động kiểm duyệt và chỉ nói những điều sếp muốn nghe.",
            "leverage": "Tập thói quen chỉ đặt câu hỏi và gật đầu lắng nghe trong suốt 90% thời lượng cuộc họp.",
            "mantra": "Lắng nghe thấu suốt tâm tư — Lời sau đanh thép muôn phần phục tùng"
        },
        {
            "num": 5,
            "meta": "KHỦNG HOẢNG GEN Z",
            "title": "Sự kiệt sức của thế hệ trẻ bắt nguồn từ việc thiếu kết nối thật",
            "ground_truth": "Gen Z là thế hệ kết nối mạng nhiều nhất nhưng lại cảm thấy cô đơn và lo âu cao nhất trong lịch sử nhân loại.",
            "surface": "Chỉ trích thế hệ trẻ là 'yếu đuối, thích nhảy việc và thiếu kiên nhẫn'.",
            "nature": "Sự thiếu hụt kỹ năng giao tiếp thực tế và văn hóa khen thưởng tức thì trên mạng xã hội đã tước đi cơ bắp chịu đựng của họ.",
            "leverage": "Lãnh đạo cần đóng vai trò người thầy cố vấn (Mentor), kiên nhẫn dạy họ kỹ năng giải quyết xung đột và kiên trì dài hạn.",
            "mantra": "Trẻ người non dạ âu lo — Cần người soi đuốc mở đò qua sông"
        },
        {
            "num": 6,
            "meta": "BẪY TÌNH BẠN AI",
            "title": "AI không thể thay thế một cái ôm và ánh mắt ấm áp",
            "ground_truth": "Hàng triệu thanh niên bắt đầu tâm sự với AI chatbot vì sợ bị tổn thương khi mở lòng với người thật.",
            "surface": "Nghĩ rằng AI sẽ giải quyết được vấn đề cô đơn của nhân loại trong tương lai.",
            "nature": "Hormone Oxytocin chỉ được giải phóng qua tiếp xúc thể chất thực tế và sự đồng cảm giữa hai sinh vật sống.",
            "leverage": "Khuyến khích các cuộc gặp mặt trực tiếp không có sự hiện diện của điện thoại thông minh.",
            "mantra": "Màn hình sáng rực vô tri — Cái ôm ấm áp diệu kỳ hơn muôn"
        },
        {
            "num": 7,
            "meta": "TRÒ CHƠI VÔ CỰC",
            "title": "Đừng cố đánh bại đối thủ; hãy cạnh tranh với chính mình của ngày hôm qua",
            "ground_truth": "Khi Microsoft tập trung toàn lực vào việc 'đánh bại Apple', họ bị mất phương hướng; khi họ quay lại sứ mệnh 'giúp mọi người làm việc hiệu quả', họ bứt phá trở lại.",
            "surface": "Suốt ngày theo dõi và sao chép từng tính năng nhỏ của đối thủ cạnh tranh.",
            "nature": "Đối thủ chỉ là tấm gương giúp bạn phát hiện ra điểm yếu của chính mình; họ không phải là mục đích tồn tại của bạn.",
            "leverage": "Tập trung 100% nguồn lực vào việc nâng cao giá trị mang lại cho khách hàng thay vì bận tâm đến đối thủ.",
            "mantra": "So bì đối thủ mệt nhoài — Nâng cao giá trị tương lai sáng ngời"
        },
        {
            "num": 8,
            "meta": "DI SẢN LÃNH ĐẠO",
            "title": "Thước đo thành công: Đội ngũ của bạn có hạnh phúc khi về nhà không?",
            "ground_truth": "Cách một người được đối xử tại nơi làm việc ảnh hưởng trực tiếp đến cách họ đối xử với vợ con vào bữa tối tại nhà.",
            "surface": "Nghĩ rằng công việc và đời sống gia đình là hai ngăn kéo hoàn toàn tách biệt.",
            "nature": "Sự ức chế và nhục nhã tại công sở sẽ biến thành bạo lực lạnh trút lên những người thân vô tội.",
            "leverage": "Lãnh đạo với nhận thức rằng mỗi quyết định của bạn đang tác động đến hạnh phúc của hàng trăm tổ ấm gia đình.",
            "mantra": "Tan ca lòng thấy nhẹ tênh — Về nhà sưởi ấm gia đình bình yên"
        }
    ],
    "environment": {
        "title": "Thiết kế văn phòng thúc đẩy sự tương tác tự nhiên",
        "items": [
            ("Khu vực uống cà phê tập trung (Watercooler Hub)", "Bố trí máy pha cà phê ở trung tâm văn phòng để các nhân viên từ các phòng ban khác nhau tình cờ gặp gỡ và trò chuyện."),
            ("Cấm mang điện thoại vào phòng họp chiến lược", "Đặt một chiếc giỏ đựng điện thoại ngoài cửa phòng họp; mọi người hoàn toàn hiện diện và nhìn vào mắt nhau khi thảo luận.")
        ],
        "mantra": "Điện thoại để lại ngoài song — Vào phòng bàn bạc một lòng đồng tâm"
    },
    "emotional": {
        "title": "Nuôi dưỡng lòng dũng cảm của người thủ lĩnh vị nhân sinh",
        "items": [
            ("Dám bảo vệ cấp dưới trước sức ép phi lý của cổ đông ngắn hạn", "Sẵn sàng đánh cược vị trí của mình để bảo vệ những giá trị đạo đức và sự an toàn của nhân viên."),
            ("Duy trì sự khiêm nhường và lòng biết ơn mỗi ngày", "Nhắc nhở bản thân rằng vị trí lãnh đạo là một đặc ân được giao phó để phục vụ, không phải quyền lực để hưởng thụ.")
        ],
        "mantra": "Chức quyền gánh nặng trên vai — Phục vụ nhân thế miệt mài chẳng ngơi"
    }
})

# 19. Dr. Joe Dispenza (FO475)
BATCH_3.append({
    "id": "90lLQVZe2Nc",
    "slug": "dr-joe-dispenza-rewire-brain-neuroplasticity-fear-podcast.html",
    "ep_code": "FO475",
    "cat_badge": "19 / KHOA HỌC NÃO BỘ & CHỮA LÀNH TỰ THÂN",
    "speaker": "Dr. Joe Dispenza",
    "speaker_role": "Chuyên gia Thần kinh học, Sinh học Biểu sinh / Tác giả Best-seller Toàn cầu",
    "tagline": "TÁI LẬP TRÌNH NÃO BỘ: KHOA HỌC VỀ THIỀN ĐỊNH & VƯỢT QUA NỖI SỢ",
    "orig_title": "Dr Joe Dispenza: Rewire Your Brain, Heal Your Mind, Fear & Anxiety",
    "youtube_url": "https://www.youtube.com/watch?v=90lLQVZe2Nc",
    "duration": "2 giờ 08 phút",
    "read_time": "~9 phút chắt lọc",
    "hero_quote": "Tâm trí mở lối tương lai — Quá khứ khép lại rạng ngời ánh dương",
    "lead_points": [
        "Đa số con người thức dậy mỗi sáng và lập tức lặp lại những cảm xúc quen thuộc của quá khứ, khiến cơ thể bị giam cầm trong một tương lai định sẵn đầy lo âu và bệnh tật.",
        "Dr. Joe Dispenza giải mã cơ chế khoa học thần kinh lượng tử: Cách thay đổi sóng não từ Beta sang Alpha và Theta, kích hoạt tính mềm dẻo thần kinh để bẻ gãy các liên kết cảm xúc độc hại và tái lập trình gen biểu sinh (Epigenetics) nhằm tự chữa lành thân tâm."
    ],
    "hero_summary": {
        "title": "Bản đồ khoa học tái lập trình hệ thần kinh và tiềm thức",
        "items": [
            ("1. Cơ thể trở thành tâm trí (Body as the Mind)", "Khi một cảm xúc tiêu cực được lặp lại suốt 10 năm, cơ thể bị nghiện hóa học với hormone cortisol và tự động từ chối sự thay đổi."),
            ("2. Chuyển hóa sóng não thông qua Thiền định lượng tử", "Hạ tần số sóng não từ Beta phân tán sang Alpha và Theta gắn kết (Coherence), mở toang cánh cửa bước vào hệ điều hành tiềm thức."),
            ("3. Sinh học biểu sinh: Ý thức thay đổi biểu hiện gen", "Cảm xúc biết ơn và lòng trắc ẩn nâng cao tín hiệu hóa sinh, kích hoạt các gen miễn dịch và tắt các gen gây ung thư.")
        ],
        "mantra": "Sóng não điều hòa êm êm — Gen lành thức giấc đẩy lùi bệnh đau"
    },
    "delusion": {
        "title": "ẢO TƯỞNG CƠ THỂ BẤT BIẾN DO GEN & SỨC MẠNH BIỂU SINH",
        "desc": "Y học truyền thống từng dạy rằng gen di truyền định đoạt 100% số phận bệnh tật của bạn. Khoa học biểu sinh (Epigenetics) hiện đại chứng minh rằng gen chỉ là bản thiết kế tiềm năng; chính môi trường cảm xúc và suy nghĩ của bạn mới là công tắc bật/tắt các gen đó.",
        "compare_left": {
            "badge": "ẢO TƯỞNG ĐÁM ĐÔNG",
            "title": "Tôi bị bệnh vì gen gia đình tôi di truyền như vậy",
            "text": "Bất lực cam chịu số phận, tiếp tục sống trong môi trường căng thẳng, giận dữ và chờ đợi bệnh tật bộc phát."
        },
        "compare_right": {
            "badge": "KHOA HỌC BIỂU SINH",
            "title": "Môi trường nội tại quyết định biểu hiện gen",
            "text": "Chủ động thanh lọc hóa học cơ thể bằng cảm xúc nâng cao (Elevated Emotions), tái tạo tế bào khỏe mạnh từ cấp độ phân tử."
        },
        "matrix_title": "So sánh giữa Tâm trí sống trong Quá khứ và Tâm trí kiến tạo Tương lai",
        "matrix_items": [
            ("Sống trong ký ức quá khứ (Living in the Past)", "• Thức dậy nhớ về những mối hận thù và hóa đơn nợ nần.<br>• Cơ thể chìm trong trạng thái sinh tồn (Survival Mode), hệ miễn dịch suy tàn."),
            ("Kiến tạo tương lai mới (Living in the Future)", "• Cảm nhận niềm vui và lòng biết ơn trước cả khi mục tiêu xuất hiện ngoài đời thật.<br>• Bộ não lập trình lại các synap như thể tương lai mới đã diễn ra.")
        ],
        "mantra": "Gen kia chỉ chiếc khung sườn — Tâm ta làm chủ mở đường tái sinh"
    },
    "insights": [
        {
            "num": 1,
            "meta": "THẦN KINH LƯỢNG TỬ",
            "title": "Nếu suy nghĩ của bạn không thay đổi, tương lai của bạn sẽ là bản sao của quá khứ",
            "ground_truth": "95% hành vi và cảm xúc của một người 35 tuổi là các chương trình tiềm thức tự động được ghi nhớ từ thời niên thiếu.",
            "surface": "Ước mơ có một cuộc sống mới giàu có hạnh phúc nhưng mỗi sáng thức dậy vẫn suy nghĩ y hệt ngày hôm qua.",
            "nature": "Các mạch nơ-ron liên kết cứng tạo thành chiếc hộp nhận thức; bạn không thể giải quyết vấn đề bằng cùng tần số năng lượng tạo ra nó.",
            "leverage": "Mỗi sáng dành 20 phút ngồi yên, hình dung chi tiết về con người mới bạn muốn trở thành trước khi bước chân xuống giường.",
            "mantra": "Nghĩ suy cũ kỹ lối mòn — Làm sao mơ ước tương lai huy hoàng"
        },
        {
            "num": 2,
            "meta": "NGHIỆN CẢM XÚC HÓA HỌC",
            "title": "Cơ thể nghiện cảm giác giận dữ và đau khổ như nghiện ma túy",
            "ground_truth": "Khi bạn giận dữ, tuyến thượng thận bơm adrenaline; cơ thể quen với liều lượng hóa chất này và sẽ vô thức tìm kiếm xung đột để được 'phê thuốc'.",
            "surface": "Nghĩ rằng hoàn cảnh bên ngoài và người khác luôn chọc tức mình một cách ngẫu nhiên.",
            "nature": "Cơ thể sinh học đóng vai trò như một kẻ nghiện; nó thao túng tâm trí suy nghĩ tiêu cực để đòi hỏi lượng hormone quen thuộc.",
            "leverage": "Bắt quả tang cơ thể: Khi thấy cơn giận trào lên, nói to 'Dừng lại! Cơ thể, mày không phải là chủ nhân của tao!'.",
            "mantra": "Cơn nghiện cảm xúc giấu mình — Tỉnh táo nhận diện giữ gìn bình yên"
        },
        {
            "num": 3,
            "meta": "SỰ GẮN KẾT NÃO BỘ",
            "title": "Sóng não Beta phân tán phá hủy sự tập trung và năng lượng",
            "ground_truth": "Khi bị căng thẳng, các vùng não bộ hoạt động rời rạc như một dàn nhạc giao hưởng không có nhạc trưởng (Incoherent Brain).",
            "surface": "Cố gắng suy nghĩ nhiều hơn, căng thẳng hơn để giải quyết một bài toán bế tắc.",
            "nature": "Não bộ phân tán tiêu tốn một lượng glucose khổng lồ và gửi tín hiệu hỗn loạn xuống toàn bộ các cơ quan nội tạng.",
            "leverage": "Thực hành thiền tập trung vào không gian trống rỗng xung quanh cơ thể để đưa sóng não về trạng thái Alpha đồng pha.",
            "mantra": "Sóng loạn tâm trí bấn loạn — Điều hòa nhịp thở sáng trưng bầu trời"
        },
        {
            "num": 4,
            "meta": "TRÁI TIM GẮN KẾT",
            "title": "Trường điện từ của trái tim mạnh gấp 5.000 lần não bộ",
            "ground_truth": "Khi thực hành cảm xúc biết ơn chân thành, nhịp tim trở nên mượt mà (Heart Coherence), gửi tín hiệu an toàn lên não bộ.",
            "surface": "Coi trái tim chỉ là một chiếc máy bơm máu cơ học không có trí tuệ.",
            "nature": "Trái tim có mạng lưới hơn 40.000 tế bào thần kinh cảm giác riêng biệt; trường điện từ của nó có thể đo được cách xa cơ thể 3 mét.",
            "leverage": "Đặt tay lên ngực, hít thở chậm qua tim và cảm nhận lòng biết ơn sâu sắc đối với một điều giản dị trong 3 phút.",
            "mantra": "Bàn tay áp chặt lồng ngực — Lòng biết ơn dâng sáng ngời ánh lân"
        },
        {
            "num": 5,
            "meta": "BIỂU SINH HỌC",
            "title": "Bật công tắc gen khỏe mạnh bằng cảm xúc nâng cao",
            "ground_truth": "Nghiên cứu trên 120 học viên thiền định 4 ngày cho thấy nồng độ kháng thể IgA tăng vọt 50% và hàng loạt gen chống viêm được kích hoạt.",
            "surface": "Nghĩ rằng thuốc tây là cách duy nhất để tăng cường hệ miễn dịch trước virus.",
            "nature": "Tế bào phản ứng với môi trường hóa chất mà bạn tắm cho nó mỗi ngày; cảm xúc thăng hoa là tín hiệu biểu sinh tối ưu nhất.",
            "leverage": "Dành 10 phút mỗi ngày sống trong trạng thái cảm xúc của sự thành công và khỏe mạnh trước cả khi nó xảy ra.",
            "mantra": "Cảm xúc thăng hoa ngút ngàn — Tế bào thức tỉnh đẩy lùi ốm đau"
        },
        {
            "num": 6,
            "meta": "VÙNG ĐẤT KHÔNG BIẾT",
            "title": "Phép màu lượng tử chỉ xảy ra ở Vùng đất Không biết (The Unknown)",
            "ground_truth": "Nếu mọi thứ trong ngày của bạn đều được dự đoán trước, bạn đang sống hoàn toàn trong quá khứ.",
            "surface": "Sợ hãi sự không chắc chắn và cố gắng kiểm soát từng chi tiết nhỏ của cuộc sống.",
            "nature": "Trường lượng tử chứa đựng mọi khả năng vô hạn; bạn phải buông bỏ sự kiểm soát cũ để cho phép điều kỳ diệu bước vào.",
            "leverage": "Dũng cảm bước ra khỏi vùng an toàn; đón nhận những sự kiện bất ngờ với tâm thế tò mò và phấn khích.",
            "mantra": "Buông lơi kiểm soát tầm thường — Đón chào kỳ tích mở đường tương lai"
        },
        {
            "num": 7,
            "meta": "VƯỢT THOÁT THỜI GIAN",
            "title": "Trở thành Không ai cả, Không là gì cả, Không ở đâu cả",
            "ground_truth": "Trong trạng thái thiền định sâu, bạn hoàn toàn quên mất cơ thể mình, tên tuổi mình, tuổi tác và căn phòng bạn đang ngồi.",
            "surface": "Bị dính mắc vào chiếc điện thoại, khuôn mặt, trang phục và chức danh xã hội của bản thân.",
            "nature": "Khi ý thức tách khỏi thực tại vật chất 3 chiều, bạn hòa nhập vào trường ý thức thuần khiết nơi mọi sáng tạo bắt đầu.",
            "leverage": "Tập trung vào khoảng không vô tận sau đôi mắt cho đến khi ranh giới giữa bạn và vũ trụ hoàn toàn tan biến.",
            "mantra": "Quên thân quên xác quên mình — Hòa vào vũ trụ ngút ngàn mênh mang"
        },
        {
            "num": 8,
            "meta": "CHỮA LÀNH TỰ THÂN",
            "title": "Cơ thể sở hữu trí tuệ tự chữa lành bẩm sinh vô biên",
            "ground_truth": "Hàng ngàn trường hợp thuyên giảm bệnh nan y tự phát (Spontaneous Remission) được ghi nhận khoa học sau khi bệnh nhân thay đổi triệt để tâm thức.",
            "surface": "Giao phó toàn bộ sinh mạng và niềm tin cho hóa chất bệnh viện trong sự tuyệt vọng.",
            "nature": "Khi bạn ngừng đầu độc cơ thể bằng hormone căng thẳng, hệ thống miễn dịch tự nhiên sẽ dọn dẹp mọi tế bào lỗi.",
            "leverage": "Xem cơ thể là người bạn đồng hành trung thành nhất; gửi tình yêu thương và sự biết ơn đến từng cơ quan nội tạng.",
            "mantra": "Thân thể trí tuệ nhiệm màu — Yêu thương ôm ấp dứt sầu tan đau"
        }
    ],
    "environment": {
        "title": "Thiết lập không gian thiền định và tái tạo năng lượng đỉnh cao",
        "items": [
            ("Không gian cách âm và nhiệt độ chuẩn", "Phòng thiền riêng tư, tắt toàn bộ đèn, sử dụng bịt mắt ngủ để giảm kích thích thị giác về mức 0 tuyệt đối."),
            ("Âm nhạc sóng não Theta và âm thanh đa chiều", "Sử dụng tai nghe chất lượng cao nghe nhạc không lời tần số 432Hz hoặc âm thanh đồng bộ hai tai (Binaural Beats) để dẫn dắt sóng não.")
        ],
        "mantra": "Phòng tối tĩnh lặng tuyệt trần — Sóng não Theta đưa thân vào miền an"
    },
    "emotional": {
        "title": "Duy trì sự gắn kết tim - não trong đời sống thường nhật",
        "items": [
            ("Dừng lại giữa ngày để kiểm tra trạng thái nội tâm", "Cứ sau 3 tiếng làm việc, nhắm mắt 60 giây và tự hỏi: 'Tôi đang ở trạng thái sinh tồn (Survival) hay sáng tạo (Creation)?'."),
            ("Không phản ứng ngay lập tức trước các tình huống tiêu cực", "Hít thở chậm 5 nhịp trước khi trả lời một cuộc gọi khó chịu để giữ vững sự gắn kết của trái tim.")
        ],
        "mantra": "Một phút dừng lại ngắm nhìn — Tim hòa cùng não giữ gìn bình an"
    }
})

print(f"Loaded {len(BATCH_3)} episodes in batch 3 (all done).")
