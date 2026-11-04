/* =========================================================
   MANIFEST — Cây điều hướng 1 trục duy nhất của kenh.fedu.vn
   Đã loại bỏ nhánh 1.0 trùng lặp, trang Giáo án rỗng & trang Sale nội bộ.
   ========================================================= */
window.HUB = {
  name: "Trung tâm Logic Xây Kênh",
  sub: "Từ tư duy → định dạng → thực hành",
  groups: [
    { id: "flow", title: "Hành trình cốt lõi" },
    { id: "ref",  title: "Kênh thật & Tài nguyên" }
  ],
  pages: [
    { id: "index",       file: "index.html",               group: "flow", n: "00", title: "Trung Tâm Logic Xây Kênh", short: "Trang chủ", stage: "ink", icon: "🧭", q: "— TRUNG TÂM TRI THỨC XÂY KÊNH & BẢN CHẤT NIỀM TIN • NGUYỄN ĐỨC VIỆT" },
    { id: "tu-duy",      file: "01-tu-duy.html",           group: "flow", n: "01", title: "Tư duy gốc: thương hiệu là hệ quả", short: "Tư duy", stage: "tuduy", icon: "🧠", q: "Vì sao làm kênh? Thương hiệu cá nhân thật sự là gì?" },
    { id: "bat-dau",     file: "02-bat-dau.html",          group: "flow", n: "02", title: "Bắt đầu từ đâu", short: "Bắt đầu", stage: "batdau", icon: "🚪", q: "Tôi là ai, có gì để quay, tuần đầu làm gì?" },
    { id: "logic-kenh",  file: "03-logic-kenh.html",       group: "flow", n: "03", title: "Logic xây kênh", short: "Logic kênh", stage: "logic", icon: "🧩", q: "View → niềm tin → khách tự chốt vận hành thế nào?" },
    { id: "niem-tin",    file: "04-niem-tin.html",         group: "flow", n: "04", title: "Logic niềm tin & storytelling vi mô", short: "Niềm tin", stage: "niemtin", icon: "🤝", q: "Nói thế nào để người xem tin ngay?" },

    // Chặng 05 duy nhất (Bản chuẩn mới nhất)
    { id: "dinh-dang-2",     file: "05-dinh-dang-2.0.html",          group: "flow", n: "05", title: "4 định dạng video, chuyển cảnh & bố cục", short: "Định dạng", stage: "dinhdang", icon: "🎬", v2: true, q: "Hệ thống 4 Định dạng chủ lực, Chuyển cảnh tự nhiên & Bố cục cảnh quay chỉn chu" },
    { id: "voice-over-2",    file: "dinh-dang/voiceover3.0.html",    group: "flow", parent: "dinh-dang-2", sub: true, n: "5.1", title: "Voice-Over & thao tác tay", short: "Voice-Over", stage: "dinhdang", icon: "🎙️", v2: true, q: "Dựng hình trước, lồng tiếng sau + Thực hành cảnh trám 3 lớp" },
    { id: "walk-and-talk-2", file: "dinh-dang/walkntalk2.0.html",    group: "flow", parent: "dinh-dang-2", sub: true, n: "5.2", title: "Walk & Talk (Vừa đi vừa nói)", short: "Walk & Talk", stage: "dinhdang", icon: "🚶", v2: true, q: "Quy tắc 3 trục 45° & Giải phẫu video mẫu thực chiến" },
    { id: "talking-head-2",  file: "dinh-dang/talkinghead2.0.html",  group: "flow", parent: "dinh-dang-2", sub: true, n: "5.3", title: "Talking Head (Ngồi nói chuyên gia)", short: "Talking Head", stage: "dinhdang", icon: "🗣️", v2: true, q: "Mặt để tin, Cảnh để hiểu, Nhịp để xem hết (Tỷ lệ 20/80)" },
    { id: "storytelling-2",  file: "dinh-dang/storytelling2.0.html", group: "flow", parent: "dinh-dang-2", sub: true, n: "5.4", title: "Storytelling (Lát cắt 5 giây)", short: "Storytelling", stage: "dinhdang", icon: "📖", v2: true, q: "Kể lát cắt 5 giây & Giữ thể diện cho người xem (T1 → T2 → T2.5 → T3)" },
    { id: "chuyen-canh-2",   file: "dinh-dang/chuyencanh2.0.html",   group: "flow", parent: "dinh-dang-2", sub: true, n: "5.5", title: "Chuyển cảnh bằng chuyển động thật", short: "Chuyển cảnh", stage: "dinhdang", icon: "⚡", v2: true, q: "Cắt trong chuyển động 70/30, Giống Selfie, Chân máy 30° & Khóa trọng tâm" },
    { id: "bo-cuc-quay-2",   file: "dinh-dang/bocucquay.html",       group: "flow", parent: "dinh-dang-2", sub: true, n: "5.6", title: "Bố cục cảnh quay chỉn chu", short: "Bố cục", stage: "dinhdang", icon: "🎥", v2: true, q: "6 Trụ cột Đường–Động–Sáng–Giờ–Tĩnh–Vào & Khoe khéo dịch vụ" },
    { id: "vo-boc-31",       file: "dinh-dang/vo-boc-31.html",       group: "flow", parent: "dinh-dang-2", sub: true, n: "5.7", title: "31 vỏ bọc video tạo lead", short: "31 vỏ bọc", stage: "dinhdang", icon: "🎭", q: "31 cách mở đầu để video chuyên môn không bị khô khan" },
    { id: "aiedit-affilate", file: "aiedit-affilate.html",           group: "flow", parent: "dinh-dang-2", sub: true, n: "5.8", title: "Affiliate AIDA & AI Edit V3.3", short: "Affiliate AIDA", stage: "dinhdang", icon: "🛒", q: "Quay & dựng sản phẩm theo 4 pha AIDA" },

    // Các trang Thực hành / Công cụ đi kèm (ẩn trên menu để thanh trái gọn, giữ shell điều hướng)
    { id: "walk-and-talk-2-ex", file: "dinh-dang/walkntalkthuchanh.html", group: "flow", parent: "dinh-dang-2", sub: true, hiddenFromMenu: true, activeMenuId: "walk-and-talk-2", v2: true, n: "5.2b", title: "Thực hành Walk & Talk (25 Ví dụ & 5 Bài tập)", short: "Bài tập Walk & Talk", stage: "dinhdang", icon: "🎬", q: "5 Bài tập nhóm 2 người • 25 ảnh phân cảnh lệch góc ≥45°" },
    { id: "bo-cuc-quay-2-ex",   file: "dinh-dang/bocucquaybaitap.html",   group: "flow", parent: "dinh-dang-2", sub: true, hiddenFromMenu: true, activeMenuId: "bo-cuc-quay-2",   v2: true, n: "5.6b", title: "Bài tập Bố cục (3 Cấp độ & 103 Mẫu)", short: "Bài tập Bố cục", stage: "dinhdang", icon: "✍️", q: "Lộ trình 3 cấp độ tại thành phố • 103 mẫu bố cục" },
    { id: "megaprompt-2",       file: "dinh-dang/megaprompt2.0.html",     group: "flow", parent: "dinh-dang-2", sub: true, hiddenFromMenu: true, activeMenuId: "dinh-dang-2",     v2: true, n: "5.9",  title: "Trung tâm MegaPrompt (4 Định dạng)", short: "MegaPrompt", stage: "dinhdang", icon: "🧰", q: "Bộ câu lệnh AI viết kịch bản theo 4 định dạng video + Lịch 4 bài/tuần" },

    { id: "ky-nang",     file: "06-ky-nang.html",    group: "flow", n: "06", title: "Bản đồ kỹ năng", short: "Kỹ năng", stage: "kynang", icon: "🛠️", q: "Cần giỏi những kỹ năng gì, học ở đâu?" },
    { id: "aieditskill", file: "aieditskill.html",   group: "flow", parent: "ky-nang", sub: true, n: "6.1", title: "Hệ thống AI Video Edit & 35 Mẫu MFX", short: "AI Edit Skill", stage: "kynang", icon: "🎞️", v2: true, q: "Hệ thống 10 cụm skill dựng AI, 35 mẫu chữ & bản vẽ 2D" },
    { id: "thuc-hanh",   file: "07-thuc-hanh.html",  group: "flow", n: "07", title: "Lộ trình thực hành 4 tuần", short: "Thực hành", stage: "thuchanh", icon: "🏋️", q: "Tuần 1 đến tuần 4 làm chính xác việc gì?" },

    { id: "case",        file: "09-case.html",       group: "ref", n: "08", title: "Hồ sơ kênh thật đã kiểm chứng", short: "Kênh thật", stage: "case", icon: "📚", q: "Giải phẫu các kênh có video thật & hàng trăm nghìn đến hàng triệu lượt xem" },
    { id: "tai-nguyen",  file: "08-tai-nguyen.html", group: "ref", n: "09", title: "Tài nguyên hệ thống & link mở ngay", short: "Tài nguyên", stage: "tainguyen", icon: "🔗", q: "Công cụ nào hỗ trợ bước nào? Bấm vào là ra." }
  ]
};
