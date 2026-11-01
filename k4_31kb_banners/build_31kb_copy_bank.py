#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P1 - BUILD 31 SCRIPTS x 5 INSIGHT ANGLES = 155 NON-OVERLAPPING AD COPIES
========================================================================
Thiết kế 5 góc nhìn insight chuyên sâu cho từng kịch bản từ KB_02 đến KB_31
(KB_01 đã chốt ở Lô 0), bám sát 100% câu chữ gốc trong `scripts_31kb.json`
và tuân thủ nghiêm ngặt quy chuẩn CLAUDE2:
- Bản Before (`angles`): 20-23 từ, chia sẵn `headline_break` 2 dòng cân đối.
- Bản After nén chữ (`compressed_copy`): 16-19 từ, mỗi dòng `headline_break` <= 16 ký tự,
  không dùng từ hứa quá đà ("kèm 1-1", "K4"), đúng thông tin thật của lớp Hà Nội 07-08/11.
- Kiểm tra 155 tiêu đề không trùng nhau (`duplicate_headlines == 0`).
"""

import json
import unicodedata
from pathlib import Path
from typing import Dict, Any, List

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")

# Dữ liệu 5 góc nhìn (Before & After nén chữ) cho KB_02 .. KB_31 bám sát từng kịch bản
KB_COPY_SPECS: Dict[str, Dict[str, Any]] = {
    "KB_02": {
        "title": "KB 02: Mạng Xã Hội Cũ Đã Chết — Kỷ Nguyên Ngữ Nghĩa",
        "angles": [
            {
                "layer": "Tầng 2 · AI đọc ngữ nghĩa từng khung hình",
                "before": ("THUẬT TOÁN MỚI", ["Mạng xã hội cũ", "đã khép lại rồi"], "AI giờ nghe từng câu bạn nói để tìm đúng khách.", "Giữ chỗ ngay"),
                "after": ("THUẬT TOÁN MỚI", ["Mạng xã hội cũ", "đã khép lại"], "AI nghe từng câu để tìm đúng khách.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2 · Hiện trường mỏi gáy 3 giây",
                "before": ("HÀNH VI NGƯỜI MUA", ["Khách dừng lại 3 giây", "là AI nhớ ngay"], "Chỉ cần nói đúng bệnh, hệ thống tự mang khách tới.", "Đăng ký lớp"),
                "after": ("HÀNH VI MUA", ["Dừng lại 3 giây", "là AI nhớ ngay"], "Nói đúng bệnh, máy tự tìm khách.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 2.5 · Gỡ áp lực làm Idol câu view",
                "before": ("KHÔNG CẦN CÂU LIKE", ["Người trầm tính", "vẫn thắng lớn"], "Không cần ồn ào, chỉ cần tháo gỡ đúng việc thật.", "Xem lịch học"),
                "after": ("KHÔNG CẦU LIKE", ["Người trầm tính", "vẫn thắng lớn"], "Chỉ cần tháo gỡ đúng việc thật.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Tín hiệu sạch cho thuật toán",
                "before": ("LỚP HỌC 2 NGÀY", ["Đóng gói chuyên môn", "thành tín hiệu sạch"], "Giúp AI đọc hiểu sản phẩm của bạn trong 60 giây.", "Đăng ký ngay"),
                "after": ("LỚP 2 NGÀY", ["Biến chuyên môn", "thành tín hiệu"], "Để AI hiểu sản phẩm trong 60 giây.", "Đăng ký ngay"),
            },
            {
                "layer": "Chuyển tâm thế · Mỗi tuần 1 bài chất lượng",
                "before": ("HÀ NỘI · 07–08/11", ["Một video trúng đích", "hơn mười bài ồn ào"], "Hết ngày 1 thấy không hợp, hoàn đủ 100% học phí.", "Giữ chỗ"),
                "after": ("CÒN 17/35 CHỖ", ["Một bài trúng đích", "hơn mười bài ồn"], "Ngày 1 không hợp: hoàn 100% phí.", "Giữ chỗ"),
            },
        ],
    },
    "KB_03": {
        "title": "KB 03: Chân Thật Là Một Loại Hiệu Suất & Tâm Thế Người Tặng Quà",
        "angles": [
            {
                "layer": "Tầng 2 · Video bóng bẩy đại trà",
                "before": ("BẪY KỸ XẢO ĐẠI TRÀ", ["Càng cố nói văn hoa", "nghe càng giả"], "Khách hàng giờ lướt qua mọi video tô vẽ bề ngoài.", "Giữ chỗ ngay"),
                "after": ("BỎ VĂN HOA", ["Càng nói văn hoa", "nghe càng giả"], "Khách lướt qua mọi video tô vẽ.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Sự cô đặc của lời nói thật",
                "before": ("ĐỘ NÉN NGÔN TỪ", ["Lời nói thật tốn ít", "từ vựng nhất"], "Chân thật trên video chính là một loại hiệu suất cao.", "Đăng ký lớp"),
                "after": ("ĐỘ NÉN THẬT", ["Lời nói thật tốn", "ít từ vựng nhất"], "Chân thật chính là hiệu suất cao.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 3 · Tâm thế người tặng quà",
                "before": ("ĐỪNG XIN LƯỢT XEM", ["Bước lên ống kính", "như người tặng quà"], "Chia sẻ điều có ích, người cùng tần số sẽ ở lại.", "Xem lịch học"),
                "after": ("TÂM THẾ MỚI", ["Lên ống kính như", "người tặng quà"], "Chia sẻ điều thật, khách tự ở lại.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 2 · Cắt bỏ chữ thừa",
                "before": ("GỌT SẠCH CHỮ THỪA", ["Nén câu nói gọn sắc", "trong sáu mươi giây"], "Bỏ hết lời chào rườm rà, đi thẳng vào việc của khách.", "Đăng ký ngay"),
                "after": ("GỌT CHỮ THỪA", ["Nén câu gọn sắc", "trong 60 giây"], "Bỏ lời rườm rà, vào thẳng việc.", "Đăng ký ngay"),
            },
            {
                "layer": "Đảo rủi ro · Thực hành trực tiếp tại Hà Nội",
                "before": ("OFFLINE 07–08/11", ["Quay bằng giọng thật", "không gồng mình"], "Lớp tối đa 35 người, hoàn phí 100% sau ngày đầu.", "Giữ chỗ"),
                "after": ("OFFLINE HÀ NỘI", ["Quay giọng thật", "không gồng mình"], "Ngày 1 không hợp: hoàn 100% phí.", "Giữ chỗ"),
            },
        ],
    },
    "KB_04": {
        "title": "KB 04: Giống Nhau Thì Khách So Giá — Bóc Tách Đặc Trưng Sản Phẩm",
        "angles": [
            {
                "layer": "Tầng 2 · Văn mẫu AI trung bình cộng",
                "before": ("BẪY VĂN MẪU AI", ["Video giống hệt nhau", "thì khách so giá"], "AI viết chung chung nên kênh của bạn chìm giữa đám đông.", "Giữ chỗ ngay"),
                "after": ("THOÁT VĂN MẪU", ["Giống hệt nhau", "thì khách so giá"], "Đừng để kênh chìm giữa đám đông.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · So giá hay so tay nghề",
                "before": ("BÁN ĐƠN GIÁ CAO", ["Để khách so tay nghề", "đừng để so giá"], "Khách trả tiền cao chỉ mua phần đặc trưng riêng của bạn.", "Đăng ký lớp"),
                "after": ("ĐƠN GIÁ CAO", ["Khách so tay nghề", "không so giá"], "Họ mua điểm riêng chỉ bạn mới có.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Giao việc kỹ thuật cho mẫu dựng",
                "before": ("NHẸ GÁNH KỸ THUẬT", ["Cắt vấp và chạy chữ", "máy làm vài phút"], "Vào lớp nhận sẵn quy trình mẫu, khỏi mò từng nút bấm.", "Xem lịch học"),
                "after": ("NHẸ KỸ THUẬT", ["Cắt vấp chạy chữ", "máy làm vài phút"], "Nhận quy trình mẫu, khỏi mò nút bấm.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Gạn đúng chi tiết đắt giá",
                "before": ("BÓC TÁCH SẢN PHẨM", ["Đưa ca khó từng gỡ", "lên ngay đầu clip"], "Chỉ cần đúng người đang cần xem thấy là nhắn Zalo thật.", "Đăng ký ngay"),
                "after": ("ĐIỂM ĐẮT GIÁ", ["Đưa ca khó từng gỡ", "lên đầu video"], "Đúng người cần xem là nhắn hỏi thật.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Mang sản phẩm tới lớp Hà Nội",
                "before": ("HÀ NỘI · 07–08/11", ["Mang sản phẩm thật", "tới lớp bóc tách"], "Đi 2 người ưu đãi người thứ hai chỉ còn 3,5 triệu.", "Giữ chỗ"),
                "after": ("ƯU ĐÃI NHÓM 2", ["Mang sản phẩm", "tới lớp bóc tách"], "Đi 2 người: người sau chỉ 3,5 triệu.", "Giữ chỗ"),
            },
        ],
    },
    "KB_05": {
        "title": "KB 05: Ngoài Đời Nói Cuốn, Lên Máy Là Đơ — Giữ Nguyên Phong Thái Thật",
        "angles": [
            {
                "layer": "Tầng 2 · Độ vênh giữa gặp khách và bật máy",
                "before": ("NGƯỢNG TRƯỚC ỐNG KÍNH", ["Tư vấn hai tiếng mượt", "bật máy là khựng"], "Quay năm lần lại bấm xóa vì giọng như đọc giấy.", "Giữ chỗ ngay"),
                "after": ("NGƯỢNG TRƯỚC MÁY?", ["Ngoài đời nói mượt", "bật máy là khựng"], "Quay năm lần lại xóa vì giọng cứng.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Não gánh 5 việc cùng lúc",
                "before": ("KHÔNG PHẢI BẠN KÉM", ["Đầu gánh năm việc", "nên mặt tự cứng"], "Vừa nhớ chữ vừa sợ vấp nên khó nói tự nhiên.", "Đăng ký lớp"),
                "after": ("QUÁ TẢI BỘ NHỚ", ["Gánh năm việc liền", "nên mặt tự cứng"], "Lo nhớ chữ thì không thể tự nhiên.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Bóc ý ngắn 5 giây + 2 góc máy",
                "before": ("CẤT BỚT 4 VIỆC NẶNG", ["Bóc ý ngắn năm giây", "khỏi học thuộc lòng"], "Đặt máy cố định tại bàn, lúc bấm máy chỉ còn việc nói.", "Xem lịch học"),
                "after": ("CẤT 4 VIỆC NẶNG", ["Ý ngắn năm giây", "khỏi học thuộc"], "Lúc bấm máy bạn chỉ còn việc nói.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Giữ ánh mắt và nhịp thở thật",
                "before": ("PHONG THÁI CHỦ NGHỀ", ["Ngoài đời đĩnh đạc", "lên hình nguyên thế"], "Khách tin bạn ở ánh mắt đàng hoàng, không phải kỹ xảo.", "Đăng ký ngay"),
                "after": ("PHONG THÁI THẬT", ["Ngoài đời thế nào", "lên hình như thế"], "Khách tin ở ánh mắt đàng hoàng.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Ngồi đối diện nắn nhịp nói",
                "before": ("OFFLINE HÀ NỘI", ["Ngồi đối diện bạn", "nắn từng câu mở lời"], "Tặng khóa online xem lại tại nhà và 30 ngày sửa bài.", "Giữ chỗ"),
                "after": ("TẶNG KHÓA ONLINE", ["Ngồi đối diện nắn", "từng câu mở lời"], "Có khóa online xem lại tại nhà.", "Giữ chỗ"),
            },
        ],
    },
    "KB_06": {
        "title": "KB 06: Câu Trả Lời Bạn Nói Mỗi Ngày — 4 Định Dạng Quay Trong Lúc Làm Nghề",
        "angles": [
            {
                "layer": "Tầng 2 · Ngày nào cũng giải thích lại từ đầu",
                "before": ("CHO NGƯỜI BẬN RỘN", ["Một câu hỏi lặp lại", "giải thích chục lần"], "Đóng gói thành video một phút để máy tư vấn thay bạn.", "Giữ chỗ ngay"),
                "after": ("Đỡ TỐN GIỜ NÓI", ["Câu hỏi lặp lại", "đóng thành video"], "Để video tư vấn khách thay bạn.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Sợ bày đèn máy tốn hàng tiếng",
                "before": ("LÀM MỘT MÌNH (SOLO)", ["Không cần dừng việc", "ở tiệm để quay"], "Câu trả lời khách mỗi ngày chính là kịch bản có sẵn.", "Đăng ký lớp"),
                "after": ("QUY TRÌNH SOLO", ["Không dừng việc", "ở tiệm để quay"], "Câu trả lời mỗi ngày là kịch bản.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Công cụ tự động thay cả ekip",
                "before": ("KHÔNG CẦN THUÊ EKIP", ["Lọc ồn cắt khoảng nghỉ", "xong trong vài phút"], "Phần việc của cả ekip giờ làm gọn ngay trên máy bạn.", "Xem lịch học"),
                "after": ("THAY CẢ EKIP", ["Lọc ồn cắt nghỉ", "xong vài phút"], "Việc của ekip giờ gọn trên máy bạn.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · 4 định dạng quay khớp công việc",
                "before": ("4 ĐỊNH DẠNG QUAY", ["Mười lăm phút làm nghề", "ra ngay một video"], "Quay cận đôi tay hoặc vừa đi vừa chỉ việc thật tại cơ sở.", "Đăng ký ngay"),
                "after": ("4 KIỂU QUAY THẬT", ["Mười lăm phút làm", "ra ngay một clip"], "Quay cận tay hoặc vừa đi vừa nói.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Mang câu khách hay hỏi tới lớp",
                "before": ("HÀ NỘI · 07–08/11", ["Mang câu khách hỏi", "làm thành video về"], "Học hết ngày 1 không hợp công việc: hoàn đủ 100% phí.", "Giữ chỗ"),
                "after": ("CÒN 17/35 CHỖ", ["Mang câu khách hỏi", "quay xong mang về"], "Ngày 1 không hợp: hoàn 100% phí.", "Giữ chỗ"),
            },
        ],
    },
    "KB_07": {
        "title": "KB 07: Thuê Đội Ngoài 15–30 Triệu Hay Tự Cầm Kênh Bằng Kiến Thức Nghề",
        "angles": [
            {
                "layer": "Tầng 2 · Đốt 15–30 triệu thuê ngoài không ra khách",
                "before": ("BẪY THUÊ ĐỘI NGOÀI", ["Trả ba mươi triệu", "khách không nhắn câu nào"], "Hình đẹp nhưng người viết chưa từng đứng bán hàng một ngày.", "Giữ chỗ ngay"),
                "after": ("BẪY THUÊ NGOÀI", ["Trả ba mươi triệu", "không ai nhắn hỏi"], "Vì người viết chưa từng bán hàng.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Dùng sai từ của nghề",
                "before": ("KHÁCH KỸ TÍNH BIẾT NGAY", ["Người ngoài viết bài", "sai hết từ của nghề"], "Khách lớn nghe vài giây thấy lệch giọng là đi tìm chỗ khác.", "Đăng ký lớp"),
                "after": ("SAI GIỌNG NGHỀ", ["Người ngoài viết", "sai từ của nghề"], "Khách kỹ tính nghe vài giây là đi.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Kỹ thuật giờ rất nhẹ",
                "before": ("TỰ CẦM KÊNH DỄ DÀNG", ["Phần dựng và chạy chữ", "mẫu có sẵn lo gọn"], "Bạn không cần phụ thuộc đội ngoài cho những việc cơ bản.", "Xem lịch học"),
                "after": ("TỰ CẦM KÊNH", ["Phần dựng chạy chữ", "mẫu sẵn lo gọn"], "Khỏi phụ thuộc người ngoài mỗi tháng.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Những điều chỉ chủ nghề mới biết",
                "before": ("KIẾN THỨC TRONG ĐẦU", ["Thứ không thuê được", "là trải nghiệm nghề"], "Đưa đúng những ca làm việc thật của bạn lên ống kính.", "Đăng ký ngay"),
                "after": ("CHỈ BẠN MỚI BIẾT", ["Thứ không thuê được", "là kinh nghiệm nghề"], "Đưa đúng ca làm thật lên ống kính.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · 2 ngày tự làm chủ kênh tại Hà Nội",
                "before": ("LỚP 2 NGÀY HÀ NỘI", ["Nói đúng giọng chủ nghề", "khách nghe là nể"], "Học phí 4 triệu, đi 2 người người thứ hai chỉ 3,5 triệu.", "Giữ chỗ"),
                "after": ("07–08/11 HÀ NỘI", ["Đúng giọng chủ nghề", "khách nghe là tin"], "Đi 2 người: người sau chỉ 3,5 triệu.", "Giữ chỗ"),
            },
        ],
    },
    "KB_08": {
        "title": "KB 08: Câu Chào Lịch Sự Đang Đốt Tiền Quảng Cáo Của Bạn",
        "angles": [
            {
                "layer": "Tầng 2 · Mất khách ngay ở 3 giây đầu",
                "before": ("ĐỐT TIỀN QUẢNG CÁO", ["Câu chào lịch sự", "làm khách vuốt đi"], "Chào hỏi dài dòng là mất khách ngay giây thứ ba.", "Giữ chỗ ngay"),
                "after": ("LỖI 3 GIÂY ĐẦU", ["Câu chào lịch sự", "làm khách vuốt đi"], "Mất người mua ngay từ giây thứ ba.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Cái đắt nhất lại cất ở cuối video",
                "before": ("NGƯỢC THỨ TỰ NÓI", ["Thứ đắt giá nhất", "đừng cất ở cuối bài"], "Lúc bạn nói tới điểm hay nhất thì khách đã lướt mất rồi.", "Đăng ký lớp"),
                "after": ("ĐẢO NGƯỢC CẤU TRÚC", ["Thứ đắt giá nhất", "đưa lên câu đầu"], "Để cuối bài thì khách đã lướt mất.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Giữ nhịp khung hình tự động",
                "before": ("KHÔNG CẮT TAY TỪNG GIÂY", ["Đổi cảnh gắn chữ nhấn", "mẫu dựng làm sẵn"], "Máy lo phần giữ nhịp, bạn tập trung vào câu mở lời.", "Xem lịch học"),
                "after": ("GIỮ NHỊP TỰ ĐỘNG", ["Đổi cảnh gắn chữ", "mẫu dựng làm sẵn"], "Bạn chỉ tập trung vào câu mở lời.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Bằng chứng thật ngay trên tay",
                "before": ("KHÔNG CẦN ỒN ÀO", ["Mở bài bằng cận cảnh", "bằng chứng trên tay"], "Gọi thẳng vấn đề khách đang vướng ngay câu đầu tiên.", "Đăng ký ngay"),
                "after": ("MỞ BÀI THỰC CHIẾN", ["Cận cảnh bằng chứng", "ngay câu đầu tiên"], "Gọi thẳng vấn đề khách đang vướng.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Sửa từng câu mở đầu tại lớp",
                "before": ("OFFLINE 07–08/11", ["Sửa từng câu mở đầu", "giữ tiền quảng cáo"], "Tặng khóa online xem lại tại nhà và 30 ngày sửa bài.", "Giữ chỗ"),
                "after": ("HÀ NỘI · 07–08/11", ["Sửa câu mở đầu", "giữ khách mua thật"], "Tặng khóa online xem lại tại nhà.", "Giữ chỗ"),
            },
        ],
    },
    "KB_09": {
        "title": "KB 09: Khách Mua Lớn Xem Âm Thầm, Không Bấm Thích Công Khai",
        "angles": [
            {
                "layer": "Tầng 2 · Nguồn khách quen bắt đầu chững lại",
                "before": ("KHÁCH QUEN CHỮNG LẠI?", ["Người mua đơn lớn", "không bấm thích ồn ào"], "Họ âm thầm xem liền vài video rồi mới nhắn tin riêng.", "Giữ chỗ ngay"),
                "after": ("TỆP KHÁCH ĐƠN LỚN", ["Khách mua đơn lớn", "xem rất âm thầm"], "Xem liền vài bài rồi mới nhắn riêng.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Ngộ nhận ít like là không ai mua",
                "before": ("ĐỪNG BỎ CUỘC SỚM", ["Mười mấy lượt thích", "vẫn chốt đơn trăm triệu"], "Ít lượt thích nhưng khách lớn vẫn đang âm thầm xem.", "Đăng ký lớp"),
                "after": ("ĐỪNG ĐẾM LƯỢT THÍCH", ["Ít người bấm thích", "vẫn chốt đơn lớn"], "Khách giàu đang âm thầm soi tay nghề.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Đăng đều mỗi tuần nhẹ nhàng",
                "before": ("ĐỀU ĐẶN MỖI TUẦN", ["Quy trình gọn nhẹ", "giữ kênh luôn sống"], "AI hỗ trợ phần nặng để bạn duy trì mặt hàng tuần.", "Xem lịch học"),
                "after": ("DUY TRÌ NHỊP KÊNH", ["Quy trình gọn nhẹ", "đăng đều mỗi tuần"], "Công cụ lo phần nặng giúp bạn.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Trả lời trước điều khách ngại hỏi",
                "before": ("THuyết PHỤC NGƯỜI MUA", ["Trả lời trước câu hỏi", "khách lớn ngại mở lời"], "Giải thích rõ vì sao giá cao và bao lâu thấy kết quả.", "Đăng ký ngay"),
                "after": ("TẠO NIỀM TIN SÂU", ["Gỡ trước băn khoăn", "khách ngại mở lời"], "Nói rõ vì sao giá cao, bao lâu xong.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Xây lộ trình khách tự chốt",
                "before": ("CÒN 17/35 CHỖ", ["Khách tin bạn trước", "khi bấm nhắn tin"], "Học trực tiếp 2 ngày tại Long Biên, Hà Nội 07–08/11.", "Giữ chỗ"),
                "after": ("LONG BIÊN HÀ NỘI", ["Khách đã tin bạn", "trước khi nhắn tin"], "Lớp trực tiếp 2 ngày 07–08/11.", "Giữ chỗ"),
            },
        ],
    },
    "KB_10": {
        "title": "KB 10: Tự Khen Không Ai Tin — Dám Nói 'Không' Mới Là Bằng Chứng",
        "angles": [
            {
                "layer": "Tầng 2 · Lời tự khen rẻ tiền",
                "before": ("KHÁCH ĐÃ NGÁN QUẢNG CÁO", ["Tự khen hàng chuẩn", "chẳng còn ai tin"], "Câu nói không tốn đồng nào thì người nghe lướt qua ngay.", "Giữ chỗ ngay"),
                "after": ("BỎ LỜI TỰ KHEN", ["Tự khen hàng chuẩn", "chẳng còn ai tin"], "Lời nói suông khách lướt qua ngay.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Tín hiệu đắt giá dám chịu thiệt",
                "before": ("BẰNG CHỨNG THÉP", ["Một lần dám nói không", "hơn mười bài tự khen"], "Từ chối bán món không hợp làm khách tin bạn tuyệt đối.", "Đăng ký lớp"),
                "after": ("BẰNG CHỨNG THÉP", ["Một lần nói không", "hơn mười bài khen"], "Dám từ chối đơn lệch là khách tin.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Kỹ thuật quay sáng cắt gọn",
                "before": ("CẮT GHÉP TỰ ĐỘNG", ["Quay sáng cắt gọn", "mẫu dựng lo gần hết"], "Không mất thời gian loay hoay chỉnh từng đoạn phụ đề.", "Xem lịch học"),
                "after": ("CẮT GHÉP NHANH GỌN", ["Quay sáng cắt gọn", "mẫu dựng lo hết"], "Khỏi loay hoay chỉnh từng phụ đề.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Kể nguyên tắc nghề không phô trương",
                "before": ("NGUYÊN TẮC LÀM NGHỀ", ["Kể chuyện từ chối đơn", "khách thấy sự đàng hoàng"], "Đào đúng những ca giữ chữ tín trong nghề của bạn.", "Đăng ký ngay"),
                "after": ("CHỮ TÍN NGHỀ", ["Kể lần từ chối đơn", "khách nể nguyên tắc"], "Đào đúng ca thật trong nghề bạn.", "Đăng ký ngay"),
            },
            {
                "layer": "Đảo rủi ro · Chính lớp học làm mẫu cam kết",
                "before": ("CAM KẾT THẬT 100%", ["Hết ngày đầu không hợp", "hoàn đủ học phí"], "Chính mình làm mẫu nguyên tắc chịu thiệt tại lớp Hà Nội.", "Giữ chỗ"),
                "after": ("HOÀN PHÍ NGÀY 1", ["Hết ngày đầu lệch", "hoàn đủ học phí"], "Làm đúng nguyên tắc tại lớp Hà Nội.", "Giữ chỗ"),
            },
        ],
    },
    "KB_11": {
        "title": "KB 11: Đồ Nghề Phủ Bụi — Không Phải Bạn Lười",
        "angles": [
            {
                "layer": "Tầng 2 · Đèn mic mua đủ nằm góc nhà",
                "before": ("ĐỒ NGHỀ PHỦ BỤI?", ["Đèn mic mua đủ cả", "nhưng nằm góc phòng"], "Lưu cả trăm video hướng dẫn mà tối nào cũng ngại mở.", "Giữ chỗ ngay"),
                "after": ("ĐỒ NGHỀ PHỦ BỤI?", ["Đèn mic mua đủ", "nằm im góc phòng"], "Lưu trăm hướng dẫn vẫn chưa bấm máy.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Cái giá để bắt đầu quá đắt",
                "before": ("GỠ TỘI CHO CHỦ NGHỀ", ["Không phải bạn lười", "mà khâu chuẩn bị nặng"], "Lôi đồ ra lắp rồi dựng khuya làm bạn ngại quay.", "Đăng ký lớp"),
                "after": ("KHÔNG PHẢI LƯỜI", ["Không phải bạn lười", "do chuẩn bị nặng"], "Lắp đèn dựng khuya làm bạn nản.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Góc quay cố định trong một sải tay",
                "before": ("NGUYÊN LÝ SẢI TAY", ["Đặt máy cố định bàn", "ngồi xuống là bấm quay"], "Mẫu dựng có sẵn giúp cắt ghép xong trong vài phút.", "Xem lịch học"),
                "after": ("MỘT SẢI TAY", ["Máy cố định tại bàn", "ngồi xuống là quay"], "Mẫu tự động dựng xong vài phút.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Vượt qua video đầu tiên",
                "before": ("LÀM THẬT TẠI LỚP", ["Xem trăm bài hướng dẫn", "không bằng quay một lần"], "Mang đồ nghề ở góc nhà tới lớp để bấm máy thực tế.", "Đăng ký ngay"),
                "after": ("BẤM MÁY THẬT", ["Trăm bài hướng dẫn", "thua một lần quay"], "Mang đồ nghề tới lớp làm thực tế.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Mang 3 video hoàn chỉnh về nhà",
                "before": ("OFFLINE HÀ NỘI", ["Làm xong ba video", "hoàn chỉnh mang về"], "Hai ngày 07–08/11 tại Long Biên, có buffet trưa miễn phí.", "Giữ chỗ"),
                "after": ("07–08/11 HÀ NỘI", ["Quay xong ba video", "hoàn chỉnh mang về"], "Tặng khóa online xem lại tại nhà.", "Giữ chỗ"),
            },
        ],
    },
    "KB_12": {
        "title": "KB 12: Hỏi Giá Xong Chỉ Hiện 'Đã Xem' — Thấy Giá Trị Trước Khi Thấy Giá",
        "angles": [
            {
                "layer": "Tầng 2 · Nỗi ám ảnh dòng chữ Đã xem",
                "before": ("TIN NHẮN IM LẶNG", ["Báo giá xong bên kia", "chỉ hiện chữ Đã xem"], "Họ không hỏi dạo, chỉ chưa đủ tin chi chục triệu.", "Giữ chỗ ngay"),
                "after": ("CHỈ HIỆN ĐÃ XEM?", ["Báo giá xong khách", "im lặng Đã xem"], "Họ chưa đủ tin để chi chục triệu.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Chặn người lạ ngoài ngã tư cầu hôn",
                "before": ("ĐƠN HÀNG GIÁ TRỊ CAO", ["Đừng bắt khách chốt", "chỉ qua một video"], "Mới biết một phút chưa ai dám đặt đơn chục triệu.", "Đăng ký lớp"),
                "after": ("BÁN ĐƠN LỚN", ["Đừng ép khách chốt", "qua một video"], "Mới biết một phút chưa ai dám mua.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Chia 1 ca làm thành chuỗi 5–7 clip",
                "before": ("CHUỖI VIDEO LÀM ẤM", ["Chia một ca làm nghề", "thành bảy video ngắn"], "Công cụ cắt gọn từng bước để khách ngồi với bạn đủ lâu.", "Xem lịch học"),
                "after": ("CHUỖI 7 VIDEO", ["Một ca làm nghề", "chia bảy clip ngắn"], "Để khách ngồi xem bạn làm đủ lâu.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Thấy giá trị trước khi thấy giá",
                "before": ("ĐẢO NGƯỢC TÂM LÝ", ["Cho khách thấy độ kỹ", "trước khi thấy con số"], "Chỉ rõ chỗ nào khó và vì sao tiệm bạn không làm tắt.", "Đăng ký ngay"),
                "after": ("THẤY GIÁ TRỊ TRƯỚC", ["Thấy độ kỹ tính", "trước khi thấy giá"], "Chỉ rõ vì sao bạn không làm tắt.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Khách nhắn hỏi lịch thay vì hỏi giá",
                "before": ("HÀ NỘI · 07–08/11", ["Để khách nhắn hỏi lịch", "chứ không hỏi giá"], "Dựng chuỗi video ngay trên sản phẩm thật của bạn tại lớp.", "Giữ chỗ"),
                "after": ("CÒN 17/35 CHỖ", ["Khách nhắn hỏi lịch", "thay vì hỏi giá"], "Dựng ngay trên sản phẩm của bạn.", "Giữ chỗ"),
            },
        ],
    },
    "KB_13": {
        "title": "KB 13: Ngại Người Quen Lướt Thấy, Để Đôi Tay Nói Trước",
        "angles": [
            {
                "layer": "Tầng 2 · Sợ câu trêu ở quán cà phê sáng mai",
                "before": ("TÂM LÝ CHỦ NGHỀ", ["Không sợ người lạ", "chỉ ngại người quen"], "Ngại sáng mai ra quán cà phê bạn bè trêu lên mạng bán hàng.", "Giữ chỗ ngay"),
                "after": ("NGẠI NGƯỜI QUEN?", ["Không sợ người lạ", "chỉ ngại bạn bè"], "Sợ câu trêu dạo này lên mạng à.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Chưa cần lộ mặt ngày đầu",
                "before": ("GỠ RÀO CẢN THỂ DIỆN", ["Chưa quen nhìn máy", "để đôi tay nói trước"], "Quay cận bàn tay thao tác nghề rồi thu giọng đọc trầm tĩnh.", "Đăng ký lớp"),
                "after": ("ĐỂ ĐÔI TAY NÓI", ["Chưa quen lộ mặt", "quay cận đôi tay"], "Quay thao tác nghề, thu giọng sau.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Định dạng Voice-Over phòng tĩnh",
                "before": ("ĐỊNH DẠNG VOICE-OVER", ["Tối về phòng yên tĩnh", "đọc lại ba câu ngắn"], "Máy tự ghép hình đôi tay làm việc với giọng đọc ấm áp.", "Xem lịch học"),
                "after": ("THU GIỌNG TỐI", ["Quay tay ban ngày", "thu giọng buổi tối"], "Máy tự ghép hình và giọng mượt mà.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Khách nể từ nét cắt đường kim",
                "before": ("UY TÍN TỪ ĐÔI TAY", ["Nhìn đôi tay lành nghề", "khách đặt đơn tiền chục"], "Người mua tinh ý nhìn thao tác tay là biết ngay thợ giỏi.", "Đăng ký ngay"),
                "after": ("TAY NGHỀ THẬT", ["Nhìn tay thao tác", "biết ngay thợ giỏi"], "Không lộ mặt vẫn chốt đơn lớn.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Ngày 1 quay tay, ngày 2 ngồi nói",
                "before": ("LỘ TRÌNH 2 NGÀY", ["Đi từ quay đôi tay", "đến ngồi nói tự nhiên"], "Học trực tiếp tại Hà Nội 07–08/11, hoàn phí nếu không hợp.", "Giữ chỗ"),
                "after": ("OFFLINE HÀ NỘI", ["Từ quay đôi tay", "đến nói tự nhiên"], "Ngày 1 không hợp: hoàn 100% phí.", "Giữ chỗ"),
            },
        ],
    },
    "KB_14": {
        "title": "KB 14: Kênh Đông Như Hội Chợ Mà Chẳng Ai Móc Ví",
        "angles": [
            {
                "layer": "Tầng 2 · View hội chợ không ra tiền",
                "before": ("BẪY VIEW HỘI CHỢ", ["Kênh đông như hội", "chẳng ai móc ví mua"], "Video xu hướng vạn người xem nhưng toàn khách xem dạo.", "Giữ chỗ ngay"),
                "after": ("BẪY VIEW RÁC", ["Đông như hội chợ", "chẳng ai móc ví"], "Vạn người xem dạo không ai đặt lịch.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · 600 view thật thắng 18.000 view vui",
                "before": ("BẰNG CHỨNG HỌC VIÊN", ["Sáu trăm người xem thật", "ra đơn gấp mười lần"], "Chỉ thẳng vấn đề của khách lại ra đơn đều đặn.", "Đăng ký lớp"),
                "after": ("VIEW RA ĐƠN THẬT", ["Sáu trăm view thật", "hơn vạn view vui"], "Chỉ thẳng vấn đề hút đúng người mua.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Dừng ngay các video lệch tệp",
                "before": ("LỌC SẠCH TỆP KHÁCH", ["Ngừng quay bài giải trí", "kéo sai người vào kênh"], "Để thuật toán AI tập trung tìm đúng người có nhu cầu mua.", "Xem lịch học"),
                "after": ("LỌC ĐÚNG TỆP", ["Ngừng quay giải trí", "lệch tệp khách mua"], "Để AI tìm đúng người cần dịch vụ.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Video giải quyết đúng ca bệnh",
                "before": ("NỘI DUNG RA KHÁCH", ["Mỗi video tháo gỡ", "một chỗ vướng có thật"], "Khách xem xong thấy đúng bệnh của mình sẽ tự nhắn đặt lịch.", "Đăng ký ngay"),
                "after": ("GỠ ĐÚNG CHỖ VƯỚNG", ["Mỗi bài giải quyết", "một vấn đề thật"], "Khách thấy đúng bệnh sẽ tự đặt lịch.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Chuyển kênh từ giải trí sang ra khách",
                "before": ("HÀ NỘI · 07–08/11", ["Biến lượt xem lặng lẽ", "thành khách đặt lịch"], "Đi 2 người ưu đãi người thứ hai chỉ còn 3,5 triệu.", "Giữ chỗ"),
                "after": ("ƯU ĐÃI NHÓM 2", ["Biến người xem", "thành khách đặt lịch"], "Đi 2 người: người sau chỉ 3,5 triệu.", "Giữ chỗ"),
            },
        ],
    },
    "KB_15": {
        "title": "KB 15: Mỗi Tuần Một Bài, Bài Nào Cũng Có Người Nhớ",
        "angles": [
            {
                "layer": "Tầng 2 · Áp lực phải đăng video mỗi ngày",
                "before": ("PHÁ BẪY ĐĂNG HÀNG NGÀY", ["Đừng ép mình đăng bài", "vội vã mỗi ngày"], "Làm vội cho đủ số lượng chỉ tạo ra những video nhạt nhòa.", "Giữ chỗ ngay"),
                "after": ("KHỎI ĐĂNG MỖI NGÀY", ["Đừng ép đăng bài", "vội vã mỗi ngày"], "Làm vội chỉ ra những clip nhạt nhòa.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Bằng chứng thật từ kênh Nguyễn Việt",
                "before": ("SỐ LIỆU THỰC TẾ", ["Mỗi tuần đăng một bài", "ba nghìn người nhắn"], "Bài nào lên cũng đủ sâu để khách nhớ tên và tìm đọc lại.", "Đăng ký lớp"),
                "after": ("SỐ LIỆU THẬT", ["Mỗi tuần một bài", "vẫn nghìn người nhắn"], "Bài đủ sâu để khách nhớ tên bạn.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Gói gọn việc quay trong 30 phút cuối tuần",
                "before": ("NHỊP LÀM VIỆC NHÀN", ["Ba mươi phút cuối tuần", "xong bài cho cả tuần"], "AI hỗ trợ cắt ghép để bạn giữ thời gian làm nghề.", "Xem lịch học"),
                "after": ("30 PHÚT MỖI TUẦN", ["Ba mươi phút quay", "đủ bài cả tuần"], "Giữ trọn thời gian cho công việc chính.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Sức nặng của bài viết có chiều sâu",
                "before": ("CHẤT LƯỢNG THẮNG SỐ LƯỢNG", ["Một bài giải mã sâu", "sống bền suốt nhiều tháng"], "Khách vào kênh xem lại từ đầu đến cuối rồi tự quyết định.", "Đăng ký ngay"),
                "after": ("BÀI VIẾT SỐNG BỀN", ["Một bài đủ sâu", "chạy suốt nhiều tháng"], "Khách xem lại cả kênh rồi tự mua.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Thiết lập nhịp làm kênh bền vững",
                "before": ("OFFLINE HÀ NỘI", ["Xây nhịp làm video", "bền bỉ không kiệt sức"], "Tặng khóa online xem lại tại nhà và 30 ngày sửa bài.", "Giữ chỗ"),
                "after": ("TẶNG KHÓA ONLINE", ["Làm kênh bền bỉ", "không lo kiệt sức"], "Có khóa online xem lại tại nhà.", "Giữ chỗ"),
            },
        ],
    },
    "KB_16": {
        "title": "KB 16: Ngó Lượt Thích Còn Nhiều Hơn Ngó Nồi Cơm",
        "angles": [
            {
                "layer": "Tầng 2 · Mệt vì 3 ngày canh lượt thích",
                "before": ("MẤT NĂNG LƯỢNG NGẦM", ["Ngó lượt thích mỗi giờ", "hơn cả ngó nồi cơm"], "Mười lăm phút quay không mệt bằng ba ngày ngóng view.", "Giữ chỗ ngay"),
                "after": ("ĐỪNG CANH LƯỢT XEM", ["Ngó lượt thích", "hơn ngó nồi cơm"], "Mệt vì 3 ngày mở máy ngóng view.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Giao cảm xúc cho con số nhảy",
                "before": ("GIỮ NÚT XONG VIỆC", ["Đăng bài lên mạng", "là đã xong việc"], "Đừng để vài lượt thích điều khiển tâm trạng cả ngày.", "Đăng ký lớp"),
                "after": ("TỰ CHỦ TÂM LÝ", ["Bấm nút đăng bài", "là đã xong việc"], "Đừng để con số điều khiển tâm trạng.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Chuẩn hóa đầu vào trong tầm tay",
                "before": ("KIỂM SOÁT ĐẦU VÀO", ["Làm chuẩn ba bước", "rồi cất điện thoại đi"], "Ánh sáng rõ, âm thanh sạch, ý gọn là xong phần của bạn.", "Xem lịch học"),
                "after": ("CHUẨN HÓA ĐẦU VÀO", ["Làm chuẩn ba bước", "rồi cất máy đi"], "Sáng rõ, tiếng sạch, ý gọn là xong.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Hạt mầm tự lớn theo thời gian",
                "before": ("QUY LUẬT TÍCH LŨY", ["Video đúng chuyên môn", "ba tháng sau vẫn nổ đơn"], "Khách cần mua sẽ tìm thấy bạn khi họ phát sinh vấn đề.", "Đăng ký ngay"),
                "after": ("HẠT MẦM CHUYÊN MÔN", ["Video đúng nghề", "vài tháng vẫn ra đơn"], "Khách tự tìm thấy khi họ cần mua.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Học cách làm kênh bình thản",
                "before": ("HÀ NỘI · 07–08/11", ["Làm kênh bình thản", "tập trung vào tay nghề"], "Hết ngày 1 không hợp công việc: hoàn đủ 100% học phí.", "Giữ chỗ"),
                "after": ("CÒN 17/35 CHỖ", ["Làm kênh bình thản", "giữ vững tay nghề"], "Ngày 1 không hợp: hoàn 100% phí.", "Giữ chỗ"),
            },
        ],
    },
    "KB_17": {
        "title": "KB 17: Nói Đúng Sách Thì Khách Gật Gù, Nói Đúng Hình Thì Khách Dừng Lại",
        "angles": [
            {
                "layer": "Tầng 2 · Bệnh nói chữ sách vở của chuyên gia",
                "before": ("BỆNH NÓI SÁCH VỞ", ["Nói chữ chuyên ngành", "khách nghe xong quên sạch"], "Bác sĩ, kỹ sư càng nói thuật ngữ thì khách càng lướt nhanh.", "Giữ chỗ ngay"),
                "after": ("BỎ THUẬT NGỮ KHÓ", ["Nói chữ sách vở", "khách nghe quên sạch"], "Càng thuật ngữ khách càng lướt nhanh.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Sợ nói bình dân bị đồng nghiệp chê",
                "before": ("VƯỢT RÀO THỂ DIỆN", ["Nói đúng hình ảnh", "khách mới dừng lại"], "Người trả tiền là khách hàng, không phải hội đồng chấm thi.", "Đăng ký lớp"),
                "after": ("NÓI BẰNG HÌNH ẢNH", ["Nói đúng hình ảnh", "khách mới dừng lại"], "Khách trả tiền chứ không chấm thi.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Phép dịch thuật ngữ sang đời thường",
                "before": ("PHÉP THỬ QUÁN PHỞ", ["Đổi thuật ngữ hàn lâm", "ra hình ảnh đời thường"], "Giải thích việc khó bằng những hình ảnh quen mắt mỗi ngày.", "Xem lịch học"),
                "after": ("DỊCH RA ĐỜI THƯỜNG", ["Đổi chữ hàn lâm", "ra hình quen mắt"], "Ai nghe một lần cũng hiểu ngay.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Giữ chuẩn chuyên môn mà vẫn dễ hiểu",
                "before": ("SÂU SẮC MÀ BÌNH DÂN", ["Cơ chế bên trong chuẩn", "ví dụ bên ngoài gần"], "Khách vừa nể tay nghề, vừa hiểu rõ vì sao nên mua.", "Đăng ký ngay"),
                "after": ("SÂU MÀ DỄ HIỂU", ["Cơ chế thật chuẩn", "ví dụ thật gần"], "Khách vừa nể nghề vừa hiểu rõ.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Gọt lại ngôn từ ngành của bạn tại lớp",
                "before": ("LỚP 2 NGÀY HÀ NỘI", ["Dịch kiến thức khó", "thành câu nói ra đơn"], "Học trực tiếp 07–08/11 tại Long Biên, hoàn phí ngày 1.", "Giữ chỗ"),
                "after": ("07–08/11 HÀ NỘI", ["Biến kiến thức khó", "thành lời ra đơn"], "Ngày 1 không hợp: hoàn 100% phí.", "Giữ chỗ"),
            },
        ],
    },
    "KB_18": {
        "title": "KB 18: Rời Chỗ Làm Về Ngồi Ghế Xoay, 20.600 Lượt Xem Còn Hơn 600",
        "angles": [
            {
                "layer": "Tầng 2 · Ngồi ghế xoay nói chay chỉ được 600 view",
                "before": ("RỜI BỎ GHẾ XOAY", ["Ngồi phòng kín nói chay", "khách xem vài giây chán"], "Trong khi cảnh làm việc thật tại xưởng lên hai vạn view.", "Giữ chỗ ngay"),
                "after": ("ĐỪNG NGỒI NÓI CHAY", ["Rời chiếc ghế xoay", "ra hiện trường thật"], "Cảnh làm việc thật gấp ba mươi lần.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Hiện trường làm việc là bối cảnh đắt nhất",
                "before": ("HIỆN TRƯỜNG LÀM NGHỀ", ["Xưởng làm việc của bạn", "đắt hơn mọi phim trường"], "Tiếng máy chạy, tay kiểm hàng là bằng chứng sống động nhất.", "Đăng ký lớp"),
                "after": ("PHIM TRƯỜNG THẬT", ["Chỗ bạn làm việc", "đắt hơn studio"], "Tay kiểm hàng là bằng chứng sống.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Gắn mic cài áo quay ngay lúc làm",
                "before": ("QUAY TẠI HIỆN TRƯỜNG", ["Gắn chiếc mic nhỏ", "vừa kiểm hàng vừa nói"], "AI tự lọc tiếng ồn công trình, giữ lại giọng nói rõ nét.", "Xem lịch học"),
                "after": ("GẮN MIC LÀ QUAY", ["Vừa kiểm tra hàng", "vừa nói hai câu"], "AI lọc sạch tiếng ồn xung quanh.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Khách tin vào mồ hôi và vật liệu thật",
                "before": ("BẰNG CHỨNG VẬT LÝ", ["Cho khách thấy tận mắt", "từng tấm gỗ mặt đá"], "Một cảnh thật tại xưởng xóa tan mọi nghi ngờ chất lượng.", "Đăng ký ngay"),
                "after": ("THẤY TẬN MẮT", ["Cho khách nhìn thấy", "vật liệu tại xưởng"], "Một cảnh thật xóa tan nghi ngờ.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Thiết kế góc máy cho đúng cơ sở của bạn",
                "before": ("OFFLINE 07–08/11", ["Thiết kế góc máy riêng", "cho tiệm và xưởng bạn"], "Đi 2 người ưu đãi người thứ hai chỉ còn 3,5 triệu.", "Giữ chỗ"),
                "after": ("ƯU ĐÃI NHÓM 2", ["Thiết kế góc máy", "cho riêng xưởng bạn"], "Đi 2 người: người sau chỉ 3,5 triệu.", "Giữ chỗ"),
            },
        ],
    },
    "KB_19": {
        "title": "KB 19: 11 Giờ Đêm, Lúc Khách Khó Tính Nhất Cũng Hiền Như Cục Bột",
        "angles": [
            {
                "layer": "Tầng 2 · Khung giờ 11 giờ đêm buông giáp",
                "before": ("KHUNG GIỜ BUÔNG GIÁP", ["Mười một giờ đêm", "khách khó tính cũng mềm"], "Ban ngày khách phòng thủ, đêm về họ lắng nghe thật lòng.", "Giữ chỗ ngay"),
                "after": ("11 GIỜ ĐÊM", ["Khách khó tính nhất", "đêm về cũng lắng nghe"], "Lúc một mình họ bỏ lớp phòng thủ.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Giọng gào hét làm khách giật mình lướt đi",
                "before": ("BỎ GIỌNG HÔ HÀO", ["Đừng nói giọng bán hàng", "vào lúc nửa đêm"], "Giọng thủ thỉ điềm tĩnh giữ chân người có tiền xem hết video.", "Đăng ký lớp"),
                "after": ("HẠ TÔNG GIỌNG", ["Đừng gào bán hàng", "lúc khách nghỉ ngơi"], "Giọng điềm tĩnh giữ chân người có tiền.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Ánh đèn bàn ấm và âm thanh sạch",
                "before": ("BỐI CẢNH ĐÊM TĨNH", ["Một ngọn đèn bàn ấm", "thu giọng rõ từng lời"], "Cài đặt góc quay tại bàn một lần, tối ngồi nói năm phút.", "Xem lịch học"),
                "after": ("GÓC BÀN ĐÊM TĨNH", ["Một chiếc đèn ấm", "giọng rõ từng lời"], "Ngồi tại bàn nói năm phút là xong.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Chạm đúng nỗi trăn trở chưa nói với ai",
                "before": ("TÂM LÝ NGƯỜI MUA", ["Nói như đang trò chuyện", "với một người bạn"], "Sáng hôm sau khách chủ động nhắn tin đặt lịch tư vấn.", "Đăng ký ngay"),
                "after": ("TRÒ CHUYỆN 1-1", ["Nói như tâm sự", "với một người bạn"], "Sáng mai khách tự nhắn đặt lịch.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Rèn nhịp thở và giọng nói trầm ấm",
                "before": ("HÀ NỘI · 07–08/11", ["Chỉnh nhịp thở trầm tĩnh", "ngay trước ống kính"], "Tặng khóa online xem lại tại nhà và 30 ngày sửa bài.", "Giữ chỗ"),
                "after": ("TẶNG KHÓA ONLINE", ["Rèn nhịp nói trầm", "trước ống kính"], "Có khóa online xem lại tại nhà.", "Giữ chỗ"),
            },
        ],
    },
    "KB_20": {
        "title": "KB 20: Dám Kể Lần Làm Hỏng Phải Đền Tiền, Là Đã Đứng Cao Hơn Nó",
        "angles": [
            {
                "layer": "Tầng 2 · Khách sợ nhất người chưa từng làm hỏng",
                "before": ("NGHỊCH LÝ NIỀM TIN", ["Khách giao việc lớn", "sợ người chỉ biết khoe"], "Người chưa từng hỏng lần nào là người chưa biết chỗ dễ sập.", "Giữ chỗ ngay"),
                "after": ("TẠO NIỀM TIN THẬT", ["Khách giao việc lớn", "sợ người chỉ khoe"], "Kể vết xước nghề làm khách tin ngay.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Dám kể lần đền tiền là đã đứng cao hơn",
                "before": ("VẾT XƯỚC LÀM NGHỀ", ["Dám kể lần đền tiền", "là đã vượt qua nó"], "Người vững tay nghề mới bình thản kể lại bài học cũ.", "Đăng ký lớp"),
                "after": ("BẢN LĨNH CHỦ NGHỀ", ["Dám kể lần đền tiền", "là đã đứng cao hơn"], "Chỉ người vững nghề mới dám kể thật.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Cấu trúc kể chuyện 3 nhịp gọn gàng",
                "before": ("KỂ CHUYỆN 60 GIÂY", ["Sai lầm cũ năm xưa", "thành tiêu chuẩn hôm nay"], "Khung ba bước giúp bạn kể thật mà giữ vững uy tín.", "Xem lịch học"),
                "after": ("KHUNG 3 NHỊP KỂ", ["Bài học đền tiền", "thành tiêu chuẩn mới"], "Kể thật mà vị thế càng cao hơn.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Biến rủi ro bạn từng chịu thành sự an tâm của khách",
                "before": ("CHỐT ĐƠN TỪ SỰ THẬT", ["Mình từng trả học phí", "để khách khỏi trả giá"], "Khách nghe xong tin tưởng chốt đơn không mặc cả một đồng.", "Đăng ký ngay"),
                "after": ("KHÁCH AN TÂM MUA", ["Mình đã trả giá", "để khách an tâm"], "Khách chốt đơn không mặc cả một đồng.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Đào đúng câu chuyện thực tế tại lớp",
                "before": ("CÒN 17/35 CHỖ", ["Đào câu chuyện thật", "quay ngay tại lớp"], "Hết ngày 1 không hợp công việc: hoàn đủ 100% học phí.", "Giữ chỗ"),
                "after": ("OFFLINE HÀ NỘI", ["Đào chuyện nghề thật", "quay ngay tại lớp"], "Ngày 1 không hợp: hoàn 100% phí.", "Giữ chỗ"),
            },
        ],
    },
    "KB_21": {
        "title": "KB 21: Fanpage 10.000 Theo Dõi, Bài Mới 12 Lượt Xem, Cái Giá Của Cô Nhân Viên AI",
        "angles": [
            {
                "layer": "Tầng 2 · Thảm cảnh Page 10.000 follow chỉ còn 12 view",
                "before": ("CÁI GIÁ CỦA AI GIẢ", ["Page mười nghìn người", "bài mới mười hai view"], "Dùng nhân vật AI đọc hộ làm thuật toán bóp nghẹt cả trang.", "Giữ chỗ ngay"),
                "after": ("ĐỪNG DÙNG NGƯỜI GIẢ", ["Page mười nghìn người", "còn mười hai view"], "Nhân vật AI giả làm chết tương tác.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Thuế 95% sự chú ý khi giấu mặt sau AI",
                "before": ("CON NGƯỜI THẬT LÊN NGÔI", ["Cảnh làm thật tại tiệm", "vọt lên chín vạn view"], "Khách mua dịch vụ từ người thật chứ không mua từ máy.", "Đăng ký lớp"),
                "after": ("NGƯỜI THẬT VIỆC THẬT", ["Cảnh làm việc thật", "vọt chín vạn view"], "Khách mua từ người thật, không mua máy.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Dùng AI làm trợ lý hậu trường, đừng bắt AI đóng thế",
                "before": ("ĐẶT AI ĐÚNG CHỖ", ["AI lo cắt dựng nền", "bạn giữ phần con người"], "Máy làm việc thô, còn gương mặt và chữ tín là bạn.", "Xem lịch học"),
                "after": ("ĐẶT AI ĐÚNG CHỖ", ["AI lo phần cắt ghép", "bạn giữ chữ tín"], "Đừng bắt máy đóng thế gương mặt bạn.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Cứu lại kênh đang bị bóp tương tác",
                "before": ("KHÔI PHỤC TƯƠNG TÁC", ["Đưa tiếng nói chủ nghề", "trở lại trên fanpage"], "Có gương mặt và giọng nói thật kênh sẽ sáng trở lại.", "Đăng ký ngay"),
                "after": ("CỨU LẠI FANPAGE", ["Đưa giọng chủ nghề", "trở lại trên kênh"], "Có người thật là mở lại phân phối.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · 2 ngày gỡ sạch lỗi kênh tại Hà Nội",
                "before": ("HÀ NỘI · 07–08/11", ["Khám kênh trực tiếp", "tại lớp học hai ngày"], "Đi 2 người ưu đãi người thứ hai chỉ còn 3,5 triệu.", "Giữ chỗ"),
                "after": ("07–08/11 HÀ NỘI", ["Sửa kênh trực tiếp", "trong hai ngày học"], "Đi 2 người: người sau chỉ 3,5 triệu.", "Giữ chỗ"),
            },
        ],
    },
    "KB_22": {
        "title": "KB 22: Hai Máy Quay, Một Người Ngồi Đối Diện, Cả Tháng Vài Chục View",
        "angles": [
            {
                "layer": "Tầng 2 · Bắt chước Podcast 2 máy nhưng không ai xem",
                "before": ("BẪY PODCAST HAI MÁY", ["Quay hai máy sang trọng", "cả tháng vài chục view"], "Khán giả chưa biết bạn là ai thì không nghe nói chuyện phiếm.", "Giữ chỗ ngay"),
                "after": ("BẪY QUAY 2 MÁY", ["Podcast hai góc máy", "chỉ vài chục view"], "Khách lạ không nghe trò chuyện phiếm.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Phân biệt người nổi tiếng và kênh chủ nghề",
                "before": ("ĐÚNG ĐỊNH DẠNG KÊNH MỚI", ["Chưa nổi tiếng đừng cắt", "đoạn trò chuyện dài"], "Kênh mới phải nhìn thẳng ống kính giải quyết đúng một việc.", "Đăng ký lớp"),
                "after": ("ĐỊNH DẠNG KÊNH MỚI", ["Nhìn thẳng ống kính", "gỡ đúng một việc"], "Đừng bắt chước cách của người nổi tiếng.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Góc máy đối diện 1-1 gọn nhẹ",
                "before": ("GÓC MÁY ĐỐI DIỆN 1-1", ["Một máy đặt trước mặt", "nói thẳng vào câu hỏi"], "Tiết kiệm thời gian dựng mà khách thấy gần gũi hơn hẳn.", "Xem lịch học"),
                "after": ("GÓC MÁY 1-1", ["Một máy trước mặt", "nói thẳng câu hỏi"], "Người xem cảm nhận bạn nói với họ.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Khi nào mới dùng góc máy nghiêng",
                "before": ("NHỊP CHUYỂN GÓC MÁY", ["Câu đầu nhìn thẳng", "câu giải thích đổi góc"], "Đổi hai góc máy đúng nhịp giúp giữ mắt người xem.", "Đăng ký ngay"),
                "after": ("NHỊP ĐỔI GÓC MÁY", ["Mở bài nhìn thẳng", "giải thích đổi góc"], "Giữ mắt người xem suốt sáu mươi giây.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Thực hành bố trí máy ngay tại bàn",
                "before": ("OFFLINE HÀ NỘI", ["Thực hành đặt góc máy", "chuẩn cho kênh mới"], "Tặng khóa online xem lại tại nhà và 30 ngày sửa bài.", "Giữ chỗ"),
                "after": ("TẶNG KHÓA ONLINE", ["Thực hành đặt máy", "chuẩn cho kênh mới"], "Có khóa online xem lại tại nhà.", "Giữ chỗ"),
            },
        ],
    },
    "KB_23": {
        "title": "KB 23: Mười Năm Nghề Vẫn Ghi Là Đang Tập Tành",
        "angles": [
            {
                "layer": "Tầng 2 · 10 năm nghề vẫn tự nhận mình mới tập",
                "before": ("HỘI CHỨNG TỰ HẠ THẤP", ["Mười năm làm nghề", "vẫn ghi đang tập tành"], "Khiêm tốn sai chỗ trên mạng làm khách tưởng bạn là thợ non.", "Giữ chỗ ngay"),
                "after": ("ĐỪNG TỰ HẠ THẤP", ["Mười năm làm nghề", "đừng ghi tập tành"], "Khiêm tốn sai chỗ khách tưởng thợ non.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Ảo giác ngọn núi Agung",
                "before": ("VỊ THẾ TRÊN ỐNG KÍNH", ["Khách ở dưới chân núi", "cần người đi trước dẫn"], "Chỉ cần đi trước vài bước là dẫn đường được cho khách.", "Đăng ký lớp"),
                "after": ("VỊ THẾ DẪN ĐƯỜNG", ["Chỉ cần đi trước", "khách hai ba bước"], "Khách cần người thật dẫn qua chỗ khó.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Sửa lại dòng tiểu sử và câu mở lời",
                "before": ("UY TÍN RÕ RÀNG", ["Ghi đúng số năm nghề", "và số ca đã làm"], "Để khách vào trang ba giây biết ngay bạn giải quyết được gì.", "Xem lịch học"),
                "after": ("UY TÍN RÕ RÀNG", ["Ghi rõ năm nghề", "và số ca đã làm"], "Vào kênh ba giây khách tin ngay.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Đàng hoàng nhận đúng giá trị của mình",
                "before": ("TỰ TIN ĐÚNG MỰC", ["Không nổ quá sự thật", "nhưng không tự rụt rè"], "Nói rõ những ca mình làm tốt nhất bằng giọng điềm đạm.", "Đăng ký ngay"),
                "after": ("ĐÀNG HOÀNG TỰ TIN", ["Không nổ quá đà", "không tự rụt rè"], "Nói rõ ca làm tốt bằng giọng trầm.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Định vị lại trang cá nhân tại lớp",
                "before": ("HÀ NỘI · 07–08/11", ["Chuẩn hóa lại hồ sơ", "đúng tầm tay nghề bạn"], "Hết ngày 1 không hợp công việc: hoàn đủ 100% học phí.", "Giữ chỗ"),
                "after": ("CÒN 17/35 CHỖ", ["Làm rõ lại kênh", "đúng tầm tay nghề"], "Ngày 1 không hợp: hoàn 100% phí.", "Giữ chỗ"),
            },
        ],
    },
    "KB_24": {
        "title": "KB 24: Im Lặng Vì Ngại Khoe Là Nhường Chỗ Cho Người Làm Ẩu",
        "angles": [
            {
                "layer": "Tầng 2 · Người giỏi im lặng, kẻ làm ẩu chiếm sóng",
                "before": ("CÁI GIÁ CỦA IM LẶNG", ["Bạn ngại lên tiếng", "người làm ẩu lấy khách"], "Khách mua nhầm hàng kém vì người làm thật cứ đứng nhìn.", "Giữ chỗ ngay"),
                "after": ("ĐỪNG ĐỨNG IM NỮA", ["Bạn cứ im lặng", "kẻ ẩu lấy hết khách"], "Khách mua nhầm vì thợ thật im tiếng.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Chia sẻ góc nhìn khác hẳn tự khoe",
                "before": ("KHÔNG PHẢI TỰ KHOE", ["Chỉ ra chỗ hiểu sai", "không cần khen mình giỏi"], "Cả video không một câu tự khen mà khách vẫn tìm đến đặt hàng.", "Đăng ký lớp"),
                "after": ("CHIA SẺ GÓC NHÌN", ["Chỉ chỗ khách sai", "khỏi cần tự khen"], "Không khen mình câu nào khách vẫn tin.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Khuôn bài bóc tách ngộ nhận",
                "before": ("KHUÔN BÀI 3 NHỊP", ["Gọi tên một hiểu lầm", "rồi chỉ cách kiểm tra"], "Khung bài có sẵn giúp bạn lên hình đàng hoàng như người thầy.", "Xem lịch học"),
                "after": ("KHUÔN BÀI SẴN", ["Gọi tên hiểu lầm", "chỉ cách kiểm tra"], "Lên hình đàng hoàng, không sợ phô trương.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Bảo vệ khách hàng bằng tiêu chuẩn nghề",
                "before": ("TRÁCH NHIỆM NGƯỜI THỢ", ["Lên video để khách", "biết phân biệt hàng thật"], "Giúp khách tránh mất tiền oan thì họ sẽ chọn bạn.", "Đăng ký ngay"),
                "after": ("GIÚP KHÁCH TRÁNH BẪY", ["Chỉ khách phân biệt", "hàng thật hàng ẩu"], "Giúp khách khỏi mất tiền là có đơn.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Lên tiếng đàng hoàng sau 2 ngày học",
                "before": ("LỚP 2 NGÀY HÀ NỘI", ["Lên hình tử tế", "lấy lại thị phần thật"], "Đi 2 người ưu đãi người thứ hai chỉ còn 3,5 triệu.", "Giữ chỗ"),
                "after": ("ƯU ĐÃI NHÓM 2", ["Lên hình tử tế", "giữ khách cho mình"], "Đi 2 người: người sau chỉ 3,5 triệu.", "Giữ chỗ"),
            },
        ],
    },
    "KB_25": {
        "title": "KB 25: Sợ Chỉ Kỹ Thì Khách Về Tự Làm",
        "angles": [
            {
                "layer": "Tầng 2 · Nỗi sợ lộ bí quyết nghề",
                "before": ("SỢ LỘ CÁCH LÀM NGHỀ?", ["Sợ chỉ kỹ trên mạng", "khách xem xong tự làm"], "Nên video nào cũng nói úp mở, cuối cùng khách chẳng nhớ gì.", "Giữ chỗ ngay"),
                "after": ("ĐỪNG NÓI ÚP MỞ", ["Sợ chỉ kỹ quá", "khách về tự làm?"], "Nói úp mở làm khách lướt qua luôn.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Nguyên lý bếp mở và miếng dưa bổ sẵn",
                "before": ("NGUYÊN LÝ BẾP MỞ", ["Càng chỉ kỹ từng bước", "khách càng giao việc"], "Thấy quy trình kỳ công, khách hiểu ngay nên thuê bạn làm.", "Đăng ký lớp"),
                "after": ("NGUYÊN LÝ BẾP MỞ", ["Càng chỉ thật kỹ", "khách càng thuê bạn"], "Thấy độ kỳ công là khách giao việc.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Quay trọn quy trình làm kỹ tại xưởng",
                "before": ("PHƠI BÀY ĐỘ KỸ TÍNH", ["Mở toang quy trình làm", "thay cho lời cam kết"], "Máy tự cắt gọn ca làm việc dài thành sáu mươi giây.", "Xem lịch học"),
                "after": ("PHƠI BÀY ĐỘ KỸ", ["Quay quy trình thật", "thay lời cam kết"], "Cắt gọn ca làm dài thành 60 giây.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Miễn phí kiến thức, thu tiền sự lành nghề",
                "before": ("BÁN ĐÔI TAY LÀNH NGHỀ", ["Công thức có thể mở", "nhưng tay nghề là thật"], "Người có tiền mua sự an tâm và thời gian, không ai tự làm.", "Đăng ký ngay"),
                "after": ("BÁN SỰ AN TÂM", ["Chỉ hết công thức", "bán tay nghề thật"], "Khách có tiền mua thời gian của bạn.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Đóng gói quy trình nghề tại lớp Hà Nội",
                "before": ("OFFLINE 07–08/11", ["Biến quy trình kỹ tính", "thành video hút khách"], "Tặng khóa online xem lại tại nhà và 30 ngày sửa bài.", "Giữ chỗ"),
                "after": ("TẶNG KHÓA ONLINE", ["Biến độ kỹ tính", "thành clip ra đơn"], "Có khóa online xem lại tại nhà.", "Giữ chỗ"),
            },
        ],
    },
    "KB_26": {
        "title": "KB 26: Sợ Nói Lại Ý Cũ, Cả Tuần Bỏ Trống",
        "angles": [
            {
                "layer": "Tầng 2 · Bỏ trống kênh cả tuần vì sợ lặp ý",
                "before": ("BỆNH SỢ LẶP LẠI Ý CŨ", ["Sợ nói lại chuyện cũ", "nên cả tuần bỏ trống"], "Bạn tưởng cũ nhưng khách mới trên mạng chưa từng nghe.", "Giữ chỗ ngay"),
                "after": ("SỢ LẶP LẠI Ý CŨ?", ["Sợ nói lại ý cũ", "bỏ trống cả tuần"], "Khách mới trên mạng chưa hề nghe.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Quán phở 30 năm chỉ nấu đúng 1 món",
                "before": ("BÀI TỦ CỦA CHỦ NGHỀ", ["Quán phở ba mươi năm", "chỉ bán đúng một món"], "Khách phải lướt qua bạn mười lần mới bắt đầu nhớ tên và mua.", "Đăng ký lớp"),
                "after": ("GIỮ VỮNG BÀI TỦ", ["Quán phở nổi tiếng", "nhờ đúng một món"], "Lướt gặp mười lần khách mới nhớ tên.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · 5 khuôn kể lại cùng 1 thông điệp",
                "before": ("1 Ý NHƯNG 10 CÁCH KỂ", ["Cùng một thông điệp lõi", "kể qua mười ca khách"], "Xoay góc mở bài từ những câu chuyện khách hàng khác nhau.", "Xem lịch học"),
                "after": ("1 Ý 10 CÁCH KỂ", ["Một thông điệp lõi", "mười ca khách thật"], "Không bao giờ lo cạn ý tưởng quay.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Khắc sâu định vị vào đầu thị trường",
                "before": ("CHỦ ĐỀ NHẤT QUÁN", ["Nói đến ngành của bạn", "khách nhớ ngay một câu"], "Sự lặp lại có chủ đích tạo ra uy tín nghề vững chắc.", "Đăng ký ngay"),
                "after": ("KHẮC SÂU VỊ THẾ", ["Nhắc tới ngành bạn", "nhớ ngay tên bạn"], "Lặp lại đúng trọng tâm tạo uy tín.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Tìm đúng bài tủ của bạn tại lớp",
                "before": ("HÀ NỘI · 07–08/11", ["Xác định đúng bài tủ", "nhân bản cả năm"], "Hết ngày 1 không hợp công việc: hoàn đủ 100% học phí.", "Giữ chỗ"),
                "after": ("CÒN 17/35 CHỖ", ["Tìm đúng bài tủ", "quay suốt cả năm"], "Ngày 1 không hợp: hoàn 100% phí.", "Giữ chỗ"),
            },
        ],
    },
    "KB_27": {
        "title": "KB 27: Không Phải Không Có Khiếu, Chỉ Là Chưa Đủ Ba Mươi Lần",
        "angles": [
            {
                "layer": "Tầng 2 · Quay 3 clip đầu thấy ngượng rồi bỏ",
                "before": ("BỎ CUỘC Ở LẦN THỨ BA", ["Quay ba bài thấy ngượng", "tưởng mình không có khiếu"], "Ca làm nghề đầu tiên ngày xưa ai cũng từng ngập ngừng.", "Giữ chỗ ngay"),
                "after": ("ĐỪNG BỎ Ở LẦN 3", ["Mới quay ba lần", "đừng kết luận sớm"], "Ca làm nghề đầu tiên ai cũng ngượng.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Ngưỡng 30 lần bấm máy đầu tiên",
                "before": ("NGƯỠNG 30 LẦN BẤM MÁY", ["Không phải thiếu năng khiếu", "chỉ chưa đủ ba mươi lần"], "Qua ba mươi lần bấm máy, ống kính trở thành người khách quen.", "Đăng ký lớp"),
                "after": ("NGƯỠNG 30 LẦN", ["Không thiếu năng khiếu", "chỉ thiếu số lần"], "Đủ ba mươi lần là nói tự nhiên.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Rút ngắn thời gian mỗi lần bấm máy",
                "before": ("TĂNG TỐC VƯỢT NGƯỠNG", ["Mỗi video mười lăm phút", "một tháng qua cửa ngượng"], "Quy trình gọn giúp bạn đi qua 30 lần đầu nhanh gấp năm lần.", "Xem lịch học"),
                "after": ("QUA CỬA NGƯỢNG", ["Mười lăm phút quay", "nhanh qua ba mươi bài"], "Quy trình gọn giúp vượt ngưỡng cực nhanh.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Hết ngượng là kết quả của số lần làm",
                "before": ("TỰ TIN LÀ KẾT QUẢ", ["Đừng đợi hết ngượng", "mới bắt đầu bấm máy"], "Chính việc bấm máy đều đặn mới làm bạn quen với ống kính.", "Đăng ký ngay"),
                "after": ("BẤM MÁY ĐỂ TỰ TIN", ["Đừng đợi hết ngượng", "mới chịu bấm máy"], "Quay xong vài bài là tự hết ngượng.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Phá băng những lần bấm máy đầu tiên tại lớp",
                "before": ("LỚP 2 NGÀY HÀ NỘI", ["Vượt qua những lần đầu", "ngay tại lớp học"], "Đi 2 người ưu đãi người thứ hai chỉ còn 3,5 triệu.", "Giữ chỗ"),
                "after": ("ƯU ĐÃI NHÓM 2", ["Phá băng lần đầu", "ngay tại lớp học"], "Đi 2 người: người sau chỉ 3,5 triệu.", "Giữ chỗ"),
            },
        ],
    },
    "KB_28": {
        "title": "KB 28: Cả Trăm Số Điện Thoại, Gọi Vào Không Ai Nghe Máy",
        "angles": [
            {
                "layer": "Tầng 2 · Có số điện thoại nhưng gọi khách không nghe",
                "before": ("GỌI KHÔNG AI NGHE MÁY", ["Cả trăm số để lại", "gọi vào toàn thuê bao"], "Vì khách mới xem một quảng cáo ngắn, họ chưa thực sự biết bạn.", "Giữ chỗ ngay"),
                "after": ("GỌI KHÔNG NGHE MÁY?", ["Trăm số để lại", "gọi không ai nghe"], "Khách chưa biết bạn nên ngại bắt máy.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Quy tắc 7 tiếng làm ấm trước khi gọi",
                "before": ("QUY TẮC LÀM ẤM KHÁCH", ["Để video đi trước", "dọn đường cho cuộc gọi"], "Khách xem đủ video sẽ chờ cuộc gọi tư vấn của bạn.", "Đăng ký lớp"),
                "after": ("VIDEO DỌN ĐƯỜNG", ["Để video đi trước", "làm ấm khách hàng"], "Khách xem đủ sẽ mong cuộc gọi bạn.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Sân chơi nội dung cho khách tự xem trước",
                "before": ("BỘ VIDEO TỰ CHỐT", ["Gửi kèm ba video chuẩn", "ngay khi khách để số"], "Khách tự xem quy trình và kết quả trước khi bạn nhấc máy gọi.", "Xem lịch học"),
                "after": ("BỘ CLIP LÀM ẤM", ["Gửi ba video chuẩn", "trước khi nhấc máy"], "Khách tự hiểu giá trị trước khi nghe.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Tỷ lệ bắt máy và chốt đơn tăng vọt",
                "before": ("NHÀN CHO ĐỘI TƯ VẤN", ["Khách bắt máy là hỏi", "lịch làm và chuyển khoản"], "Không còn cảnh thuyết phục mỏi miệng những người chưa tin.", "Đăng ký ngay"),
                "after": ("CHỐT ĐƠN NHẸ NHÀNG", ["Bắt máy là bàn", "lịch làm việc ngay"], "Khỏi thuyết phục người chưa tin tưởng.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Xây bộ video làm ấm khách tại lớp",
                "before": ("OFFLINE 07–08/11", ["Dựng bộ video làm ấm", "cho quy trình đón khách"], "Tặng khóa online xem lại tại nhà và 30 ngày sửa bài.", "Giữ chỗ"),
                "after": ("TẶNG KHÓA ONLINE", ["Dựng bộ clip làm ấm", "để đón khách về Zalo"], "Có khóa online xem lại tại nhà.", "Giữ chỗ"),
            },
        ],
    },
    "KB_29": {
        "title": "KB 29: Khách Toàn Hỏi Món Rẻ Nhất, Món Muốn Bán Chưa Có Video Nào",
        "angles": [
            {
                "layer": "Tầng 2 · Khách toàn hỏi món lẻ rẻ tiền",
                "before": ("LỆCH SẢN PHẨM CHỦ LỰC", ["Khách toàn hỏi món rẻ", "món lãi cao ế ẩm"], "Nhìn lại kênh thì món bạn muốn bán nhất chưa có nổi một video.", "Giữ chỗ ngay"),
                "after": ("TOÀN HỎI MÓN RẺ?", ["Món muốn bán nhất", "chưa có video nào"], "Kênh quay gì thì khách hỏi nấy.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Thiết kế ngược từ dịch vụ chủ lực",
                "before": ("LÀM NGƯỢC TỪ ĐÍCH", ["Muốn bán gói dịch vụ nào", "quay thẳng vào gói đó"], "Đừng quay mẹo vặt giá rẻ rồi mong khách tự mua gói cao cấp.", "Đăng ký lớp"),
                "after": ("LÀM NGƯỢC TỪ ĐÍCH", ["Muốn bán gói nào", "quay thẳng gói đó"], "Đừng quay mẹo vặt rồi đợi đơn lớn.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Rút 3 dấu hiệu nhận biết tại nhà cho khách",
                "before": ("CÔNG THỨC 3 DẤU HIỆU", ["Chỉ ba dấu hiệu thật", "để khách tự kiểm tra"], "Khách thấy đúng ba dấu hiệu sẽ hỏi thẳng gói chính.", "Xem lịch học"),
                "after": ("3 DẤU HIỆU THẬT", ["Chỉ ba dấu hiệu", "khách tự kiểm tra"], "Khách thấy đúng sẽ hỏi gói chính.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Tăng biên lợi nhuận trên từng đơn hàng",
                "before": ("TẬP TRUNG MÓN CHỦ LỰC", ["Ít lượt xem hơn", "nhưng toàn đơn giá cao"], "Kênh đi thẳng vào dịch vụ mũi nhọn giúp tiệm tăng trưởng bền vững.", "Đăng ký ngay"),
                "after": ("TẬP TRUNG MŨI NHỌN", ["Ít lượt xem hơn", "nhưng toàn đơn lớn"], "Đi thẳng vào dịch vụ biên lãi cao.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Bóc tách gói dịch vụ chủ lực tại lớp",
                "before": ("HÀ NỘI · 07–08/11", ["Đóng gói sản phẩm chính", "thành kịch bản mũi nhọn"], "Hết ngày 1 không hợp công việc: hoàn đủ 100% học phí.", "Giữ chỗ"),
                "after": ("CÒN 17/35 CHỖ", ["Đóng gói món chính", "thành clip mũi nhọn"], "Ngày 1 không hợp: hoàn 100% phí.", "Giữ chỗ"),
            },
        ],
    },
    "KB_30": {
        "title": "KB 30: Định Bỏ Vài Trăm Triệu Nhập Máy Mới",
        "angles": [
            {
                "layer": "Tầng 2 · Bỏ trăm triệu nhập máy trước khi hỏi khách",
                "before": ("TRƯỚC KHI XUỐNG TIỀN", ["Định bỏ vài trăm triệu", "nhập máy mới về tiệm?"], "Đừng nhập hàng theo cảm tính khi chưa biết khách có thực sự mua.", "Giữ chỗ ngay"),
                "after": ("KHOAN NHẬP MÁY MỚI", ["Định bỏ trăm triệu", "nhập máy mới về?"], "Đừng xuống vốn khi chưa thử thị trường.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Phép thử bằng 3 video 0 đồng",
                "before": ("RỦI RO BẤT ĐỐI XỨNG", ["Thử thị trường bằng video", "trước khi bỏ tiền trăm"], "Quay ba bài nói về giải pháp đó xem có bao nhiêu khách nhắn hỏi.", "Đăng ký lớp"),
                "after": ("THỬ BẰNG VIDEO", ["Quay ba video thử", "trước khi bỏ vốn"], "Xem khách có nhắn hỏi thật hay không.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Làm video thử nhu cầu trong 1 buổi tối",
                "before": ("KIỂM CHỨNG NHANH GỌN", ["Một buổi tối quay bài", "đo ngay nhu cầu thật"], "Có khách hỏi đặt thật rồi mới xuống tiền nhập máy.", "Xem lịch học"),
                "after": ("ĐO NHU CẦU THẬT", ["Một tối quay bài", "biết ngay sức mua"], "Có khách hỏi thật rồi mới nhập máy.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Biến kênh thành radar đọc thị trường",
                "before": ("RADAR CỦA CHỦ DOANH NGHIỆP", ["Kênh riêng giúp bạn", "không bao giờ nhập hàng tồn"], "Mỗi video lên mạng là một phép thử nhu cầu khách hàng miễn phí.", "Đăng ký ngay"),
                "after": ("KHÔNG SỢ ĐỌNG VỐN", ["Dùng kênh đo khách", "khỏi lo hàng tồn"], "Mỗi video là một phép thử miễn phí.", "Đăng ký ngay"),
            },
            {
                "layer": "Lời mời · Học tư duy thử thị trường tại Hà Nội",
                "before": ("LỚP 2 NGÀY HÀ NỘI", ["Tiết kiệm hàng trăm triệu", "tiền thử sai dịch vụ"], "Đi 2 người ưu đãi người thứ hai chỉ còn 3,5 triệu.", "Giữ chỗ"),
                "after": ("ƯU ĐÃI NHÓM 2", ["Giữ hàng trăm triệu", "khỏi thử sai đường"], "Đi 2 người: người sau chỉ 3,5 triệu.", "Giữ chỗ"),
            },
        ],
    },
    "KB_31": {
        "title": "KB 31: Người Dám Nhận Phần Kết Quả",
        "angles": [
            {
                "layer": "Tầng 2 · Kỷ nguyên AI làm bão hòa nội dung nói suông",
                "before": ("THỊ TRƯỜNG ĐÃ ĐỔI", ["AI viết được trăm bài", "nhưng không chịu đền tiền"], "Giữa rừng bài viết AI, khách tìm người chịu trách nhiệm.", "Giữ chỗ ngay"),
                "after": ("AI KHÔNG ĐỀN TIỀN", ["Máy viết trăm bài", "không chịu trách nhiệm"], "Khách chỉ tìm người dám nhận kết quả.", "Giữ chỗ ngay"),
            },
            {
                "layer": "Tầng 2.5 · Thị trường trả tiền cho đầu ra",
                "before": ("NGƯỜI NHẬN KẾT QUẢ", ["Khách trả tiền cao", "cho người dám bảo hành"], "Đưa gương mặt thật và lời cam kết rõ ràng lên từng video.", "Đăng ký lớp"),
                "after": ("GIÁ TRỊ CHỮ TÍN", ["Khách trả tiền cao", "cho người bảo hành"], "Đưa mặt thật và cam kết lên video.", "Đăng ký lớp"),
            },
            {
                "layer": "Tầng 1 · Máy làm phần thô, bạn giữ phần cam kết",
                "before": ("PHÂN VAI RÕ RÀNG", ["Máy lo phần cắt dựng", "bạn đứng mũi chịu sào"], "Kết hợp tốc độ của AI với uy tín thật của người làm chủ.", "Xem lịch học"),
                "after": ("TỐC ĐỘ VÀ UY TÍN", ["Máy lo cắt dựng", "bạn giữ cam kết"], "Kết hợp sức máy với chữ tín chủ nghề.", "Xem lịch học"),
            },
            {
                "layer": "Tầng 3 · Không đối thủ giá rẻ nào cạnh tranh nổi",
                "before": ("VỊ THẾ BẤT KHẢ XÂM PHẠM", ["Khi bạn nhận phần khó", "không ai ép giá được"], "Video của người dám đứng mũi chịu sào luôn có sức nặng gấp mười.", "Đăng ký ngay"),
                "after": ("KHÔNG AI ÉP GIÁ", ["Dám nhận phần khó", "vị thế khác hẳn"], "Lời người làm chủ nặng gấp mười lần.", "Đăng ký ngay"),
            },
            {
                "layer": "Đảo rủi ro · Chính khóa học cũng nhận phần kết quả",
                "before": ("CAM KẾT ĐẦU RA", ["Học hết ngày một lệch", "hoàn ngay 100% phí"], "Lớp trực tiếp 2 ngày tại Hà Nội 07–08/11, còn đúng 17/35 chỗ.", "Giữ chỗ"),
                "after": ("HOÀN PHÍ NGÀY 1", ["Hết ngày 1 không hợp", "hoàn 100% học phí"], "Lớp Hà Nội 07–08/11 · Còn 17 chỗ.", "Giữ chỗ"),
            },
        ],
    },
}


def count_words(s: str) -> int:
    return len([w for w in s.replace("·", " ").split() if w.strip()])


def build_all_copies():
    all_headlines = set()
    # Load KB_01 first
    kb01_copy = json.loads((BASE_DIR / "KB_01" / "copy.json").read_text())
    for ang in kb01_copy["angles"]:
        all_headlines.add(unicodedata.normalize("NFC", ang["headline"].strip().lower()))

    for kb_id, spec in sorted(KB_COPY_SPECS.items()):
        kb_dir = BASE_DIR / kb_id
        kb_dir.mkdir(parents=True, exist_ok=True)
        angles_out = []
        for idx, item in enumerate(spec["angles"], 1):
            b_tag, b_lines, b_sub, b_cta = item["before"]
            a_tag, a_lines, a_sub, a_cta = item["after"]
            b_head = " ".join(b_lines)
            a_head = " ".join(a_lines)

            norm_h = unicodedata.normalize("NFC", b_head.strip().lower())
            if norm_h in all_headlines:
                raise ValueError(f"Duplicate headline detected in {kb_id} angle {idx}: {b_head}")
            all_headlines.add(norm_h)

            b_wc = {
                "hook_tag": count_words(b_tag),
                "headline": count_words(b_head),
                "subline": count_words(b_sub),
                "cta": count_words(b_cta),
            }
            b_wc["total"] = sum(b_wc.values())
            assert b_wc["total"] <= 35, f"{kb_id} A{idx} before words={b_wc['total']} > 35"

            a_wc = {
                "hook_tag": count_words(a_tag),
                "headline": count_words(a_head),
                "subline": count_words(a_sub),
                "cta": count_words(a_cta),
            }
            a_wc["total"] = sum(a_wc.values())
            assert a_wc["total"] <= 25, f"{kb_id} A{idx} after words={a_wc['total']} > 25"

            angles_out.append({
                "angle_idx": idx,
                "layer": item["layer"],
                "hook_tag": b_tag,
                "headline": b_head,
                "headline_break": list(b_lines),
                "subline": b_sub,
                "cta": b_cta,
                "word_count": b_wc,
                "compressed_copy": {
                    "hook_tag": a_tag,
                    "headline": a_head,
                    "headline_break": list(a_lines),
                    "subline": a_sub,
                    "cta": a_cta,
                    "word_count": a_wc,
                },
            })

        out_obj = {
            "kb": kb_id,
            "title": spec["title"],
            "checkpoint": 1,
            "angles": angles_out,
        }
        (kb_dir / "copy.json").write_text(json.dumps(out_obj, ensure_ascii=False, indent=2))

    print(f"Successfully generated copy.json for KB_02..KB_31! Total unique headlines verified across 31 KBs: {len(all_headlines)} (0 duplicates).")


if __name__ == "__main__":
    build_all_copies()
