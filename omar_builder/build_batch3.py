# -*- coding: utf-8 -*-
"""
build_batch3.py: Tạo episodes_batch3.py chứa 10 tập (OE21 - OE30)
"""
import json

with open('/Users/vietmac/.gemini/antigravity/brain/24deb8b1-3156-43d0-91a1-3246f0cc4078/scratch/omar_40_videos.json') as f:
    raw_vids = {v['idx']: v for v in json.load(f)}

batch3 = [
    # 21. Communication Skills (h8QnMNUXuls)
    {
        "id": raw_vids[21]['id'],
        "slug": "level-up-your-communication-skills-masterclass-podcast.html",
        "ep_code": "OE21",
        "cat_badge": "05 / TÂM LÝ BÁN HÀNG & GIAO TIẾP",
        "speaker": "Omar Eltakrori & Chuyên gia Giao tiếp Đỉnh cao",
        "speaker_role": "Cố vấn Đàm phán Doanh nghiệp & Chuyên gia Tâm lý Đối thoại",
        "tagline": "NÂNG CẤP KỸ NĂNG GIAO TIẾP VÀ ĐỐI THOẠI ĐỈNH CAO TRONG 90 PHÚT",
        "orig_title": raw_vids[21]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[21]['id']}",
        "publish_date": raw_vids[21]['date'],
        "raw_date": f"{raw_vids[21]['raw_date'][:4]}-{raw_vids[21]['raw_date'][4:6]}-{raw_vids[21]['raw_date'][6:]}",
        "duration": "1 giờ 28 phút",
        "read_time": "~9 phút chắt lọc",
        "hero_quote": "Lời nói thấu tỏ tâm can — Mở đường đàm phán muôn vàn hanh thông",
        "lead_points": [
            "Khả năng diễn đạt gãy gọn, truyền tải cảm xúc và lắng nghe chủ động là kỹ năng đòn bẩy số 1 quyết định thu nhập và vị thế lãnh đạo của bạn trong mọi cuộc thương thảo.",
            "Phân tích 3 trụ cột giao tiếp: Điều khiển tông giọng (Vocal Tonality), Sử dụng khoảng lặng chiến lược và Nghệ thuật đặt câu hỏi dẫn dắt không gây phòng thủ."
        ],
        "hero_summary": {
            "title": "Bản đồ nâng cấp năng lực giao tiếp và thu phục lòng người",
            "items": [
                ("1. Tông giọng quyết định 90% cảm xúc", "Nội dung chỉ chiếm 7%; ngữ điệu ấm áp, điềm tĩnh và dứt khoát quyết định mức độ tin tưởng của người nghe."),
                ("2. Nghệ thuật lắng nghe phản chiếu (Mirroring)", "Lặp lại 3 từ khóa cuối cùng của đối tác để tạo ra cảm giác thấu hiểu tức thì."),
                ("3. Kiểm soát nhịp thở và tốc độ nói", "Nói chậm lại 20% so với bình thường để toát lên uy quyền của người nắm thế chủ động.")
            ],
            "mantra": "Giọng trầm chậm rãi uy nghi — Người nghe thấm thía ngại gì cách ngăn"
        },
        "delusion": {
            "title": "ẢO TƯỞNG ĂN NÓI KHÉO LÉO & SỰ THẬT VỀ SỰ CHÂN THÀNH",
            "desc": "Nhiều người lầm tưởng giao tiếp giỏi là phải biết nịnh hót và dùng từ ngữ hoa mỹ. Người khôn ngoan nhận diện sự giả tạo trong tích tắc; giao tiếp đỉnh cao là khả năng nói thật một cách tinh tế và không làm tổn thương người khác.",
            "compare_left": {
                "badge": "LỐI MÒN XÃ GIAO",
                "title": "Dùng kỹ xảo ngôn từ đãi bôi bề nổi",
                "text": "Nói những lời tâng bốc sáo rỗng để lấy lòng người khác nhưng không tạo được mối quan hệ sâu sắc."
            },
            "compare_right": {
                "badge": "GIAO TIẾP CHÂN THỰC",
                "title": "Thấu cảm và lắng nghe từ tận đáy lòng",
                "text": "Đặt toàn bộ sự chú ý vào cảm xúc của đối phương, giúp họ cảm thấy được tôn trọng và thấu hiểu trọn vẹn."
            },
            "matrix_title": "So sánh Xã giao khéo léo và Đối thoại thấu suốt",
            "matrix_items": [
                ("Xã giao đãi bôi", "• Quan hệ hời hợt, dễ tan vỡ khi có xung đột lợi ích.<br>• Luôn cảm thấy mệt mỏi vì phải đeo mặt nạ làm hài lòng mọi người."),
                ("Đối thoại thấu suốt", "• Xây dựng niềm tin vững chắc như bàn thạch.<br>• Giải quyết xung đột êm đẹp, biến đối thủ thành đồng minh.")
            ],
            "mantra": "Khéo léo đãi bôi người chê — Chân thành thấu hiểu người mê trọn đời"
        },
        "insights": [
            {"num": 1, "meta": "TÔNG GIỌNG TRẦM", "title": "Hạ tông giọng ở cuối câu để khẳng định uy quyền", "ground_truth": "Người lên giọng ở cuối câu phát ra tín hiệu bất an và cầu xin sự chấp thuận.", "surface": "Nói chuyện với ngữ điệu đều đều hoặc hay lên giọng ở đuôi câu.", "nature": "Tiềm thức con người liên kết tông giọng trầm đi xuống với sự tự tin và địa vị xã hội cao.", "leverage": "Thực hành hạ tông giọng xuống nửa cung ở từ cuối cùng của mỗi câu khẳng định.", "mantra": "Cuối câu hạ giọng dứt khoát — Uy quyền toát nhẹ định đoạt lòng người"},
            {"num": 2, "meta": "LẮNG NGHE CHỦ ĐỘNG", "title": "Lắng nghe để thấu hiểu, không lắng nghe để trả đũa", "ground_truth": "Đa số mọi người không lắng nghe; họ chỉ đang chờ đối phương dứt lời để nói phần của mình.", "surface": "Ngắt lời người khác ngay khi họ chưa nói hết câu.", "nature": "Sự ngắt lời kích hoạt cảm giác bị coi thường và đóng chặt cánh cửa tiếp nhận thông tin.", "leverage": "Dừng lại 2 giây sau khi đối phương nói xong trước khi bạn bắt đầu cất lời.", "mantra": "Dừng hai giây lắng nghe sâu — Đối phương cảm kích trước sau chung lòng"},
            {"num": 3, "meta": "KHOẢNG LẶNG QUYỀN LỰC", "title": "Sử dụng khoảng lặng để nhấn mạnh thông điệp quan trọng", "ground_truth": "Người sợ khoảng lặng là người thiếu tự tin vào trọng lượng của lời nói mình.", "surface": "Chêm vào vô số từ đệm 'ờ, à, kiểu như' để lấp đầy sự im lặng.", "nature": "Một khoảng lặng 3 giây đúng lúc buộc người nghe phải tập trung toàn bộ tâm trí vào câu nói tiếp theo.", "leverage": "Thay vì nói 'ờ', hãy ngậm miệng và hít một hơi thở sâu bằng mũi.", "mantra": "Lặng im gom hết chú ý — Câu sau thốt nhẹ khắc ghi vào lòng"},
            {"num": 4, "meta": "KẾT NỐI ÁNH MẮT", "title": "Tam giác ánh mắt (Eye Contact Triangle)", "ground_truth": "Né tránh ánh mắt là tín hiệu của sự thiếu trung thực hoặc tự ti.", "surface": "Nhìn chằm chằm vào mắt đối phương không chớp gây cảm giác bị đe dọa.", "nature": "Ánh nhìn ấm áp luân chuyển giữa hai mắt và trán tạo cảm giác an toàn và chân thành.", "leverage": "Duy trì ánh mắt 70% thời lượng cuộc trò chuyện, luân chuyển nhẹ nhàng.", "mantra": "Ánh mắt ấm áp chân thành — Nối liền hai cõi tâm linh tương phùng"},
            {"num": 5, "meta": "NGHỆ THUẬT ĐẶT CÂU HỎI", "title": "Hỏi câu hỏi 'Thế nào' và 'Cái gì' thay vì 'Tại sao'", "ground_truth": "Câu hỏi 'Tại sao' thường kích hoạt tâm lý phòng thủ và tìm lý do biện minh.", "surface": "Hỏi: 'Tại sao anh lại làm như vậy?'.", "nature": "Từ 'Tại sao' mang tính phán xét; từ 'Thế nào' mở ra không gian cùng nhau giải quyết vấn đề.", "leverage": "Đổi thành: 'Điều gì đã dẫn đến quyết định đó và chúng ta có thể làm thế nào để tốt hơn?'.", "mantra": "Đổi câu gỡ nút phòng thủ — Cùng nhau tìm lối thấu suốt nguồn cơn"},
            {"num": 6, "meta": "THỪA NHẬN CẢM XÚC", "title": "Dán nhãn cảm xúc của đối phương (Emotional Labeling)", "ground_truth": "Khi một cảm xúc tiêu cực được gọi đúng tên, cường độ của nó sẽ giảm đi một nửa.", "surface": "Bảo người khác: 'Anh đừng tức giận nữa' (làm họ tức giận hơn).", "nature": "Bảo người khác đừng giận là phủ nhận cảm xúc của họ.", "leverage": "Nói: 'Dường như anh đang cảm thấy rất thất vọng về tiến độ dự án, có phải vậy không?'.", "mantra": "Gọi tên cảm xúc êm đềm — Giận hờn tan biến ấm êm cõi lòng"},
            {"num": 7, "meta": "GIAO TIẾP PHI NGÔN NGỮ", "title": "Mở rộng tư thế cơ thể để giải phóng testosterone", "ground_truth": "Ngôn ngữ cơ thể định hình cảm xúc nội tâm của chính bạn trước khi tác động đến người khác.", "surface": "Khoanh tay trước ngực, gù lưng cúi đầu khi bước vào phòng họp.", "nature": "Tư thế thu mình làm tăng hormone cortisol gây căng thẳng và suy giảm sự tự tin.", "leverage": "Đứng thẳng lưng, mở rộng hai vai, hai bàn tay để mở tự nhiên trên bàn.", "mantra": "Mở rộng hai vai hiên ngang — Tự tin tỏa rạng muôn vàn khí chất"},
            {"num": 8, "meta": "KẾT THÚC ẤN TƯỢNG", "title": "Nguyên lý Đỉnh - Đáy (Peak-End Rule)", "ground_truth": "Người ta chỉ nhớ khoảnh khắc cảm xúc cao trào nhất và cách bạn kết thúc cuộc nói chuyện.", "surface": "Kết thúc cuộc gặp bằng sự vội vã, nhạt nhẽo không có điểm nhấn.", "nature": "Ấn tượng cuối cùng là thứ đọng lại lâu nhất trong ký ức dài hạn của đối tác.", "leverage": "Luôn kết thúc bằng một lời cảm ơn chân thành cụ thể và một cam kết hành động rõ ràng.", "mantra": "Khởi đầu ấn tượng rộn ràng — Kết thúc chu đáo muôn vàn vấn vương"}
        ],
        "environment": {
            "title": "Bố trí không gian đối thoại không rào cản",
            "items": [
                ("1. Ngồi góc 90 độ thay vì đối đầu trực diện", "Tránh đặt một chiếc bàn làm việc to chắn ngang ở giữa; ngồi ghế sofa góc 90 độ tạo cảm giác đồng minh."),
                ("2. Không gian ánh sáng tự nhiên dịu nhẹ", "Tránh đèn huỳnh quang chói mắt gây căng thẳng thần kinh thị giác."),
                ("3. Nhiệt độ phòng mát mẻ 22–24 độ C", "Nhiệt độ dễ chịu giúp nhịp tim ổn định và các cuộc thảo luận không bị nóng nảy.")
            ],
            "mantra": "Ngồi góc đồng minh chan hòa — Không gian mát mẻ nở hoa ân tình"
        },
        "emotional": {
            "title": "Giữ tâm thế bình an và từ bi trong mọi cuộc đối thoại",
            "items": [
                ("1. Không coi người bất đồng ý kiến là kẻ thù", "Xem họ là người đang có một góc nhìn khác cần được lắng nghe và khám phá."),
                ("2. Tách rời sự công kích cá nhân khỏi bản thân", "Khi ai đó tức giận, hiểu rằng họ đang chiến đấu với nỗi đau của chính họ, không phải do bạn."),
                ("3. Luôn giữ nụ cười ấm áp từ ánh mắt", "Nụ cười chân thành là chiếc chìa khóa vạn năng mở toang mọi cánh cửa phòng thủ kiên cố nhất.")
            ],
            "mantra": "Tâm từ bi sáng tựa gương — Nụ cười hóa giải muôn đường phong ba"
        }
    },

    # 22. Hired a Therapist (obiMzzLrgLc)
    {
        "id": raw_vids[22]['id'],
        "slug": "hired-therapist-grow-business-mindset-podcast.html",
        "ep_code": "OE22",
        "cat_badge": "05 / TÂM LÝ BÁN HÀNG & GIAO TIẾP",
        "speaker": "Omar Eltakrori",
        "speaker_role": "Nhà sáng lập, Đạo diễn hình ảnh & Cố vấn Xây dựng Thương hiệu Doanh nhân",
        "tagline": "TRỊ LIỆU TÂM LÝ TRONG KINH DOANH: ĐỐI DIỆN GÓC TỐI VÀ ĐIỂM NGHẼN NỘI TÂM",
        "orig_title": raw_vids[22]['title'],
        "youtube_url": f"https://www.youtube.com/watch?v={raw_vids[22]['id']}",
        "publish_date": raw_vids[22]['date'],
        "raw_date": f"{raw_vids[22]['raw_date'][:4]}-{raw_vids[22]['raw_date'][4:6]}-{raw_vids[22]['raw_date'][6:]}",
        "duration": "1 giờ 11 phút",
        "read_time": "~8 phút chắt lọc",
        "hero_quote": "Doanh nghiệp phản chiếu nội tâm — Chữa lành gốc rễ vững tầm tương lai",
        "lead_points": [
            "Điểm nghẽn lớn nhất kìm hãm sự tăng trưởng của doanh nghiệp không nằm ở chiến lược marketing hay sản phẩm, mà nằm ở những tổn thương tâm lý chưa được chữa lành của người sáng lập.",
            "Omar chia sẻ trải nghiệm thuê chuyên gia trị liệu tâm lý và bị bóc trần hội chứng 'Cầu toàn cưỡng chế' (Perfectionism) và nỗi sợ bị từ chối ngầm định khiến doanh nghiệp dậm chân tại chỗ."
        ],
        "hero_summary": {
            "title": "Bản đồ giải phóng điểm nghẽn tâm lý của nhà sáng lập",
            "items": [
                ("1. Doanh nghiệp là tấm gương của người đứng đầu", "Nỗi sợ tiền bạc, sự ngờ vực nhân viên hay tính kiểm soát thái quá đều bắt nguồn từ chấn thương tuổi thơ."),
                ("2. Sự cầu toàn là vỏ bọc của nỗi sợ xấu hổ", "Trì hoãn ra mắt sản phẩm vì sợ bị chê cười và sợ không hoàn hảo trong mắt người khác."),
                ("3. Phân quyền thực sự đòi hỏi sự buông bỏ kiểm soát", "Không thể nhân bản doanh nghiệp nếu bạn không tin tưởng vào năng lực của đội ngũ cộng sự.")
            ],
            "mantra": "Tâm an doanh nghiệp vững vàng — Tháo gỡ nỗi sợ mở đàng tiến xa"
        },
        "delusion": {
            "title": "ẢO TƯỞNG CỨ CỐ GẮNG CHĂM CHỈ LÀ THÀNH CÔNG & SỰ THẬT VỀ TỰ PHÁ HOẠI",
            "desc": "Nhiều doanh nhân làm việc kiệt sức nhưng cứ đến ngưỡng doanh thu nhất định là công ty lại gặp sự cố hoặc phá sản. Đây là hiện tượng Tự phá hoại tiềm thức (Subconscious Self-Sabotage) do niềm tin giới hạn về tiền bạc.",
            "compare_left": {
                "badge": "LẨM TƯỞNG BỀ NỔI",
                "title": "Nghĩ rằng mình chỉ thiếu kỹ năng kinh doanh",
                "text": "Đi học thêm hàng chục khóa học quản trị nhưng doanh thu vẫn không tăng vì tâm thức bị khóa chặt bởi nỗi sợ giàu có."
            },
            "compare_right": {
                "badge": "TỈNH THỨC NỘI TÂM",
                "title": "Chữa lành niềm tin giới hạn trong tiềm thức",
                "text": "Đối diện với những nỗi sợ sâu kín, cho phép bản thân được xứng đáng đón nhận sự thịnh vượng và hạnh phúc."
            },
            "matrix_title": "So sánh Doanh nhân mắc kẹt nội tâm và Doanh nhân đã chữa lành",
            "matrix_items": [
                ("Mắc kẹt trong chấn thương", "• Nghiện làm việc để trốn tránh cảm giác trống rỗng nội tâm.<br>• Luôn nghi ngờ nhân viên và đẩy những người tài năng ra xa."),
                ("Tâm thức giải phóng tự do", "• Lãnh đạo bằng sự tin tưởng và trao quyền mạnh mẽ.<br>• Doanh nghiệp tăng trưởng vượt bậc trong khi người sáng lập thảnh thơi an yên.")
            ],
            "mantra": "Chữa lành gốc rễ thân tâm — Cơ đồ tự khắc tháng năm đơm hoa"
        },
        "insights": [
            {"num": 1, "meta": "TẤM GƯƠNG DOANH NGHIỆP", "title": "Doanh nghiệp không bao giờ lớn hơn sự trưởng thành tâm lý của bạn", "ground_truth": "Mọi vấn đề lặp đi lặp lại trong công ty đều là tấm gương phản chiếu điểm mù của CEO.", "surface": "Đổ lỗi cho nhân viên lười biếng hoặc thị trường suy thoái.", "nature": "Bạn thu hút và dung túng những hành vi tiêu cực đúng như những gì bạn chưa dám giải quyết bên trong mình.", "leverage": "Khi công ty gặp trục trặc, hãy ngồi tĩnh lặng tự hỏi: 'Phần nào trong tôi đã tạo ra kết quả này?'.", "mantra": "Soi mình vào giữa việc chung — Nhận ra điểm nghẽn ung dung sửa mình"},
            {"num": 2, "meta": "BẪY CẦU TOÀN", "title": "Chủ nghĩa cầu toàn là hình thức tinh vi của sự hèn nhát", "ground_truth": "Bạn không phải người có tiêu chuẩn cao; bạn là người sợ bị phán xét.", "surface": "Tự hào rằng mình là người theo chủ nghĩa hoàn hảo nên video chưa thể đăng.", "nature": "Sự cầu toàn là chiếc khiên chắn giúp bạn né tránh việc bị thị trường chấm điểm thực tế.", "leverage": "Áp dụng tiêu chuẩn 80%: Hoàn thành tốt hơn hoàn hảo, đăng bài và đón nhận phản hồi thực tế.", "mantra": "Cầu toàn vỏ bọc nỗi lo — Buông lơi hoàn hảo tự do cất lời"},
            {"num": 3, "meta": "NGHIỆN KIỂM SOÁT", "title": "Cố gắng kiểm soát mọi việc vì thiếu niềm tin vào cuộc đời", "ground_truth": "CEO ôm đồm mọi việc chi tiết là biểu hiện của sự bất an sâu sắc.", "surface": "Không dám giao quyền quyết định cho cấp dưới vì sợ họ làm sai.", "nature": "Tâm lý muốn kiểm soát bắt nguồn từ cảm giác bất lực trong quá khứ khi bị phản bội hoặc bỏ rơi.", "leverage": "Học cách chấp nhận nhân viên làm sai trong giới hạn ngân sách cho phép để họ tự trưởng thành.", "mantra": "Buông tay kiểm soát nhẹ nhàng — Tin người trao việc mở đàng tiến xa"},
            {"num": 4, "meta": "HỘI CHỨNG CỨU THẾ", "title": "Ngừng đóng vai người hùng đi giải cứu tất cả mọi người", "ground_truth": "Gánh vác trách nhiệm của người khác sẽ biến bạn thành người kiệt sức và biến họ thành kẻ ăn bám.", "surface": "Luôn nhảy vào giải quyết rắc rối cá nhân của nhân viên và khách hàng.", "nature": "Hội chứng người cứu thế (Savior Complex) là cách bạn tìm kiếm cảm giác mình có giá trị.", "leverage": "Trao lại trách nhiệm cho chính chủ thể và chỉ hỗ trợ với tư cách người hướng dẫn từ xa.", "mantra": "Ngừng làm người hùng chở che — Để người tự đứng vẹn bề thành công"},
            {"num": 5, "meta": "GIỚI HẠN XỨNG ĐÁNG", "title": "Nâng trần nhiệt kế tài chính trong tâm thức (Upper Limit Problem)", "ground_truth": "Mỗi người có một ngưỡng chịu đựng sự hạnh phúc và giàu có ngầm định trong não bộ.", "surface": "Vừa kiếm được nhiều tiền xong liền gặp sự cố xe cộ hoặc ốm đau để mất tiền.", "nature": "Tiềm thức cảm thấy tội lỗi khi vượt qua mức sống của cha mẹ hoặc bạn bè đồng trang lứa.", "leverage": "Tập làm quen với cảm giác xứng đáng được hưởng thụ sự sung túc mà không cảm thấy cắn rứt lương tâm.", "mantra": "Xứng đáng đón nhận lộc trời — Mở lòng thênh thang sáng ngời tương lai"},
            {"num": 6, "meta": "ĐỐI DIỆN NỖI CÔ ĐƠN", "title": "Dám ngồi yên một mình trong phòng kín không điện thoại", "ground_truth": "Phần lớn các quyết định kinh doanh sai lầm được đưa ra chỉ để khỏa lấp sự cô đơn và buồn chán.", "surface": "Luôn luôn phải nghe podcast hoặc lướt mạng xã hội mỗi khi rảnh rỗi.", "nature": "Không dám đối diện với những suy nghĩ và cảm xúc thật trong sự tĩnh lặng nội tâm.", "leverage": "Thực hành ngồi tĩnh lặng 15 phút mỗi ngày không làm gì cả, chỉ quan sát hơi thở tự nhiên.", "mantra": "Tĩnh lặng đối diện chính mình — Tâm an trí sáng phân minh tỏ tường"},
            {"num": 7, "meta": "RANH GIỚI BẢO VỆ", "title": "Học cách nói 'Không' mà không cần phải giải thích hay xin lỗi", "ground_truth": "Mỗi lần bạn nói 'Có' với người khác là một lần bạn nói 'Không' với ước mơ và gia đình của mình.", "surface": "Nhận lời tham gia mọi cuộc gặp gỡ vô bổ vì sợ làm mất lòng người khác.", "nature": "Căn bệnh làm hài lòng người khác (People Pleaser) phá hủy toàn bộ sự tập trung chiến lược.", "leverage": "Nói dứt khoát: 'Cảm ơn anh đã nghĩ tới tôi, nhưng hiện tại tôi không thể nhận thêm dự án này'.", "mantra": "Nói không dứt khoát nhẹ nhàng — Giữ gìn thời lượng mở đàng thênh thang"},
            {"num": 8, "meta": "TỰ DO TÂM HỒN", "title": "Bình an nội tại là đỉnh cao cao nhất của sự giàu có", "ground_truth": "Có hàng triệu USD trong tài khoản nhưng đêm nào cũng mất ngủ uống thuốc an thần là một địa ngục trần gian.", "surface": "Đuổi theo những con số tài sản vô tận mà không bao giờ cảm thấy thỏa mãn.", "nature": "Sự đủ đầy thực sự là khi tâm hồn bạn được tự do, không còn bị trói buộc bởi nỗi sợ hãi và lòng tham lam.", "leverage": "Nuôi dưỡng lòng biết ơn mỗi ngày, sống chậm lại và tận hưởng những vẻ đẹp giản dị của cuộc sống.", "mantra": "Tâm an giữa chốn nhân gian — Đó là tài sản muôn vàn quý hơn"}
        ],
        "environment": {
            "title": "Thiết lập không gian trị liệu và tĩnh tâm cá nhân",
            "items": [
                ("1. Đệm ngồi thiền bằng vỏ đậu tự nhiên", "Hỗ trợ xương chậu thẳng, giúp ngồi tĩnh tâm 20 phút mà không bị tê chân hay đau lưng."),
                ("2. Tinh dầu trầm hương hoặc gỗ tuyết tùng tự nhiên", "Mùi hương mộc mạc kích hoạt hệ thần kinh phó giao cảm giúp cơ thể thư giãn sâu sắc."),
                ("3. Chuông xoay Tây Tạng (Singing Bowl)", "Tiếng chuông ngân vang thanh lọc năng lượng tiêu cực tích tụ trong phòng làm việc sau một ngày dài.")
            ],
            "mantra": "Hương trầm thoang thoảng an nhiên — Tiếng chuông thanh tịnh nối liền yêu thương"
        },
        "emotional": {
            "title": "Chữa lành đứa trẻ bên trong nhà lãnh đạo",
            "items": [
                ("1. Ôm lấy đứa trẻ từng bị tổn thương trong quá khứ", "Nói với chính mình rằng: 'Bây giờ tôi đã lớn, tôi an toàn và tôi tự bảo vệ được chính mình'."),
                ("2. Cho phép bản thân được yếu đuối và khóc khi cần", "Khóc không phải là yếu đuối; khóc là sự dũng cảm giải phóng những gánh nặng đè nén quá lâu."),
                ("3. Biết ơn từng vết sẹo cuộc đời", "Những vết sẹo đó chính là huy chương chứng minh bạn đã chiến đấu kiên cường để trưởng thành.")
            ],
            "mantra": "Vết sẹo hóa ngọc lung linh — Tự yêu thương lấy chính mình an vui"
        }
    }
]

BATCH_3 = batch3

# Ghi ra episodes_batch3.py
with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch3.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
"""
episodes_batch3.py
Batch 3: Episodes (OE21 - OE30)
"""

BATCH_3 = ''' + json.dumps(BATCH_3, ensure_ascii=False, indent=4) + '\n')

print(f"Đã tạo episodes_batch3.py với {len(BATCH_3)} tập ban đầu (OE21 - OE22)!")
