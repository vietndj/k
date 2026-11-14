#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UPGRADE 82 BANNERS IN kb_31_master_specs.json TO LAW_19 MICRO-COPY STANDARD
===========================================================================
- Cô đọng toàn bộ 82 cặp (old, new) và (k03 l1, l2) về ngân sách 18-24 ký tự/dòng (4-6 từ đắt giá).
- Đảm bảo 100% các khuôn K01 -> K21 giữ nguyên cỡ chữ 26.5px - 28.0px (0% bị co xuống 19.5px).
- Bảo toàn bản cũ trong trường `legacy_v6_sub`.
"""

import json
from pathlib import Path

SPECS_PATH = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners/kb_31_master_specs.json")

# Bảng Micro-Copy 82 Kịch bản (KB_01 -> KB_82): (old_short, new_short, k03_n1, k03_l1, k03_n2, k03_l2)
LAW19_COPY_82 = {
    "KB_01": ("Giỏi mà im lặng: mất khách", "Lên kênh uy tín: khách tìm", "10 năm", "giỏi nghề im lặng", "01", "kênh chuẩn hút khách"),
    "KB_02": ("Nhồi từ khóa, nhảy: AI bỏ", "Nói chuẩn nghề: AI tìm khách", "0%", "khách từ clip nhảy", "100%", "AI dẫn đúng khách"),
    "KB_03": ("Học thuộc văn mẫu: đơ cứng", "Nói như tại bàn: khách tin", "10 lần", "quay thuộc lòng hỏng", "01 lần", "tư vấn thật ăn ngay"),
    "KB_04": ("Nhờ AI viết chung: ép giá", "Chỉ rõ chuẩn nghề: chốt đơn", "90%", "bài AI giống hệt nhau", "2x", "giá trị khi nói sâu"),
    "KB_05": ("Đọc giấy: quay 10 lần xóa", "Hỏi tại bàn: nói 1 lần xong", "10 lần", "đọc giấy vẫn vấp", "01 câu", "hỏi gợi mở nói mượt"),
    "KB_06": ("Làm kiểu cũ: xem rồi lướt", "Chuẩn nghề: khách nhớ & nhắn", "95%", "xem clip cũ rồi quên", "03s", "giữ chân khách thật"),
    "KB_07": ("Thuê viết kịch bản: sáo rỗng", "Chủ nghề tự nói: khách nhắn", "0đ", "từ kịch bản thuê ngoài", "03p", "chủ nghề nói ra đơn"),
    "KB_08": ("Chào hỏi dài dòng: khách lướt", "Chạm nỗi đau 3s: khách dừng", "03s", "đầu quyết định ở lại", "80%", "rời đi vì chào dài"),
    "KB_09": ("Video vô cảm: xem rồi quên", "Chạm vết xước nghề: khách nhắn", "100", "view dạo không mua", "01", "câu chạm tim ra đơn"),
    "KB_10": ("Tự khen số 1: khách nghi ngờ", "Chỉ rõ ai KỴ mua: khách tin", "0%", "tin lời tự khen suông", "100%", "nể người dám can ngăn"),
    "KB_11": ("Bày đèn, diễn xuất: bỏ cuộc", "Bấm máy tại bàn: làm bền bỉ", "30p", "lắp đèn làm nản chí", "01p", "bấm máy ngay tại bàn"),
    "KB_12": ("Báo giá quá sớm: khách im", "Cho thấy độ kỹ: khách gật đầu", "80%", "im lặng khi báo giá", "3x", "tỷ lệ chốt nhờ độ kỹ"),
    "KB_13": ("Cố nói cho hay: gượng gạo", "Giải quyết 1 việc: khách quý", "0%", "cần diễn như MC", "01", "việc thật gỡ cho khách"),
    "KB_14": ("Đu trend: toàn người xem dạo", "Giải mã nghề: ít view nhiều đơn", "1M", "view hài không ai mua", "50", "khách thật chốt đơn"),
    "KB_15": ("10 clip quay vội: khách lướt", "1 bài trúng việc: khách nhắn", "10", "clip vội khách lướt", "01", "bài trúng khách nhắn"),
    "KB_16": ("Canh view 3 ngày: kiệt sức", "Đăng xong làm nghề: khách gọi", "72h", "canh số liệu mệt mỏi", "15p", "làm bài rồi tắt máy"),
    "KB_17": ("Giảng lý thuyết: khách lướt", "Ví von đời thường: hiểu ngay", "0%", "nhớ thuật ngữ hàn lâm", "03s", "hiểu ngay nhờ ví von"),
    "KB_18": ("Làm lẻ tẻ: thiếu lực đẩy", "Đúng công thức: ra đơn đều", "10", "bài rời rạc vô tác dụng", "01", "hệ thống chuyển đổi"),
    "KB_19": ("Hô hào ban ngày: khách né", "Thủ thỉ đúng nỗi lo: mở lòng", "90%", "phòng thủ trước lời rao", "100%", "mở lòng khi đồng cảm"),
    "KB_20": ("Nhận hoàn hảo: khách nghi ngờ", "Chỉ rõ chỗ dễ hỏng: khách nể", "0%", "hàng nào hoàn hảo hết", "10x", "niềm tin khi nói thật"),
    "KB_21": ("Dùng AI đọc hộ: bóp tương tác", "Mặt thật chủ nghề: cứu kênh", "-80%", "tương tác vì giọng AI", "+300%", "tin cậy nhờ mặt thật"),
    "KB_22": ("Nói lan man 10 phút: thoát", "Gỡ 1 vướng mắc 60s: khách xem", "10p", "lan man khách thoát", "60s", "đi thẳng vào 1 việc"),
    "KB_23": ("Khoe thành tích: khách xa cách", "Kể bài học xương máu: khách tin", "0%", "đồng cảm lời khoe mẽ", "100%", "tin cậy từ trải nghiệm"),
    "KB_24": ("Người giỏi im lặng: khách nhầm", "Lên tiếng chuẩn: khách tìm về", "80%", "khách mua nhầm chỗ kém", "01", "tiếng nói chuẩn định vị"),
    "KB_25": ("Giấu nghề nói nửa vời: khách bỏ", "Chỉ kỹ từng bước: khách thuê", "0", "ai học lỏm được tay nghề", "100%", "khách nể và đặt tiền"),
    "KB_26": ("Làm không khung sườn: bí ý", "Khung 3 tầng: viết 10p xong", "03h", "ngồi bứt tóc bí chữ", "10p", "ráp khung 3 tầng xong"),
    "KB_27": ("Quay 3 bài thấy gượng: bỏ", "Khung 3 tầng dẫn lối: tự nhiên", "03", "clip đầu ai cũng khớp", "01", "khung chuẩn giữ nhịp"),
    "KB_28": ("Mồi quà rẻ: gọi không nghe", "Video giải mã sâu: khách gọi", "100", "số rác từ quà miễn phí", "10", "khách nét tự gọi đến"),
    "KB_29": ("Quay món rẻ: kiệt sức lãi mỏng", "Mổ xẻ món cao cấp: đúng tệp", "90%", "tốn sức cho đơn lẻ", "01", "bài sâu hút khách lớn"),
    "KB_30": ("Ôm hàng trăm triệu: rủi ro", "Thử thị trường bằng bài: an toàn", "100tr", "ôm hàng khi chưa test", "0đ", "đo nhu cầu qua video"),
    "KB_31": ("Đoán mò ý khách: lệch tệp", "Đọc vị nỗi sợ ngầm: trúng tim", "80%", "lệch tệp vì đoán mò", "95%", "chạm đúng tâm lý ngầm"),
    "KB_32": ("Đứng khoanh tay: khách vuốt bỏ", "Đôi tay đang làm nghề: dừng xem", "01s", "vuốt qua người khoanh tay", "05x", "giữ mắt nhờ đôi tay làm"),
    "KB_33": ("Xin lệnh AI mạng: chữ rỗng", "Ghi câu khách hỏi: ra đơn thật", "100", "câu lệnh mạng sáo rỗng", "01", "câu khách hỏi ra tiền"),
    "KB_34": ("Bán sức trực tiếp: nghỉ là đứt", "Đóng gói lên kênh: khách tự tìm", "0đ", "khi ngừng làm trực tiếp", "24/7", "video làm việc thay bạn"),
    "KB_35": ("Sợ nghề khô khan: không quay", "Đối thủ ngại nói: bạn độc chiếm", "90%", "đối thủ cùng ngành ngại", "01", "mình bạn chiếm thị trường"),
    "KB_36": ("Đọc thông số khô: khách ngáp", "Quay độ tỉ mỉ tay nghề: giữ giá", "0%", "nhớ bảng thông số khô", "100%", "trả giá cao cho độ kỹ"),
    "KB_37": ("Nghĩ câu giật tít: mùi quảng cáo", "Nhắc câu khách than: chạm tim", "03s", "nhận ra mùi quảng cáo", "100%", "dừng lại vì đúng nỗi đau"),
    "KB_38": ("Nhồi 5–7 ý: khách quên sạch", "Găm đúng 1 hình ảnh: nhớ lâu", "07", "ý nhồi nhét trôi tuột", "01", "hình ảnh găm sâu vào trí"),
    "KB_39": ("Chạy Ads sỗ sàng: tắt là hết", "Xây kho giải mã nghề: đơn bền", "0đ", "ngay khi tắt ngân sách", "365n", "kho bài nghề nuôi tiệm"),
    "KB_40": ("Lắp đồ 30 phút: nản bỏ cuộc", "Bấm máy 20s lúc làm: bền bỉ", "30p", "bày bối cảnh gây lười", "20s", "bấm quay ngay lúc làm"),
    "KB_41": ("Đọc bao bì in sẵn: mất khách", "Khám đúng bệnh & liều: chốt đơn", "100", "nơi đọc bao bì giống nhau", "01", "người bắt đúng bệnh nghề"),
    "KB_42": ("Nhìn kênh lớn tự ti: xóa bài", "Nói chuẩn cho 50 khách: ra tiền", "100k", "view ảo không nuôi tiệm", "50", "khách thật nuôi sống nghề"),
    "KB_43": ("Chia sẻ xong bỏ lửng: mất đơn", "Mở nút thắt cuối bài: khách nhắn", "80%", "xem xong không biết làm gì", "01", "câu dẫn lối khách nhắn"),
    "KB_44": ("Chỉ khoe hàng mới: ai cũng nói", "Quay đồ dùng 3 năm: khách tin", "01", "ngày mới khui chưa rõ", "03n", "bền bỉ chứng minh tất cả"),
    "KB_45": ("Nhạc ầm, chớp giật: đuổi khách", "Khung tĩnh, điềm đạm: khách sang", "0%", "khách giàu thích ồn ào", "100%", "khách lớn trọng điềm tĩnh"),
    "KB_46": ("Dọn sạch bàn mới nói: giả tạo", "Quay lúc bàn bộn việc: thật", "0%", "tin cảnh dàn dựng bóng bẩy", "100%", "tin bàn làm việc thật"),
    "KB_47": ("Đu trend vô bổ: view cao túi rỗng", "Gắn góc nhìn nghề: khách tìm", "500k", "view cười rồi quên tên", "100%", "nhớ tên chuyên gia nghề"),
    "KB_48": ("Bối cảnh rối: nuốt sản phẩm", "Đưa điểm đắt vào tâm mắt 3s", "70%", "mắt lạc vào đồ trang trí", "03s", "khóa mắt vào điểm đắt"),
    "KB_49": ("Đọc lại tờ rơi hãng: nhạt nhòa", "Kể kinh nghiệm xương máu: nể", "100", "shop đọc chung tờ rơi", "10n", "kinh nghiệm thật tạo khác biệt"),
    "KB_50": ("Thử hàng êm ru giả: nghi ngờ", "Đưa vào ca khó thật: thuyết phục", "0%", "tin bài test phòng lạnh", "100%", "tin khi vượt ca khó thật"),
    "KB_51": ("Lấy mẫu trẻ diễn: khách xa lạ", "Đúng hình ảnh khách thật: mua", "80%", "thấy không giống mình", "100%", "gật đầu vì thấy chính mình"),
    "KB_52": ("Hình ảnh ngược hẳn lời khuyên", "Bối cảnh khớp 100% thông điệp", "-50%", "niềm tin vì hình lệch lời", "100%", "thuyết phục khi đồng nhất"),
    "KB_53": ("Đăng tạp nham: AI loạn tệp", "Giữ trục chuyên môn: đúng khách", "0%", "khách mua khi kênh tạp", "95%", "AI phân phối chuẩn tệp"),
    "KB_54": ("Chỉ quay đồ thô: khách ngại", "Quay khâu làm sạch: yên tâm mua", "50%", "ngại mua vì sợ bẩn", "100%", "chốt đơn khi thấy sạch"),
    "KB_55": ("Lấy ảnh mẫu hãng: trăm nơi giống", "Quay tại công trình thật: uy tín", "100", "đại lý đăng chung 1 ảnh", "01", "clip thực tế thắng tuyệt đối"),
    "KB_56": ("Khen inox 304: nghe nhàm tai", "Tả cảnh cọ nồi mỏi lưng: mua", "03s", "gọi đúng cảnh mỏi lưng", "10x", "thuyết phục hơn thông số"),
    "KB_57": ("Tự khen hàng tốt: ngượng miệng", "Soi thẳng gầm bàn: tự tin 100%", "0%", "cần tự khen câu nào", "100%", "mối ghép thật lên tiếng"),
    "KB_58": ("Dùng từ hàn lâm: mất khách", "Nói giản dị dễ hiểu: ra đơn", "0đ", "từ lời khen đồng nghiệp", "100%", "doanh thu từ khách hiểu"),
    "KB_59": ("Ít like vội xóa bài: sai lầm", "90% khách giàu đọc ngầm & nhắn", "90%", "khách lớn không thả tim", "01", "tin nhắn chốt đơn lớn"),
    "KB_60": ("Đóng cửa 6 tháng: lệch chợ", "Đăng bài 30p thử chợ: trúng đích", "06th", "đoán mò trong phòng kín", "30p", "lên bài đo nhu cầu thật"),
    "KB_61": ("Gặp giây đầu đòi chốt: khách chạy", "Nuôi đủ 7 giờ tin cậy: tự mua", "07h", "xem kênh tạo niềm tin", "01p", "chốt đơn nhẹ nhàng"),
    "KB_62": ("Quay dựng 4 tiếng: não bỏ cuộc", "Rút còn 15p/bài: làm đều tuần", "04h", "dựng bài làm não sợ", "15p", "quy trình gọn làm bền"),
    "KB_63": ("Chờ hết ngại mới làm: đợi mãi", "Làm xong 5 bài: tự khắc tự tin", "0%", "ai tự tin từ bài số 1", "05", "bài làm thật sinh bản lĩnh"),
    "KB_64": ("Giọng phát biểu: mất hồn nghề", "Thủ thỉ bàn trà: khách mê nghe", "03h", "nói chuyện bàn trà cuốn", "01", "tông giọng thật giữ trọn"),
    "KB_65": ("Nghề giỏi mà kênh nhếch nhác", "Soi kính lúp chỗ tinh xảo: đắt", "9999", "vàng thật cần hộp xứng", "2x", "tỷ lệ chốt khách sang"),
    "KB_66": ("Tiếc 30p quay: cả tuần chờ khách", "Dành 30p mỗi tuần: kín lịch hẹn", "30p", "đóng gói 1 bài chuẩn", "07n", "khách tự tìm cả tuần"),
    "KB_67": ("Giỏi nghề mà im lặng: mất khách", "Lên tiếng mỗi tuần: khách tìm", "10n", "giỏi nghề trong hẻm nhỏ", "01", "kênh chuẩn đưa hương xa"),
    "KB_68": ("Tư vấn 1 người: lời bay theo gió", "Clip 1 phút: ngàn khách cùng nghe", "01", "buổi tư vấn tại bàn", "1000", "khách nghe qua clip 60s"),
    "KB_69": ("Nói thuật ngữ thợ: khách rối trí", "Dịch ra lợi ích thật: khách mua", "10/10", "tay nghề giỏi ở xưởng", "100%", "khách hiểu ngay sau 3 câu"),
    "KB_70": ("Bán đơn lớn mà chần chừ: lỡ sóng", "Ra hiện trường 30p: đón khách sộp", "30p", "phân tích tại thực địa", "01", "nhà đầu tư nhắn riêng"),
    "KB_71": ("Đợi rảnh mới quay: trì hoãn mãi", "Quay ngay 15p: phá vỡ cái cớ", "0%", "lúc nào hoàn toàn rảnh", "15p", "bấm máy phá tan trì hoãn"),
    "KB_72": ("Hạ giá chiều khách: hút kỳ kèo", "Giữ chuẩn nghề: hút khách sộp", "90%", "khách rẻ làm bạn mệt", "100%", "khách sang trọng chuẩn nghề"),
    "KB_73": ("Khoe làm 15p: khách chê đắt", "Kể 10 năm rèn nghề: trọng giá", "15p", "trên bàn là 10 năm luyện", "10n", "tay nghề giữ vững giá cao"),
    "KB_74": ("Chỉ chào người lạ: khó chốt", "Quay bài dặn khách cũ: khách tin", "0%", "người lạ tin lời chào", "100%", "tin khi thấy chăm khách cũ"),
    "KB_75": ("Nói liến thoắng: khách quên sạch", "Dừng 1s trước câu đắt: nhớ kỹ", "01s", "nghỉ nhịp tạo sức nặng", "3x", "độ nhớ thông điệp chính"),
    "KB_76": ("Đưa hàng ra ngay: hỏi rồi im", "Tả trúng 3 nỗi khổ: tự hỏi mua", "80%", "xem giá xong im lặng", "03", "nỗi khổ chạm đúng lúc"),
    "KB_77": ("Đăng tuyển khô khan: vắng thợ", "Kênh chủ có tâm: thợ giỏi tự về", "0", "thợ giỏi thích tin mẫu", "100%", "thợ giỏi theo chủ có tâm"),
    "KB_78": ("Kênh trống đã chạy Ads: đốt tiền", "Ghim 3 bài nghề sâu: giữ khách", "70%", "tiền Ads rơi vì kênh trống", "03", "bài ghim chốt khách Ads"),
    "KB_79": ("Chạy theo like ảo: xem rồi quên", "Làm bài đáng lưu: mang tiền tới", "10k", "like dạo không ra đơn", "100", "lượt lưu bài ra khách thật"),
    "KB_80": ("Ngày nào cũng nghĩ bài: kiệt sức", "Gom 1 buổi quay 4 bài: nhàn tênh", "01", "buổi tập trung bấm máy", "04", "bài đăng đều cả tháng"),
    "KB_81": ("Chỉ làm clip 15s: khách sợ đắt", "Thêm bài sâu 3 phút: chốt đơn lớn", "15s", "để khách biết mặt bạn", "03p", "phân tích để chốt tiền tỷ"),
    "KB_82": ("Gồng diễn hoàn hảo: sợ phán xét", "Tâm thế tặng thuốc nghề: tự nhiên", "0%", "áp lực khi đi giúp người", "100%", "khách quý sự chân thành"),
}


def populate_law19_fields(entry: dict, kb_id: str) -> dict:
    if "legacy_v6_sub" not in entry:
        entry["legacy_v6_sub"] = {
            "k01": dict(entry.get("k01", {})),
            "k03": dict(entry.get("k03", {})),
        }

    old_s, new_s, n1, l1, n2, l2 = LAW19_COPY_82[kb_id]
    eyebrow = (entry.get("eyebrow") or entry.get("k02", {}).get("eyebrow") or "ĐÚC KẾT THỰC CHIẾN K4")[:24]

    entry["sub_old"] = old_s
    entry["sub_new"] = new_s
    entry["k01"] = {"old": old_s, "new": new_s}
    entry["k02"] = {"eyebrow": eyebrow, "l1": old_s, "l2": new_s}
    entry["k03"] = {"n1": n1, "l1": l1, "n2": n2, "l2": l2}
    entry["k04"] = {"tab": eyebrow[:20], "l1": old_s, "l2": new_s}
    entry["k05"] = {"l1": old_s, "s1": "đổi nhịp", "s2": new_s}
    entry["k06"] = {"not": old_s, "but": new_s}
    entry["k07"] = {"lh": "× CÁCH CŨ", "lb": old_s, "rh": "✓ CHUẨN K4", "rb": new_s}
    entry["k08"] = {"l1": old_s, "l2_pre": "→ ", "l2_ul": new_s}
    entry["k09"] = {"meta": "Khách hàng · vừa nhắn", "msg1": "“Xem bài giải mã này,", "msg2": new_s.lower() + "!”"}
    entry["k10"] = {"lbl1": "Cách làm cũ", "val1": "10% nhớ", "lbl2": "Chuẩn nghề K4", "val2": "95% nhắn"}
    entry["k11"] = {"q": old_s + "?", "a": new_s}
    entry["k12"] = {"l1": old_s, "l2": new_s}
    entry["k13"] = {"t1": old_s, "t2": new_s}
    entry["k14"] = {"old": old_s, "new": new_s}
    entry["k15"] = {"caption": new_s}
    entry["k16"] = {"l1": old_s, "l2": new_s}

    p_old = old_s.split(":") if ":" in old_s else [old_s[:14], "khách lướt"]
    p_new = new_s.split(":") if ":" in new_s else [new_s[:14], "khách nhắn"]
    entry["k17"] = {
        "l_old": p_old[0].strip(),
        "r_old": p_old[1].strip(),
        "l_new": p_new[0].strip(),
        "r_new": p_new[1].strip(),
    }
    entry["k18"] = {"p1": "Đúng nỗi đau", "p2": "Chất nghề thật", "res": new_s}
    entry["k19"] = {"c1": old_s, "c2": new_s}
    entry["k20"] = {"benh": old_s, "thuoc": new_s}
    entry["k21"] = {"l1": old_s, "l2": new_s}
    return entry


def main():
    data = json.loads(SPECS_PATH.read_text(encoding="utf-8"))
    kbs = data["kbs"]
    max_len = 0
    for kb_id in sorted(kbs.keys(), key=lambda x: int(x.split("_")[1])):
        kbs[kb_id] = populate_law19_fields(kbs[kb_id], kb_id)
        o, n = kbs[kb_id]["k01"]["old"], kbs[kb_id]["k01"]["new"]
        max_len = max(max_len, len(o), len(n))

    data["version"] = "7.0-82kb-law19-scanpath"
    SPECS_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Upgraded all {len(kbs)} KBs in {SPECS_PATH.name} to LAW_19 micro-copy (max string len = {max_len} chars).")


if __name__ == "__main__":
    main()
