#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render & Audit:
1. 10 Họ Font Chữ To Có Chân Mới (H31 -> H40) — hoàn tất trọn bộ 40 Chữ To Có Chân (H01..H40)
2. 11 Khuôn Khung Chữ Nhỏ Mới (K11 làm lại chuẩn 16/16 + K41 -> K50) — hoàn tất tròn 50 Khuôn Khung Chữ Nhỏ (K01..K50)
Mọi bản render đều được kiểm toán qua uiux_auditor.py (all_13_pass = True, hBottom <= 717, sTop >= 734, minSubFs >= 19.5px, rPad >= 14px, sibGap >= 8px).
"""
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List

from PIL import Image
from playwright.sync_api import sync_playwright

sys.path.insert(0, "/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
from uiux_auditor import audit_v3_banner

FONT_DIR = Path("/Users/vietmac/Documents/CODE/fedu-font/fonts")
PILOT_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners/v2_pilots")
BG_PATH = PILOT_DIR / "kb_15_v22_bg.png"
BRAIN_DIR = Path("/Users/vietmac/.gemini/antigravity/brain/d0674648-f186-46ae-a77c-066e17e36fb5")
REPORT_JSON = Path("/tmp/report_h40_k50.json")

# ==================== 10 NEW HEADLINE SERIF TYPEFACES (H31 -> H40) ====================
NEW_HEADLINE_SPECS: List[Dict[str, Any]] = [
    {
        "hid": "H31",
        "hgroup": "H1B",
        "hgroup_label": "Nhóm 1B • Sắc Bén (xH 0.47–0.49)",
        "sid": "kb_15_new_k11_thanh_truot_doi_cuc",
        "name": "Adobe Caslon Bold (Garalde Classic)",
        "font_file": "FDAdobeCaslon-Bold.ttf",
        "focal_file": "FDAdobeCaslon-BoldItalic.ttf",
        "focal_style": "italic",
        "foundry": "Adobe Originals",
        "desc": "Kinh điển Garalde chuẩn mực của Carol Twombly: chân chữ cổ điển đầm ấm, độ tương phản nét vừa phải giúp đọc lướt êm mắt.",
    },
    {
        "hid": "H32",
        "hgroup": "H1B",
        "hgroup_label": "Nhóm 1B • Sắc Bén (xH 0.47–0.49)",
        "sid": "kb_15_new_k41_chu_ky_tich_luy",
        "name": "Adobe Jenson Bold (Venetian Oldstyle)",
        "font_file": "FDAdobeJenson-Bold.ttf",
        "focal_file": "FDAdobeJenson-BoldItalic.ttf",
        "focal_style": "italic",
        "foundry": "Robert Slimbach",
        "desc": "Phong cách Venetian Phục Hưng của Robert Slimbach: trục chữ nhân văn vững chãi, chân chữ vát nhẹ mang đậm khí chất học thuật.",
    },
    {
        "hid": "H33",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k42_ma_tran_4o",
        "name": "GT Ultra Median Bold (Contemporary Flare)",
        "font_file": "GRUltraMedian-Bold.woff2",
        "focal_file": "GRUltraMedian-BoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Grilli Type",
        "desc": "Nhánh Median cân bằng nhất của họ GT Ultra (Grilli Type): kết hợp độ đầm của Serif cổ điển với đầu nét vát đương đại, đọc siêu thoáng.",
    },
    {
        "hid": "H34",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k43_thang_do_3cap",
        "name": "GT Pantheon Text Bold (Monumental)",
        "font_file": "GRPantheonText-Bold.woff2",
        "focal_file": "GRPantheonText-BoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Grilli Type",
        "desc": "Kiến trúc chữ khắc bia đá La Mã đương đại của Grilli Type: lòng chữ mở rộng, nét vát dứt khoát tạo uy quyền ngay lập tức.",
    },
    {
        "hid": "H35",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k44_phuong_trinh_niem_tin",
        "name": "GT Flaire Extra Bold (High-Flare)",
        "font_file": "GRFlaireExtraBold.woff2",
        "focal_file": "GRFlaireExtraBoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Grilli Type",
        "desc": "Phiên bản độ mở chân chữ cực đại (Extra Flare) của họ GT Flaire: đầu nét vát loe sắc lẹm như lưỡi giáo trên nền tối sâu.",
    },
    {
        "hid": "H36",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k45_cau_hoi_phan_bien",
        "name": "GT Canon M Standard Bold",
        "font_file": "GRCanonMStandardBold.woff2",
        "focal_file": "GRCanonMStandardBoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Grilli Type",
        "desc": "Bản Optical Size M (Medium Display) cân bằng hoàn hảo giữa độ đầm của bản Text và sự sắc sảo của bản L trên khung 4:5.",
    },
    {
        "hid": "H37",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k46_chan_doan_truc_tiep",
        "name": "Domaine Text Bold (High-xH Baroque)",
        "font_file": "FDDomaineText-Bold.woff2",
        "focal_file": "FDDomaineText-BoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Klim Type Foundry",
        "desc": "Nhánh Text của họ Domaine lừng danh với lòng chữ cao vọt và nét phụ dày hơn bản Display, giúp chữ rõ nét tuyệt đối trên điện thoại.",
    },
    {
        "hid": "H38",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k47_bien_ban_tu_van",
        "name": "Epicene Text Bold (Sculpted Frame)",
        "font_file": "FDEpiceneText-Bold.woff2",
        "focal_file": "FDEpiceneText-BoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Klim Type Foundry",
        "desc": "Phiên bản Text của Epicene với khung xương điêu khắc Baroque sang trọng nhưng nét chữ đầm khỏe, cực kỳ bắt sáng.",
    },
    {
        "hid": "H39",
        "hgroup": "H1B",
        "hgroup_label": "Nhóm 1B • Sắc Bén (xH 0.47–0.49)",
        "sid": "kb_15_new_k48_tin_nhan_nua_dem",
        "name": "Heldane Text Bold (Renaissance Text)",
        "font_file": "FDHeldaneText-Bold.woff2",
        "focal_file": "FDHeldaneText-BoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Klim Type Foundry",
        "desc": "Tinh hoa chữ in Phục Hưng Pháp kết hợp kỹ thuật cắt nét hiện đại của Klim Type, mang lại vẻ đẹp điềm tĩnh, trí thức.",
    },
    {
        "hid": "H40",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k49_giai_dap_nghi_ngo",
        "name": "GT Sectra Fine Bold (Scalpel Edge)",
        "font_file": "GRSectraFine-Bold.woff2",
        "focal_file": "GRSectraFine-BoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Grilli Type",
        "desc": "Nhánh Fine cao cấp của GT Sectra: kết hợp góc cắt dao mổ sắc bén với tỷ lệ nét thanh – nét đậm biên tập tạp chí quốc tế.",
    },
]

# ==================== 11 NEW SUBLINE BOX ARCHETYPES (K11 + K41 -> K50) ====================
NEW_SUBBOX_SPECS: List[Dict[str, Any]] = [
    {
        "kid": "K11",
        "kgroup": "KA",
        "kgroup_label": "Họ 1 • Đối Lập & So Sánh 2 Vế",
        "sid": "kb_15_new_k11_thanh_truot_doi_cuc",
        "name": "Thanh Trượt Đối Cực Cũ / Mới ([CỰC CŨ] ──●► [CỰC MỚI])",
        "author": "GEMINI",
        "sample_quote": "[CỰC CŨ: Đăng theo cảm hứng] ──●► [CỰC MỚI: Đăng theo bệnh án] | Dịch chuyển trục nội dung: ít bài hơn nhưng trúng huyệt.",
        "desc": "Thanh ray đối cực đặt 2 thái cực Cũ / Mới trên cùng một trục ngang có nút trượt dẫn hướng, chốt câu dịch chuyển ở đáy.",
        "h_main_file": "FDAdobeCaslon-Bold.ttf",
        "h_focal_file": "FDAdobeCaslon-BoldItalic.ttf",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k11">
          <div class="k11-rail">
            <span class="k11-pole old">CỰC CŨ: Đăng theo cảm hứng</span>
            <span class="k11-knob mono">●►</span>
            <span class="k11-pole new">CỰC MỚI: Đăng theo bệnh án</span>
          </div>
          <div class="k11-foot">Dịch chuyển trục nội dung: <b class="gold">ít bài hơn nhưng trúng huyệt.</b></div>
        </div>
        """,
    },
    {
        "kid": "K41",
        "kgroup": "KB",
        "kgroup_label": "Họ 2 • Con Số & Thời Gian / Lịch",
        "sid": "kb_15_new_k41_chu_ky_tich_luy",
        "name": "Chu Kỳ Tích Lũy Lãi Kép 3 Mốc (Tuần 01 → Tuần 04 → Tháng 03)",
        "author": "CLAUDE2",
        "sample_quote": "[TUẦN 01: 02 bài] · [TUẦN 04: 08 bài] · [THÁNG 03: Kho 24 bài chốt khách] | Mỗi bài giải mã là 01 tài sản số nuôi kênh dài hạn.",
        "desc": "Ba hộp mốc thời gian nối tiếp nhau thể hiện hiệu ứng lãi kép nội dung từ Tuần 01 đến Tháng 03, chốt định nghĩa tài sản số ở đáy.",
        "h_main_file": "FDAdobeJenson-Bold.ttf",
        "h_focal_file": "FDAdobeJenson-BoldItalic.ttf",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k41">
          <div class="k41-stages">
            <span class="k41-box">TUẦN 01: 02 bài</span>
            <span class="k41-box">TUẦN 04: 08 bài</span>
            <span class="k41-box active">THÁNG 03: Kho 24 bài chốt khách</span>
          </div>
          <div class="k41-foot">Mỗi bài giải mã là <b class="mono gold">01</b> <b class="gold">tài sản số</b> nuôi kênh dài hạn.</div>
        </div>
        """,
    },
    {
        "kid": "K42",
        "kgroup": "KC",
        "kgroup_label": "Họ 3 • Công Thức & Bảng Kiểm",
        "sid": "kb_15_new_k42_ma_tran_4o",
        "name": "Ma Trận Kiểm Định 4 Ô Vuông (2×2 Quadrant Checklist)",
        "author": "GEMINI",
        "sample_quote": "[✓ 01. Đúng triệu chứng] | [✓ 02. Đúng cơ chế gốc] / [✓ 03. Đúng bằng chứng] | [✓ 04. Đúng lời mời học]",
        "desc": "Lưới ma trận 2×2 ô vuông kiểm định 4 tiêu chuẩn bài viết K4 có dấu tích vàng, giúp rà soát chất lượng bài trong 3 giây.",
        "h_main_file": "GRUltraMedian-Bold.woff2",
        "h_focal_file": "GRUltraMedian-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k42">
          <div class="k42-grid">
            <div class="k42-cell"><b class="gold">✓</b> 01. Đúng triệu chứng</div>
            <div class="k42-cell"><b class="gold">✓</b> 02. Đúng cơ chế gốc</div>
            <div class="k42-cell"><b class="gold">✓</b> 03. Đúng bằng chứng</div>
            <div class="k42-cell active"><b class="gold">✓</b> 04. Đúng lời mời học</div>
          </div>
        </div>
        """,
    },
    {
        "kid": "K43",
        "kgroup": "KC",
        "kgroup_label": "Họ 3 • Công Thức & Bảng Kiểm",
        "sid": "kb_15_new_k43_thang_do_3cap",
        "name": "Thang Đo 3 Cấp Độ Vị Thế (Cấp 1 → Cấp 2 → Cấp 3)",
        "author": "CLAUDE2",
        "sample_quote": "[CẤP 1] Đăng cho có mặt trên bảng tin | [CẤP 2] Chia sẻ mẹo vặt ai cũng biết | [CẤP 3 · K4] Giải mã đúng bệnh khiến khách tự tìm",
        "desc": "Ba thanh ngang xếp tầng tăng dần độ sáng từ Cấp 1 (đăng cho có) lên Cấp 3 · K4 (giải mã đúng bệnh khiến khách tự tìm).",
        "h_main_file": "GRPantheonText-Bold.woff2",
        "h_focal_file": "GRPantheonText-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k43">
          <div class="k43-tier lv1">
            <span class="k43-tag mono">CẤP 1</span>
            <span class="k43-txt">Đăng cho có mặt trên bảng tin</span>
          </div>
          <div class="k43-tier lv2">
            <span class="k43-tag mono">CẤP 2</span>
            <span class="k43-txt">Chia sẻ mẹo vặt ai cũng biết</span>
          </div>
          <div class="k43-tier lv3">
            <span class="k43-tag active mono">CẤP 3 · K4</span>
            <span class="k43-txt bright">Giải mã đúng bệnh khiến khách tự tìm</span>
          </div>
        </div>
        """,
    },
    {
        "kid": "K44",
        "kgroup": "KC",
        "kgroup_label": "Họ 3 • Công Thức & Bảng Kiểm",
        "sid": "kb_15_new_k44_phuong_trinh_niem_tin",
        "name": "Phương Trình Nhân Hệ Số Chuyển Đổi ([Độ Sâu] × [Đúng Đau] = [Tự Chốt])",
        "author": "GEMINI",
        "sample_quote": "[01 BÀI SÂU] × [TRÚNG NỖI SỢ] = [KHÁCH TỰ NHẮN] — Một vế bằng 0 thì đăng 100 bài kết quả vẫn bằng 0.",
        "desc": "Biểu diễn quy luật chuyển đổi bằng phương trình phép nhân trực quan: chỉ cần một vế bằng 0 thì đăng 100 bài kết quả vẫn bằng 0.",
        "h_main_file": "GRFlaireExtraBold.woff2",
        "h_focal_file": "GRFlaireExtraBoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k44">
          <div class="k44-eq">
            <span class="k44-term">01 BÀI SÂU</span>
            <span class="k44-op mono">×</span>
            <span class="k44-term">TRÚNG NỖI SỢ</span>
            <span class="k44-op mono">=</span>
            <span class="k44-term active">KHÁCH TỰ NHẮN</span>
          </div>
          <div class="k44-foot">Một vế bằng <b class="mono">0</b> thì đăng <b class="mono">100</b> bài kết quả vẫn bằng <b class="mono gold">0</b>.</div>
        </div>
        """,
    },
    {
        "kid": "K45",
        "kgroup": "KD",
        "kgroup_label": "Họ 4 • Tin Nhắn & Hỏi–Đáp",
        "sid": "kb_15_new_k45_cau_hoi_phan_bien",
        "name": "Thẻ Câu Hỏi Phản Biện Ngược ([NGHỊCH LÝ XÂY KÊNH])",
        "author": "CLAUDE2",
        "sample_quote": "[? NGHỊCH LÝ] Vì sao kênh trăm nghìn xem vẫn vắng khách hỏi mua? | [! LỜI GIẢI] Vì người xem giải trí khác hẳn người sẵn sàng trả tiền.",
        "desc": "Đặt câu hỏi phản biện trực diện vào nghịch lý 'nhiều view nhưng 0 khách', sau đó chốt lời giải đanh thép ở dòng dưới.",
        "h_main_file": "GRCanonMStandardBold.woff2",
        "h_focal_file": "GRCanonMStandardBoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k45">
          <div class="k45-block">
            <div class="k45-tag muted mono">? NGHỊCH LÝ</div>
            <div class="k45-q">Vì sao kênh trăm nghìn xem vẫn vắng khách hỏi mua?</div>
          </div>
          <div class="div-line"></div>
          <div class="k45-block">
            <div class="k45-tag active mono">! LỜI GIẢI</div>
            <div class="k45-a">Vì người xem giải trí khác hẳn người sẵn sàng trả tiền.</div>
          </div>
        </div>
        """,
    },
    {
        "kid": "K46",
        "kgroup": "KD",
        "kgroup_label": "Họ 4 • Tin Nhắn & Hỏi–Đáp",
        "sid": "kb_15_new_k46_chan_doan_truc_tiep",
        "name": "Hộp Thoại Bác Sĩ Kênh ([BỆNH NHÂN KỂ] / [BÁC SĨ KÊ ĐƠN])",
        "author": "GEMINI",
        "sample_quote": "[TÂM SỰ] “Em quay clip mỗi ngày mà khách chỉ xem rồi lướt...” | [KÊ ĐƠN] Dừng quay vội. Viết 01 bài gọi đúng tên nỗi đau nghề.",
        "desc": "Mô phỏng ca khám bệnh kênh thực chiến: hàng trên là lời than thở của chủ kênh, hàng dưới là phác đồ kê đơn dứt khoát.",
        "h_main_file": "FDDomaineText-Bold.woff2",
        "h_focal_file": "FDDomaineText-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k46">
          <div class="k46-row old">
            <span class="k46-badge muted mono">TÂM SỰ</span>
            <span class="k46-txt">“Em quay clip mỗi ngày mà khách chỉ xem rồi lướt...”</span>
          </div>
          <div class="div-line"></div>
          <div class="k46-row new">
            <span class="k46-badge active mono">KÊ ĐƠN</span>
            <span class="k46-txt bright">Dừng quay vội. Viết <b class="gold">01 bài gọi đúng bệnh nghề.</b></span>
          </div>
        </div>
        """,
    },
    {
        "kid": "K47",
        "kgroup": "KD",
        "kgroup_label": "Họ 4 • Tin Nhắn & Hỏi–Đáp",
        "sid": "kb_15_new_k47_bien_ban_tu_van",
        "name": "Biên Bản Tự Vấn Trước Khi Đăng ([CÂU HỎI GÁC CỔNG])",
        "author": "CLAUDE2",
        "sample_quote": "CÂU HỎI GÁC CỔNG TRƯỚC KHI BẤM ĐĂNG: “Bài viết này giải quyết đứt điểm việc gì cho khách?”",
        "desc": "Khung viền trái vàng đậm đóng vai trò trạm gác cổng tư duy trước khi bấm đăng bài: buộc bài viết phải giải quyết đứt điểm 1 việc.",
        "h_main_file": "FDEpiceneText-Bold.woff2",
        "h_focal_file": "FDEpiceneText-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k47">
          <div class="k47-inner">
            <div class="k47-hdr mono">CÂU HỎI GÁC CỔNG TRƯỚC KHI BẤM ĐĂNG:</div>
            <div class="k47-body">“Bài viết này <b class="gold">giải quyết đứt điểm việc gì</b> cho khách?”</div>
          </div>
        </div>
        """,
    },
    {
        "kid": "K48",
        "kgroup": "KD",
        "kgroup_label": "Họ 4 • Tin Nhắn & Hỏi–Đáp",
        "sid": "kb_15_new_k48_tin_nhan_nua_dem",
        "name": "Nhật Ký Tin Nhắn Đến Lúc 23:14 ([23:14 · HỘP THƯ ĐẾN])",
        "author": "GEMINI",
        "sample_quote": "● 23:14 ĐÊM · TIN NHẮN TỪ KHÁCH LẠ: “Anh ơi em đọc đúng 01 bài của anh mà thấy giống hệt mình.”",
        "desc": "Tái hiện khoảnh khắc khách hàng tự nhắn tin lúc 23:14 đêm sau khi đọc trúng 1 bài viết bóc tách đúng tâm lý.",
        "h_main_file": "FDHeldaneText-Bold.woff2",
        "h_focal_file": "FDHeldaneText-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k48">
          <div class="k48-hdr">
            <span class="k48-dot"></span>
            <span class="k48-title mono">23:14 ĐÊM · TIN NHẮN TỪ KHÁCH LẠ</span>
          </div>
          <div class="k48-msg">“Anh ơi đọc đúng <b class="gold">01 bài của anh</b> thấy giống hệt mình.”</div>
        </div>
        """,
    },
    {
        "kid": "K49",
        "kgroup": "KD",
        "kgroup_label": "Họ 4 • Tin Nhắn & Hỏi–Đáp",
        "sid": "kb_15_new_k49_giai_dap_nghi_ngo",
        "name": "Thẻ Hóa Giải Ngại Ngùng Thầm Kín ([KHÁCH NGẠI NÓI] → [BÀI VIẾT GỌI TÊN])",
        "author": "CLAUDE2",
        "sample_quote": "[ĐIỀU KHÁCH NGẠI] Sợ hỏi giá xong không mua bị đánh giá | [BÀI VIẾT MỞ ĐƯỜNG] Phân tích rõ cơ chế để khách yên tâm đặt lịch.",
        "desc": "Chia 2 dòng đối ứng: gọi tên rào cản tâm lý khách ngại nói ra và dùng bài viết mở đường để khách yên tâm đặt lịch.",
        "h_main_file": "GRSectraFine-Bold.woff2",
        "h_focal_file": "GRSectraFine-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k49">
          <div class="k49-row old">
            <span class="k49-lbl muted mono">ĐIỀU KHÁCH NGẠI</span>
            <span class="k49-txt">Sợ hỏi giá xong không mua bị đánh giá</span>
          </div>
          <div class="div-line"></div>
          <div class="k49-row new">
            <span class="k49-lbl active mono">BÀI VIẾT MỞ ĐƯỜNG</span>
            <span class="k49-txt bright">Phân tích rõ cơ chế để khách yên tâm đặt lịch.</span>
          </div>
        </div>
        """,
    },
    {
        "kid": "K50",
        "kgroup": "KE",
        "kgroup_label": "Họ 5 • Tuyên Ngôn & Đúc Kết",
        "sid": "kb_15_new_k50_hien_chuong_k4",
        "name": "Bản Hiến Chương Đúc Kết K4 ([NGUYÊN TẮC SỐ 50 · CHỐT HẠ])",
        "author": "GEMINI",
        "sample_quote": "★ NGUYÊN TẮC SỐ 50 · ĐÚC KẾT K4 ★ Đừng lấy số lượng bài đăng che đậy sự lười suy nghĩ. Hãy đầu tư chất xám vào 01 bài khiến khách nể phục.",
        "desc": "Khung hiến chương khép lại trọn bộ 50 khuôn K4: đóng khung ngôi sao vàng ở đỉnh, tuyên ngôn 2 vế đanh thép bên dưới.",
        "h_main_file": "GRSectraFine-Bold.woff2",
        "h_focal_file": "GRSectraFine-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k50">
          <div class="k50-badge mono">★ NGUYÊN TẮC SỐ 50 · ĐÚC KẾT K4 ★</div>
          <div class="k50-p1">Đừng lấy số lượng bài đăng che đậy sự lười suy nghĩ.</div>
          <div class="k50-p2">Hãy đầu tư chất xám vào 01 bài khiến khách nể phục.</div>
        </div>
        """,
    },
]


def build_html(spec: Dict[str, Any]) -> str:
    focal_style = spec.get("h_focal_style", "italic")
    return f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"><style>
  @font-face {{
    font-family: "HeadMain";
    src: url("file://{FONT_DIR}/{spec['h_main_file']}");
    font-weight: 700;
    font-style: normal;
  }}
  @font-face {{
    font-family: "HeadFocal";
    src: url("file://{FONT_DIR}/{spec['h_focal_file']}");
    font-weight: 700;
    font-style: {focal_style};
  }}
  @font-face {{
    font-family: "SubMed";
    src: url("file://{FONT_DIR}/{spec['sub_med_file']}");
    font-weight: 500;
  }}
  @font-face {{
    font-family: "SubBold";
    src: url("file://{FONT_DIR}/{spec['sub_bold_file']}");
    font-weight: 700;
  }}
  @font-face {{
    font-family: "MetaMono";
    src: url("file://{FONT_DIR}/{spec['mono_file']}");
    font-weight: 700;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
  body {{ width: 1080px; height: 1350px; background: transparent; overflow: hidden; position: relative; }}
  .zone {{
    position: absolute; left: 32px; top: 135px; width: 544px; height: 1090px;
    display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
  }}
  .headline {{
    font-family: "HeadMain", serif;
    font-size: 86px;
    line-height: 1.08;
    letter-spacing: -0.010em;
    color: #FFFFFF;
    margin-bottom: 50px;
    text-shadow: 0 14px 36px rgba(0, 0, 0, 0.72);
  }}
  .headline .line {{
    display: block;
    width: max-content;
    white-space: nowrap;
    font-size: 1em;
  }}
  .headline .hl {{
    font-family: "HeadFocal", serif;
    font-style: {focal_style};
    font-weight: 700;
    font-size: 1em;
    color: #FACC15;
    text-shadow: 0 12px 32px rgba(0, 0, 0, 0.82);
  }}

  .sub-box {{
    width: 544px;
    max-width: 544px;
    background: rgba(5, 9, 18, 0.84);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 16px;
    padding: 18px 18px;
    margin-bottom: 42px;
    box-shadow: 0 22px 48px rgba(0, 0, 0, 0.48);
    font-family: "SubMed", sans-serif;
    color: #F8FAFC;
  }}
  .mono {{
    font-family: "MetaMono", monospace !important;
    letter-spacing: -0.01em;
  }}
  .gold {{ color: #FACC15 !important; }}
  .div-line {{ height: 1px; background: rgba(255, 255, 255, 0.11); width: 100%; margin: 10px 0; }}

  /* K11 Polarity Slider */
  .k11-rail {{ display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-bottom: 11px; }}
  .k11-pole {{ flex: 1; text-align: center; padding: 6px 8px; border-radius: 8px; font-size: 16px; white-space: nowrap; }}
  .k11-pole.old {{ background: rgba(255,255,255,0.05); border: 1px solid rgba(148,163,184,0.25); color: #94A3B8; }}
  .k11-pole.new {{ background: rgba(250,204,21,0.14); border: 1.5px solid #FACC15; color: #FACC15; font-family: "SubBold", sans-serif; }}
  .k11-knob {{ background: #FACC15; color: #070B14; padding: 4px 8px; border-radius: 99px; font-size: 14px; font-weight: 900; flex-shrink: 0; white-space: nowrap; }}
  .k11-foot {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #FFFFFF; text-align: center; padding-top: 9px; border-top: 1px solid rgba(255,255,255,0.12); white-space: nowrap; }}

  /* K41 Compounding 3 Milestones */
  .k41-stages {{ display: flex; align-items: center; justify-content: space-between; gap: 9px; margin-bottom: 11px; }}
  .k41-box {{ background: rgba(255,255,255,0.05); border: 1px solid rgba(148,163,184,0.24); border-radius: 8px; padding: 6px 8px; font-size: 15px; color: #CBD5E1; white-space: nowrap; }}
  .k41-box.active {{ background: rgba(250,204,21,0.14); border: 1.5px solid #FACC15; color: #FACC15; font-family: "SubBold", sans-serif; flex: 1; text-align: center; }}
  .k41-foot {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #FFFFFF; padding-top: 9px; border-top: 1px solid rgba(255,255,255,0.12); text-align: center; white-space: nowrap; }}

  /* K42 2x2 Quadrant Matrix */
  .k42-grid {{ display: grid; grid-template-columns: 1fr 1fr; column-gap: 12px; row-gap: 10px; }}
  .k42-cell {{ background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.14); border-radius: 10px; padding: 10px 12px; font-family: "SubBold", sans-serif; font-size: 19.5px; color: #FFFFFF; white-space: nowrap; }}
  .k42-cell.active {{ background: rgba(250,204,21,0.14); border: 1.5px solid #FACC15; color: #FACC15; }}

  /* K43 3-Level Altitude Scale */
  .box-k43 {{ display: flex; flex-direction: column; gap: 8px; }}
  .k43-tier {{ display: flex; align-items: center; gap: 11px; padding: 7px 11px; border-radius: 9px; }}
  .k43-tier.lv1 {{ background: rgba(255,255,255,0.03); border: 1px solid rgba(148,163,184,0.18); color: #94A3B8; }}
  .k43-tier.lv2 {{ background: rgba(255,255,255,0.06); border: 1px solid rgba(148,163,184,0.28); color: #CBD5E1; }}
  .k43-tier.lv3 {{ background: rgba(250,204,21,0.14); border: 1.5px solid #FACC15; color: #FFFFFF; }}
  .k43-tag {{ font-size: 13px; padding: 3px 8px; border-radius: 5px; background: rgba(148,163,184,0.18); color: #CBD5E1; white-space: nowrap; flex-shrink: 0; }}
  .k43-tag.active {{ background: #FACC15; color: #070B14; font-weight: 800; }}
  .k43-txt {{ font-size: 19.5px; white-space: nowrap; }}
  .k43-txt.bright {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #FFFFFF; }}

  /* K44 Conversion Multiplier Equation */
  .k44-eq {{ display: flex; align-items: center; justify-content: space-between; gap: 9px; margin-bottom: 11px; }}
  .k44-term {{ background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.16); border-radius: 8px; padding: 6px 10px; font-family: "SubBold", sans-serif; font-size: 16.5px; color: #E2E8F0; white-space: nowrap; flex: 1; text-align: center; }}
  .k44-term.active {{ background: rgba(250,204,21,0.15); border: 1.5px solid #FACC15; color: #FACC15; }}
  .k44-op {{ font-size: 18px; color: #FACC15; font-weight: 800; flex-shrink: 0; }}
  .k44-foot {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #FFFFFF; text-align: center; padding-top: 9px; border-top: 1px solid rgba(255,255,255,0.12); white-space: nowrap; }}

  /* K45 Reverse Paradox Card */
  .k45-block {{ display: flex; flex-direction: column; gap: 4px; }}
  .k45-tag {{ align-self: flex-start; font-size: 12.5px; padding: 2px 8px; border-radius: 5px; white-space: nowrap; }}
  .k45-tag.muted {{ background: rgba(148,163,184,0.16); color: #94A3B8; border: 1px solid rgba(148,163,184,0.28); }}
  .k45-tag.active {{ background: #FACC15; color: #070B14; font-weight: 800; }}
  .k45-q {{ font-size: 19.5px; color: #CBD5E1; white-space: nowrap; }}
  .k45-a {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #FACC15; white-space: nowrap; }}

  /* K46 Channel Doctor Prescription */
  .k46-row {{ display: flex; align-items: center; gap: 10px; }}
  .k46-badge {{ font-size: 13px; padding: 3px 8px; border-radius: 5px; white-space: nowrap; flex-shrink: 0; }}
  .k46-badge.muted {{ background: rgba(148,163,184,0.16); color: #94A3B8; border: 1px solid rgba(148,163,184,0.28); }}
  .k46-badge.active {{ background: #FACC15; color: #070B14; font-weight: 800; }}
  .k46-txt {{ font-size: 19.5px; color: #94A3B8; white-space: nowrap; }}
  .k46-txt.bright {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #FFFFFF; }}

  /* K47 Gatekeeper Self-Audit */
  .k47-inner {{ border-left: 4px solid #FACC15; padding-left: 14px; display: flex; flex-direction: column; gap: 7px; }}
  .k47-hdr {{ font-size: 13.5px; color: #FACC15; letter-spacing: 0.04em; white-space: nowrap; }}
  .k47-body {{ font-family: "SubBold", sans-serif; font-size: 20.5px; color: #FFFFFF; line-height: 1.32; white-space: nowrap; }}

  /* K48 23:14 Midnight Inbox Log */
  .k48-hdr {{ display: flex; align-items: center; gap: 10px; margin-bottom: 9px; padding-bottom: 8px; border-bottom: 1px solid rgba(255,255,255,0.11); }}
  .k48-dot {{ width: 9px; height: 9px; border-radius: 50%; background: #22C55E; box-shadow: 0 0 8px #22C55E; flex-shrink: 0; }}
  .k48-title {{ font-size: 13.5px; color: #FACC15; letter-spacing: 0.04em; white-space: nowrap; }}
  .k48-msg {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #FFFFFF; line-height: 1.32; white-space: nowrap; }}

  /* K49 Silent Objection Resolver */
  .k49-row {{ display: flex; flex-direction: column; gap: 4px; }}
  .k49-lbl {{ align-self: flex-start; font-size: 12.5px; padding: 2px 8px; border-radius: 5px; white-space: nowrap; }}
  .k49-lbl.muted {{ background: rgba(148,163,184,0.16); color: #94A3B8; border: 1px solid rgba(148,163,184,0.28); }}
  .k49-lbl.active {{ background: #FACC15; color: #070B14; font-weight: 800; }}
  .k49-txt {{ font-size: 19.5px; color: #CBD5E1; white-space: nowrap; }}
  .k49-txt.bright {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #FACC15; white-space: nowrap; }}

  /* K50 K4 Charter Principle #50 */
  .box-k50 {{ display: flex; flex-direction: column; align-items: center; text-align: center; gap: 7px; }}
  .k50-badge {{ background: rgba(250,204,21,0.15); border: 1.5px solid #FACC15; color: #FACC15; font-size: 13.5px; padding: 4px 14px; border-radius: 99px; letter-spacing: 0.04em; white-space: nowrap; margin-bottom: 2px; }}
  .k50-p1 {{ font-size: 19.5px; color: #CBD5E1; white-space: nowrap; }}
  .k50-p2 {{ font-family: "SubBold", sans-serif; font-size: 20.5px; color: #FACC15; white-space: nowrap; }}

  .meta {{
    font-family: "MetaMono", monospace;
    font-size: 24px;
    color: #E2E8F0;
    letter-spacing: 0.01em;
    display: flex; align-items: center; gap: 12px;
  }}
  .dot {{ width: 11px; height: 11px; border-radius: 50%; background: #F59E0B; }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      <span class="line">Đừng ép mình</span>
      <span class="line">đăng bài <span class="hl">vội vã</span></span>
      <span class="line">mỗi ngày.</span>
    </h1>
    {spec["subbox_html"]}
    <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
  </div>
</body></html>"""


def render_and_audit():
    bg_img = Image.open(BG_PATH).convert("RGBA")
    rendered_by_sid: Dict[str, Any] = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)

        for spec in NEW_SUBBOX_SPECS:
            sid = spec["sid"]
            hfile = PILOT_DIR / f"{sid}.html"
            hfile.write_text(build_html(spec), encoding="utf-8")

            page.goto(f"file://{hfile.resolve()}", wait_until="networkidle")
            page.evaluate("() => document.fonts.ready")
            page.wait_for_timeout(60)

            calc = page.evaluate("""() => {
              const h = document.querySelector('.headline');
              const lines = Array.from(document.querySelectorAll('.headline .line'));
              const hl = document.querySelector('.headline .hl');
              const c = document.createElement('canvas');
              c.width = 700; c.height = 260;
              const ctx = c.getContext('2d');
              const base = 170;

              function measureGlyphRatio(fontSpec, ch, fs) {
                ctx.clearRect(0, 0, 700, 260);
                ctx.font = fontSpec;
                ctx.fillStyle = '#fff';
                ctx.textBaseline = 'alphabetic';
                ctx.fillText(ch, 20, base);
                const d = ctx.getImageData(0, 0, 700, 260).data;
                let minY = 260, maxY = 0;
                for (let y = 0; y < 260; y++) {
                  for (let x = 0; x < 700; x++) {
                    if (d[(y * 700 + x) * 4 + 3] > 25) {
                      if (y < minY) minY = y;
                      if (y > maxY) maxY = y;
                    }
                  }
                }
                return (maxY - minY) / fs;
              }

              const fam = getComputedStyle(h).fontFamily;
              const wt = getComputedStyle(h).fontWeight;
              const xH = +measureGlyphRatio(wt + ' 90px ' + fam, 'x', 90).toFixed(3);
              const capH = +measureGlyphRatio(wt + ' 90px ' + fam, 'H', 90).toFixed(3);

              let hlXH = xH;
              if (hl) {
                const hlSt = getComputedStyle(hl);
                const hlSpec = (hlSt.fontStyle || 'normal') + ' ' + (hlSt.fontWeight || '700') + ' 90px ' + hlSt.fontFamily;
                hlXH = +measureGlyphRatio(hlSpec, 'x', 90).toFixed(3);
              }

              let lsEm = +Math.max(-0.020, Math.min(-0.006, -0.012 - 0.08 * (xH - 0.47))).toFixed(4);
              h.style.letterSpacing = lsEm + 'em';

              let fs = xH >= 0.56 ? 88 : 95;
              h.style.fontSize = fs + 'px';
              while (fs > 74) {
                const maxW = Math.max(...lines.map(el => el.getBoundingClientRect().width));
                if (maxW <= 540) break;
                fs -= 1;
                h.style.fontSize = fs + 'px';
              }

              const fontSpec = wt + ' ' + fs + 'px ' + fam;
              function getInkProfile(str, useLetterSpacing) {
                ctx.clearRect(0, 0, 700, 260);
                ctx.font = fontSpec;
                if (useLetterSpacing && 'letterSpacing' in ctx) ctx.letterSpacing = lsEm + 'em';
                else if ('letterSpacing' in ctx) ctx.letterSpacing = '0px';
                ctx.fillStyle = '#fff';
                ctx.textBaseline = 'alphabetic';
                ctx.fillText(str, 10, base);
                const d = ctx.getImageData(0, 0, 700, 260).data;
                const topCol = new Array(700).fill(999);
                const botCol = new Array(700).fill(-999);
                for (let x = 0; x < 700; x++) {
                  for (let y = 0; y < 260; y++) {
                    if (d[(y * 700 + x) * 4 + 3] > 25) {
                      const relY = y - base;
                      if (relY < topCol[x]) topCol[x] = relY;
                      if (relY > botCol[x]) botCol[x] = relY;
                    }
                  }
                }
                return {topCol, botCol};
              }

              // Match auditor's exact 2D gap profile (dx in [-6, 6], letterSpacing = 0)
              const p1 = getInkProfile('Đừng ép mình', false);
              const p2 = getInkProfile('đăng bài vội vã', false);
              const p3 = getInkProfile('mỗi ngày.', false);

              const gMin = Math.max(8, Math.round(0.095 * fs));
              function minDist2D(pUpper, pLower) {
                let reqD = 0;
                const r = 6;
                for (let x = 0; x < 700; x++) {
                  if (pUpper.botCol[x] === -999) continue;
                  for (let dx = -r; dx <= r; dx++) {
                    const x2 = x + dx;
                    if (x2 >= 0 && x2 < 700 && pLower.topCol[x2] !== 999) {
                      const needed = pUpper.botCol[x] - pLower.topCol[x2] + gMin;
                      if (needed > reqD) reqD = needed;
                    }
                  }
                }
                return reqD;
              }

              const d12_2d = minDist2D(p1, p2);
              const d23_2d = minDist2D(p2, p3);
              const L_2D = +((Math.max(d12_2d, d23_2d)) / fs).toFixed(2);
              const L_rhythm = +Math.max(1.01, Math.min(1.15, 2.22 * xH)).toFixed(2);
              const L_max_tight = +(2.52 * xH).toFixed(2);
              let L_target = +Math.min(L_max_tight, Math.max(L_rhythm, L_2D)).toFixed(2);

              // Ensure min2dGapPx >= 7 and opticalW in [1.10, 1.55]
              function calcAudit2dGap(lhVal) {
                const distPx = lhVal * fs;
                const profs = [p1, p2, p3];
                let worstGap = 999;
                for (let i = 0; i < profs.length - 1; i++) {
                  const pU = profs[i], pL = profs[i + 1];
                  for (let x = 0; x < 700; x++) {
                    if (pU.botCol[x] === -999) continue;
                    for (let dx = -6; dx <= 6; dx++) {
                      const x2 = x + dx;
                      if (x2 >= 0 && x2 < 700 && pL.topCol[x2] !== 999) {
                        const gap = (distPx + pL.topCol[x2]) - pU.botCol[x];
                        if (gap < worstGap) worstGap = gap;
                      }
                    }
                  }
                }
                return Math.round(worstGap);
              }

              while (L_target < 1.26) {
                const gap2d = calcAudit2dGap(L_target);
                const wOpt = +((L_target - xH) / Math.max(0.3, xH)).toFixed(2);
                if (gap2d >= 7 && wOpt >= 1.10) break;
                L_target = +(L_target + 0.01).toFixed(2);
              }

              const W_ratio = +((L_target - xH) / xH).toFixed(2);
              h.style.lineHeight = String(L_target);
              lines.forEach(l => { l.style.lineHeight = String(L_target); });

              // Calibrate vertical boundaries: hBottom <= 716 and sTop >= 736, plus G14 optical vertical balance
              let hRect = h.getBoundingClientRect();
              let sEl = document.querySelector('.sub-box');
              let sRect = sEl.getBoundingClientRect();
              const zone = document.querySelector('.zone');
              if (hRect.bottom > 716) {
                const shiftUp = Math.ceil(hRect.bottom - 713);
                zone.style.top = (135 - shiftUp) + 'px';
                hRect = h.getBoundingClientRect();
                sRect = sEl.getBoundingClientRect();
              }
              if (sRect.top < 736) {
                const extraGap = Math.ceil(738 - sRect.top);
                h.style.marginBottom = (50 + extraGap) + 'px';
              }

              hRect = h.getBoundingClientRect();
              sRect = sEl.getBoundingClientRect();
              const mEl = document.querySelector('.meta');
              let mRect = mEl.getBoundingClientRect();

              return {
                fs, xH, hlXH, capH, lsEm, L_2D, L_rhythm, L_target, W_ratio,
                hTop: Math.round(hRect.top), hBottom: Math.round(hRect.bottom),
                sTop: Math.round(sRect.top), sBottom: Math.round(sRect.bottom),
                mBottom: Math.round(mRect.bottom)
              };
            }""")

            hfile.write_text(page.content(), encoding="utf-8")
            txt_png = PILOT_DIR / f"{sid}_text.png"
            page.screenshot(path=str(txt_png), omit_background=True)
            comp = Image.alpha_composite(bg_img, Image.open(txt_png).convert("RGBA")).convert("RGB")

            jpg_path = PILOT_DIR / f"{sid}.jpg"
            comp.save(jpg_path, quality=93)
            shutil.copy2(jpg_path, BRAIN_DIR / f"{sid}.jpg")

            # 1. Crop Headline only (620x440)
            y_h2 = min(calc["sTop"] - 12, calc["hBottom"] + 46)
            y_h1 = max(0, y_h2 - 440)
            crop_h = comp.crop((16, y_h1, 636, y_h2)).resize((620, 440), Image.Resampling.LANCZOS)
            crop_h_path = PILOT_DIR / f"crop_head_{sid}.jpg"
            crop_h.save(crop_h_path, quality=92)
            shutil.copy2(crop_h_path, BRAIN_DIR / f"crop_head_{sid}.jpg")

            # 2. Crop Subline + Meta (580x315)
            y_s1 = max(0, calc["sTop"] - 26)
            crop_s = comp.crop((20, y_s1, 600, min(1350, y_s1 + 315))).resize((580, 315), Image.Resampling.LANCZOS)
            crop_s_path = PILOT_DIR / f"crop_sub_{sid}.jpg"
            crop_s.save(crop_s_path, quality=92)
            shutil.copy2(crop_s_path, BRAIN_DIR / f"crop_sub_{sid}.jpg")

            rendered_by_sid[sid] = {
                "calc": calc,
                "hfile": str(hfile),
                "jpg_path": str(jpg_path),
            }

        browser.close()

    # Audit outside sync_playwright() context
    for sid, info in rendered_by_sid.items():
        calc = info["calc"]
        hfile = Path(info["hfile"])
        jpg_path = Path(info["jpg_path"])
        audit_res = audit_v3_banner(hfile, jpg_path, expected_lines=3, person_side="right")
        g1 = audit_res["gates"]["G1_font_scale_hierarchy"]
        g2 = audit_res["gates"]["G2_LAW09_per_font_optical_leading"]
        g16 = audit_res["gates"]["G16_LAW11_subbox_textnode_and_sibling_gap"]

        rendered_by_sid[sid] = {
            "calc": calc,
            "score": audit_res["score"],
            "all_pass": audit_res["all_13_pass"],
            "minSubFs": g1["min_subline_fs_px"],
            "gap2D": g2["min_2d_ink_gap_px"],
            "rPad": g16["min_right_pad_px"],
            "lPad": g16["min_left_pad_px"],
            "sibGap": g16["min_sibling_gap_px"],
            "failed": [k for k, v in audit_res["gates"].items() if not v.get("pass")],
            "gates": audit_res["gates"],
        }
        print(
            f"[{sid:35s}] fs={calc['fs']}px xH={calc['xH']} LH={calc['L_target']} W={calc['W_ratio']}x "
            f"gap2D={g2['min_2d_ink_gap_px']}px minSubFs={g1['min_subline_fs_px']}px "
            f"rPad={g16['min_right_pad_px']}px sibGap={g16['min_sibling_gap_px']}px "
            f"hBot={calc['hBottom']} sTop={calc['sTop']} => {audit_res['score']} (PASS={audit_res['all_13_pass']})"
        )
        if not audit_res["all_13_pass"]:
            print("   FAILED:", rendered_by_sid[sid]["failed"])
            for fg in rendered_by_sid[sid]["failed"]:
                print("   ", fg, audit_res["gates"][fg])

    # 1. Build 5x2 composite overview grid: h31_h40_10headlines_grid.jpg (2 cols x 5 rows)
    grid_h = Image.new("RGB", (620 * 2 + 36, 440 * 5 + 72), (7, 11, 20))
    for idx, hspec in enumerate(NEW_HEADLINE_SPECS):
        col = idx % 2
        row = idx // 2
        im = Image.open(PILOT_DIR / f"crop_head_{hspec['sid']}.jpg")
        grid_h.paste(im, (12 + col * (620 + 12), 12 + row * (440 + 12)))
    grid_h.save(PILOT_DIR / "h31_h40_10headlines_grid.jpg", quality=92)
    shutil.copy2(PILOT_DIR / "h31_h40_10headlines_grid.jpg", BRAIN_DIR / "h31_h40_10headlines_grid.jpg")

    # 2. Build 6x2 composite overview grid: k11_k41_k50_11subboxes_grid.jpg (2 cols x 6 rows)
    grid_k = Image.new("RGB", (580 * 2 + 36, 315 * 6 + 84), (7, 11, 20))
    for idx, kspec in enumerate(NEW_SUBBOX_SPECS):
        col = idx % 2
        row = idx // 2
        im = Image.open(PILOT_DIR / f"crop_sub_{kspec['sid']}.jpg")
        grid_k.paste(im, (12 + col * (580 + 12), 12 + row * (315 + 12)))
    grid_k.save(PILOT_DIR / "k11_k41_k50_11subboxes_grid.jpg", quality=92)
    shutil.copy2(PILOT_DIR / "k11_k41_k50_11subboxes_grid.jpg", BRAIN_DIR / "k11_k41_k50_11subboxes_grid.jpg")

    out_report = {
        "rendered_by_sid": rendered_by_sid,
        "new_headlines_h31_h40": NEW_HEADLINE_SPECS,
        "new_subboxes_k11_k41_k50": NEW_SUBBOX_SPECS,
    }
    REPORT_JSON.write_text(json.dumps(out_report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved full audit report to {REPORT_JSON}")


if __name__ == "__main__":
    render_and_audit()
