# -*- coding: utf-8 -*-
"""
make_batch1.py: Hoàn thiện episodes_batch1.py với 10 tập đầy đủ OE01 - OE10
"""
import json

with open('/Users/vietmac/.gemini/antigravity/brain/24deb8b1-3156-43d0-91a1-3246f0cc4078/scratch/omar_40_videos.json') as f:
    raw_vids = {v['idx']: v for v in json.load(f)}

# Nạp OE01 - OE04 từ episodes_batch1.py hiện tại
import sys
sys.path.append('/Users/vietmac/Documents/CODE/k/omar_builder')
from episodes_batch1 import BATCH_1

# Thêm OE05 - OE10
batch1_remaining = [
    # 05. $10M CEO (Nu5lRv9d8nk)
    {
        "id": raw_vids[5]['id'],
        "slug": "10m-ceo-why-ceos-need-personal-brand-podcast.html",
        "ep_code": "OE05",
        "cat_badge": "02 / THƯƠNG HIỆU CÁ NHÂN & VỊ THẾ DẪN ĐẦU",
        "speaker": "Omar Eltakrori & Khách mời CEO 10M USD",
        "speaker_role": "Nhà sáng lập Tập đoàn Đa ngành & Cố vấn Chiến lược Doanh nghiệp",
        "tagline": "TẠI SAO MỌI CEO ĐỀU BẮT BUỘC PHẢI CÓ THƯƠNG HIỆU CÁ NHÂN",
        "orig_title": raw_vids[5]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[5]['id']}",
        "publish_date": raw_vids[5]['date'],
        "raw_date": f"{raw_vids[5]['raw_date'][:4]}-{raw_vids[5]['raw_date'][4:6]}-{raw_vids[5]['raw_date'][6:]}",
        "duration": "1 giờ 12 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Doanh nghiệp biển hiệu xa xôi — Con người đứng mũi sáng soi cơ đồ",
        "lead_points": [
            "Khách hàng thời đại số không còn tin vào các thông cáo báo chí vô hồn của công ty; họ đưa ra quyết định mua hàng vì tin tưởng vào khuôn mặt, giá trị sống và uy tín của người đứng đầu.",
            "Phân tích chiến lược biến CEO thành kênh truyền thông mạnh nhất của doanh nghiệp, giúp giảm chi phí quảng cáo về 0 và thu hút nhân tài xuất sắc nhất."
        ],
        "hero_summary": {
            "title": "Bản đồ đòn bẩy thương hiệu lãnh đạo cho doanh nghiệp",
            "items": [
                ("1. Vũ khí giảm chi phí thu hút khách (CAC)", "Thương hiệu cá nhân của CEO biến doanh nghiệp thành thỏi nam châm hút khách hàng tự nhiên mà không tốn tiền chạy ads."),
                ("2. Nam châm thu hút nhân sự xuất sắc", "Nhân tài hàng đầu muốn cống hiến cho một nhà lãnh đạo có tầm nhìn và triết lý sống rõ ràng, không phải một pháp nhân vô cảm."),
                ("3. Khiên chắn bảo vệ khi xảy ra khủng hoảng", "Lòng tin được tích lũy vào con người thật sẽ giúp doanh nghiệp vượt qua mọi sóng gió truyền thông thị trường.")
            ],
            "mantra": "Thủ lĩnh đứng mũi chịu sào — Uy danh tỏa sáng đón chào nhân tài"
        },
        "delusion": {
            "title": "ẢO TƯỞNG ẨN MÌNH SAU DOANH NGHIỆP & SỰ THẬT VỀ QUYỀN LỰC TRUYỀN THÔNG",
            "desc": "Nhiều chủ doanh nghiệp nghĩ rằng chỉ cần tập trung làm sản phẩm tốt và đứng sau cánh gà là đủ. Nhưng trong thế giới phân mảnh chú ý, người vô danh sẽ bị kẻ biết làm truyền thông vượt mặt.",
            "compare_left": {
                "badge": "ẢO TƯỞNG CŨ",
                "title": "CEO chỉ nên làm việc nội bộ trong phòng họp",
                "text": "Né tránh xuất hiện trên mạng xã hội vì sợ bị đánh giá là khoe mẽ hoặc làm phiền cuộc sống riêng tư."
            },
            "compare_right": {
                "badge": "SỰ THẬT HIỆN ĐẠI",
                "title": "CEO là đại sứ thương hiệu số 1 của tổ chức",
                "text": "Chủ động chia sẻ bài học quản trị, góc nhìn ngành và văn hóa công ty để định hình luật chơi trong tâm trí khách hàng."
            },
            "matrix_title": "Đối chiếu Doanh nghiệp có CEO làm thương hiệu và Doanh nghiệp ẩn danh",
            "matrix_items": [
                ("Doanh nghiệp ẩn danh", "• Chi phí quảng cáo tăng dần theo năm, phụ thuộc hoàn toàn vào các thuật toán nền tảng.<br>• Nhân tài xem đây chỉ là nơi làm thuê tạm thời."),
                ("Doanh nghiệp có CEO thương hiệu mạnh", "• Khách hàng tự tìm đến qua video, chu kỳ bán hàng rút ngắn 70%.<br>• Nhà đầu tư và đối tác lớn chủ động ngỏ lời hợp tác chiến lược.")
            ],
            "mantra": "Ẩn mình chịu cảnh lép vế — Xuất đầu lộ diện mở lối vinh quang"
        },
        "insights": [
            {"num": 1, "meta": "BẢN CHẤT LÒNG TIN", "title": "Con người mua từ con người, không mua từ logo", "ground_truth": "Mọi khảo sát người tiêu dùng đều chỉ ra sự suy giảm niềm tin vào các thương hiệu tập đoàn vô danh.", "surface": "Chi tiền tỷ làm bộ nhận diện thương hiệu công ty thật hoành tráng.", "nature": "Hệ thần kinh gương (Mirror Neurons) của con người chỉ rung động trước ánh mắt và cảm xúc của một con người thật.", "leverage": "Đặt khuôn mặt của CEO vào các video giải thích giải pháp cốt lõi của công ty.", "mantra": "Logo dẫu đẹp muôn phần — Sao bằng ánh mắt ân cần trao tin"},
            {"num": 2, "meta": "THU HÚT NHÂN TÀI", "title": "Chiêu mộ người giỏi bằng tầm nhìn công khai", "ground_truth": "Những chuyên gia hàng đầu luôn tìm kiếm lãnh đạo truyền cảm hứng để theo học hỏi.", "surface": "Đăng tin tuyển dụng truyền thống trên các website việc làm với mô tả khô khan.", "nature": "Người giỏi chỉ muốn đi theo người giỏi hơn họ hoặc người có lý tưởng vĩ đại.", "leverage": "Chia sẻ những trăn trở và tiêu chuẩn đạo đức của công ty qua các video dài trên YouTube.", "mantra": "Tầm nhìn rạng rỡ bay xa — Nhân tài bốn bể một nhà chung tay"},
            {"num": 3, "meta": "ĐỊNH HÌNH THỊ TRƯỜNG", "title": "Trở thành người phát ngôn của toàn ngành", "ground_truth": "Ai lên tiếng trước và định nghĩa vấn đề của ngành, người đó nắm quyền định giá.", "surface": "Lặng lẽ chạy theo sau các xu hướng do đối thủ khởi xướng.", "nature": "Thị trường luôn tôn vinh kẻ dũng cảm lên tiếng chỉ ra những bất cập của phương pháp cũ.", "leverage": "Làm chuỗi video 'Sự thật trần trụi về ngành [Tên ngành]' để tái định vị toàn bộ tiêu chuẩn.", "mantra": "Dẫn đầu cất tiếng tiên phong — Định hình chuẩn mực giữa dòng phong ba"},
            {"num": 4, "meta": "GIẢM PHÍ ADS", "title": "Biến nội dung cá nhân thành phễu bán hàng triệu USD", "ground_truth": "Tỷ lệ chuyển đổi từ traffic tự nhiên của CEO cao gấp 5 lần traffic từ Facebook Ads.", "surface": "Bơm tiền chạy quảng cáo rầm rộ cho các trang landing page bán hàng lạnh.", "nature": "Khách hàng đã xem CEO nói chuyện suốt 20 phút không còn coi đây là người lạ bán hàng nữa.", "leverage": "Chèn lời kêu gọi hành động tinh tế ở cuối video dẫn về form tư vấn giải pháp doanh nghiệp.", "mantra": "Video nói chuyện chân tình — Hút ngàn đơn bạc chẳng cần chi ads"},
            {"num": 5, "meta": "BẢO VỆ KHỦNG HOẢNG", "title": "Uy tín cá nhân là lá chắn thép trước biến cố", "ground_truth": "Khi công ty gặp sự cố kỹ thuật, nếu CEO chân thành nhận lỗi, khách hàng sẵn sàng tha thứ.", "surface": "Trốn tránh trách nhiệm và đổ lỗi cho cấp dưới hoặc gửi thông cáo báo chí né tránh.", "nature": "Sự dũng cảm đối diện và nhận lỗi công khai biến khủng hoảng thành cơ hội củng cố niềm tin.", "leverage": "Quay video mộc mạc giải thích rõ nguyên nhân sự cố và cam kết bồi thường thỏa đáng.", "mantra": "Chân thành nhận lỗi thẳng ngay — Khách thương tha thứ chung tay đồng lòng"},
            {"num": 6, "meta": "ĐÒN BẨY ĐẦU TƯ", "title": "Gọi vốn và hợp tác dễ dàng hơn nhờ sự minh bạch", "ground_truth": "Các quỹ đầu tư rót tiền vào nhà sáng lập trước khi rót tiền vào sản phẩm.", "surface": "Làm slide pitch deck bóng bẩy nhưng hồ sơ cá nhân của CEO trên mạng lại trống trơn.", "nature": "Nhà đầu tư dùng lịch sử nội dung của CEO để đánh giá chỉ số kiên trì và tầm nhìn chiến lược.", "leverage": "Duy trì kho tư liệu video hành trình phát triển doanh nghiệp công khai trên YouTube.", "mantra": "Hành trình sáng tỏ tỏ tường — Quỹ đầu tư tới mở đường rót vốn"},
            {"num": 7, "meta": "TỰ ĐỘNG HÓA QUY TRÌNH", "title": "Tư liệu hóa tri thức CEO thành giáo trình nội bộ", "ground_truth": "CEO thường xuyên phải lặp lại cùng một câu trả lời cho nhân viên và đối tác mới.", "surface": "Họp hành liên miên mỗi ngày để đào tạo từng nhân sự mới vào công ty.", "nature": "Thời gian của CEO là tài sản đắt giá nhất của doanh nghiệp, không được lãng phí vào việc nhắc lại.", "leverage": "Quay lại các bài phân tích sâu một lần và biến chúng thành thư viện tri thức đào tạo trọn đời.", "mantra": "Quay một lần dùng trăm năm — Tri thức tổ chức vững bền tương lai"},
            {"num": 8, "meta": "DI SẢN DOANH NHÂN", "title": "Thương hiệu cá nhân đi theo bạn suốt cuộc đời", "ground_truth": "Công ty có thể bán đi hoặc phá sản, nhưng uy tín cá nhân của bạn sẽ tồn tại vĩnh viễn.", "surface": "Đồng nhất 100% bản sắc cá nhân vào một công ty cụ thể duy nhất.", "nature": "Khi chuyển sang dự án kinh doanh mới, thương hiệu cá nhân giúp bạn bắt đầu ở vạch đích thay vì số 0.", "leverage": "Xây dựng tệp khán giả trung thành gắn chặt với tên riêng của bạn, độc lập với tên công ty.", "mantra": "Công ty có thể đổi dời — Uy danh tên tuổi trọn đời sáng trong"}
        ],
        "environment": {
            "title": "Thiết kế phòng quay tối giản cho CEO bận rộn",
            "items": [
                ("1. Thiết lập 1-chạm (1-Touch Studio)", "Camera, micro và đèn luôn cắm điện sẵn trên tripod cố định; chỉ cần bật một công tắc là bắt đầu quay ngay."),
                ("2. Không gian phản ánh tầm vóc lãnh đạo", "Kệ sách gọn gàng, ánh sáng ấm cúng, bàn làm việc gỗ tự nhiên tạo cảm giác vững chãi và đáng tin cậy."),
                ("3. Teleprompter hiển thị dàn ý ý niệm", "Dùng máy nhắc chữ hiển thị 3 gạch đầu dòng lớn thay vì đọc kịch bản chữ để giữ ánh mắt tự nhiên.")
            ],
            "mantra": "Bật công tắc quay được ngay — Giữ nét lãnh đạo tháng ngày đĩnh đạc"
        },
        "emotional": {
            "title": "Vượt qua nỗi sợ lộ diện của người đứng đầu",
            "items": [
                ("1. Chấp nhận sự phán xét ban đầu", "Hiểu rằng những người bình luận tiêu cực thường là những kẻ chưa từng xây dựng được doanh nghiệp nào."),
                ("2. Tập trung vào sứ mệnh dẫn dắt", "Nói vì sự phát triển của đội ngũ và khách hàng, quên đi cái tôi cá nhân trước ống kính máy quay."),
                ("3. Giữ gìn năng lượng tích cực", "Chỉ đọc các phản hồi mang tính xây dựng, ủy quyền cho trợ lý lọc bỏ các bình luận rác trên mạng.")
            ],
            "mantra": "Tâm vững trước sóng thị phi — Hướng về đích lớn ngại gì gió sương"
        }
    },

    # 06. New Content Gameplan (Yy7slgaEfg4)
    {
        "id": raw_vids[6]['id'],
        "slug": "new-content-gameplan-for-personal-brands-podcast.html",
        "ep_code": "OE06",
        "cat_badge": "02 / THƯƠNG HIỆU CÁ NHÂN & VỊ THẾ DẪN ĐẦU",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "BẢN KẾ HOẠCH NỘI DUNG THẾ HỆ MỚI: XÂY DỰNG VỊ THẾ CÁ NHÂN CHO MỌI NGÀNH",
        "orig_title": raw_vids[6]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[6]['id']}",
        "publish_date": raw_vids[6]['date'],
        "raw_date": f"{raw_vids[6]['raw_date'][:4]}-{raw_vids[6]['raw_date'][4:6]}-{raw_vids[6]['raw_date'][6:]}",
        "duration": "49 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Nội dung chẳng phải ngẫu nhiên — Kế hoạch định sẵn triền miên gặt vàng",
        "lead_points": [
            "Lý do số 1 khiến các nhà sáng tạo kiệt sức là sáng tạo nội dung ngẫu hứng không có hệ thống; hôm nay nghĩ gì đăng nấy khiến kênh bị loãng và mất định vị.",
            "Omar chia sẻ chiến lược '1 Pillar Video -> 10 Micro Assets': Sản xuất 1 video dài chất lượng mỗi tuần rồi phân rã thành Shorts, Reels, bài viết LinkedIn và Email Newsletter."
        ],
        "hero_summary": {
            "title": "Hệ thống phân rã nội dung đa kênh không tốn sức",
            "items": [
                ("1. Video trụ cột (Pillar Content)", "1 video YouTube dài 20–30 phút giải quyết triệt để 1 câu hỏi lớn của thị trường."),
                ("2. Phân tách vi mô (Micro Slicing)", "Trích xuất 3–5 đoạn cao trào 60 giây làm TikTok/Reels để kéo lượng khán giả mới."),
                ("3. Chuyển thể văn bản (Text Repurposing)", "Dùng AI chuyển transcript video thành bài phân tích chuyên sâu cho Newsletter và mạng xã hội.")
            ],
            "mantra": "Một nguồn nước mát trong lành — Rẽ thành trăm nhánh tươi xanh muôn miền"
        },
        "delusion": {
            "title": "ẢO TƯỞNG CÀY CUỐC ĐĂNG BÀI MỖI NGÀY & SỰ THẬT VỀ ĐÒN BẨY HỆ THỐNG",
            "desc": "Nhiều người lầm tưởng rằng làm content là phải cầm điện thoại quay mọi lúc mọi nơi. Cách làm này dẫn tới kiệt sức (Burnout) sau 3 tháng. Người thông minh xây dựng cỗ máy tái sử dụng nội dung thông minh.",
            "compare_left": {
                "badge": "ẢO TƯỞNG CƠ BẮP",
                "title": "Quay riêng lẻ từng video ngắn mỗi ngày",
                "text": "Mỗi ngày thức dậy đều đau đầu tự hỏi 'Hôm nay quay gì?', tốn 4 tiếng chỉ để ra 1 video TikTok 30 giây."
            },
            "compare_right": {
                "badge": "HỆ THỐNG THÔNG MINH",
                "title": "Quay theo mẻ (Batching) 1 lần cho cả tháng",
                "text": "Dành trọn 1 ngày cuối tuần quay 4 video dài chuyên sâu, sau đó giao cho đội ngũ hoặc AI cắt dựng thành 30 nội dung đa nền tảng."
            },
            "matrix_title": "So sánh Sáng tạo thủ công và Vận hành theo mẻ",
            "matrix_items": [
                ("Sáng tạo thủ công ngẫu hứng", "• Chất lượng trồi sụt, thông điệp rời rạc không nhất quán.<br>• Mất năng lượng sáng tạo, luôn cảm thấy tội lỗi khi không đăng bài."),
                ("Quy trình Batching có hệ thống", "• Đầu óc thảnh thơi tập trung kinh doanh cốt lõi.<br>• Nội dung xuất bản đều đặn như đồng hồ Thụy Sĩ.")
            ],
            "mantra": "Quay mẻ một buổi thảnh thơi — Đăng đều cả tháng sáng ngời uy danh"
        },
        "insights": [
            {"num": 1, "meta": "QUY LUẬT TẬP TRUNG", "title": "Sức mạnh của việc quay theo mẻ (Content Batching)", "ground_truth": "Chi phí chuyển đổi bối cảnh (Context Switching) tiêu tốn tới 40% năng suất làm việc của não bộ.", "surface": "Mỗi ngày dựng máy quay, gắn micro, bật đèn rồi lại dọn dẹp.", "nature": "Khi đã vào trạng thái dòng chảy (Flow State), bạn có thể quay 4 video liên tiếp với năng lượng cao gấp đôi.", "leverage": "Khóa lịch 1 ngày duy nhất trong tuần chỉ dành riêng cho việc ghi hình.", "mantra": "Tập trung một mạch thăng hoa — Xong xuôi công việc cả nhà chung vui"},
            {"num": 2, "meta": "CÂU HỎI THỊ TRƯỜNG", "title": "Tìm chủ đề từ những câu hỏi thật của khách hàng", "ground_truth": "Nội dung có lượt xem cao nhất luôn là câu trả lời cho những băn khoăn đau đớn nhất của khách.", "surface": "Cố gắng sáng tạo ra những chủ đề cao siêu mà không ai tìm kiếm.", "nature": "Khán giả chỉ quan tâm đến vấn đề của chính họ; khi thấy vấn đề của mình được giải quyết, họ sẽ bấm xem.", "leverage": "Ghi chép lại mọi câu hỏi khách hàng từng hỏi bạn trong các cuộc tư vấn để làm tiêu đề video.", "mantra": "Khách hỏi điều gì băn khoăn — Trả lời thấu đáo muôn phần lắng nghe"},
            {"num": 3, "meta": "CẤU TRÚC 3 PHẦN", "title": "Khung kịch bản Hook - Story - Offer bất biến", "ground_truth": "80% khán giả quyết định ở lại hay rời đi trong 5 giây đầu tiên của video.", "surface": "Mở đầu video bằng đoạn giới thiệu bản thân dài dòng và logo hoạt họa.", "nature": "Bộ não người lướt mạng có ngưỡng kiên nhẫn cực thấp; bạn phải nêu ngay kết quả họ nhận được trong 3 giây.", "leverage": "Vào thẳng vấn đề ngay giây đầu tiên: 'Trong video này, tôi sẽ chỉ cho bạn cách...'.", "mantra": "Mở đầu giật trúng tâm can — Giữ chân khán giả muôn vàn khắc sâu"},
            {"num": 4, "meta": "ĐA DẠNG HÓA KÊNH", "title": "Một ý tưởng - Ba định dạng truyền thông", "ground_truth": "Mỗi nhóm khách hàng có thói quen tiêu thụ nội dung khác nhau (Xem video, Nghe podcast hoặc Đọc bài).", "surface": "Chỉ làm duy nhất 1 định dạng video ngắn trên TikTok.", "nature": "Bỏ qua định dạng văn bản và âm thanh là bạn đang bỏ rơi 50% thị trường khách hàng tiềm năng.", "leverage": "Biến 1 video thành 1 bài viết dài và 1 tập podcast đưa lên Spotify/Apple Podcasts.", "mantra": "Một cây trổ ba nhánh hoa — Video, chữ viết, bài ca êm đềm"},
            {"num": 5, "meta": "THUẬT TOÁN RETENTION", "title": "Giữ chân người xem bằng nhịp điệu thị giác (Pacing)", "ground_truth": "Thời lượng xem trung bình (AVD) là chỉ số quan trọng nhất quyết định video có được đề xuất hay không.", "surface": "Ngồi một chỗ nói chuyện đều đều không thay đổi góc máy suốt 20 phút.", "nature": "Mắt người sẽ bị mỏi và buồn ngủ nếu khung hình không có sự thay đổi sau mỗi 5–7 giây.", "leverage": "Chèn thêm B-roll minh họa, phóng to/thu nhỏ khung hình (Punch-in) và thêm chữ nhấn mạnh.", "mantra": "Khung hình thay đổi nhịp nhàng — Người xem cuốn hút chẳng màng thời gian"},
            {"num": 6, "meta": "KÊU GỌI HÀNH ĐỘNG", "title": "Một video chỉ có duy nhất một lời kêu gọi hành động (Single CTA)", "ground_truth": "Khi bạn yêu cầu người xem làm 3 việc cùng lúc, họ sẽ không làm bất kỳ việc nào.", "surface": "Kêu gọi like, share, subscribe, bấm chuông, bình luận và click link mua hàng.", "nature": "Nghịch lý quá tải lựa chọn khiến người dùng bị bối rối và thoát ra ngoài.", "leverage": "Chỉ chọn 1 hành động quan trọng nhất cho mỗi video (ví dụ: 'Bấm link ở phần mô tả để nhận tài liệu miễn phí').", "mantra": "Một lời kêu gọi dứt dứt — Khách hàng ghi nhớ nhất tề làm theo"},
            {"num": 7, "meta": "ĐÒN BẨY EMAIL", "title": "Chuyển đổi người xem trên mạng xã hội thành danh sách email", "ground_truth": "Bạn không thực sự sở hữu người theo dõi trên YouTube hay TikTok; nền tảng có thể khóa kênh bất cứ lúc nào.", "surface": "Chỉ đếm số lượng người theo dõi trên kênh và tự mãn.", "nature": "Danh sách email là tài sản kinh doanh duy nhất bạn nắm quyền kiểm soát 100%.", "leverage": "Tặng quà tặng giá trị cao (Lead Magnet) để đổi lấy địa chỉ email của khán giả trung thành.", "mantra": "Kênh mạng chỉ đất thuê thôi — Danh sách email mới ngôi nhà mình"},
            {"num": 8, "meta": "TÁI BẢN NỘI DUNG", "title": "Đừng ngần ngại nhắc lại những thông điệp cốt lõi", "ground_truth": "Khán giả không nhớ hết những gì bạn nói tuần trước; họ cần được nhắc nhở liên tục.", "surface": "Luôn luôn áp lực phải nghĩ ra triết lý mới mẻ chưa ai từng nói.", "nature": "Sự kiên định lặp lại một thông điệp cốt lõi chính là điều tạo nên thương hiệu biểu tượng.", "leverage": "Làm mới lại các video thành công nhất của năm ngoái với góc nhìn và ví dụ của năm nay.", "mantra": "Nhắc lại chân lý ngàn đời — Khắc sâu ghi nhớ rạng ngời niềm tin"}
        ],
        "environment": {
            "title": "Thiết lập trạm sáng tạo nội dung hiệu suất cao",
            "items": [
                ("1. Thẻ nhớ và pin luôn sạc đầy trong hộp", "Tránh tình trạng chuẩn bị quay thì máy báo hết pin, dập tắt ngọn lửa cảm hứng."),
                ("2. Bảng viết dạ trắng để phác thảo sơ đồ ý", "Vẽ cấu trúc luồng ý tưởng lớn lên bảng trước khi bấm máy để bài nói liền mạch."),
                ("3. Không gian cách âm tốt với thảm và rèm", "Trải thảm sàn và kéo rèm dày để triệt tiêu tiếng vọng âm khó chịu.")
            ],
            "mantra": "Pin đầy máy sẵn sàng sàng — Bảng sơ đồ tỏ hiên ngang lên hình"
        },
        "emotional": {
            "title": "Giữ tâm thế kiên định không phụ thuộc vào lượt xem",
            "items": [
                ("1. Không kiểm tra số liệu trong 24 giờ đầu", "Đăng video xong hãy rời khỏi máy tính, không F5 liên tục để xem view tăng hay giảm."),
                ("2. Xem mỗi video là một viên gạch tài sản", "Một video xuất sắc có thể âm thầm mang lại khách hàng cho bạn sau 3 năm nữa."),
                ("3. Tận hưởng quá trình hoàn thiện bản thân", "Mỗi lần đứng trước ống kính là một lần rèn luyện tư duy và khả năng biểu đạt đỉnh cao.")
            ],
            "mantra": "Gieo hạt không ngóng từng giờ — Cây đời lớn dậy bất ngờ nở hoa"
        }
    }
]

BATCH_1.extend(batch1_remaining)

# Ghi lại episodes_batch1.py hoàn chỉnh
with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch1.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
"""
episodes_batch1.py
Batch 1: 10 Episodes (OE01 - OE10)
"""

BATCH_1 = ''' + json.dumps(BATCH_1, ensure_ascii=False, indent=4) + '\n')

print(f"Hoàn thành episodes_batch1.py với {len(BATCH_1)} tập!")
