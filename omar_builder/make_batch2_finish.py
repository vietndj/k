# -*- coding: utf-8 -*-
"""
make_batch2_finish.py: Hoàn thành OE13 - OE20 cho episodes_batch2.py
"""
import json
import sys
sys.path.append('/Users/vietmac/Documents/CODE/k/omar_builder')
from episodes_batch2 import BATCH_2

with open('/Users/vietmac/.gemini/antigravity/brain/24deb8b1-3156-43d0-91a1-3246f0cc4078/scratch/omar_40_videos.json') as f:
    raw_vids = {v['idx']: v for v in json.load(f)}

eps = [
    # 13. Stop Guessing Content (SUzayesJTMI)
    {
        "id": raw_vids[13]['id'],
        "slug": "new-way-to-win-as-content-creator-podcast.html",
        "ep_code": "OE13",
        "cat_badge": "03 / CHIẾN LƯỢC NỘI DUNG YOUTUBE & VIDEO TRIỆU VIEW",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "LUẬT CHƠI MỚI CỦA CONTENT CREATOR: NGỪNG PHỎNG ĐOÁN, TẬP TRUNG DỮ LIỆU",
        "orig_title": raw_vids[13]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[13]['id']}",
        "publish_date": raw_vids[13]['date'],
        "raw_date": f"{raw_vids[13]['raw_date'][:4]}-{raw_vids[13]['raw_date'][4:6]}-{raw_vids[13]['raw_date'][6:]}",
        "duration": "1 giờ 00 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Đoán già đoán non phí hoài — Nhìn vào số liệu mở tài khai hoa",
        "lead_points": [
            "Đa số người làm YouTube thất bại vì làm video dựa trên cảm xúc cá nhân thay vì giải mã các tín hiệu dữ liệu thực tế từ công cụ nghiên cứu từ khóa và biểu đồ phân tích tỷ lệ giữ chân (Retention Graph).",
            "Omar bóc tách quy trình 3 giai đoạn: Nghiên cứu nhu cầu tìm kiếm -> Thiết kế bao bì (Title & Thumbnail) trước khi quay -> Tối ưu hóa 30 giây đầu tiên để giữ chân người xem."
        ],
        "hero_summary": {
            "title": "Bản đồ sản xuất nội dung dựa trên bằng chứng dữ liệu",
            "items": [
                ("1. Thiết kế bao bì trước khi bấm máy", "Tiêu đề và ảnh thu nhỏ (Thumbnail) phải được phê duyệt trước khi viết kịch bản; nếu không có góc nhìn hấp dẫn, không bao giờ bấm máy."),
                ("2. Đọc vị biểu đồ giữ chân (Retention Dip)", "Phát hiện chính xác từng giây khán giả rời bỏ video để cắt bỏ triệt để các đoạn giải thích rườm rà trong video tiếp theo."),
                ("3. Tối ưu hóa CTR (Click-Through-Rate)", "Tạo ra sự tò mò trí tuệ kết hợp với độ tương phản thị giác cao trên thumbnail để kích hoạt phản xạ bấm chuột tự nhiên.")
            ],
            "mantra": "Bao bì chuẩn chỉ rõ ràng — Người xem bấm chuột nhẹ nhàng vào xem"
        },
        "delusion": {
            "title": "ẢO TƯỞNG CỨ QUAY ĐI RỒI TÍNH & BẢN CHẤT CẠNH TRANH THỊ GIÁC",
            "desc": "Người mới thường quay video xong xuôi rồi mới vội vàng chụp đại một tấm ảnh làm thumbnail và đặt một cái tên chung chung. Đây là nguyên nhân khiến 95% video chìm nghỉm dưới đáy đại dương thuật toán.",
            "compare_left": {
                "badge": "SAI LẦM PHỔ BIẾN",
                "title": "Quay video trước, nghĩ tiêu đề sau",
                "text": "Bỏ ra 20 tiếng quay dựng một kiệt tác nhưng đặt tiêu đề chán ngắt khiến không ai thèm bấm vào xem."
            },
            "compare_right": {
                "badge": "QUY CHUẨN THỰC CHIẾN",
                "title": "Bắt đầu từ cái kết: Ý tưởng & Thumbnail",
                "text": "Kiểm chứng 3 phương án tiêu đề và 2 mẫu ảnh thumbnail xem có đủ sức cạnh tranh với các video hàng đầu hay không rồi mới viết kịch bản."
            },
            "matrix_title": "So sánh Sáng tạo cảm tính và Sáng tạo dựa trên dữ liệu",
            "matrix_items": [
                ("Sáng tạo cảm tính ngẫu hứng", "• Lượt xem trồi sụt bấp bênh, phụ thuộc vào vận may may rủi.<br>• Thường xuyên rơi vào trạng thái thất vọng vì video tâm huyết không ai xem."),
                ("Sáng tạo có chiến lược dữ liệu", "• Tỷ lệ thành công dự đoán trước được trên 70%.<br>• Kênh tăng trưởng ổn định theo biểu đồ dốc đứng qua từng quý.")
            ],
            "mantra": "Bao bì đi trước mở đường — Nội dung vững bước muôn phương đón chào"
        },
        "insights": [
            {"num": 1, "meta": "THIẾT KẾ BAO BÌ", "title": "Bao bì quyết định 80% thành công của video", "ground_truth": "Nếu không ai bấm vào xem, nội dung bên trong hay đến đâu cũng trở thành vô nghĩa.", "surface": "Chụp đại một bức ảnh cắt từ video làm thumbnail.", "nature": "Mắt người lướt qua thumbnail trong 0.2 giây; não bộ quyết định bấm xem hoàn toàn dựa trên sự tò mò và cảm xúc thị giác tức thì.", "leverage": "Thiết kế thumbnail có chủ thể nổi bật, biểu cảm khuôn mặt rõ nét và văn bản dưới 4 từ mang tính kích thích tò mò.", "mantra": "Hình ảnh bắt mắt tức thì — Người xem bấm chuột ngại gì thời gian"},
            {"num": 2, "meta": "30 GIÂY VÀNG", "title": "Giữ trọn lời hứa của tiêu đề trong 10 giây đầu tiên", "ground_truth": "Tỷ lệ thoát trang cao nhất luôn xảy ra ở giây thứ 15 đến 30 của video.", "surface": "Mở đầu video bằng lời chào rườm rà và kêu gọi đăng ký kênh.", "nature": "Khán giả vào xem để tìm câu trả lời cho tiêu đề; khi thấy người nói vòng vo, họ sẽ bấm back ngay lập tức.", "leverage": "Xác nhận ngay vấn đề và hứa hẹn kết quả đột phá trong 3 câu đầu tiên của video.", "mantra": "Mở đầu đi thẳng nguồn cơn — Giữ chân khán giả muôn phần say mê"},
            {"num": 3, "meta": "NGHIÊN CỨU TỪ KHÓA", "title": "Giải quyết các câu hỏi có nhu cầu tìm kiếm cao (Search Intent)", "ground_truth": "Kênh nhỏ phát triển nhanh nhất bằng cách trả lời các câu hỏi cụ thể mà khán giả đang chủ động gõ tìm kiếm.", "surface": "Làm video vlog đời thường kể về cuộc sống của mình khi chưa ai biết mình là ai.", "nature": "Khán giả không quan tâm bạn ăn gì hôm nay; họ chỉ tìm kiếm cách giải quyết nỗi đau của họ.", "leverage": "Dùng tính năng YouTube Search Suggest để tìm kiếm các từ khóa bắt đầu bằng 'Làm sao để...' trong ngành.", "mantra": "Tìm tòi câu hỏi người cần — Trả lời thấu đáo muôn phần tiếng vang"},
            {"num": 4, "meta": "MẠO HIỂM NỘI DUNG", "title": "Tỷ lệ 70/20/10 trong chiến lược nội dung", "ground_truth": "70% nội dung an toàn đã được chứng minh hiệu quả, 20% nội dung thử nghiệm mới và 10% nội dung đột phá sáng tạo.", "surface": "Hoặc là chỉ làm mãi một chủ đề cũ kỹ, hoặc là liên tục đổi chủ đề khiến kênh mất định vị.", "nature": "Thuật toán cần sự nhất quán để phân phối, nhưng khán giả cần sự mới mẻ để không bị nhàm chán.", "leverage": "Giữ vững 70% chủ đề cốt lõi và dành 1 video mỗi tháng để thử nghiệm góc nhìn độc lạ.", "mantra": "Bảy phần giữ vững gốc cành — Ba phần trổ nhánh ngọt lành muôn hoa"},
            {"num": 5, "meta": "ĐỘ DÀI TỐI ƯU", "title": "Độ dài video phải dài đúng bằng lượng giá trị nó mang lại", "ground_truth": "Không có video quá dài; chỉ có video quá chán khiến người ta không muốn xem tiếp.", "surface": "Cố tình kéo dài video ra 10 phút để chèn nhiều quảng cáo bằng cách nói vòng vo.", "nature": "Sự thừa thãi làm giảm thời lượng xem trung bình và phá hủy điểm chất lượng của kênh trong mắt thuật toán.", "leverage": "Cắt bỏ không thương tiếc mọi câu nói thừa, từ đệm 'ờ, à' và các đoạn dừng hình không cần thiết trong khâu hậu kỳ.", "mantra": "Cắt gọt chữ nghĩa tinh thanh — Xem xong đọng lại ngọt lành bài hay"},
            {"num": 6, "meta": "KẾT NỐI DANH SÁCH PHÁT", "title": "Chiến lược giữ chân người xem trong một vòng lặp vô tận (Binge-Watching)", "ground_truth": "Phiên xem kéo dài (Session Time) là chỉ số thuật toán yêu thích nhất.", "surface": "Mỗi video đứng riêng lẻ không có sự liên kết nào với các video khác.", "nature": "Khi 1 khán giả xem liền 3 video của bạn trong 1 buổi tối, thuật toán sẽ tự động đề xuất kênh của bạn cho hàng ngàn người tương tự.", "leverage": "Dùng màn hình kết thúc (End Screen) giới thiệu chính xác video tiếp theo nối tiếp mạch câu chuyện.", "mantra": "Nối liền từng tập từng chương — Khách xem say đắm vấn vương đêm ngày"},
            {"num": 7, "meta": "TƯƠNG TÁC THỰC", "title": "Đặt câu hỏi tranh luận ở giữa video để kích hoạt bình luận", "ground_truth": "Khu vực bình luận sôi nổi là tín hiệu báo cho thuật toán biết nội dung có tính gắn kết cộng đồng cao.", "surface": "Chỉ nói 'Hãy bình luận bên dưới' một cách chung chung.", "nature": "Khán giả muốn được bày tỏ quan điểm khi gặp một câu hỏi kích thích tư duy hoặc quan điểm đối lập.", "leverage": "Đưa ra 2 luồng ý kiến trái chiều và hỏi: 'Anh chị thuộc phe A hay phe B? Hãy chia sẻ lý do bên dưới'.", "mantra": "Hỏi câu gợi mở tâm tư — Khán giả tranh luận bức thư gửi về"},
            {"num": 8, "meta": "KIÊN ĐỊNH CHIẾN LƯỢC", "title": "Cuộc chơi marathon 100 video đầu tiên", "ground_truth": "Đa số kênh YouTube thành công chỉ thực sự cất cánh sau video thứ 50 hoặc 70.", "surface": "Kỳ vọng video thứ 3 sẽ viral và bỏ cuộc khi thấy ít lượt xem.", "nature": "Mỗi video là một bài học giúp bạn nâng cấp kỹ năng ăn nói, biên tập và thấu hiểu khán giả.", "leverage": "Ký hợp đồng cam kết với chính bản thân: Xuất bản 1 video mỗi tuần trong vòng 1 năm không ngắt quãng.", "mantra": "Đường dài thử sức ngựa hay — Chăm chỉ gieo hạt tháng ngày nở hoa"}
        ],
        "environment": {
            "title": "Thiết lập quy trình biên tập và kiểm soát chất lượng video",
            "items": [
                ("1. Màn hình chuẩn màu đồ họa IPS", "Đảm bảo màu da và màu sắc trên thumbnail hiển thị chuẩn xác trên mọi thiết bị di động."),
                ("2. Checklist kiểm tra trước khi xuất bản", "Danh sách 10 điểm kiểm tra: Tiêu đề, Thumbnail, Thẻ tag, Mô tả, Ghim bình luận, Màn hình kết thúc, Phụ đề."),
                ("3. Tai nghe kiểm âm phòng thu Audio-Technica ATH-M50x", "Phát hiện từng tạp âm nhỏ hoặc tiếng xì xào để xử lý sạch sẽ trước khi đưa lên mạng.")
            ],
            "mantra": "Checklist từng bước rõ ràng — Kiểm tra chu đáo vững vàng lên sóng"
        },
        "emotional": {
            "title": "Quản trị năng lượng tinh thần của người làm sáng tạo",
            "items": [
                ("1. Tách rời giá trị bản thân khỏi biểu đồ view", "Một video ít view không có nghĩa là bạn kém cỏi; đó chỉ là một bài test thị trường cần điều chỉnh góc tiếp cận."),
                ("2. Giữ sự tò mò của một đứa trẻ", "Tiếp cận mỗi video với tâm thế háo hức khám phá và học hỏi kỹ năng mới."),
                ("3. Ăn mừng sự kiên trì của chính mình", "Tự thưởng cho bản thân mỗi khi hoàn thành xuất bản một video đúng hạn bất kể kết quả ra sao.")
            ],
            "mantra": "Vững tâm gieo bước kiên trì — Mặc cho số liệu thị phi biến dời"
        }
    },

    # 14. $1M Content Strategy (IuiupaSfMkA)
    {
        "id": raw_vids[14]['id'],
        "slug": "1m-dollar-content-strategy-any-business-podcast.html",
        "ep_code": "OE14",
        "cat_badge": "03 / CHIẾN LƯỢC NỘI DUNG YOUTUBE & VIDEO TRIỆU VIEW",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "CHIẾN LƯỢC NỘI DUNG TRIỆU USD ÁP DỤNG CHO MỌI MÔ HÌNH KINH DOANH",
        "orig_title": raw_vids[14]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[14]['id']}",
        "publish_date": raw_vids[14]['date'],
        "raw_date": f"{raw_vids[14]['raw_date'][:4]}-{raw_vids[14]['raw_date'][4:6]}-{raw_vids[14]['raw_date'][6:]}",
        "duration": "1 giờ 14 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Nội dung xây dựng phễu vàng — Khách hàng tự tới bạc vàng sinh sôi",
        "lead_points": [
            "Làm nội dung để kiếm triệu đô hoàn toàn khác với làm nội dung để trở thành người nổi tiếng: Mục tiêu không phải là hàng triệu view vô nghĩa, mà là dẫn dắt người xem qua 3 giai đoạn Nhận thức -> Tin tưởng -> Chuyển đổi.",
            "Omar tiết lộ cấu trúc ma trận nội dung 4 trụ cột: Nội dung thu hút (Attract), Nội dung nuôi dưỡng (Nurture), Nội dung phá bỏ rào cản (Overcome Objections) và Nội dung chốt đơn (Convert)."
        ],
        "hero_summary": {
            "title": "Ma trận nội dung chuyển đổi triệu đô",
            "items": [
                ("1. Trụ cột Thu hút (Top of Funnel)", "Giải quyết các câu hỏi nhập môn rộng để tiếp cận tệp khách hàng tiềm năng mới."),
                ("2. Trụ cột Nuôi dưỡng (Middle of Funnel)", "Phân tích sâu các case study thực tế, bộc lộ triết lý làm nghề độc bản để xây dựng lòng tin tuyệt đối."),
                ("3. Trụ cột Chốt đơn (Bottom of Funnel)", "Lời mời hợp tác trực tiếp, giải quyết mọi thắc mắc về giá cả và cam kết hoàn vốn.")
            ],
            "mantra": "Bốn trụ ma trận phân minh — Dẫn đường chỉ lối ân tình bền lâu"
        },
        "delusion": {
            "title": "ẢO TƯỞNG CÀNG NHIỀU VIEW CÀNG GIÀU & SỰ THẬT VỀ ĐỘ CHUYỂN ĐỔI",
            "desc": "Nhiều chủ doanh nghiệp thuê các bạn trẻ làm video bắt trend TikTok nhảy múa hàng triệu view nhưng không bán được bất kỳ đơn hàng nào. Nội dung phục vụ kinh doanh phải đo bằng doanh số trên mỗi lượt xem (Revenue Per View), không phải số view thô.",
            "compare_left": {
                "badge": "LỐI MÒN GIẢI TRÍ",
                "title": "Chạy theo nội dung sốc, hài hước mua vui",
                "text": "Kênh đạt 100.000 người theo dõi nhưng khi đăng bài bán hàng thì nhận về sự phẫn nộ hoặc thờ ơ."
            },
            "compare_right": {
                "badge": "CHIẾN LƯỢC KINH DOANH",
                "title": "Nội dung định vị chuyên gia giải quyết vấn đề",
                "text": "Mỗi video đều sàng lọc chính xác những người có nhu cầu cấp bách và có ngân sách thanh toán sẵn sàng."
            },
            "matrix_title": "So sánh Nội dung mua vui và Nội dung sinh doanh số",
            "matrix_items": [
                ("Nội dung mua vui", "• Khán giả chỉ tìm kiếm cảm giác giải trí giết thời gian.<br>• Doanh thu gần như bằng 0 khi chuyển đổi sang sản phẩm giáo dục hoặc dịch vụ."),
                ("Nội dung kinh doanh triệu đô", "• Khán giả là các chủ doanh nghiệp và người có tiền tìm kiếm giải pháp thực chiến.<br>• Tỷ lệ chuyển đổi thành khách hàng trả phí cực kỳ cao.")
            ],
            "mantra": "Mua vui nhí nhố tiền rơi — Chuyên gia giải quyết muôn đời ấm no"
        },
        "insights": [
            {"num": 1, "meta": "DOANH THU TRÊN VIEW", "title": "Tập trung vào chỉ số RPV (Revenue Per View)", "ground_truth": "Một video 500 view mang lại 2 hợp đồng $10.000 có giá trị gấp trăm lần một video 1 triệu view mang lại $50 tiền AdSense.", "surface": "Đo lường thành công bằng lượt xem hiển thị công khai.", "nature": "Doanh thu thực tế đến từ số lượng giao dịch giá trị cao được sinh ra từ những người xem chất lượng.", "leverage": "Tối ưu hóa nội dung hướng thẳng tới nhóm khách hàng có khả năng chi trả lớn.", "mantra": "Số view chỉ để ngắm nhìn — Tiền vào tài khoản vững tin làm nghề"},
            {"num": 2, "meta": "PHẪU NỘI DUNG 4 TẦNG", "title": "Phân bổ thời lượng cho 4 tầng nhận thức của khách hàng", "ground_truth": "Khách hàng không bao giờ mua ngay ở lần đầu tiên xem video của bạn.", "surface": "Chỉ làm video giới thiệu sản phẩm và giá bán trong mọi tập.", "nature": "Não bộ cần được dẫn dắt từ nhận biết vấn đề, hiểu nguyên nhân gốc rễ, so sánh giải pháp rồi mới đến hành động.", "leverage": "Sản xuất nội dung xen kẽ: 40% thu hút, 30% nuôi dưỡng, 20% gỡ rối rào cản và 10% chốt đơn.", "mantra": "Bốn tầng phễu chuyển hanh thông — Khách đi từng bước thỏa lòng ước mong"},
            {"num": 3, "meta": "BÓC TÁCH CASE STUDY", "title": "Kể chuyện thành công của khách hàng dưới góc nhìn phân tích phẫu thuật", "ground_truth": "Người ta không tin vào lời hứa; người ta tin vào kết quả đã được chứng minh của người đi trước.", "surface": "Khoe thành tích khách hàng một cách hời hợt trên mạng xã hội.", "nature": "Sự tin phục xuất hiện khi bạn mổ xẻ tường tận từng khó khăn khách hàng gặp phải và cách hai bên cùng gỡ rối.", "leverage": "Dành trọn 1 video 30 phút phân tích chi tiết case study một khách hàng từ bờ vực phá sản đến doanh thu triệu đô.", "mantra": "Mổ xẻ câu chuyện thành công — Người xem thấy tỏ ấm lòng gửi trao"},
            {"num": 4, "meta": "LẬP TRÌNH TƯ DUY", "title": "Tái định hình hệ thống niềm tin của khách hàng (Belief Shifting)", "ground_truth": "Trước khi mua giải pháp của bạn, khách hàng phải tin rằng phương pháp cũ của họ đã hoàn toàn lỗi thời.", "surface": "Cố gắng thuyết phục sản phẩm của mình tốt hơn đối thủ 10%.", "nature": "Cải tiến nhỏ không đủ động lực để người ta thay đổi; bạn cần chỉ ra rằng con đường cũ đang dẫn họ tới vực thẳm.", "leverage": "Làm video chỉ ra 3 cái bẫy chết người của cách làm truyền thống và vì sao cần chuyển sang mô hình mới.", "mantra": "Đập tan lối cũ sai lầm — Mở ra đường mới vững tầm tương lai"},
            {"num": 5, "meta": "LÀM CHỦ PHỄU EMAIL", "title": "Mọi con đường nội dung đều phải dẫn về danh sách email độc quyền", "ground_truth": "Thuật toán mạng xã hội biến động liên tục; danh sách email là tài sản kinh doanh bất khả xâm phạm.", "surface": "Chỉ kêu gọi bấm đăng ký kênh YouTube.", "nature": "Khách hàng mua các gói dịch vụ lớn thường đưa ra quyết định sau chuỗi 7–10 email nuôi dưỡng chuyên sâu.", "leverage": "Tặng bộ tài liệu PDF hướng dẫn độc quyền để đổi lấy email trong mọi video.", "mantra": "Email là đất nhà mình — Nuôi dòng tài chính ân tình dài lâu"},
            {"num": 6, "meta": "CHỐNG BÃO GIÁ", "title": "Xây dựng thương hiệu cao cấp giúp bạn miễn nhiễm với cạnh tranh giá rẻ", "ground_truth": "Khách hàng sẵn sàng trả gấp 5 lần nếu họ cảm nhận được sự vượt trội về đẳng cấp và trải nghiệm.", "surface": "Hạ giá để cạnh tranh với các đối thủ mới nổi trên thị trường.", "nature": "Giảm giá là sự tự sát chậm chạp của doanh nghiệp; giá cao là tấm vé bảo đảm chất lượng dịch vụ hoàn hảo.", "leverage": "Đầu tư vào chất lượng hình ảnh, âm thanh và sự chỉn chu trong từng khung hình video để định vị đẳng cấp cao.", "mantra": "Chỉn chu từng nét từng ly — Đẳng cấp vượt trội ngại gì cạnh tranh"},
            {"num": 7, "meta": "TỰ ĐỘNG HÓA CHUYỂN ĐỔI", "title": "Cung cấp đường link đặt lịch hẹn trực tiếp trong phần mô tả", "ground_truth": "Khách hàng bận rộn không muốn nhắn tin qua lại chờ đợi; họ muốn bấm link và chọn lịch tư vấn ngay.", "surface": "Bảo khách 'Hãy inbox cho mình nhé' rồi để họ chờ đợi cả ngày.", "nature": "Sự chậm trễ trong giao tiếp làm nguội lạnh cảm xúc mua hàng tức thì của đối tác.", "leverage": "Cài đặt Calendly kết nối trực tiếp với Google Calendar trong phần mô tả của từng video.", "mantra": "Lịch hẹn đặt sẵn trên bàn — Khách bấm một chạm nhẹ nhàng gặp nhau"},
            {"num": 8, "meta": "TÍCH LŨY DÀI HẠN", "title": "Doanh nghiệp triệu đô được xây trên nền tảng của sự bền bỉ", "ground_truth": "Không có chiến lược nội dung nào hiệu quả nếu bạn chỉ làm việc trong 3 tháng rồi bỏ cuộc.", "surface": "Tìm kiếm các mẹo hack thuật toán để giàu nhanh qua đêm.", "nature": "Sự tin cậy của thị trường cần thời gian để thẩm thấu và kiểm chứng qua các mùa bão táp.", "leverage": "Xem việc làm video như việc đánh răng rửa mặt mỗi tuần, duy trì kỷ luật thép suốt 3–5 năm liên tục.", "mantra": "Bền lòng gieo bước thời gian — Cơ đồ triệu bạc vẻ vang sáng ngời"}
        ],
        "environment": {
            "title": "Thiết lập hệ thống kiểm soát dữ liệu chuyển đổi nội dung",
            "items": [
                ("1. Bảng điều khiển CRM theo dõi nguồn gốc khách hàng", "Ghi nhận chính xác khách hàng ký hợp đồng đến từ video YouTube cụ thể nào."),
                ("2. Quy trình kiểm tra định kỳ hàng tuần", "Họp rà soát các video có tỷ lệ chuyển đổi cao nhất để nhân bản thêm các chủ đề tương tự."),
                ("3. Kịch bản chốt hợp đồng in sẵn trên bàn", "Sẵn sàng tài liệu hướng dẫn chuyển giao dịch vụ ngay khi có khách đặt lịch tư vấn.")
            ],
            "mantra": "Số liệu ghi chép rõ ràng — Nguồn gốc khách tới nhẹ nhàng quản chi"
        },
        "emotional": {
            "title": "Duy trì tâm thái kiên định của nhà kiến trúc kinh doanh",
            "items": [
                ("1. Không bị lay chuyển bởi các trào lưu ngắn hạn", "Giữ vững sự tập trung vào chiến lược dài hạn, không nhảy theo các trend vô bổ."),
                ("2. Bình thản khi doanh số có những tháng trồi sụt", "Hiểu rằng kinh doanh có tính chu kỳ; mùa đông là thời gian chuẩn bị hạt giống cho mùa xuân rực rỡ."),
                ("3. Tận hưởng niềm vui phụng sự thị trường", "Xem mỗi hợp đồng ký kết là một cơ hội giúp đối tác bứt phá cuộc đời.")
            ],
            "mantra": "Vững tâm giữa chốn phong ba — Hướng về đích lớn nở hoa nụ cười"
        }
    }
]

BATCH_2.extend(eps)

# Cập nhật lại episodes_batch2.py
with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch2.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
"""
episodes_batch2.py
Batch 2: Episodes (OE11 - OE20)
"""

BATCH_2 = ''' + json.dumps(BATCH_2, ensure_ascii=False, indent=4) + '\n')

print(f"Hoàn thành cập nhật episodes_batch2.py với {len(BATCH_2)} tập (OE11 - OE14)!")
