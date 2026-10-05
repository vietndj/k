# -*- coding: utf-8 -*-
"""
make_batch1_finish.py: Hoàn thiện nốt OE07 - OE10 cho episodes_batch1.py
"""
import json
import sys
sys.path.append('/Users/vietmac/Documents/CODE/k/omar_builder')
from episodes_batch1 import BATCH_1

with open('/Users/vietmac/.gemini/antigravity/brain/24deb8b1-3156-43d0-91a1-3246f0cc4078/scratch/omar_40_videos.json') as f:
    raw_vids = {v['idx']: v for v in json.load(f)}

eps = [
    # 07. Make $100K+ Selling Knowledge (EYwPIPEFTlk)
    {
        "id": raw_vids[7]['id'],
        "slug": "how-to-make-100k-selling-your-knowledge-podcast.html",
        "ep_code": "OE07",
        "cat_badge": "01 / ĐÓNG GÓI TRI THỨC & ĐỊNH GIÁ CAO CẤP",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "LỘ TRÌNH KIẾM 100.000 USD TỪ BÁN TRI THỨC TRONG KỶ NGUYÊN SỐ",
        "orig_title": raw_vids[7]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[7]['id']}",
        "publish_date": raw_vids[7]['date'],
        "raw_date": f"{raw_vids[7]['raw_date'][:4]}-{raw_vids[7]['raw_date'][4:6]}-{raw_vids[7]['raw_date'][6:]}",
        "duration": "1 giờ 07 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Chuyên môn tích lũy bao năm — Đóng gói tri thức trăm phần vinh hoa",
        "lead_points": [
            "Kiếm 100.000 USD đầu tiên từ kinh doanh tri thức không đòi hỏi bạn phải có hàng trăm ngàn người theo dõi, mà cần một lời chào hàng chuyển đổi cao và 20 khách hàng trả $5.000.",
            "Phân tích lộ trình 4 giai đoạn: Xác thực ý tưởng -> Xây dựng sản phẩm mẫu (MVP) -> Bán trước khi hoàn thiện (Presell) -> Tối ưu hóa phễu khách hàng tự nhiên."
        ],
        "hero_summary": {
            "title": "Bản đồ chinh phục cột mốc 100.000 USD từ tài sản trí tuệ",
            "items": [
                ("1. Nghệ thuật bán trước (Preselling)", "Không bao giờ dành 3 tháng quay khóa học khi chưa có người đặt cọc tiền mặt trước."),
                ("2. Định giá tối thiểu $1.000 - $3.000", "Bỏ qua các sản phẩm giá rẻ $27 hay $97 nếu muốn đạt mốc 100K USD nhanh nhất với nguồn lực nhỏ."),
                ("3. Phễu tư vấn 1-chạm", "Dùng video YouTube dài để nuôi dưỡng lòng tin và điều hướng thẳng vào lịch hẹn tư vấn 1-1.")
            ],
            "mantra": "Bán trước khi dựng sản phẩm — Khách trao tiền cọc vững tâm thi hành"
        },
        "delusion": {
            "title": "ẢO TƯỞNG CẦN NHIỀU FOLLOWER & SỰ THẬT VỀ TỶ LỆ CHUYỂN ĐỔI",
            "desc": "Nhiều người nghĩ phải trở thành influencer triệu view mới kiếm được 100.000 USD. Thực tế, những chuyên gia kiếm tiền giỏi nhất thường chỉ có vài ngàn người theo dõi nhưng đều là khách hàng chi trả cao.",
            "compare_left": {
                "badge": "ẢO TƯỞNG SỐ LƯỢNG",
                "title": "Chạy theo view ảo và số lượng follower",
                "text": "Đăng tải video hài hước bắt trend để kéo follow nhưng không ai trong số họ sẵn sàng bỏ tiền mua dịch vụ chuyên môn."
            },
            "compare_right": {
                "badge": "BẢN CHẤT CHẤT LƯỢNG",
                "title": "Tập trung vào tệp khán giả có khả năng chi trả",
                "text": "Sản xuất video giải quyết các bài toán hóc búa của chủ doanh nghiệp và những người có ngân sách đầu tư nghiêm túc."
            },
            "matrix_title": "So sánh Kênh Triệu View Giá Trị Thấp và Kênh Ngách Chuyển Đổi Cao",
            "matrix_items": [
                ("Kênh triệu view đại trà", "• Lượt xem khổng lồ nhưng chỉ kiếm được tiền lẻ từ quảng cáo AdSense.<br>• Khán giả chủ yếu là học sinh, sinh viên tìm kiếm nội dung giải trí miễn phí."),
                ("Kênh ngách chuyên sâu (Micro-Authority)", "• Mỗi video chỉ 1.000 - 3.000 view nhưng đem lại 5–10 hợp đồng tư vấn giá trị lớn.<br>• Khán giả là người ra quyết định có tiền và cần giải pháp gấp.")
            ],
            "mantra": "Triệu view nhí nhố tiền vơi — Vài nghìn người chuẩn trọn đời ấm no"
        },
        "insights": [
            {"num": 1, "meta": "BÁN TRƯỚC (PRE-SALE)", "title": "Bán giải pháp khi chưa quay xong bài giảng", "ground_truth": "Lý do lớn nhất khiến các khóa học thất bại là sản phẩm không khớp với nhu cầu thực tế của thị trường.", "surface": "Ngồi trong phòng kín 6 tháng quay 50 video rồi mới mang ra bán.", "nature": "Tiền cọc của khách hàng là bảo chứng duy nhất cho thấy ý tưởng của bạn có giá trị thương mại.", "leverage": "Mở bán nhóm thử nghiệm đầu tiên (Beta Cohort) cho 10 người với cam kết vừa dạy trực tiếp vừa hoàn thiện giáo trình.", "mantra": "Tiền cọc trao tay vững dạ — Dạy tới đâu sửa tới đó tài tình"},
            {"num": 2, "meta": "TOÁN HỌC 100K", "title": "Công thức toán học đơn giản để chạm mốc $100K", "ground_truth": "Bán 20 hợp đồng $5.000 dễ gấp 10 lần bán 2.000 món hàng $50.", "surface": "Cố gắng bán thật nhiều ebook giá rẻ để gom góp từng đồng.", "nature": "Quản lý 20 khách hàng cao cấp đem lại trải nghiệm chăm sóc tuyệt vời và tỷ lệ thành công 100%.", "leverage": "Định giá chương trình đồng hành 90 ngày ở mức $3.000 - $5.000 và tập trung chốt 2 khách hàng mỗi tháng.", "mantra": "Hai mươi khách quý đồng hành — Trăm ngàn đô chạm dễ dàng thong dong"},
            {"num": 3, "meta": "NỘI DUNG NUÔI DƯỠNG", "title": "Video YouTube dài là nhân viên kinh doanh làm việc 24/7", "ground_truth": "Khán giả dành 45 phút xem bạn phân tích chuyên môn sẽ tin tưởng bạn hơn xem 100 video ngắn 15 giây.", "surface": "Chỉ mải mê làm video ngắn TikTok giật gân.", "nature": "Video dạng dài tạo ra sự gắn kết cảm xúc sâu sắc và chứng minh năng lực tư duy thấu suốt của chuyên gia.", "leverage": "Làm các video chuyên đề 30–45 phút mổ xẻ tường tận các case study thành công trong ngành.", "mantra": "Video phân tích đàng hoàng — Khách xem thấm thía ngỡ ngàng gửi trao"},
            {"num": 4, "meta": "LỜI KÊU GỌI TINH TẾ", "title": "Đưa ra lời kêu gọi hành động định hướng phỏng vấn", "ground_truth": "Đừng bảo khách 'Hãy mua khóa học của tôi'; hãy mời họ tham gia một buổi đánh giá năng lực.", "surface": "Chèn banner quảng cáo chói mắt kêu gọi mua ngay kẻo lỡ.", "nature": "Khách hàng cao cấp muốn được đối xử như một đối tác chiến lược trong buổi làm việc nghiêm túc.", "leverage": "Kêu gọi: 'Nếu anh muốn tôi trực tiếp xem xét hệ thống hiện tại của anh, hãy điền thông tin vào form bên dưới'.", "mantra": "Mời vào đánh giá khách quan — Khách thương tìm tới bàn tròn kết duyên"},
            {"num": 5, "meta": "KẾT QUẢ HỌC VIÊN", "title": "Case Study là vũ khí bán hàng tối thượng", "ground_truth": "Một câu chuyện thành công của học viên cũ có sức thuyết phục gấp 100 lần lời tự khen của bạn.", "surface": "Đăng tải ảnh chụp màn hình tin nhắn cảm ơn chung chung không có số liệu.", "nature": "Khách hàng muốn nhìn thấy bằng chứng xác thực về sự thay đổi từ điểm A (bế tắc) sang điểm B (thành công rực rỡ).", "leverage": "Phỏng vấn trực tiếp học viên đã kiếm được tiền và đăng toàn bộ cuộc nói chuyện lên YouTube.", "mantra": "Học viên nói hộ lòng mình — Người xem thấy rõ phân minh tỏ tường"},
            {"num": 6, "meta": "BỎ QUA CÔNG NGHỆ RỜI", "title": "Tối giản hóa phễu bán hàng chỉ còn 2 bước", "ground_truth": "Phễu càng nhiều bước phức tạp, tỷ lệ rơi rụng khách hàng càng cao.", "surface": "Cài đặt phần mềm marketing phức tạp với hàng chục trang upsell, downsell.", "nature": "Sự phức tạp tạo ra ma sát và làm chậm tốc độ tiếp cận khách hàng.", "leverage": "Quy trình 2 bước: Video YouTube giá trị cao -> Form Google Form đặt lịch tư vấn 1-1 qua Calendly.", "mantra": "Đơn giản hóa để vững bền — Hai bước chốt gọn dựng nên cơ đồ"},
            {"num": 7, "meta": "TÂM THÁI ĐỊNH VỊ", "title": "Không bán cho người không có tiền hoặc đang mắc nợ", "ground_truth": "Nhận tiền của những người đang tuyệt vọng tài chính sẽ tạo ra áp lực tiêu cực khủng khiếp lên bạn.", "surface": "Ai có tiền là nhận bừa để nhanh đạt chỉ tiêu doanh số.", "nature": "Khách hàng vay nợ để học thường kỳ vọng phép màu qua đêm và dễ dàng nổi giận khi gặp khó khăn.", "leverage": "Quy định rõ trong form đăng ký: Chỉ nhận những người đã có dòng tiền ổn định và sẵn sàng đầu tư nghiêm túc.", "mantra": "Lựa người trao gửi niềm tin — Tránh xa bão táp giữ gìn uy danh"},
            {"num": 8, "meta": "TỰ DO THỜI GIAN", "title": "Chuyển từ tư vấn cá nhân 1-1 sang mô hình nhóm (Group Coaching)", "ground_truth": "Làm việc 1-1 sẽ chạm trần thời gian khi bạn có quá 10 khách hàng cùng lúc.", "surface": "Dành 8 tiếng mỗi ngày để gọi điện cho từng học viên riêng lẻ.", "nature": "Học viên học hỏi được rất nhiều từ câu hỏi và tình huống của các bạn học khác trong cùng một phiên nhóm.", "leverage": "Gom học viên vào các buổi Mastermind nhóm hàng tuần và tạo diễn đàn nội bộ để hỗ trợ lẫn nhau.", "mantra": "Nhóm đông chia sẻ ngọt bùi — Thời gian giải phóng thảnh thơi nụ cười"}
        ],
        "environment": {
            "title": "Thiết lập studio sản xuất nội dung bán tri thức",
            "items": [
                ("1. Micro Shure SM7B hoặc mic thu âm podcast", "Giọng nói dày ấm, loại bỏ tuyệt đối tạp âm xung quanh mang lại cảm giác đài truyền hình chuyên nghiệp."),
                ("2. Đèn Key Light dịu mắt với Softbox lớn", "Ánh sáng tỏa đều không gây gắt mặt, giúp mắt bạn không bị mỏi khi quay hình nhiều giờ."),
                ("3. Bảng theo dõi doanh thu thực tế", "Ghi con số mục tiêu $100.000 và danh sách các khách hàng thành công lên bảng để tự nhắc nhở sứ mệnh.")
            ],
            "mantra": "Ánh sáng dịu mát chan hòa — Micro ấm áp bài ca khởi đầu"
        },
        "emotional": {
            "title": "Duy trì bản lĩnh của người định giá cao",
            "items": [
                ("1. Tự hào về giá trị mình mang lại", "Biết rõ giải pháp của bạn sẽ giúp khách hàng tiết kiệm được hàng năm trời mò mẫm và hàng trăm triệu đồng mất oan."),
                ("2. Không hạ mình trước khách hàng trịch thượng", "Dù khách có nhiều tiền đến đâu, nếu họ thiếu tôn trọng bạn, hãy từ chối phục vụ ngay lập tức."),
                ("3. Bình thản đón nhận những lời chê đắt", "Hiểu rằng Mercedes không bao giờ thanh minh tại sao xe của họ đắt hơn Toyota.")
            ],
            "mantra": "Giá trị tự tại uy nghi — Ai chê đắt đỏ mỉm cười cho qua"
        }
    },

    # 08. Dan Martell AI Strategy (mFoNp1tdtiM)
    {
        "id": raw_vids[8]['id'],
        "slug": "dan-martell-ai-strategy-for-entrepreneurs-podcast.html",
        "ep_code": "OE08",
        "cat_badge": "04 / TRÍ TUỆ NHÂN TẠO & ĐỘT PHÁ NĂNG SUẤT",
        "speaker": "Dan Martell & Omar Eltakrori",
        "speaker_role": "Doanh nhân Công nghệ, Tác giả Best-seller 'Buy Back Your Time' & Nhà đầu tư Thiên thần",
        "tagline": "CHIẾN LƯỢC ỨNG DỤNG AI ĐỂ MUA LẠI THỜI GIAN & NHÂN BẢN TÀI SẢN DOANH NGHIỆP",
        "orig_title": raw_vids[8]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[8]['id']}",
        "publish_date": raw_vids[8]['date'],
        "raw_date": f"{raw_vids[8]['raw_date'][:4]}-{raw_vids[8]['raw_date'][4:6]}-{raw_vids[8]['raw_date'][6:]}",
        "duration": "1 giờ 17 phút",
        "read_time": "~9 phút chắt lọc",
        "hero_quote": "Dùng AI mua lại thời gian — Thảnh thơi điều hành muôn vàn sinh sôi",
        "lead_points": [
            "Tỷ phú Dan Martell chỉ ra rằng sai lầm lớn nhất của các chủ doanh nghiệp là dùng AI để làm thêm việc, trong khi mục tiêu tối thượng của AI phải là 'Mua lại thời gian' (Buy Back Your Time) để bạn tập trung vào vùng thiên tài.",
            "Bóc tách khung chiến lược 'Thay thế - Tự động hóa - Nhân bản': Cách đào tạo AI làm trợ lý điều hành, phân tích tài chính và tạo dàn ý nội dung chuẩn xác theo văn phong của bạn."
        ],
        "hero_summary": {
            "title": "Khung kiến trúc AI giải phóng thời gian cho doanh nhân",
            "items": [
                ("1. Thang đo giá trị thời gian ($/giờ)", "Tính toán chính xác giá trị 1 giờ của bạn; bất kỳ công việc nào có giá trị thấp hơn con số đó đều phải giao cho AI hoặc trợ lý ảo xử lý."),
                ("2. Huấn luyện AI theo 'Bộ não thứ hai'", "Cung cấp toàn bộ tri thức, quy trình SOP và tài liệu nội bộ để AI trả lời khách hàng như chính bạn."),
                ("3. Vùng thiên tài (Genius Zone)", "Dành 80% thời gian cho 2 việc quan trọng nhất: Sáng tạo tầm nhìn và Xây dựng mối quan hệ chiến lược.")
            ],
            "mantra": "Giá trị giờ tính rạch ròi — Việc mọn AI đỡ thảnh thơi tầm nhìn"
        },
        "delusion": {
            "title": "ẢO TƯỞNG AI THAY THẾ CON NGƯỜI & SỰ THẬT VỀ ĐÒN BẨY KHUẾCH ĐẠI",
            "desc": "Nhiều người lo sợ AI sẽ cướp mất công việc hoặc ngược lại xem AI là cây đũa thần làm giàu lười biếng. Thực chất, AI chỉ là chiếc kính lúp: Nếu quy trình của bạn rối rắm, AI sẽ khuếch đại sự hỗn loạn; nếu quy trình chuẩn xác, AI sẽ nhân bản kết quả gấp 100 lần.",
            "compare_left": {
                "badge": "ẢO TƯỞNG THỤ ĐỘNG",
                "title": "Nghĩ rằng AI tự vận hành kiếm tiền mà không cần tư duy",
                "text": "Bấm vài nút prompt chung chung rồi mong chờ AI tạo ra bài viết hay hoặc doanh thu triệu đô tự động."
            },
            "compare_right": {
                "badge": "TƯ DUY KIẾN TRÚC SƯ",
                "title": "Xem AI là đội ngũ thực tập sinh siêu tốc cần được huấn luyện",
                "text": "Xây dựng các quy chuẩn SOP rõ ràng, cung cấp ngữ cảnh đầy đủ để AI thực thi chính xác 80% khối lượng công việc thô."
            },
            "matrix_title": "Đối chiếu Doanh nghiệp chậm chuyển đổi và Doanh nghiệp AI-First",
            "matrix_items": [
                ("Doanh nghiệp cồng kềnh truyền thống", "• Chi phí nhân sự khổng lồ, bộ máy quan liêu chậm chạp.<br>• Chủ doanh nghiệp làm việc 16 tiếng mỗi ngày vẫn ngập trong việc vặt."),
                ("Doanh nghiệp Solo Creator dùng AI", "• Bộ máy 1–3 người nhưng tạo ra doanh thu và tầm ảnh hưởng ngang ngửa công ty 30 người.<br>• Nhà sáng lập đi du lịch nhưng hệ thống vẫn tự động vận hành 24/7.")
            ],
            "mantra": "Cồng kềnh bộ máy hao tài — Tinh gọn đòn bẩy ngày ngày tự do"
        },
        "insights": [
            {"num": 1, "meta": "MUA LẠI THỜI GIAN", "title": "Nguyên lý Buy Back Your Time", "ground_truth": "Bạn không thể phát triển một doanh nghiệp triệu USD nếu bạn vẫn tự tay trả lời từng email $10/giờ.", "surface": "Tự làm mọi việc vặt để tiết kiệm vài triệu đồng chi phí thuê ngoài.", "nature": "Thời gian và sự tập trung của bạn có giới hạn nghiêm ngặt; lãng phí năng lượng vào việc vặt sẽ triệt tiêu năng lực chiến lược.", "leverage": "Dùng AI tự động hóa việc tóm tắt email, lên lịch hẹn và phân loại hồ sơ khách hàng.", "mantra": "Việc mọn giao phó máy làm — Giữ đầu minh mẫn lo toan việc đại"},
            {"num": 2, "meta": "NGỮ CẢNH ĐỘC QUYỀN", "title": "AI chỉ thông minh bằng dữ liệu bạn nạp vào", "ground_truth": "Prompt chung chung sẽ cho ra câu trả lời rác chung chung.", "surface": "Hỏi AI những câu ngây ngô: 'Hãy viết cho tôi 1 bài post viral'.", "nature": "Mô hình ngôn ngữ lớn cần ngữ cảnh cụ thể, dữ liệu quá khứ và giọng văn mẫu để tạo ra kết quả xuất sắc.", "leverage": "Tạo một kho tài liệu 'Brand Voice & Philosophy' và nạp làm Custom Instructions cho AI.", "mantra": "Dữ liệu nạp chuẩn từng dòng — Máy sinh kiệt tác thỏa lòng ước mong"},
            {"num": 3, "meta": "QUY TRÌNH TRƯỚC CÔNG CỤ", "title": "Đừng tự động hóa một quy trình đang bị lỗi", "ground_truth": "Tự động hóa sự hỗn loạn chỉ tạo ra một đống rác tự động nhanh hơn.", "surface": "Vội vã cài đặt hàng chục công cụ AI mới nổi mà chưa hiểu rõ luồng công việc.", "nature": "Công nghệ chỉ phát huy tác dụng khi quy trình cốt lõi bằng tay đã được kiểm chứng thành công.", "leverage": "Làm thủ công cho đến khi thuần thục, viết thành checklist 5 bước rồi mới áp dụng công cụ AI.", "mantra": "Quy trình mạch lạc rõ ràng — Đưa máy vào chạy nhẹ nhàng tiến xa"},
            {"num": 4, "meta": "TRỢ LÝ TƯ DUY", "title": "Dùng AI làm đối tác phản biện (Sparring Partner)", "ground_truth": "Người cô đơn nhất trong công ty chính là CEO; họ thiếu người dám chỉ ra lỗ hổng trong ý tưởng của mình.", "surface": "Chỉ dùng AI để viết bài hoặc dịch thuật đơn giản.", "nature": "AI có khả năng đóng vai đối thủ cạnh tranh khó tính nhất để mổ xẻ chiến lược kinh doanh của bạn.", "leverage": "Prompt: 'Hãy đóng vai một nhà đầu tư mạo hiểm khắc nghiệt nhất, chỉ ra 5 lý do tại sao ý tưởng kinh doanh này sẽ phá sản'.", "mantra": "Máy làm đối tác phản hồi — Chỉ ra điểm yếu kịp thời sửa sai"},
            {"num": 5, "meta": "TỐC ĐỘ THỬ NGHIỆM", "title": "Rút ngắn thời gian từ ý tưởng đến thị trường từ 3 tuần xuống 3 giờ", "ground_truth": "Trong kinh doanh số, tốc độ thử nghiệm quan trọng hơn sự hoàn hảo ban đầu.", "surface": "Mất hàng tháng trời thuê designer làm ảnh và copywriter viết trang bán hàng.", "nature": "Thị trường mới là trọng tài cuối cùng; bạn cần đưa sản phẩm ra thử nghiệm nhanh nhất có thể.", "leverage": "Dùng AI viết bản nháp landing page và tạo hình ảnh minh họa chỉ trong 1 buổi chiều.", "mantra": "Ý tưởng thử nghiệm thần tốc — Thị trường phán xét kịp thời chỉnh trang"},
            {"num": 6, "meta": "CHĂM SÓC KHÁCH TỰ ĐỘNG", "title": "Xây dựng AI Agent hỗ trợ học viên 24/7", "ground_truth": "80% câu hỏi của học viên là những thắc mắc cơ bản đã có trong giáo trình.", "surface": "Chuyên gia phải thức đêm trả lời từng câu hỏi lặp đi lặp lại của thành viên.", "nature": "Sự chậm trễ trong giải đáp làm giảm trải nghiệm học tập của người dùng.", "leverage": "Huấn luyện một AI Bot trên toàn bộ transcript các buổi học để trả lời tức thì mọi câu hỏi của học viên.", "mantra": "Trợ lý túc trực đêm ngày — Trả lời thấu đáo dựng xây lòng tin"},
            {"num": 7, "meta": "BẢO TOÀN TÍNH NGƯỜI", "title": "AI lo phần logic, con người lo phần cảm xúc", "ground_truth": "Nội dung 100% do AI viết hoàn toàn vô cảm và bị người đọc nhận diện lướt qua ngay.", "surface": "Sao chép nguyên văn văn bản AI tạo ra và đăng lên mạng xã hội.", "nature": "Sự kết nối giữa người với người được xây dựng trên những tổn thương, trải nghiệm thật và góc nhìn độc bản.", "leverage": "Dùng AI để lên khung sườn ý tưởng, sau đó tự tay chèn thêm các câu chuyện đời thực của bản thân.", "mantra": "Khung xương máy dựng sẵn sàng — Thổi hồn cảm xúc chứa chan nghĩa tình"},
            {"num": 8, "meta": "TỰ DO TUYỆT ĐỐI", "title": "Mục tiêu cuối cùng của kinh doanh là sự tự do tự tại", "ground_truth": "Doanh nghiệp kiếm được triệu đô nhưng người sáng lập không có thời gian ăn tối cùng gia đình là một thất bại.", "surface": "Tự hào khoe mình làm việc 100 giờ mỗi tuần không có ngày nghỉ.", "nature": "Đó là sự nghiện làm việc vô nghĩa (Toxic Hustle) hủy hoại sức khỏe và các mối quan hệ thiêng liêng.", "leverage": "Thiết lập hệ thống vận hành tự động để bạn có thể nghỉ ngơi trọn vẹn 1 tháng mà công ty vẫn tăng trưởng.", "mantra": "Kinh doanh hướng tới tự do — Gia đình sum họp ấm no tháng ngày"}
        ],
        "environment": {
            "title": "Thiết lập môi trường làm việc số hóa tự động",
            "items": [
                ("1. Bảng điều khiển quản lý tác vụ AI", "Tập hợp các đường link prompt và workflow tự động vào một trang Notion trung tâm."),
                ("2. Micro đàm thoại chất lượng cao để voice-to-text", "Nói suy nghĩ của bạn vào micro để AI tự động chuyển thành dàn ý văn bản thay vì gõ phím cọc cạch."),
                ("3. Màn hình phụ theo dõi các luồng tự động hóa", "Màn hình dọc hiển thị trạng thái xử lý tác vụ của các AI Agent trong thời gian thực.")
            ],
            "mantra": "Nói thành văn bản tức thì — Hệ thống tự chạy việc gì cũng xong"
        },
        "emotional": {
            "title": "Quản trị tâm lý khi chuyển giao quyền lực cho hệ thống",
            "items": [
                ("1. Từ bỏ nỗi ám ảnh muốn tự tay làm mọi việc", "Học cách chấp nhận công việc được hoàn thành 80% chuẩn mực bởi người khác hoặc AI hơn là 100% bởi chính bạn."),
                ("2. Dũng cảm đối diện với khoảng trống thời gian", "Khi đã giải phóng được thời gian, đừng vội vã lấp đầy bằng việc vặt khác; hãy dùng thời gian đó để tư duy chiến lược."),
                ("3. Giữ tâm trí bình an trước làn sóng công nghệ mới", "Không hoang mang trước hàng ngàn công cụ AI ra mắt mỗi ngày; chỉ tập trung vào những gì phục vụ mục tiêu cốt lõi.")
            ],
            "mantra": "Buông tay cho máy làm thay — Tâm an trí sáng dựng xây cơ đồ"
        }
    },

    # 09. Teach and Grow Rich (0OY6LKEZIPQ)
    {
        "id": raw_vids[9]['id'],
        "slug": "how-to-teach-and-grow-rich-business-model-podcast.html",
        "ep_code": "OE09",
        "cat_badge": "01 / ĐÓNG GÓI TRI THỨC & ĐỊNH GIÁ CAO CẤP",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "DẠY HỌC ĐỂ LÀM GIÀU: MÔ HÌNH KINH DOANH GIÁO DỤC CHUYỂN ĐỔI CAO",
        "orig_title": raw_vids[9]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[9]['id']}",
        "publish_date": raw_vids[9]['date'],
        "raw_date": f"{raw_vids[9]['raw_date'][:4]}-{raw_vids[9]['raw_date'][4:6]}-{raw_vids[9]['raw_date'][6:]}",
        "duration": "50 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Dạy người vượt khó thoát nghèo — Phúc tài tích lũy dạt dào niềm vui",
        "lead_points": [
            "Mô hình kinh doanh vĩ đại nhất trong thế kỷ 21 không phải là sản xuất hàng hóa vật lý cồng kềnh, mà là 'Kinh doanh Giáo dục & Chuyển giao Năng lực' (Education Business Model) với biên lợi nhuận ròng lên tới 85–90%.",
            "Omar hướng dẫn cấu trúc một bài giảng chuẩn mực có tính chuyển đổi: Biến kiến thức phức tạp thành sơ đồ 3 bước dễ hiểu, giúp học viên thực hành được ngay trong 15 phút."
        ],
        "hero_summary": {
            "title": "Khung vận hành cỗ máy đào tạo chuyển giao tri thức",
            "items": [
                ("1. Biên lợi nhuận vô song (85–90%)", "Không chi phí kho bãi, không hỏng hóc hàng tồn; sản phẩm trí tuệ có thể nhân bản vô hạn với chi phí cận biên bằng 0."),
                ("2. Đơn giản hóa kiến thức chuyên sâu", "Người thầy vĩ đại không phải người nói những từ đao to búa lớn, mà là người có khả năng giải thích vấn đề phức tạp cho một đứa trẻ 10 tuổi hiểu."),
                ("3. Tạo ra sự chuyển hóa hành vi", "Không dạy lý thuyết suông; mỗi bài học phải gắn liền với một kết quả đầu ra cụ thể có thể kiểm chứng.")
            ],
            "mantra": "Biên lợi nhuận cao thênh thang — Trao đi tri thức bạc vàng sinh sôi"
        },
        "delusion": {
            "title": "ẢO TƯỞNG PHẢI CÓ BẰNG CẤP SƯ PHẠM & SỰ THẬT VỀ KẾT QUẢ THỰC CHIẾN",
            "desc": "Nhiều người có chuyên môn xuất sắc nhưng không dám mở lớp dạy vì tự ti không có bằng sư phạm. Trong nền kinh tế tri thức hiện đại, học viên chỉ quan tâm bạn đã tự tay làm được kết quả đó chưa và có chỉ lại cho họ được không.",
            "compare_left": {
                "badge": "TƯ DUY HÀN LÂM CŨ",
                "title": "Đòi hỏi chứng chỉ và bằng cấp học thuật",
                "text": "Nghĩ rằng phải học thêm thạc sĩ, tiến sĩ mới đủ tư cách đứng lớp chia sẻ kinh nghiệm."
            },
            "compare_right": {
                "badge": "CHUẨN MỰC THỰC CHIẾN",
                "title": "Chứng minh bằng kết quả thực tế của bản thân",
                "text": "Khán giả trả tiền cho người đã thực sự lăn lộn chiến trường và đúc kết thành bí quyết sống còn."
            },
            "matrix_title": "So sánh Giáo dục Hàn lâm và Giáo dục Chuyển hóa Thực chiến",
            "matrix_items": [
                ("Giáo dục hàn lâm truyền thống", "• Nặng về lý thuyết trừu tượng, mất hàng năm trời nhưng không áp dụng được vào kiếm tiền.<br>• Người dạy thường chưa từng kinh doanh thành công ngoài đời thực."),
                ("Giáo dục chuyển hóa thực chiến", "• Đi thẳng vào thực hành, giải quyết các bài toán cơm áo gạo tiền cấp bách.<br>• Học viên thấy ngay kết quả sau từng bài học.")
            ],
            "mantra": "Bằng cấp dẫu có trên bàn — Thực chiến không có muôn vàn hư danh"
        },
        "insights": [
            {"num": 1, "meta": "BIÊN LỢI NHUẬN", "title": "Mô hình kinh doanh có biên lợi nhuận cao nhất thế giới", "ground_truth": "Kinh doanh hàng vật lý chịu biên lợi nhuận mỏng 10–15%, trong khi kinh doanh tri thức đạt 85–95%.", "surface": "Đổ tiền ôm hàng nghìn sản phẩm tồn kho rồi đau đầu lo phí thuê mặt bằng.", "nature": "Sản phẩm số (Digital Assets) được tạo ra một lần và bán lại hàng ngàn lần mà không tốn thêm chi phí nguyên vật liệu.", "leverage": "Đóng gói toàn bộ kinh nghiệm tích lũy thành khóa học trực tuyến và chương trình cố vấn.", "mantra": "Sản phẩm trí tuệ tạo ra — Bán đi ngàn bận chẳng hao một phần"},
            {"num": 2, "meta": "NGHỆ THUẬT ĐƠN GIẢN", "title": "Năng lực đơn giản hóa là thước đo đỉnh cao của chuyên gia", "ground_truth": "Người nói khó hiểu không phải vì họ quá giỏi, mà vì chính họ chưa thực sự thấu suốt vấn đề.", "surface": "Dùng các thuật ngữ chuyên ngành tiếng Anh để tỏ ra nguy hiểm trước học viên.", "nature": "Bộ não con người ghét sự phức tạp; khi không hiểu, họ sẽ đóng cửa tiếp nhận và bỏ đi.", "leverage": "Dùng các phép so sánh ẩn dụ bình dân quen thuộc để giải thích các khái niệm kỹ thuật.", "mantra": "Nói sao cho trẻ cũng thông — Đó là đỉnh cội của dòng chuyên gia"},
            {"num": 3, "meta": "DẠY ĐỂ HỌC SÂU", "title": "Dạy học là cách học tập nhanh nhất thế giới", "ground_truth": "Theo Tháp học tập (Learning Pyramid), bạn chỉ nhớ 10% những gì đọc được nhưng nhớ tới 90% khi dạy lại cho người khác.", "surface": "Chỉ đọc sách một mình và nghĩ rằng mình đã nắm vững kiến thức.", "nature": "Khi phải dạy lại cho người khác, não bộ bắt buộc phải hệ thống hóa và lấp đầy mọi lỗ hổng tư duy.", "leverage": "Mỗi khi học được một điều mới, hãy lập tức bật máy quay và làm một video chia sẻ lại.", "mantra": "Dạy người là cách học sâu — Tri thức ngấm chặt vào đầu bền lâu"},
            {"num": 4, "meta": "THƯƠNG HIỆU HỌC TẬP", "title": "Thu hút khán giả qua hành trình học tập công khai (Learn in Public)", "ground_truth": "Mọi người thích theo dõi một người đang nỗ lực học tập và tiến bộ từng ngày hơn là một bức tượng đài hoàn hảo.", "surface": "Đợi đến khi trở thành số 1 mới dám mở miệng chia sẻ.", "nature": "Sự đồng hành từ những bước đi chập chững ban đầu tạo nên sợi dây liên kết lòng trung thành bền chặt nhất.", "leverage": "Chia sẻ những cuốn sách bạn đọc mỗi tuần và những thử nghiệm thực tế có cả thất bại.", "mantra": "Công khai từng bước đi lên — Khán giả chứng kiến vững bền theo sau"},
            {"num": 5, "meta": "QUY TRÌNH HÓA THÀNH CÔNG", "title": "Biến trực giác thành công thức có thể sao chép", "ground_truth": "Học viên không thể học theo 'cảm giác' của bạn; họ cần các bước 1-2-3 rõ ràng.", "surface": "Dạy học theo kiểu 'Tôi làm thế này thấy hợp thì làm theo'.", "nature": "Học viên cần một khuôn mẫu có cấu trúc để họ có thể tự tin áp dụng vào hoàn cảnh riêng của họ.", "leverage": "Đặt tên cho phương pháp của bạn (ví dụ: 'Quy trình 3 nhịp', 'Khung 4 bước') để tăng tính bảo chứng.", "mantra": "Công thức đúc kết rõ ràng — Học viên tiếp bước dễ dàng làm theo"},
            {"num": 6, "meta": "ĐỊNH VỊ GIÁ TRỊ", "title": "Đừng bao giờ dạy miễn phí những điều có thể thay đổi cuộc đời họ", "ground_truth": "Con người không bao giờ trân trọng những thứ họ nhận được quá dễ dàng mà không tốn công sức.", "surface": "Tặng không toàn bộ các khóa học chuyên sâu vì nghĩ làm vậy là làm phúc.", "nature": "Khi không trả tiền, học viên không có sự cam kết (Skin in the game) và sẽ không bao giờ hành động để có kết quả.", "leverage": "Cung cấp nội dung 'Cái gì' (What) miễn phí trên YouTube, nhưng thu phí cao cho phần 'Làm như thế nào' (How) và sự đồng hành.", "mantra": "Thu phí là tạo quyết tâm — Khách dồn năng lực tháng năm đổi đời"},
            {"num": 7, "meta": "NUÔI DƯỠNG CỘNG ĐỒNG", "title": "Biến học viên thành những người truyền giáo tự nhiên", "ground_truth": "Lời giới thiệu từ một học viên đã thay đổi cuộc đời có sức mạnh hơn triệu USD tiền quảng cáo.", "surface": "Chăm sóc qua loa sau khi khóa học kết thúc.", "nature": "Cộng đồng cựu học viên thành đạt là tài sản vô giá bảo chứng cho sự nghiệp đào tạo của bạn.", "leverage": "Tạo mạng lưới cựu học viên để họ tiếp tục giao lưu và hỗ trợ các khóa học viên mới.", "mantra": "Học viên thành đạt rạng danh — Tự nhiên truyền tụng mối tình thầy trò"},
            {"num": 8, "meta": "PHỤNG SỰ XÃ HỘI", "title": "Nghề dạy học là nghề tích lũy phước báu lớn nhất", "ground_truth": "Không có niềm vui nào lớn hơn khi nhận được tin nhắn: 'Khóa học của anh đã cứu sống doanh nghiệp và gia đình em'.", "surface": "Chỉ nhìn vào số tiền thu được sau mỗi đợt khai giảng.", "nature": "Sự thỏa mãn tinh thần từ việc nâng đỡ cuộc đời người khác là liều thuốc dưỡng tâm tối thượng cho doanh nhân.", "leverage": "Luôn giữ tâm nguyện phụng sự trong từng bài giảng, tiền bạc sẽ tự đến như một quy luật nhân quả tất yếu.", "mantra": "Nâng bước bao kiếp con người — Phúc dày lộc lớn sáng ngời tương lai"}
        ],
        "environment": {
            "title": "Bố trí không gian giảng dạy chuyên nghiệp",
            "items": [
                ("1. Bảng vẽ điện tử hoặc màn hình tương tác", "Vừa nói vừa vẽ sơ đồ trực tiếp lên màn hình giúp học viên tiếp thu thông tin đa giác quan."),
                ("2. Ghế ngồi công thái học hỗ trợ cột sống", "Đảm bảo tư thế ngồi thẳng thớm, mở rộng lồng ngực để hơi thở sâu và giọng nói vang khỏe suốt buổi dạy."),
                ("3. Ánh sáng chiếu sáng từ trên xuống và hai bên", "Loại bỏ bóng đổ dưới mắt, giúp khuôn mặt luôn rạng rỡ và tràn đầy năng lượng tích cực.")
            ],
            "mantra": "Bảng vẽ tay chỉ đường đi — Ánh sáng rạng rỡ giảng tri thức vàng"
        },
        "emotional": {
            "title": "Tâm thế của người thầy mẫu mực",
            "items": [
                ("1. Lấy sự thành công của học viên làm thước đo danh dự", "Không bao giờ giấu nghề; đem hết ruột gan chia sẻ những gì tinh túy nhất cho học trò."),
                ("2. Giữ sự khiêm nhường trước biển tri thức", "Luôn tự nhắc nhở bản thân cũng chỉ là người đi trước vài bước, không tự mãn coi mình là toàn năng."),
                ("3. Kiên nhẫn với những học viên tiếp thu chậm", "Mỗi bông hoa có thời điểm nở rộ riêng; nhiệm vụ của người thầy là kiên trì tưới nước và chăm bón.")
            ],
            "mantra": "Ruột gan dốc hết trao đi — Khiêm nhường học hỏi ngại gì gian nan"
        }
    },

    # 10. Start Teaching Millionaire (kmlHGVjub_k)
    {
        "id": raw_vids[10]['id'],
        "slug": "how-to-become-a-millionaire-start-teaching-podcast.html",
        "ep_code": "OE10",
        "cat_badge": "01 / ĐÓNG GÓI TRI THỨC & ĐỊNH GIÁ CAO CẤP",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "TRỞ THÀNH TRIỆU PHÚ BẰNG CÁCH ĐÀO TẠO VÀ CHUYỂN GIAO NĂNG LỰC",
        "orig_title": raw_vids[10]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[10]['id']}",
        "publish_date": raw_vids[10]['date'],
        "raw_date": f"{raw_vids[10]['raw_date'][:4]}-{raw_vids[10]['raw_date'][4:6]}-{raw_vids[10]['raw_date'][6:]}",
        "duration": "38 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Chuyển giao năng lực cho người — Đường lên triệu phú sáng ngời bước chân",
        "lead_points": [
            "Bí mật tài chính lớn nhất của thời đại thông tin: Những người kiếm được nhiều tiền nhất không phải là người trực tiếp làm việc chuyên môn, mà là người biết cách dạy lại quy trình đó cho người khác.",
            "Omar bóc tách con đường từ một người quay phim tự do (Freelancer) chật vật kiếm ăn trở thành triệu phú nhờ việc đóng gói kinh nghiệm làm video thành các chương trình huấn luyện toàn cầu."
        ],
        "hero_summary": {
            "title": "Lộ trình chuyển đổi từ Thợ lành nghề sang Chủ doanh nghiệp Đào tạo",
            "items": [
                ("1. Vượt qua bẫy Freelancer", "Làm dịch vụ đơn lẻ (Done-for-you) khiến bạn bị trói chặt vào thời gian; chuyển sang đào tạo (Done-with-you) giải phóng 80% sức lao động."),
                ("2. Chuẩn hóa kinh nghiệm thành tài sản sở hữu trí tuệ", "Mọi mẹo vặt, kỹ thuật xử lý sự cố đều có thể viết thành quy trình SOP bán được giá cao."),
                ("3. Xây dựng thương hiệu chuyên gia đào tạo", "Định vị bản thân là người thầy của những người làm nghề, nắm giữ vị thế cao nhất trong chuỗi giá trị.")
            ],
            "mantra": "Thợ lành nghề bước sang trang — Làm thầy chỉ lối vẻ vang muôn phần"
        },
        "delusion": {
            "title": "ẢO TƯỞNG DẤU NGHỀ VÌ SỢ MẤT KHÁCH & SỰ THẬT VỀ TẦM ẢNH HƯỞNG",
            "desc": "Tâm lý tiểu nông thường sợ rằng nếu dạy hết bí quyết cho người khác thì học trò sẽ cướp mất mối làm ăn của mình. Thực tế hoàn toàn ngược lại: Càng công khai chia sẻ bí quyết, bạn càng củng cố vị thế chuyên gia số 1 mà không ai có thể thay thế.",
            "compare_left": {
                "badge": "TÂM LÝ SỢ HÃI",
                "title": "Giấu kín bí quyết làm ăn trong bóng tối",
                "text": "Sợ người khác học lỏm nên không dám làm nội dung chia sẻ chuyên sâu, suốt đời chỉ quanh quẩn làm việc chân tay."
            },
            "compare_right": {
                "badge": "TÂM THÁI TRIỆU PHÚ",
                "title": "Công khai chia sẻ toàn bộ phương pháp đỉnh cao",
                "text": "Hiểu rằng thông tin là miễn phí, nhưng người ta trả tiền để được chính bạn dẫn dắt và sửa lỗi thực tế."
            },
            "matrix_title": "So sánh Người làm nghề giấu nghề và Chuyên gia đào tạo",
            "matrix_items": [
                ("Người giấu nghề", "• Thu nhập bị giới hạn bởi số giờ làm việc trong ngày.<br>• Tuổi tác càng cao, sức khỏe càng giảm thì thu nhập càng teo tóp."),
                ("Chuyên gia đào tạo phóng khoáng", "• Đào tạo ra hàng trăm đệ tử giỏi, mở rộng tầm ảnh hưởng khắp thị trường.<br>• Thu nhập thụ động tăng theo cấp số nhân nhờ uy tín bảo chứng.")
            ],
            "mantra": "Giấu nghề mòn mỏi thân côi — Dạy người tỏa sáng trọn đời vẻ vang"
        },
        "insights": [
            {"num": 1, "meta": "BƯỚC NGOẶT VỊ THẾ", "title": "Dịch chuyển từ 'Người làm' sang 'Người chỉ đường'", "ground_truth": "Trong mọi ngành nghề, người đào tạo luôn có vị thế xã hội và thu nhập cao hơn người thừa hành.", "surface": "Tiếp tục nhận các dự án gia công giá rẻ với khách hàng khó tính.", "nature": "Làm thuê dịch vụ khiến bạn luôn ở thế dưới bị khách hàng săm soi từng chi tiết.", "leverage": "Tuyên bố chuyển sang vai trò Cố vấn & Đào tạo: Dạy cho các doanh nghiệp cách tự làm nội dung chuyên nghiệp.", "mantra": "Bước lên vị thế chỉ đường — Thoát ly kiếp thợ muôn đường vinh hoa"},
            {"num": 2, "meta": "QUY LUẬT NHÂN BẢN", "title": "Nhân bản tri thức không làm suy giảm giá trị của bạn", "ground_truth": "Lửa từ một ngọn nến có thể thắp sáng hàng ngàn ngọn nến khác mà không hề làm ngọn nến gốc lụi tàn.", "surface": "Nơm nớp lo sợ học trò giỏi hơn thầy sẽ cạnh tranh trực tiếp với mình.", "nature": "Thành công của học trò chính là bảo chứng đắt giá nhất nâng tầm uy tín của người thầy lên một tầm cao mới.", "leverage": "Hỗ trợ học viên xuất sắc nhất mở doanh nghiệp riêng và sẵn sàng kết nối hợp tác win-win.", "mantra": "Thắp ngàn ngọn nến sáng ngời — Ngọn nến ban đầu vẫn rạng muôn nơi"},
            {"num": 3, "meta": "ĐÓNG GÓI BẢN QUYỀN", "title": "Bản quyền trí tuệ là cỗ máy in tiền tự động", "ground_truth": "Những người giàu nhất thế giới đều sở hữu tài sản trí tuệ (Sách, Giáo trình, Bằng sáng chế).", "surface": "Bán thời gian từng giờ cho khách hàng.", "nature": "Thời gian bán đi là mất vĩnh viễn; tài sản trí tuệ bán đi vẫn thuộc quyền sở hữu của bạn.", "leverage": "Tập hợp các video bài giảng và tài liệu thành một hệ thống giáo trình có bản quyền thương hiệu.", "mantra": "Tài sản trí tuệ trong tay — Bán đi ngàn bận tháng ngày sinh sôi"},
            {"num": 4, "meta": "CHUYỂN ĐỔI KHÁN GIẢ", "title": "Mỗi video chia sẻ kiến thức là một buổi phỏng vấn tuyển sinh", "ground_truth": "Khán giả xem các video hướng dẫn tỉ mỉ của bạn sẽ tự khắc muốn đăng ký học chương trình chuyên sâu.", "surface": "Làm nội dung vô thưởng vô phạt chỉ để câu view giải trí.", "nature": "Nội dung mang tính giáo dục sâu sắc là công cụ xây dựng lòng tin mạnh mẽ nhất từng được phát minh.", "leverage": "Mỗi video đều giải quyết triệt để 1 khúc mắc kỹ thuật để chứng minh trình độ sư phạm vượt trội.", "mantra": "Chia sẻ thấu đáo tận tình — Khán giả xin học gửi mình niềm tin"},
            {"num": 5, "meta": "XÂY DỰNG HỆ SINH THÁI", "title": "Hệ sinh thái sản phẩm từ miễn phí đến cao cấp", "ground_truth": "Không thể bắt người lạ vừa gặp lần đầu chi ngay $5.000 cho bạn.", "surface": "Chỉ có duy nhất 1 sản phẩm giá cao và không có gì khác.", "nature": "Khách hàng cần thời gian làm quen và trải nghiệm các nấc thang giá trị nhỏ trước khi đưa ra quyết định lớn.", "leverage": "Xây dựng phễu: Video YouTube miễn phí -> Ebook $27 -> Khóa học $497 -> Coaching $5.000.", "mantra": "Bậc thang từng bước đi lên — Dẫn dắt người bước vững bền tiến xa"},
            {"num": 6, "meta": "NÂNG TẦM DIỄN ĐẠT", "title": "Luyện tập kỹ năng nói trước đám đông mỗi ngày", "ground_truth": "Khả năng ăn nói lưu loát, truyền cảm hứng là kỹ năng kiếm tiền quan trọng nhất của người làm đào tạo.", "surface": "Nghĩ rằng chỉ cần có kiến thức trong đầu là tự nhiên nói hay.", "nature": "Khẩu khí và nhịp điệu phát âm cần được rèn luyện cơ bắp như một vận động viên thể thao.", "leverage": "Quay video nói chuyện 15 phút mỗi ngày mà không nhìn kịch bản để rèn luyện tư duy ngôn ngữ nhanh nhạy.", "mantra": "Khẩu khí luyện tập hằng ngày — Lời vàng ngọc thốt đong đầy yêu thương"},
            {"num": 7, "meta": "TỰ ĐỘNG TUYỂN SINH", "title": "Xây dựng hệ thống tiếp thị tự động thu hút học viên", "ground_truth": "Người thầy không nên dành thời gian đi gõ cửa từng nhà để xin người ta vào học.", "surface": "Đi nhắn tin làm phiền từng người lạ trong các hội nhóm Facebook.", "nature": "Sự chào mời rẻ rúng phá hủy hoàn toàn vị thế tôn nghiêm của một người thầy.", "leverage": "Dùng video YouTube chất lượng cao làm kênh hút tự nhiên, để học viên tự động tìm đến xin tư vấn.", "mantra": "Hữu xạ tự nhiên hương bay — Học viên tìm tới ngày ngày đông vui"},
            {"num": 8, "meta": "MỤC TIÊU TRIỆU PHÚ", "title": "Triệu phú đích thực là người tạo ra những triệu phú khác", "ground_truth": "Thước đo thành công cao nhất của một người thầy là số lượng học trò vượt qua chính mình.", "surface": "Tự mãn với danh xưng triệu phú của riêng mình.", "nature": "Khi bạn giúp được 10 người trở thành triệu phú, bạn sẽ tự động trở thành đa triệu phú bền vững.", "leverage": "Dành toàn bộ tâm huyết hỗ trợ thế hệ học trò kế cận vươn lên đỉnh cao của ngành nghề.", "mantra": "Giúp người thành đạt vẻ vang — Đời mình rực rỡ muôn vàn vinh hoa"}
        ],
        "environment": {
            "title": "Bố trí studio đào tạo triệu đô",
            "items": [
                ("1. Hai góc máy quay (Wide & Close-up)", "Góc rộng để thấy toàn cảnh không gian uy nghi; góc cận để truyền tải cảm xúc chân thành qua ánh mắt."),
                ("2. Màn hình Monitor kiểm tra khung hình ngay trước mặt", "Đảm bảo trang phục, nét mặt và góc máy luôn ở trạng thái hoàn hảo nhất trước khi bấm máy."),
                ("3. Bàn làm việc đứng (Standing Desk)", "Đứng giảng bài giúp năng lượng cơ thể cao hơn 30% so với ngồi, giọng nói phát ra đầy uy lực và nhiệt huyết.")
            ],
            "mantra": "Đứng thẳng giảng dạy hiên ngang — Khí chất ngời ngời muôn vàn truyền trao"
        },
        "emotional": {
            "title": "Nuôi dưỡng tâm thế người truyền cảm hứng vĩ đại",
            "items": [
                ("1. Yêu thương học trò như người thân trong gia đình", "Xem sự tiến bộ của họ là niềm tự hào lớn nhất của cuộc đời mình."),
                ("2. Không nản lòng trước những trường hợp cá biệt", "Giữ vững niềm tin vào tiềm năng vô hạn của con người dù xuất phát điểm của họ có khó khăn đến đâu."),
                ("3. Giữ trọn ngọn lửa đam mê với nghề", "Mỗi lần bước lên bục giảng là một lần cống hiến hết mình như thể đó là bài giảng cuối cùng trong đời.")
            ],
            "mantra": "Trọn vẹn tâm huyết trao đi — Yêu thương soi sáng đường đi muôn người"
        }
    }
]

BATCH_1.extend(eps)

with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch1.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
"""
episodes_batch1.py
Batch 1: 10 Episodes (OE01 - OE10)
"""

BATCH_1 = ''' + json.dumps(BATCH_1, ensure_ascii=False, indent=4) + '\n')

print(f"Hoàn tất 100% episodes_batch1.py với đầy đủ {len(BATCH_1)} tập!")
