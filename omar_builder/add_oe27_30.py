# -*- coding: utf-8 -*-
"""
add_oe27_30.py: Hoàn thiện nốt OE27 - OE30 cho episodes_batch3.py
"""
import json
import sys
sys.path.append('/Users/vietmac/Documents/CODE/k/omar_builder')
from episodes_batch3 import BATCH_3

with open('/Users/vietmac/.gemini/antigravity/brain/24deb8b1-3156-43d0-91a1-3246f0cc4078/scratch/omar_40_videos.json') as f:
    raw_vids = {v['idx']: v for v in json.load(f)}

eps = [
    # 27. Get Rich Off Salary (fdzQ-Vs9mwg)
    {
        "id": raw_vids[27]['id'],
        "slug": "get-rich-off-salary-money-masterclass-podcast.html",
        "ep_code": "OE27",
        "cat_badge": "05 / TÂM LÝ BÁN HÀNG & GIAO TIẾP",
        "speaker": "Omar Eltakrori & Chuyên gia Tài chính Cá nhân",
        "speaker_role": "Cố vấn Quản trị Gia sản & Nhà đầu tư Bất động sản Dòng tiền",
        "tagline": "QUẢN TRỊ TÀI CHÍNH CÁ NHÂN & BIẾN DÒNG TIỀN LƯƠNG THÀNH ĐÒN BẨY ĐẦU TƯ",
        "orig_title": raw_vids[27]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[27]['id']}",
        "publish_date": raw_vids[27]['date'],
        "raw_date": f"{raw_vids[27]['raw_date'][:4]}-{raw_vids[27]['raw_date'][4:6]}-{raw_vids[27]['raw_date'][6:]}",
        "duration": "1 giờ 35 phút",
        "read_time": "~9 phút chắt lọc",
        "hero_quote": "Đồng lương tích lũy khôn ngoan — Đầu tư sinh lợi muôn vàn tự do",
        "lead_points": [
            "Con đường làm giàu bền vững không đòi hỏi bạn phải liều lĩnh bỏ việc ngay lập tức để khởi nghiệp, mà bắt đầu từ việc tối ưu hóa dòng tiền lương: Chi tiêu dưới mức thu nhập, đầu tư vào tài sản sinh lời và xây dựng kênh kinh doanh bán thời gian bên cạnh công việc chính.",
            "Phân tích công thức phân bổ tài chính 50/30/20 cải tiến và cách biến từng đồng lương ổn định thành nguồn vốn đầu tư an toàn cho các cỗ máy kiếm tiền trên internet."
        ],
        "hero_summary": {
            "title": "Bản đồ biến dòng lương ổn định thành đòn bẩy tự do tài chính",
            "items": [
                ("1. Nghịch lý lạm phát lối sống (Lifestyle Creep)", "Lương tăng gấp đôi nhưng tài khoản vẫn trống rỗng vì nhu cầu tiêu xài vô bổ tăng tương ứng."),
                ("2. Dòng lương là nhà đầu tư thiên thần", "Dùng sự ổn định của công việc chính để tài trợ vốn cho việc học tập kỹ năng mới và mua sắm thiết bị sáng tạo nội dung."),
                ("3. Tách biệt tài khoản tự do", "Tự động trích 20–30% thu nhập ngay khi lương về vào tài khoản đầu tư sinh lời trước khi chi tiêu bất kỳ khoản nào.")
            ],
            "mantra": "Tiền lương làm vốn đầu tư — Lối sống giản dị ấm no tháng ngày"
        },
        "delusion": {
            "title": "ẢO TƯỞNG PHẢI NGHỈ VIỆC MỚI LÀM GIÀU & BẢN CHẤT CỦA SỰ AN TOÀN",
            "desc": "Nhiều người trẻ bị tiêm nhiễm tư duy cực đoan rằng phải nghỉ việc ngay, đốt thuyền khởi nghiệp mới là dũng cảm. Thực tế, khi không có dòng tiền trang trải tiền nhà và cơm ăn áo mặc, bạn sẽ rơi vào trạng thái hoảng loạn và đưa ra các quyết định kinh doanh sai lầm chết người.",
            "compare_left": {
                "badge": "LIỀU LĨNH MÙ QUÁNG",
                "title": "Đốt thuyền nghỉ việc khi chưa có dòng tiền",
                "text": "Áp lực cơm áo gạo tiền đè nặng khiến bạn phải bán phá giá dịch vụ và chấp nhận phục vụ những khách hàng tồi tệ nhất."
            },
            "compare_right": {
                "badge": "CHIẾN LƯỢC KHÔN NGOAN",
                "title": "Khởi nghiệp bán thời gian trên bệ đỡ công việc chính",
                "text": "Lấy tiền lương nuôi dưỡng ước mơ kinh doanh cho đến khi nguồn thu phụ vượt gấp đôi lương chính thức mới chuyển dịch an toàn."
            },
            "matrix_title": "So sánh Khởi nghiệp liều mạng và Khởi nghiệp có bệ đỡ",
            "matrix_items": [
                ("Khởi nghiệp liều mạng không bệ đỡ", "• Tâm trạng bất an, luôn chực chờ nguy cơ vỡ nợ.<br>• Tỷ lệ thất bại và bỏ cuộc sau 6 tháng lên tới 90%."),
                ("Khởi nghiệp trên bệ đỡ tiền lương", "• Tâm lý vững vàng, thoải mái sáng tạo nội dung chất lượng cao.<br>• Từng bước tích lũy kinh nghiệm và chuyển giao mượt mà sang tự do tài chính.")
            ],
            "mantra": "Bệ đỡ tiền lương vững vàng — Khởi nghiệp từng bước mở đàng vinh hoa"
        },
        "insights": [
            {"num": 1, "meta": "LẠM PHÁT LỐI SỐNG", "title": "Cái bẫy tăng lương tăng chi tiêu", "ground_truth": "Nếu bạn không thể tiết kiệm được tiền khi kiếm 15 triệu/tháng, bạn cũng sẽ không tiết kiệm được gì khi kiếm 100 triệu/tháng.", "surface": "Nghĩ rằng chỉ cần được tăng lương là mọi vấn đề tài chính sẽ được giải quyết.", "nature": "Sự thỏa mãn từ vật chất chỉ kéo dài vài tuần; sau đó não bộ sẽ đòi hỏi những thứ đắt đỏ hơn để duy trì dopamine.", "leverage": "Khóa chặt chi phí sinh hoạt cố định, toàn bộ phần thu nhập tăng thêm được chuyển thẳng vào quỹ đầu tư.", "mantra": "Lương tăng chi phí giữ nguyên — Dòng tiền dư dả nối liền tự do"},
            {"num": 2, "meta": "TRẢ CHO MÌNH TRƯỚC", "title": "Quy tắc tự động trích lập đầu tư ngay ngày nhận lương", "ground_truth": "Nếu bạn đợi chi tiêu hết cả tháng rồi mới tiết kiệm phần còn lại, con số đó luôn luôn bằng 0.", "surface": "Tiêu xài thoải mái và tự hứa cuối tháng còn dư bao nhiêu sẽ đem gửi tiết kiệm.", "nature": "Bản năng con người sẽ tự động tìm cách tiêu hết số tiền có sẵn trong tài khoản thanh toán.", "leverage": "Cài đặt lệnh chuyển tiền tự động 20% lương sang tài khoản đầu tư chứng khoán hoặc mua vàng ngay ngày mùng 1.", "mantra": "Lương về trích quỹ đầu tư — Phần còn chi trả ấm no tháng ngày"},
            {"num": 3, "meta": "KINH DOANH BÁN THỜI GIAN", "title": "Quy luật 5 đến 9 (The 5 to 9 Hustle)", "ground_truth": "Từ 9h sáng đến 5h chiều là nuôi sống hiện tại; từ 5h chiều đến 9h tối là xây dựng tương lai.", "surface": "Đi làm về mệt mỏi nằm dài lướt TikTok và xem phim giải trí suốt buổi tối.", "nature": "Thời gian buổi tối là tài nguyên duy nhất giúp bạn bứt phá khỏi tầng lớp làm thuê.", "leverage": "Dành 2 tiếng mỗi tối viết kịch bản, quay video và xây dựng hệ thống sản phẩm số của riêng bạn.", "mantra": "Năm đến chín tối miệt mài — Dựng xây sự nghiệp tương lai sáng ngời"},
            {"num": 4, "meta": "ĐẦU TƯ BẢN THÂN", "title": "Khoản đầu tư có ROI cao nhất là nâng cấp kỹ năng của chính bạn", "ground_truth": "Bỏ 20 triệu mua một khóa học thực chiến có thể giúp bạn tăng thu nhập thêm 200 triệu mỗi năm trọn đời.", "surface": "Tiếc tiền mua sách và học hỏi, nhưng sẵn sàng chi tiền mua điện thoại mới.", "nature": "Kỹ năng kiếm tiền cao (High-Income Skills) là tài sản duy nhất không ai có thể đánh thuế hay cướp mất của bạn.", "leverage": "Trích 10% thu nhập mỗi tháng vào quỹ phát triển bản thân để mua sách và tham gia các khóa học chất lượng cao.", "mantra": "Đầu tư trí tuệ bản thân — Lợi nhuận vô tận muôn phần sinh sôi"},
            {"num": 5, "meta": "TIÊU DIỆT NỢ XẤU", "title": "Nợ tiêu dùng là xiềng xích nô lệ thời hiện đại", "ground_truth": "Quẹt thẻ tín dụng mua sắm trả góp là bạn đang vay mượn tương lai của chính mình để mua những thứ bạn không cần.", "surface": "Dùng thẻ tín dụng để mua điện thoại đời mới và quần áo hàng hiệu cho bằng bạn bằng bè.", "nature": "Lãi suất thẻ tín dụng 25–35%/năm sẽ hủy hoại toàn bộ nỗ lực tích lũy tài sản của bạn.", "leverage": "Cắt bỏ toàn bộ thẻ tín dụng tiêu dùng, chỉ thanh toán bằng tiền mặt hoặc thẻ ghi nợ có sẵn tiền.", "mantra": "Nợ nần xiềng xích mỏi mòn — Trả xong thanh thản vuông tròn tương lai"},
            {"num": 6, "meta": "ĐA DẠNG HÓA DÒNG TIỀN", "title": "Không bao giờ để gia đình phụ thuộc vào một nguồn thu nhập duy nhất", "ground_truth": "Một công việc dù tốt đến đâu cũng chỉ cách cảnh thất nghiệp đúng một quyết định cắt giảm nhân sự của ban giám đốc.", "surface": "Cảm thấy hoàn toàn an toàn và tự mãn với công việc văn phòng hiện tại.", "nature": "Sự phụ thuộc đơn nhất tạo ra rủi ro sinh tồn cực lớn khi nền kinh tế bước vào chu kỳ suy thoái.", "leverage": "Xây dựng ít nhất 2 nguồn thu nhập phụ từ internet (Khóa học, tư vấn, tiếp thị liên kết) bên cạnh tiền lương.", "mantra": "Hai nguồn nước mát chảy về — Không lo hạn hán vẹn bề ấm êm"},
            {"num": 7, "meta": "TÂM THÁI BIẾT ĐỦ", "title": "Người giàu nhất không phải người có nhiều tiền nhất, mà là người cần ít nhất", "ground_truth": "Sự tự do tài chính thực sự xuất hiện khi chi phí sinh hoạt của bạn thấp hơn rất nhiều so với thu nhập thụ động.", "surface": "Cố gắng phô trương sự giàu có bằng cách mua nhà to, xe sang ngập trong nợ nần.", "nature": "Sự phô trương bên ngoài chỉ để gây ấn tượng với những người bạn thậm chí còn không thích.", "leverage": "Thực hành lối sống tối giản, tìm kiếm niềm vui trong những điều giản dị, không bị cuốn vào vòng xoáy tiêu dùng.", "mantra": "Biết đủ tâm trí thảnh thơi — Chẳng màng hư ảo sáng ngời bình an"},
            {"num": 8, "meta": "KẾ HOẠCH NGHỈ VIỆC", "title": "Công thức chuyển dịch an toàn sang làm chủ trọn thời gian", "ground_truth": "Thời điểm vàng để nghỉ việc là khi thu nhập từ kinh doanh phụ vượt 200% lương chính liên tục trong 6 tháng.", "surface": "Nghỉ việc theo cảm xúc bốc đồng sau một cuộc cãi vã với sếp.", "nature": "Sự chuyển dịch có chuẩn bị kỹ lưỡng đảm bảo công việc kinh doanh mới có bệ phóng vững chắc nhất.", "leverage": "Tích lũy đủ 12 tháng chi phí sinh hoạt dự phòng trước khi nộp đơn xin nghỉ việc chính thức.", "mantra": "Chuẩn bị chu đáo lên đường — Nộp đơn từ biệt muôn phương vẫy chào"}
        ],
        "environment": {
            "title": "Thiết lập hệ thống quản trị ngân sách gia đình",
            "items": [
                ("1. Bảng tính theo dõi dòng tiền thu chi tự động", "Ghi nhận toàn bộ các khoản chi tiêu lớn nhỏ trong tháng để phát hiện các lỗ rò rỉ tài chính."),
                ("2. 3 Tài khoản ngân hàng chuyên biệt", "Tài khoản 1: Chi tiêu thiết yếu; Tài khoản 2: Quỹ đầu tư sinh lời; Tài khoản 3: Quỹ học tập và phát triển."),
                ("3. Két sắt an toàn lưu giữ tài liệu pháp lý và vàng tích lũy", "Lưu trữ hợp đồng bảo hiểm, giấy tờ đất đai và tài sản phòng hộ vật lý an toàn tại nhà.")
            ],
            "mantra": "Ba tài khoản chia rạch ròi — Dòng tiền kiểm soát thảnh thơi an lòng"
        },
        "emotional": {
            "title": "Nuôi dưỡng tâm thế điềm tĩnh trước tiền bạc",
            "items": [
                ("1. Không để tiền bạc chi phối lòng tự trọng", "Hiểu rằng giá trị của bạn nằm ở phẩm chất đạo đức và sự tử tế, không phải ở số tiền bạn đang có."),
                ("2. Kiên nhẫn với hành trình tích lũy lãi kép", "Lãi kép cần thời gian để phát huy sức mạnh kỳ diệu; không sốt ruột tìm kiếm các cơ hội làm giàu nhanh lừa đảo."),
                ("3. Trân trọng từng đồng tiền kiếm được bằng mồ hôi chân chính", "Mỗi đồng tiền chân chính đều mang năng lượng phúc đức nuôi dưỡng cuộc sống của gia đình bạn.")
            ],
            "mantra": "Lãi kép cần có thời gian — Tâm an tích lũy muôn vàn sinh sôi"
        }
    },

    # 28. First $100K in Business (WskDzuwVtqc)
    {
        "id": raw_vids[28]['id'],
        "slug": "make-first-100k-in-business-beginner-podcast.html",
        "ep_code": "OE28",
        "cat_badge": "05 / TÂM LÝ BÁN HÀNG & GIAO TIẾP",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "CHINH PHỤC 100.000 USD ĐẦU TIÊN: LỜI KHUYÊN NỀN TẢNG CHO NGƯỜI MỚI BẮT ĐẦU",
        "orig_title": raw_vids[28]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[28]['id']}",
        "publish_date": raw_vids[28]['date'],
        "raw_date": f"{raw_vids[28]['raw_date'][:4]}-{raw_vids[28]['raw_date'][4:6]}-{raw_vids[28]['raw_date'][6:]}",
        "duration": "1 giờ 04 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Chặng đầu gian khó chông gai — Vượt qua trăm ngàn tương lai mở đàng",
        "lead_points": [
            "Kiếm 100.000 USD đầu tiên là chặng đường khó khăn nhất trong toàn bộ sự nghiệp kinh doanh, vì bạn phải tự mình làm mọi việc từ bán hàng, phục vụ khách, xử lý kỹ thuật đến quản trị cảm xúc cá nhân.",
            "Omar đúc kết 5 bài học sống còn: Tập trung vào 1 sản phẩm duy nhất, phục vụ 1 tệp khách hàng duy nhất, sử dụng 1 kênh truyền thông duy nhất và lặp lại liên tục cho đến khi đạt mục tiêu."
        ],
        "hero_summary": {
            "title": "Bản đồ quy tắc 1-1-1-1 chinh phục 100K USD đầu đời",
            "items": [
                ("1. Một lời chào hàng cốt lõi (One Offer)", "Không đa dạng hóa sản phẩm khi chưa đạt doanh thu 100.000 USD từ sản phẩm đầu tiên."),
                ("2. Một kênh tiếp cận duy nhất (One Traffic Source)", "Dồn 100% nguồn lực làm chủ thuật toán YouTube trước khi phân tán sang TikTok hay Facebook."),
                ("3. Kỷ luật thép thực thi liên tục", "Không thay đổi chiến lược giữa chừng khi chưa thực hiện đủ 100 lần thử nghiệm nghiêm túc.")
            ],
            "mantra": "Một lòng một dạ kiên trì — Trăm ngàn đô chạm ngại gì gian nan"
        },
        "delusion": {
            "title": "ẢO TƯỞNG ĐA DẠNG HÓA SẢN PHẨM & BẢN CHẤT SỰ TẬP TRUNG TUYỆT ĐỐI",
            "desc": "Người mới kinh doanh thường vội vã mở ra hàng chục dịch vụ khác nhau vì sợ bỏ sót khách hàng. Nhưng trong kinh doanh, sự phân tán nguồn lực là nguyên nhân số 1 dẫn đến phá sản. Người thắng cuộc là người tập trung toàn lực vào một mũi nhọn duy nhất.",
            "compare_left": {
                "badge": "PHÂN TÁN NGUỒN LỰC",
                "title": "Cái gì cũng bán, ai cũng nhận phục vụ",
                "text": "Tạo ra 5 website, 3 fanpage và 10 gói dịch vụ khác nhau khiến năng lượng bị xé nhỏ và không việc nào ra hồn."
            },
            "compare_right": {
                "badge": "MŨI NHỌN CHIẾN LƯỢC",
                "title": "Một sản phẩm - Một thị trường - Một thông điệp",
                "text": "Mài sắc một mũi khoan duy nhất cho đến khi xuyên thủng bức tường thị trường và chiếm lĩnh vị thế độc tôn."
            },
            "matrix_title": "So sánh Doanh nghiệp phân tán và Doanh nghiệp tập trung",
            "matrix_items": [
                ("Doanh nghiệp phân tán nguồn lực", "• Quá tải vận hành, chất lượng dịch vụ kém, khách hàng không hài lòng.<br>• Thu nhập lẹt đẹt vài chục triệu không bứt phá lên được."),
                ("Doanh nghiệp tập trung cao độ", "• Tối ưu hóa quy trình đến mức hoàn hảo, khách hàng tự động giới thiệu nhau.<br>• Nhanh chóng cán mốc 100.000 USD chỉ trong vòng 12–18 tháng.")
            ],
            "mantra": "Phân tán xé nát cơ đồ — Tập trung mũi nhọn dựng nên cơ đồ"
        },
        "insights": [
            {"num": 1, "meta": "QUY TẮC MŨI NHỌN", "title": "Quy tắc 1-1-1-1 để chạm mốc $100K", "ground_truth": "1 Lời chào hàng + 1 Tệp khách hàng + 1 Kênh truyền thông + 1 Năm kiên trì = 100.000 USD.", "surface": "Cùng lúc mở kênh YouTube, xây tài khoản TikTok, chạy quảng cáo Facebook và làm podcast.", "nature": "Lực lượng mỏng phân tán trên nhiều mặt trận sẽ bị đối thủ tập trung đánh bại trên từng điểm.", "leverage": "Đóng băng toàn bộ các kênh phụ, dồn toàn bộ thời gian và trí tuệ làm chủ kênh YouTube.", "mantra": "Một kênh một hướng kiên trì — Dồn toàn tâm sức ngại gì khó khăn"},
            {"num": 2, "meta": "TỰ TAY BÁN HÀNG", "title": "Người sáng lập bắt buộc phải là nhân viên bán hàng số 1", "ground_truth": "Bạn không thể thuê người khác bán hàng hộ khi chính bạn chưa từng chốt thành công 20 khách hàng đầu tiên.", "surface": "Vừa mở công ty đã vội vàng tuyển nhân viên sale và giao phó toàn bộ trách nhiệm.", "nature": "Chỉ có người sáng lập mới hiểu rõ nhất nỗi đau của khách hàng và những phản hồi thực tế để cải tiến sản phẩm.", "leverage": "Tự mình thực hiện toàn bộ các cuộc gọi tư vấn cho đến khi công thức chốt sale đạt tỷ lệ trên 25%.", "mantra": "Tự tay chốt khách đầu đời — Hiểu sâu thị trường rạng ngời thành công"},
            {"num": 3, "meta": "HOÀN THIỆN SẢN PHẨM", "title": "Sản phẩm xuất sắc là công cụ marketing tốt nhất", "ground_truth": "Một sản phẩm tồi tệ được quảng cáo rầm rộ chỉ khiến nó chết nhanh hơn.", "surface": "Chi toàn bộ ngân sách cho quảng cáo mà không cải thiện chất lượng phục vụ.", "nature": "Sự thất vọng của khách hàng đầu tiên sẽ lan truyền nhanh hơn bất kỳ chiến dịch PR nào.", "leverage": "Chăm sóc 10 khách hàng đầu tiên chu đáo như người thân trong gia đình để nhận về những lời khen ngợi chân thành.", "mantra": "Sản phẩm xuất sắc vẹn toàn — Khách khen nức nở tiếng vang muôn trùng"},
            {"num": 4, "meta": "QUẢN TRỊ DÒNG TIỀN MẶT", "title": "Tiền mặt là dưỡng khí của doanh nghiệp non trẻ", "ground_truth": "Doanh nghiệp không chết vì thiếu lợi nhuận trên sổ sách; doanh nghiệp chết vì hết tiền mặt trong tài khoản.", "surface": "Chi tiền mua sắm bàn ghế văn phòng đắt tiền và máy tính đời mới ngay khi vừa mở công ty.", "nature": "Lãng phí tiền mặt vào tài sản cố định khiến bạn không còn nguồn lực duy trì khi thị trường biến động.", "leverage": "Giữ chi phí cố định ở mức tối thiểu tuyệt đối, thuê ngoài thay vì mua sắm tài sản lớn.", "mantra": "Tiền mặt giữ chặt trong tay — Chi tiêu tằn tiện tháng ngày hanh thông"},
            {"num": 5, "meta": "TỐC ĐỘ PHẢN HỒI", "title": "Lắng nghe phản hồi của khách hàng và sửa đổi ngay trong ngày", "ground_truth": "Lợi thế lớn nhất của doanh nghiệp nhỏ trước các tập đoàn lớn là tốc độ thích ứng nhanh như chớp.", "surface": "Bảo thủ bảo vệ ý kiến của mình, phớt lờ những lời góp ý của khách hàng.", "nature": "Khách hàng là người trả tiền; sự hài lòng của họ là kim chỉ nam duy nhất cho sự tồn tại của bạn.", "leverage": "Khi học viên báo lỗi trong bài giảng, sửa lại ngay lập tức và gửi bản cập nhật trong vòng 2 tiếng.", "mantra": "Khách góp ý sửa liền tay — Tốc độ thần tốc dựng xây lòng tin"},
            {"num": 6, "meta": "KỶ LUẬT THÓI QUEN", "title": "Thực hiện những việc nhàm chán lặp đi lặp lại mỗi ngày", "ground_truth": "Thành công không phải là những khoảnh khắc lấp lánh; thành công là việc hoàn thành những việc đơn điệu không ai thấy.", "surface": "Chỉ làm việc khi có cảm hứng và bỏ dở khi cảm thấy chán nản.", "nature": "Cảm hứng là thứ không đáng tin cậy; chỉ có kỷ luật thép mới đưa bạn cán đích.", "leverage": "Lên lịch làm việc chi tiết từng giờ và tuân thủ nghiêm ngặt bất kể tâm trạng vui hay buồn.", "mantra": "Kỷ luật thép vững như đồng — Vượt qua buồn chán thỏa lòng ước mong"},
            {"num": 7, "meta": "HỌC HỎI TỪ BẬC THẦY", "title": "Tìm một người cố vấn đã đạt được kết quả bạn khao khát", "ground_truth": "Tự mò mẫm một mình sẽ khiến bạn mất 5 năm và hàng trăm triệu đồng học phí cho những sai lầm ngớ ngẩn.", "surface": "Cố gắng tự làm theo ý mình vì sợ tốn tiền thuê người cố vấn.", "nature": "Một lời chỉ dẫn chính xác của người đi trước giúp bạn đi tắt đón đầu qua những bãi mìn nguy hiểm.", "leverage": "Đầu tư tiền bạc để được một người thầy thực chiến kèm cặp và sửa lỗi trực tiếp.", "mantra": "Có thầy chỉ lối đưa đường — Bãi mìn vượt thoát muôn phương an lành"},
            {"num": 8, "meta": "BẢN LĨNH VƯỢT KHÓ", "title": "Giai đoạn từ 0 đến 100K USD tôi luyện nên nhân cách doanh nhân", "ground_truth": "Mục tiêu lớn nhất của việc kiếm 100.000 USD không phải là số tiền, mà là con người bản lĩnh bạn trở thành.", "surface": "Nản lòng và muốn bỏ cuộc mỗi khi gặp khó khăn thử thách ban đầu.", "nature": "Những giọt mồ hôi và nước mắt trong chặng đường đầu tiên chính là ngọn lửa tôi luyện nên ý chí kim cương.", "leverage": "Coi mỗi khó khăn là một bài kiểm tra tư cách xem bạn đã xứng đáng bước vào hàng ngũ doanh nhân hay chưa.", "mantra": "Lửa thử vàng gian nan thử dạ — Vượt chặng đầu rạng rỡ tương lai"}
        ],
        "environment": {
            "title": "Thiết lập không gian khởi nghiệp tinh gọn và tập trung",
            "items": [
                ("1. Góc làm việc tối giản trong phòng ngủ", "Chỉ cần 1 chiếc bàn, 1 máy tính và 1 ghế ngồi thoải mái; không cần văn phòng thuê ngoài tốn kém."),
                ("2. Tai nghe chống ồn chủ động Sony WH-1000XM5", "Cách ly hoàn toàn tiếng ồn xung quanh để tập trung 100% vào việc sáng tạo và bán hàng."),
                ("3. Bảng mục tiêu doanh số dán trên tường", "Chia nhỏ mục tiêu $100.000 thành từng nấc: $10.000 -> $25.000 -> $50.000 -> $100.000 và gạch bỏ khi đạt được.")
            ],
            "mantra": "Góc phòng nhỏ bé đơn sơ — Nuôi dưỡng chí lớn giấc mơ triệu vàng"
        },
        "emotional": {
            "title": "Nuôi dưỡng ý chí kiên cường không gục ngã",
            "items": [
                ("1. Chấp nhận sự cô đơn trên con đường khởi nghiệp", "Hiểu rằng bạn bè và người thân có thể không hiểu con đường bạn đang đi; hãy chứng minh bằng kết quả."),
                ("2. Giữ vững niềm tin sắt đá vào tương lai", "Không bao giờ để những khó khăn tạm thời làm lung lay mục tiêu lớn của cuộc đời."),
                ("3. Ăn mừng từng chiến thắng nhỏ đầu tiên", "Tự hào khi kiếm được 1 triệu đồng đầu tiên từ khách hàng lạ trên internet.")
            ],
            "mantra": "Chí kiên cường vững tựa non — Vượt qua sóng gió vuông tròn ước mơ"
        }
    },

    # 29. Longform Content Monetize (u3Gt-_P4GeY)
    {
        "id": raw_vids[29]['id'],
        "slug": "fastest-way-to-monetize-content-longform-podcast.html",
        "ep_code": "OE29",
        "cat_badge": "03 / CHIẾN LƯỢC NỘI DUNG YOUTUBE & VIDEO TRIỆU VIEW",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "VIDEO DẠNG DÀI (LONGFORM): CON ĐƯỜNG KIẾM TIỀN VÀ XÂY DỰNG FAN TRUNG THÀNH NHANH NHẤT",
        "orig_title": raw_vids[29]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[29]['id']}",
        "publish_date": raw_vids[29]['date'],
        "raw_date": f"{raw_vids[29]['raw_date'][:4]}-{raw_vids[29]['raw_date'][4:6]}-{raw_vids[29]['raw_date'][6:]}",
        "duration": "1 giờ 53 phút",
        "read_time": "~9 phút chắt lọc",
        "hero_quote": "Video dài thấu hiểu tâm can — Gắn kết tri kỷ muôn vàn sắc son",
        "lead_points": [
            "Trong khi cả thế giới mải mê chạy theo các video ngắn 15 giây trôi qua như gió thoảng, những nhà sáng tạo kiếm được nhiều tiền nhất lại tập trung toàn lực vào video dạng dài (Longform 30–60 phút).",
            "Phân tích cơ chế tâm lý học: Video ngắn mang lại sự chú ý hời hợt, nhưng chỉ có video dài mới có khả năng chuyển hóa nhận thức, xây dựng lòng tin sâu sắc và chốt các hợp đồng giá trị cao."
        ],
        "hero_summary": {
            "title": "Bản đồ quyền lực của nội dung dạng dài trong thời đại số",
            "items": [
                ("1. Độ sâu của sự gắn kết (Depth of Connection)", "Khán giả dành 45 phút nghe bạn chia sẻ sẽ cảm thấy thân thiết như một người bạn tri kỷ ngoài đời thực."),
                ("2. Khả năng giải thích thấu đáo", "Video dài cho phép bạn mổ xẻ nguyên nhân gốc rễ, đưa ra các ví dụ thực tế và giải quyết trọn vẹn sự hoài nghi của người mua."),
                ("3. Tỷ lệ chuyển đổi hợp đồng cao vượt trội", "Khách hàng đến từ video dài hầu như không bao giờ trả giá; họ đến với tâm thế sẵn sàng quẹt thẻ hợp tác.")
            ],
            "mantra": "Video dài đọng lại tình thâm — Khách xem thấm thía ngàn năm nhớ hoài"
        },
        "delusion": {
            "title": "ẢO TƯỞNG NGƯỜI DÙNG KHÔNG CÒN KIÊN NHẪN & SỰ THẬT VỀ NỘI DUNG SÂU",
            "desc": "Người ta thường lặp lại câu nói sáo rỗng: 'Thời đại này không ai xem video dài nữa đâu'. Thực tế, các podcast dài 2–3 tiếng của Joe Rogan hay Andrew Huberman thu hút hàng chục triệu lượt xem mỗi tập. Khán giả không ghét video dài; họ chỉ ghét video dài mà rỗng tuếch.",
            "compare_left": {
                "badge": "LỐI MÒN NÔNG CẠN",
                "title": "Chỉ mải mê làm video ngắn 30 giây",
                "text": "Có hàng triệu lượt xem nhưng không ai nhớ tên bạn và không bán được bất kỳ sản phẩm giá trị cao nào."
            },
            "compare_right": {
                "badge": "CHIẾN LƯỢC SÂU SẮC",
                "title": "Lấy video dài làm trung tâm của vũ trụ nội dung",
                "text": "Sản xuất video dài chất lượng cao để xây dựng uy quyền chuyên gia, sau đó trích xuất video ngắn làm phễu dẫn đường."
            },
            "matrix_title": "So sánh Hiệu quả chuyển đổi giữa Video Ngắn và Video Dài",
            "matrix_items": [
                ("Video ngắn (Shorts/Reels)", "• Tiếp cận người lạ nhanh nhưng sự chú ý biến mất sau 3 giây.<br>• Rất khó để bán các dịch vụ tư vấn giá trên $1.000."),
                ("Video dạng dài (Longform)", "• Lượt xem khiêm tốn hơn nhưng tỷ lệ chuyển đổi thành khách hàng trả phí cực kỳ cao.<br>• Xây dựng cộng đồng fan trung thành sẵn sàng bảo vệ thương hiệu.")
            ],
            "mantra": "Video ngắn thoáng qua như mây — Video dài đọng lại tháng ngày bền sâu"
        },
        "insights": [
            {"num": 1, "meta": "THỜI GIAN TIẾP XÚC", "title": "Khái niệm 'Tổng thời lượng tiêu thụ' (Total Time Consumed)", "ground_truth": "Mức độ tin cậy tỷ lệ thuận với tổng số phút một người đã lắng nghe bạn nói.", "surface": "Đo lường thành công bằng số lượt bấm xem (Views).", "nature": "Một người xem hết video 45 phút có giá trị thương mại gấp 90 lần một người xem video 30 giây.", "leverage": "Tối ưu hóa nội dung để giữ chân người xem ở lại càng lâu càng tốt bằng cấu trúc kể chuyện cuốn hút.", "mantra": "Thời gian tiếp xúc càng sâu — Niềm tin gắn chặt trước sau vẹn toàn"},
            {"num": 2, "meta": "CẤU TRÚC CUỐN HÚT", "title": "Nghệ thuật giữ nhịp video dài không gây buồn ngủ", "ground_truth": "Video dài cần có cấu trúc từng chương hồi rõ ràng với các điểm cao trào định kỳ mỗi 5 phút.", "surface": "Nói chuyện miên man không có điểm dừng và không có dàn ý phân đoạn.", "nature": "Bộ não người xem cần các mốc chuyển đoạn (Chapters) để nghỉ ngơi và tiếp nhận ý niệm mới.", "leverage": "Thêm thanh tiến trình từng chương trên video YouTube và thay đổi nhạc nền nhẹ khi chuyển chủ đề.", "mantra": "Từng chương từng đoạn rõ ràng — Người xem theo dõi nhẹ nhàng say mê"},
            {"num": 3, "meta": "PHÒNG BÀN LUẬN CHUYÊN SÂU", "title": "Video dài chứng minh năng lực tư duy thấu suốt", "ground_truth": "Bất kỳ ai cũng có thể học thuộc lòng một đoạn văn 30 giây để diễn; chỉ có chuyên gia thực thụ mới nói chuyện sâu sắc suốt 1 tiếng.", "surface": "Sợ làm video dài vì không biết nói gì sau 3 phút đầu.", "nature": "Sự thiếu hụt kiến thức thực chiến sẽ lập tức bị lộ tẩy khi đứng trước ống kính máy quay dài thời lượng.", "leverage": "Đào sâu vào bản chất triết lý, phân tích các góc nhìn trái chiều và đưa ra case study thực tế.", "mantra": "Nói dài mới tỏ tài năng — Chuyên gia thực thụ muôn phần uy phong"},
            {"num": 4, "meta": "TỰ ĐỘNG LỌC KHÁCH HÀNG", "title": "Video dài là bộ lọc tự nhiên loại bỏ những kẻ lười biếng", "ground_truth": "Những người không đủ kiên nhẫn xem hết video 20 phút sẽ không bao giờ là học viên chịu làm bài tập nghiêm túc.", "surface": "Cố gắng làm video thật ngắn để chiều chuộng những người lười suy nghĩ.", "nature": "Khách hàng trả phí cao luôn là những người thích đọc sâu, học kỹ và tìm kiếm giải pháp gốc rễ.", "leverage": "Tự hào làm video dài cho tệp khán giả tinh hoa có năng lực tập trung cao.", "mantra": "Video dài lọc người khôn — Kẻ lười bỏ dở người kiên bước vào"},
            {"num": 5, "meta": "THUẬT TOÁN ĐỀ XUẤT", "title": "Thuật toán YouTube ưu tiên thời lượng xem tích lũy (Watch Time)", "ground_truth": "Mục tiêu tối thượng của YouTube là giữ chân người dùng ở lại trên nền tảng càng lâu càng tốt.", "surface": "Nghĩ rằng thuật toán chỉ thích video ngắn như TikTok.", "nature": "Một video 40 phút giữ chân khán giả được 20 phút sẽ được thuật toán thưởng điểm đề xuất khổng lồ.", "leverage": "Tập trung tối ưu hóa chỉ số Average View Duration (AVD) thay vì chỉ nhìn vào CTR.", "mantra": "Giữ chân khán giả ở lâu — Thuật toán ưu ái đứng đầu bảng tin"},
            {"num": 6, "meta": "CHÈN LỜI KÊU GỌI TỰ NHIÊN", "title": "Nghệ thuật chèn lời mời hợp tác tinh tế ở giữa video", "ground_truth": "Khán giả xem đến phút thứ 15 là những người đã hoàn toàn tin tưởng bạn và sẵn sàng nghe lời khuyên.", "surface": "Chỉ chèn lời kêu gọi ở 5 giây cuối cùng khi mọi người đã chuẩn bị tắt video.", "nature": "Thời điểm vàng để đưa ra lời chào hàng là ngay sau khi bạn vừa chia sẻ một bài học đột phá nhất.", "leverage": "Khẽ ngỏ: 'Nếu anh chị muốn áp dụng hệ thống này vào doanh nghiệp của mình, hãy bấm link đặt lịch ở phần mô tả'.", "mantra": "Giữa dòng chia sẻ ân tình — Khẽ trao lời ngỏ kết tình tri giao"},
            {"num": 7, "meta": "TÁI SỬ DỤNG VÔ TẬN", "title": "Một video dài là mỏ vàng sinh ra toàn bộ nội dung trong tuần", "ground_truth": "Bạn không bao giờ phải đau đầu nghĩ bài đăng mạng xã hội nếu bạn có 1 video dài chất lượng mỗi tuần.", "surface": "Mỗi ngày ngồi nghĩ một câu danh ngôn riêng lẻ để đăng Facebook.", "nature": "Video dài chứa đựng đầy đủ ngữ cảnh, câu chuyện và luận điểm để cắt thành 5 video ngắn và 3 bài viết.", "leverage": "Thiết lập quy trình phân rã nội dung từ video YouTube dài sang mọi nền tảng khác.", "mantra": "Một mỏ vàng quý trong tay — Cắt ra trăm nhánh tháng ngày nở hoa"},
            {"num": 8, "meta": "XÂY DỰNG DI SẢN", "title": "Thư viện video dài là gia tài số trường tồn của bạn", "ground_truth": "Các video dài giải quyết vấn đề muôn thuở sẽ tiếp tục mang về khán giả và khách hàng sau 10 năm nữa.", "surface": "Chỉ chạy theo các tin tức giật gân hết hạn sau 48 giờ.", "nature": "Tri thức gốc rễ về bản chất con người và kinh doanh không bao giờ bị lỗi thời theo năm tháng.", "leverage": "Tập trung làm các chủ đề bất biến (Evergreen): Xây dựng thương hiệu, Quản trị thời gian, Tâm lý bán hàng.", "mantra": "Tri thức gốc rễ trường tồn — Mười năm nhìn lại vẫn còn vẹn nguyên"}
        ],
        "environment": {
            "title": "Thiết lập bối cảnh quay video dài thư thái và thoải mái",
            "items": [
                ("1. Ghế bành ngồi thư giãn có đệm lưng êm ái", "Giúp bạn ngồi trò chuyện suốt 2 tiếng mà không bị mỏi lưng hay gò bó cử động."),
                ("2. Bình nước giữ nhiệt và tách trà ấm", "Nhấp ngụm trà ấm giữa các phần nói chuyện giúp giọng nói luôn giữ được độ trong trẻo và truyền cảm."),
                ("3. Màn hình đồng hồ đếm giờ hiển thị lớn", "Theo dõi thời lượng để phân bổ nhịp điệu bài giảng hợp lý mà không cần nhìn điện thoại.")
            ],
            "mantra": "Ghế êm tách trà ấm nồng — Thong dong chia sẻ thỏa lòng ước mong"
        },
        "emotional": {
            "title": "Nuôi dưỡng sự kiên nhẫn và phong thái ung dung",
            "items": [
                ("1. Không vội vã, không hối thúc", "Nói chuyện với sự từ tốn và đĩnh đạc; sự vội vàng chỉ bộc lộ sự nông cạn và bất an."),
                ("2. Tin tưởng vào chiều sâu của tri thức", "Biết rằng những người có tâm và có tầm sẽ nhận ra giá trị vàng ngọc trong từng câu chữ của bạn."),
                ("3. Tận hưởng niềm vui của sự giãi bày trọn vẹn", "Hạnh phúc khi được dốc hết ruột gan chia sẻ những tâm huyết cả đời cho người hữu duyên.")
            ],
            "mantra": "Từ tốn đĩnh đạc bước đi — Người khôn nhận biết ngại gì cách ngăn"
        }
    },

    # 30. 11 Years Content Creation (d6ZW6FHpnew)
    {
        "id": raw_vids[30]['id'],
        "slug": "11-years-content-creation-what-actually-works-podcast.html",
        "ep_code": "OE30",
        "cat_badge": "03 / CHIẾN LƯỢC NỘI DUNG YOUTUBE & VIDEO TRIỆU VIEW",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "11 NĂM LÀM CONTENT: NHỮNG NGUYÊN LÝ THỰC CHIẾN BẤT BIẾN VƯỢT THỜI GIAN",
        "orig_title": raw_vids[30]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[30]['id']}",
        "publish_date": raw_vids[30]['date'],
        "raw_date": f"{raw_vids[30]['raw_date'][:4]}-{raw_vids[30]['raw_date'][4:6]}-{raw_vids[30]['raw_date'][6:]}",
        "duration": "40 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Mười một năm nếm trải phong ba — Đúc thành nguyên lý nở hoa ngàn đời",
        "lead_points": [
            "Tổng kết 11 năm lăn lộn sáng tạo nội dung từ thuở sơ khai của YouTube: Các nền tảng có thể đến rồi đi, thuật toán có thể thay đổi liên tục, nhưng bản chất tâm lý con người và những nguyên lý kết nối cảm xúc là bất biến.",
            "Omar đúc kết 7 bài học đắt giá nhất: Tại sao thiết bị không quan trọng bằng ánh sáng, tại sao âm thanh quan trọng hơn hình ảnh, và tại sao sự kiên trì vượt qua thung lũng tuyệt vọng là phẩm chất duy nhất phân định người chiến thắng."
        ],
        "hero_summary": {
            "title": "Bản đồ 11 năm đúc kết nguyên lý sáng tạo nội dung bất biến",
            "items": [
                ("1. Âm thanh là 50% trải nghiệm thị giác", "Khán giả có thể kiên nhẫn xem một video hình ảnh mờ, nhưng họ sẽ tắt ngay lập tức nếu âm thanh bị rè hoặc chói tai."),
                ("2. Ánh sáng quan trọng hơn thân máy ảnh", "Một chiếc máy ảnh $500 với ánh sáng chuẩn 3 điểm cho ra khung hình đẹp gấp mười lần máy ảnh $5.000 đặt trong phòng tối."),
                ("3. Kỷ luật vượt qua sự chán nản", "Mọi người đều hào hứng trong tuần đầu tiên; người thành công là người vẫn tiếp tục bấm máy vào ngày thứ 1.000 khi không có ai vỗ tay.")
            ],
            "mantra": "Mười một năm một tấm lòng — Kiên trì gieo hạt thỏa mong cơ đồ"
        },
        "delusion": {
            "title": "ẢO TƯỞNG VỀ MÁY ẢNH ĐẮT TIỀN & SỰ THẬT VỀ CÂU CHUYỆN NỘI DUNG",
            "desc": "Người mới thường mắc phải căn bệnh 'Nghiện mua sắm thiết bị' (Gear Acquisition Syndrome): Nghĩ rằng nếu mình mua chiếc máy ảnh Sony FX3 hay ống kính G-Master thì video sẽ tự động viral. Thực tế, chiếc máy ảnh đắt tiền chỉ làm cho một nội dung nhàm chán hiển thị ở độ phân giải 4K sắc nét hơn mà thôi.",
            "compare_left": {
                "badge": "LỐI MÒN NÔNG NỔI",
                "title": "Đổ lỗi cho thiết bị thiếu thốn",
                "text": "Vay nợ mua máy móc đắt tiền rồi nhận ra mình vẫn không biết nói gì trước ống kính và lượt xem vẫn lẹt đẹt."
            },
            "compare_right": {
                "badge": "TỈNH THỨC NGHỀ NGHIỆP",
                "title": "Tập trung mài sắc thông điệp và năng lực kể chuyện",
                "text": "Dùng chính chiếc điện thoại thông minh sẵn có, học cách chiếu sáng thông minh và kể những câu chuyện lay động lòng người."
            },
            "matrix_title": "So sánh Trọng tâm Thiết bị và Trọng tâm Thông điệp",
            "matrix_items": [
                ("Trọng tâm Thiết bị (Gear-Focused)", "• Tốn kém tiền bạc, thiết lập cồng kềnh mất thời gian.<br>• Video bóng bẩy nhưng rỗng tuếch, người xem lướt qua không đọng lại gì."),
                ("Trọng tâm Thông điệp (Story-Focused)", "• Chi phí tối giản, thiết lập nhanh gọn trong 2 phút.<br>• Chạm sâu vào trái tim, thay đổi nhận thức và hành vi của người xem.")
            ],
            "mantra": "Máy móc đắt đỏ uổng công — Câu chuyện sâu sắc ấm lòng người nghe"
        },
        "insights": [
            {"num": 1, "meta": "ƯU TIÊN ÂM THANH", "title": "Âm thanh chất lượng cao là tiêu chuẩn sống còn", "ground_truth": "Người ta có thể vừa nghe video vừa làm việc khác; nếu âm thanh tồi tệ, họ sẽ rời đi ngay lập tức.", "surface": "Chi toàn bộ ngân sách mua máy ảnh đắt tiền và dùng micro tích hợp sẵn trong máy.", "nature": "Micro tích hợp thu toàn bộ tạp âm và tiếng vọng khiến giọng nói bị suy hao nghiêm trọng.", "leverage": "Đầu tư vào một chiếc micro chất lượng cao và đặt nó càng gần miệng càng tốt (khoảng cách 15–20cm).", "mantra": "Micro thu âm ấm nồng — Đi thẳng vào dạ thỏa lòng người nghe"},
            {"num": 2, "meta": "QUYỀN NĂNG ÁNH SÁNG", "title": "Ánh sáng tạo nên chất lượng điện ảnh, không phải cảm biến", "ground_truth": "Máy ảnh chỉ làm nhiệm vụ ghi lại ánh sáng; nếu ánh sáng xấu, cảm biến đắt tiền đến đâu cũng bất lực.", "surface": "Bật đèn tuýp trần nhà chiếu thẳng từ trên đỉnh đầu xuống tạo quầng thâm mắt ma quái.", "nature": "Ánh sáng dịu hướng 45 độ (Key Light lớn) tạo khối bóng đổ mềm mại tôn lên nét mặt thanh tú.", "leverage": "Dùng một đèn LED có vòm khuếch tán (Softbox) đường kính 90cm đặt góc 45 độ ngang mặt.", "mantra": "Ánh sáng mềm mại chan hòa — Khuôn mặt rạng rỡ nở hoa nụ cười"},
            {"num": 3, "meta": "CÂU CHUYỆN LÀ VUA", "title": "Cấu trúc kể chuyện vượt thời gian của Joseph Campbell (Hero's Journey)", "ground_truth": "Bộ não loài người được lập trình hàng triệu năm qua để tiếp nhận thông tin qua cấu trúc câu chuyện anh hùng vượt khó.", "surface": "Liệt kê danh sách các sự thật khô khan không có mở bài, thân bài hay cao trào.", "nature": "Các sự kiện khô khan bị lãng quên ngay; nhưng một câu chuyện có nhân vật, có nghịch cảnh và có bài học sẽ khắc sâu trọn đời.", "leverage": "Lồng ghép bài giảng vào một câu chuyện: Nhân vật gặp khó khăn -> Tìm thấy giải pháp -> Chiến thắng rực rỡ.", "mantra": "Câu chuyện bắc nhịp êm đềm — Đưa người qua bến ấm êm nụ cười"},
            {"num": 4, "meta": "TIÊU ĐỀ VÀ Ý TƯỞNG", "title": "Ý tưởng tồi không thể được cứu vãn bởi khâu hậu kỳ xuất sắc", "ground_truth": "Nếu ý tưởng gốc không đủ hấp dẫn, dù bạn có hiệu ứng kỹ xảo đẹp đến đâu video vẫn thất bại.", "surface": "Bỏ ra 40 tiếng dựng phim cho một chủ đề không ai quan tâm.", "nature": "Sự quan tâm của khán giả quyết định tiềm năng tối đa của video trước cả khi bạn bấm máy.", "leverage": "Dành 50% tổng thời gian cho khâu lên ý tưởng và hoàn thiện tiêu đề trước khi quay.", "mantra": "Ý tưởng xuất sắc mở đường — Khâu dựng tiếp bước muôn phương đón chào"},
            {"num": 5, "meta": "TÍNH NHẤT QUÁN THẬP KỶ", "title": "Sự kiên trì đều đặn đánh bại tài năng bẩm sinh", "ground_truth": "Đa số những người tài năng xuất chúng mà Omar từng biết trong 11 năm qua đều đã bỏ cuộc giữa chừng.", "surface": "Nghĩ rằng chỉ những người có năng khiếu thiên bẩm mới thành công lâu dài.", "nature": "Người có kỷ luật xuất bản đều đặn mỗi tuần sẽ liên tục tiến bộ và vượt mặt những kẻ tài năng nhưng lười biếng.", "leverage": "Cam kết với bản thân không bao giờ bỏ lỡ một tuần xuất bản nào trong suốt sự nghiệp.", "mantra": "Tài năng bỏ cuộc giữa đường — Kiên trì tiếp bước muôn phương sáng ngời"},
            {"num": 6, "meta": "THÍCH NGHI VỚI THAY ĐỔI", "title": "Không bao giờ yêu một nền tảng cụ thể nào", "ground_truth": "Vine, Periscope, Google+ từng thống trị rồi biến mất không dấu vết.", "surface": "Gắn chặt sự nghiệp vào duy nhất một nền tảng mạng xã hội.", "nature": "Các công ty công nghệ luôn ưu tiên lợi ích cổ đông của họ; họ có thể thay đổi thuật toán hoặc đóng cửa bất cứ lúc nào.", "leverage": "Luôn chuyển đổi người theo dõi từ các nền tảng thuê ngoài sang danh sách email và cộng đồng sở hữu riêng.", "mantra": "Nền tảng biến đổi khôn lường — Sở hữu danh sách muôn đường bình an"},
            {"num": 7, "meta": "SỨ MỆNH PHỤNG SỰ", "title": "Làm vì khán giả, không làm vì cái tôi của bản thân", "ground_truth": "Khi bạn chuyển trọng tâm từ 'Tôi muốn kiếm bao nhiêu tiền' sang 'Video này sẽ giúp người xem giải quyết được gì', phép màu sẽ xảy ra.", "surface": "Làm video chỉ để khoe mẽ sự thông minh và giàu có của bản thân.", "nature": "Sự kiêu ngạo tạo ra khoảng cách; tinh thần phụng sự chân thành tạo ra tình yêu thương vô điều kiện.", "leverage": "Trước khi bấm máy, chắp tay nguyện cầu: 'Xin cho những lời nói hôm nay mang lại lợi lạc thực sự cho người nghe'.", "mantra": "Tâm nguyện phụng sự nhân gian — Tiền tài danh vọng muôn vàn tự nhiên"},
            {"num": 8, "meta": "LỜI KHUYÊN CHO NGƯỜI MỚI", "title": "Bấm nút quay ngay hôm nay với những gì bạn đang có", "ground_truth": "11 năm trước Omar cũng bắt đầu bằng một chiếc máy ảnh cũ kỹ mượn của bạn bè và góc phòng chật hẹp.", "surface": "Chờ đợi đến khi có đủ tiền, đủ kiến thức và đủ sự tự tin mới dám bắt đầu.", "nature": "Sự tự tin không xuất hiện trước khi hành động; sự tự tin là kết quả sinh ra sau khi bạn đã dám hành động nhiều lần.", "leverage": "Cầm điện thoại lên, lau sạch ống kính và quay video đầu tiên ngay trong buổi tối hôm nay.", "mantra": "Bấm máy cất bước lên đường — Mười một năm nữa muôn phương rạng ngời"}
        ],
        "environment": {
            "title": "Thiết lập không gian sáng tạo bền bỉ qua năm tháng",
            "items": [
                ("1. Bàn làm việc bằng gỗ tự nhiên bền chắc", "Gợi nhắc sự vững chãi và kiên định của người làm nghề qua bao mùa bão táp."),
                ("2. Tủ chống ẩm bảo quản ống kính máy ảnh", "Bảo vệ các thấu kính đắt giá khỏi nấm mốc trong khí hậu nhiệt đới gió mùa ẩm ướt."),
                ("3. Đèn đọc sách cổ điển đặt cạnh ghế thư giãn", "Nơi ngồi đọc những trang sách hay mỗi buổi tối để nạp thêm chất liệu tri thức cho các bài giảng.")
            ],
            "mantra": "Bàn gỗ vững chãi trang nghiêm — Tủ bảo quản tốt êm đềm tháng năm"
        },
        "emotional": {
            "title": "Tâm thế của người làm nghề thâm niên trầm tĩnh",
            "items": [
                ("1. Bình thản trước mọi cơn sốt trào lưu ngắn hạn", "Hiểu rằng những gì bùng nổ quá nhanh cũng sẽ lụi tàn nhanh chóng; chỉ có giá trị thực mới trường tồn."),
                ("2. Biết ơn từng người xem đã dành thời gian cho mình", "Trân trọng từng bình luận, từng lượt xem như một món quà thiêng liêng mà cuộc đời ban tặng."),
                ("3. Giữ trọn sự say mê như ngày đầu tiên bước vào nghề", "Mỗi lần bấm máy vẫn hồi hộp và hào hứng như đứa trẻ được khám phá thế giới diệu kỳ.")
            ],
            "mantra": "Mười một năm trọn vẹn tình — Vẫn nguyên ngọn lửa lung linh buổi đầu"
        }
    }
]

BATCH_3.extend(eps)

with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch3.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
"""
episodes_batch3.py
Batch 3: 10 Episodes (OE21 - OE30)
"""

BATCH_3 = ''' + json.dumps(BATCH_3, ensure_ascii=False, indent=4) + '\n')

print(f"Hoàn tất 100% episodes_batch3.py với đầy đủ {len(BATCH_3)} tập!")
