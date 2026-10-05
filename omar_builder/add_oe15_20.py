# -*- coding: utf-8 -*-
"""
add_oe15_20.py: Hoàn thành OE15 - OE20 cho episodes_batch2.py
"""
import json
import sys
sys.path.append('/Users/vietmac/Documents/CODE/k/omar_builder')
from episodes_batch2 import BATCH_2

with open('/Users/vietmac/.gemini/antigravity/brain/24deb8b1-3156-43d0-91a1-3246f0cc4078/scratch/omar_40_videos.json') as f:
    raw_vids = {v['idx']: v for v in json.load(f)}

eps = [
    # 15. Sell Knowledge (CxTn4fAjP8w)
    {
        "id": raw_vids[15]['id'],
        "slug": "sell-your-knowledge-make-money-online-podcast.html",
        "ep_code": "OE15",
        "cat_badge": "01 / ĐÓNG GÓI TRI THỨC & ĐỊNH GIÁ CAO CẤP",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "ĐÓNG GÓI KỸ NĂNG CHUYÊN SÂU: BÁN KHÓA HỌC & DỊCH VỤ TƯ VẤN CAO CẤP",
        "orig_title": raw_vids[15]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[15]['id']}",
        "publish_date": raw_vids[15]['date'],
        "raw_date": f"{raw_vids[15]['raw_date'][:4]}-{raw_vids[15]['raw_date'][4:6]}-{raw_vids[15]['raw_date'][6:]}",
        "duration": "1 giờ 39 phút",
        "read_time": "~9 phút chắt lọc",
        "hero_quote": "Đóng gói kỹ năng thành tài sản — Bán đường đi lối rạng tương lai",
        "lead_points": [
            "Biến những kinh nghiệm làm nghề tích lũy hàng chục năm thành một sản phẩm số có cấu trúc chuyển giao rõ ràng, giúp khách hàng đạt kết quả nhanh gấp 5 lần so với tự mày mò.",
            "Phân tích cách xây dựng chương trình Coaching cao cấp: Xác định điểm A (Nỗi đau hiện tại) và điểm B (Mục tiêu khao khát), thiết kế lộ trình 6 cột mốc và định giá dựa trên giá trị chuyển hóa."
        ],
        "hero_summary": {
            "title": "Bản đồ đóng gói sản phẩm tri thức từ số 0",
            "items": [
                ("1. Xác định năng lực lõi độc bản", "Tìm ra điểm mạnh nhất mà người khác thường xuyên tìm đến bạn để xin lời khuyên miễn phí."),
                ("2. Quy trình hóa lộ trình chuyển hóa", "Chia nhỏ hành trình thành 6 giai đoạn logic với các biểu mẫu hành động cụ thể."),
                ("3. Định vị dịch vụ cao cấp", "Tập trung phục vụ nhóm đối tượng có cam kết hành động cao và sẵn sàng đầu tư xứng đáng.")
            ],
            "mantra": "Kinh nghiệm đóng gói tinh tường — Thành tài sản quý muôn đường nở hoa"
        },
        "delusion": {
            "title": "ẢO TƯỞNG AI CŨNG BIẾT RỒI & SỰ THẬT VỀ ĐỘ LỆCH THÔNG TIN",
            "desc": "Nhiều chuyên gia giỏi mắc phải 'Lời nguyền của sự hiểu biết' (Curse of Knowledge): Họ nghĩ những gì họ biết là bình thường nên không ai trả tiền. Thực tế, những điều cơ bản với bạn lại là điều kỳ diệu đối với người mới bắt đầu.",
            "compare_left": {
                "badge": "TỰ TI NỘI TÂM",
                "title": "Nghĩ rằng kiến thức của mình quá tầm thường",
                "text": "Ngại chia sẻ vì sợ các chuyên gia đầu ngành chê cười, bỏ lỡ cơ hội giúp đỡ hàng ngàn người đi sau."
            },
            "compare_right": {
                "badge": "SỰ THẬT THỊ TRƯỜNG",
                "title": "Người mới chỉ cần người đi trước 2 bước",
                "text": "Khách hàng thường thích học từ người vừa vượt qua thử thách gần đây hơn là các giáo sư hàn lâm xa vời."
            },
            "matrix_title": "So sánh Hội chứng kẻ giả mạo và Tinh thần phụng sự",
            "matrix_items": [
                ("Mắc kẹt trong hội chứng kẻ giả mạo", "• Luôn trì hoãn, không dám ra mắt sản phẩm, thu nhập dậm chân tại chỗ.<br>• Để mặc những kẻ kém cỏi hơn nhưng dám nói to chiếm lĩnh thị trường."),
                ("Tự tin đóng gói tri thức thực chiến", "• Giúp đỡ được hàng trăm học viên có công ăn việc làm và tăng thu nhập.<br>• Khẳng định vị thế chuyên gia đầu ngành được kính trọng.")
            ],
            "mantra": "Ngại ngùng giấu kín tài năng — Để phường dối trá lộng hành bon chen"
        },
        "insights": [
            {"num": 1, "meta": "LỜI NGUYỀN HIỂU BIẾT", "title": "Giải thoát khỏi lời nguyền của sự hiểu biết", "ground_truth": "Những gì là bản năng tự nhiên của bạn chính là bài học vô giá đối với người khác.", "surface": "Nghĩ rằng kiến thức làm video hay bán hàng của mình ai cũng biết rồi.", "nature": "Sự lệch pha thông tin giữa chuyên gia và người mới là cơ hội kinh doanh bền vững nhất.", "leverage": "Liệt kê 10 kỹ năng bạn làm dễ dàng nhất và đóng gói thành cẩm nang cho người mới.", "mantra": "Chuyện thường với bản thân ta — Lại là bí kíp người xa tìm tìm"},
            {"num": 2, "meta": "LỘ TRÌNH ĐIỂM B", "title": "Bán chiếc cầu nối từ Điểm A sang Điểm B", "ground_truth": "Khách hàng chỉ mua sự dịch chuyển cuộc đời, họ không mua bài giảng.", "surface": "Liệt kê danh sách 50 video trong khóa học như một bản mục lục sách.", "nature": "Mục lục càng dài càng gây cảm giác mệt mỏi và sợ hãi cho người học.", "leverage": "Vẽ lộ trình 6 bước đưa khách hàng từ 'Chưa có kênh' đến 'Kênh sinh lời 100 triệu/tháng'.", "mantra": "Cầu nối bắc nhịp êm đềm — Đưa người qua bến ấm êm nụ cười"},
            {"num": 3, "meta": "ĐỊNH GIÁ DỰA TRÊN KẾT QUẢ", "title": "Định giá bằng 10% giá trị kết quả mang lại", "ground_truth": "Nếu giải pháp của bạn giúp khách hàng kiếm được $50.000, mức giá $5.000 là một món hời lớn.", "surface": "Tính giá dựa trên số giờ bạn ngồi tư vấn cho khách.", "nature": "Thời gian là chi phí của khách; kết quả mới là tài sản họ nhận được.", "leverage": "Chứng minh bài toán kinh tế: 'Khoản đầu tư này sẽ hoàn vốn ngay sau 2 khách hàng đầu tiên của anh'.", "mantra": "Giá trao một phần mười lời — Khách mua hớn hở trọn đời biết ơn"},
            {"num": 4, "meta": "CÔNG CỤ THAY VÌ LÝ THUYẾT", "title": "Tặng kèm các công cụ phần mềm và mẫu có sẵn", "ground_truth": "Khách hàng lười biếng muốn được làm hộ 80% phần việc ban đầu.", "surface": "Chỉ nói về tư duy chiến lược trừu tượng mà không có công cụ thực thi.", "nature": "Công cụ sẵn dùng giúp học viên vượt qua sự ngần ngại ban đầu và hành động ngay.", "leverage": "Tặng kèm bộ bảng tính tính toán chi phí, kho prompt AI và bộ slide thuyết trình mẫu.", "mantra": "Công cụ trao tận bàn tay — Học viên áp dụng tháng ngày hanh thông"},
            {"num": 5, "meta": "GIỮ CHÂN HỌC VIÊN", "title": "Tổ chức các buổi tổng kết vinh danh định kỳ", "ground_truth": "Nhu cầu được công nhận và khen ngợi mạnh mẽ hơn cả tiền bạc.", "surface": "Không quan tâm đến học viên sau khi họ nộp bài tập.", "nature": "Sự công nhận công khai kích hoạt dopamine và củng cố lòng trung thành tuyệt đối với người thầy.", "leverage": "Trao chứng nhận danh dự và phần thưởng cho những học viên có bước tiến xuất sắc nhất tháng.", "mantra": "Khen ngợi nỗ lực từng ngày — Học viên gắn kết dựng xây phong trào"},
            {"num": 6, "meta": "CHUYỂN GIAO QUYỀN LỰC", "title": "Dạy cho học viên cách tự câu cá thay vì cho cá", "ground_truth": "Học viên chỉ thực sự tôn trọng bạn khi họ tự tay làm ra kết quả độc lập.", "surface": "Làm hộ toàn bộ bài tập cho học viên để lấy lòng họ.", "nature": "Làm hộ tạo ra sự phụ thuộc yếu đuối và biến bạn thành người làm thuê cho họ.", "leverage": "Chỉ dẫn nguyên lý, giám sát học viên tự tay bấm nút và sửa lỗi tư duy cho họ.", "mantra": "Trao cần dạy cách buông câu — Tự thân lập nghiệp dài lâu vững bền"},
            {"num": 7, "meta": "TỰ DO ĐỊA ĐIỂM", "title": "Kinh doanh tri thức mang lại sự tự do địa lý tuyệt đối", "ground_truth": "Bạn có thể điều hành doanh nghiệp giáo dục triệu đô chỉ với chiếc laptop tại bất kỳ bãi biển nào.", "surface": "Mở văn phòng trung tâm đắt đỏ để chứng tỏ đẳng cấp.", "nature": "Văn phòng vật lý là gánh nặng tài chính không cần thiết trong kỷ nguyên số hóa đám mây.", "leverage": "Vận hành toàn bộ hệ thống qua Skool, Zoom, Stripe và Google Drive.", "mantra": "Laptop mở bãi biển xanh — Vận hành doanh nghiệp rạng danh cơ đồ"},
            {"num": 8, "meta": "TIẾP NỐI THẾ HỆ", "title": "Đào tạo thế hệ kế thừa tiếp tục sứ mệnh", "ground_truth": "Sự nghiệp giáo dục vĩ đại nhất là tạo ra những người thầy tiếp tục đi gieo hạt giá trị.", "surface": "Muốn giữ độc quyền ngai vàng chuyên gia suốt đời.", "nature": "Khi học trò của bạn trở thành những chuyên gia lớn, tầm ảnh hưởng của bạn được nhân lên gấp bội.", "leverage": "Xây dựng chương trình đào tạo nhà huấn luyện (Train the Trainer) cho những học viên giỏi nhất.", "mantra": "Tre già măng mọc vươn cao — Rừng cây tri thức dạt dào sắc hương"}
        ],
        "environment": {
            "title": "Bố trí không gian tư vấn trực tuyến đỉnh cao",
            "items": [
                ("1. Tai nghe In-Ear Monitor kín đáo", "Giúp nghe rõ từng ngữ điệu của học viên mà không để lộ tai nghe chụp đầu cồng kềnh trên khung hình."),
                ("2. Đèn hắt trần tạo ánh sáng gián tiếp", "Không gian sáng tự nhiên êm dịu, tạo cảm giác thư giãn và cởi mở cho các cuộc đàm thoại sâu sắc."),
                ("3. Kính lọc gió cho micro thu âm", "Loại bỏ tiếng phù của hơi thở khi phát âm các phụ âm mạnh, giữ âm thanh luôn trong trẻo.")
            ],
            "mantra": "Ánh sáng dịu mát chan hòa — Âm thanh trong trẻo lời ca gửi trao"
        },
        "emotional": {
            "title": "Giữ tâm thế của người dẫn dắt bao dung",
            "items": [
                ("1. Luôn nhìn vào tiềm năng tương lai của học viên", "Không đánh giá họ qua những vụng về hiện tại; nhìn thấy phiên bản rực rỡ của họ sau 1 năm nữa."),
                ("2. Bình thản trước những lời phàn nàn vô lý", "Lắng nghe với sự thấu cảm, tìm hiểu nguyên nhân sâu xa và giải quyết bằng tình thương yêu."),
                ("3. Tự chăm sóc sức khỏe tinh thần của bản thân", "Không nhận quá nhiều học viên cùng lúc; giữ cho tâm trí luôn thanh tịnh để cống hiến trọn vẹn.")
            ],
            "mantra": "Bao dung nâng đỡ con người — Tâm trong trí sáng nụ cười an vui"
        }
    },

    # 16. Unstuck Personal Brand (UZ6pzwqvkH8)
    {
        "id": raw_vids[16]['id'],
        "slug": "how-to-get-your-personal-brand-unstuck-podcast.html",
        "ep_code": "OE16",
        "cat_badge": "02 / THƯƠNG HIỆU CÁ NHÂN & VỊ THẾ DẪN ĐẦU",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "PHÁ VỠ NÚT THẮT ĐÌNH TRỆ: CÁCH HỒI SINH THƯƠNG HIỆU CÁ NHÂN MẤT TƯƠNG TÁC",
        "orig_title": raw_vids[16]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[16]['id']}",
        "publish_date": raw_vids[16]['date'],
        "raw_date": f"{raw_vids[16]['raw_date'][:4]}-{raw_vids[16]['raw_date'][4:6]}-{raw_vids[16]['raw_date'][6:]}",
        "duration": "1 giờ 23 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Thương hiệu đình trệ bế tắc — Thay đổi góc nhìn khởi sắc hồi sinh",
        "lead_points": [
            "Mọi nhà sáng tạo đều sẽ trải qua giai đoạn 'bức tường đình trệ' (The Plateau): Lượt xem giảm sút, tương tác đóng băng và cảm giác cạn kiệt ý tưởng sau vài năm làm nội dung.",
            "Omar chia sẻ chiến lược 'Tái định vị bản sắc' (Identity Reinvention): Cách thừa nhận sự thay đổi của bản thân, dũng cảm từ bỏ tệp khán giả cũ không còn phù hợp để đón nhận làn sóng tăng trưởng mới."
        ],
        "hero_summary": {
            "title": "Bản đồ hồi sinh thương hiệu cá nhân rơi vào bế tắc",
            "items": [
                ("1. Chấp nhận sự tiến hóa của bản thân", "Bạn của ngày hôm nay không còn là con người của 3 năm trước; đừng cố gượng ép bản thân đóng lại vai diễn cũ."),
                ("2. Dọn sạch rác nội dung", "Dũng cảm xóa bỏ hoặc ẩn đi những video cũ lỗi thời không còn phản ánh đúng đẳng cấp hiện tại."),
                ("3. Tái xuất hiện với câu chuyện lột xác", "Làm video chân thành chia sẻ về những khủng hoảng và bài học thức tỉnh vừa trải qua để tái kết nối sâu sắc.")
            ],
            "mantra": "Dũng cảm lột xác sang trang — Rũ bùn đứng dậy hiên ngang sáng ngời"
        },
        "delusion": {
            "title": "ẢO TƯỞNG THUẬT TOÁN ĐÌ KÊNH & SỰ THẬT VỀ SỰ NHÀM CHÁN CỦA KHÁN GIẢ",
            "desc": "Khi lượt xem giảm, người làm nội dung thường đổ lỗi cho thuật toán YouTube hay TikTok bóp tương tác. Thực tế, lý do chính là chính bạn đã cảm thấy chán nản với chủ đề cũ và khán giả ngửi thấy mùi thiếu nhiệt huyết đó.",
            "compare_left": {
                "badge": "TÂM LÝ ĐỔ LỖI",
                "title": "Đổ lỗi cho thuật toán và nền tảng",
                "text": "Nghĩ rằng nền tảng đang chơi xấu mình, liên tục than vãn trên mạng xã hội và mất hết tinh thần sáng tạo."
            },
            "compare_right": {
                "badge": "TỰ CHỊU TRÁCH NHIỆM",
                "title": "Nhìn thẳng vào sự suy giảm chất lượng nội dung",
                "text": "Nhận diện sự lặp lại nhàm chán, chủ động nâng cấp thiết bị, góc nhìn và phong cách dẫn dắt mới mẻ."
            },
            "matrix_title": "So sánh Kênh mắc kẹt trong lối cũ và Kênh tái sinh thành công",
            "matrix_items": [
                ("Mắc kẹt trong vùng an toàn cũ", "• Tiếp tục làm đi làm lại một công thức cũ đã hết thời.<br>• Tương tác ngày càng giảm dần cho đến khi kênh chết hẳn."),
                ("Dũng cảm tái định vị thương hiệu", "• Đưa ra góc nhìn mới sắc bén hơn, nâng tầm chất lượng điện ảnh.<br>• Thu hút tệp khán giả trưởng thành và sẵn sàng chi trả cao hơn.")
            ],
            "mantra": "Đổ lỗi cho máy sao đành — Xem lại chính mình sửa nhanh từng phần"
        },
        "insights": [
            {"num": 1, "meta": "CHU KỲ TIẾN HÓA", "title": "Thương hiệu cá nhân là một thực thể sống liên tục tiến hóa", "ground_truth": "Nếu sau 3 năm mà nội dung của bạn vẫn y hệt ngày đầu, bạn đang thụt lùi so với thời đại.", "surface": "Cố gắng giữ nguyên hình ảnh 'anh chàng vui vẻ' ban đầu dù nội tâm đã trầm tĩnh hơn.", "nature": "Sự giả tạo trong việc cố gượng ép bản thân sẽ phát ra tần số giả tạo khiến khán giả rời xa.", "leverage": "Công khai chia sẻ sự dịch chuyển trong tư duy và các mối quan tâm mới của bạn.", "mantra": "Nước chảy đá mòn theo năm — Người khôn tiến hóa tháng năm rạng ngời"},
            {"num": 2, "meta": "DŨNG CẢM MẤT VIEW", "title": "Sẵn sàng mất đi tệp khán giả cũ để đón tệp khán giả mới", "ground_truth": "Để bước lên nấc thang mới, bạn phải chấp nhận buông tay khỏi nấc thang cũ.", "surface": "Sợ mất lượt xem nên không dám thay đổi chủ đề sang hướng cao cấp hơn.", "nature": "Những người theo dõi bạn vì nội dung rẻ tiền trước đây sẽ không bao giờ ủng hộ bạn khi bạn nâng giá.", "leverage": "Thanh lọc tệp khán giả: Tập trung làm nội dung phục vụ tệp khách hàng lý tưởng mới.", "mantra": "Buông bỏ cái cũ qua đi — Đón chào cái mới ngại chi đổi dời"},
            {"num": 3, "meta": "NÂNG CẤP THỊ GIÁC", "title": "Thay đổi diện mạo hình ảnh để báo hiệu sự lột xác", "ground_truth": "Con người phản ứng tức thì với các tín hiệu thay đổi thị giác (Visual Rebranding).", "surface": "Tiếp tục dùng ảnh đại diện, banner và phong cách thumbnail từ 5 năm trước.", "nature": "Một bộ nhận diện mới mẻ, đẳng cấp sẽ báo cho khán giả biết bạn đã bước sang một chương mới.", "leverage": "Chụp lại bộ ảnh chân dung mới với trang phục chỉn chu, thiết kế lại toàn bộ cover kênh.", "mantra": "Áo mới diện mạo khang trang — Báo hiệu bước ngoặt vẻ vang bắt đầu"},
            {"num": 4, "meta": "QUAY VỀ GỐC RỄ", "title": "Tìm lại ngọn lửa đam mê nguyên bản ban đầu", "ground_truth": "Bạn bắt đầu làm video vì tình yêu nghề hay chỉ vì muốn kiếm tiền?", "surface": "Mỗi ngày làm video như một nghĩa vụ trả bài mệt mỏi.", "nature": "Khi mất đi niềm vui thuần khiết, năng lượng sáng tạo sẽ bị bóp nghẹt.", "leverage": "Dành 1 tuần không làm video kiếm tiền; quay 1 video chỉ nói về điều bạn thực sự say mê nhất.", "mantra": "Tìm về ngọn lửa ban sơ — Đam mê sống lại ước mơ rạng ngời"},
            {"num": 5, "meta": "PHỎNG VẤN NGƯỜI GIỎI HƠN", "title": "Mời các chuyên gia tầm cao hơn lên kênh của bạn", "ground_truth": "Cách nhanh nhất để nâng tầm vị thế thương hiệu là xuất hiện bên cạnh những người khổng lồ.", "surface": "Chỉ ngồi một mình nói chuyện trước ống kính máy quay.", "nature": "Hiệu ứng hào quang (Halo Effect): Uy tín của khách mời sẽ tự động lan tỏa sang người phỏng vấn.", "leverage": "Mời các CEO, tác giả best-seller hoặc chuyên gia đầu ngành tham gia podcast đối thoại.", "mantra": "Đứng cạnh bậc thầy anh hào — Uy danh tự khắc vút cao muôn phần"},
            {"num": 6, "meta": "ĐỘT PHÁ NỘI DUNG", "title": "Tạo ra một dự án thử thách điên rồ (Crazy Challenge)", "ground_truth": "Khán giả yêu thích những câu chuyện mạo hiểm với kết quả chưa biết trước.", "surface": "Chỉ ngồi phòng máy lạnh giảng giải lý thuyết suông.", "nature": "Một thử thách thực tế có rủi ro thất bại sẽ tạo ra kịch tính và thu hút sự chú ý tột độ.", "leverage": "Làm chuỗi video: 'Thử thách xây kênh mới từ con số 0 trong 30 ngày kiếm $10.000'.", "mantra": "Thử thách kịch tính dấn thân — Người xem hồi hộp muôn phần ngóng trông"},
            {"num": 7, "meta": "NGẮT KẾT NỐI ĐỂ TÁI TẠO", "title": "Dũng cảm nghỉ ngơi 2 tuần để thanh lọc tâm trí", "ground_truth": "Một tâm trí kiệt sức không thể sinh ra bất kỳ ý tưởng đột phá nào.", "surface": "Cố gắng gồng mình quay video trong trạng thái cạn kiệt năng lượng.", "nature": "Bộ não cần thời gian ủ ý tưởng (Incubation Period) trong trạng thái thư giãn tuyệt đối.", "leverage": "Thông báo tạm dừng 2 tuần, đi du lịch hòa mình vào thiên nhiên và tắt hết thông báo mạng xã hội.", "mantra": "Nghỉ ngơi lấy lại tinh anh — Trở về mạnh mẽ tung hoành bốn phương"},
            {"num": 8, "meta": "TỰ TIN NỘI TẠI", "title": "Bạn là tác giả duy nhất của cuốn sách cuộc đời mình", "ground_truth": "Thất bại tạm thời chỉ là một chương nhỏ trong cuốn tiểu thuyết thành công vĩ đại.", "surface": "Đánh giá sự nghiệp cả đời chỉ qua vài tuần view thấp.", "nature": "Những huyền thoại vĩ đại nhất đều từng trải qua những năm tháng tăm tối trước khi tỏa sáng rực rỡ.", "leverage": "Nhắc nhở bản thân: Đây chỉ là đoạn lùi lại để lấy đà nhảy xa hơn trong chương tiếp theo.", "mantra": "Lùi một bước để nhảy xa — Cơ đồ rực rỡ bài ca khải hoàn"}
        ],
        "environment": {
            "title": "Thiết kế không gian tái sinh năng lượng sáng tạo",
            "items": [
                ("1. Thay đổi cách bài trí phòng làm việc", "Kê lại bàn ghế, sơn lại màu tường hoặc thay đổi vị trí góc quay để tạo cảm giác tươi mới."),
                ("2. Loại bỏ toàn bộ đồ đạc bừa bộn", "Dọn dẹp sạch sẽ mặt bàn, chỉ để lại những vật dụng tối cần thiết để giải phóng không gian tâm trí."),
                ("3. Bổ sung âm nhạc không lời truyền cảm hứng", "Mở nhạc Lo-fi hoặc nhạc giao hưởng Baroque khi lên ý tưởng kịch bản mới.")
            ],
            "mantra": "Góc phòng đổi mới phong quang — Tâm hồn khoáng đạt nhẹ nhàng bay cao"
        },
        "emotional": {
            "title": "Bảo toàn tâm thế trước những giai đoạn khủng hoảng",
            "items": [
                ("1. Ôm lấy nỗi sợ hãi và bất an", "Thừa nhận mình đang cảm thấy bế tắc mà không cần phải gồng mình che giấu."),
                ("2. Tin tưởng vào quy luật chu kỳ tự nhiên", "Mùa đông có lạnh giá đến đâu thì mùa xuân ấm áp cũng chắc chắn sẽ quay trở lại."),
                ("3. Yêu thương bản thân vô điều kiện", "Tự khen ngợi mình vì đã không bỏ cuộc và vẫn kiên cường đứng vững đến ngày hôm nay.")
            ],
            "mantra": "Mùa đông buốt giá qua đi — Mùa xuân ấm áp thầm thì hoa khai"
        }
    },

    # 17. Family Wake-Up Call (u2PFE36SJ1w)
    {
        "id": raw_vids[17]['id'],
        "slug": "family-time-entrepreneur-wake-up-call-podcast.html",
        "ep_code": "OE17",
        "cat_badge": "05 / TÂM LÝ BÁN HÀNG & GIAO TIẾP",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "BÀI HỌC TỈNH THỨC VỀ GIA ĐÌNH, THỜI GIAN VÀ SỰ ĐÁNH ĐỔI CỦA NGƯỜI KHỞI NGHIỆP",
        "orig_title": raw_vids[17]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[17]['id']}",
        "publish_date": raw_vids[17]['date'],
        "raw_date": f"{raw_vids[17]['raw_date'][:4]}-{raw_vids[17]['raw_date'][4:6]}-{raw_vids[17]['raw_date'][6:]}",
        "duration": "1 giờ 11 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Mải mê đuổi bóng phù hoa — Mẹ cha tóc bạc xót xa ngậm ngùi",
        "lead_points": [
            "Lời cảnh tỉnh sâu sắc cho những người khởi nghiệp đang hy sinh thời gian bên cha mẹ già và gia đình nhỏ để đổi lấy những con số ảo trên tài khoản ngân hàng.",
            "Omar chia sẻ câu chuyện xúc động về sự hữu hạn của đời người: Nếu cha mẹ bạn đã ngoài 60 tuổi và bạn chỉ về thăm họ 1 lần mỗi năm, bạn chỉ còn gặp họ khoảng 15 lần nữa trong đời."
        ],
        "hero_summary": {
            "title": "Bản đồ tỉnh thức về thứ tự ưu tiên tối thượng của cuộc đời",
            "items": [
                ("1. Toán học tàn nhẫn của thời gian", "Tiền mất đi có thể kiếm lại được gấp mười lần; thời gian bên cha mẹ già trôi qua vĩnh viễn không bao giờ lấy lại được."),
                ("2. Bẫy thành công cô độc", "Chinh phục đỉnh cao danh vọng nhưng khi quay đầu lại không còn ai để chia sẻ niềm vui là bi kịch lớn nhất."),
                ("3. Tái thiết lập ranh giới công việc", "Khóa lịch ăn tối cùng gia đình và những ngày cuối tuần trọn vẹn không điện thoại thông minh.")
            ],
            "mantra": "Tiền tài kiếm lại được ngay — Mẹ cha già yếu tháng ngày vơi dần"
        },
        "delusion": {
            "title": "ẢO TƯỞNG CỨ KIẾM THẬT NHIỀU TIỀN RỒI MỚI BÁO HIẾU & SỰ THẬT VỀ THỜI GIAN",
            "desc": "Người trẻ thường tự an ủi: 'Con đang bận cày cuốc để sau này có nhiều tiền lo cho cha mẹ'. Nhưng cha mẹ già không cần biệt thự hay xe sang; điều duy nhất họ mong mỏi là sự hiện diện bằng xương bằng thịt của bạn bên mâm cơm gia đình.",
            "compare_left": {
                "badge": "LẦM TƯỞNG TAI HẠI",
                "title": "Chờ đợi thành công lớn mới quay về nhà",
                "text": "Bỏ lỡ những năm tháng khỏe mạnh cuối cùng của cha mẹ để đổi lấy những dự án kinh doanh không hồi kết."
            },
            "compare_right": {
                "badge": "TỈNH THỨC SỐNG",
                "title": "Hiện diện trọn vẹn ngay trong hiện tại",
                "text": "Dành thời gian gọi điện mỗi ngày, về thăm nhà mỗi tháng và lắng nghe những câu chuyện xưa cũ của đấng sinh thành."
            },
            "matrix_title": "So sánh Hối tiếc muộn màng và Tỉnh thức trọn vẹn",
            "matrix_items": [
                ("Mải miết theo đuổi danh lợi", "• Khi nhận được giải thưởng lớn cũng là lúc cha mẹ đã nằm trên giường bệnh.<br>• Nỗi ân hận khôn nguôi theo suốt phần đời còn lại."),
                ("Cân bằng giữa sự nghiệp và chữ hiếu", "• Công việc kinh doanh phát triển bền vững trên nền tảng gia đình hòa thuận.<br>• Tâm hồn an yên, thanh thản vì đã làm tròn đạo hiếu.")
            ],
            "mantra": "Đừng chờ phú quý giàu sang — Mẹ cha khuất bóng muôn vàn tiếc thương"
        },
        "insights": [
            {"num": 1, "meta": "TOÁN HỌC CUỘC ĐỜI", "title": "Quy luật đếm ngược số lần gặp gỡ cha mẹ", "ground_truth": "Sau khi rời khỏi mái ấm gia đình năm 18 tuổi, bạn đã tiêu thụ 90% tổng thời gian được ở bên cha mẹ trong cả cuộc đời.", "surface": "Nghĩ rằng cha mẹ sẽ luôn luôn ở đó chờ đợi mình rảnh rỗi.", "nature": "Sự lão hóa sinh học không chờ đợi bất kỳ dự án kinh doanh nào của bạn hoàn thành.", "leverage": "Tính toán số ngày còn lại và chủ động lên lịch thăm nhà cố định mỗi quý trong năm.", "mantra": "Chín mươi phần trăm đã qua — Mười phần còn lại thiết tha giữ gìn"},
            {"num": 2, "meta": "SỰ HIỆN DIỆN THỰC SỰ", "title": "Có mặt bằng thể xác nhưng tâm trí dán vào điện thoại", "ground_truth": "Ngồi ăn cơm cùng cha mẹ nhưng tay liên tục bấm tin nhắn công việc là một hình thức bất kính tinh vi.", "surface": "Tự hào khoe mình đã về thăm nhà cuối tuần.", "nature": "Cha mẹ cảm nhận được sự xa cách và cô đơn ngay cả khi con cái đang ngồi bên cạnh.", "leverage": "Để điện thoại ở chế độ im lặng trong phòng ngủ trong suốt bữa ăn cùng gia đình.", "mantra": "Bên mâm cơm ấm ngọt ngào — Tắt đi màn ảo gửi trao ân tình"},
            {"num": 3, "meta": "LƯỢNG GIÁ THÀNH CÔNG", "title": "Thành công thực sự bắt đầu từ hạnh phúc dưới mái nhà", "ground_truth": "Nếu bạn được cả thế giới tung hô nhưng gia đình tan vỡ thì bạn là kẻ thất bại toàn tập.", "surface": "Đánh giá thành công bằng số lượng follower và doanh số công ty.", "nature": "Gia đình là gốc rễ của mọi nguồn năng lượng; gốc rễ mục ruỗng thì cái cây sớm muộn cũng đổ gục.", "leverage": "Đặt mục tiêu hạnh phúc gia đình ngang hàng với chỉ tiêu doanh số hàng năm.", "mantra": "Gốc rễ gia đạo bình an — Cơ đồ sự nghiệp vững vàng vươn cao"},
            {"num": 4, "meta": "LẮNG NGHE CHUYỆN XƯA", "title": "Ghi âm và lưu giữ giọng nói, ký ức của cha mẹ", "ground_truth": "Một ngày nào đó, bạn sẽ sẵn sàng đánh đổi toàn bộ gia tài chỉ để được nghe lại giọng nói của cha mẹ dù chỉ 1 phút.", "surface": "Tỏ ra khó chịu khi nghe cha mẹ kể đi kể lại những câu chuyện thời bao cấp.", "nature": "Đó là cách người già kết nối và truyền tải kho tàng ký ức của dòng họ cho thế hệ sau.", "leverage": "Dùng máy quay ghi lại những cuộc phỏng vấn sâu về cuộc đời và bài học của cha mẹ làm tư liệu gia phả.", "mantra": "Ghi âm giọng nói mẹ cha — Mai sau nhớ lại lệ nhòa rưng rưng"},
            {"num": 5, "meta": "QUẢN TRỊ CÔNG VIỆC", "title": "Công việc sẽ tự nở ra để lấp đầy thời gian bạn cho phép (Định luật Parkinson)", "ground_truth": "Nếu bạn không đặt giới hạn giờ làm, công việc kinh doanh sẽ nuốt chửng 100% cuộc sống riêng tư của bạn.", "surface": "Nói rằng mình 'quá bận' không có thời gian cho gia đình.", "nature": "Sự bận rộn thường là bình phong che đậy sự yếu kém trong quản trị và phân quyền.", "leverage": "Quy định giờ giới nghiêm: Đúng 18h tối tắt máy tính và toàn tâm toàn ý cho gia đình.", "mantra": "Định luật thời gian rạch ròi — Đúng giờ buông việc thảnh thơi gia đình"},
            {"num": 6, "meta": "BÁO HIẾU BẰNG SỰ AN TÂM", "title": "Món quà lớn nhất cho cha mẹ là sự trưởng thành đạo đức của con", "ground_truth": "Cha mẹ không cần tiền của bạn kiếm được từ những việc làm mờ ám, phi đạo đức.", "surface": "Mang thật nhiều tiền về biếu cha mẹ nhưng sống cuộc đời sa đọa, bất an.", "nature": "Sự an tâm về nhân cách và lối sống tử tế của con cái là liều thuốc bổ dưỡng nhất cho tuổi già của đấng sinh thành.", "leverage": "Sống chính trực, minh bạch trong mọi giao dịch kinh doanh để cha mẹ tự hào.", "mantra": "Sống đời chính trực thiện lương — Mẹ cha an dạ muôn đường tự hào"},
            {"num": 7, "meta": "TÂM THỨC VÔ THƯỜNG", "title": "Chiêm nghiệm cái chết (Memento Mori) để sống sâu sắc hơn", "ground_truth": "Nhận thức rõ ràng về sự hữu hạn của kiếp người giúp bạn lập tức loại bỏ những điều phù phiếm vô nghĩa.", "surface": "Sống như thể mình và những người thân yêu sẽ bất tử mãi mãi.", "nature": "Tâm thức vô thường đánh thức lòng trắc ẩn và sự trân trọng từng giây phút hiện tại bên người thân.", "leverage": "Mỗi sáng tự nhắc nhở: 'Hôm nay có thể là ngày cuối cùng mình được ôm người thân yêu'.", "mantra": "Vô thường nhắc nhở bên tai — Trân quý hiện tại ngày mai đổi dời"},
            {"num": 8, "meta": "DI SẢN TÌNH THƯƠNG", "title": "Tình thương yêu là tài sản duy nhất truyền qua nhiều thế hệ", "ground_truth": "Con cái bạn sẽ đối xử với bạn khi về già đúng như cách bạn đang đối xử với cha mẹ bạn hôm nay.", "surface": "Nghĩ rằng chỉ cần để lại nhiều bất động sản cho con là đủ.", "nature": "Trẻ con học bằng cách quan sát hành vi thực tế của cha mẹ, không học qua lời rao giảng.", "leverage": "Làm gương hiếu thảo với cha mẹ để con cái noi theo như một dòng chảy phúc đức.", "mantra": "Gương xưa hiếu thảo rạng ngời — Cháu con tiếp bước trọn đời noi theo"}
        ],
        "environment": {
            "title": "Thiết lập không gian sum vầy ấm cúng",
            "items": [
                ("1. Bàn ăn tròn ấm cúng không có tivi", "Mọi thành viên ngồi quây quần nhìn thấy mặt nhau, khuyến khích những cuộc trò chuyện chân thành."),
                ("2. Khay đựng điện thoại ở cửa ra vào", "Mọi người bước vào nhà đều đặt điện thoại vào khay để tâm trí hoàn toàn thuộc về gia đình."),
                ("3. Album ảnh gia đình in trên giấy", "Lật từng trang ảnh in để sống lại những kỷ niệm đẹp thay vì xem lướt trên màn hình điện thoại.")
            ],
            "mantra": "Bàn ăn tròn ấm yêu thương — Tắt màn hình ảo vấn vương ân tình"
        },
        "emotional": {
            "title": "Nuôi dưỡng lòng hiếu thảo và sự tĩnh lặng nội tâm",
            "items": [
                ("1. Tha thứ cho những khiếm khuyết của cha mẹ", "Hiểu rằng cha mẹ đã nuôi nấng bạn bằng tất cả những gì tốt nhất họ có trong hoàn cảnh lịch sử khó khăn của họ."),
                ("2. Dũng cảm nói lời yêu thương và xin lỗi", "Không ngần ngại ôm cha mẹ và nói câu 'Con yêu cha mẹ' trước khi quá muộn."),
                ("3. Bình an đón nhận quy luật sinh lão bệnh tử", "Đồng hành cùng cha mẹ qua tuổi già bằng sự chăm sóc ân cần và lòng biết ơn sâu sắc.")
            ],
            "mantra": "Thương yêu tha thứ muôn vàn — Mẹ cha ấm dạ muôn vàn an vui"
        }
    },

    # 18. Genius Personal Brand (jKaXbbcC_uM)
    {
        "id": raw_vids[18]['id'],
        "slug": "genius-personal-brand-advice-entrepreneurs-podcast.html",
        "ep_code": "OE18",
        "cat_badge": "02 / THƯƠNG HIỆU CÁ NHÂN & VỊ THẾ DẪN ĐẦU",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "ĐỊNH VỊ CÁ NHÂN THIÊN TÀI: BIẾN TOÀN BỘ TRẢI NGHIỆM SỐNG THÀNH ĐÒN BẨY",
        "orig_title": raw_vids[18]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[18]['id']}",
        "publish_date": raw_vids[18]['date'],
        "raw_date": f"{raw_vids[18]['raw_date'][:4]}-{raw_vids[18]['raw_date'][4:6]}-{raw_vids[18]['raw_date'][6:]}",
        "duration": "46 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Đời ta là một pho kinh — Chắt chiu trải nghiệm dựng thành uy danh",
        "lead_points": [
            "Lời khuyên xây dựng thương hiệu cá nhân thiên tài nhất: Đừng cố gắng tạo ra một nhân vật hoàn hảo để đóng kịch, hãy biến chính cuộc sống thực tế (cả chiến thắng lẫn thất bại) thành chất liệu truyền thông thu hút nhất.",
            "Phân tích nguyên lý 'Tư liệu hóa thay vì Sáng tạo' (Document, Don't Create): Cách ghi lại các cuộc họp, quyết định kinh doanh và bài học thường nhật để tạo ra nội dung bất tận mà không tốn công vắt óc suy nghĩ."
        ],
        "hero_summary": {
            "title": "Khung biến cuộc đời thành cỗ máy truyền thông tự nhiên",
            "items": [
                ("1. Tư liệu hóa hành trình (Documenting)", "Ghi lại những gì bạn đang thực sự làm mỗi ngày thay vì cố gắng ngồi nghĩ ra những điều vĩ mô."),
                ("2. Góc nhìn độc bản (Unique Lens)", "Cùng một sự kiện, người có góc nhìn triết lý sâu sắc sẽ rút ra bài học đắt giá khiến người khác phải trầm trồ."),
                ("3. Sự hòa quyện giữa cuộc sống và công việc", "Khách hàng không chỉ mua sản phẩm; họ muốn học theo phong cách sống và triết lý nhân sinh của bạn.")
            ],
            "mantra": "Sống sao viết vậy chân tình — Cuộc đời thành đuốc soi mình soi ai"
        },
        "delusion": {
            "title": "ẢO TƯỞNG PHẢI ĐÓNG KỊCH & BẢN CHẤT SỨC MẠNH CỦA SỰ THẬT",
            "desc": "Người ta thường nghĩ xây dựng thương hiệu cá nhân là phải mặc vest sang trọng, thuê xe xịn và nói những lời đạo lý bay bổng. Sự giả tạo đó vô cùng mệt mỏi và nhanh chóng bị khán giả lột mặt nạ.",
            "compare_left": {
                "badge": "LỐI SỐNG GIẢ TẠO",
                "title": "Cố gắng diễn vai người thành đạt hoàn hảo",
                "text": "Luôn căng thẳng vì sợ lộ ra điểm yếu hoặc thất bại; sống cuộc đời hai mặt mệt mỏi."
            },
            "compare_right": {
                "badge": "SỨC HÚT THỰC SỰ",
                "title": "Dũng cảm công khai những góc khuất và bài học",
                "text": "Sự chân thật mộc mạc tạo ra sức mạnh kết nối vĩ đại, biến bạn thành biểu tượng của sự dũng cảm và chân thành."
            },
            "matrix_title": "So sánh Thương hiệu nhân tạo và Thương hiệu bắt rễ từ đời thực",
            "matrix_items": [
                ("Thương hiệu diễn kịch", "• Nhanh chóng kiệt sức vì phải duy trì vỏ bọc dối trá.<br>• Khi gặp scandal, lòng tin sụp đổ hoàn toàn không thể cứu vãn."),
                ("Thương hiệu bắt rễ từ đời thực", "• Càng làm càng thoải mái vì bạn chỉ cần là chính mình.<br>• Khán giả yêu quý con người thật, gắn bó trung thành qua hàng thập kỷ.")
            ],
            "mantra": "Đóng kịch mệt mỏi thân tâm — Sống thật rạng rỡ ngàn năm vững bền"
        },
        "insights": [
            {"num": 1, "meta": "TƯ LIỆU HÓA HÀNH TRÌNH", "title": "Nguyên lý Document, Don't Create", "ground_truth": "Bạn không cần phải mất hàng giờ nghĩ kịch bản; bạn chỉ cần bật máy quay ghi lại những gì đang diễn ra trong doanh nghiệp của bạn.", "surface": "Ngồi trước trang giấy trắng và bế tắc vì không biết hôm nay viết gì.", "nature": "Thực tế cuộc sống kinh doanh sinh động và hấp dẫn hơn bất kỳ kịch bản hư cấu nào.", "leverage": "Quay lại các cuộc họp chiến lược, các buổi trao đổi với khách hàng (với sự đồng ý) và chia sẻ bài học rút ra.", "mantra": "Ghi lại cuộc sống hằng ngày — Kịch bản chân thật đong đầy giá trị"},
            {"num": 2, "meta": "BÀI HỌC TỪ THẤT BẠI", "title": "Thất bại hôm nay là nội dung đắt giá nhất của ngày mai", "ground_truth": "Người ta học được từ sai lầm của bạn nhiều hơn từ những chiến thắng dễ dàng.", "surface": "Giấu kín những dự án thua lỗ vì sợ bị coi là yếu kém.", "nature": "Sự dũng cảm mổ xẻ thất bại chứng minh bạn là người dám làm, dám chịu và có tinh thần cầu tiến tột bậc.", "leverage": "Làm video: 'Tôi đã mất 1 tỷ đồng vì 3 sai lầm này như thế nào'.", "mantra": "Mất tiền đổi lấy bài hay — Chia sẻ chân thật dựng xây cơ đồ"},
            {"num": 3, "meta": "GÓC NHÌN ĐỘC BẢN", "title": "Góc nhìn (Perspective) quan trọng hơn thông tin (Information)", "ground_truth": "Thông tin đầy rẫy trên Google; người ta tìm đến bạn để xem bạn đánh giá thông tin đó như thế nào.", "surface": "Chỉ làm nhiệm vụ điểm tin tức thời sự một cách vô hồn.", "nature": "Thế giới quan và hệ giá trị đạo đức của bạn là thứ duy nhất tạo nên sự khác biệt độc bản.", "leverage": "Đưa ra bình luận sắc bén dưới lăng kính kinh nghiệm thực chiến của riêng bạn cho các sự kiện nóng.", "mantra": "Thông tin thiên hạ thiếu chi — Góc nhìn thấu suốt người ghi vào lòng"},
            {"num": 4, "meta": "LỒNG GHÉP ĐỜI SỐNG", "title": "Kết hợp sở thích cá nhân vào nội dung chuyên môn", "ground_truth": "Khán giả kết nối với bạn qua những điểm chạm sở thích chung (Cà phê, chạy bộ, làm vườn, âm nhạc).", "surface": "Chỉ nói thuần túy về công việc kinh doanh khô khan.", "nature": "Những sở thích cá nhân giúp chân dung của bạn trở nên sống động, gần gũi và có chiều sâu.", "leverage": "Quay cảnh bạn pha cà phê sáng hoặc chạy bộ trong khi chia sẻ bài học quản trị kinh doanh.", "mantra": "Cà phê buổi sáng thơm lành — Triết lý quản trị đan thanh cuộc đời"},
            {"num": 5, "meta": "NGÔN TỪ MỘC MẠC", "title": "Nói bằng thứ ngôn ngữ của quán nước vỉa hè", "ground_truth": "Ngôn ngữ càng bình dân, sức lan tỏa càng rộng lớn và chạm sâu vào lòng người.", "surface": "Dùng từ ngữ bác học phức tạp để chứng tỏ học thức uyên thâm.", "nature": "Sự cao ngạo ngôn từ tạo ra bức tường ngăn cách giữa chuyên gia và công chúng.", "leverage": "Gọt giũa câu chữ, dùng những từ ngữ đời thường mộc mạc nhất để diễn đạt các nguyên lý vĩ mô.", "mantra": "Lời ăn tiếng nói bình dân — Chạm vào ruột gan muôn phần khắc sâu"},
            {"num": 6, "meta": "TÍNH NHẤT QUÁN", "title": "Sống đúng với những gì bạn rao giảng trên mạng", "ground_truth": "Sự mâu thuẫn giữa lời nói trên mạng và hành vi ngoài đời thực là cái chết êm ái của thương hiệu.", "surface": "Nói đạo lý từ bi trên mạng nhưng đối xử tệ bạc với nhân viên và người thân.", "nature": "Năng lượng giả tạo sẽ bị phát hiện bởi những người tiếp xúc gần và sự thật sẽ sớm lan truyền.", "leverage": "Lấy tiêu chuẩn nội dung làm chuẩn mực tu dưỡng đạo đức và hành vi cho chính bản thân mỗi ngày.", "mantra": "Lời nói đi với việc làm — Trong ngoài như một tiếng thơm lưu truyền"},
            {"num": 7, "meta": "ĐÒN BẨY QUAN HỆ", "title": "Nâng đỡ những người khác trên kênh của bạn", "ground_truth": "Khen ngợi và giới thiệu những người tài năng khác sẽ làm tăng uy tín của chính bạn.", "surface": "Sợ người khác nổi bật hơn mình nên không bao giờ nhắc đến ai.", "nature": "Sự hào sảng chứng minh bạn có tâm thế đủ đầy và không sợ hãi sự cạnh tranh.", "leverage": "Làm video tôn vinh các cộng sự xuất sắc và những đối tác tử tế đã giúp đỡ bạn.", "mantra": "Nâng người vươn tới trời cao — Tự nhiên vị thế dạt dào ánh quang"},
            {"num": 8, "meta": "BẢO VỆ NGUYÊN BẢN", "title": "Không bán linh hồn vì những bản hợp đồng tài trợ bẩn", "ground_truth": "Quảng cáo một sản phẩm kém chất lượng vì tiền sẽ hủy hoại uy tín bạn gầy dựng cả đời.", "surface": "Nhận bất kỳ hợp đồng tài trợ nào miễn là có tiền thù lao cao.", "nature": "Khán giả tin bạn nên mới mua sản phẩm bạn giới thiệu; phản bội niềm tin đó là dấu chấm hết.", "leverage": "Từ chối thẳng thừng mọi lời mời quảng cáo cho các sản phẩm bạn chưa từng tự tay sử dụng và kiểm chứng.", "mantra": "Lương tâm giữ sáng như gương — Bạc tiền không chuyển muôn phương vững bền"}
        ],
        "environment": {
            "title": "Bố trí thiết bị gọn nhẹ để sẵn sàng quay mọi lúc",
            "items": [
                ("1. Điện thoại iPhone với gimbal chống rung", "Sẵn sàng ghi lại những khoảnh khắc đời thực sống động khi đang di chuyển ngoài đường."),
                ("2. Micro cài áo nhỏ gọn cắm thẳng vào điện thoại", "Bắt âm giọng nói rõ ràng ngay cả khi đang đi bộ trong quán cà phê hay công viên."),
                ("3. Ứng dụng ghi chú nhanh Apple Notes hoặc Notion", "Ghi lại ngay lập tức các ý tưởng lóe lên trong đầu trước khi chúng biến mất.")
            ],
            "mantra": "Máy sẵn trong tay gọn gàng — Ý tưởng lóe sáng nhẹ nhàng ghi ghi"
        },
        "emotional": {
            "title": "Nuôi dưỡng sự tự tin vào giá trị độc bản của bản thân",
            "items": [
                ("1. Tôn trọng hành trình riêng biệt của chính mình", "Không cần phải trở thành Steve Jobs hay Elon Musk; thế giới đang cần phiên bản tốt nhất của chính bạn."),
                ("2. Tha thứ cho những lỗi lầm trong quá khứ", "Xem mọi vấp ngã là học phí bắt buộc để tôi luyện nên con người bản lĩnh của ngày hôm nay."),
                ("3. Sống trọn vẹn từng khoảnh khắc", "Tận hưởng từng hơi thở và cuộc gặp gỡ, biết ơn cuộc đời vì đã cho mình cơ hội được cống hiến.")
            ],
            "mantra": "Tự tin là chính mình thôi — Độc bản tỏa sáng đất trời ngát hương"
        }
    },

    # 19. Stop Being Overlooked (VNf9_nT8QtQ)
    {
        "id": raw_vids[19]['id'],
        "slug": "stop-being-overlooked-become-famous-any-industry-podcast.html",
        "ep_code": "OE19",
        "cat_badge": "02 / THƯƠNG HIỆU CÁ NHÂN & VỊ THẾ DẪN ĐẦU",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "THOÁT KHỎI SỰ VÔ DANH: CÔNG THỨC TRỞ NÊN NỔI BẬT VÀ DẪN ĐẦU TRONG NGÀNH",
        "orig_title": raw_vids[19]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[19]['id']}",
        "publish_date": raw_vids[19]['date'],
        "raw_date": f"{raw_vids[19]['raw_date'][:4]}-{raw_vids[19]['raw_date'][4:6]}-{raw_vids[19]['raw_date'][6:]}",
        "duration": "51 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Tài năng giấu kín ai hay — Đứng lên cất tiếng tháng ngày rạng danh",
        "lead_points": [
            "Bi kịch lớn nhất của người tài là bị ngó lơ (Overlooked) trong khi những kẻ kém cỏi hơn nhưng biết làm truyền thông lại chiếm trọn khách hàng và sự tôn vinh của xã hội.",
            "Omar vạch ra bản kế hoạch 2026: Cách phá vỡ sự vô danh bằng chiến lược 'Sự hiện diện đa kênh áp đảo' (Omnipresence) và định vị bản thân là chuyên gia không thể thay thế trong một ngách hẹp."
        ],
        "hero_summary": {
            "title": "Chiến lược thoát khỏi cái bóng vô danh bước ra ánh sáng",
            "items": [
                ("1. Thước đo thành công mới: Khả năng được nhận biết", "Giỏi chuyên môn chỉ là điều kiện cần; được thị trường biết đến và công nhận mới là điều kiện đủ để thành công."),
                ("2. Tấn công ngách hẹp (Niche Dominance)", "Trở thành con cá lớn trong ao nhỏ trước khi bước ra biển lớn đại dương."),
                ("3. Tần suất xuất hiện áp đảo", "Xuất hiện liên tục trước mắt khách hàng mục tiêu cho đến khi họ không thể phớt lờ bạn được nữa.")
            ],
            "mantra": "Tài năng phải có tiếng vang — Vô danh lủi thủi muôn vàn thiệt thòi"
        },
        "delusion": {
            "title": "ẢO TƯỞNG HỮU XẠ TỰ NHIÊN HƯƠNG & SỰ THẬT VỀ SỰ CẠNH TRANH CHÚ Ý",
            "desc": "Câu ngạn ngữ 'Hữu xạ tự nhiên hương' đã hoàn toàn lỗi thời trong thế giới internet ngập tràn thông tin rác. Nếu bạn không chủ động quảng bá và cất lên tiếng nói, hương thơm của bạn sẽ bị chôn vùi dưới đáy đại dương.",
            "compare_left": {
                "badge": "LỐI MÒN BẢO THỦ",
                "title": "Ngồi im chờ đợi người khác tự phát hiện ra mình",
                "text": "Nghĩ rằng chỉ cần làm tốt việc của mình thì tự khắc khách hàng sẽ ùn ùn kéo đến tìm kiếm."
            },
            "compare_right": {
                "badge": "CHỦ ĐỘNG TẤN CÔNG",
                "title": "Chủ động bước ra ánh sáng và định hình luật chơi",
                "text": "Tận dụng mọi nền tảng video để liên tục giáo dục thị trường và khẳng định vị thế dẫn đầu."
            },
            "matrix_title": "So sánh Chuyên gia vô danh và Chuyên gia có thương hiệu mạnh",
            "matrix_items": [
                ("Chuyên gia vô danh", "• Giỏi chuyên môn nhưng luôn phải chật vật kiếm ăn từng tháng.<br>• Phải hạ giá và van xin khách hàng ký hợp đồng."),
                ("Chuyên gia có thương hiệu áp đảo", "• Khách hàng xếp hàng chờ đợi hàng tháng để được phục vụ.<br>• Nắm toàn quyền định giá cao cấp và lựa chọn đối tác phù hợp.")
            ],
            "mantra": "Chờ đợi hương bay luống công — Chủ động cất tiếng rạng dòng thành công"
        },
        "insights": [
            {"num": 1, "meta": "BẪY TỰ MÃN CHUYÊN MÔN", "title": "Sự xuất sắc bị giấu kín là một dạng lãng phí tài nguyên", "ground_truth": "Nếu bạn có phương pháp chữa bệnh xuất sắc mà không ai biết, bệnh nhân vẫn tiếp tục chịu đau đớn.", "surface": "Tự hào rằng mình là người khiêm tốn không màng danh lợi.", "nature": "Sự khiêm tốn tiêu cực thực chất là vỏ bọc che đậy nỗi sợ bị từ chối và lười biếng làm truyền thông.", "leverage": "Xem việc làm thương hiệu là nghĩa vụ đạo đức để đưa giải pháp tốt đến tay người cần.", "mantra": "Tài giỏi phải cứu nhân gian — Giấu kín trong tối muôn vàn tiếc thay"},
            {"num": 2, "meta": "CHIẾM LĨNH NGÁCH NHỎ", "title": "Thu hẹp thị trường mục tiêu cho đến khi bạn là số 1", "ground_truth": "Rất khó để trở thành 'Luật sư giỏi nhất Việt Nam'; nhưng rất dễ để thành 'Luật sư giỏi nhất về tranh chấp bản quyền nội dung số'.", "surface": "Cố gắng phục vụ tất cả mọi người trong mọi lĩnh vực.", "nature": "Chuyên gia đa năng (Generalist) bị xem là tầm thường; chuyên gia đặc trị (Specialist) được trả thù lao gấp 10 lần.", "leverage": "Định vị bản thân gắn liền với 1 vấn đề cụ thể của 1 nhóm khách hàng cụ thể.", "mantra": "Ngách nhỏ ta đứng đầu đàn — Biển lớn bon chen muôn vàn sóng xô"},
            {"num": 3, "meta": "QUY LUẬT 7 GIỜ", "title": "Khách hàng cần 7 giờ tiếp xúc nội dung trước khi ra quyết định lớn", "ground_truth": "Theo nghiên cứu của Google, người mua hàng B2B cần tiêu thụ trung bình 7 giờ nội dung trên 4 nền tảng khác nhau.", "surface": "Kỳ vọng khách hàng ký hợp đồng sau khi chỉ xem 1 video ngắn 60 giây.", "nature": "Niềm tin cần thời gian tích lũy qua nhiều bối cảnh tiếp xúc khác nhau.", "leverage": "Xây dựng kho video YouTube dài kết hợp podcast để khách hàng có thể nghe say sưa suốt nhiều giờ.", "mantra": "Bảy giờ gắn kết ân tình — Khách nghe thấm thía trao mình niềm tin"},
            {"num": 4, "meta": "QUAN HỆ BÁO CHÍ", "title": "Tự tạo ra các sự kiện tin tức để thu hút truyền thông", "ground_truth": "Báo chí luôn khao khát những góc nhìn mới lạ và những câu chuyện đột phá có số liệu dẫn chứng.", "surface": "Chi tiền mua các bài PR báo chí rẻ tiền không ai đọc.", "nature": "Các bài báo tự nhiên khen ngợi bạn có sức nặng bảo chứng gấp trăm lần bài quảng cáo mua bằng tiền.", "leverage": "Công bố các báo cáo khảo sát độc quyền về ngành nghề của bạn để báo chí tự động trích dẫn.", "mantra": "Số liệu khảo sát rõ ràng — Báo chí đưa tin rộn ràng uy danh"},
            {"num": 5, "meta": "PHONG CÁCH ĐẶC TRƯNG", "title": "Tạo ra một dấu ấn thị giác độc bản không thể nhầm lẫn", "ground_truth": "Những nhân vật biểu tượng luôn có một phụ kiện hoặc phong cách thời trang cố định (Áo cổ lọ Steve Jobs, Kính tròn Gandhi).", "surface": "Mỗi ngày mặc một kiểu trang phục lộn xộn không có định hình phong cách.", "nature": "Bộ não con người ghi nhớ hình ảnh nhanh hơn chữ viết; một dấu ấn thị giác giúp bạn được nhận diện tức thì.", "leverage": "Chọn một màu sắc chủ đạo, một kiểu mũ hoặc một món phụ kiện đặc trưng xuất hiện trong mọi video.", "mantra": "Dấu ấn thị giác phân minh — Nhìn qua nhận diện bóng hình chuyên gia"},
            {"num": 6, "meta": "XUẤT HIỆN SỰ KIỆN", "title": "Bước lên các sân khấu lớn của ngành", "ground_truth": "Đứng trên bục diễn giả tự động mang lại cho bạn hào quang uy quyền của người dẫn đầu.", "surface": "Chỉ ngồi dưới hàng ghế khán giả lắng nghe người khác nói.", "nature": "Người đứng trên sân khấu là người định hình nhận thức của toàn bộ hội trường.", "leverage": "Chủ động gửi đề xuất tham luận tới các ban tổ chức hội thảo chuyên ngành để được mời làm diễn giả.", "mantra": "Bước lên sân khấu hiên ngang — Truyền trao tri thức muôn vàn tiếng vang"},
            {"num": 7, "meta": "DÁM GÂY TRANH CÃI", "title": "Có quan điểm rõ ràng và dám chỉ trích cái sai", "ground_truth": "Một thương hiệu làm hài lòng tất cả mọi người là một thương hiệu nhạt nhòa không ai nhớ đến.", "surface": "Luôn phát biểu những điều dĩ hòa vi quý, không dám đụng chạm ai.", "nature": "Sự dũng cảm lên tiếng bảo vệ chân lý tạo ra lượng người ủng hộ cuồng nhiệt sẵn sàng bảo vệ bạn.", "leverage": "Tấn công trực diện vào những phương pháp sai lầm đang phổ biến và gây hại cho người tiêu dùng trong ngành.", "mantra": "Dám nói thẳng thật chẳng màng — Người khôn nể phục kẻ gian hãi hùng"},
            {"num": 8, "meta": "TÍNH BỀN BỈ ÁP ĐẢO", "title": "Chiến thắng bằng việc là người cuối cùng còn trụ lại", "ground_truth": "Đa số đối thủ của bạn sẽ tự động biến mất và bỏ cuộc sau 1–2 năm vì thiếu kiên trì.", "surface": "Sốt ruột khi thấy đối thủ tăng trưởng nhanh bằng các chiêu trò ngắn hạn.", "nature": "Kinh doanh là một trò chơi vô hạn (Infinite Game); người chiến thắng không phải người chạy nhanh nhất, mà là người không bao giờ dừng bước.", "leverage": "Giữ nhịp độ xuất bản đều đặn, ăn uống lành mạnh và tập luyện thể thao để duy trì sức bền suốt 20 năm.", "mantra": "Trò chơi vô hạn đường dài — Kiên trì trụ lại tương lai rạng ngời"}
        ],
        "environment": {
            "title": "Thiết lập bối cảnh định vị chuyên gia quyền lực",
            "items": [
                ("1. Góc quay ngang tầm mắt hoặc hơi hướng lên nhẹ", "Tạo cảm giác vững chãi, uy nghi và đường bệ của một nhà lãnh đạo."),
                ("2. Kệ sách trưng bày các giải thưởng và sách chuyên ngành", "Các chứng nhận uy tín nằm mờ phía sau hậu cảnh tạo sự tin cậy ngầm định."),
                ("3. Trang phục phẳng phiu chuẩn phong thái doanh nhân", "Chọn trang phục có cổ, tông màu trung tính (Xanh navy, Đen, Xám) toát lên vẻ chuyên nghiệp.")
            ],
            "mantra": "Góc quay vững chãi uy nghi — Tấm lòng rộng mở ngại gì phong ba"
        },
        "emotional": {
            "title": "Giải phóng nỗi sợ bị chú ý và phán xét",
            "items": [
                ("1. Sẵn sàng đón nhận những ý kiến trái chiều", "Hiểu rằng khi bạn nổi bật, việc có 10% người ghét bạn là dấu hiệu chứng minh bạn đã có lập trường rõ ràng."),
                ("2. Giữ sự khiêm tốn từ tận đáy lòng", "Danh tiếng chỉ là công cụ để phụng sự, không phải thước đo để kiêu ngạo coi thường người khác."),
                ("3. Tận hưởng niềm vui của sự cống hiến", "Biết ơn vì tiếng nói của mình đã truyền cảm hứng và thay đổi cuộc sống của nhiều người.")
            ],
            "mantra": "Tiếng vang lan tỏa muôn nơi — Giữ tâm khiêm tốn trọn đời an vui"
        }
    },

    # 20. New Way Monetize (HRFZ527j0DE)
    {
        "id": raw_vids[20]['id'],
        "slug": "new-way-to-monetize-your-content-online-podcast.html",
        "ep_code": "OE20",
        "cat_badge": "03 / CHIẾN LƯỢC NỘI DUNG YOUTUBE & VIDEO TRIỆU VIEW",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "LỘ TRÌNH KIẾM TIỀN TỪ NỘI DUNG SỐ: MASTERCLASS CHUYỂN ĐỔI NGƯỜI XEM THÀNH KHÁCH HÀNG",
        "orig_title": raw_vids[20]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[20]['id']}",
        "publish_date": raw_vids[20]['date'],
        "raw_date": f"{raw_vids[20]['raw_date'][:4]}-{raw_vids[20]['raw_date'][4:6]}-{raw_vids[20]['raw_date'][6:]}",
        "duration": "1 giờ 30 phút",
        "read_time": "~9 phút chắt lọc",
        "hero_quote": "Nội dung dẫn lối đưa đường — Kiếm tiền bền vững muôn phương đón chào",
        "lead_points": [
            "Khóa học tổng hợp Masterclass về 5 dòng doanh thu cốt lõi của một Creator hiện đại: Dịch vụ tư vấn cao cấp, Khóa học Hybrid, Cộng đồng trả phí định kỳ, Tiếp thị liên kết chọn lọc và Hợp đồng tài trợ thương hiệu.",
            "Omar bóc tách sai lầm của 90% creator chỉ chăm chăm dựa vào tiền quảng cáo AdSense còm cõi, và hướng dẫn cách xây dựng cỗ máy doanh thu đa tầng sinh lời ngay cả khi kênh chỉ có vài trăm lượt xem mỗi video."
        ],
        "hero_summary": {
            "title": "Ma trận 5 dòng doanh thu bền vững cho nhà sáng tạo",
            "items": [
                ("1. Tự do tài chính khỏi AdSense", "Tiền quảng cáo AdSense chỉ là tiền tiêu vặt; dòng tiền thực sự đến từ các sản phẩm và dịch vụ do chính bạn sở hữu."),
                ("2. Cộng đồng thành viên trả phí (Membership/Skool)", "Tạo dòng tiền định kỳ hàng tháng (MRR) ổn định giúp bạn yên tâm sáng tạo nội dung dài hạn."),
                ("3. Phễu chuyển đổi bậc thang", "Dẫn dắt khán giả từ nội dung miễn phí -> Sản phẩm giá thấp -> Khóa học chuyên sâu -> Cố vấn 1-1 cấp cao.")
            ],
            "mantra": "Năm dòng tài chính hanh thông — Thoát ly quảng cáo thỏa lòng ước mong"
        },
        "delusion": {
            "title": "ẢO TƯỞNG LÀM YOUTUBE ĐỂ ĂN TIỀN QUẢNG CÁO & SỰ THẬT VỀ QUY MÔ DÒNG TIỀN",
            "desc": "Người mới thường mơ mộng về việc nhận tiền nghìn đô từ YouTube AdSense. Nhưng với tỷ giá RPM tại Việt Nam hay các thị trường ngách, 100.000 view chỉ mang về vài trăm nghìn đồng không đủ tiền trả tiền điện và internet. Creator thông minh sở hữu sản phẩm của riêng mình.",
            "compare_left": {
                "badge": "LỐI MÒN NÔ LỆ ADS",
                "title": "Phụ thuộc 100% vào tiền chia sẻ quảng cáo của nền tảng",
                "text": "Phải cày view kiệt sức, làm nội dung giật gân rẻ tiền để kiếm từng đồng bạc cắc từ Google AdSense."
            },
            "compare_right": {
                "badge": "TƯ DUY DOANH NHÂN SỐ",
                "title": "Sở hữu toàn bộ chuỗi giá trị sản phẩm và dịch vụ",
                "text": "Xem YouTube là công cụ thu hút khách hàng miễn phí cho hệ sinh thái kinh doanh trị giá hàng tỷ đồng của mình."
            },
            "matrix_title": "So sánh Nô lệ AdSense và Doanh nhân sáng tạo nội dung",
            "matrix_items": [
                ("Nô lệ AdSense", "• 1 triệu view kiếm được $300 - $1.000.<br>• Thu nhập bấp bênh, tâm trạng phụ thuộc vào sự điều chỉnh thuật toán của nền tảng."),
                ("Doanh nhân sở hữu sản phẩm", "• 10.000 view kiếm được $10.000 - $50.000 từ việc bán khóa học và tư vấn.<br>• Toàn quyền kiểm soát dòng tiền và tương lai của chính mình.")
            ],
            "mantra": "AdSense tiền lẻ bấp bênh — Sản phẩm tự có dựng nên cơ đồ"
        },
        "insights": [
            {"num": 1, "meta": "GIẢI PHÓNG KHỎI ADS", "title": "AdSense là nguồn thu nhập kém hiệu quả nhất thế giới", "ground_truth": "Bạn đang cho các thương hiệu khác mượn khán giả của mình để họ bán sản phẩm và kiếm tiền tỷ, trong khi bạn chỉ nhận vài đồng xu lẻ.", "surface": "Tự hào khoe tháng này kiếm được 5 triệu từ quảng cáo YouTube.", "nature": "Mỗi người xem bấm vào quảng cáo rời bỏ kênh của bạn là một khách hàng bạn đã đánh mất vĩnh viễn.", "leverage": "Tắt quảng cáo của bên thứ ba hoặc thay thế bằng lời giới thiệu sản phẩm của chính bạn.", "mantra": "Quảng cáo người khác tiền vơi — Sản phẩm mình bán trọn đời ấm no"},
            {"num": 2, "meta": "DÒNG TIỀN ĐỊNH KỲ (MRR)", "title": "Sức mạnh của mô hình cộng đồng trả phí hàng tháng", "ground_truth": "100 thành viên trả $50/tháng mang lại $5.000 thu nhập định kỳ bền vững mỗi tháng.", "surface": "Tháng nào cũng phải lo sốt vó đi tìm khách hàng mới để chốt sale.", "nature": "Thu nhập định kỳ đều đặn giúp giải phóng áp lực tài chính và cho phép bạn tập trung nâng cao chất lượng nội dung.", "leverage": "Xây dựng cộng đồng Skool thu phí $49 - $99/tháng với các buổi hỏi đáp và kết nối kinh doanh hàng tuần.", "mantra": "Thu nhập định kỳ mỗi trăng — Tâm an trí sáng thăng hoa cõi lòng"},
            {"num": 3, "meta": "TIẾP THỊ LIÊN KẾT CHỌN LỌC", "title": "Chỉ làm Affiliate cho các công cụ phần mềm bạn tự dùng mỗi ngày", "ground_truth": "Các phần mềm SaaS trả hoa hồng định kỳ trọn đời (Recurring Commission) là mỏ vàng thụ động.", "surface": "Tiếp thị liên kết hàng trăm món đồ tạp nham trên Shopee để ăn vài phần trăm hoa hồng nhỏ.", "nature": "Giới thiệu phần mềm thiết yếu cho doanh nghiệp giúp bạn nhận hoa hồng đều đặn mỗi khi khách gia hạn hàng tháng.", "leverage": "Đặt link giới thiệu các phần mềm bạn tin dùng (Hosting, Email, Tool AI) trong phần mô tả video.", "mantra": "Phần mềm thiết yếu giới thiệu — Hoa hồng định kỳ đều đều chảy về"},
            {"num": 4, "meta": "HỢP ĐỒNG TÀI TRỢ", "title": "Báo giá tài trợ dựa trên uy tín và độ chuyển đổi, không dựa trên view", "ground_truth": "Các nhãn hàng B2B sẵn sàng trả $5.000 cho 1 video chỉ có 2.000 view nếu khán giả của bạn là các CEO và nhà sáng lập.", "surface": "Đồng ý nhận tài trợ giá rẻ mạt dựa trên công thức tính CPM thông thường.", "nature": "Chất lượng của khán giả (Audience Quality) quyết định giá trị thương mại của kênh.", "leverage": "Làm bản truyền thông (Media Kit) nêu rõ chân dung khán giả thu nhập cao và tỷ lệ chuyển đổi thực tế.", "mantra": "Khán giả chất lượng đỉnh cao — Hợp đồng tài trợ vút cao ngút ngàn"},
            {"num": 5, "meta": "SẢN PHẨM RÀO CẢN THẤP", "title": "Món hàng chuyển đổi đầu tiên $7 - $27 (Tripwire Offer)", "ground_truth": "Khoảng cách tâm lý giữa $0 và $1 lớn gấp 100 lần khoảng cách giữa $1 và $1.000.", "surface": "Chỉ có dịch vụ $3.000 và không có sản phẩm nào cho người mới làm quen.", "nature": "Một khi khách hàng đã rút thẻ quẹt dù chỉ $7, họ đã chính thức bước qua lằn ranh trở thành người mua hàng.", "leverage": "Bán bộ template kịch bản hoặc kho dữ liệu độc quyền với giá $27 ở cuối video.", "mantra": "Bước đầu gật nhẹ một lần — Về sau tin cậy muôn phần mở mua"},
            {"num": 6, "meta": "EMAIL LAUNCH CAMPAIGN", "title": "Nghệ thuật mở bán theo chiến dịch 5 ngày", "ground_truth": "Doanh thu của cả năm thường được quyết định bởi 2–3 đợt mở bán chiến dịch lớn (Launches).", "surface": "Lúc nào cũng treo bán sản phẩm thụ động không có thời hạn hay áp lực hành động.", "nature": "Con người luôn trì hoãn nếu không có lý do cấp bách để đưa ra quyết định ngay hôm nay.", "leverage": "Tổ chức chiến dịch mở bán 5 ngày mỗi quý với ưu đãi quà tặng giới hạn để kích hoạt hành động.", "mantra": "Năm ngày mở bán rộn ràng — Quà tặng giới hạn bạc vàng sinh sôi"},
            {"num": 7, "meta": "TỰ ĐỘNG HÓA CHUYỂN TIỀN", "title": "Tích hợp cổng thanh toán quốc tế và trong nước mượt mà", "ground_truth": "Khách hàng muốn mua nhưng giao diện thanh toán lỗi sẽ khiến bạn mất trắng 30% doanh số.", "surface": "Bắt khách chuyển khoản thủ công rồi gửi ảnh chụp biên lai chờ duyệt.", "nature": "Mọi ma sát trong khâu thanh toán đều làm gia tăng tỷ lệ bỏ cuộc giữa chừng.", "leverage": "Tích hợp cổng thanh toán tự động cấp quyền truy cập khóa học ngay sau 3 giây quẹt thẻ.", "mantra": "Thanh toán một chạm hanh thông — Tiền vào tài khoản thỏa lòng ước mong"},
            {"num": 8, "meta": "TỰ DO TÀI CHÍNH BỀN VỮNG", "title": "Đầu tư lợi nhuận từ nội dung vào các tài sản sinh lời thực tế", "ground_truth": "Kiếm được nhiều tiền chỉ là bước một; giữ được tiền và bắt tiền đẻ ra tiền mới là bản lĩnh thực sự.", "surface": "Kiếm được tiền từ khóa học liền tiêu xài hoang phí vào đồ hiệu và xe sang.", "nature": "Thói quen sống xa hoa vượt quá thu nhập sẽ biến bạn thành nô lệ của việc kiếm tiền.", "leverage": "Trích 50% lợi nhuận mỗi tháng đầu tư vào bất động sản, chứng khoán chỉ số và tái đầu tư vào hệ thống.", "mantra": "Bạc tiền kiếm được giữ gìn — Đầu tư tài sản tự tin trọn đời"}
        ],
        "environment": {
            "title": "Thiết lập trung tâm điều hành tài chính của Creator",
            "items": [
                ("1. Phần mềm quản trị dòng tiền tự động (Stripe Dashboard & QuickBooks)", "Theo dõi chính xác doanh thu hàng ngày, tỷ lệ gia hạn và chi phí vận hành."),
                ("2. Quy trình trích lập quỹ dự phòng 6 tháng", "Luôn có sẵn quỹ dự phòng bằng tiền mặt để duy trì cuộc sống và doanh nghiệp trong mọi hoàn cảnh."),
                ("3. Bảng mục tiêu tự do tài chính", "Ghi rõ con số dòng tiền thụ động cần đạt được để trang trải toàn bộ chi phí sinh hoạt của gia đình.")
            ],
            "mantra": "Dòng tiền quản trị rạch ròi — Quỹ phòng sẵn có thảnh thơi tháng ngày"
        },
        "emotional": {
            "title": "Tâm thái thịnh vượng và tự do đích thực",
            "items": [
                ("1. Xem tiền bạc là công cụ phụng sự", "Tiền bạc giúp bạn mở rộng tầm ảnh hưởng, giúp đỡ nhiều người hơn và chăm sóc gia đình chu đáo hơn."),
                ("2. Không rơi vào cái bẫy so sánh giàu có", "Hạnh phúc đích thực là biết đủ và sống cuộc đời tự do theo đúng những giá trị cốt lõi của mình."),
                ("3. Giữ trọn sự hào sảng và phóng khoáng", "Sẵn sàng chia sẻ và giúp đỡ những người có hoàn cảnh khó khăn với tấm lòng rộng mở.")
            ],
            "mantra": "Tâm lành tích đức sâu dày — Tự do tài chính tháng ngày an nhiên"
        }
    }
]

BATCH_2.extend(eps)

with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch2.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
"""
episodes_batch2.py
Batch 2: 10 Episodes (OE11 - OE20)
"""

BATCH_2 = ''' + json.dumps(BATCH_2, ensure_ascii=False, indent=4) + '\n')

print(f"Hoàn tất 100% episodes_batch2.py với đầy đủ {len(BATCH_2)} tập!")
