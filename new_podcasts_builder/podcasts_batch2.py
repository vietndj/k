# -*- coding: utf-8 -*-
"""
podcasts_batch2.py
Batch 2: 6 Episodes (FO511, FO509, FO504, FO503, FO502, FO501)
"""

BATCH_2 = [
    # 8. Dr. Bhaskar Rao (FO511)
    {
        "id": "bRR9Hzi60YA",
        "slug": "dr-bhaskar-rao-hospital-economics-healthcare-truth-podcast.html",
        "ep_code": "FO511",
        "cat_badge": "08 / KINH TẾ HỌC Y TẾ & QUẢN TRỊ BỆNH VIỆN",
        "speaker": "Dr. Bhaskar Rao",
        "speaker_role": "Bác sĩ Phẫu thuật Tim mạch / Chủ tịch kiêm Tổng giám đốc Bệnh viện KIMS",
        "tagline": "KINH TẾ HỌC BỆNH VIỆN & SỰ THẬT Y TẾ HIỆN ĐẠI",
        "orig_title": "How Hospitals Make Money: KIMS, Costs & Hospital Business Truth",
        "youtube_url": "https://www.youtube.com/watch?v=bRR9Hzi60YA",
        "duration": "1 giờ 34 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Dao mổ cứu người lúc nguy nan — Trái tim y đức mới an muôn đời",
        "lead_points": [
            "Đa số người dân chỉ nhìn thấy hóa đơn viện phí đắt đỏ mà không hiểu được cấu trúc chi phí khổng lồ của công nghệ y tế, rủi ro pháp lý và trách nhiệm sinh tử của đội ngũ y bác sĩ.",
            "Dr. Bhaskar Rao bóc trần toàn bộ sự thật đằng sau mô hình kinh doanh bệnh viện: Làm thế nào để cân bằng giữa bài toán lợi nhuận sống còn và y đức cứu người không vụ lợi."
        ],
        "hero_summary": {
            "title": "Bản đồ phân rã chi phí và quản trị hệ thống y tế",
            "items": [
                ("1. Cấu trúc chi phí công nghệ cao", "Máy chụp MRI, phòng mổ vô trùng áp lực âm và hệ thống robot phẫu thuật tiêu tốn hàng triệu USD với thời gian khấu hao ngắn."),
                ("2. Tầm quan trọng của Y tế dự phòng (Preventive Care)", "Chi phí điều trị một cơn nhồi máu cơ tim gấp 100 lần chi phí xét nghiệm phát hiện sớm và điều chỉnh lối sống từ 5 năm trước."),
                ("3. Đào tạo và giữ chân nhân tài y khoa", "Đào tạo một bác sĩ phẫu thuật tim độc lập mất 15 năm; sự gắn bó của nhân sự y tế quyết định uy tín của bệnh viện.")
            ],
            "mantra": "Phòng bệnh hơn chữa bệnh nguy — Giữ thân khỏe mạnh bước đi vững vàng"
        },
        "delusion": {
            "title": "ẢO TƯỞNG VỀ BỆNH VIỆN TỪ THIỆN & THỰC TẾ CHI PHÍ Y KHOA",
            "desc": "Người bệnh thường mong muốn bệnh viện phải cung cấp dịch vụ 5 sao với giá miễn phí. Nhưng nếu bệnh viện không có lãi để tái đầu tư máy móc hiện đại và trả lương tương xứng cho chuyên gia, chất lượng điều trị sẽ suy tàn nhanh chóng.",
            "compare_left": {
                "badge": "ẢO TƯỞNG ĐÁM ĐÔNG",
                "title": "Bệnh viện tư nhân chỉ tìm cách 'chặt chém' bệnh nhân",
                "text": "Nghi ngờ mọi chỉ định xét nghiệm và phẫu thuật, cho rằng bác sĩ chỉ đang cố tình kiếm tiền hoa hồng."
            },
            "compare_right": {
                "badge": "SỰ THẬT QUẢN TRỊ Y TẾ",
                "title": "Xét nghiệm là lớp bảo hiểm an toàn sinh tử",
                "text": "Một chỉ định cận lâm sàng kỹ lưỡng giúp phát hiện các ổ nhiễm trùng tiềm ẩn hoặc bệnh lý nền nguy hiểm trước khi gây mê."
            },
            "matrix_title": "Đối chiếu giữa Chữa bệnh thụ động và Quản trị sức khỏe chủ động",
            "matrix_items": [
                ("Chữa bệnh thụ động (Late Intervention)", "• Chờ đến khi đau đớn dữ dội mới nhập viện cấp cứu.<br>• Tốn kém hàng trăm triệu đồng, biến chứng nặng nề và giảm tuổi thọ."),
                ("Quản trị sức khỏe chủ động (Preventive Medicine)", "• Khám sức khỏe định kỳ 6 tháng một lần, theo dõi chỉ số đường huyết, mỡ máu và tim mạch.<br>• Chi phí thấp, bảo tồn nguyên vẹn năng lượng sống và hiệu suất làm việc.")
            ],
            "mantra": "Để bệnh trở nặng tiêu tan — Chăm lo từ sớm ngút ngàn thảnh thơi"
        },
        "insights": [
            {
                "num": 1,
                "meta": "CỬA SỔ VÀNG CẤP CỨU",
                "title": "Thời gian là cơ tim: 60 phút quyết định sự sống còn",
                "ground_truth": "Trong cơn nhồi máu cơ tim cấp, mỗi phút trôi qua hàng triệu tế bào cơ tim sẽ chết vĩnh viễn nếu không được thông mạch vành.",
                "surface": "Nằm nghỉ ngơi tại nhà uống nước gừng và xoa dầu khi thấy đau thắt ngực, chờ đợi cơn đau tự qua đi.",
                "nature": "Tắc nghẽn động mạch vành làm ngưng trệ tuần hoàn oxy; tổn thương hoại tử cơ tim là không thể đảo ngược.",
                "leverage": "Thuộc lòng các dấu hiệu nhồi máu cơ tim (đau thắt ngực lan ra cánh tay trái) và gọi cấp cứu ngay trong giờ đầu tiên.",
                "mantra": "Giờ vàng chớp mắt qua mau — Mau vào viện kịp cứu nhau thoát nạn"
            },
            {
                "num": 2,
                "meta": "CHI PHÍ KHẤU HAO MÁY MÓC",
                "title": "Tại sao giá dịch vụ chẩn đoán hình ảnh kỹ thuật cao lại đắt",
                "ground_truth": "Một máy xạ trị ung thư công nghệ mới có giá từ 4-6 triệu USD và cần bảo trì hàng tháng với chi phí bằng cả gia tài.",
                "surface": "Nghĩ rằng nằm vào máy chụp vài phút không tốn kém gì nên giá viện phí là vô lý.",
                "nature": "Chi phí khấu hao thiết bị công nghệ cao và tiền lương của đội ngũ kỹ sư vận hành chuyên môn sâu cực kỳ đắt đỏ.",
                "leverage": "Mua bảo hiểm y tế toàn diện để được bảo vệ tài chính trước những khoản chi phí công nghệ cao bất ngờ.",
                "mantra": "Máy móc hiện đại tinh vi — Bảo hiểm trợ lực gánh đi nhọc nhằn"
            },
            {
                "num": 3,
                "meta": "TRÁCH NHIỆM BÁC SĨ PHẪU THUẬT",
                "title": "Gánh nặng tâm lý đứng trước lằn ranh sinh tử",
                "ground_truth": "Bác sĩ phẫu thuật tim phải đứng liên tục 8-10 tiếng với sự tập trung tuyệt đối vào đường khâu kích thước milimet.",
                "surface": "Xem bác sĩ như một người bán dịch vụ thông thường, phán xét thái độ khi họ ít nói cười.",
                "nature": "Áp lực tâm lý khi nắm giữ mạng sống con người đòi hỏi sự lạnh lùng và tập trung cao độ của lý trí.",
                "leverage": "Xây dựng mối quan hệ tôn trọng và hợp tác với nhân viên y tế để tạo môi trường điều trị thuận lợi nhất.",
                "mantra": "Mũi kim sợi chỉ li ti — Căng đầu tập trung gánh đi mạng người"
            },
            {
                "num": 4,
                "meta": "BẢO HIỂM Y TẾ",
                "title": "Không có bảo hiểm là canh bạc lớn nhất của đời người",
                "ground_truth": "Hàng triệu gia đình trung lưu rơi xuống đáy nghèo đói chỉ sau một biến cố bệnh hiểm nghèo của trụ cột gia đình.",
                "surface": "Nghĩ rằng mình còn trẻ khỏe nên việc mua bảo hiểm y tế là lãng phí tiền bạc hàng năm.",
                "nature": "Rủi ro bệnh tật và tai nạn tuân theo phân phối ngẫu nhiên; không ai có quyền miễn nhiễm tuyệt đối.",
                "leverage": "Ưu tiên mua bảo hiểm bệnh hiểm nghèo ngay từ khi nhận tháng lương đầu tiên trong đời.",
                "mantra": "Trời quang mây tạnh mua ô — Bão giông ập đến chẳng lo gập ghềnh"
            },
            {
                "num": 5,
                "meta": "ĐẠO ĐỨC NGHỀ Y",
                "title": "Y đức không phải là sự nghèo khó, y đức là sự trung thực",
                "ground_truth": "Bệnh viện KIMS duy trì tỷ lệ chỉ định phẫu thuật chuẩn mực, từ chối mổ nếu bệnh nhân có thể điều trị bảo tồn bằng thuốc.",
                "surface": "Đánh đồng y đức với việc bác sĩ phải làm việc không công và chịu đựng thiếu thốn cơ sở vật chất.",
                "nature": "Bác sĩ có thu nhập xứng đáng mới có thể toàn tâm toàn ý nâng cao tay nghề mà không bị cám dỗ bởi tiêu cực.",
                "leverage": "Đánh giá uy tín của một bệnh viện dựa trên tỷ lệ thành công của ca mổ và mức độ minh bạch của phác đồ điều trị.",
                "mantra": "Trung thực soi sáng tâm can — Giúp người đúng lúc muôn vàn phúc ân"
            },
            {
                "num": 6,
                "meta": "QUẢN TRỊ NHIỄM KHUẨN",
                "title": "Nhiễm khuẩn bệnh viện là sát thủ thầm lặng nguy hiểm nhất",
                "ground_truth": "Rửa tay đúng quy trình 6 bước của nhân viên y tế giúp giảm hơn 50% nguy cơ tử vong do nhiễm khuẩn chéo sau mổ.",
                "surface": "Coi nhẹ việc sát khuẩn tay và đeo khẩu trang khi vào thăm bệnh nhân trong phòng hồi sức.",
                "nature": "Vi khuẩn trong môi trường bệnh viện thường là các chủng kháng kháng sinh cực kỳ nguy hiểm.",
                "leverage": "Tuân thủ nghiêm ngặt quy định cách ly và hạn chế người nhà vào thăm bệnh nhân sau các ca mổ lớn.",
                "mantra": "Đôi tay rửa sạch tinh tươm — Ngăn ngừa vi khuẩn khôn lường lây lan"
            },
            {
                "num": 7,
                "meta": "LỐI SỐNG TIM MẠCH",
                "title": "3 kẻ thù lớn nhất hủy hoại mạch máu: Thuốc lá, Stress và Đường",
                "ground_truth": "Khói thuốc lá phá hủy trực tiếp lớp nội mạc mạch máu, tạo điều kiện cho cholesterol xấu lắng đọng thành mảng xơ vữa.",
                "surface": "Tin rằng uống thuốc bổ có thể bù đắp lại tác hại của việc hút một gói thuốc mỗi ngày.",
                "nature": "Tổn thương viêm mãn tính trong lòng mạch máu là nguyên nhân trực tiếp dẫn đến đột quỵ và nhồi máu cơ tim.",
                "leverage": "Bỏ thuốc lá ngay lập tức, cắt giảm nước ngọt có gas và duy trì chỉ số vòng eo dưới 85cm đối với nam giới.",
                "mantra": "Khói thuốc độc hại khôn cùng — Bỏ đi giữ lấy mạch thông tim lành"
            },
            {
                "num": 8,
                "meta": "TÂM LÝ BỆNH NHÂN",
                "title": "Niềm tin và ý chí sống chiếm 50% hiệu quả hồi phục",
                "ground_truth": "Những bệnh nhân có tinh thần lạc quan và sự ủng hộ của gia đình hồi phục sau phẫu thuật tim nhanh gấp đôi người tuyệt vọng.",
                "surface": "Coi cơ thể con người như một cỗ máy chỉ cần sửa chữa phần cứng sinh học.",
                "nature": "Trạng thái tinh thần tích cực kích hoạt giải phóng endorphin và tăng cường hoạt động của tế bào miễn dịch tự nhiên.",
                "leverage": "Bao quanh người bệnh bằng tình yêu thương và sự động viên tinh thần chân thành của người thân.",
                "mantra": "Thuốc hay dao sắc chưa đủ — Nụ cười niềm tin rũ sạch ưu phiền"
            }
        ],
        "environment": {
            "title": "Thiết lập môi trường sống bảo vệ hệ tim mạch gia đình",
            "items": [
                ("Máy đo huyết áp điện tử tại phòng khách", "Tập thói quen đo huyết áp mỗi tuần một lần cho cha mẹ lớn tuổi để phát hiện sớm 'kẻ giết người thầm lặng' tăng huyết áp."),
                ("Loại bỏ đồ ăn vặt nhiều muối và đường khỏi tầm mắt", "Thay thế bánh kẹo chế biến sẵn bằng các loại hạt tự nhiên (hạnh nhân, óc chó) và trái cây tươi ít ngọt.")
            ],
            "mantra": "Huyết áp theo dõi đều tay — Món ăn thanh đạm tháng ngày an khang"
        },
        "emotional": {
            "title": "Nuôi dưỡng sự bình tĩnh của thân nhân trước cửa phòng mổ",
            "items": [
                ("Đặt trọn niềm tin vào phác đồ chuyên môn của bác sĩ", "Tránh đọc những thông tin nhiễu loạn trên diễn đàn mạng gây hoang mang lo sợ không đáng có."),
                ("Giữ tâm thế kiên cường làm điểm tựa cho người bệnh", "Bộc lộ sự vững chãi khi bước vào thăm để truyền năng lượng tích cực cho bệnh nhân chiến đấu vượt qua bệnh tật.")
            ],
            "mantra": "Vững tâm làm điểm tựa người — Vượt qua giông bão rạng ngời ngày mai"
        }
    },

    # 9. Sourav Ganguly (FO509)
    {
        "id": "ZsPygh37hpw",
        "slug": "sourav-ganguly-cricket-leadership-team-building-podcast.html",
        "ep_code": "FO509",
        "cat_badge": "09 / NGHỆ THUẬT LÃNH ĐẠO & BẢN LĨNH CHIẾN TRƯỜNG",
        "speaker": "Sourav Ganguly",
        "speaker_role": "Huyền thoại Đội trưởng Cricket Ấn Độ / Cựu Chủ tịch BCCI",
        "tagline": "NGHỆ THUẬT LÃNH ĐẠO: BẢN LĨNH ĐỘI TRƯỞNG & DẪN ĐẦU",
        "orig_title": "Sourav Ganguly on Leadership, Team Building, BCCI, Match-Fixing Era & Aggression",
        "youtube_url": "https://www.youtube.com/watch?v=ZsPygh37hpw",
        "duration": "1 giờ 45 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Đứng mũi chịu sào giữa giông bão — Lãnh đạo can trường mở lối đi",
        "lead_points": [
            "Tiếp quản đội tuyển quốc gia ngay sau bê bối dàn xếp tỷ số đen tối nhất lịch sử, Sourav Ganguly đã tái sinh tinh thần chiến đấu của một dân tộc bằng lối chơi tấn công không sợ hãi.",
            "Bài học kinh điển về thuật dùng người: Cách phát hiện tài năng trẻ từ vạch xuất phát, bảo vệ đồng đội trước búa rìu dư luận và tinh thần sẵn sàng chịu trách nhiệm tuyệt đối khi thất bại."
        ],
        "hero_summary": {
            "title": "Cẩm nang lãnh đạo và chuyển hóa đội ngũ trong khủng hoảng",
            "items": [
                ("1. Lãnh đạo bằng sự dũng cảm và tấn công chủ động", "Xóa bỏ tâm lý tự ti của đội bóng nhút nhát, dạy các cầu thủ cách nhìn thẳng vào mắt đối thủ mạnh nhất thế giới."),
                ("2. Đặt niềm tin vô điều kiện vào tài năng trẻ", "Kiên quyết bảo vệ những huyền thoại tương lai (như MS Dhoni, Yuvraj Singh) qua những trận thi đấu sa sút ban đầu."),
                ("3. Đứng ra che chắn mọi chỉ trích cho đồng đội", "Khi đội bóng thua, đội trưởng nhận toàn bộ lỗi; khi đội bóng thắng, nhường toàn bộ ánh hào quang cho anh em.")
            ],
            "mantra": "Dám làm dám chịu đứng đầu — Đội quân trăm tướng một màu sắc son"
        },
        "delusion": {
            "title": "ẢO TƯỞNG LÃNH ĐẠO ÔN HÒA CẢ NỂ & BẢN LĨNH QUYẾT ĐOÁN",
            "desc": "Nhiều người lầm tưởng rằng làm lãnh đạo là phải làm hài lòng tất cả mọi người. Nhưng người lãnh đạo xuất sắc sẵn sàng đưa ra những quyết định đau đớn, loại bỏ ngôi sao sa sút để bảo vệ tinh thần chiến đấu chung của tập thể.",
            "compare_left": {
                "badge": "ẢO TƯỞNG ĐÁM ĐÔNG",
                "title": "Dĩ hòa vi quý để giữ ghế an toàn",
                "text": "Tránh né xung đột, không dám chấn chỉnh sai lầm của nhân sự kỳ cựu khiến kỷ luật đội bóng bị xói mòn."
            },
            "compare_right": {
                "badge": "BẢN LĨNH THỦ LĨNH",
                "title": "Quyết đoán thiết lập chuẩn mực mới",
                "text": "Sẵn sàng chịu chỉ trích của truyền thông để thay máu đội hình, đặt lợi ích chiến thắng của tập thể lên trên quan hệ cá nhân."
            },
            "matrix_title": "Đối chiếu giữa Người quản lý chức danh và Thủ lĩnh truyền cảm hứng",
            "matrix_items": [
                ("Người quản lý chức danh (Boss)", "• Ra lệnh bằng quyền lực hành chính, trừng phạt lỗi lầm cơ học.<br>• Nhân viên chỉ làm việc đối phó, rệu rã khi gặp nghịch cảnh."),
                ("Thủ lĩnh truyền cảm hứng (True Leader)", "• Dẫn dắt bằng tấm gương xông pha đi đầu, truyền lửa tự tin.<br>• Đồng đội sẵn sàng chiến đấu đến giọt mồ hôi cuối cùng vì niềm tin vào thủ lĩnh.")
            ],
            "mantra": "Cả nể làm hại toàn quân — Can trường quyết đoán muôn phần thắng to"
        },
        "insights": [
            {
                "num": 1,
                "meta": "CHỊU TRÁCH NHIỆM",
                "title": "Quy tắc cốt lõi: Nhận lỗi về mình, chia vinh quang cho đội",
                "ground_truth": "Trong mọi cuộc họp báo sau thất bại cay đắng, Ganguly luôn khẳng định chiến thuật của ông sai chứ không bao giờ đổ lỗi cho cá nhân cầu thủ.",
                "surface": "Lãnh đạo tìm người để đổ trách nhiệm và thanh minh cho sự yếu kém của bản thân.",
                "nature": "Nếu cấp dưới sợ bị trừng phạt khi thất bại, họ sẽ không bao giờ dám sáng tạo hay dấn thân vào những tình huống khó.",
                "leverage": "Luôn là người đầu tiên đứng ra nhận trách nhiệm trước ban giám đốc và khách hàng khi dự án gặp sự cố.",
                "mantra": "Thất bại nhận hết về mình — Thành công nhường bạn trọn tình anh em"
            },
            {
                "num": 2,
                "meta": "PHÁT HIỆN TÀI NĂNG",
                "title": "Nhìn ra ngọn lửa trong mắt chứ không chỉ xem bảng thành tích",
                "ground_truth": "Ganguly đã đấu tranh với ban tuyển chọn để giữ lại Sehwag và Yuvraj dù họ có khởi đầu mùa giải không ấn tượng.",
                "surface": "Chỉ tuyển dụng những người có CV hoàn hảo và điểm số kiểm tra an toàn.",
                "nature": "Bản lĩnh thi đấu dưới áp lực sinh tử không thể đo lường bằng bài kiểm tra lý thuyết; nó thể hiện qua ánh mắt khát khao chiến thắng.",
                "leverage": "Quan sát phản ứng của ứng viên khi gặp thất bại trong quá khứ để đánh giá sức bền tâm lý thực sự.",
                "mantra": "Nhìn sâu vào mắt anh tài — Thấy mầm dũng khí tương lai rạng ngời"
            },
            {
                "num": 3,
                "meta": "TINH THẦN QUẢ CẢM",
                "title": "Hành động cởi áo trên ban công Lord's: Đập tan sự tự ti thuộc địa",
                "ground_truth": "Khoảnh khắc Ganguly cởi áo ăn mừng chiến thắng tại thánh địa Lord's đã thay đổi vĩnh viễn tâm lý của thể thao Ấn Độ.",
                "surface": "Bị truyền thông phương Tây chỉ trích là thiếu lịch thiệp và quá hung hăng.",
                "nature": "Để phá vỡ sự tự ti thâm căn cố đế của một tập thể, thủ lĩnh phải thực hiện một hành vi bộc phát phá vỡ mọi ranh giới ước lệ.",
                "leverage": "Dám thể hiện cảm xúc mãnh liệt và tinh thần tự hào về nguồn cội để truyền cảm hứng cho cấp dưới.",
                "mantra": "Bung áo xóa sạch tự ti — Rền vang tiếng thét uy nghi sơn hà"
            },
            {
                "num": 4,
                "meta": "ỦY QUYỀN TRÊN SÂN",
                "title": "Tự do trong khuôn khổ: Trao quyền tối đa cho chuyên gia",
                "ground_truth": "Khi trao bóng cho các tay ném trẻ, Ganguly chỉ nói một câu: 'Hãy sắp xếp vị trí phòng thủ theo ý cậu, tôi tin cậu'.",
                "surface": "Vi mô quản lý (Micromanagement), chỉ đạo từng bước chạy khiến cầu thủ bị căng cứng cơ bắp.",
                "nature": "Con người chỉ phát huy 100% năng lực tiềm ẩn khi họ cảm thấy mình là chủ nhân thực sự của quyết định đó.",
                "leverage": "Xác định rõ mục tiêu cuối cùng và để nhân sự tự do lựa chọn phương pháp thực thi trong phạm vi ngân sách.",
                "mantra": "Trao quyền gửi trọn niềm tin — Tự do vùng vẫy giữ gìn chiến công"
            },
            {
                "num": 5,
                "meta": "VƯỢT QUA TẨY CHAY",
                "title": "Bị tước băng đội trưởng và sự trở lại ngoạn mục bằng gậy",
                "ground_truth": "Sau khi bị huấn luyện viên Greg Chappell đẩy ra khỏi đội tuyển, Ganguly quay về giải nội địa tập luyện cật lực và trở lại giành danh hiệu cầu thủ xuất sắc nhất.",
                "surface": "Than vãn bất công, đổ lỗi cho chính trị nội bộ và từ bỏ sự nghiệp trong cay đắng.",
                "nature": "Màn đáp trả đanh thép nhất trước mọi định kiến và trù dập là kết quả thực tế trên sân cỏ.",
                "leverage": "Khi bị giáng chức hoặc đối xử bất công, hãy im lặng tuyệt đối và để năng lực thực chiến lên tiếng thay bạn.",
                "mantra": "Bị hắt hủi chớ oán hờn — Lặng im mài gậy tiếng vang đáp lời"
            },
            {
                "num": 6,
                "meta": "QUẢN TRỊ NGÔI SAO",
                "title": "Tôn trọng cái tôi của ngôi sao nhưng giữ vững kỷ luật chung",
                "ground_truth": "Đội hình thời Ganguly có những cá tính khổng lồ như Sachin Tendulkar, Rahul Dravid, Anil Kumble nhưng không bao giờ có bè phái.",
                "surface": "Tìm cách đè bẹp cá tính của các ngôi sao để chứng tỏ quyền lực của thủ lĩnh.",
                "nature": "Tập thể vĩ đại được tạo nên từ những cá nhân kiệt xuất; lãnh đạo khôn ngoan biết hòa sắc màu của họ vào một bức tranh lớn.",
                "leverage": "Giao nhiệm vụ danh dự tương xứng với tầm vóc của từng ngôi sao để họ cảm thấy được tôn trọng tối đa.",
                "mantra": "Núi cao gom góp đá to — Thủ lĩnh kết nối chẳng lo tranh giành"
            },
            {
                "num": 7,
                "meta": "BẢN LĨNH NGOẠI GIAO",
                "title": "Từ vận động viên đến chủ tịch cơ quan quyền lực nhất môn thể thao",
                "ground_truth": "Trên cương vị Chủ tịch BCCI, Ganguly đàm phán hợp đồng bản quyền truyền hình IPL trị giá hơn 6 tỷ USD kỷ lục.",
                "surface": "Nghĩ rằng vận động viên chỉ có cơ bắp, không thể làm kinh tế hay quản trị chính trị thể thao.",
                "nature": "Sự thấu hiểu sâu sắc từ góc nhìn người trong cuộc kết hợp với tư duy chiến lược tạo ra lợi thế đàm phán áp đảo.",
                "leverage": "Không ngừng học hỏi kiến thức pháp lý và tài chính để sẵn sàng bước lên vũ đài quản trị cấp cao sau khi giải nghệ.",
                "mantra": "Rời sân bước tới chính trường — Tư duy chiến lược mở đường thênh thang"
            },
            {
                "num": 8,
                "meta": "TRIẾT LÝ DI SẢN",
                "title": "Thước đo của người lãnh đạo là số lượng nhà lãnh đạo họ tạo ra",
                "ground_truth": "Dưới bàn tay dìu dắt của Ganguly, thế hệ tiếp theo đã sản sinh ra MS Dhoni và Virat Kohli — những người tiếp tục đưa đội bóng lên đỉnh thế giới.",
                "surface": "Sợ cấp dưới giỏi hơn sẽ soán ngôi và làm lu mờ tên tuổi của mình.",
                "nature": "Người lãnh đạo bất tử là người xây dựng được một thế hệ kế cận mạnh mẽ hơn chính bản thân mình.",
                "leverage": "Chủ động huấn luyện và tạo điều kiện cho các trợ lý trẻ thử sức ở các vị trí chỉ huy dự án quan trọng.",
                "mantra": "Thầy giỏi đào tạo trò tài — Tre già măng mọc tương lai vững vàng"
            }
        ],
        "environment": {
            "title": "Thiết kế văn hóa phòng thay đồ gắn kết như gia đình",
            "items": [
                ("Bữa ăn tập thể bắt buộc sau mỗi buổi tập", "Mọi thành viên từ ngôi sao triệu đô đến tân binh mới vào đội đều ngồi chung một bàn, cấm sử dụng điện thoại để trò chuyện cởi mở."),
                ("Góc vinh danh đóng góp thầm lặng", "Biểu dương các nhân viên hậu cần, bác sĩ trị liệu và trợ lý trước toàn đội sau mỗi chiến dịch thành công.")
            ],
            "mantra": "Chung mâm chung chén đậm đà — Kề vai sát cánh như nhà ruột rà"
        },
        "emotional": {
            "title": "Rèn luyện thần kinh thép trước sức ép của 1 tỷ người hâm mộ",
            "items": [
                ("Miễn nhiễm với cơn lốc truyền thông và mạng xã hội", "Tắt toàn bộ tin tức báo chí trong suốt thời gian diễn ra giải đấu lớn để bảo vệ tâm trí khỏi sự phán xét."),
                ("Tập trung 100% vào quả bóng tiếp theo", "Quên ngay cú đánh hỏng vừa xảy ra; trong thể thao đỉnh cao, quá khứ đã chết chỉ có khoảnh khắc này là có thật.")
            ],
            "mantra": "Mặc cho dư luận râm ran — Trụ tâm một điểm đàng hoàng lập công"
        }
    }
]
print(f"Loaded {len(BATCH_2)} episodes in batch 2 (part 1).")

# 10. Lakshya Sen (FO504)
BATCH_2.append({
    "id": "23dbj3silMU",
    "slug": "lakshya-sen-olympic-champion-mindset-resilience-podcast.html",
    "ep_code": "FO504",
    "cat_badge": "10 / THỂ THAO ĐỈNH CAO & TÂM LÝ CHIẾN BINH",
    "speaker": "Lakshya Sen",
    "speaker_role": "Tay vợt Cầu lông Olympic / Nhà vô địch Commonwealth Games",
    "tagline": "TÂM THÁI OLYMPIC: VƯỢT NỖI ĐAU THẤT BẠI & TRỞ LẠI",
    "orig_title": "Lakshya Sen on Champion Mindset, Olympic Heartbreak, Injuries & Comebacks",
    "youtube_url": "https://www.youtube.com/watch?v=23dbj3silMU",
    "duration": "1 giờ 28 phút",
    "read_time": "~8 phút chắt lọc",
    "hero_quote": "Thất bại thắt lại từng cơn — Đứng lên lau lệ đặng đền ơn non",
    "lead_points": [
        "Sau trận tranh huy chương đồng Olympic Paris nghẹt thở và đầy tiếc nuối, Lakshya Sen đã phải đối diện với sự sụp đổ cảm xúc tột cùng trước khi tìm lại ngọn lửa chiến đấu.",
        "Bài học về việc biến nỗi đau thành nhiên liệu tinh thần: Cách vượt qua những chấn thương thể xác tàn khốc, kỷ luật tập luyện khổ hạnh và triết lý xem mỗi trận đấu là một canh bạc sinh tử."
    ],
    "hero_summary": {
        "title": "Bản thiết kế tinh thần chiến binh thể thao đỉnh cao",
        "items": [
            ("1. Chấp nhận và giải tỏa nỗi đau thất bại", "Không trốn tránh cảm giác cay đắng; khóc cho cạn nước mắt rồi ngay lập tức quay lại phân tích băng ghi hình lỗi kỹ thuật."),
            ("2. Kỷ luật phục hồi sau chấn thương phẫu thuật", "Kiên nhẫn tập từng bước đi nhỏ trên thảm tập khi các đối thủ đang thi đấu giành cúp khắp thế giới."),
            ("3. Tâm lý 'Match Point' dưới áp lực nghẹt thở", "Rèn luyện khả năng đóng băng cảm xúc khi khán đài 10.000 người đang gào thét, chỉ tập trung vào đường bay của quả cầu.")
        ],
        "mantra": "Gục ngã một thoáng đau thương — Vươn vai đứng dậy can trường tiến lên"
    },
    "delusion": {
        "title": "ẢO TƯỞNG THIÊN PHÚ TỰ NHIÊN & GIÁ PHẢI TRẢ CỦA TẤM HUY CHƯƠNG",
        "desc": "Khán giả chỉ nhìn thấy những pha cứu cầu không tưởng trên sóng truyền hình mà không biết rằng phía sau là 15 năm sống xa gia đình, tập luyện 8 tiếng mỗi ngày từ năm 10 tuổi và đôi chân đầy vết sẹo phẫu thuật.",
        "compare_left": {
            "badge": "ẢO TƯỞNG ĐÁM ĐÔNG",
            "title": "Nghĩ rằng nhà vô địch không biết sợ hãi",
            "text": "Tin rằng các vận động viên đỉnh cao sinh ra đã có thần kinh thép bẩm sinh, không bao giờ lo lắng hay run rẩy."
        },
        "compare_right": {
            "badge": "SỰ THẬT ĐẤU TRƯỜNG",
            "title": "Chiến đấu cùng với nỗi sợ hãi",
            "text": "Tim vẫn đập thình thịch trong lồng ngực nhưng cơ thể đã được huấn luyện tự động thực hiện động tác chuẩn xác nhờ hàng triệu lần lặp lại."
        },
        "matrix_title": "So sánh giữa Vận động viên phong trào và Chiến binh Olympic",
        "matrix_items": [
            ("Vận động viên phong trào", "• Tập luyện khi thấy hưng phấn, bỏ tập khi thời tiết xấu hoặc đau nhức cơ bắp.<br>• Mất tinh thần cả tuần chỉ vì thua một set đấu giao hữu."),
            ("Chiến binh Olympic", "• Coi cơn đau cơ bắp và mồ hôi là người bạn đồng hành quen thuộc mỗi ngày.<br>• Reset tâm trí về con số 0 ngay sau mỗi pha cầu, dù vừa ghi điểm hay mất điểm.")
        ],
        "mantra": "Mồ hôi thấm đẫm sàn đấu — Đổi lấy giây phút huy hoàng vinh quang"
    },
    "insights": [
        {
            "num": 1,
            "meta": "TÂM LÝ HỌC THẤT BẠI",
            "title": "Nỗi đau thua trận tại Olympic là người thầy vĩ đại nhất",
            "ground_truth": "Dẫn trước ở set 1 nhưng thua ngược ở set 2 và set 3 trong trận tranh huy chương đồng Paris 2024 là bài học đắt giá nhất sự nghiệp Lakshya Sen.",
            "surface": "Tìm lý do đổ lỗi cho trọng tài, ánh sáng nhà thi đấu hay vận xui để xoa dịu cái tôi.",
            "nature": "Thất bại chỉ ra chính xác lỗ hổng về sức bền chiến thuật và sự nôn nóng trong thời điểm quyết định.",
            "leverage": "Mổ xẻ từng pha cầu hỏng trong 24 giờ sau trận đấu, ghi chép vào sổ tay chiến thuật để biến điểm yếu thành vũ khí mới.",
            "mantra": "Cay đắng khắc dạ ghi lòng — Rút ra bài học mới mong chuyển mình"
        },
        {
            "num": 2,
            "meta": "KỶ LUẬT PHỤC HỒI",
            "title": "Chiến thắng thực sự diễn ra trong phòng vật lý trị liệu",
            "ground_truth": "Ca phẫu thuật mũi và chấn thương lưng từng khiến Lakshya phải nằm bất động suốt nhiều tuần, tụt dốc thê thảm trên bảng xếp hạng thế giới.",
            "surface": "Nôn nóng trở lại sân tập quá sớm khi cơ thể chưa hoàn toàn hồi phục, dẫn đến tái phát chấn thương nặng hơn.",
            "nature": "Sự kiên nhẫn trong giai đoạn phục hồi đòi hỏi sức mạnh tinh thần gấp bội so với việc thi đấu trên sân.",
            "leverage": "Tuân thủ nghiêm ngặt phác đồ kéo giãn cơ, ngâm bồn nước đá và bài tập phục hồi chức năng của chuyên gia thể lực.",
            "mantra": "Chấn thương rèn giũa lòng kiên — Lặng thầm tích lũy bình yên trở về"
        },
        {
            "num": 3,
            "meta": "CẮT BỎ NHIỄU SỐ",
            "title": "Chế độ cô lập tuyệt đối trước thềm các giải đấu lớn",
            "ground_truth": "Huấn luyện viên Padukone đã tịch thu toàn bộ điện thoại thông minh của Lakshya Sen trong suốt 3 tháng chuẩn bị cho Olympic.",
            "surface": "Lướt mạng xã hội xem những lời khen ngợi và kỳ vọng của người hâm mộ để lấy động lực.",
            "nature": "Kỳ vọng của đám đông là chiếc balo đá tảng đè nặng lên đôi vai của vận động viên trong thời khắc căng thẳng.",
            "leverage": "Cắt đứt toàn bộ liên lạc với thế giới mạng xã hội trước mỗi kỳ thi hoặc dự án sinh tử của cuộc đời.",
            "mantra": "Bỏ ngoài tai vạn lời khen — Giữ tâm thanh tịnh ánh đèn sáng trong"
        },
        {
            "num": 4,
            "meta": "TỐC ĐỘ PHẢN XẠ",
            "title": "Quả cầu bay 400 km/h: Phản xạ vô thức thay thế suy nghĩ lý trí",
            "ground_truth": "Cầu lông là môn thể thao dùng vợt nhanh nhất hành tinh; thời gian phản xạ chỉ tính bằng phần mười giây.",
            "surface": "Cố gắng suy nghĩ và phân tích quỹ đạo cầu bằng tư duy logic trong khi đối thủ smash.",
            "nature": "Tư duy lý trí quá chậm; não bộ phải chuyển quyền điều khiển cho tiểu não và trí nhớ cơ bắp (Muscle Memory).",
            "leverage": "Lặp lại bài tập phản xạ cầu đa hướng 10.000 lần cho đến khi cơ thể tự động phản ứng mà không cần suy nghĩ.",
            "mantra": "Cầu bay xé gió ngút trời — Tay vung chính xác chẳng rời một li"
        },
        {
            "num": 5,
            "meta": "HY SINH TUỔI TRẺ",
            "title": "Cái giá của sự xuất sắc: Từ bỏ cuộc sống bình thường của tuổi 20",
            "ground_truth": "Từ năm 10 tuổi, Lakshya đã sống trong học viện xa gia đình, không tiệc tùng, không rạp chiếu phim, không kỳ nghỉ cuối tuần.",
            "surface": "Muốn trở thành nhà vô địch thế giới nhưng vẫn đòi hỏi có thời gian đi chơi, thức khuya như bạn bè đồng trang lứa.",
            "nature": "Quy luật đánh đổi không khoan nhượng: Để đạt được điều 99,99% người khác không có, bạn phải chịu đựng những điều 99,99% người khác không chịu nổi.",
            "leverage": "Chấp nhận sự cô đơn và đơn điệu như một phần tất yếu của hành trình theo đuổi sự hoàn hảo.",
            "mantra": "Tuổi xuân gửi lại sân tập — Đổi lấy tên tuổi tạc vào non sông"
        },
        {
            "num": 6,
            "meta": "SỰ ĐỒNG HÀNH GIA ĐÌNH",
            "title": "Hậu phương thầm lặng: Gia đình là bệ phóng niềm tin",
            "ground_truth": "Cha của Lakshya — một huấn luyện viên cầu lông — đã đồng hành cùng con trai từ những bước chạy đầu tiên trên sân xi măng gồ ghề.",
            "surface": "Nghĩ rằng vận động viên có thể đơn độc chinh phục thế giới mà không cần điểm tựa tình cảm.",
            "nature": "Tình yêu thương vô điều kiện của gia đình là chiếc lưới an toàn giúp vận động viên dám mạo hiểm tung hết sức mình.",
            "leverage": "Luôn bày tỏ lòng biết ơn và giữ liên lạc ấm áp với gia đình sau mỗi chuyến du đấu xa nhà.",
            "mantra": "Công cha nghĩa mẹ sinh thành — Điểm tựa vững chãi chắp cánh bay xa"
        },
        {
            "num": 7,
            "meta": "CHIẾN THUẬT BIẾN THIÊN",
            "title": "Không bao giờ dùng một bài đánh với đối thủ đẳng cấp",
            "ground_truth": "Khi đối đầu với Viktor Axelsen, việc chỉ dùng lối đánh phòng thủ phản công cũ kỹ sẽ bị đối thủ bắt bài và đè bẹp hoàn toàn.",
            "surface": "Trung thành mù quáng với sở trường cũ ngay cả khi nó đang bị đối phương khai thác triệt để.",
            "nature": "Đỉnh cao thể thao là cuộc đấu trí tiến hóa liên tục; kẻ nào không dám thay đổi phong cách sẽ trở thành mồi ngon.",
            "leverage": "Chủ động học hỏi các kỹ thuật tấn công lưới mới và rèn luyện thể lực để tăng tính biến hóa trong lối chơi.",
            "mantra": "Biến hóa khôn lường trên sân — Địch không bắt mạch muôn phần vẻ vang"
        },
        {
            "num": 8,
            "meta": "KHÁT VỌNG TƯƠNG LAI",
            "title": "Mục tiêu không bao giờ thay đổi: Tấm huy chương vàng Los Angeles 2028",
            "ground_truth": "Ngay khi rời Paris trong nước mắt, Lakshya đã bắt đầu chu kỳ tập luyện 4 năm tiếp theo hướng tới kỳ Olympic Los Angeles.",
            "surface": "Gục ngã và đánh mất niềm tin vào bản thân sau một giải đấu lớn không như ý.",
            "nature": "Sự nghiệp thể thao là một cuộc chạy marathon trường kỳ; kẻ chiến thắng cuối cùng là kẻ không bao giờ từ bỏ đường đua.",
            "leverage": "Xem mỗi thất bại là một khoản đầu tư cho chiến thắng vĩ đại hơn trong tương lai.",
            "mantra": "Paris dang dở niềm mơ — Bốn năm tôi luyện đợi cờ vinh quang"
        }
    ],
    "environment": {
        "title": "Thiết lập kỷ luật sinh hoạt chuẩn vận động viên chuyên nghiệp",
        "items": [
            ("Phòng ngủ tối ưu hóa phục hồi sâu", "Sử dụng đệm chỉnh hình, rèm cản sáng 100% và máy tạo ẩm để tối đa hóa thời gian ngủ sâu (Deep Sleep) tái tạo mô cơ."),
            ("Nhật ký theo dõi chỉ số thể chất hàng ngày", "Ghi lại nhịp tim khi nghỉ ngơi (Resting Heart Rate), mức độ đau mỏi cơ bắp và lượng calo tiêu thụ mỗi tối.")
        ],
        "mantra": "Ngủ sâu phục hồi cơ bắp — Nhật ký theo dõi từng ngày tiến xa"
    },
    "emotional": {
        "title": "Rèn luyện sự bình thản trước vinh quang và cay đắng",
        "items": [
            ("Xem thể thao là một trò chơi cuộc đời (Play the Game)", "Dốc hết 100% năng lượng chiến đấu nhưng không để kết quả thắng thua định đoạt giá trị nhân phẩm của mình."),
            ("Giữ ngọn lửa đam mê thuần khiết của cậu bé 10 tuổi", "Nhớ lại lý do đầu tiên bạn cầm cây vợt lên: Không phải vì tiền hay huy chương, mà vì niềm vui sướng khi quả cầu chạm mặt vợt.")
        ],
        "mantra": "Thắng không kiêu ngạo vênh vang — Bại không nản chí hiên ngang kiên cường"
    }
})

# 11. Mark Manson (FO503)
BATCH_2.append({
    "id": "ig1VtIEFkcI",
    "slug": "mark-manson-psychology-of-love-toxic-relationships-podcast.html",
    "ep_code": "FO503",
    "cat_badge": "11 / TÂM LÝ HỌC HIỆN ĐẠI & QUAN HỆ ĐỘC HẠI",
    "speaker": "Mark Manson",
    "speaker_role": "Tác giả Best-seller Toàn cầu (Nghệ Thuật Tinh Tế Của Việc Đếch Quan Tâm)",
    "tagline": "TÂM LÝ HỌC TÌNH YÊU: BẪY ÁI KỶ & BẢN LĨNH ĐÀN ÔNG",
    "orig_title": "Psychology of Love: Narcissism, Toxic Love & Male Identity",
    "youtube_url": "https://www.youtube.com/watch?v=ig1VtIEFkcI",
    "duration": "1 giờ 56 phút",
    "read_time": "~9 phút chắt lọc",
    "hero_quote": "Quan tâm chi chuyện viển vông — Giữ lòng trong sáng sống không thẹn thò",
    "lead_points": [
        "Văn hóa hiện đại đang cổ súy cho sự ái kỷ độc hại và những mối quan hệ phụ thuộc lẫn nhau (Codependency), nơi con người dùng tình yêu để khỏa lấp sự trống rỗng trong tâm hồn.",
        "Mark Manson bóc tách góc tối của tâm lý học tình cảm: Sự thật về tính nam hiện đại, ranh giới cá nhân lành mạnh và cách từ bỏ thói quen tìm kiếm sự công nhận phù phiếm từ người khác."
    ],
    "hero_summary": {
        "title": "Bản đồ giải mã ranh giới cảm xúc và tâm lý độc hại",
        "items": [
            ("1. Phân biệt Tình yêu lành mạnh và Bẫy ái kỷ (Narcissism)", "Tình yêu độc hại đòi hỏi đối phương phải chịu trách nhiệm cho cảm xúc của mình; tình yêu lành mạnh là hai cá nhân độc lập cùng chia sẻ cuộc sống."),
            ("2. Nghệ thuật thiết lập Ranh giới cá nhân (Boundaries)", "Dám nói 'Không' và sẵn sàng rời bỏ mối quan hệ nếu các giá trị cốt lõi bị giẫm đạp."),
            ("3. Cuộc khủng hoảng bản sắc của nam giới hiện đại", "Nam giới rơi vào bẫy cô đơn vì thiếu những người bạn tâm giao thực sự và bị định kiến xã hội ép phải kìm nén cảm xúc.")
        ],
        "mantra": "Ranh giới vạch rõ rõ ràng — Tôn trọng lẫn nhau mới an một đời"
    },
    "delusion": {
        "title": "ẢO TƯỞNG CẢM XÚC KỊCH TÍNH & SỰ BÌNH YÊN BỀN VỮNG",
        "desc": "Nhiều người nhầm lẫn giữa sự bất an, ghen tuông kịch tính (Drama) với tình yêu say đắm. Thực chất những mối quan hệ độc hại kích hoạt chu kỳ nghiện hormone hệt như cờ bạc; tình yêu thực sự thường mang lại cảm giác bình yên, nhẹ nhàng và đôi khi hơi nhàm chán.",
        "compare_left": {
            "badge": "ẢO TƯỞNG ĐÁM ĐÔNG",
            "title": "Tình yêu là phải đau đớn, cãi vã rồi làm lành say đắm",
            "text": "Nghiện cảm giác kịch tính lên bổng xuống trầm, coi sự kiểm soát và ghen tuông là minh chứng của tình yêu chân thật."
        },
        "compare_right": {
            "badge": "TÂM LÝ HỌC THỰC THỰC",
            "title": "Tình yêu là sự an toàn, tin cậy và tôn trọng ranh giới",
            "text": "Cả hai không cần phải thăm dò hay phòng thủ, hoàn toàn tự do theo đuổi mục tiêu cá nhân mà không sợ bị phán xét."
        },
        "matrix_title": "So sánh giữa Mối quan hệ độc hại và Mối quan hệ trưởng thành",
        "matrix_items": [
            ("Mối quan hệ độc hại (Toxic Attachment)", "• 'Em làm anh buồn, em phải xin lỗi và sửa đổi'.<br>• Dùng sự dỗi hờn, im lặng hoặc đe dọa để thao túng hành vi của đối phương."),
            ("Mối quan hệ trưởng thành (Healthy Boundaries)", "• 'Anh cảm thấy buồn vì sự việc X, nhưng anh chịu trách nhiệm cho cảm xúc của chính mình'.<br>• Tôn trọng sự khác biệt và sẵn sàng đối thoại thẳng thắn.")
        ],
        "mantra": "Kịch tính cay đắng nghiện ngập — Bình yên thanh thản mới là bến neo"
    },
    "insights": [
        {
            "num": 1,
            "meta": "RANH GIỚI CÁ NHÂN",
            "title": "Bạn chịu trách nhiệm cho cảm xúc của mình, không phải của người khác",
            "ground_truth": "Phần lớn các mối quan hệ độc hại bắt nguồn từ việc một người cố gắng 'sửa chữa' hoặc 'cứu vớt' cảm xúc bất ổn của người kia.",
            "surface": "Cảm thấy có lỗi và hoảng sợ mỗi khi bạn đời buồn bã hoặc tức giận.",
            "nature": "Mỗi người trưởng thành phải tự sở hữu và chịu trách nhiệm cho phản ứng sinh học của chính mình.",
            "leverage": "Nói rõ ràng: 'Tôi yêu bạn và sẵn sàng lắng nghe, nhưng tôi không thể chịu trách nhiệm cho việc làm bạn vui lên'.",
            "mantra": "Cảm xúc của ai nấy lo — Giúp nhau lắng nghe chẳng gò ép nhau"
        },
        {
            "num": 2,
            "meta": "BẪY ÁI KỶ HIỆN ĐẠI",
            "title": "Tâm lý nạn nhân là một dạng ái kỷ ngược tinh vi",
            "ground_truth": "Những người luôn than vãn 'Tại sao mọi điều tồi tệ chỉ xảy ra với tôi?' thực chất đang tự đặt mình làm trung tâm vũ trụ.",
            "surface": "Thương hại và cố gắng cung phụng một người luôn đóng vai nạn nhân của cuộc đời.",
            "nature": "Tâm lý nạn nhân giúp họ né tránh trách nhiệm hành động và thao túng người khác bằng sự tội lỗi.",
            "leverage": "Từ chối tham gia vào vở kịch than vãn; đặt câu hỏi: 'Bạn định làm gì cụ thể để giải quyết vấn đề đó?'.",
            "mantra": "Than thân trách phận làm chi — Tự mình đứng dậy bước đi đàng hoàng"
        },
        {
            "num": 3,
            "meta": "SỰ TỪ BỎ LÀNH MẠNH",
            "title": "Năng lực nói 'Không' là nền móng của sự chân thật",
            "ground_truth": "Một mối quan hệ mà bạn không thể nói 'Không' mà không sợ bị trừng phạt là một mối quan hệ độc tài.",
            "surface": "Luôn giả vờ đồng ý với mọi sở thích và yêu cầu của bạn đời để giữ hòa khí giả tạo.",
            "nature": "Sự đồng ý chỉ có giá trị khi người ta có quyền tự do từ chối mà vẫn được tôn trọng.",
            "leverage": "Dũng cảm từ chối những lời đề nghị đi ngược lại giá trị cá nhân; quan sát phản ứng của đối phương để kiểm tra độ lành mạnh.",
            "mantra": "Dám nói lời 'Không' chân thành — Tình yêu mới thắm bền lành dài lâu"
        },
        {
            "num": 4,
            "meta": "TÍNH NAM HIỆN ĐẠI",
            "title": "Đàn ông hiện đại cần những tình bạn có chiều sâu cảm xúc",
            "ground_truth": "Hơn 60% đàn ông hiện đại thú nhận họ không có lấy một người bạn thân mà họ có thể tâm sự những bất an thầm kín.",
            "surface": "Tụ tập nhậu nhẹt, chơi game đông vui nhưng chỉ nói chuyện thể thao, công việc bề nổi.",
            "nature": "Sự cô đơn cảm xúc khiến đàn ông dồn toàn bộ gánh nặng tâm lý lên vai người vợ hoặc bạn gái, bóp nghẹt mối quan hệ.",
            "leverage": "Chủ động xây dựng nhóm bạn thân cùng rèn luyện, dám chia sẻ những khó khăn và nỗi sợ mà không sợ bị phán xét.",
            "mantra": "Bạn nhậu ngàn chén dễ say — Tri kỷ tâm giao mấy ai tìm cùng"
        },
        {
            "num": 5,
            "meta": "NGHỆ THUẬT BUÔNG BỎ",
            "title": "Chọn việc để quan tâm: Tinh hoa của cuốn sách Best-seller",
            "ground_truth": "Năng lượng và sự chú ý của con người là hữu hạn; nếu bạn quan tâm đến mọi thứ, bạn sẽ bị cuộc đời xé nát.",
            "surface": "Bực bội vì một bình luận ác ý trên mạng, lo lắng vì ánh mắt soi mói của người lạ ngoài đường.",
            "nature": "Trưởng thành là quá trình tàn nhẫn gạt bỏ những điều vớ vẩn để chỉ giữ lại 2-3 giá trị cốt lõi đáng để chiến đấu.",
            "leverage": "Mỗi sáng tự hỏi: 'Hôm nay điều gì thực sự xứng đáng với năng lượng quý giá của tôi?'.",
            "mantra": "Mặc cho miệng thế khen chê — Giữ tâm vững chãi hướng về điều hay"
        },
        {
            "num": 6,
            "meta": "NGHỊCH LÝ SỰ HOÀN HẢO",
            "title": "Theo đuổi sự hoàn hảo là con đường ngắn nhất dẫn đến bất hạnh",
            "ground_truth": "Mọi cuộc sống đều đi kèm với những vấn đề và rắc rối riêng; hạnh phúc nằm ở việc chọn được những vấn đề bạn thích giải quyết.",
            "surface": "Mơ ước một cuộc đời hoàn hảo không có khó khăn, không có mâu thuẫn hay thất bại.",
            "nature": "Cuộc sống là một chuỗi giải quyết vấn đề liên tục; hết vấn đề này sẽ có vấn đề khác xuất hiện.",
            "leverage": "Đừng hỏi 'Làm sao để hết khổ?', hãy hỏi 'Tôi sẵn sàng chịu đựng nỗi đau nào để đạt được mục tiêu này?'.",
            "mantra": "Đời là biển khổ mênh mông — Chọn điều xứng đáng mà gồng mình qua"
        },
        {
            "num": 7,
            "meta": "CHÂN THẬT TRIỆT ĐỂ",
            "title": "Sự dễ bị tổn thương (Vulnerability) là nguồn gốc của sự dũng cảm",
            "ground_truth": "Những người cố tỏ ra mạnh mẽ và không bao giờ bộc lộ điểm yếu thực chất là những kẻ nhát gan sợ bị từ chối nhất.",
            "surface": "Xây dựng lớp vỏ bọc hoàn hảo, lạnh lùng để bảo vệ bản thân khỏi những tổn thương tình cảm.",
            "nature": "Bạn không thể trải nghiệm tình yêu sâu sắc nếu không dám mở lòng chấp nhận rủi ro bị từ chối.",
            "leverage": "Dám thừa nhận: 'Tôi đang cảm thấy bất an và tôi cần sự giúp đỡ của bạn' trong những cuộc trò chuyện quan trọng.",
            "mantra": "Mở lòng phơi trải thật lòng — Dũng cảm đón nhận mới mong vẹn toàn"
        },
        {
            "num": 8,
            "meta": "CÁI CHẾT VÀ Ý NGHĨA",
            "title": "Bản di chúc tâm linh: Bạn muốn người ta nhớ về mình thế nào?",
            "ground_truth": "Trong đám tang của bạn, không ai nhắc đến số tiền trong tài khoản hay chức danh giám đốc; họ chỉ nhớ cách bạn đối xử với họ.",
            "surface": "Hy sinh toàn bộ các mối quan hệ và sức khỏe để đổi lấy những con số tài sản vô tri.",
            "nature": "Ý nghĩa cuộc đời được đo bằng chiều sâu của những kết nối con người mà bạn để lại phía sau.",
            "leverage": "Đối xử với những người thân yêu như thể đây là lần cuối cùng bạn được nhìn thấy họ trên cõi đời này.",
            "mantra": "Trăm năm một kiếp phù du — Nghĩa tình sâu đậm thiên thu lưu truyền"
        }
    ],
    "environment": {
        "title": "Thiết lập không gian thanh lọc tinh thần và cai nghiện sự chú ý",
        "items": [
            ("Xóa toàn bộ ứng dụng mạng xã hội trên điện thoại di động", "Chỉ truy cập mạng xã hội qua trình duyệt máy tính vào một khung giờ cố định trong ngày để triệt tiêu phản xạ kiểm tra vô thức."),
            ("Không gian đọc sách giấy tĩnh lặng mỗi tối", "Dành 45 phút trước khi đi ngủ đọc sách triết học cổ điển dưới ánh đèn vàng ấm áp, không có sự hiện diện của màn hình led.")
        ],
        "mantra": "Tắt màn hình sáng phù hoa — Trở về trang sách lòng ta thanh nhàn"
    },
    "emotional": {
        "title": "Duy trì sự độc lập cảm xúc và tự trọng bản thân",
        "items": [
            ("Không bao giờ van xin tình cảm hay sự chú ý", "Nhận thức rõ giá trị của bản thân; nếu đối phương không trân trọng, hãy bình thản thu dọn hành lý và bước đi."),
            ("Thực hành tha thứ cho bản thân về những sai lầm trong quá khứ", "Xem những mối tình tan vỡ cũ là học phí bắt buộc để trưởng thành, không tự dằn vặt hay hối tiếc.")
        ],
        "mantra": "Chẳng cần van vái xin xỏ — Vững chân bước tiếp ngày dài thênh thang"
    }
})

# 12. Dr. Ravinder (FO502)
BATCH_2.append({
    "id": "CdsneNlNpXw",
    "slug": "dr-ravinder-rice-wheat-anemia-nutrition-podcast.html",
    "ep_code": "FO502",
    "cat_badge": "12 / SINH HÓA DINH DƯỠNG & Y HỌC DỰ PHÒNG",
    "speaker": "Dr. Ravinder",
    "speaker_role": "Tiến sĩ Sinh hóa Dinh dưỡng / Chuyên gia Nghiên cứu Vi chất & Chuyển hóa",
    "tagline": "MỐI NGUY TỪ TINH BỘT TINH CHẾ & NGHỊCH LÝ THIẾU MÁU",
    "orig_title": "The Hidden Danger in Rice and Wheat: Focus Issues, Iron Loss & Anemia",
    "youtube_url": "https://www.youtube.com/watch?v=CdsneNlNpXw",
    "duration": "1 giờ 32 phút",
    "read_time": "~8 phút chắt lọc",
    "hero_quote": "Ăn no bụng dạ phập phồng — Hóa ra thiếu máu suy đồi trí khôn",
    "lead_points": [
        "Hàng trăm triệu người châu Á đang bị 'nạn đói tiềm ẩn' (Hidden Hunger): No đủ về mặt calo nhưng cơ thể bị suy kiệt vi chất trầm trọng do chế độ ăn áp đảo bởi gạo trắng và lúa mì tinh chế.",
        "Dr. Ravinder bóc trần cơ chế sinh hóa: Acid Phytic trong ngũ cốc cản trở hấp thu sắt và kẽm, gây ra tình trạng thiếu máu giấu mặt, suy giảm khả năng tập trung của não bộ và sương mù não kinh niên."
    ],
    "hero_summary": {
        "title": "Bản đồ sinh hóa về dinh dưỡng và chuyển hóa năng lượng",
        "items": [
            ("1. Kẻ phá hoại vô hình: Acid Phytic trong ngũ cốc", "Hợp chất kháng dinh dưỡng (Anti-nutrient) liên kết chặt chẽ với khoáng chất Sắt, Kẽm, Canxi khiến cơ thể không thể hấp thu qua thành ruột."),
            ("2. Cơ chế gây 'Sương mù não' (Brain Fog) từ tinh bột chỉ số GI cao", "Gạo trắng và bột mì làm đường huyết tăng vọt rồi tụt dốc thê thảm, khiến tế bào não bị đói năng lượng sau bữa ăn."),
            ("3. Tái cấu trúc đĩa ăn cân bằng sinh học", "Hạ tỷ lệ tinh bột xuống dưới 30%, tăng cường đạm sinh học cao, chất béo tốt và các loại rau xanh giàu vi chất hấp thu.")
        ],
        "mantra": "Hiểu rõ từng hạt gạo tinh — Ăn đúng nuôi dưỡng thân hình thông minh"
    },
    "delusion": {
        "title": "ẢO TƯỞNG CƠM TRẮNG NO BỤNG & SỰ SUY KIỆT VI CHẤT NGẦM",
        "desc": "Thói quen ăn cơm trắng đầy ắp bát từ thời nghèo khó đã trở thành thảm họa sức khỏe trong kỷ nguyên tĩnh tại. Ăn no không đồng nghĩa với đủ chất; đa số người béo phì hiện nay thực chất đang bị suy dinh dưỡng vi chất trầm trọng.",
        "compare_left": {
            "badge": "THÓI QUEN TRUYỀN THỐNG",
            "title": "Ăn 3 bát cơm trắng đầy mỗi bữa để 'chắc dạ'",
            "text": "Đĩa thức ăn gồm 80% tinh bột tinh chế, chỉ có vài cọng rau và vài miếng thịt mỡ, làm đường huyết tăng vọt."
        },
        "compare_right": {
            "badge": "SINH HÓA HIỆN ĐẠI",
            "title": "Ưu tiên vi chất, đạm sạch và chất xơ hòa tan",
            "text": "Ngũ cốc được ngâm ủ nảy mầm để triệt tiêu acid phytic, kết hợp với thực phẩm giàu sắt heme dễ hấp thu."
        },
        "matrix_title": "So sánh giữa Bữa ăn quá tải Carbohydrate và Bữa ăn tối ưu Sinh hóa",
        "matrix_items": [
            ("Bữa ăn quá tải Carbohydrate tinh chế", "• Buồn ngủ rũ rượi sau khi ăn 45 phút, khó tập trung làm việc.<br>• Mỡ nội tạng tích tụ quanh gan, thiếu máu thiếu sắt âm ỉ, rụng tóc mệt mỏi."),
            ("Bữa ăn tối ưu Sinh hóa (Nutrient-Dense)", "• Năng lượng ổn định kéo dài 4-5 tiếng không bị sụt giảm đường huyết.<br>• Tinh thần tỉnh táo, nồng độ hemoglobin và ferritin trong máu đạt chuẩn tối ưu.")
        ],
        "mantra": "No bụng mà ruột đói meo — Đổi thay bữa ăn vượt nghèo bệnh đau"
    },
    "insights": [
        {
            "num": 1,
            "meta": "CHẤT KHÁNG DINH DƯỠNG",
            "title": "Acid Phytic: Chiếc khóa kẹp chặt sắt và kẽm trong ruột",
            "ground_truth": "Lớp cám của lúa mì và ngũ cốc nguyên cám chưa qua chế biến đúng cách chứa lượng acid phytic đủ để khóa 60-80% lượng sắt trong bữa ăn.",
            "surface": "Nghĩ rằng ăn ngũ cốc thô chưa ngâm là hoàn toàn bổ dưỡng và lành mạnh tuyệt đối.",
            "nature": "Thực vật tạo ra acid phytic để bảo vệ hạt giống khỏi bị tiêu hóa sớm trong tự nhiên.",
            "leverage": "Ngâm ngũ cốc và các loại đậu trong nước ấm có pha chút giấm hoặc chanh từ 8-12 tiếng trước khi nấu để kích hoạt men phytase bẻ gãy acid phytic.",
            "mantra": "Ngâm ủ hạt giống qua đêm — Khóa gông phá vỡ dưỡng chất thêm dồi dào"
        },
        {
            "num": 2,
            "meta": "THIẾU MÁU GIẤU MẶT",
            "title": "Chỉ số Ferritin: Thước đo kho dự trữ sắt thực sự của tế bào",
            "ground_truth": "Nhiều người có chỉ số Hemoglobin bình thường nhưng Ferritin (kho dự trữ sắt) đã cạn kiệt, gây ra tình trạng mệt mỏi kinh niên không rõ nguyên nhân.",
            "surface": "Chỉ đi xét nghiệm công thức máu thông thường và chủ quan khi thấy bác sĩ nói 'chưa thiếu máu'.",
            "nature": "Cơ thể sẽ rút cạn kho dự trữ sắt trong tủy xương và gan trước khi chỉ số hemoglobin trên máu ngoại vi giảm xuống.",
            "leverage": "Bắt buộc yêu cầu xét nghiệm Serum Ferritin định kỳ hàng năm; duy trì mức tối ưu từ 50-100 ng/mL.",
            "mantra": "Kho sắt cạn kiệt từ lâu — Xét nghiệm chuyên sâu mới thấu sự tình"
        },
        {
            "num": 3,
            "meta": "SƯƠNG MÙ NÃO BỘ",
            "title": "Tàu lượn đường huyết phá hủy khả năng tập trung sâu",
            "ground_truth": "Một bữa trưa nhiều cơm trắng làm tăng vọt glucose máu, kích hoạt tụy tiết cơn lũ insulin dìm đường huyết xuống đáy sau 90 phút.",
            "surface": "Nghĩ rằng mình bị thiếu ngủ hoặc lười biếng nên cứ 2h chiều là mắt díp lại ngáp liên tục.",
            "nature": "Tế bào não phụ thuộc vào nguồn cung cấp glucose ổn định; đường huyết rơi tự do khiến não bộ kích hoạt chế độ ngủ tiết kiệm năng lượng.",
            "leverage": "Áp dụng thứ tự ăn thông minh: Ăn rau và chất xơ trước &rarr; Ăn đạm và chất béo &rarr; Tinh bột ăn cuối cùng.",
            "mantra": "Rau trước thịt sau cơm cùng — Đường huyết êm ả chẳng lo ngủ gật"
        },
        {
            "num": 4,
            "meta": "SẮT HEME VS NON-HEME",
            "title": "Sự khác biệt sinh khả dụng giữa sắt động vật và thực vật",
            "ground_truth": "Cơ thể chỉ hấp thu 2-5% sắt từ rau bina (Spinach), trong khi hấp thu 20-30% sắt heme từ gan và thịt đỏ.",
            "surface": "Tin vào huyền thoại hoạt hình thủy thủ Popeye rằng chỉ cần ăn rau bina là cơ bắp cuồn cuộn đủ máu.",
            "nature": "Sắt non-heme trong thực vật bị ức chế bởi polyphenol và phytate; sắt heme có kênh vận chuyển riêng biệt qua niêm mạc ruột.",
            "leverage": "Nếu ăn chay, bắt buộc phải uống kèm vitamin C (nước chanh, ớt chuông) trong bữa ăn để tăng hấp thu sắt lên gấp 3 lần.",
            "mantra": "Thực vật sắt khóa khó thông — Kèm vitamin C mở thông dòng vào"
        },
        {
            "num": 5,
            "meta": "TRÀ VÀ CÀ PHÊ",
            "title": "Tannin trong trà bóp chết khả năng hấp thu khoáng chất",
            "ground_truth": "Uống một tách trà đậm đặc ngay sau bữa ăn có thể làm giảm hấp thu sắt lên tới 70% do hợp chất tannin kết tủa với sắt.",
            "surface": "Thói quen uống trà nóng hoặc cà phê ngay sau khi vừa buông đũa ăn cơm.",
            "nature": "Tannin liên kết hóa học bền vững với ion kim loại tạo thành phức hợp không tan mà ruột không thể hấp thu.",
            "leverage": "Cách ly trà và cà phê cách xa bữa ăn chính ít nhất 60-90 phút.",
            "mantra": "Cơm xong chớ vội uống trà — Cách một giờ sau mới là thông minh"
        },
        {
            "num": 6,
            "meta": "SỨC KHỎE ĐƯỜNG RUỘT",
            "title": "Bệnh Celiac và hội chứng ruột rò rỉ do Gluten công nghiệp",
            "ground_truth": "Lúa mì lai tạo hiện đại chứa hàm lượng gluten cực cao làm tăng tính thấm thành ruột (Zonulin), gây viêm mãn tính toàn thân.",
            "surface": "Coi các triệu chứng đầy hơi, khó tiêu sau khi ăn bánh mì chỉ là do 'yếu bụng'.",
            "nature": "Ruột bị viêm mạn tính sẽ làm teo các vi nhung mao (Villi), làm mất hoàn toàn bề mặt hấp thu dưỡng chất của cơ thể.",
            "leverage": "Thử nghiệm cắt bỏ toàn bộ lúa mì và gluten trong 30 ngày để cảm nhận sự thay đổi của hệ tiêu hóa và làn da.",
            "mantra": "Ruột rò viêm nhiễm khắp mình — Bỏ đi bột trắng giữ gìn an khang"
        },
        {
            "num": 7,
            "meta": "KHOÁNG CHẤT KẼM",
            "title": "Kẽm: Vị thần hộ mệnh của hệ miễn dịch và hormone nam giới",
            "ground_truth": "Thiếu kẽm do chế độ ăn nhiều tinh bột làm suy giảm 40% nồng độ testosterone và khiến các vết thương chậm lành gấp đôi.",
            "surface": "Uống thuốc kháng sinh liên tục mỗi khi bị cảm cúm mà không bổ sung kẽm.",
            "nature": "Hơn 300 enzyme trong cơ thể phụ thuộc trực tiếp vào nguyên tử kẽm để hoạt động.",
            "leverage": "Bổ sung thực phẩm giàu kẽm tự nhiên như hạt bí ngô, hàu biển, thịt bò ăn cỏ vào thực đơn hàng tuần.",
            "mantra": "Kẽm quý tựa ngọc trong thân — Đề kháng vững chãi muôn phần uy phong"
        },
        {
            "num": 8,
            "meta": "DINH DƯỠNG CÁ NHÂN",
            "title": "Không có chế độ ăn vạn năng cho tất cả mọi người",
            "ground_truth": "Mỗi cá nhân có một hệ vi sinh vật và bộ gen chuyển hóa khác biệt; người này ăn gạo không sao nhưng người kia ăn vào là tiền tiểu đường.",
            "surface": "Mù quáng chạy theo các chế độ ăn kiêng trào lưu trên mạng xã hội (Keto, Carnivore, Vegan).",
            "nature": "Tính biến thiên sinh học cá thể (Biochemical Individuality) đòi hỏi phải lắng nghe phản ứng thực tế của cơ thể bạn.",
            "leverage": "Sử dụng máy đo đường huyết liên tục (CGM) trong 2 tuần để xác định chính xác thực phẩm nào làm đường huyết của bạn tăng vọt.",
            "mantra": "Cơ thể mình tựa gương soi — Ăn đúng hợp tạng rạng ngời sức xuân"
        }
    ],
    "environment": {
        "title": "Thiết kế gian bếp sinh học bảo tồn tối đa vi chất",
        "items": [
            ("Hũ thủy tinh ngâm ủ ngũ cốc trên kệ bếp", "Chuẩn bị sẵn các loại hạt và đậu ngâm nước ấm qua đêm để sẵn sàng nấu nướng cho ngày hôm sau mà không tốn công."),
            ("Nồi gang truyền thống (Cast Iron) thay thế chảo chống dính", "Nấu ăn bằng nồi chảo gang giúp giải phóng một lượng sắt tự nhiên vào thức ăn, hỗ trợ phòng ngừa thiếu máu an toàn.")
        ],
        "mantra": "Nồi gang ủ hạt tinh tường — Bếp ấm đỏ lửa yêu thương tròn đầy"
    },
    "emotional": {
        "title": "Thay đổi mối quan hệ cảm xúc với đồ ăn tinh bột",
        "items": [
            ("Xóa bỏ thói quen dùng đồ ngọt để giải tỏa căng thẳng (Emotional Eating)", "Khi thấy thèm đường, nhận diện rằng cơ thể đang thiếu dopamine hoặc mệt mỏi, hãy đi bộ 10 phút thay vì mở tủ lạnh."),
            ("Thực hành ăn trong chánh niệm không xem điện thoại", "Nhai kỹ từng miếng ăn tối thiểu 20 lần để enzyme amylase trong nước bọt tiêu hóa tinh bột ngay tại khoang miệng.")
        ],
        "mantra": "Ăn chậm nhai kỹ từng phần — Vị ngọt tự nhiên nuôi dưỡng thân tâm"
    }
})

# 13. Prashant Desai (FO501)
BATCH_2.append({
    "id": "rb9536WrfDA",
    "slug": "prashant-desai-protein-metabolic-health-muscle-podcast.html",
    "ep_code": "FO501",
    "cat_badge": "13 / SỨC KHỎE CHUYỂN HÓA & NGHỆ THUẬT SỐNG THỌ",
    "speaker": "Prashant Desai",
    "speaker_role": "Chuyên gia Sức khỏe Chuyển hóa / Tác giả Sách 'The Biomarker Revolution'",
    "tagline": "NGHỊCH LÝ THIẾU HỤT PROTEIN & TEO CƠ SỚM",
    "orig_title": "Indian Diet Problem: Low Protein, High Calories & Muscle Loss",
    "youtube_url": "https://www.youtube.com/watch?v=rb9536WrfDA",
    "duration": "1 giờ 42 phút",
    "read_time": "~8 phút chắt lọc",
    "hero_quote": "Cơ bắp là chiếc áo giáp vàng — Giữ cho tuổi thọ vững vàng trăm năm",
    "lead_points": [
        "Hơn 80% người trưởng thành châu Á đang bị thiếu hụt protein trầm trọng, dẫn đến tình trạng 'Gầy gò nhưng béo phì nội tạng' (Skinny Fat) và suy giảm cơ bắp sớm (Sarcopenia) ngay từ tuổi 35.",
        "Prashant Desai chia sẻ công thức khoa học để đảo ngược lão hóa: Cơ bắp là cơ quan nội tiết lớn nhất cơ thể; mất cơ bắp đồng nghĩa với việc mở toang cánh cửa đón nhận tiểu đường, loãng xương và mất trí nhớ."
    ],
    "hero_summary": {
        "title": "Bản thiết kế tái tạo khối cơ và chuyển hóa năng lượng",
        "items": [
            ("1. Khủng hoảng suy dinh dưỡng protein", "Một người 60kg chỉ nạp 25-30g protein mỗi ngày, trong khi nhu cầu sinh học tối thiểu để bảo tồn cơ là 1.2 - 1.6g trên mỗi kg trọng lượng."),
            ("2. Cơ bắp là bồn chứa Glucose lớn nhất", "Càng có nhiều khối cơ nạc, cơ thể càng tiêu thụ đường hiệu quả mà không cần tuyến tụy phải gồng mình bơm insulin."),
            ("3. Tập kháng lực (Resistance Training) là liều thuốc cải lão hoàn đồng", "Nâng tạ kích hoạt tín hiệu mTOR tổng hợp protein và tăng cường mật độ khoáng chất của xương khớp.")
        ],
        "mantra": "Xây cơ đắp giáp bền lâu — Tuổi già khỏe mạnh chẳng sầu bệnh đau"
    },
    "delusion": {
        "title": "ẢO TƯỞNG CÂN NẶNG TRÊN BÀN CÂN & CHỈ SỐ MỠ NỘI TẠNG",
        "desc": "Đa số mọi người chỉ chăm chăm nhìn vào số cân nặng và chỉ số BMI. Một người trông gầy gò mặc quần áo size nhỏ vẫn có thể có lượng mỡ nội tạng bao quanh gan và tim cao gấp đôi người tập tạ đô con.",
        "compare_left": {
            "badge": "ẢO TƯỞNG ĐÁM ĐÔNG",
            "title": "Nhịn ăn giảm cân để có số đo nhỏ",
            "text": "Ăn kiêng khắc nghiệt làm mất nước và teo cơ bắp, khiến tỷ lệ trao đổi chất cơ bản (BMR) tụt dốc, sau đó tăng cân trở lại gấp đôi."
        },
        "compare_right": {
            "badge": "KHOA HỌC CHUYỂN HÓA",
            "title": "Ăn đủ protein và tập tạ để tăng cơ giảm mỡ",
            "text": "Không quan tâm số cân nặng tổng; tập trung tăng khối lượng cơ nạc và giảm tỷ lệ mỡ dưới 15% đối với nam, 22% đối với nữ."
        },
        "matrix_title": "So sánh giữa Kiểu hình Skinny Fat và Kiểu hình Cơ nạc khỏe mạnh",
        "matrix_items": [
            ("Kiểu hình Béo gầy (Skinny Fat)", "• Chân tay teo tóp, bụng dưới phình to, da thịt nhão nhẽo.<br>• Kháng insulin nặng nề, dễ gãy xương khi về già và mệt mỏi kinh niên."),
            ("Kiểu hình Cơ nạc săn chắc (Metabolically Fit)", "• Khối cơ bắp phát triển đều, tỷ lệ trao đổi chất cao ăn không sợ béo.<br>• Độ nhạy insulin tối hảo, xương khớp vững chãi bảo vệ cơ thể trước mọi cú ngã.")
        ],
        "mantra": "Chớ nhìn con số bàn cân — Khối cơ săn chắc muôn phần quý hơn"
    },
    "insights": [
        {
            "num": 1,
            "meta": "NGƯỠNG LEUCINE",
            "title": "Cần tối thiểu 2.5 - 3g Leucine để kích hoạt tổng hợp cơ bắp",
            "ground_truth": "Nếu một bữa ăn chứa dưới 20-25g protein tổng hợp, nồng độ acid amin Leucine không đủ để bật công tắc mTOR trong tế bào cơ.",
            "surface": "Ăn rải rác một chút đậu hoặc một quả trứng mỗi bữa rồi nghĩ rằng mình đã nạp đủ protein.",
            "nature": "Tổng hợp protein cơ bắp là cơ chế 'Bật hoặc Tắt' (All-or-None); không đạt ngưỡng kích hoạt thì protein chỉ bị đốt thành calo thông thường.",
            "leverage": "Đảm bảo mỗi bữa ăn chính chứa ít nhất 30-40g protein chất lượng cao để vượt qua ngưỡng Leucine.",
            "mantra": "Đủ ngưỡng công tắc mới bật — Cơ bắp sinh sôi vững chắc từng ngày"
        },
        {
            "num": 2,
            "meta": "BẪY ĂN CHAY THIẾU ĐẠM",
            "title": "Đậu lăng (Dal) không phải là nguồn protein hoàn hảo",
            "ground_truth": "Một bát đậu lăng nấu chín chứa 8g protein nhưng đi kèm với 40g carbohydrate; để nạp đủ 100g protein từ đậu bạn sẽ nạp tới 500g carb.",
            "surface": "Tin rằng người ăn chay chỉ cần ăn nhiều cơm và đậu là đủ lượng đạm cần thiết cho cơ thể.",
            "nature": "Đạm thực vật thường thiếu hụt các acid amin thiết yếu (như Lysine, Methionine) và có tỷ lệ hấp thu sinh học thấp hơn đạm động vật.",
            "leverage": "Nếu ăn chay, bắt buộc phải kết hợp whey protein isolate từ sữa thực vật hoặc bổ sung các dạng acid amin thiết yếu (EAA).",
            "mantra": "Đậu hạt carb nhiều đạm vơi — Kết hợp thông thái mới ngời sức trai"
        },
        {
            "num": 3,
            "meta": "MẤT CƠ DO TUỔI TÁC",
            "title": "Từ sau tuổi 30, bạn mất tự nhiên 3-8% khối cơ mỗi thập kỷ",
            "ground_truth": "Hội chứng teo cơ (Sarcopenia) là nguyên nhân hàng đầu khiến người già mất khả năng tự chủ sinh hoạt và tử vong sau cú ngã đầu tiên.",
            "surface": "Nghĩ rằng tuổi già thì đương nhiên phải yếu đuối, đi lại chậm chạp và run rẩy.",
            "nature": "Mất cơ bắp là một quá trình thoái hóa sinh học có thể phòng ngừa và đảo ngược hoàn toàn bằng rèn luyện kháng lực.",
            "leverage": "Bắt đầu tập tạ ngay hôm nay bất kể bạn đang 20 hay 60 tuổi; không bao giờ là quá muộn để xây dựng cơ bắp.",
            "mantra": "Ba mươi tuổi cơ bắt đầu vơi — Tập tạ kháng lực trọn đời dẻo dai"
        },
        {
            "num": 4,
            "meta": "HIỆU ỨNG NHIỆT CỦA THỨC ĂN",
            "title": "Protein đốt cháy 25-30% calo chỉ để tự tiêu hóa",
            "ground_truth": "Hiệu ứng nhiệt (TEF) của protein cao gấp 4 lần tinh bột và gấp 10 lần chất béo.",
            "surface": "Nghĩ rằng 100 calo từ đường hay 100 calo từ ức gà vào cơ thể cũng đều như nhau.",
            "nature": "Cơ thể phải tiêu tốn một lượng năng lượng khổng lồ để bẻ gãy các liên kết peptide phức tạp của chuỗi acid amin.",
            "leverage": "Tăng tỷ lệ protein trong khẩu phần ăn là cách tự nhiên nhất để tăng tốc độ trao đổi chất mà không cần nhịn đói.",
            "mantra": "Calo đâu phải như nhau — Ăn đạm đốt mỡ trước sau nhẹ mình"
        },
        {
            "num": 5,
            "meta": "SỨC KHỎE XƯƠNG KHỚP",
            "title": "Xương chỉ chắc khỏe khi cơ bắp kéo căng liên tục",
            "ground_truth": "Uống sữa hay viên canxi không làm tăng mật độ xương nếu thiếu áp lực cơ học từ việc nâng tạ nặng.",
            "surface": "Sợ tập tạ sẽ làm đau lưng, hỏng khớp nên chỉ đi bộ nhẹ nhàng dưỡng sinh.",
            "nature": "Định luật Wolff: Xương thích nghi và đặc chắc hơn để phản ứng lại lực căng cơ học tác động lên nó.",
            "leverage": "Thực hiện các bài tập đa khớp (Compound lifts: Squat, Deadlift, Overhead Press) với trọng lượng tạ tăng tiến.",
            "mantra": "Kéo tạ gân cốt dẻo dai — Xương lỳ đặc chắc tương lai vững vàng"
        },
        {
            "num": 6,
            "meta": "GIẢI MÃ CƠN THÈM ĂN",
            "title": "Đòn bẩy Protein: Cơ thể sẽ ăn cho đến khi nạp đủ lượng đạm",
            "ground_truth": "Giả thuyết đòn bẩy protein (Protein Leverage Hypothesis) chứng minh con người sẽ ăn quá mức calo nếu thức ăn nghèo nàn chất đạm.",
            "surface": "Không hiểu vì sao mình luôn cảm thấy thèm ăn vặt liên tục dù vừa ăn xong một đĩa mì lớn.",
            "nature": "Bản năng sinh học thôi thúc bạn tiếp tục tìm kiếm thức ăn chừng nào nhu cầu acid amin thiết yếu chưa được đáp ứng.",
            "leverage": "Luôn ăn phần thức ăn giàu protein đầu tiên trong bữa ăn để tín hiệu no peptide YY được gửi lên não kịp thời.",
            "mantra": "Đủ đạm cơn thèm tắt ngay — Não bộ no thỏa tháng ngày bình yên"
        },
        {
            "num": 7,
            "meta": "CƠ BẮP LÀ KHO DỰ TRỮ SINH TỒN",
            "title": "Khi ốm nặng, cơ thể sẽ phân hủy cơ bắp để nuôi hệ miễn dịch",
            "ground_truth": "Bệnh nhân nằm phòng hồi sức cấp cứu (ICU) có khối lượng cơ cao có tỷ lệ sống sót gấp 3 lần người gầy yếu.",
            "surface": "Coi cơ bắp chỉ để khoe mẽ ngoài bãi biển hoặc chụp ảnh sống ảo.",
            "nature": "Các kháng thể và tế bào miễn dịch được cấu tạo từ acid amin; khi bị nhiễm trùng nặng, cơ thể rút đạm từ cơ bắp để chiến đấu.",
            "leverage": "Xem việc xây dựng cơ bắp như việc gửi tiền vào tài khoản tiết kiệm sinh mạng cho những biến cố sức khỏe bất ngờ.",
            "mantra": "Cơ bắp tài khoản dự phòng — Giúp ta vượt khó qua vòng hiểm nguy"
        },
        {
            "num": 8,
            "meta": "CHỈ SỐ SINH HỌC CẦN THEO DÕI",
            "title": "HbA1c và Tỷ lệ Triglyceride/HDL: Bộ đôi chỉ điểm chuyển hóa",
            "ground_truth": "Tỷ lệ Triglyceride trên HDL vượt quá 2.0 là dấu hiệu cảnh báo sớm bạn đang bị kháng insulin và gan nhiễm mỡ từ nhiều năm trước khi phát bệnh.",
            "surface": "Chỉ nhìn vào chỉ số Cholesterol toàn phần rồi lo lắng uống thuốc hạ mỡ máu bừa bãi.",
            "nature": "Mỡ máu cao do ăn quá nhiều tinh bột chuyển hóa thành triglyceride tại gan chứ không phải do ăn mỡ lành mạnh.",
            "leverage": "Xét nghiệm máu định kỳ theo dõi HbA1c dưới 5.4% và tỷ lệ Triglyceride/HDL dưới 1.5.",
            "mantra": "Chỉ số máu tỏ tường minh — Lối sống chuẩn xác thân hình khang trang"
        }
    ],
    "environment": {
        "title": "Thiết lập môi trường hỗ trợ xây dựng cơ bắp tại gia đình",
        "items": [
            ("Cặp tạ tay có thể điều chỉnh trọng lượng tại góc phòng", "Đặt tạ ở nơi dễ thấy để thực hiện 3 hiệp squat hoặc hít đất ngay trong các giờ giải lao giữa giờ làm việc."),
            ("Bình lắc protein và các nguồn đạm chuẩn bị sẵn trong tủ lạnh", "Luôn luộc sẵn trứng và chuẩn bị ức gà áp chảo để khi đói có thức ăn giàu đạm ngay lập tức, tránh mua đồ ăn nhanh.")
        ],
        "mantra": "Tạ đặt sẵn sàng góc phòng — Đồ ăn chuẩn bị chẳng màng đồ ôi"
    },
    "emotional": {
        "title": "Kiên nhẫn với hành trình tái tạo vóc dáng dài hạn",
        "items": [
            ("Không nản lòng khi cân nặng không thay đổi trong tháng đầu", "Hiểu rằng cơ bắp nặng hơn mỡ; bạn có thể đang giảm 2kg mỡ và tăng 2kg cơ cùng lúc, vóc dáng săn chắc hơn dù cân nặng đứng yên."),
            ("Tôn vinh cảm giác khỏe mạnh tràn đầy sinh lực mỗi sáng thức dậy", "Lấy sự nhẹ nhõm của cơ thể và sự minh mẫn của trí não làm phần thưởng cao quý nhất cho lối sống kỷ luật.")
        ],
        "mantra": "Kiên trì mài giũa tháng ngày — Vóc dáng khỏe khoắn đong đầy niềm vui"
    }
})

print(f"Loaded {len(BATCH_2)} episodes in batch 2.")
