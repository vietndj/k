/* =========================================================
   MANIFEST — Cây điều hướng chuẩn https://kenh.fedu.vn (18 trang)
   Gồm: Trục Logic 5 Mắt Xích · 4 Định Dạng & Kỹ Thuật · Thực Thi & Kênh Thật · Chuyên Khảo 1.0
   ========================================================= */
window.LINKS = {
  offline: "https://offline.fedu.vn",
  online:  "https://video.fedu.vn",
  ytuong:  "https://ytuong.fedu.vn",
  broll:   "https://brollbank.fedu.vn",
  nhac:    "https://nhac.fedu.vn",
  profile: "https://fedu.vn",
  backup:  "https://fedu.vn/kenh-goc/"
};

window.HUB = {
  name: "Trung tâm Logic Xây Kênh (2.0)",
  sub: "Từ 0 → đủ 7 giờ → khách tự chốt",
  groups: [
    { id: "flow", title: "Trục logic & định dạng" },
    { id: "ref",  title: "Bàn mổ kênh mẫu" },
    { id: "v1",   title: "Bản đọc tổng hợp" }
  ],
  pages: [
    // I. TRỤC LOGIC 5 MẮT XÍCH (5 trang)
    { id: "index",      file: "index.html",         group: "flow", n: "00", title: "Bản đồ từ 0 đến tự chốt",        short: "Tổng quan", stage: "ink",     icon: "00", v2: true, q: "BẢN ĐỒ TỔNG THỂ • 5 MẮT XÍCH TỪ 0 ĐẾN KHÁCH TỰ CHỐT TRONG IM LẶNG" },
    { id: "tu-duy",     file: "01-tu-duy.html",     group: "flow", n: "01", title: "Bản chất cuộc chơi & 7 giờ",      short: "Tư duy",    stage: "tuduy",   icon: "01", v2: true, q: "CHẶNG 01 • BẢO KÊ ĐẦU RA, BỘ KỸ NĂNG MỚI THỜI AI, ĐÓNG GÓI SỰ THẬT & BÀI TOÁN 7 GIỜ" },
    { id: "bat-dau",    file: "02-bat-dau.html",    group: "flow", n: "02", title: "Tín hiệu đắt giá & Vòng gửi xe",  short: "Bắt đầu",   stage: "batdau",  icon: "02", v2: true, q: "CHẶNG 02 • TÍN HIỆU ĐẮT GIÁ, 3 ĐẦU RA & VÒNG GỬI XE 3 GIÂY" },
    { id: "logic-kenh", file: "03-logic-kenh.html", group: "flow", n: "03", title: "5 mắt xích & 3 dòng nội dung",    short: "Logic kênh",stage: "logic",   icon: "03", v2: true, q: "CHẶNG 03 • QUÁ TRÌNH NGƯỜI XEM THẦM LẶNG & CHỐT ĐƠN QUA ZALO" },
    { id: "niem-tin",   file: "04-niem-tin.html",   group: "flow", n: "04", title: "Tâm lý 4 tầng & Thể diện T2.5",   short: "Niềm tin",  stage: "niemtin", icon: "04", v2: true, q: "CHẶNG 04 • LÁT CẮT 3 GIÂY & LÝ DO ĐÀNG HOÀNG ĐỂ KHÁCH MUA" },

    // II. 4 ĐỊNH DẠNG & KỸ THUẬT THỰC CHIẾN (9 trang)
    { id: "dinh-dang-2",     file: "05-dinh-dang-2.0.html",          group: "flow", n: "05", title: "Chọn định dạng theo độ dạn ống kính", short: "Định dạng",    stage: "dinhdang", icon: "05",  v2: true, q: "CHẶNG 05 • 4 ĐỊNH DẠNG TĂNG DẦN ĐỘ THOẢI MÁI & 2 KỸ NĂNG NỀN" },
    { id: "voice-over-2",    file: "dinh-dang/voiceover3.0.html",    group: "flow", parent: "dinh-dang-2", sub: true, n: "5.1", title: "Voice-Over & thao tác tay",         short: "Voice-Over",   stage: "dinhdang", icon: "5.1", v2: true, q: "ĐỊNH DẠNG 01 • KHÔNG LỘ MẶT, QUAY ĐÔI TAY ĐANG LÀM VIỆC THẬT" },
    { id: "walk-and-talk-2", file: "dinh-dang/walkntalk2.0.html",    group: "flow", parent: "dinh-dang-2", sub: true, n: "5.2", title: "Walk & Talk (Vừa đi vừa nói)",      short: "Walk & Talk",  stage: "dinhdang", icon: "5.2", v2: true, q: "ĐỊNH DẠNG 02 • ĐI LẠI ĐỂ THẢ LỎNG & 5 DẢI GÓC MÁY LỆCH 45°" },
    { id: "talking-head-2",  file: "dinh-dang/talkinghead2.0.html",  group: "flow", parent: "dinh-dang-2", sub: true, n: "5.3", title: "Talking Head (Ngồi nói tại bàn)",   short: "Talking Head", stage: "dinhdang", icon: "5.3", v2: true, q: "ĐỊNH DẠNG 03 • MẶT ĐỂ TIN, CẢNH ĐỂ HIỂU, NHỊP ĐỂ XEM HẾT (20/80)" },
    { id: "storytelling-2",  file: "dinh-dang/storytelling2.0.html", group: "flow", parent: "dinh-dang-2", sub: true, n: "5.4", title: "Storytelling (Lát cắt 5 giây)",     short: "Storytelling", stage: "dinhdang", icon: "5.4", v2: true, q: "ĐỊNH DẠNG 04 • KỂ 1 LÁT CẮT 5 GIÂY & NỐI SANG QUY LUẬT NGHỀ" },
    { id: "chuyen-canh-2",   file: "dinh-dang/chuyencanh2.0.html",   group: "flow", parent: "dinh-dang-2", sub: true, n: "5.5", title: "Chuyển cảnh 2.0: Cỡ cảnh, góc máy & 4 cấp độ", short: "Chuyển cảnh", stage: "dinhdang", icon: "5.5", v2: true, q: "KỸ THUẬT NỐI • CỠ CẢNH GÓC MÁY • CẤP CƠ BẢN 70/30 • CẦM TAY • CHÂN MÁY ĐIỆN ẢNH • INSERT SHOT" },
    { id: "bo-cuc-quay-2",   file: "dinh-dang/bocucquay.html",       group: "flow", parent: "dinh-dang-2", sub: true, n: "5.6", title: "Bố cục khung hình sạch",            short: "Bố cục",       stage: "dinhdang", icon: "5.6", v2: true, q: "KỸ THUẬT HÌNH • 6 QUY TẮC KHUNG HÌNH SẠCH LÀ LỜI KHEN KHÔNG CẦN NÓI" },
    { id: "vo-boc-31",       file: "dinh-dang/vo-boc-31.html",       group: "flow", parent: "dinh-dang-2", sub: true, n: "5.7", title: "31 vỏ bọc video tạo khách",         short: "31 vỏ bọc",    stage: "dinhdang", icon: "5.7", v2: true, q: "ĐA DẠNG HÓA • MƯỢN CHUYỆN ĐỜI THƯỜNG ĐỂ ĐƯA LÕI TAY NGHỀ VÀO VIDEO", adminOnly: true },
    { id: "megaprompt-2",    file: "dinh-dang/megaprompt2.0.html",   group: "flow", parent: "dinh-dang-2", sub: true, n: "5.8", title: "Bộ câu lệnh AI (4 định dạng)",      short: "Câu lệnh AI",  stage: "dinhdang", icon: "5.8", v2: true, q: "CÔNG CỤ AI • BỘ CÂU LỆNH VIẾT KỊCH BẢN KHỚP TỪNG CÁCH ĐẶT MÁY QUAY" },

    // III. THỰC THI & KÊNH THẬT (2 trang)
    { id: "thuc-hanh", file: "07-thuc-hanh.html", group: "flow", n: "06", title: "Lộ trình 4 tuần & 4 kỹ năng",   short: "Thực hành", stage: "thuchanh", icon: "06", v2: true, q: "CHẶNG 06 • LỘ TRÌNH 4 TUẦN CHO NGƯỜI CHỈ CÓ 2–3 GIỜ BẤM MÁY MỖI TUẦN" },
    { id: "case",      file: "09-case.html",      group: "ref",  n: "07", title: "Giải phẫu 7 kênh mẫu",          short: "Kênh mẫu",  stage: "case",     icon: "07", v2: true, q: "BÀN MỔ KÊNH MẪU • 7 KÊNH NGOÀI ĐỜI HỌC VIÊN GỬI VỀ: CHỖ RA KHÁCH, CHỖ ĐỨT MẠCH" },

    // IV. BẢN CHUYÊN KHẢO TỔNG HỢP 2.0 & GỐC 1.0
    { id: "logic-tong-hop", file: "logic-tong-hop.html",    group: "v1", n: "2.0", title: "Logic Xây Kênh Tổng Hợp (Mới)",      short: "Tổng hợp 2.0", stage: "ink", icon: "2.0", q: "Bản tổng hợp mới: Việc thật, tâm thế món quà, bảo kê đầu ra & đo hai pha" },
    { id: "cu",          file: "cu/index.html",          group: "v1", n: "1.0", title: "Logic Storytelling & Niềm tin (1.0)", short: "Niềm tin 1.0",  stage: "ink", icon: "1.0", q: "Chuyên khảo gốc 1.0: Hàng giá rẻ bán bằng View, hàng giá cao bán bằng Niềm tin", adminOnly: true },
    { id: "cu-xay-kenh", file: "cu/logic-xay-kenh.html", group: "v1", n: "1.0", title: "Logic Xây Kênh: 0 → Tự chốt (1.0)",   short: "Xây kênh 1.0", stage: "ink", icon: "1.0", q: "Chuyên khảo gốc 1.0: Lộ trình từ 0 → Khách tự chốt trong im lặng", adminOnly: true }
  ]
};
