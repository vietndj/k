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
    { id: "ref",  title: "Tra cứu & Dữ liệu" },
    { id: "fmt",  title: "Chi tiết 4 định dạng + chuyển cảnh" }
  ],
  pages: [
    { id: "index",       file: "index.html",       group: "flow", n: "00", title: "Bản đồ hành trình", short: "Bản đồ", stage: "ink", icon: "🧭", q: "Tôi đang đứng ở đâu, đi tiếp đường nào?" },
    { id: "tu-duy",      file: "01-tu-duy.html",   group: "flow", n: "01", title: "Tư duy gốc: thương hiệu là hệ quả", short: "Tư duy", stage: "tuduy", icon: "🧠", q: "Vì sao làm kênh? Thương hiệu cá nhân thật sự là gì?" },
    { id: "bat-dau",     file: "02-bat-dau.html",  group: "flow", n: "02", title: "Bắt đầu từ đâu", short: "Bắt đầu", stage: "batdau", icon: "🚪", q: "Tôi là ai, có gì để quay, tuần đầu làm gì?" },
    { id: "logic-kenh",  file: "03-logic-kenh.html", group: "flow", n: "03", title: "Logic xây kênh", short: "Logic kênh", stage: "logic", icon: "🧩", q: "View → niềm tin → khách tự chốt vận hành thế nào?" },
    { id: "niem-tin",    file: "04-niem-tin.html", group: "flow", n: "04", title: "Logic niềm tin & storytelling vi mô", short: "Niềm tin", stage: "niemtin", icon: "🤝", q: "Nói thế nào để người xem tin ngay?" },
    { id: "dinh-dang",   file: "05-dinh-dang.html",group: "flow", n: "05", title: "4 định dạng video + chuyển cảnh", short: "Định dạng", stage: "dinhdang", icon: "🎬", q: "Quay kiểu nào trước, kiểu nào sau?" },
    { id: "ky-nang",     file: "06-ky-nang.html",  group: "flow", n: "06", title: "Bản đồ kỹ năng", short: "Kỹ năng", stage: "kynang", icon: "🛠️", q: "Cần giỏi những kỹ năng gì, học ở đâu?" },
    { id: "thuc-hanh",   file: "07-thuc-hanh.html",group: "flow", n: "07", title: "Lộ trình thực hành", short: "Thực hành", stage: "thuchanh", icon: "🏋️", q: "Tuần 1, tuần 2... làm chính xác việc gì?" },

    { id: "tai-nguyen",  file: "08-tai-nguyen.html", group: "ref", n: "08", title: "Tài nguyên hệ thống & link mở ngay", short: "Tài nguyên", stage: "tainguyen", icon: "🔗", q: "Công cụ nào hỗ trợ bước nào? Bấm vào là ra." },
    { id: "case",        file: "09-case.html",     group: "ref", n: "09", title: "Case study theo ngành", short: "Case", stage: "case", icon: "📚", q: "Ngành của tôi đã có ai làm chưa, làm thế nào?" },
    { id: "hoc-vien",    file: "10-hoc-vien.html", group: "ref", n: "10", title: "Dữ liệu thật về học viên", short: "Học viên", stage: "dulieu", icon: "📊", q: "Người học thật sự đau ở đâu, sợ gì, cần gì?" },
    { id: "giao-an",     file: "11-giao-an.html",  group: "ref", n: "11", title: "Giáo án động (bổ sung dữ liệu)", short: "Giáo án", stage: "ink", icon: "🗂️", q: "28 vấn đề, ví dụ, bài tập — và cách tôi thêm vào." },

    { id: "voice-over",   file: "dinh-dang/voice-over.html",   group: "fmt", n: "5.1", title: "Voice-Over & thao tác tay", short: "Voice-Over", stage: "dinhdang", icon: "🎙️", q: "Chưa dám lộ mặt?" },
    { id: "walk-and-talk",file: "dinh-dang/walk-and-talk.html",group: "fmt", n: "5.2", title: "Walk & Talk", short: "Walk & Talk", stage: "dinhdang", icon: "🚶", q: "Nói cứng, cần tự nhiên?" },
    { id: "talking-head", file: "dinh-dang/talking-head.html", group: "fmt", n: "5.3", title: "Talking Head", short: "Talking Head", stage: "dinhdang", icon: "🗣️", q: "Cần dựng uy tín chuyên gia?" },
    { id: "storytelling", file: "dinh-dang/storytelling.html", group: "fmt", n: "5.4", title: "Storytelling 2.5", short: "Storytelling", stage: "dinhdang", icon: "📖", q: "Chạm đúng chỗ đau giấu kín?" },
    { id: "chuyen-canh",  file: "dinh-dang/chuyen-canh.html",  group: "fmt", n: "5.5", title: "Chuyển cảnh (chất keo)", short: "Chuyển cảnh", stage: "dinhdang", icon: "⚡", q: "Video giật, mất người xem?" },
    { id: "vo-boc-31",    file: "dinh-dang/vo-boc-31.html",    group: "fmt", n: "5.6", title: "31 vỏ bọc video tạo lead", short: "31 vỏ bọc", stage: "dinhdang", icon: "🎭", q: "Nghĩ gì để quay hôm nay?" }
  ]
};
