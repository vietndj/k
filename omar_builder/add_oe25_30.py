# -*- coding: utf-8 -*-
"""
add_oe25_30.py: Hoàn thiện nốt OE25 - OE30 cho episodes_batch3.py
"""
import json
import sys
sys.path.append('/Users/vietmac/Documents/CODE/k/omar_builder')
from episodes_batch3 import BATCH_3

with open('/Users/vietmac/.gemini/antigravity/brain/24deb8b1-3156-43d0-91a1-3246f0cc4078/scratch/omar_40_videos.json') as f:
    raw_vids = {v['idx']: v for v in json.load(f)}

eps = [
    # 25. Use AI To Build 7 Figure (8Ruw4SzZwGQ)
    {
        "id": raw_vids[25]['id'],
        "slug": "use-ai-to-build-7-figure-personal-brand-podcast.html",
        "ep_code": "OE25",
        "cat_badge": "04 / TRÍ TUỆ NHÂN TẠO & ĐỘT PHÁ NĂNG SUẤT",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "TẬN DỤNG AI ĐỂ XÂY DỰNG THƯƠNG HIỆU CÁ NHÂN 7 CON SỐ",
        "orig_title": raw_vids[25]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[25]['id']}",
        "publish_date": raw_vids[25]['date'],
        "raw_date": f"{raw_vids[25]['raw_date'][:4]}-{raw_vids[25]['raw_date'][4:6]}-{raw_vids[25]['raw_date'][6:]}",
        "duration": "58 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Đòn bẩy AI trong bàn tay — Triệu đô thương hiệu tháng ngày nở hoa",
        "lead_points": [
            "Cách các nhà sáng tạo nội dung hàng đầu kết hợp công nghệ AI vào toàn bộ quy trình: Từ nghiên cứu chủ đề viral, viết dàn ý kịch bản, tự động cắt dựng video ngắn đến thiết kế thumbnail chuyển đổi cao.",
            "Phân tích hệ thống kiến trúc AI 5 lớp: Lớp Nghiên cứu dữ liệu -> Lớp Sáng tạo ý niệm -> Lớp Biên tập âm thanh hình ảnh -> Lớp Phân phối đa kênh -> Lớp Chăm sóc khách hàng tự động."
        ],
        "hero_summary": {
            "title": "Hệ thống AI 5 lớp nâng tầm thương hiệu triệu USD",
            "items": [
                ("1. Tăng tốc nghiên cứu gấp 10 lần", "Dùng AI quét hàng ngàn video hàng đầu để tìm ra những khoảng trống nội dung mà chưa ai trả lời thấu đáo."),
                ("2. Giữ vững giọng văn độc bản (Voice DNA)", "Huấn luyện mô hình AI trên các bài viết và bài giảng tốt nhất của bạn để văn phong luôn giữ đúng chất riêng."),
                ("3. Tự động hóa sản xuất video ngắn", "Tự động trích xuất các đoạn cắt cao trào, thêm phụ đề động và tạo hiệu ứng chuyển cảnh chỉ bằng một câu lệnh.")
            ],
            "mantra": "Máy lo việc mọn tinh tường — Người lo chiến lược muôn đường thăng hoa"
        },
        "delusion": {
            "title": "ẢO TƯỞNG PHÓ MẶC CHO AI & SỰ THẬT VỀ LINH HỒN NỘI DUNG",
            "desc": "Nhiều người lười biếng để AI tự viết kịch bản 100% rồi đọc lại như một cái máy. Nội dung như vậy vô cùng nhạt nhẽo và không thể tạo ra bất kỳ cảm xúc nào. AI chỉ là trợ lý; linh hồn và câu chuyện thật phải do chính bạn thổi vào.",
            "compare_left": {
                "badge": "LƯỜI BIẾNG BỀ NỔI",
                "title": "Phó mặc toàn bộ cho AI viết bài",
                "text": "Tạo ra những nội dung sáo rỗng vô hồn khiến khán giả nhận ra ngay và rời bỏ kênh."
            },
            "compare_right": {
                "badge": "LÀM CHỦ CÔNG NGHỆ",
                "title": "Dùng AI làm bệ phóng cho trí tuệ con người",
                "text": "Dùng AI để hoàn thành 70% công việc thô, dành 30% thời gian quý báu chèn thêm cảm xúc, bài học thật và góc nhìn độc bản."
            },
            "matrix_title": "So sánh Nội dung AI đại trà và Nội dung AI có linh hồn con người",
            "matrix_items": [
                ("Nội dung AI 100%", "• Giọng văn chung chung, lặp lại các khuôn mẫu sáo rỗng.<br>• Tỷ lệ thoát trang cao, không ai nhớ tác giả là ai."),
                ("Nội dung kết hợp AI + Con người", "• Tốc độ xuất bản thần tốc nhưng vẫn giữ trọn sự sâu sắc và chạm sâu vào tâm khảm.<br>• Xây dựng thương hiệu triệu đô bền vững.")
            ],
            "mantra": "Máy làm khung sườn vững vàng — Người thổi cảm xúc chứa chan nghĩa tình"
        },
        "insights": [
            {"num": 1, "meta": "TỐC ĐỘ Ý TƯỞNG", "title": "Tìm 50 góc nhìn độc lạ chỉ trong 60 giây bằng AI", "ground_truth": "Bế tắc ý tưởng là dấu hiệu của việc thiếu dữ liệu đầu vào.", "surface": "Ngồi vò đầu bứt tai suy nghĩ cả buổi sáng không ra một ý tưởng hay.", "nature": "AI có thể kết hợp các lĩnh vực hoàn toàn trái ngược nhau để tạo ra những ý tưởng sáng tạo bất ngờ.", "leverage": "Prompt: 'Hãy kết hợp tâm lý học Phật giáo với thuật toán YouTube để đưa ra 10 góc nhìn độc lạ'.", "mantra": "Ý tưởng bừng sáng muôn phương — Kết hợp kim cổ mở đường sáng tạo"},
            {"num": 2, "meta": "DỰNG PHIM SIÊU TỐC", "title": "Cắt bỏ khoảng lặng tự động trong 3 giây", "ground_truth": "Người biên tập video thủ công mất hàng giờ chỉ để bấm phím cắt các đoạn thở dài và từ đệm.", "surface": "Tự tay ngồi kéo chuột cắt từng đoạn im lặng nhỏ trong thanh timeline.", "nature": "Đây là công việc cơ bắp đơn giản mà thuật toán AI có thể xử lý chính xác tuyệt đối trong tích tắc.", "leverage": "Ứng dụng các công cụ AI tự động loại bỏ toàn bộ khoảng lặng và câu nói vấp chỉ với một cú nhấp chuột.", "mantra": "Khoảng lặng cắt gọn tinh thanh — Video trôi chảy ngọt lành êm tai"},
            {"num": 3, "meta": "PHỤ ĐỀ ĐỘNG BẮT MẮT", "title": "Tự động tạo phụ đề động chuẩn xác 99%", "ground_truth": "85% người xem video ngắn trên điện thoại tắt âm thanh và chỉ đọc chữ phụ đề.", "surface": "Tự gõ từng dòng chữ phụ đề hoặc bỏ qua không làm phụ đề.", "nature": "Phụ đề động có đổi màu theo nhịp nói giúp giữ mắt người xem dán chặt vào màn hình điện thoại.", "leverage": "Dùng AI sinh phụ đề tự động, gắn biểu tượng cảm xúc và làm nổi bật các từ khóa quan trọng.", "mantra": "Chữ chạy đổi màu nhịp nhàng — Người xem dán mắt chẳng màng rời xa"},
            {"num": 4, "meta": "THUMBNAIL BẰNG AI", "title": "Tách nền và tạo phông nền điện ảnh bằng Generative Fill", "ground_truth": "Một bức ảnh chân dung tầm thường có thể biến thành poster phim Hollywood nhờ công nghệ AI tạo sinh.", "surface": "Chụp ảnh trong phòng trọ lộn xộn và để nguyên hậu cảnh xấu xí.", "nature": "Phông nền chuyên nghiệp, sang trọng làm tăng vọt giá trị cảm nhận của chuyên gia trong mắt người xem.", "leverage": "Dùng AI xóa phông nền cũ và thay thế bằng studio phong cách tối giản sang trọng với ánh sáng nghệ thuật.", "mantra": "Hậu cảnh sang trọng uy nghi — Nâng tầm đẳng cấp ngại gì gian nan"},
            {"num": 5, "meta": "CHUYỂN THỂ ĐA KÊNH", "title": "Một video dài sinh ra 10 định dạng bài viết trong 5 phút", "ground_truth": "Phân phối đa kênh là cách duy nhất để tối đa hóa lợi nhuận trên mỗi giờ làm việc của bạn.", "surface": "Quay xong video YouTube rồi để mặc nó ở đó mà không chia sẻ lên các nền tảng khác.", "nature": "Nội dung giá trị cao có thể được tái cấu trúc thành bài viết LinkedIn, chuỗi Twitter và bản tin Email.", "leverage": "Nạp transcript video vào AI và yêu cầu chuyển thể thành 5 định dạng bài viết khác nhau theo chuẩn từng mạng xã hội.", "mantra": "Một hạt trổ nở mười hoa — Đa kênh lan tỏa bài ca rạng ngời"},
            {"num": 6, "meta": "BẢO VỆ CHẤT RIÊNG", "title": "Luôn biên tập lại 30% nội dung do AI tạo ra", "ground_truth": "Văn bản AI nguyên bản luôn chứa những từ ngữ sáo rỗng như 'delve', 'testament', 'revolutionize'.", "surface": "Đăng ngay văn bản AI viết mà không thèm đọc lại một lần.", "nature": "Những từ ngữ sáo rỗng của AI lập tức báo động cho bộ não người đọc về sự lười biếng và giả tạo.", "leverage": "Tự tay đọc lại, thay thế các từ đao to búa lớn bằng ngôn ngữ mộc mạc và chèn câu chuyện cá nhân.", "mantra": "Gọt giũa từ ngữ sáo cằn — Thổi hồn mộc mạc muôn phần đáng yêu"},
            {"num": 7, "meta": "HỖ TRỢ KHÁCH HÀNG THÔNG MINH", "title": "AI giải đáp thắc mắc chuyên sâu theo đúng triết lý của bạn", "ground_truth": "Khách hàng nhận được câu trả lời chính xác trong 3 phút có tỷ lệ hài lòng cao gấp 5 lần chờ đợi 24 giờ.", "surface": "Tự mình trả lời hàng trăm câu hỏi kỹ thuật giống nhau mỗi ngày.", "nature": "Sự chậm trễ trong hỗ trợ là nguyên nhân hàng đầu khiến khách hàng hủy dịch vụ.", "leverage": "Huấn luyện AI Bot trên kho video và tài liệu của bạn để giải đáp thắc mắc chuyên môn 24/7.", "mantra": "Trợ lý thông minh đêm ngày — Giải đáp thấu đáo dựng xây niềm tin"},
            {"num": 8, "meta": "TỰ DO KIẾN TẠO", "title": "AI giúp bạn tập trung 100% vào việc sống một cuộc đời đáng sống", "ground_truth": "Trải nghiệm sống phong phú bên ngoài màn hình máy tính chính là chất liệu nuôi dưỡng sự nghiệp sáng tạo của bạn.", "surface": "Dùng AI để làm nhiều việc hơn rồi lại cắm mặt vào máy tính suốt ngày.", "nature": "Đòn bẩy công nghệ sinh ra để trả lại tự do cho con người, không phải để biến bạn thành nô lệ kỹ thuật số.", "leverage": "Rút ngắn giờ làm việc xuống 4 tiếng mỗi ngày, dành thời gian đi du lịch, đọc sách và ở bên người thân.", "mantra": "Công nghệ trả lại tự do — Sống đời trọn vẹn ấm no thảnh thơi"}
        ],
        "environment": {
            "title": "Thiết lập quy trình tự động hóa AI một chạm",
            "items": [
                ("1. Bàn phím Macro Elgato Stream Deck", "Bấm 1 phím vật lý để tự động mở toàn bộ ứng dụng quay hình, ghi âm và công cụ AI."),
                ("2. Quy trình đồng bộ đám mây tự động (Zapier / Make)", "Tự động gửi video từ máy tính sang công cụ phụ đề và lưu trữ vào thư viện nội bộ."),
                ("3. Kính lọc ánh sáng xanh bảo vệ mắt", "Đeo kính chống ánh sáng xanh khi làm việc với màn hình máy tính để giấc ngủ đêm sâu hơn.")
            ],
            "mantra": "Một chạm phím bấm nhẹ nhàng — Toàn bộ hệ thống sẵn sàng thi hành"
        },
        "emotional": {
            "title": "Tâm thế người làm chủ công nghệ thanh thản",
            "items": [
                ("1. Không lo lắng bị AI thay thế", "Tự tin vào trái tim, tâm hồn và khả năng yêu thương độc bản của con người mà không thuật toán nào sao chép được."),
                ("2. Thong dong thử nghiệm những điều mới mẻ", "Xem công nghệ như một trò chơi thú vị giúp mở rộng năng lực sáng tạo của bản thân."),
                ("3. Giữ trọn sự chân thành trong mọi thông điệp", "Dù công nghệ có thay đổi đến đâu, sự chân thành vẫn là chiếc chìa khóa duy nhất chạm tới trái tim người khác.")
            ],
            "mantra": "Làm chủ máy móc ung dung — Trái tim nhân ái muôn trùng sáng trong"
        }
    },

    # 26. AI First and Win (XOVY57gysSQ)
    {
        "id": raw_vids[26]['id'],
        "slug": "how-to-use-ai-first-and-win-podcast.html",
        "ep_code": "OE26",
        "cat_badge": "04 / TRÍ TUỆ NHÂN TẠO & ĐỘT PHÁ NĂNG SUẤT",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "TƯ DUY AI-FIRST: CÁCH DẪN ĐẦU CUỘC CHƠI TRONG MỌI NGÀNH NGHỀ",
        "orig_title": raw_vids[26]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[26]['id']}",
        "publish_date": raw_vids[26]['date'],
        "raw_date": f"{raw_vids[26]['raw_date'][:4]}-{raw_vids[26]['raw_date'][4:6]}-{raw_vids[26]['raw_date'][6:]}",
        "duration": "1 giờ 35 phút",
        "read_time": "~9 phút chắt lọc",
        "hero_quote": "Tư duy đi trước một bước — AI mở lối dẫn đường thành công",
        "lead_points": [
            "Khái niệm 'AI-First Mindset': Trước khi bắt đầu bất kỳ dự án nào, hãy tự hỏi 'Làm thế nào để AI có thể giải quyết 80% phần việc nặng nhọc này?' thay vì lao đầu vào làm theo cách thủ công cũ.",
            "Phân tích cách tái cấu trúc doanh nghiệp và kỹ năng cá nhân để trở thành người dẫn đầu trong kỷ nguyên chuyển dịch công nghệ lớn nhất lịch sử loài người."
        ],
        "hero_summary": {
            "title": "Bản đồ chuyển đổi tư duy sang mô hình AI-First",
            "items": [
                ("1. Phản xạ AI-First", "Mỗi khi đối diện với nhiệm vụ mới, phản xạ đầu tiên là thiết kế prompt hoặc quy trình tự động hóa thay vì tự tay làm thủ công."),
                ("2. Tối ưu hóa chi phí vận hành", "Giảm thiểu chi phí cố định, biến các khoản chi phí khổng lồ thành các dịch vụ phần mềm linh hoạt."),
                ("3. Nâng cao giá trị thù lao cá nhân", "Người làm chủ AI nhận thù lao cao gấp 5 lần người chỉ biết làm việc chân tay thông thường.")
            ],
            "mantra": "Đổi mới phản xạ tư duy — Đón đầu ngọn sóng ngại gì chông gai"
        },
        "delusion": {
            "title": "ẢO TƯỞNG CÔNG NGHỆ CHỈ LÀ TRÀO LƯU NHẤT THỜI & SỰ THẬT VỀ SỰ ĐÀO THẢI",
            "desc": "Nhiều người bảo thủ cho rằng AI chỉ là cơn sốt nhất thời như metaverse rồi sẽ xẹp xuống. Những ai chần chừ không học cách ứng dụng AI hôm nay sẽ chịu chung số phận với những người từng từ chối sử dụng máy tính và internet 25 năm trước.",
            "compare_left": {
                "badge": "TƯ DUY BẢO THỦ",
                "title": "Từ chối học hỏi vì sợ phức tạp",
                "text": "Tiếp tục làm việc theo thói quen cũ, năng suất dậm chân tại chỗ và dần bị thị trường đào thải."
            },
            "compare_right": {
                "badge": "TIÊN PHONG ĐÓN ĐẦU",
                "title": "Chủ động làm chủ công cụ và dẫn dắt cuộc chơi",
                "text": "Nhanh chóng làm chủ các công cụ mới, nhân bản năng suất cá nhân và trở thành nhân sự không thể thay thế."
            },
            "matrix_title": "So sánh Người kháng cự công nghệ và Người dẫn đầu AI-First",
            "matrix_items": [
                ("Người kháng cự", "• Chi phí thời gian cao, năng suất thấp, luôn cảm thấy quá tải trong công việc.<br>• Thu nhập ngày càng giảm sút do giá trị lao động cơ bắp bị hạ thấp."),
                ("Người dẫn đầu AI-First", "• Hoàn thành công việc trong thời gian ngắn kỷ lục, chất lượng vượt trội.<br>• Trở thành cố vấn chiến lược được săn đón với mức thù lao cao ngất ngưởng.")
            ],
            "mantra": "Kháng cự chuốc lấy lụi tàn — Tiên phong đón sóng mở đàng vinh hoa"
        },
        "insights": [
            {"num": 1, "meta": "PHẢN XẠ AI-FIRST", "title": "Thiết lập phản xạ AI-First trong mọi quyết định hàng ngày", "ground_truth": "Người chiến thắng trong kỷ nguyên mới là người có phản xạ hỏi AI trước khi tự tay làm.", "surface": "Bắt tay vào gõ từng dòng văn bản báo cáo hoặc tìm kiếm tài liệu thủ công suốt 3 tiếng.", "nature": "Hành vi thủ công tiêu tốn năng lượng nhận thức quý giá vào những việc đã có lời giải tối ưu.", "leverage": "Mở đầu ngày làm việc bằng việc giao các tác vụ nghiên cứu và phân loại tài liệu cho AI.", "mantra": "Trước khi bắt bước làm ngay — Hỏi máy giải quyết tháng ngày thảnh thơi"},
            {"num": 2, "meta": "KỸ NĂNG PROMPT ĐỈNH CAO", "title": "Kỹ thuật Prompting theo vai trò, bối cảnh và tiêu chuẩn đầu ra", "ground_truth": "Chất lượng câu trả lời của AI phản ánh chính xác chất lượng tư duy của người đặt câu hỏi.", "surface": "Gõ những câu lệnh ngắn ngủn và phàn nàn AI trả lời quá ngô nghê.", "nature": "AI cần được cung cấp vai trò chuyên gia, bối cảnh cụ thể, mục tiêu rõ ràng và các ràng buộc tiêu chuẩn.", "leverage": "Cấu trúc prompt 4 phần: Vai trò (Role) + Bối cảnh (Context) + Nhiệm vụ (Task) + Định dạng đầu ra (Format).", "mantra": "Bốn phần câu lệnh rõ ràng — Máy sinh đáp án nhẹ nhàng hanh thông"},
            {"num": 3, "meta": "PHÂN TÍCH ĐỐI THỦ", "title": "Bóc tách chiến lược của đối thủ cạnh tranh trong 5 phút", "ground_truth": "Mọi dữ liệu công khai của đối thủ đều có thể được AI phân tích để tìm ra điểm yếu chí mạng.", "surface": "Ngồi xem từng video của đối thủ và ghi chép thủ công mệt mỏi.", "nature": "AI có thể đọc toàn bộ phụ đề 50 video của đối thủ để chỉ ra những chủ đề khán giả phàn nàn nhiều nhất.", "leverage": "Thu thập transcript kênh đối thủ, dùng AI phân tích những nỗi đau chưa được giải quyết để làm video vượt trội.", "mantra": "Điểm mù đối thủ sáng soi — Ta vào giải quyết người người ngợi khen"},
            {"num": 4, "meta": "SÁNG TẠO HÌNH ẢNH", "title": "Tạo ra các ấn phẩm truyền thông đẳng cấp thế giới không cần designer", "ground_truth": "Các công cụ tạo ảnh AI Midjourney và DALL-E 3 tạo ra hình ảnh nghệ thuật vượt xa designer nghiệp dư.", "surface": "Chờ đợi designer 3 ngày chỉ để có 1 bức ảnh bìa Facebook bình thường.", "nature": "Sự chậm trễ trong khâu hình ảnh làm nghẽn toàn bộ tốc độ ra mắt chiến dịch.", "leverage": "Tự tay sinh ảnh minh họa siêu thực và concept nghệ thuật chỉ trong 2 phút bằng các câu lệnh chính xác.", "mantra": "Hình ảnh kiệt tác hiện ra — Chỉ trong tích tắc cả nhà chung vui"},
            {"num": 5, "meta": "HỌC TẬP THẦN TỐC", "title": "Rút ngắn thời gian đọc và thẩm thấu một cuốn sách xuống 30 phút", "ground_truth": "Bạn không cần đọc từng chữ trong cuốn sách 300 trang; bạn chỉ cần rút ra 3 bài học thực chiến lớn nhất.", "surface": "Mất cả tháng trời để đọc xong 1 cuốn sách lý thuyết dày cộp.", "nature": "Sự quá tải thông tin khiến bạn quên sạch những gì đã đọc sau 2 tuần.", "leverage": "Nạp file sách vào AI, yêu cầu trích xuất các nguyên lý hành động và bài tập thực hành áp dụng ngay vào doanh nghiệp.", "mantra": "Chắt chiu tinh túy sách dày — Áp dụng thực tế tháng ngày sinh sôi"},
            {"num": 6, "meta": "LẬP TRÌNH KHÔNG CẦN CODE", "title": "Xây dựng các công cụ phần mềm nội bộ bằng No-code và AI", "ground_truth": "Bất kỳ ai cũng có thể tạo ra ứng dụng web đơn giản chỉ bằng việc mô tả ý tưởng bằng ngôn ngữ tự nhiên.", "surface": "Bỏ ra hàng trăm triệu thuê lập trình viên làm những tính năng đơn giản.", "nature": "Mô hình ngôn ngữ lớn có khả năng viết mã code hoàn chỉnh và sửa lỗi tự động chỉ trong vài giây.", "leverage": "Dùng AI viết các đoạn mã tự động hóa quy trình nội bộ và tạo công cụ tính toán tiện ích cho khách hàng.", "mantra": "Ý tưởng cất tiếng rõ ràng — Phần mềm tự động sẵn sàng thi hành"},
            {"num": 7, "meta": "BẢO MẬT VÀ QUYỀN RIÊNG TƯ", "title": "Bảo vệ bí mật kinh doanh khi sử dụng các công cụ AI đám mây", "ground_truth": "Đưa toàn bộ dữ liệu nhạy cảm của công ty lên các mô hình công cộng có thể gây rò rỉ bí mật thương mại.", "surface": "Tải toàn bộ báo cáo tài chính và danh sách mật khẩu lên các công cụ AI miễn phí.", "nature": "Các mô hình công cộng có thể dùng dữ liệu của bạn để huấn luyện phiên bản tiếp theo.", "leverage": "Tắt tính năng chia sẻ dữ liệu huấn luyện, sử dụng các phiên bản Enterprise hoặc chạy mô hình AI mã nguồn mở cục bộ.", "mantra": "Bảo mật dữ liệu hàng đầu — Giữ gìn bí mật dài lâu vững bền"},
            {"num": 8, "meta": "CON ĐƯỜNG TIÊN PHONG", "title": "Trở thành người chia sẻ và đào tạo AI trong ngách của bạn", "ground_truth": "Thị trường đang khao khát những người biết cách ứng dụng AI vào các ngành nghề truyền thống cụ thể.", "surface": "Giữ kín những mẹo AI hay ho cho riêng mình mà không chia sẻ.", "nature": "Người tiên phong hướng dẫn đồng nghiệp cách ứng dụng công nghệ sẽ tự động trở thành lãnh đạo tinh thần của ngành.", "leverage": "Tổ chức các buổi workshop chia sẻ: 'Cách ứng dụng AI để tăng gấp 3 năng suất trong ngành [Tên ngành]'.", "mantra": "Tiên phong chỉ lối dẫn đường — Uy danh tỏa rạng muôn phương kính vì"}
        ],
        "environment": {
            "title": "Thiết lập không gian nghiên cứu công nghệ AI tập trung",
            "items": [
                ("1. Trình duyệt chuyên dụng cho AI với các extension phím tắt", "Cài đặt các extension gán phím tắt nhanh để gọi AI tóm tắt trang web chỉ bằng 1 thao tác."),
                ("2. Môi trường ánh sáng trắng kích thích sự tỉnh táo (5000K)", "Ánh sáng trắng giúp duy trì sự tỉnh táo và tập trung cao độ khi nghiên cứu dữ liệu phức tạp."),
                ("3. Sổ tay ghi chép các công thức prompt hiệu quả", "Ghi lại những câu lệnh tạo ra kết quả xuất sắc để biến thành tài sản biểu mẫu dùng lại.")
            ],
            "mantra": "Phím tắt thao tác gọn gàng — Sổ tay ghi chép nhẹ nhàng lưu tâm"
        },
        "emotional": {
            "title": "Nuôi dưỡng tâm thế tò mò và cầu tiến không ngừng",
            "items": [
                ("1. Giữ tâm trí của một người mới bắt đầu (Beginner's Mind)", "Sẵn sàng xóa bỏ những định kiến cũ để đón nhận những chân trời kiến thức mới mẻ."),
                ("2. Không hoảng loạn trước tốc độ phát triển chóng mặt của công nghệ", "Bình thản tiếp nhận từng bước, tập trung vào những nguyên lý cốt lõi bất biến của con người."),
                ("3. Tìm thấy niềm vui thuần khiết trong việc giải phóng sức lao động", "Hạnh phúc khi thấy những công việc nhàm chán trước đây nay đã được máy móc làm thay hoàn hảo.")
            ],
            "mantra": "Tâm trí mở rộng thênh thang — Đón luồng gió mới nhẹ nhàng bay cao"
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

print(f"Hoàn thành cập nhật episodes_batch3.py với {len(BATCH_3)} tập (OE21 - OE26)!")
