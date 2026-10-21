/* =========================================================
   MANIFEST — thêm / đổi tên trang tại đây, menu tự cập nhật.
   id        : trùng với <body data-page="...">
   file      : đường dẫn từ thư mục gốc trung-tam-kenh/
   stage     : tên biến màu trong style.css (--c-xxx)
   q         : câu hỏi mà chặng này trả lời (hiện ở bản đồ + thanh trên)
   ========================================================= */
window.HUB = {
  name: "Trung tâm Logic Xây Kênh",
  sub: "Từ tư duy → định dạng → thực hành",
  groups: [
    { id: "flow", title: "Hành trình (đọc theo thứ tự)" },
    { id: "ref",  title: "Tra cứu & Dữ liệu" }
  ],
  pages: [
    { id: "index",       file: "index.html",         group: "flow", n: "00", title: "Trung Tâm Logic Xây Kênh", short: "Trang chủ", stage: "ink", icon: "🧭", q: "— TRUNG TÂM TRI THỨC XÂY KÊNH & BẢN CHẤT NIỀM TIN • NGUYỄN ĐỨC VIỆT" },
    { id: "tu-duy",      file: "01-tu-duy.html",     group: "flow", n: "01", title: "Tư duy gốc: thương hiệu là hệ quả", short: "Tư duy", stage: "tuduy", icon: "🧠", q: "Vì sao làm kênh? Thương hiệu cá nhân thật sự là gì?" },
    { id: "bat-dau",     file: "02-bat-dau.html",    group: "flow", n: "02", title: "Bắt đầu từ đâu", short: "Bắt đầu", stage: "batdau", icon: "🚪", q: "Tôi là ai, có gì để quay, tuần đầu làm gì?" },
    { id: "logic-kenh",  file: "03-logic-kenh.html",   group: "flow", n: "03", title: "Logic xây kênh", short: "Logic kênh", stage: "logic", icon: "🧩", q: "View → niềm tin → khách tự chốt vận hành thế nào?" },
    { id: "niem-tin",    file: "04-niem-tin.html",   group: "flow", n: "04", title: "Logic niềm tin & storytelling vi mô", short: "Niềm tin", stage: "niemtin", icon: "🤝", q: "Nói thế nào để người xem tin ngay?" },
    { id: "dinh-dang",   file: "05-dinh-dang.html",  group: "flow", n: "05", title: "4 định dạng video + chuyển cảnh", short: "Định dạng", stage: "dinhdang", icon: "🎬", q: "Quay kiểu nào trước, kiểu nào sau?" },

    // Các trang định dạng trực thuộc Chặng 05 (Bản 1.0 gốc)
    { id: "voice-over",   file: "dinh-dang/voice-over.html",   group: "flow", parent: "dinh-dang", sub: true, n: "5.1", title: "Voice-Over & thao tác tay", short: "Voice-Over", stage: "dinhdang", icon: "🎙️", q: "Chưa dám lộ mặt?" },
    { id: "walk-and-talk",file: "dinh-dang/walk-and-talk.html",group: "flow", parent: "dinh-dang", sub: true, n: "5.2", title: "Walk & Talk", short: "Walk & Talk", stage: "dinhdang", icon: "🚶", q: "Nói cứng, cần tự nhiên?" },
    { id: "talking-head", file: "dinh-dang/talking-head.html", group: "flow", parent: "dinh-dang", sub: true, n: "5.3", title: "Talking Head", short: "Talking Head", stage: "dinhdang", icon: "🗣️", q: "Cần dựng uy tín chuyên gia?" },
    { id: "storytelling", file: "dinh-dang/storytelling.html", group: "flow", parent: "dinh-dang", sub: true, n: "5.4", title: "Storytelling 2.5", short: "Storytelling", stage: "dinhdang", icon: "📖", q: "Chạm đúng chỗ đau giấu kín?" },
    { id: "chuyen-canh",  file: "dinh-dang/chuyen-canh.html",  group: "flow", parent: "dinh-dang", sub: true, n: "5.5", title: "Chuyển cảnh (chất keo)", short: "Chuyển cảnh", stage: "dinhdang", icon: "⚡", q: "Video giật, mất người xem?" },
    { id: "vo-boc-31",    file: "dinh-dang/vo-boc-31.html",    group: "flow", parent: "dinh-dang", sub: true, n: "5.6", title: "31 vỏ bọc video tạo lead", short: "31 vỏ bọc", stage: "dinhdang", icon: "🎭", q: "Nghĩ gì để quay hôm nay?" },

    // Chặng 05 (Bản 2.0 Mới Nhất — Tách riêng để đối chiếu trực tiếp với mục cũ)
    { id: "dinh-dang-2",     file: "05-dinh-dang-2.0.html",          group: "flow", n: "2.0", title: "4 định dạng video và chuyển cảnh 2.0", short: "Định dạng 2.0", stage: "dinhdang", icon: "🎬", v2: true, q: "Bản nâng cấp 2.0: 4 Định dạng, Chuyển cảnh, Bố cục Cinematic, Ví dụ & Slide .html" },
    { id: "voice-over-2",    file: "dinh-dang/voiceover3.0.html",    group: "flow", parent: "dinh-dang-2", sub: true, n: "2.1", title: "Voice-Over & thao tác tay 2.0", short: "Voice-Over 2.0", stage: "dinhdang", icon: "🎙️", v2: true, q: "Bản 3.0/2.0: Dựng hình trước, lồng tiếng sau + Studio 6 thực hành cảnh trám 3 lớp" },
    { id: "walk-and-talk-2", file: "dinh-dang/walkntalk2.0.html",    group: "flow", parent: "dinh-dang-2", sub: true, n: "2.2", title: "Walk & Talk 2.0", short: "Walk & Talk 2.0", stage: "dinhdang", icon: "🚶", v2: true, q: "Bản 2.0: Quy tắc 3 trục 45°, giải phẫu 7 video mẫu & 5 bài tập nhóm 2 người" },
    { id: "talking-head-2",  file: "dinh-dang/talkinghead2.0.html",  group: "flow", parent: "dinh-dang-2", sub: true, n: "2.3", title: "Talking Head 2.0", short: "Talking Head 2.0", stage: "dinhdang", icon: "🗣️", v2: true, q: "Bản 2.0 MasterClass: Mặt để tin, Cảnh để hiểu, Nhịp để xem hết + 10 kịch bản ngành" },
    { id: "storytelling-2",  file: "dinh-dang/storytelling2.0.html", group: "flow", parent: "dinh-dang-2", sub: true, n: "2.4", title: "Storytelling 2.5 (2.0)", short: "Storytelling 2.0", stage: "dinhdang", icon: "📖", v2: true, q: "Bản 2.0: Kể lát cắt 5 giây & Giữ thể diện cho người xem (T1 → T2 → T2.5 → T3)" },
    { id: "chuyen-canh-2",   file: "dinh-dang/chuyencanh2.0.html",   group: "flow", parent: "dinh-dang-2", sub: true, n: "2.5", title: "Chuyển cảnh (chất keo) 2.0", short: "Chuyển cảnh 2.0", stage: "dinhdang", icon: "⚡", v2: true, q: "Bản 2.0: Cắt trong chuyển động 70/30, Giống Selfie, Chân máy 30° & Khóa trọng tâm" },
    { id: "bo-cuc-quay-2",   file: "dinh-dang/bocucquay.html",       group: "flow", parent: "dinh-dang-2", sub: true, n: "2.6", title: "Bố cục Cinematic 2.0", short: "Bố cục 2.0", stage: "dinhdang", icon: "🎥", v2: true, q: "Bản 3.0: 6 Trụ cột Đường–Động–Sáng–Giờ–Tĩnh–Vào & Nghệ thuật khoe khéo dịch vụ" },

    // Các trang Thực hành / Ví dụ / Công cụ đi kèm thuộc mục 2.0 (vẫn hiển thị Sidebar Menu trái)
    { id: "walk-and-talk-2-ex", file: "dinh-dang/walkntalkthuchanh.html", group: "flow", parent: "dinh-dang-2", sub: true, hiddenFromMenu: true, activeMenuId: "walk-and-talk-2", v2: true, n: "2.2b", title: "Thực hành Walk & Talk 2.0 (25 Ví dụ & 5 Bài tập)", short: "Bài tập Walk & Talk", stage: "dinhdang", icon: "🎬", q: "5 Bài tập nhóm 2 người • 25 ảnh phân cảnh lệch góc ≥45° • 25 kịch bản lớp K3" },
    { id: "bo-cuc-quay-2-ex",   file: "dinh-dang/bocucquaybaitap.html",   group: "flow", parent: "dinh-dang-2", sub: true, hiddenFromMenu: true, activeMenuId: "bo-cuc-quay-2",   v2: true, n: "2.6b", title: "Bài tập Bố cục Cinematic (3 Cấp độ & 103 Mẫu)", short: "Bài tập Bố cục", stage: "dinhdang", icon: "✍️", q: "Lộ trình 3 cấp độ tại thành phố • Phòng tập tương tác 8 ngành • 103 mẫu bố cục" },
    { id: "voice-over-2-full",  file: "dinh-dang/voiceover2.0.html",      group: "flow", parent: "dinh-dang-2", sub: true, hiddenFromMenu: true, activeMenuId: "voice-over-2",    v2: true, n: "2.1b", title: "Voice-Over 2.0 (Bản đầy đủ 61 Video Khám Kênh)", short: "Voice-Over 61 Video", stage: "dinhdang", icon: "📚", q: "Bản tư liệu đầy đủ 61 video khám kênh thực tế học viên FEDU" },
    { id: "voice-over-1-arch",  file: "dinh-dang/voiceover1.0.html",      group: "flow", parent: "dinh-dang-2", sub: true, hiddenFromMenu: true, activeMenuId: "voice-over-2",    v2: true, n: "2.1c", title: "Voice-Over 1.0 (Bản lưu trữ đối chiếu)", short: "Voice-Over 1.0", stage: "dinhdang", icon: "📜", q: "Bản lưu trữ Voice-Over 1.0 ban đầu" },
    { id: "megaprompt-2",       file: "dinh-dang/megaprompt2.0.html",     group: "flow", parent: "dinh-dang-2", sub: true, hiddenFromMenu: true, activeMenuId: "dinh-dang-2",     v2: true, n: "2.7",  title: "Trung tâm MegaPrompt 2.0 (4 Định dạng)", short: "MegaPrompt 2.0", stage: "dinhdang", icon: "🧰", q: "Cỗ máy AI viết kịch bản theo 4 định dạng video + Lịch 4 bài/tuần" },

    { id: "ky-nang",     file: "06-ky-nang.html",    group: "flow", n: "06", title: "Bản đồ kỹ năng", short: "Kỹ năng", stage: "kynang", icon: "🛠️", q: "Cần giỏi những kỹ năng gì, học ở đâu?" },
    { id: "aieditskill", file: "aieditskill.html",   group: "flow", parent: "ky-nang", sub: true, n: "6.1", title: "Hệ thống Kỹ năng AI Video Edit & 35 Mẫu MFX", short: "AI Edit Skill", stage: "kynang", icon: "🎞️", q: "Hệ thống 10 cụm skill dựng AI, 35 mẫu chữ & bản vẽ 2D vận hành thế nào?" },
    { id: "thuc-hanh",   file: "07-thuc-hanh.html",  group: "flow", n: "07", title: "Lộ trình thực hành", short: "Thực hành", stage: "thuchanh", icon: "🏋️", q: "Tuần 1, tuần 2... làm chính xác việc gì?" },

    { id: "tai-nguyen",  file: "08-tai-nguyen.html", group: "ref", n: "08", title: "Tài nguyên hệ thống & link mở ngay", short: "Tài nguyên", stage: "tainguyen", icon: "🔗", q: "Công cụ nào hỗ trợ bước nào? Bấm vào là ra." },
    { id: "case",        file: "09-case.html",       group: "ref", n: "09", title: "Case study theo ngành", short: "Case", stage: "case", icon: "📚", q: "Ngành của tôi đã có ai làm chưa, làm thế nào?" },
    { id: "hoc-vien",    file: "10-hoc-vien.html",   group: "ref", n: "10", title: "Dữ liệu thật về học viên", short: "Học viên", stage: "dulieu", icon: "📊", q: "Người học thật sự đau ở đâu, sợ gì, cần gì?" },
    { id: "cu", file: "cu/index.html", group: "ref", n: "📜", title: "Bản chuyên khảo cũ (1.0)", short: "Bản cũ 1.0", stage: "ink", icon: "📜", q: "Xem lại toàn văn bản chuyên khảo 1.0 ban đầu" },
    { id: "giao-an",     file: "11-giao-an.html",    group: "ref", n: "11", title: "Giáo án động (bổ sung dữ liệu)", short: "Giáo án", stage: "ink", icon: "🗂️", q: "28 vấn đề, ví dụ, bài tập — và cách tôi thêm vào." }
  ]
};
