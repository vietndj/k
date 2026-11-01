#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Khởi tạo:
1. Bộ ảnh nền gần toàn thân sạch Vùng Trống (bg_pool) cho cả 2 bố cục:
   - RIGHT_PERSON (Nhân vật bên Phải, Chữ bên Trái x=48..508)
   - LEFT_PERSON  (Nhân vật bên Trái, Chữ bên Phải x=548..1008)
2. Sổ cái nội dung 31 Kịch bản (`kb_31_master_specs.json`) biên tập chuẩn xác
   theo 8 Kiểu Đã Duyệt (#01..#08) trong Bộ Chọn Chữ Banner.
3. Khởi tạo sẵn `banner2_cards/KB_01.json` và `banner2_cards/KB_15.json`.
"""

import json
from pathlib import Path
import cv2
import numpy as np
from PIL import Image

BASE_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
PILOT_DIR = BASE_DIR / "v2_pilots"
BG_POOL_DIR = PILOT_DIR / "bg_pool"
CARDS_DIR = BASE_DIR / "banner2_cards"
BG_POOL_DIR.mkdir(parents=True, exist_ok=True)
CARDS_DIR.mkdir(parents=True, exist_ok=True)


def create_clean_hero_bg(src_path: Path, dst_path: Path, person_side: str, tone_rgb=(10, 15, 26)):
    """Chuẩn hóa ảnh nền 1080x1350 với vùng trống phẳng mịn Canny = 0.0% ở phía đối diện nhân vật."""
    if dst_path.exists():
        return
    with Image.open(src_path) as im:
        rgb = im.convert("RGB")
        w0, h0 = rgb.size
        target_ratio = 1080.0 / 1350.0
        cur_ratio = w0 / float(h0)
        if cur_ratio > target_ratio:
            new_w = int(round(h0 * target_ratio))
            left = (w0 - new_w) if person_side == "right" else 0
            cropped = rgb.crop((left, 0, left + new_w, h0))
        else:
            new_h = int(round(w0 / target_ratio))
            top = max(0, min(int((h0 - new_h) * 0.12), h0 - new_h))
            cropped = rgb.crop((0, top, w0, top + new_h))
        im_1080 = cropped.resize((1080, 1350), Image.Resampling.LANCZOS)

    arr = np.array(im_1080, dtype=np.uint8)
    yy, xx = np.mgrid[0:1350, 0:1080]
    if person_side == "right":
        alpha_x = np.clip((610.0 - xx) / 180.0, 0.0, 1.0)
        matte_mask = (alpha_x * 0.88 + 0.10 * (1.0 - xx / 1080.0)).clip(0.0, 0.92)
    else:
        alpha_x = np.clip((xx - 470.0) / 180.0, 0.0, 1.0)
        matte_mask = (alpha_x * 0.88 + 0.10 * (xx / 1080.0)).clip(0.0, 0.92)

    blurred = cv2.GaussianBlur(arr, (45, 45), 0)
    base_tone = np.array(tone_rgb, dtype=np.float32)
    w_mask = matte_mask[:, :, None]
    blended = arr.astype(np.float32) * (1.0 - w_mask) + (blurred.astype(np.float32) * 0.12 + base_tone * 0.88) * w_mask
    out_u8 = np.clip(blended, 0, 255).astype(np.uint8)
    Image.fromarray(out_u8).save(dst_path, "PNG")


def prepare_bg_pool():
    # 1. BG Right Navy (Blazer Navy chuẩn KB_15)
    bg1 = BG_POOL_DIR / "bg_right_navy_01.png"
    if (PILOT_DIR / "kb_15_v22_bg.png").exists():
        bg1.write_bytes((PILOT_DIR / "kb_15_v22_bg.png").read_bytes())

    # 2. BG Left Linen (Sơ mi Linen Be chuẩn KB_01)
    bg2 = BG_POOL_DIR / "bg_left_linen_02.png"
    if (PILOT_DIR / "kb_01_v22_bg.png").exists():
        bg2.write_bytes((PILOT_DIR / "kb_01_v22_bg.png").read_bytes())

    # 3. BG Right Warm Slate (Biến thể tông trầm ấm từ Blazer Navy)
    bg3 = BG_POOL_DIR / "bg_right_slate_03.png"
    create_clean_hero_bg(PILOT_DIR / "kb_15_v22_bg.png", bg3, "right", tone_rgb=(14, 17, 24))

    # 4. BG Left Deep Charcoal (Biến thể tông than sâu từ Sơ mi Linen)
    bg4 = BG_POOL_DIR / "bg_left_charcoal_04.png"
    create_clean_hero_bg(PILOT_DIR / "kb_01_v22_bg.png", bg4, "left", tone_rgb=(11, 15, 24))

    return {
        "BG_R_NAVY": str(bg1),
        "BG_L_LINEN": str(bg2),
        "BG_R_SLATE": str(bg3),
        "BG_L_CHARCOAL": str(bg4),
    }


STYLE_NAMES = {
    "K01": "Kiểu #01 · Hai Vế Đối Lập (× / ✓)",
    "K02": "Kiểu #02 · Khối Trích Dẫn Tối Sâu (Dark Callout)",
    "K03": "Kiểu #03 · Cặp Con Số Bằng Chứng (→)",
    "K04": "Kiểu #04 · Nhãn Tab Vàng (ĐIỂM MẤU CHỐT)",
    "K05": "Kiểu #05 · Chuỗi Mũi Tên (→) & Khối Đệm Lệch",
    "K06": "Kiểu #06 · Đảo Ngược ([KHÔNG PHẢI] / [MÀ LÀ])",
    "K07": "Kiểu #07 · Thẻ Chia 2 Ngăn Trái–Phải (50/50)",
    "K08": "Kiểu #08 · Gạch Chân Quang Học & Đáy Liền Khối",
}

STYLE_FONTS = {
    "K01": ("FDFinancierDisplay-Bold.woff2", "FDFinancierDisplay-Bold", 82, 1.06),
    "K02": ("FDNoeDisplay-Bold.ttf", "FDNoeDisplay-Bold", 76, 1.08),
    "K03": ("FDHeldaneDisplay-Bold.woff2", "FDHeldaneDisplay-Bold", 82, 1.07),
    "K04": ("FDTiemposHeadline-Bold.woff2", "FDTiemposHeadline-Bold", 71, 1.09),
    "K05": ("GT-Sectra-LCGV-Display-Bold.otf", "GT-Sectra-Display-Bold", 75, 1.09),
    "K06": ("FDNewzald-Bold.woff2", "FDNewzald-Bold", 80, 1.07),
    "K07": ("FDMartinaPlantijn-Bold.woff2", "FDMartinaPlantijn-Bold", 78, 1.08),
    "K08": ("FDDomaineDisplay-Bold.woff2", "FDDomaineDisplay-Bold", 74, 1.08),
}

# Danh sách 29 Kịch bản còn lại (KB_02..KB_14, KB_16..KB_31) gán luân phiên 8 Kiểu Đã Duyệt (K01..K08)
SPECS_29 = {
    "KB_02": {
        "title": "Mạng Xã Hội Cũ Đã Chết — Kỷ Nguyên Ngữ Nghĩa",
        "style": "K01",
        "bg": "BG_R_NAVY",
        "side": "right",
        "headline_lines": ["Mạng xã hội cũ", "đã <span class=\"hl\">khép lại</span>", "thật rồi."],
        "hl_kw": "khép lại",
        "k01": {"old": "Nhồi từ khóa, nhảy nhót: AI bỏ qua", "new": "Nói đúng chuyện nghề: AI tìm khách"},
        "k02": {"eyebrow": "THUẬT TOÁN NGỮ NGHĨA MỚI", "l1": "AI giờ nghe từng câu bạn nói", "l2": "để dẫn đúng khách đang cần."},
    },
    "KB_03": {
        "title": "Chân Thật Là Một Loại Hiệu Suất",
        "style": "K02",
        "bg": "BG_L_LINEN",
        "side": "left",
        "headline_lines": ["Càng cố nói", "văn hoa bóng bẩy", "nghe <span class=\"hl\">càng giả.</span>"],
        "hl_kw": "càng giả.",
        "k02": {"eyebrow": "TÂM THẾ NGƯỜI LÀM NGHỀ", "l1": "Khách lướt qua mọi lời tô vẽ,", "l2": "họ dừng lại vì giọng nói thật."},
        "k01": {"old": "Học thuộc kịch bản văn mẫu: đơ cứng", "new": "Nói như tư vấn tại bàn: khách tin"},
    },
    "KB_04": {
        "title": "Giống Nhau Thì Khách So Giá",
        "style": "K03",
        "bg": "BG_R_SLATE",
        "side": "right",
        "headline_lines": ["Video giống nhau", "thì khách hàng", "chỉ <span class=\"hl\">so giá.</span>"],
        "hl_kw": "so giá.",
        "k03": {"n1": "100", "l1": "clip văn mẫu AI", "n2": "01", "l2": "chi tiết nghề giữ giá"},
        "k01": {"old": "Nhờ AI viết bài chung chung: bị ép giá", "new": "Chỉ rõ tiêu chuẩn nghề: khách chốt"},
    },
    "KB_05": {
        "title": "Ngoài Đời Nói Cuốn, Lên Máy Là Đơ",
        "style": "K04",
        "bg": "BG_L_CHARCOAL",
        "side": "left",
        "headline_lines": ["Tư vấn hai tiếng,", "bật máy quay lên", "lại <span class=\"hl\">đơ cứng.</span>"],
        "hl_kw": "đơ cứng.",
        "k04": {"tab": "ĐIỂM MẤU CHỐT", "l1": "Đừng cố nhìn ống kính đọc thuộc lòng,", "l2": "hãy trả lời như đang ngồi trước khách."},
        "k01": {"old": "Đọc giấy trước ống kính: quay 10 lần xóa", "new": "Đặt câu hỏi tại bàn: nói 1 lần ăn ngay"},
    },
    "KB_06": {
        "title": "Câu Trả Lời Bạn Nói Mỗi Ngày",
        "style": "K05",
        "bg": "BG_R_NAVY",
        "side": "right",
        "headline_lines": ["Một câu hỏi lặp", "đừng giải thích", "đến <span class=\"hl\">chục lần.</span>"],
        "hl_kw": "chục lần.",
        "k05": {"l1": "Ghi hình 1 lần câu trả lời kỹ nhất", "s1": "gửi khách xem", "s2": "tự chốt đơn."},
        "k02": {"eyebrow": "ĐÓNG GÓI TRI THỨC NGHỀ", "l1": "Quay đúng câu khách hỏi mỗi ngày", "l2": "để video tư vấn thay bạn 24/7."},
    },
    "KB_07": {
        "title": "Thuê Đội Ngoài 30 Triệu Hay Tự Cầm Kênh",
        "style": "K06",
        "bg": "BG_L_LINEN",
        "side": "left",
        "headline_lines": ["Chi ba mươi triệu", "thuê đội quay ngoài", "vẫn <span class=\"hl\">không khách.</span>"],
        "hl_kw": "không khách.",
        "k06": {"not": "thiếu máy quay tiền trăm triệu", "but": "thiếu người hiểu nghề trong clip"},
        "k01": {"old": "Thuê ngoài viết kịch bản: hào nhoáng, rỗng", "new": "Chủ nghề tự nói 3 phút: khách nhắn"},
    },
    "KB_08": {
        "title": "Câu Chào Lịch Sự Đang Đốt Tiền Quảng Cáo",
        "style": "K07",
        "bg": "BG_R_SLATE",
        "side": "right",
        "headline_lines": ["Câu chào lịch sự", "đang làm khách", "<span class=\"hl\">vuốt qua</span> ngay."],
        "hl_kw": "vuốt qua",
        "k07": {"lh": "3 GIÂY ĐẦU CHÀO HỎI", "lb": "Mất 80% người xem,<br/>đốt tiền quảng cáo.", "rh": "VÀO THẲNG VẤN ĐỀ", "rb": "Giữ đúng người mua,<br/>tăng gấp đôi tin nhắn."},
        "k01": {"old": "Xin chào mọi người mình là...: khách lướt", "new": "Bấm trúng nỗi đau giây số 1: khách dừng"},
    },
    "KB_09": {
        "title": "Khách Mua Lớn Xem Âm Thầm",
        "style": "K08",
        "bg": "BG_L_CHARCOAL",
        "side": "left",
        "headline_lines": ["Người mua đơn lớn", "không bấm thích", "chỗ <span class=\"hl\">ồn ào.</span>"],
        "hl_kw": "ồn ào.",
        "k08": {"l1": "Họ âm thầm xem liền 5 bài chuyên môn,", "l2_pre": "rồi thẳng tay ", "l2_ul": "nhắn tin chốt lịch."},
        "k02": {"eyebrow": "HÀNH VI KHÁCH HÀNG GIÁ TRỊ CAO", "l1": "Khách sộp không bình luận dạo,", "l2": "họ xem kỹ tay nghề rồi nhắn riêng."},
    },
    "KB_10": {
        "title": "Tự Khen Không Ai Tin — Dám Nói Không",
        "style": "K01",
        "bg": "BG_R_NAVY",
        "side": "right",
        "headline_lines": ["Tự khen hàng tốt", "trên mạng giờ", "<span class=\"hl\">chẳng ai tin.</span>"],
        "hl_kw": "chẳng ai tin.",
        "k01": {"old": "Cam kết uy tín số 1: khách nghi ngờ", "new": "Chỉ rõ ai KHÔNG nên mua: khách tin"},
        "k02": {"eyebrow": "BẰNG CHỨNG TỪ SỰ THẲNG THẮN", "l1": "Dám từ chối khách không phù hợp", "l2": "mới là lời khẳng định đắt giá nhất."},
    },
    "KB_11": {
        "title": "Đồ Nghề Phủ Bụi — Không Phải Bạn Lười",
        "style": "K02",
        "bg": "BG_L_LINEN",
        "side": "left",
        "headline_lines": ["Đèn mic mua đủ", "nhưng vẫn nằm", "<span class=\"hl\">phủ bụi</span> góc nhà."],
        "hl_kw": "phủ bụi",
        "k02": {"eyebrow": "GỠ NÚT THẮT TÂM LÝ QUAY VIDEO", "l1": "Không phải bạn lười làm kênh,", "l2": "chỉ vì quy trình cũ quá rườm rà."},
        "k01": {"old": "Bày đèn, học thuộc, diễn xuất: bỏ cuộc", "new": "Bấm máy ngay tại bàn làm việc: bền bỉ"},
    },
    "KB_12": {
        "title": "Hỏi Giá Xong Chỉ Hiện Đã Xem",
        "style": "K03",
        "bg": "BG_R_SLATE",
        "side": "right",
        "headline_lines": ["Báo giá xong", "bên kia chỉ hiện", "chữ <span class=\"hl\">Đã xem.</span>"],
        "hl_kw": "Đã xem.",
        "k03": {"n1": "0đ", "l1": "niềm tin trước đó", "n2": "100%", "l2": "im lặng khi nghe giá"},
        "k01": {"old": "Khách chưa hiểu nghề đã báo giá: im lặng", "new": "Cho thấy độ kỹ trước khi báo giá: gật đầu"},
    },
    "KB_13": {
        "title": "Ngại Người Quen Lướt Thấy",
        "style": "K04",
        "bg": "BG_L_CHARCOAL",
        "side": "left",
        "headline_lines": ["Không sợ người lạ,", "chỉ ngại <span class=\"hl\">người quen</span>", "lướt thấy mình."],
        "hl_kw": "người quen",
        "k04": {"tab": "ĐIỂM MẤU CHỐT", "l1": "Người quen không trả hóa đơn cho bạn,", "l2": "nói chuyện nghề đàng hoàng ai cũng nể."},
        "k02": {"eyebrow": "VƯỢT QUA RÀO CẢN THỂ DIỆN", "l1": "Khi bạn chia sẻ kiến thức nghề thật,", "l2": "người quen cũng biến thành người giới thiệu."},
    },
    "KB_14": {
        "title": "Kênh Đông Như Hội Mà Chẳng Ai Mua",
        "style": "K05",
        "bg": "BG_R_NAVY",
        "side": "right",
        "headline_lines": ["Kênh đông như hội", "mà chẳng có ai", "<span class=\"hl\">móc ví</span> mua."],
        "hl_kw": "móc ví",
        "k05": {"l1": "Bỏ ngay kịch bản hài nhảm câu view", "s1": "lọc người mua", "s2": "ra đơn thật."},
        "k01": {"old": "Đu trend triệu view: toàn người xem dạo", "new": "Giải mã đúng bệnh nghề: ít view, nhiều đơn"},
    },
    "KB_16": {
        "title": "Ngó Lượt Thích Nhiều Hơn Ngó Nồi Cơm",
        "style": "K06",
        "bg": "BG_L_LINEN",
        "side": "left",
        "headline_lines": ["Ngó lượt thích", "còn nhiều hơn cả", "ngó <span class=\"hl\">nồi cơm.</span>"],
        "hl_kw": "nồi cơm.",
        "k06": {"not": "cần vài chục nghìn tim ảo", "but": "cần 5 khách nhắn hỏi mua thật"},
        "k01": {"old": "Quay 15 phút, ngồi canh view 3 ngày: kiệt sức", "new": "Đăng xong tắt máy làm nghề: khách tự gọi"},
    },
    "KB_17": {
        "title": "Nói Đúng Sách Thì Gật, Nói Đúng Hình Thì Dừng",
        "style": "K07",
        "bg": "BG_R_SLATE",
        "side": "right",
        "headline_lines": ["Nói chữ chuyên ngành", "khách nghe xong", "<span class=\"hl\">quên sạch</span> ngay."],
        "hl_kw": "quên sạch",
        "k07": {"lh": "THUẬT NGỮ SÁCH VỞ", "lb": "Khách nghe mệt não,<br/>vuốt đi sau 2 giây.", "rh": "VÍ DỤ ĐỜI THƯỜNG", "rb": "Nhìn thấy hình ngay,<br/>nhớ tên bạn cả năm."},
        "k01": {"old": "Giảng lý thuyết hàn lâm: khách lướt qua", "new": "Ví von bằng vật lý đời thường: khách hiểu"},
    },
    "KB_18": {
        "title": "Rời Ghế Xoay Ra Hiện Trường Thật",
        "style": "K08",
        "bg": "BG_L_CHARCOAL",
        "side": "left",
        "headline_lines": ["Ngồi phòng kín", "nói chay một mình", "khách <span class=\"hl\">chóng chán.</span>"],
        "hl_kw": "chóng chán.",
        "k08": {"l1": "Đưa máy ra đúng bàn làm việc thật,", "l2_pre": "uy tín tăng ", "l2_ul": "gấp mười lần lời nói."},
        "k02": {"eyebrow": "SỨC NẶNG CỦA BỐI CẢNH THẬT", "l1": "Khách không tin lời nói trong phòng trống,", "l2": "họ tin đôi tay đang làm việc thật."},
    },
    "KB_19": {
        "title": "11 Giờ Đêm Khách Khó Tính Cũng Mềm Lòng",
        "style": "K01",
        "bg": "BG_R_NAVY",
        "side": "right",
        "headline_lines": ["Mười một giờ đêm", "khách khó tính nhất", "cũng <span class=\"hl\">lắng nghe.</span>"],
        "hl_kw": "lắng nghe.",
        "k01": {"old": "Hô hào giục mua ban ngày: khách phòng thủ", "new": "Thủ thỉ đúng nỗi lo lúc đêm: khách mở lòng"},
        "k02": {"eyebrow": "NHỊP ĐIỆU TÂM LÝ NGƯỜI XEM", "l1": "Ban ngày khách dựng rào chắn phòng thủ,", "l2": "đêm về họ cần một người hiểu chuyện."},
    },
    "KB_20": {
        "title": "Dám Kể Lần Làm Hỏng Phải Đền Tiền",
        "style": "K02",
        "bg": "BG_L_LINEN",
        "side": "left",
        "headline_lines": ["Khách giao việc lớn", "rất sợ người", "chỉ biết <span class=\"hl\">khoe hay.</span>"],
        "hl_kw": "khoe hay.",
        "k02": {"eyebrow": "BẢN LĨNH NGƯỜI LÀM NGHỀ LÂU NĂM", "l1": "Dám kể bài học một lần trả giá đắt", "l2": "khiến khách tin trọn vào tay nghề bạn."},
        "k01": {"old": "Lúc nào cũng nhận hoàn hảo: khách nghi ngờ", "new": "Chỉ rõ chỗ dễ hỏng & cách ngừa: khách nể"},
    },
    "KB_21": {
        "title": "Cái Giá Của Cô Nhân Viên AI Đọc Hộ",
        "style": "K03",
        "bg": "BG_R_SLATE",
        "side": "right",
        "headline_lines": ["Page mười nghìn người,", "bài mới đăng lên", "lẹt đẹt <span class=\"hl\">mười view.</span>"],
        "hl_kw": "mười view.",
        "k03": {"n1": "10K", "l1": "theo dõi có sẵn", "n2": "12", "l2": "lượt xem vì mặt AI"},
        "k01": {"old": "Dùng avatar AI đọc hộ: bóp nghẹt tương tác", "new": "Gương mặt thật của chủ nghề: cứu sống kênh"},
    },
    "KB_22": {
        "title": "Hai Máy Quay Podcast Mà Vài Chục View",
        "style": "K04",
        "bg": "BG_L_CHARCOAL",
        "side": "left",
        "headline_lines": ["Quay hai góc máy", "như đài truyền hình", "vẫn <span class=\"hl\">vài chục view.</span>"],
        "hl_kw": "vài chục view.",
        "k04": {"tab": "ĐIỂM MẤU CHỐT", "l1": "Khi khách chưa biết bạn là ai,", "l2": "đừng bắt họ nghe cuộc trò chuyện dài dòng."},
        "k01": {"old": "Ngồi đối đáp lan man 10 phút: khách thoát", "new": "Gỡ thẳng 1 vướng mắc trong 60s: khách xem"},
    },
    "KB_23": {
        "title": "Mười Năm Nghề Vẫn Ghi Đang Tập Tành",
        "style": "K05",
        "bg": "BG_R_NAVY",
        "side": "right",
        "headline_lines": ["Mười năm làm nghề", "đừng tự nhận mình", "đang <span class=\"hl\">tập tành.</span>"],
        "hl_kw": "tập tành.",
        "k05": {"l1": "Khiêm tốn sai chỗ làm mất vị thế", "s1": "đứng đúng tầm", "s2": "hút khách lớn."},
        "k02": {"eyebrow": "ĐỊNH VỊ VỊ THẾ CHUYÊN GIA", "l1": "Khách trả tiền cao để tìm người cầm lái,", "l2": "không ai giao việc lớn cho người tập sự."},
    },
    "KB_24": {
        "title": "Im Lặng Là Nhường Khách Cho Người Làm Ẩu",
        "style": "K06",
        "bg": "BG_L_LINEN",
        "side": "left",
        "headline_lines": ["Bạn ngại lên tiếng,", "người làm ẩu", "<span class=\"hl\">lấy hết</span> khách."],
        "hl_kw": "lấy hết",
        "k06": {"not": "khoe mẽ bản thân trên mạng", "but": "bảo vệ khách khỏi hàng kém chất"},
        "k01": {"old": "Người giỏi nghề im lặng: khách mua nhầm", "new": "Lên tiếng chuẩn mực: khách tìm về đúng chỗ"},
    },
    "KB_25": {
        "title": "Sợ Chỉ Kỹ Thì Khách Về Tự Làm",
        "style": "K07",
        "bg": "BG_R_SLATE",
        "side": "right",
        "headline_lines": ["Sợ chỉ kỹ quá", "khách xem xong rồi", "về <span class=\"hl\">tự làm?</span>"],
        "hl_kw": "tự làm?",
        "k07": {"lh": "GIẤU NGHỀ ÚP MỞ", "lb": "Video nhạt nhòa,<br/>khách chẳng nhớ tên.", "rh": "BÓC TÁCH TẬN GỐC", "rb": "Khách thấy độ khó,<br/>giao trọn việc cho bạn."},
        "k01": {"old": "Nói nửa vời vì sợ lộ nghề: khách bỏ đi", "new": "Chỉ kỹ từng bước: khách nể và thuê bạn"},
    },
    "KB_26": {
        "title": "Sợ Nói Lại Ý Cũ, Cả Tuần Bỏ Trống",
        "style": "K08",
        "bg": "BG_L_CHARCOAL",
        "side": "left",
        "headline_lines": ["Sợ nói chuyện cũ", "nên để cả tuần", "<span class=\"hl\">bỏ trống</span> kênh."],
        "hl_kw": "bỏ trống",
        "k08": {"l1": "Với bạn là chuyện nói trăm lần,", "l2_pre": "với khách mới là ", "l2_ul": "phao cứu sinh."},
        "k02": {"eyebrow": "NGUYÊN LÝ LẶP LẠI TRONG ĐỊNH VỊ", "l1": "Một triết lý nghề kể qua 10 tình huống", "l2": "sẽ khắc sâu tên bạn vào trí nhớ khách."},
    },
    "KB_27": {
        "title": "Không Phải Không Có Khiếu — Chưa Đủ 30 Lần",
        "style": "K01",
        "bg": "BG_R_NAVY",
        "side": "right",
        "headline_lines": ["Quay ba bài ngượng", "đừng vội nghĩ mình", "<span class=\"hl\">không có khiếu.</span>"],
        "hl_kw": "không có khiếu.",
        "k01": {"old": "Quay 3 clip đầu thấy gượng: tự bỏ cuộc", "new": "Có khung sườn 3 tầng dẫn lối: nói tự nhiên"},
        "k02": {"eyebrow": "KỸ NĂNG ĐƯỢC RÈN QUA QUY TRÌNH", "l1": "Ca làm nghề đầu tiên ai cũng từng khớp,", "l2": "đúng phương pháp thì bài thứ 5 đã mượt."},
    },
    "KB_28": {
        "title": "Cả Trăm Số Điện Thoại Gọi Không Nghe Máy",
        "style": "K02",
        "bg": "BG_L_LINEN",
        "side": "left",
        "headline_lines": ["Cả trăm số để lại,", "gọi vào máy toàn", "báo <span class=\"hl\">thuê bao.</span>"],
        "hl_kw": "thuê bao.",
        "k02": {"eyebrow": "CHẤT LƯỢNG LEAD TỪ NỘI DUNG SÂU", "l1": "Khách để số khi chưa hiểu giá trị", "l2": "sẽ từ chối nghe máy khi sale gọi."},
        "k01": {"old": "Mồi quà rẻ lấy trăm số: gọi không bắt máy", "new": "Video giải mã sâu: khách chủ động gọi bạn"},
    },
    "KB_29": {
        "title": "Khách Toàn Hỏi Món Rẻ, Món Lãi Cao Ế Ẩm",
        "style": "K03",
        "bg": "BG_R_SLATE",
        "side": "right",
        "headline_lines": ["Khách toàn hỏi món rẻ,", "món chủ lực lại", "nằm <span class=\"hl\">ế ẩm.</span>"],
        "hl_kw": "ế ẩm.",
        "k03": {"n1": "0", "l1": "bài về món chủ lực", "n2": "90%", "l2": "khách chỉ hỏi đồ rẻ"},
        "k01": {"old": "Chỉ quay món rẻ dễ bán: kiệt sức, lãi mỏng", "new": "Giải phẫu giá trị món cao cấp: đúng tệp"},
    },
    "KB_30": {
        "title": "Định Bỏ Vài Trăm Triệu Nhập Máy Mới",
        "style": "K04",
        "bg": "BG_L_CHARCOAL",
        "side": "left",
        "headline_lines": ["Định bỏ trăm triệu", "nhập máy mới về", "mà <span class=\"hl\">chưa có khách?</span>"],
        "hl_kw": "chưa có khách?",
        "k04": {"tab": "ĐIỂM MẤU CHỐT", "l1": "Làm 3 video đo lực cầu thị trường trước,", "l2": "có khách đặt lịch rồi mới xuống tiền nhập."},
        "k01": {"old": "Ôm máy trăm triệu rồi mới tìm khách: rủi ro", "new": "Dùng nội dung thử thị trường trước: an toàn"},
    },
    "KB_31": {
        "title": "Giữa Rừng AI, Khách Tìm Người Chịu Trách Nhiệm",
        "style": "K05",
        "bg": "BG_R_NAVY",
        "side": "right",
        "headline_lines": ["AI viết trăm bài", "nhưng không đứng ra", "<span class=\"hl\">chịu trách nhiệm.</span>"],
        "hl_kw": "chịu trách nhiệm.",
        "k05": {"l1": "Đưa mặt thật và cam kết nghề lên kênh", "s1": "vượt rừng AI", "s2": "khách chọn bạn."},
        "k02": {"eyebrow": "LỢI THẾ TUYỆT ĐỐI CỦA NGƯỜI THẬT", "l1": "AI tạo ra chữ miễn phí trong 3 giây,", "l2": "nhưng uy tín con người là thứ bất khả sao chép."},
    },
}


def main():
    bg_pool = prepare_bg_pool()
    master_out = {
        "version": "3.0",
        "bg_pool": bg_pool,
        "style_names": STYLE_NAMES,
        "style_fonts": STYLE_FONTS,
        "kbs": SPECS_29,
    }
    out_path = BASE_DIR / "kb_31_master_specs.json"
    out_path.write_text(json.dumps(master_out, ensure_ascii=False, indent=2), encoding="utf-8")

    # Khởi tạo sẵn 2 card đã duyệt KB_01 và KB_15 trong banner2_cards/
    kb01_card = {
        "kb_id": "KB_01",
        "order": 1,
        "title": "Giỏi Mà Tàng Hình — Tắt Chế Độ Tàng Hình",
        "status": "APPROVED",
        "style_code": "K04",
        "style_name": "Kiểu Kết Khối Serif × Sans (Đã Duyệt #01)",
        "font_name": "FDTiemposHeadline-Bold 83px",
        "side": "left",
        "headline_plain": "Trăm clip viral vẫn tàng hình với khách mua",
        "subline_summary": "Khách chỉ xuống tiền khi thấy góc nhìn riêng và năng lực thật của bạn.",
        "old_img_url": "https://media.fedu.vn/banner2/kb_01_step1_old_error.png",
        "final_img_url": "https://media.fedu.vn/banner2/kb_01_step3_v22_approved.jpg",
        "secondary_img_url": "https://media.fedu.vn/banner2/kb_01_v22_tri_evolution.jpg",
        "secondary_label": "3 Bước Tiến Hóa KB_01",
        "audit_score": "13/13 PASS",
        "updated_at": "2026-11-01T09:25:00+07:00",
    }
    (CARDS_DIR / "KB_01.json").write_text(json.dumps(kb01_card, ensure_ascii=False, indent=2), encoding="utf-8")

    kb15_card = {
        "kb_id": "KB_15",
        "order": 15,
        "title": "Mỗi Tuần Một Bài, Bài Nào Cũng Có Người Nhớ",
        "status": "APPROVED",
        "style_code": "K01 + K02",
        "style_name": "Kiểu #01 (Hai Vế ×/✓) & Kiểu #02 (Trích Dẫn Tối Sâu)",
        "font_name": "FDFinancierDisplay-Bold 83px & FDNoeDisplay-Bold 77px",
        "side": "right",
        "headline_plain": "Đừng ép mình đăng bài vội vã mỗi ngày.",
        "subline_summary": "× 10 clip quay vội: khách lướt | ✓ 1 bài trúng việc: khách nhắn",
        "old_img_url": "https://media.fedu.vn/banner2/kb_15_v1_old_error.jpg",
        "final_img_url": "https://media.fedu.vn/banner2/kb_15_pa2_financier_split.jpg",
        "secondary_img_url": "https://media.fedu.vn/banner2/kb_15_pa3_noe_callout.jpg",
        "secondary_label": "Phương Án 3 Đã Duyệt (Noe Display)",
        "audit_score": "13/13 PASS",
        "updated_at": "2026-11-01T10:15:00+07:00",
    }
    (CARDS_DIR / "KB_15.json").write_text(json.dumps(kb15_card, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Prepared {len(bg_pool)} clean backgrounds and {len(SPECS_29)} KB specs -> {out_path}")


if __name__ == "__main__":
    main()
