# -*- coding: utf-8 -*-
"""
add_oe23_30.py: Hoàn thành OE23 - OE30 cho episodes_batch3.py
"""
import json
import sys
sys.path.append('/Users/vietmac/Documents/CODE/k/omar_builder')
from episodes_batch3 import BATCH_3

with open('/Users/vietmac/.gemini/antigravity/brain/24deb8b1-3156-43d0-91a1-3246f0cc4078/scratch/omar_40_videos.json') as f:
    raw_vids = {v['idx']: v for v in json.load(f)}

eps = [
    # 23. Jasmine Star (5akJgNp8OlM)
    {
        "id": raw_vids[23]['id'],
        "slug": "jasmine-star-build-brand-automate-trust-podcast.html",
        "ep_code": "OE23",
        "cat_badge": "02 / THƯƠNG HIỆU CÁ NHÂN & VỊ THẾ DẪN ĐẦU",
        "speaker": "Jasmine Star & Omar Eltakrori",
        "speaker_role": "Nữ hoàng Tiếp thị Mạng xã hội, CEO Social Curator & Diễn giả Quốc tế",
        "tagline": "XÂY DỰNG THƯƠNG HIỆU THAY VÌ CHỈ LÀM KINH DOANH: TỰ ĐỘNG HÓA LÒNG TIN",
        "orig_title": raw_vids[23]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[23]['id']}",
        "publish_date": raw_vids[23]['date'],
        "raw_date": f"{raw_vids[23]['raw_date'][:4]}-{raw_vids[23]['raw_date'][4:6]}-{raw_vids[23]['raw_date'][6:]}",
        "duration": "1 giờ 32 phút",
        "read_time": "~9 phút chắt lọc",
        "hero_quote": "Kinh doanh bán một lần thôi — Thương hiệu gắn kết trọn đời niềm tin",
        "lead_points": [
            "Sự khác biệt giữa một doanh nghiệp bình thường và một thương hiệu biểu tượng: Doanh nghiệp cạnh tranh bằng tính năng và giá cả; thương hiệu sở hữu cảm xúc và tự động hóa lòng tin của khách hàng.",
            "Jasmine Star chia sẻ công thức 'Câu chuyện nguồn gốc' (Origin Story) và nghệ thuật xây dựng cộng đồng gắn bó keo sơn trên mạng xã hội bằng sự thấu hiểu phụ nữ và doanh nhân khởi nghiệp."
        ],
        "hero_summary": {
            "title": "Bản đồ tự động hóa lòng tin và nâng tầm thương hiệu",
            "items": [
                ("1. Từ chức năng sang cảm xúc", "Khách hàng không mua chiếc máy ảnh; họ mua những kỷ niệm gia đình thiêng liêng được lưu giữ mãi mãi."),
                ("2. Tự động hóa sự nhất quán (Consistency)", "Xuất hiện đều đặn mỗi ngày như một người bạn thân thiết, tạo thói quen theo dõi tự nhiên trong tiềm thức khán giả."),
                ("3. Quyền năng của sự dễ bị tổn thương (Vulnerability)", "Dám chia sẻ những nỗi sợ hãi ban đầu để tạo ra sự đồng cảm và lòng trung thành trọn đời.")
            ],
            "mantra": "Bán cảm xúc ấm cõi lòng — Tự động gắn kết vẹn dòng yêu thương"
        },
        "delusion": {
            "title": "ẢO TƯỞNG CẠNH TRANH TÍNH NĂNG & BẢN CHẤT LÒNG TRUNG THÀNH",
            "desc": "Nhiều người nghĩ chỉ cần liệt kê tính năng sản phẩm vượt trội là khách sẽ mua. Nhưng nếu không có sợi dây liên kết cảm xúc thương hiệu, đối thủ chỉ cần giảm giá 5% là khách hàng lập tức quay lưng.",
            "compare_left": {
                "badge": "LỐI MÒN CƠ BẮP",
                "title": "Chỉ tập trung quảng cáo tính năng kỹ thuật",
                "text": "Bảng so sánh thông số khô khan khiến sản phẩm bị xếp vào hàng hóa tiêu dùng đại trà (Commodity)."
            },
            "compare_right": {
                "badge": "ĐẲNG CẤP THƯƠNG HIỆU",
                "title": "Xây dựng câu chuyện và phong cách sống",
                "text": "Biến sản phẩm thành biểu tượng của sự tự do, sáng tạo và bản lĩnh cá nhân mà khách hàng tự hào sở hữu."
            },
            "matrix_title": "So sánh Doanh nghiệp bán hàng và Thương hiệu cảm xúc",
            "matrix_items": [
                ("Doanh nghiệp thuần bán hàng", "• Khách hàng so đo từng đồng, tỷ lệ rời bỏ cao.<br>• Phụ thuộc nặng vào quảng cáo giảm giá để duy trì doanh số."),
                ("Thương hiệu biểu tượng", "• Khách hàng tự hào giới thiệu cho bạn bè và người thân.<br>• Miễn nhiễm hoàn toàn với các cuộc chiến tranh giá rẻ trên thị trường.")
            ],
            "mantra": "Tính năng khô cứng người rời — Thương hiệu cảm xúc trọn đời vấn vương"
        },
        "insights": [
            {"num": 1, "meta": "CÂU CHUYỆN NGUỒN GỐC", "title": "Sức mạnh của Origin Story trong việc xây dựng lòng tin", "ground_truth": "Mọi người nhớ câu chuyện bạn đã vượt qua nghịch cảnh như thế nào sâu sắc hơn bất kỳ bản lý lịch chuyên môn nào.", "surface": "Khoe khoang những thành tích và bằng khen học thuật bóng bẩy.", "nature": "Điểm xuất phát khiêm tốn và những vấp ngã ban đầu là chiếc cầu nối tạo ra sự đồng cảm của công chúng.", "leverage": "Kể câu chuyện ngày đầu tiên khởi nghiệp từ hai bàn tay trắng và bài học xương máu đầu đời.", "mantra": "Chuyện xưa gian khó buổi đầu — Kể ra mộc mạc bắc cầu ân giao"},
            {"num": 2, "meta": "TỰ ĐỘNG HÓA LÒNG TIN", "title": "Sự xuất hiện nhất quán quan trọng hơn sự bùng nổ thất thường", "ground_truth": "Một bài đăng mỗi ngày trong 1 năm xây dựng niềm tin mạnh mẽ hơn 1 chiến dịch rầm rộ rồi biến mất 6 tháng.", "surface": "Đăng bài ồ ạt trong 1 tuần rồi lặn mất tăm vì bận rộn việc khác.", "nature": "Sự biến mất thất thường phát ra tín hiệu của sự thiếu cam kết và thiếu chuyên nghiệp.", "leverage": "Lên lịch nội dung tự động trước 30 ngày để luôn duy trì sự hiện diện đều đặn trên các nền tảng.", "mantra": "Mưa dầm thấm đất từng ngày — Đều đặn xuất hiện dựng xây cơ đồ"},
            {"num": 3, "meta": "NGHỆ THUẬT KỂ CHUYỆN MẠNG XÃ HỘI", "title": "Quy tắc 3 khối nội dung mạng xã hội", "ground_truth": "Nếu bạn chỉ đăng ảnh sản phẩm, tài khoản mạng xã hội của bạn sẽ biến thành catalogue quảng cáo rác.", "surface": "Chụp ảnh sản phẩm và ghi giá bán trong mọi bài đăng.", "nature": "Mạng xã hội là nơi người ta tìm kiếm sự giải trí, học hỏi và kết nối con người.", "leverage": "Chia tỷ lệ: 1/3 chuyên môn hữu ích, 1/3 câu chuyện đời thường chân thật và 1/3 lời kêu gọi hành động.", "mantra": "Ba phần phân bổ rạch ròi — Khách theo dõi mãi sáng ngời niềm vui"},
            {"num": 4, "meta": "XÂY DỰNG BỘ TỘC (TRIBE)", "title": "Tạo ra ngôn ngữ và thuật ngữ độc quyền cho cộng đồng", "ground_truth": "Những cộng đồng mạnh nhất luôn có những từ ngữ và khẩu hiệu riêng mà chỉ thành viên mới hiểu.", "surface": "Dùng những từ ngữ đại trà không có tính nhận diện bộ tộc.", "nature": "Cảm giác thuộc về (Sense of Belonging) được gia cố mạnh mẽ khi cùng nhau chia sẻ một bộ mật mã văn hóa.", "leverage": "Đặt tên cho nhóm khán giả của bạn và sáng tạo các khẩu hiệu hành động truyền cảm hứng.", "mantra": "Ngôn từ riêng biệt chung lòng — Bộ tộc gắn kết một dòng đồng thanh"},
            {"num": 5, "meta": "ĐÓN NHẬN NỖI SỢ HÃI", "title": "Dũng cảm thừa nhận những ngày tồi tệ nhất", "ground_truth": "Không ai có thể sống hoàn hảo 365 ngày mỗi năm; việc che giấu sự kiệt sức chỉ tạo ra sự giả tạo.", "surface": "Luôn luôn phải tỏ ra tích cực độc hại (Toxic Positivity) trên mạng xã hội.", "nature": "Sự dũng cảm chia sẻ những ngày năng lượng thấp giúp bạn trở nên gần gũi và chân thật như một con người thực sự.", "leverage": "Chia sẻ cách bạn vượt qua một ngày tồi tệ và bài học phục hồi năng lượng.", "mantra": "Buồn vui chia sẻ chân thành — Người thương thấu hiểu ngọt lành bên nhau"},
            {"num": 6, "meta": "SỨC MẠNH CỦA VIDEO DỌC", "title": "Tận dụng Reels và Shorts để tiếp cận hàng triệu người lạ", "ground_truth": "Video ngắn dọc là công cụ tiếp cận người dùng mới rẻ nhất và nhanh nhất trong lịch sử internet.", "surface": "Bỏ qua video ngắn vì nghĩ nó chỉ dành cho giới trẻ nhảy múa.", "nature": "Thuật toán video ngắn ưu tiên đề xuất cho người chưa từng biết bạn dựa trên sở thích của họ.", "leverage": "Cắt các đoạn chia sẻ triết lý 30–60 giây từ podcast dài đưa lên Reels và TikTok mỗi ngày.", "mantra": "Video ngắn dọc mở đường — Hút triệu người lạ muôn phương tìm về"},
            {"num": 7, "meta": "CHĂM SÓC TIN NHẮN TRỰC TIẾP", "title": "Hộp thư DM là nơi các hợp đồng lớn nhất được ký kết", "ground_truth": "Bình luận là công khai, nhưng quyết định chi tiền luôn diễn ra trong không gian riêng tư của tin nhắn.", "surface": "Để mặc tin nhắn của khán giả cho bot trả lời tự động một cách vô hồn.", "nature": "Khách hàng cảm động sâu sắc khi nhận được tin nhắn thoại (Voice Note) trả lời từ chính chuyên gia.", "leverage": "Dành 20 phút mỗi ngày gửi tin nhắn thoại ngắn trả lời trực tiếp thắc mắc của những người theo dõi tích cực.", "mantra": "Tin nhắn gửi gắm lời vàng — Khách thương tin cậy nhẹ nhàng chốt sale"},
            {"num": 8, "meta": "BẢO VỆ DANH TIẾNG TRỌN ĐỜI", "title": "Thương hiệu là những gì người ta nói về bạn khi bạn rời khỏi phòng", "ground_truth": "Uy tín của bạn không nằm trên các bài tự khen; nó nằm trong miệng của khách hàng cũ nói với bạn bè của họ.", "surface": "Chỉ quan tâm đến những lời khen công khai trên mạng.", "nature": "Lời truyền miệng âm thầm trong các hội nhóm kín quyết định sự sống còn của doanh nghiệp bạn.", "leverage": "Luôn phục vụ vượt quá sự mong đợi của khách hàng (Overdeliver) để họ tự hào đi giới thiệu bạn.", "mantra": "Rời phòng tiếng tốt vẫn vang — Khách khen nức nở vẻ vang cơ đồ"}
        ],
        "environment": {
            "title": "Thiết lập studio ấm áp phong cách sống hiện đại",
            "items": [
                ("1. Góc quay sofa ấm cúng với cây xanh và gối tựa", "Tạo cảm giác thân mật như một cuộc trò chuyện giữa hai người bạn thân bên phòng khách."),
                ("2. Ánh sáng vàng ấm (Warm Light 3200K - 4000K)", "Mang lại cảm giác an toàn, thư thái và làm tôn lên vẻ đẹp tự nhiên của làn da."),
                ("3. Bảng kế hoạch nội dung trực quan bằng giấy dán (Sticky Notes)", "Dán các mẩu giấy màu lên tường kính để phân loại chủ đề bài đăng theo tuần.")
            ],
            "mantra": "Sofa ấm áp hoa tươi — Ánh vàng dịu mát nụ cười thân thương"
        },
        "emotional": {
            "title": "Tâm thế của người phụng sự bằng tình yêu thương",
            "items": [
                ("1. Yêu thương khán giả như những người bạn tri kỷ", "Mỗi dòng trạng thái viết ra đều mang tâm nguyện nâng đỡ và tiếp thêm sức mạnh cho người đọc."),
                ("2. Giữ sự kiên cường trước sóng gió cuộc đời", "Xem mọi thử thách là chất liệu quý giá giúp hoàn thiện bức tranh cuộc đời rực rỡ."),
                ("3. Tận hưởng từng khoảnh khắc hiện tại", "Không để những lo toan tương lai đánh cắp đi niềm hạnh phúc giản dị của ngày hôm nay.")
            ],
            "mantra": "Gửi trao tất cả yêu thương — Tâm hồn khoáng đạt muôn phương an lành"
        }
    },

    # 24. Film Everything (HiMJY0H9Dxs)
    {
        "id": raw_vids[24]['id'],
        "slug": "personal-brand-blueprint-film-everything-podcast.html",
        "ep_code": "OE24",
        "cat_badge": "02 / THƯƠNG HIỆU CÁ NHÂN & VỊ THẾ DẪN ĐẦU",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "KHUNG KIẾN TRÚC THƯƠNG HIỆU CÁ NHÂN 2026: QUY TRÌNH TƯ LIỆU HÓA MỌI TRẢI NGHIỆM",
        "orig_title": raw_vids[24]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[24]['id']}",
        "publish_date": raw_vids[24]['date'],
        "raw_date": f"{raw_vids[24]['raw_date'][:4]}-{raw_vids[24]['raw_date'][4:6]}-{raw_vids[24]['raw_date'][6:]}",
        "duration": "1 giờ 02 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Quay lại mọi bước đường đi — Mai sau nhìn lại ngại gì phong ba",
        "lead_points": [
            "Chiến lược xây dựng thương hiệu cá nhân đột phá nhất cho doanh nhân: Bật máy quay ghi lại mọi khoảnh khắc làm việc, đàm phán, thất bại và chiến thắng (Film Everything) để xây dựng kho tư liệu số khổng lồ.",
            "Phân tích cách biến 1 ngày làm việc bình thường thành 5 video giá trị cao: Không diễn xuất, không kịch bản giả tạo, chỉ có nhịp sống chân thực của một người đang nỗ lực kiến tạo doanh nghiệp."
        ],
        "hero_summary": {
            "title": "Hệ thống vận hành tư liệu hóa cuộc đời doanh nhân",
            "items": [
                ("1. Máy quay luôn ở chế độ sẵn sàng", "Đặt máy ảnh góc rộng tĩnh trong phòng làm việc để tự động ghi lại toàn bộ tiến trình công việc mỗi ngày."),
                ("2. Phân loại tư liệu theo thẻ nhớ", "Tạo thư mục B-roll phân loại theo cảm xúc: Tập trung, Đàm phán, Thất bại, Vinh quang để làm chất liệu dựng sau này."),
                ("3. Lời bình sâu sắc (Voice-over)", "Lồng tiếng chia sẻ những bài học triết lý đằng sau những thước phim đời thực mộc mạc.")
            ],
            "mantra": "Ghi hình từng bước gian nan — Sau này nhìn lại muôn vàn tự hào"
        },
        "delusion": {
            "title": "ẢO TƯỞNG ĐỜI MÌNH NHÀM CHÁN & SỰ THẬT VỀ SỨC HÚT ĐỜI THƯỜNG",
            "desc": "Nhiều người nghĩ chỉ có các ngôi sao Hollywood mới có cuộc sống đáng xem. Thực tế, khán giả mê mẩn những thước phim chân thật về một người bình thường đang vật lộn khởi nghiệp và từng bước vươn lên.",
            "compare_left": {
                "badge": "TỰ TI NỘI TÂM",
                "title": "Nghĩ rằng công việc của mình quá nhàm chán",
                "text": "Không dám quay hình vì thấy mình chỉ ngồi gõ máy tính và nghe điện thoại cả ngày."
            },
            "compare_right": {
                "badge": "TƯ DUY ĐIỆN ẢNH",
                "title": "Mọi khoảnh khắc đều có tính điện ảnh nếu biết góc quay",
                "text": "Ánh sáng đẹp, âm thanh chân thực và lời bình sâu sắc biến một buổi làm việc bình thường thành một tác phẩm nghệ thuật truyền cảm hứng."
            },
            "matrix_title": "So sánh Cuộc sống bị giấu kín và Cuộc đời được tư liệu hóa",
            "matrix_items": [
                ("Cuộc sống bị giấu kín", "• Mọi nỗ lực và mồ hôi của bạn trôi vào quên lãng không ai biết đến.<br>• Mất đi tài sản truyền thông đắt giá nhất của đời người."),
                ("Cuộc đời được tư liệu hóa", "• Tạo dựng kho tư liệu vô giá chứng minh quá trình trưởng thành bền bỉ.<br>• Khán giả trở thành những người đồng hành trung thành chứng kiến sự vươn lên.")
            ],
            "mantra": "Ghi lại nỗ lực tháng ngày — Thành trang sử quý đong đầy tự hào"
        },
        "insights": [
            {"num": 1, "meta": "BẢN CHẤT TƯ LIỆU", "title": "Giá trị của thước phim tăng theo thời gian như rượu quý", "ground_truth": "Đoạn video bạn quay trong căn phòng trọ chật hẹp hôm nay sẽ là thước phim triệu view đắt giá nhất sau 5 năm nữa.", "surface": "Đợi đến khi có văn phòng đẹp mới chịu bật máy quay.", "nature": "Khán giả khao khát được chứng kiến những ngày đầu tiên đầy khó khăn và sự kiên cường vươn lên từ bùn lầy.", "leverage": "Quay lại toàn bộ bối cảnh khởi đầu khó khăn hiện tại mà không cần giấu giếm bất kỳ điều gì.", "mantra": "Phòng trọ gian khó hôm nay — Mai sau triệu bạc sáng say lòng người"},
            {"num": 2, "meta": "THIẾT LẬP CAMERA TĨNH", "title": "Góc máy thứ ba (Third-Person Perspective)", "ground_truth": "Đặt camera ở một góc phòng và quên đi sự tồn tại của nó sẽ mang lại những thước phim tự nhiên nhất.", "surface": "Luôn nhìn chằm chằm vào ống kính và cố tỏ ra nghiêm túc.", "nature": "Hành vi tự nhiên khi tập trung làm việc toát lên năng lượng chuyên nghiệp và sự tận tụy đáng kính.", "leverage": "Bật máy quay góc tĩnh bên cạnh bàn làm việc và làm việc bình thường suốt 2 tiếng.", "mantra": "Quên đi máy ảnh bên mình — Chăm lo công việc tự nhiên sáng ngời"},
            {"num": 3, "meta": "KHO B-ROLL ĐỘC QUYỀN", "title": "Xây dựng ngân hàng hình ảnh cá nhân độc bản", "ground_truth": "Dùng video B-roll có sẵn trên mạng khiến video của bạn trông rẻ tiền và vô hồn.", "surface": "Tải các video stock miễn phí trên Pexels chèn vào bài nói chuyện.", "nature": "Khán giả muốn nhìn thấy chính bạn đang pha cà phê, đang suy tư, đang viết sổ tay hay đang chỉ đạo đội ngũ.", "leverage": "Dành 1 buổi chiều quay 50 cảnh B-roll đời thực của bản thân để dùng dần cho cả năm.", "mantra": "Hình ảnh độc bản của mình — Chèn vào video lung linh sắc màu"},
            {"num": 4, "meta": "TIẾNG ĐỘNG ĐỜI THỰC (FOLEY)", "title": "Âm thanh môi trường chân thực kích thích thính giác (ASMR)", "ground_truth": "Tiếng gõ phím lách cách, tiếng rót nước sôi, tiếng lật trang sách tạo ra cảm giác chân thực tuyệt đối.", "surface": "Chèn nhạc nền ồn ào át hết mọi âm thanh đời thực.", "nature": "Âm thanh chân thật giúp não bộ người xem hòa mình vào không gian làm việc của bạn.", "leverage": "Thu âm tiếng động môi trường tự nhiên và giữ mức âm lượng vừa phải trong khâu hòa âm.", "mantra": "Tiếng gõ lách cách thân quen — Người xem như ở kề bên chuyện trò"},
            {"num": 5, "meta": "LỜI BÌNH CHIÊM NGHIỆM", "title": "Kỹ thuật lồng tiếng Voice-over chiêm nghiệm sâu sắc", "ground_truth": "Hình ảnh đời thực kết hợp với lời bình triết lý tạo nên chiều sâu cảm xúc lay động lòng người.", "surface": "Chỉ quay hình ảnh mà không có lời giải thích ý nghĩa đằng sau.", "nature": "Lời bình phản tư giúp nâng tầm một hành động bình thường thành một bài học nhân sinh đắt giá.", "leverage": "Thu âm lời bình sau khi đã dựng xong khung hình, nói bằng giọng trầm ấm từ tốn.", "mantra": "Hình ảnh kết hợp lời bình — Đi sâu vào dạ lung linh sáng ngời"},
            {"num": 6, "meta": "GIA ĐÌNH VÀ CỘNG SỰ", "title": "Tôn trọng quyền riêng tư của những người xung quanh", "ground_truth": "Không phải ai cũng muốn xuất hiện trên mạng xã hội như bạn.", "surface": "Chĩa máy quay vào mặt nhân viên hoặc người thân khi chưa được họ đồng ý.", "nature": "Sự xâm phạm đời tư gây ra ức chế và làm rạn nứt các mối quan hệ thiêng liêng.", "leverage": "Luôn hỏi ý kiến và chỉ ghi hình những cộng sự cảm thấy thoải mái trước ống kính.", "mantra": "Tôn trọng riêng tư mọi người — Vui vẻ đồng thuận nụ cười nở hoa"},
            {"num": 7, "meta": "QUY TRÌNH HẬU KỲ TINH GỌN", "title": "Ủy quyền khâu cắt dựng cho biên tập viên chuyên nghiệp", "ground_truth": "Thời gian của bạn nên dành cho việc kinh doanh và tạo tư liệu thô; đừng ngồi cắt từng khung hình cả ngày.", "surface": "Tự mình ngồi mò mẫm cắt ghép video suốt đêm kiệt sức.", "nature": "Chủ doanh nghiệp ngồi dựng video là sự lãng phí tài năng nghiêm trọng.", "leverage": "Tải toàn bộ file thô lên Google Drive và thuê một video editor tài năng dựng theo mẫu chuẩn.", "mantra": "Ghi hình nạp dữ liệu xong — Giao cho thợ dựng thong dong việc nhà"},
            {"num": 8, "meta": "DI SẢN TRUYỀN THỜI", "title": "Một cuốn phim tài liệu vô giá cho con cháu mai sau", "ground_truth": "Tài sản lớn nhất bạn để lại cho thế hệ sau là cuốn nhật ký hình ảnh sống động về cuộc đời cha ông.", "surface": "Chỉ nghĩ đến việc làm video để bán hàng trước mắt.", "nature": "Nhìn thấy hành trình vượt khó của cha mẹ là nguồn động lực và sự giáo dục nhân cách vĩ đại nhất cho con cái.", "leverage": "Lưu trữ toàn bộ kho tư liệu gốc trên các ổ cứng ngoài an toàn để làm di sản gia đình trọn đời.", "mantra": "Cuốn phim di sản mai sau — Cháu con noi dấu tự hào tiến xa"}
        ],
        "environment": {
            "title": "Thiết lập hệ thống lưu trữ dữ liệu an toàn",
            "items": [
                ("1. Hệ thống ổ cứng mạng NAS Synology chạy RAID 1", "Tự động sao lưu toàn bộ video từ điện thoại và máy ảnh ngay khi về nhà, chống mất dữ liệu."),
                ("2. Đầu đọc thẻ nhớ USB-C tốc độ cao", "Chuyển file video 4K sang máy tính chỉ trong vài phút, loại bỏ thời gian chờ đợi lãng phí."),
                ("3. Kẹp điện thoại MagSafe gắn bàn làm việc", "Đặt điện thoại vào vị trí quay cố định chỉ bằng 1 thao tác gắn nam châm tiện lợi.")
            ],
            "mantra": "Dữ liệu sao lưu chu toàn — Ổ cứng sẵn sàng bảo toàn tương lai"
        },
        "emotional": {
            "title": "Tâm thế người làm phim về chính cuộc đời mình",
            "items": [
                ("1. Xem mình là nhân vật chính trong bộ phim cuộc đời", "Mỗi thử thách, khó khăn chỉ là khúc cua kịch tính giúp nhân vật trưởng thành và mạnh mẽ hơn."),
                ("2. Không diễn kịch, không giả vờ", "Giữ trọn vẹn sự trung thực mộc mạc; sự chân thành là thứ ánh sáng lấp lánh nhất."),
                ("3. Trân trọng từng phút giây đang sống", "Hạnh phúc nằm trên từng bước chân của cuộc hành trình, không phải ở đích đến xa xôi.")
            ],
            "mantra": "Nhân vật chính của đời ta — Đi qua bão táp nở hoa kiên cường"
        }
    }
]

BATCH_3.extend(eps)

# Cập nhật episodes_batch3.py
with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch3.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
"""
episodes_batch3.py
Batch 3: Episodes (OE21 - OE30)
"""

BATCH_3 = ''' + json.dumps(BATCH_3, ensure_ascii=False, indent=4) + '\n')

print(f"Hoàn thành cập nhật episodes_batch3.py với {len(BATCH_3)} tập (OE21 - OE24)!")
