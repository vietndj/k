# -*- coding: utf-8 -*-
import json

with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch4.py', 'r', encoding='utf-8') as f:
    # Read BATCH_4
    code = f.read()

# Load BATCH_4
from episodes_batch4 import BATCH_4

delusions_upgrade = {
    "OE31": {
        "title": "ẢO TƯỞNG THUẬT TOÁN VIRAL & SỰ THẬT VỀ SỰ THỎA MÃN CỦA KHÁN GIẢ",
        "desc": "Người làm nội dung thường đuổi theo các mẹo vặt đánh lừa thuật toán, giật gân câu view nhất thời. Thực tế 2026 chứng minh: Thuật toán phục vụ sự thỏa mãn của người xem; nếu nội dung không giải quyết được vấn đề thực tế, kênh sẽ lụi tàn nhanh chóng.",
        "compare_left": {
            "badge": "LỐI MÒN CLICKBAIT",
            "title": "Tối ưu hóa lượt nhấp chuột bằng giật gân",
            "text": "Làm tiêu đề và ảnh bìa phóng đại quá mức khiến người xem bấm vào rồi thất vọng thoát ra sau vài chục giây."
        },
        "compare_right": {
            "badge": "THỎA MÃN CHIỀU SÂU",
            "title": "Cung cấp giá trị trọn vẹn vượt kỳ vọng",
            "text": "Giải thích bản chất vấn đề sâu sắc, biến mỗi video thành một bài học thực chiến mà người xem muốn lưu lại và chia sẻ."
        },
        "matrix_title": "So sánh Nội dung Câu view và Nội dung Chuyển đổi Khách hàng",
        "matrix_items": [
            [
                "Nội dung Câu view đại trà",
                "• Thu hút lượt xem lớn nhưng không ai nhớ bạn là ai.<br>• Không tạo ra doanh thu từ dịch vụ cao cấp, tỷ lệ huỷ đăng ký cao."
            ],
            [
                "Nội dung Chuyên gia chuyển đổi",
                "• Lượt xem vừa phải nhưng đúng 100% tệp khách hàng mục tiêu.<br>• Rút ngắn chu kỳ bán hàng, khách hàng chủ động tìm đến đặt lịch tư vấn."
            ]
        ],
        "mantra": "Câu view nhất thời tan hoang — Chiều sâu giá trị mở đường hiển vinh"
    },
    "OE32": {
        "title": "ẢO TƯỞNG BẮT CHƯỚC KÊNH LỚN & LỢI THẾ THỰC CHIẾN CỦA KÊNH NHỎ",
        "desc": "Kênh nhỏ dưới 10K sub thường chết yểu vì làm vlog cá nhân hoặc chọn chủ đề quá rộng như các YouTuber triệu sub. Khán giả chưa biết bạn là ai thì họ chỉ bấm vào khi bạn trả lời trúng câu hỏi cấp bách của họ.",
        "compare_left": {
            "badge": "BẮT CHƯỚC MÙ QUÁNG",
            "title": "Làm nội dung phong cách đời sống, tâm sự",
            "text": "Làm video giải trí chung chung, đặt tiêu đề bí ẩn khiến người lạ không có lý do gì để bấm vào xem."
        },
        "compare_right": {
            "badge": "ĐÁNH CHIẾM NGÁCH HẸP",
            "title": "Trả lời câu hỏi tìm kiếm cụ thể và sâu sắc",
            "text": "Tập trung giải quyết nỗi đau cụ thể theo từ khóa tìm kiếm có chủ đích cao, tận dụng sự gần gũi để phản hồi 1-1 với người xem."
        },
        "matrix_title": "So sánh Tiếp cận của Kênh lớn và Kênh nhỏ",
        "matrix_items": [
            [
                "Kênh lớn (> 1.000.000 Sub)",
                "• Dựa vào thương hiệu cá nhân có sẵn để làm nội dung rộng.<br>• Không thể tương tác cá nhân với từng người xem."
            ],
            [
                "Kênh nhỏ (< 10.000 Sub)",
                "• Phải dựa vào nội dung hữu ích theo tìm kiếm để kéo người xem mới.<br>• Tương tác sâu sắc 1-1 biến người xem đầu tiên thành fan cuồng trung thành."
            ]
        ],
        "mantra": "Kênh nhỏ ngách hẹp đi đầu — Chớ theo kênh lớn rước sầu vào thân"
    },
    "OE33": {
        "title": "ẢO TƯỞNG Ý TƯỞNG AI & SỨC HÚT ĐỘC BẢN TỪ TRẢI NGHIỆM ĐỜI THỰC",
        "desc": "Lạm dụng ChatGPT tạo ra hàng triệu bài viết bóng bẩy giống nhau nhưng hoàn toàn vô hồn. Khán giả ngày nay khao khát những góc nhìn gai góc, những vết sẹo thất bại và kinh nghiệm thực chiến từ đời thực.",
        "compare_left": {
            "badge": "LỆ THUỘC CHATGPT",
            "title": "Copy nguyên văn dàn ý tổng hợp từ AI",
            "text": "Bài viết trôi chảy nhưng sáo rỗng, dùng các từ ngữ văn mẫu AI khiến người đọc lướt qua sau 3 giây vì cảm giác giả tạo."
        },
        "compare_right": {
            "badge": "ĐỘC BẢN ĐỜI THỰC",
            "title": "Khai thác câu hỏi khách hàng và bài học cá nhân",
            "text": "Ghi chép lại các tình huống thực tế giải quyết khó khăn cho khách hàng, dám nói lên những sự thật ngượng miệng trong ngành."
        },
        "matrix_title": "So sánh Nội dung AI tổng hợp và Nội dung Thực chiến độc bản",
        "matrix_items": [
            [
                "Nội dung AI tổng hợp",
                "• Thông tin đại trà ai cũng tìm thấy trên Google.<br>• Không tạo được sự kết nối cảm xúc và niềm tin thương hiệu."
            ],
            [
                "Nội dung Thực chiến độc bản",
                "• Mang dấu ấn cá nhân không thể bị sao chép hay thay thế.<br>• Thuyết phục người xem bằng kết quả thực tế và sự đồng cảm chân thành."
            ]
        ],
        "mantra": "AI văn mẫu nhạt nhòa — Lời từ tim óc nở hoa lòng người"
    },
    "OE34": {
        "title": "ẢO TƯỞNG LÀM GIÀU CHỤP GIẬT & NỀN TẢNG THỊNH VƯỢNG ĐỨC TIN",
        "desc": "Đuổi theo tiền bạc bằng mọi giá thường dẫn đến sự sụp đổ đạo đức và kiệt quệ tinh thần. Sự giàu có bền vững đến từ tư duy người quản gia: dùng tài năng và tài chính để phụng sự tha nhân và tạo giá trị cho đời.",
        "compare_left": {
            "badge": "LÒNG THAM BẤT CHẤP",
            "title": "Kiếm tiền nhanh bằng thủ thuật và chiêu trò",
            "text": "Xem khách hàng như con mồi để móc túi, sẵn sàng cắt xén chất lượng và bội tín để tối đa hóa lợi nhuận trước mắt."
        },
        "compare_right": {
            "badge": "PHỤNG SỰ TẬN HIẾN",
            "title": "Tâm thế người quản lý ủy thác tài sản",
            "text": "Kinh doanh chính trực, giữ trọn chữ tín và coi thành công của khách hàng là mục tiêu cao nhất của doanh nghiệp."
        },
        "matrix_title": "So sánh Làm giàu trục lợi và Thịnh vượng đạo đức",
        "matrix_items": [
            [
                "Làm giàu trục lợi",
                "• Tài sản đến nhanh nhưng tiêu tan trong chớp mắt.<br>• Luôn sống trong lo âu, nghi kỵ và mất ngủ mỗi đêm."
            ],
            [
                "Thịnh vượng đạo đức",
                "• Nền móng vững chắc như núi đá, truyền lại cho nhiều thế hệ.<br>• Bình an trong tâm hồn, được cộng đồng kính trọng và yêu mến."
            ]
        ],
        "mantra": "Tâm lành gieo hạt phước an — Tiền tài danh vọng muôn vàn tự nhiên"
    },
    "OE35": {
        "title": "ẢO TƯỞNG SẢN PHẨM MỚI & SỰ THẬT VỀ ĐIỂM NGHẼN DOANH NGHIỆP",
        "desc": "Khi doanh thu chững lại, nhiều người vội vã tung sản phẩm mới hoặc tuyển thêm người. Thực tế, doanh nghiệp sụp đổ vì bỏ mặc điểm nghẽn cốt lõi ở khâu chuyển đổi và giữ chân khách hàng cũ.",
        "compare_left": {
            "badge": "PHÂN TÁN NGUỒN LỰC",
            "title": "Liên tục tung sản phẩm mới khi cái cũ chưa chạy",
            "text": "Tạo ra một danh mục sản phẩm lộn xộn khiến khách hàng hoang mang và đội ngũ kiệt sức vì vận hành quá tải."
        },
        "compare_right": {
            "badge": "GIẢI PHÓNG ĐIỂM NGHẼN",
            "title": "Tập trung sửa đúng mắt xích yếu nhất trong hệ thống",
            "text": "Tối ưu hóa tỷ lệ chốt sale, hoàn thiện quy trình chăm sóc sau bán và xây dựng SOP chuẩn để hệ thống tự vận hành."
        },
        "matrix_title": "So sánh Doanh nghiệp phân tán và Doanh nghiệp tinh gọn tập trung",
        "matrix_items": [
            [
                "Doanh nghiệp phân tán",
                "• Làm nhiều việc nhưng không việc nào đạt đến độ chín muồi.<br>• Chi phí vận hành phình to ăn mòn toàn bộ lợi nhuận."
            ],
            [
                "Doanh nghiệp tinh gọn",
                "• 1 Sản phẩm xuất sắc + 1 Phễu chuyển đổi chuẩn = Triệu đô doanh thu.<br>• Tự động hóa cao, dòng tiền mặt dồi dào và ổn định."
            ]
        ],
        "mantra": "Sửa đúng điểm nghẽn hanh thông — Dòng tiền chảy xiết thỏa lòng ước mong"
    },
    "OE36": {
        "title": "ẢO TƯỞNG BÁN HÀNG ÉP BUỘC & KỸ NĂNG GIẢI QUYẾT BÀI TOÁN LỚN",
        "desc": "Nhiều người nghĩ rằng kỹ năng kiếm tiền quan trọng nhất là chiêu trò chốt sale. Thực tế những người kiếm hàng triệu đô la là những kiến trúc sư có khả năng giải quyết các vấn đề phức tạp nhất của thị trường.",
        "compare_left": {
            "badge": "THỢ BÁN HÀNG RONG",
            "title": "Dùng kỹ thuật thao túng tâm lý để ép chốt đơn",
            "text": "Tập trung vào thủ thuật chốt sale khiến khách hàng đề phòng và hối hận sau khi mua hàng."
        },
        "compare_right": {
            "badge": "KIẾN TRÚC SƯ GIẢI PHÁP",
            "title": "Chẩn đoán chính xác nỗi đau và thiết kế lộ trình giải quyết",
            "text": "Biến vấn đề phức tạp của doanh nghiệp thành giải pháp đơn giản từng bước, khách hàng tự nguyện trả phí cao."
        },
        "matrix_title": "So sánh Bán hàng kỹ xảo và Giải quyết vấn đề chiến lược",
        "matrix_items": [
            [
                "Bán hàng kỹ xảo",
                "• Nhận thù lao nhỏ trên từng giao dịch vất vả.<br>• Dễ bị thay thế bởi các công cụ tự động hóa hoặc AI."
            ],
            [
                "Giải quyết vấn đề chiến lược",
                "• Nhận phần thưởng tỷ lệ thuận với quy mô bài toán hàng triệu đô.<br>• Được thị trường săn đón như tài sản vô giá không thể thay thế."
            ]
        ],
        "mantra": "Không màng kỹ xảo cao siêu — Giải bài toán khó tiền tiêu ngập tràn"
    },
    "OE37": {
        "title": "ẢO TƯỞNG BỎ VIỆC KHỞI NGHIỆP & CHIẾN LƯỢC KINH DOANH BÁN THỜI GIAN",
        "desc": "Hô hào bỏ việc lao vào khởi nghiệp khi chưa có dòng tiền ổn định là một hành động liều lĩnh. Mô hình thông minh là tận dụng sự an toàn từ lương chính để xây dựng doanh nghiệp 1 người High-Ticket bán thời gian.",
        "compare_left": {
            "badge": "LIỀU LĨNH THIẾU TÍNH TOÁN",
            "title": "Nghỉ việc ngay lập tức và bán sản phẩm giá rẻ",
            "text": "Rơi vào khủng hoảng tài chính, chấp nhận nhận khách hàng giá bèo để trả tiền nhà và kiệt quệ tinh thần."
        },
        "compare_right": {
            "badge": "ĐÒN BẨY KHỐI THỜI GIAN",
            "title": "Làm chủ 2 giờ sáng sớm và bán dịch vụ cao cấp",
            "text": "Dùng lương chính làm quỹ đầu tư rủi ro, tập trung phục vụ 2-3 khách hàng High-Ticket mỗi tháng với thu nhập vượt trội."
        },
        "matrix_title": "So sánh Khởi nghiệp mạo hiểm và Xây dựng doanh nghiệp bán thời gian",
        "matrix_items": [
            [
                "Khởi nghiệp mạo hiểm",
                "• 90% thất bại trong năm đầu tiên vì cạn kiệt dòng tiền mặt.<br>• Căng thẳng tâm lý triệt tiêu khả năng sáng tạo chiến lược."
            ],
            [
                "Doanh nghiệp bán thời gian",
                "• Tâm lý ung dung, tự tin từ chối các hợp đồng tồi tệ.<br>• Chỉ chuyển toàn thời gian khi doanh thu phụ gấp đôi lương chính trong 6 tháng."
            ]
        ],
        "mantra": "Thời gian bán phần tinh anh — Doanh thu triệu mức ngọt lành vững êm"
    },
    "OE38": {
        "title": "ẢO TƯỞNG TÍNH PHÍ THEO GIỜ & NGHỆ THUẬT ĐỊNH GIÁ THEO GIÁ TRỊ",
        "desc": "Tính phí theo giờ là cái bẫy nô lệ thời đại số: Bạn càng giỏi và làm nhanh, bạn càng bị trả ít tiền hơn. Định giá dựa trên giá trị giải phóng chuyên gia và đem lại thù lao xứng đáng cho 20 năm kinh nghiệm đúc kết.",
        "compare_left": {
            "badge": "NÔ LỆ TÍNH GIỜ",
            "title": "Bán thời gian và công sức trực tiếp",
            "text": "Khách hàng luôn săm soi từng phút làm việc và tìm cách cắt giảm số giờ để trả ít tiền nhất có thể."
        },
        "compare_right": {
            "badge": "ĐỊNH GIÁ GIÁ TRỊ",
            "title": "Bán kết quả tài chính và sự biến đổi toàn diện",
            "text": "Thu phí dựa trên mức độ thiệt hại bạn ngăn chặn được hoặc khoản lợi nhuận khổng lồ bạn mang lại cho đối tác."
        },
        "matrix_title": "So sánh Định giá theo giờ và Định giá theo kết quả",
        "matrix_items": [
            [
                "Định giá theo giờ ($50/h)",
                "• Thu nhập bị chặn trần bởi 24 giờ mỗi ngày.<br>• Càng làm nhanh càng thiệt hại tài chính."
            ],
            [
                "Định giá theo kết quả ($5.000 - $50.000/deal)",
                "• Không giới hạn trần thu nhập; giải quyết vấn đề trong 10 phút vẫn nhận trọn vẹn số tiền.<br>• Khách hàng vui vẻ chi trả vì ROI đạt gấp 10 lần."
            ]
        ],
        "mantra": "Định giá theo giờ khổ sai — Định giá kết quả rạng mai cơ đồ"
    },
    "OE39": {
        "title": "ẢO TƯỞNG QUẢNG CÁO CHÈO KÉO & SỰ THỐNG TRỊ CỦA QUẢNG CÁO GIÁO DỤC",
        "desc": "Thời đại người dùng dị ứng với quảng cáo 'Mua ngay kẻo lỡ'. Cách tiếp cận hiện đại chuyển đổi cao nhất là mang nội dung giáo dục giá trị cao phục vụ khách hàng trước khi yêu cầu họ trả tiền.",
        "compare_left": {
            "badge": "CHÈO KÉO TRUYỀN THỐNG",
            "title": "Hối thúc mua hàng bằng giảm giá và cam kết ảo",
            "text": "Đốt tiền quảng cáo vào các tệp khách hàng lạnh với thông điệp bán hàng lộ liễu khiến chi phí CPM tăng vọt."
        },
        "compare_right": {
            "badge": "QUẢNG CÁO GIÁO DỤC",
            "title": "Giúp khách hàng giải quyết 1 vấn đề nhỏ miễn phí",
            "text": "Video ngắn 2-3 phút chia sẻ giải pháp thực chiến, AI tự động nhận diện đối tượng quan tâm và đưa vào phễu đặt lịch."
        },
        "matrix_title": "So sánh Quảng cáo Chèo kéo và Quảng cáo Giáo dục High-Ticket",
        "matrix_items": [
            [
                "Quảng cáo Chèo kéo",
                "• Tỷ lệ bỏ qua (Skip rate) cao, khách hàng bức xúc báo cáo vi phạm.<br>• Chi phí chuyển đổi đắt đỏ, không bền vững."
            ],
            [
                "Quảng cáo Giáo dục",
                "• Người xem cảm thấy được học bài học bổ ích, tự nguyện bấm vào link.<br>• Xây dựng vị thế chuyên gia ngay từ lần chạm đầu tiên."
            ]
        ],
        "mantra": "Quảng cáo giáo dục mở đường — Thu hút khách quý muôn phương tự tìm"
    },
    "OE40": {
        "title": "ẢO TƯỞNG YOUTUBE ĐẠI TRÀ & BẢN CHẤT LÀM KÊNH CỦA DOANH NHÂN",
        "desc": "Doanh nhân làm YouTube không cần triệu subscriber giải trí; bạn chỉ cần 1.000 người mua hàng trung thành. Chỉ cần trả lời thẳng vào 50 câu hỏi khó nhất của khách hàng là đủ tạo nên phễu chuyển đổi triệu đô.",
        "compare_left": {
            "badge": "ĐU THEO XU HƯỚNG",
            "title": "Làm video hài hước bắt trend để kiếm nhiều view",
            "text": "Video triệu view nhưng toàn khán giả không có nhu cầu hoặc khả năng chi trả cho sản phẩm doanh nghiệp."
        },
        "compare_right": {
            "badge": "TRẢ LỜI CÂU HỎI",
            "title": "Chuyên sâu vào các vấn đề kỹ thuật và chi phí thực tế",
            "text": "Rút ngắn chu kỳ bán hàng từ vài tháng xuống còn một buổi xem video; khách hàng tự động chốt sale trước khi gọi điện."
        },
        "matrix_title": "So sánh Kênh YouTube Giải trí và Kênh YouTube Doanh nhân",
        "matrix_items": [
            [
                "Kênh YouTube Giải trí",
                "• Phụ thuộc vào tiền quảng cáo AdSense bèo bọt.<br>• Luôn chịu áp lực làm nội dung giật gân để giữ view."
            ],
            [
                "Kênh YouTube Doanh nhân",
                "• Mỗi lượt xem là một khách hàng tiềm năng trị giá hàng nghìn đô la.<br>• Trở thành thư viện tài sản số làm việc 24/7 cho công ty suốt 10 năm."
            ]
        ],
        "mantra": "Doanh nhân làm kênh đàng hoàng — Trả lời trúng đích muôn vàn niềm tin"
    }
}

for ep in BATCH_4:
    code = ep['ep_code']
    if code in delusions_upgrade:
        ep['delusion'] = delusions_upgrade[code]

with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch4.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
"""
episodes_batch4.py
Batch 4: 10 Episodes (OE31 - OE40)
"""

BATCH_4 = ''' + json.dumps(BATCH_4, ensure_ascii=False, indent=4) + '\n')

print("Đã nâng cấp xong delusion cho BATCH_4!")
